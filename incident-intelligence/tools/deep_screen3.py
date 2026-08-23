#!/usr/bin/env python3
"""Corrected registry-aware probes: right slug->registry mapping, multi-chain attempts."""
import json,sys,re,time,os,collections
sys.path.insert(0,'/home/user/dd1/incident-intelligence/tools')
import chain as C
B='/home/user/dd1/incident-intelligence'
W=json.load(open(f'{B}/protocols/deep_screen_worklist.json'))
REG=json.load(open(f'{B}/protocols/registry_configs.json'))
RM=json.load(open(f'{B}/protocols/registry_slug_map.json'))      # slug -> registry key (correct direction)
PR=json.load(open(f'{B}/protocols/onchain_probes.json'))
E={r['slug']:r for r in json.load(open(f'{B}/protocols/eligibility.json'))}
ALIAS={'binance':'bsc','avax':'avalanche','xdai':'gnosis','bnb':'bsc'}
def chains_for(slug,cfg):
    out=[]
    for c in (E.get(slug,{}).get('_chains') or []):
        c=ALIAS.get(c.lower(),c.lower())
        if c in C.RPC or c in C.CHAINID: out.append(c)
    for c in (cfg.get('chains_in_config') or []):
        c=ALIAS.get(c.lower(),c.lower())
        if (c in C.RPC or c in C.CHAINID) and c not in out: out.append(c)
    return out[:5]

def find_chain(addr,chains):
    for ch in chains:
        cs=C.code_size(ch,addr)
        if cs: return ch,cs
    return None,None

def compound2(slug):
    rk=RM.get(slug); cfg=REG.get(rk,{}) if rk else {}
    comps=(cfg.get('addresses') or {}).get('comptroller') or []
    out={"registry_key":rk,"comptrollers":comps,"registry_flags":cfg.get('flags',[]),
         "markets":[],"markets_by_comptroller":{},"chains_tried":chains_for(slug,cfg)}
    if not comps: out["status"]="NO_COMPTROLLER_IN_REGISTRY"; return out
    probed=0
    for comp in comps[:4]:
        ch,cs=find_chain(comp,out["chains_tried"])
        if not ch: out["markets_by_comptroller"][comp]="NO_CODE_ON_TRIED_CHAINS"; continue
        mk=C.dec_addr_array(C.call(ch,comp,C.SEL["getAllMarkets"]) or "")
        out["markets_by_comptroller"][comp]={"chain":ch,"code_size":cs,"markets":len(mk)}
        for m in mk[:6]:
            out["markets"].append({"chain":ch,"comptroller":comp,"cToken":m,
              "exchangeRateStored":C.dec_uint(C.call(ch,m,C.SEL["exchangeRateStored"])),
              "totalSupply":C.dec_uint(C.call(ch,m,C.SEL["totalSupply"])),
              "getCash":C.dec_uint(C.call(ch,m,C.SEL["getCash"])),
              "totalBorrows":C.dec_uint(C.call(ch,m,C.SEL["totalBorrows"])),
              "supplyCap":C.dec_uint(C.call(ch,comp,C.SEL["supplyCaps"]+C.enc_addr(m)))})
            time.sleep(0.1)
        probed+=1
        time.sleep(0.15)
    if out["markets"]:
        m0=out["markets"][0]; s=C.source(m0["chain"],m0["cToken"])
        if s:
            src=s["source"] or ""
            out["market_source"]={"chain":m0["chain"],"address":m0["cToken"],"name":s["ContractName"],
              "verified":s["verified"],
              "has_getCashPrior_balanceOf":bool(re.search(r'getCashPrior[\s\S]{0,600}?balanceOf\s*\(\s*address\s*\(\s*this',src)),
              "has_balanceOf_this_in_cash_path":bool(re.search(r'balanceOf\s*\(\s*address\s*\(\s*this\s*\)\s*\)',src)),
              "has_internal_cash_counter":bool(re.search(r'\binternalCash\b|\btotalCash\s*[-+]?=',src)),
              "has_exchange_rate_cap":bool(re.search(r'maxExchangeRate|rateCap|exchangeRateDelta|MAX_RATE',src,re.I)),
              "mentions_supply_cap":bool(re.search(r'supplyCap',src)),"source_chars":len(src)}
    out["status"]="PROBED" if out["markets"] else ("COMPTROLLER_UNRESPONSIVE" if probed else "NO_CODE_FOUND")
    return out

def aave2(slug):
    rk=RM.get(slug); cfg=REG.get(rk,{}) if rk else {}
    a=cfg.get('addresses') or {}
    regs=(a.get('registry') or [])+(a.get('addressesProvider') or [])+(a.get('poolAddressesProvider') or [])+(a.get('chain_shorthand') or [])
    out={"registry_key":rk,"addresses_providers":regs[:8],"providers":[],"chains_tried":chains_for(slug,cfg)}
    if not regs: out["status"]="NO_PROVIDER_IN_REGISTRY"; return out
    for r in regs[:5]:
        ch,cs=find_chain(r,out["chains_tried"])
        if not ch: out["providers"].append({"addressesProvider":r,"status":"NO_CODE_ON_TRIED_CHAINS"}); continue
        oracle=C.dec_addr(C.call(ch,r,C.SEL["getPriceOracle"]) or "")
        pool=C.dec_addr(C.call(ch,r,C.SEL["getPool"]) or "") or C.dec_addr(C.call(ch,r,C.SEL["getLendingPool"]) or "")
        own=C.dec_addr(C.call(ch,r,C.SEL["owner"]) or "")
        Z="0x"+"0"*40
        reserves=C.dec_addr_array(C.call(ch,pool,C.SEL["getReservesList"]) or "") if (pool and pool!=Z) else []
        out["providers"].append({"addressesProvider":r,"chain":ch,"code_size":cs,
          "priceOracle":oracle if oracle and oracle!=Z else None,
          "pool":pool if pool and pool!=Z else None,
          "owner":own if own and own!=Z else None,
          "reserve_count":len(reserves),"reserves_sample":reserves[:6],"status":"OK"})
        time.sleep(0.15)
    out["status"]="PROBED" if any(x.get("priceOracle") or x.get("pool") for x in out["providers"]) else "PROVIDER_UNRESPONSIVE"
    return out

def curator2(slug):
    rk=RM.get(slug); cfg=REG.get(rk,{}) if rk else {}
    a=cfg.get('addresses') or {}
    owners=a.get('morphoVaultOwners') or []
    vaults=(a.get('morpho') or [])+(a.get('turtleclub') or [])+(a.get('vaults') or [])
    out={"registry_key":rk,"curator_owner_addresses":owners,"declared_vaults":vaults[:30],
         "declared_vault_count":len(vaults),"vault_reads":[],"chains_tried":chains_for(slug,cfg)}
    if not vaults: out["status"]="NO_VAULTS_IN_REGISTRY"; return out
    for v in vaults[:8]:
        ch,cs=find_chain(v,out["chains_tried"] or ["ethereum"])
        if not ch: continue
        ta=C.dec_uint(C.call(ch,v,C.SEL["totalAssets"])); ts=C.dec_uint(C.call(ch,v,C.SEL["totalSupply"]))
        out["vault_reads"].append({"vault":v,"chain":ch,"code_size":cs,"totalAssets":ta,"totalSupply":ts,
          "asset":C.dec_addr(C.call(ch,v,C.SEL["asset"]) or ""),
          "owner":C.dec_addr(C.call(ch,v,C.SEL["owner"]) or ""),
          "implied_share_price":(ta/ts if (ta and ts) else None)})
        time.sleep(0.12)
    out["status"]="PROBED" if out["vault_reads"] else "VAULTS_UNRESPONSIVE"
    return out

FB=collections.defaultdict(set)
for w in W: FB[w['protocol_slug']].add(w['family_id'])
DON={"ACC-DONATION-UNACCOUNTED-BALANCE","ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE",
     "LIQUIDATION-ON-MANIPULABLE-VALUATION","ACC-ZERO-SUPPLY-INFLATION",
     "ORACLE-STALE-OR-SILENT-FALLBACK","ORACLE-SPOT-THIN-LIQUIDITY"}
NAV={"ACC-NAV-SHAREPRICE-MANIPULABLE","CALLBACK-STATE-LOCK-INCOMPLETE",
     "ACC-REWARD-INDEX-INIT-AND-ORDERING","SETTLEMENT-EPOCH-BOUNDARY-CREDIT"}
targets=[s for s in dict.fromkeys(w['protocol_slug'] for w in W) if s in RM]
print("registry-mapped worklist protocols:",len(targets),flush=True)
for i,slug in enumerate(targets):
    rk=RM[slug]; a=(REG.get(rk,{}).get('addresses') or {}); fams=FB[slug]; e=PR.setdefault(slug,{}); did=[]
    if fams & DON and a.get('comptroller'): e['compound']=compound2(slug); did.append("compound="+e['compound']['status'])
    if fams & DON and (a.get('registry') or a.get('addressesProvider') or a.get('chain_shorthand')):
        e['aave']=aave2(slug); did.append("aave="+e['aave']['status'])
    if fams & NAV and (a.get('morpho') or a.get('turtleclub') or a.get('morphoVaultOwners')):
        e['curator']=curator2(slug); did.append("curator="+e['curator']['status'])
    print(f"[{i+1}/{len(targets)}] {slug} ({rk}): {', '.join(did) or 'no applicable registry probe'}",flush=True)
json.dump(PR,open(f'{B}/protocols/onchain_probes.json','w'),indent=1)
print("done")
