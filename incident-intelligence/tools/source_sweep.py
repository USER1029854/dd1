#!/usr/bin/env python3
"""Read-only deployed-source sweep with on-disk source caching.

Indicators are deliberately narrow. A pattern that matches every OpenZeppelin contract
(bare _msgSender(), _update + _mint, a lone `.call(`) is worthless for discrimination and
would manufacture candidates, so those are either tightened or demoted to role WEAK, which
contributes to ordering but never to a precondition or a score.
Roles: PRE = prerequisite evidence | GUARD = decisive guard | WEAK = ordering only.
"""
import json,sys,os,re,time,collections,hashlib
sys.path.insert(0,'/home/user/dd1/incident-intelligence/tools')
import chain as C
B='/home/user/dd1/incident-intelligence'
CACHE=f'{B}/sources/deployments'; os.makedirs(CACHE,exist_ok=True)

def near(src,a,b,window=300):
    for m in re.finditer(a,src,re.I):
        if re.search(b,src[max(0,m.start()-window):m.end()+window],re.I): return True
    return False
def fnbody(src,namepat):
    """Return the ~1800 chars following each matching function signature."""
    return [src[m.start():m.start()+1800] for m in re.finditer(r'function\s+'+namepat+r'\s*\(',src,re.I)]

VIEW_HELPER=re.compile(r'(lens|reader|viewer|dataprovider|helper|quoter|resolver|multicall|utils?|'
                       r'oracleview|statereader|aggregatorview|periphery.?view)$',re.I)
def is_view_helper(name,src):
    """A read-only helper cannot move value, so a shape found inside one is not a prerequisite."""
    if name and VIEW_HELPER.search(str(name)): return True
    if src:
        movers=len(re.findall(r'\b(transfer|transferFrom|safeTransfer|_mint|_burn|call\{value)',src))
        views=len(re.findall(r'\bview\b|\bpure\b',src))
        if movers==0 and views>20: return True
    return False

def indicators(src):
    I={}
    # ---------------- signature / proof ----------------
    I['ecrecover_used']=bool(re.search(r'\becrecover\s*\(',src))
    I['ecrecover_without_zero_check']= I['ecrecover_used'] and not near(src,r'\becrecover\s*\(',r'!=\s*address\s*\(\s*0\s*\)|==\s*address\s*\(\s*0\s*\)|ECDSA\.|require\s*\(\s*signer')
    I['uses_oz_ecdsa']=bool(re.search(r'ECDSA\.(recover|tryRecover)',src))
    I['erc1271_caller_supplied_signer']=bool(re.search(r'SignatureChecker\.\w+\s*\(\s*(?!address\s*\(\s*this)\w+',src))
    I['encodePacked_multi_dynamic']=bool(re.search(r'abi\.encodePacked\s*\([^;]{0,200}?\b(bytes|string)\b[^;]{0,200}?,[^;]{0,200}?\b(bytes|string)\b',src))
    I['eip712_typehash_present']=bool(re.search(r'TYPEHASH|_hashTypedDataV4',src))
    I['nonce_mapping_present']=bool(re.search(r'nonces?\s*\[|mapping\s*\([^)]*=>\s*uint\d*\s*\)\s*\w*\s*(public|private|internal)?\s*\w*nonces?\b',src,re.I))
    # a signed struct that carries no id/nonce/deadline field
    _th=[m.group(0) for m in re.finditer(r'TYPEHASH\s*=\s*keccak256\s*\([\s\S]{0,600}?\)\s*;',src)]
    I['typehash_without_id_or_nonce']= bool(_th) and not any(
        re.search(r'\b(nonce|deadline|tokenId|positionId|salt|chainId|expiry)\b',t,re.I) for t in _th)
    # ---------------- auth ----------------
    I['owner_compare_without_nonzero']= bool(re.search(r'(msg\.sender|_msgSender\(\))\s*==\s*(owner|_owner|admin|_admin)\b',src)) and \
        not near(src,r'(msg\.sender|_msgSender\(\))\s*==\s*(owner|_owner|admin|_admin)\b',r'!=\s*address\s*\(\s*0')
    I['constant_secret_like']=bool(re.search(r'\b(constant|immutable)\b[^;\n]{0,60}\b(signer|secret|password|privkey|magic|passphrase)\w*\s*=',src,re.I))
    I['hardcoded_signer_address']=bool(re.search(r'address\s+(?:private|internal|public\s+)?(?:constant|immutable)\s+\w*signer\w*\s*=\s*0x[a-fA-F0-9]{40}',src,re.I))
    # ---------------- call / approval surface ----------------
    # require a function that takes BOTH an address and bytes, and calls .call on that very parameter
    _tgt=re.findall(r'function\s+\w+\s*\(([^)]*\baddress\s+(\w+)[^)]*\bbytes\s+(?:calldata|memory)\s+(\w+)[^)]*)\)',src)
    I['arbitrary_target_and_calldata_param']=any(
        re.search(re.escape(t)+r'\s*\.\s*call\s*(\{[^}]*\})?\s*\(\s*'+re.escape(d),src) for _,t,d in _tgt)
    I['delegatecall_on_param']=any(re.search(re.escape(t)+r'\s*\.\s*delegatecall',src) for _,t,_ in _tgt)
    I['transferFrom_param_payer']=bool(re.search(r'transferFrom\s*\(\s*(payer|_payer|from|_from)\s*,',src)) and \
        bool(re.search(r'\b(payer|_payer)\b',src))
    _cbs=fnbody(src,r'\w*(swapCallback|flashCallback|lockAcquired|uniswapV[23]Call|pancakeCall|onFlashLoan|pay)\w*')
    I['callback_without_caller_check']=bool(_cbs) and not any(
        re.search(r'require\s*\(\s*msg\.sender\s*==|if\s*\(\s*msg\.sender\s*!=',b) for b in _cbs)
    I['no_target_allowlist']= I['arbitrary_target_and_calldata_param'] and not bool(
        re.search(r'allowlist|whitelist|isAllowed|approvedTarget|allowedSelector',src,re.I))
    # ---------------- accounting ----------------
    I['balanceOf_this_in_value_path']=bool(re.search(r'balanceOf\s*\(\s*address\s*\(\s*this\s*\)\s*\)',src))
    I['totalAssets_defined']=bool(re.search(r'function\s+totalAssets\s*\(',src))
    I['totalAssets_reads_balanceOf']=any(re.search(r'balanceOf\s*\(\s*address\s*\(\s*this',b) for b in fnbody(src,r'totalAssets'))
    I['getCashPrior_balanceOf']=any(re.search(r'balanceOf\s*\(\s*address\s*\(\s*this',b) for b in fnbody(src,r'getCashPrior'))
    I['internal_cash_counter']=bool(re.search(r'\binternalCash\b|\btotalCash\s*[-+]=',src))
    I['virtual_shares_offset']=bool(re.search(r'_decimalsOffset|virtualShares|VIRTUAL_(SHARES|ASSETS)',src))
    I['dead_shares_minted']=bool(re.search(r'_mint\s*\(\s*address\s*\(\s*(0|0xdead)',src,re.I))
    I['zero_supply_branch']=bool(re.search(r'(totalSupply\s*\(\s*\)|_totalSupply|supply)\s*==\s*0',src))
    I['zero_supply_branch_unguarded']= I['zero_supply_branch'] and not (I['virtual_shares_offset'] or I['dead_shares_minted'])
    I['balance_delta_credit']=bool(re.search(r'(balanceAfter|_after|postBalance)\s*-\s*(balanceBefore|_before|preBalance)',src,re.I))
    I['unchecked_block']=bool(re.search(r'\bunchecked\s*\{',src))
    I['safecast_used']=bool(re.search(r'SafeCast\.',src))
    I['signed_unsigned_cast']=bool(re.search(r'\bint(?:8|16|32|64|128|256)?\s*\(\s*uint|\buint(?:8|16|32|64|128|256)?\s*\(\s*int',src))
    I['unsafe_cross_sign_cast']= I['signed_unsigned_cast'] and not I['safecast_used']
    I['id_array_param']=bool(re.search(r'\b(uint256|uint128|uint64)\[\]\s*(calldata|memory)\s+\w*(ids?|tokenIds?|poolIds?)\b',src,re.I))
    I['id_array_loop_without_dedup']= I['id_array_param'] and bool(re.search(r'for\s*\([^)]*\)\s*\{',src)) and \
        not bool(re.search(r'(seen|claimed|processed|used)\s*\[\s*\w*ids?\[',src,re.I))
    # ---------------- oracle ----------------
    I['latestRoundData_used']=bool(re.search(r'latestRoundData\s*\(',src))
    I['staleness_check']= I['latestRoundData_used'] and near(src,r'latestRoundData',r'updatedAt|answeredInRound|staleness|heartbeat',360)
    I['latestRoundData_without_staleness']= I['latestRoundData_used'] and not I['staleness_check']
    _factory_lookup=r'(getPool|getPair)\s*\(\s*[\w\.\[\]]+\s*,\s*[\w\.\[\]]+\s*(,\s*[\w\.\[\]]+\s*)?\)'
    I['getPool_without_zero_check']=bool(re.search(_factory_lookup,src)) and \
        not near(src,_factory_lookup,r'!=\s*address\s*\(\s*0|==\s*address\s*\(\s*0|require\s*\(')
    I['spot_reserves_read']=bool(re.search(r'getReserves\s*\(|\.slot0\s*\(',src))
    I['twap_present']=bool(re.search(r'\bobserve\s*\(|consult\s*\(|TWAP|twap|secondsAgo',src))
    I['spot_without_twap']= I['spot_reserves_read'] and not I['twap_present']
    I['convertToAssets_as_price']=bool(re.search(r'convertToAssets\s*\(|getPricePerFullShare|pricePerShare',src))
    I['rate_used_as_price']= I['convertToAssets_as_price'] and bool(re.search(r'price|oracle|collateral',src,re.I))
    # ---------------- reentrancy / hooks ----------------
    I['nonreentrant_present']=bool(re.search(r'nonReentrant|ReentrancyGuard',src))
    _hooks=fnbody(src,r'_(update|beforeTokenTransfer|afterTokenTransfer)')
    I['hook_does_value_work']=any(re.search(r'_mint\s*\(|_burn\s*\(|harvest|accrue|distribute|reward',b,re.I) for b in _hooks)
    I['hook_zero_amount_unguarded']= I['hook_does_value_work'] and not any(
        re.search(r'(amount|value)\s*==\s*0|require\s*\(\s*(amount|value)\s*>\s*0',b) for b in _hooks)
    # ---------------- meta-tx / upgrade ----------------
    I['erc2771_forwarder']=bool(re.search(r'trustedForwarder|ERC2771|isTrustedForwarder',src))
    I['erc2771_with_multicall']= I['erc2771_forwarder'] and bool(re.search(r'function\s+multicall\s*\(|Multicall',src))
    I['initializer_modifier_present']=bool(re.search(r'\binitializer\b|\breinitializer\s*\(',src))
    I['initialize_without_modifier']=any(
        not re.search(r'\binitializer\b|\bonlyOwner\b|\breinitializer\b', m.group(0))
        for m in re.finditer(r'function\s+initialize\w*\s*\([^)]*\)\s*[^{;]{0,120}\{',src))
    I['diamondcut_present']=bool(re.search(r'diamondCut',src))
    I['timelock_present']=bool(re.search(r'TimelockController|\btimelock\b|MIN_DELAY',src,re.I))
    # ---------------- claim / peg / caps ----------------
    _claims=[b for b in fnbody(src,r'\w*(claim|harvest)\w*')
             if not re.match(r'function\s+\w*(claimFee|claimOwner|claimAdmin|harvestFee)',b,re.I)
             and not re.search(r'^function\s+\w+\s*\(\s*\w+\.\w+\s+(calldata|memory)',b)]
    I['public_claim_fn']=bool(_claims)
    _ELIG=(r'(claimed|hasClaimed|eligible|allocation|entitle|reward|share|balance|stake|position|request|lock)\w*'
           r'\s*\[\s*(msg\.sender|_msgSender\(\)|account|user|owner)'
           r'|MerkleProof\.|verifyProof'
           r'|ownerOf\s*\(|balanceOf\s*\(\s*(msg\.sender|_msgSender\(\)|account|user)'
           r'|require\s*\([^;]{0,120}msg\.sender'
           r'|onlyOwner|onlyRole|_checkRole|hasRole\s*\(')
    # The MOKE shape is a claim path that never consults ANY caller-specific state.
    I['claim_without_eligibility_map']=bool(_claims) and not any(re.search(_ELIG,b,re.I) for b in _claims)
    I['merkle_proof_gate']=bool(re.search(r'MerkleProof\.|verifyProof',src))
    _redeems=fnbody(src,r'\w*(burn|redeem)\w*')
    I['redeem_hardcoded_peg']=any(
        re.search(r'\b1e18\b|\b1e8\b|10\s*\*\*\s*18',b) and not re.search(r'latestRoundData|getPrice|oracle',b,re.I)
        for b in _redeems) and bool(re.search(r'latestRoundData|getPrice|oracle',src,re.I))
    I['supply_cap_present']=bool(re.search(r'supplyCap|borrowCap|maxDeposit|depositCap',src))
    return I

FAMILY_SIGNALS={
 "SIG-VERIFIER-DEFEATABLE":[("ecrecover_without_zero_check",True,"PRE"),("uses_oz_ecdsa",True,"GUARD")],
 "AUTH-ZERO-ADDRESS-ACCEPTED":[("owner_compare_without_nonzero",True,"PRE")],
 "SECRET-EMBEDDED-IN-PUBLIC-CODE-AS-AUTH":[("constant_secret_like",True,"PRE"),("hardcoded_signer_address",True,"PRE")],
 "CALLDATA-CALLER-CONTROLLED-TARGET":[("arbitrary_target_and_calldata_param",True,"PRE"),
                                      ("no_target_allowlist",True,"PRE"),("delegatecall_on_param",True,"WEAK")],
 "CALLBACK-UNAUTHENTICATED-CALLER-USES-APPROVALS":[("callback_without_caller_check",True,"PRE"),
                                                   ("transferFrom_param_payer",True,"PRE")],
 "CALLBACK-STATE-LOCK-INCOMPLETE":[("nonreentrant_present",False,"PRE"),("nonreentrant_present",True,"GUARD")],
 "ACC-DONATION-UNACCOUNTED-BALANCE":[("getCashPrior_balanceOf",True,"PRE"),("totalAssets_reads_balanceOf",True,"PRE"),
                                     ("internal_cash_counter",True,"GUARD")],
 "ACC-NAV-SHAREPRICE-MANIPULABLE":[("totalAssets_reads_balanceOf",True,"PRE"),("totalAssets_defined",True,"WEAK")],
 "ACC-ZERO-SUPPLY-INFLATION":[("zero_supply_branch_unguarded",True,"PRE"),("virtual_shares_offset",True,"GUARD"),
                              ("dead_shares_minted",True,"GUARD")],
 "ACC-SIGN-OR-BOUND-CHECK-MISSING":[("unsafe_cross_sign_cast",True,"PRE"),("safecast_used",True,"GUARD")],
 "ACC-DUPLICATE-ID-ACCUMULATION":[("id_array_loop_without_dedup",True,"PRE")],
 "ACC-CREDIT-NOT-RECEIVED":[("balance_delta_credit",True,"PRE"),("public_claim_fn",True,"WEAK")],
 "SIG-DIGEST-AMBIGUOUS-OR-UNBOUND":[("encodePacked_multi_dynamic",True,"PRE"),("eip712_typehash_present",True,"WEAK")],
 "SIG-REPLAY-CROSS-POSITION":[("typehash_without_id_or_nonce",True,"PRE"),("nonce_mapping_present",True,"GUARD")],
 "AUTH-IDENTITY-SATISFIABLE-BY-ATTACKER-CONTRACT":[("erc1271_caller_supplied_signer",True,"PRE")],
 "ORACLE-STALE-OR-SILENT-FALLBACK":[("latestRoundData_without_staleness",True,"PRE"),
                                    ("getPool_without_zero_check",True,"PRE"),("staleness_check",True,"GUARD")],
 "ORACLE-SPOT-THIN-LIQUIDITY":[("spot_without_twap",True,"PRE"),("twap_present",True,"GUARD"),
                               ("supply_cap_present",True,"GUARD")],
 "ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE":[("rate_used_as_price",True,"PRE")],
 "HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL":[("hook_zero_amount_unguarded",True,"PRE")],
 "METATX-SENDER-IDENTITY-CONFUSION":[("erc2771_with_multicall",True,"PRE"),("erc2771_forwarder",True,"WEAK")],
 "UPGRADE-INITIALIZER-REACHABLE-LIVE":[("initialize_without_modifier",True,"PRE"),
                                       ("initializer_modifier_present",True,"GUARD")],
 "GOV-CHEAP-CONTROL-NO-TIMELOCK":[("timelock_present",True,"GUARD")],
 "AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY":[("claim_without_eligibility_map",True,"PRE"),("merkle_proof_gate",True,"GUARD")],
 "ACC-HARDCODED-PEG-REDEMPTION":[("redeem_hardcoded_peg",True,"PRE"),("latestRoundData_used",True,"WEAK")],
 "AUTH-MISSING-ON-VALUE-MOVING-PATH":[("owner_compare_without_nonzero",True,"WEAK")],
}

def cache_path(ch,addr): return f"{CACHE}/{ch}_{addr.lower()}.sol.txt"
def get_source(ch,addr):
    p=cache_path(ch,addr)
    if os.path.exists(p):
        t=open(p,encoding='utf-8',errors='replace').read()
        return {"cached":True,"verified":not t.startswith("__UNVERIFIED__"),
                "name":t.split("\n",1)[0].replace("__NAME__:","") if t.startswith("__NAME__:") else None,
                "source":t.split("\n",1)[1] if t.startswith("__NAME__:") else t}
    s=C.source(ch,addr)
    if not s: return None
    if s.get('verified'):
        open(p,'w',encoding='utf-8').write(f"__NAME__:{s.get('ContractName')}\n"+(s.get('source') or ""))
        return {"cached":False,"verified":True,"name":s.get('ContractName'),"source":s.get('source') or ""}
    open(p,'w',encoding='utf-8').write("__UNVERIFIED__")
    return {"cached":False,"verified":False,"name":s.get('ContractName'),"source":""}

def main():
    W=json.load(open(f'{B}/protocols/deep_screen_worklist.json'))
    PR=json.load(open(f'{B}/protocols/onchain_probes.json'))
    BUDGET=int(sys.argv[1]) if len(sys.argv)>1 else 400
    FORCE='--reanalyze' in sys.argv
    order=list(dict.fromkeys(w['protocol_slug'] for w in W))
    todo=[s for s in order if PR.get(s,{}).get('deployment',{}).get('addresses_probed')
          and (FORCE or 'source_sweep' not in PR.get(s,{}))][:BUDGET]
    print(f"source sweep over {len(todo)} protocols (reanalyze={FORCE})",flush=True); t0=time.time()
    for i,slug in enumerate(todo):
        dep=PR[slug]['deployment']; ap=dep['addresses_probed']
        fb=dep.get('chain_probed') or (dep.get('chains_tried') or [None])[0]
        picks=[]; seen=set()
        for a in ap:
            ch=a.get('chain') or fb
            if not ch: continue
            t=a.get('erc1967_implementation') or a.get('implementation_fn') or a['address']
            if t.lower() in seen: continue
            seen.add(t.lower()); picks.append((ch,t,a['address'],bool(a.get('is_proxy'))))
            if len(picks)>=2: break
        res={"contracts":[],"indicators":{},"family_signals":{}}; agg=collections.defaultdict(list)
        for ch,t,orig,isp in picks:
            s=get_source(ch,t)
            if not s: res["contracts"].append({"address":t,"chain":ch,"status":"SOURCE_UNAVAILABLE"}); continue
            if not s['verified']:
                res["contracts"].append({"address":t,"chain":ch,"proxy_of":orig if isp else None,
                                         "status":"IMPLEMENTATION_NOT_VERIFIED","name":s.get('name')}); continue
            ind=indicators(s['source'])
            vh=is_view_helper(s.get('name'),s['source'])
            res["contracts"].append({"address":t,"chain":ch,"proxy_of":orig if isp else None,"status":"VERIFIED",
                "name":s.get('name'),"source_chars":len(s['source']),"view_helper":vh,
                "indicators_true":sorted(k for k,v in ind.items() if v),"from_cache":s['cached']})
            if vh:
                res.setdefault("view_helpers_skipped",[]).append(s.get('name'))
            else:
                for k,v in ind.items(): agg[k].append(v)
            if not s['cached']: time.sleep(0.12)
        if agg:
            res["indicators"]={k:any(v) for k,v in agg.items()}
            for fid,sig in FAMILY_SIGNALS.items():
                hit={ind:{"observed":res["indicators"][ind],"expected":exp,"role":role,
                          "match":res["indicators"][ind]==exp}
                     for ind,exp,role in sig if ind in res["indicators"]}
                if hit: res["family_signals"][fid]=hit
        PR[slug]["source_sweep"]=res
        if i%40==0:
            json.dump(PR,open(f'{B}/protocols/onchain_probes.json','w'))
            print(f"  [{i}/{len(todo)}] {slug} ({time.time()-t0:.0f}s)",flush=True)
    json.dump(PR,open(f'{B}/protocols/onchain_probes.json','w'))
    fam=collections.Counter()
    for v in PR.values():
        for f,sig in (v.get('source_sweep',{}).get('family_signals') or {}).items():
            if any(h['match'] and h['role']=='PRE' for h in sig.values()): fam[f]+=1
    print(json.dumps({"protocols_swept":sum(1 for v in PR.values() if 'source_sweep' in v),
     "contracts_verified":sum(1 for v in PR.values() for c in v.get('source_sweep',{}).get('contracts',[]) if c.get('status')=='VERIFIED'),
     "implementations_unverified":sum(1 for v in PR.values() for c in v.get('source_sweep',{}).get('contracts',[]) if c.get('status')=='IMPLEMENTATION_NOT_VERIFIED'),
     "families_with_PRE_match":dict(fam.most_common())},indent=2))
if __name__=="__main__": main()
