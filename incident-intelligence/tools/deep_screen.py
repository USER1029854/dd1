#!/usr/bin/env python3
"""Phase H.3: read-only deep screen. For each protocol-family pair, evaluate each
mandatory precondition and each decisive guard as PRESENT / ABSENT / UNKNOWN / NOT_APPLICABLE."""
import json,sys,re,time,collections
sys.path.insert(0,'/home/user/dd1/incident-intelligence/tools')
import chain as C
B='/home/user/dd1/incident-intelligence'
W=json.load(open(f'{B}/protocols/deep_screen_worklist.json'))
AD=json.load(open(f'{B}/protocols/adapters_index.json'))
REG=json.load(open(f'{B}/protocols/registry_configs.json'))
RMAP=json.load(open(f'{B}/protocols/registry_slug_map.json'))
E={r['slug']:r for r in json.load(open(f'{B}/protocols/eligibility.json'))}
slug2reg={}
for rk,sl in RMAP.items():
    if sl: slug2reg.setdefault(sl,rk)
for rk in REG:                      # also try direct name match
    slug2reg.setdefault(rk,rk)

CHAIN_ALIAS={"binance":"bsc","avax":"avalanche","xdai":"gnosis"}
def pick_chain(p):
    for c in (p.get('chains') or []):
        c=c.lower()
        if c in C.RPC or c in C.CHAINID: return c
    return None

def compound_probe(slug,p):
    """Read comptroller -> markets -> rate/supply/cash. Read implementation source."""
    rk=slug2reg.get(slug); cfg=REG.get(rk,{}) if rk else {}
    comps=(cfg.get('addresses') or {}).get('comptroller') or []
    out={"comptrollers":comps,"registry_key":rk,"registry_flags":cfg.get('flags',[]),"markets":[]}
    ch=pick_chain(p)
    if not comps or not ch: out["status"]="NO_COMPTROLLER_OR_CHAIN"; return out
    out["chain_probed"]=ch
    for comp in comps[:2]:
        r=C.call(ch,comp,C.SEL["getAllMarkets"]); mk=C.dec_addr_array(r)
        out.setdefault("markets_by_comptroller",{})[comp]=len(mk)
        for m in mk[:8]:
            rate=C.dec_uint(C.call(ch,m,C.SEL["exchangeRateStored"]))
            ts  =C.dec_uint(C.call(ch,m,C.SEL["totalSupply"]))
            cash=C.dec_uint(C.call(ch,m,C.SEL["getCash"]))
            bor =C.dec_uint(C.call(ch,m,C.SEL["totalBorrows"]))
            cap =C.dec_uint(C.call(ch,comp,C.SEL["supplyCaps"]+C.enc_addr(m)))
            out["markets"].append({"cToken":m,"exchangeRateStored":rate,"totalSupply":ts,
                                   "getCash":cash,"totalBorrows":bor,"supplyCap":cap})
            time.sleep(0.12)
        time.sleep(0.2)
    # implementation source of the first market
    if out["markets"]:
        s=C.source(ch,out["markets"][0]["cToken"])
        if s:
            src=s["source"] or ""
            out["market_source"]={"name":s["ContractName"],"verified":s["verified"],
              "has_getCashPrior_balanceOf":bool(re.search(r'getCashPrior[\s\S]{0,400}?balanceOf\s*\(\s*address\s*\(\s*this',src)),
              "has_internal_cash_counter":bool(re.search(r'\binternalCash\b|\btotalCash\b\s*[-+]?=',src)),
              "has_exchange_rate_cap":bool(re.search(r'maxExchangeRate|rateCap|exchangeRateDelta|MAX_RATE',src,re.I)),
              "mentions_supply_cap":bool(re.search(r'supplyCap',src)),
              "source_chars":len(src)}
    out["status"]="PROBED"
    return out

def curator_probe(slug,p):
    rk=slug2reg.get(slug); cfg=REG.get(rk,{}) if rk else {}
    addrs=cfg.get('addresses') or {}
    owners=addrs.get('morphoVaultOwners') or []
    vaults=(addrs.get('morpho') or [])+(addrs.get('turtleclub') or [])+(addrs.get('vaults') or [])
    out={"registry_key":rk,"curator_owner_addresses":owners,"declared_vaults":vaults[:20],
         "declared_vault_count":len(vaults),"vault_reads":[]}
    ch=pick_chain(p) or "ethereum"
    out["chain_probed"]=ch
    for v in vaults[:6]:
        ta=C.dec_uint(C.call(ch,v,C.SEL["totalAssets"]))
        ts=C.dec_uint(C.call(ch,v,C.SEL["totalSupply"]))
        asset=C.dec_addr(C.call(ch,v,C.SEL["asset"]) or "")
        cs=C.code_size(ch,v)
        out["vault_reads"].append({"vault":v,"totalAssets":ta,"totalSupply":ts,
                                   "asset":asset,"code_size":cs,
                                   "implied_share_price":(ta/ts if (ta and ts) else None)})
        time.sleep(0.12)
    out["status"]="PROBED" if out["vault_reads"] else "NO_VAULTS_IN_REGISTRY"
    return out

def deployment_probe(slug,p):
    """Legacy/upgrade probes: adapter addresses -> code, balance, owner, proxy slots."""
    a=AD.get(slug,{})
    addrs=a.get("hardcoded_addresses") or []
    ch=pick_chain(p)
    out={"chain_probed":ch,"addresses_probed":[],"adapter_status":a.get("status")}
    if not ch or not addrs: out["status"]="NO_ADDRESSES_OR_CHAIN"; return out
    for ad in addrs[:6]:
        cs=C.code_size(ch,ad)
        if not cs: continue
        impl=C.storage(ch,ad,C.SLOT_1967_IMPL)
        adm =C.storage(ch,ad,C.SLOT_1967_ADMIN)
        bea =C.storage(ch,ad,C.SLOT_1967_BEACON)
        ozi =C.storage(ch,ad,C.SLOT_OZ5_INIT)
        own =C.dec_addr(C.call(ch,ad,C.SEL["owner"]) or "")
        pau =C.dec_uint(C.call(ch,ad,C.SEL["paused"]) or "")
        nz=lambda h: bool(h) and h!="0x"+"0"*64
        out["addresses_probed"].append({"address":ad,"code_size":cs,
          "erc1967_implementation":C.dec_addr(impl) if nz(impl) else None,
          "erc1967_admin":C.dec_addr(adm) if nz(adm) else None,
          "erc1967_beacon":C.dec_addr(bea) if nz(bea) else None,
          "oz5_initializable_slot":ozi if nz(ozi) else None,
          "is_proxy":nz(impl) or nz(bea),
          "owner":own if own and own!="0x"+"0"*40 else None,
          "owner_is_zero":own=="0x"+"0"*40 if own else None,
          "paused":bool(pau) if pau is not None else None})
        time.sleep(0.15)
    out["status"]="PROBED" if out["addresses_probed"] else "NO_LIVE_CODE_AT_ADAPTER_ADDRESSES"
    return out

DONATION_FAMS={"ACC-DONATION-UNACCOUNTED-BALANCE","ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE",
               "LIQUIDATION-ON-MANIPULABLE-VALUATION","ACC-ZERO-SUPPLY-INFLATION",
               "ORACLE-STALE-OR-SILENT-FALLBACK","ORACLE-SPOT-THIN-LIQUIDITY"}
NAV_FAMS={"ACC-NAV-SHAREPRICE-MANIPULABLE","CALLBACK-STATE-LOCK-INCOMPLETE",
          "ACC-REWARD-INDEX-INIT-AND-ORDERING","SETTLEMENT-EPOCH-BOUNDARY-CREDIT"}

LIMIT=int(sys.argv[1]) if len(sys.argv)>1 else 60
prot_order=[]
for w in W:
    if w['protocol_slug'] not in prot_order: prot_order.append(w['protocol_slug'])
targets=prot_order[:LIMIT]
probes={}
for i,slug in enumerate(targets):
    p=next(w for w in W if w['protocol_slug']==slug)
    fams={w['family_id'] for w in W if w['protocol_slug']==slug}
    e={}
    try:
        if fams & DONATION_FAMS and slug2reg.get(slug) in REG: e["compound"]=compound_probe(slug,p)
        if fams & NAV_FAMS and slug2reg.get(slug) in REG:      e["curator"]=curator_probe(slug,p)
        e["deployment"]=deployment_probe(slug,p)
    except Exception as ex:
        e["error"]=str(ex)[:200]
    probes[slug]=e
    print(f"[{i+1}/{len(targets)}] {slug}: "+", ".join(f"{k}={v.get('status')}" for k,v in e.items() if isinstance(v,dict)),flush=True)
json.dump(probes,open(f'{B}/protocols/onchain_probes.json','w'),indent=1)
print("done",len(probes))
