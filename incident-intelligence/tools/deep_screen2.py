#!/usr/bin/env python3
"""Extend the read-only deep screen: registry-aware probes for every worklist protocol."""
import json,sys,re,time,collections,os
sys.path.insert(0,'/home/user/dd1/incident-intelligence/tools')
import chain as C
from deep_screen import compound_probe, curator_probe, deployment_probe, pick_chain   # reuse
B='/home/user/dd1/incident-intelligence'
W=json.load(open(f'{B}/protocols/deep_screen_worklist.json'))
REG=json.load(open(f'{B}/protocols/registry_configs.json'))
RM=json.load(open(f'{B}/protocols/registry_slug_map.json'))
DM=json.load(open(f'{B}/protocols/dead_adapter_slug_map.json'))
DEAD=json.load(open(f'{B}/protocols/dead_adapters.json'))
PR=json.load(open(f'{B}/protocols/onchain_probes.json')) if os.path.exists(f'{B}/protocols/onchain_probes.json') else {}

def aave_probe(slug,p):
    rk=RM.get(slug); cfg=REG.get(rk,{}) if rk else {}
    a=cfg.get('addresses') or {}
    regs=(a.get('registry') or [])+(a.get('addressesProvider') or [])+(a.get('poolAddressesProvider') or [])+(a.get('chain_shorthand') or [])
    out={"registry_key":rk,"addresses_providers":regs[:6],"providers":[]}
    ch=pick_chain(p)
    if not regs or not ch: out["status"]="NO_PROVIDER_OR_CHAIN"; return out
    out["chain_probed"]=ch
    for r in regs[:4]:
        oracle=C.dec_addr(C.call(ch,r,C.SEL["getPriceOracle"]) or "")
        pool  =C.dec_addr(C.call(ch,r,C.SEL["getPool"]) or "") or C.dec_addr(C.call(ch,r,C.SEL["getLendingPool"]) or "")
        own   =C.dec_addr(C.call(ch,r,C.SEL["owner"]) or "")
        reserves=[]
        if pool and pool!="0x"+"0"*40:
            reserves=C.dec_addr_array(C.call(ch,pool,C.SEL["getReservesList"]) or "")
        out["providers"].append({"addressesProvider":r,
          "priceOracle":oracle if oracle and oracle!="0x"+"0"*40 else None,
          "pool":pool if pool and pool!="0x"+"0"*40 else None,
          "owner":own if own and own!="0x"+"0"*40 else None,
          "reserve_count":len(reserves),"reserves_sample":reserves[:6],
          "code_size_provider":C.code_size(ch,r)})
        time.sleep(0.15)
    out["status"]="PROBED" if any(x.get("priceOracle") or x.get("pool") for x in out["providers"]) else "PROVIDER_UNRESPONSIVE"
    return out

FAMS_BY_SLUG=collections.defaultdict(set)
for w in W: FAMS_BY_SLUG[w['protocol_slug']].add(w['family_id'])
DON={"ACC-DONATION-UNACCOUNTED-BALANCE","ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE",
     "LIQUIDATION-ON-MANIPULABLE-VALUATION","ACC-ZERO-SUPPLY-INFLATION",
     "ORACLE-STALE-OR-SILENT-FALLBACK","ORACLE-SPOT-THIN-LIQUIDITY"}
NAV={"ACC-NAV-SHAREPRICE-MANIPULABLE","CALLBACK-STATE-LOCK-INCOMPLETE",
     "ACC-REWARD-INDEX-INIT-AND-ORDERING","SETTLEMENT-EPOCH-BOUNDARY-CREDIT"}

order=list(dict.fromkeys(w['protocol_slug'] for w in W))
for i,slug in enumerate(order):
    p=next(w for w in W if w['protocol_slug']==slug)
    e=PR.setdefault(slug,{}); fams=FAMS_BY_SLUG[slug]; rk=RM.get(slug); cfg=REG.get(rk,{}) if rk else {}
    a=cfg.get('addresses') or {}
    did=[]
    try:
        if slug in DM:
            e["dead_adapter"]={"key":DM[slug],"deadFrom":DEAD[DM[slug]].get("deadFrom"),
                               "hallmarks":DEAD[DM[slug]].get("hallmarks"),
                               "source":"DefiLlama registries/deadAdapters.json"}
            did.append("dead")
        if fams & DON and a.get('comptroller') and e.get('compound',{}).get('status')!='PROBED':
            e["compound"]=compound_probe(slug,p); did.append("compound="+e["compound"]["status"])
        if fams & DON and (a.get('registry') or a.get('addressesProvider') or a.get('chain_shorthand')) \
           and e.get('aave',{}).get('status')!='PROBED':
            e["aave"]=aave_probe(slug,p); did.append("aave="+e["aave"]["status"])
        if fams & NAV and (a.get('morpho') or a.get('turtleclub') or a.get('morphoVaultOwners')) \
           and e.get('curator',{}).get('status')!='PROBED':
            e["curator"]=curator_probe(slug,p); did.append("curator="+e["curator"]["status"])
        if 'deployment' not in e:
            e["deployment"]=deployment_probe(slug,p); did.append("deployment="+e["deployment"]["status"])
    except Exception as ex:
        e["error"]=str(ex)[:200]; did.append("ERR")
    print(f"[{i+1}/{len(order)}] {slug}: {', '.join(did) or 'already covered'}",flush=True)
json.dump(PR,open(f'{B}/protocols/onchain_probes.json','w'),indent=1)
print("done",len(PR))
