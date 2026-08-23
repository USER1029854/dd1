#!/usr/bin/env python3
"""Phase F.3 (L1): fetch each candidate's official DefiLlama adapter module and
extract architecture evidence (addresses, factories, dynamic sources, staleness)."""
import json,os,re,subprocess,time,hashlib,collections
B='/home/user/dd1/incident-intelligence'; OUT=f'{B}/sources/defillama/adapters'
os.makedirs(OUT,exist_ok=True)
W=json.load(open(f'{B}/protocols/deep_screen_worklist.json'))
prot={}
for w in W: prot.setdefault(w['protocol_slug'],w)
RAW="https://raw.githubusercontent.com/DefiLlama/DefiLlama-Adapters/main/projects/"

def get(url,dest):
    r=subprocess.run(["curl","-sSL","-m","30","-o",dest,"-w","%{http_code}",url],
                     capture_output=True,text=True)
    return (r.stdout or "").strip()[-3:]

res={}
for slug,w in prot.items():
    mod=w.get('module') or ''
    if not mod: res[slug]={"status":"NO_MODULE_FIELD"}; continue
    cands=[mod]
    if not mod.endswith('.js'): cands=[mod+'/index.js', mod+'.js']
    got=None
    for c in cands:
        dest=f"{OUT}/{slug}__{c.replace('/','__')}"
        code=get(RAW+c,dest)
        if code=="200" and os.path.getsize(dest)>20: got=(c,dest); break
        if os.path.exists(dest): os.remove(dest)
    if not got:
        res[slug]={"status":"ADAPTER_MISSING","module":mod,
                   "tried":cands,"note":"module path did not resolve in DefiLlama-Adapters main"}
        continue
    c,dest=got; src=open(dest,encoding='utf-8',errors='replace').read()
    addrs=sorted(set(re.findall(r'0x[a-fA-F0-9]{40}', src)))
    res[slug]={"status":"READ","module":c,"snapshot":os.path.basename(dest),
      "sha256":hashlib.sha256(src.encode()).hexdigest(),"bytes":len(src),
      "hardcoded_addresses":addrs[:80],"hardcoded_address_count":len(addrs),
      "uses_factory_or_registry":bool(re.search(r'factory|registry|allPairs|allMarkets|getAllMarkets|createdPools|poolLength',src,re.I)),
      "uses_external_api":bool(re.search(r'https?://(?!raw\.githubusercontent)',src)),
      "external_endpoints":sorted(set(re.findall(r'https?://[^\s\'"`,\)]+',src)))[:12],
      "uses_subgraph":bool(re.search(r'subgraph|graphql|thegraph',src,re.I)),
      "uses_event_logs":bool(re.search(r'getLogs|eventAbi|topic',src,re.I)),
      "mentions_v1_v2_legacy":sorted(set(re.findall(r'\b(v1|v2|v3|v4|legacy|deprecated|old|migrat\w*)\b',src,re.I)))[:12],
      "vault_or_share_terms":sorted(set(re.findall(r'\b(vault|share|totalAssets|pricePerShare|convertToAssets|exchangeRate|nav|ark|silo|strateg\w*)\b',src,re.I)))[:12],
      "lending_terms":sorted(set(re.findall(r'\b(cToken|vToken|aToken|comptroller|unitroller|market\w*|borrow\w*|collateral)\b',src,re.I)))[:12],
      "bridge_terms":sorted(set(re.findall(r'\b(bridge|escrow|lock\w*|mint\w*|wrapped|peer|endpoint)\b',src,re.I)))[:12],
      "chains_referenced":sorted(set(re.findall(r"\b(ethereum|arbitrum|optimism|base|bsc|polygon|avax|avalanche|solana|sui|linea|scroll|blast|mantle|sonic|hyperliquid|berachain)\b",src,re.I)))[:16],
      "looks_stale":bool(re.search(r'//\s*(TODO|FIXME|broken|disabled|deprecated)',src,re.I)) or len(src)<200,
      }
    time.sleep(0.25)
json.dump(res,open(f'{B}/protocols/adapters_index.json','w'),indent=1)
c=collections.Counter(v['status'] for v in res.values())
print(json.dumps({"protocols":len(prot),"by_status":c,
 "with_hardcoded_addresses":sum(1 for v in res.values() if v.get('hardcoded_address_count')),
 "dynamic_factory_or_registry":sum(1 for v in res.values() if v.get('uses_factory_or_registry')),
 "external_api_dependent":sum(1 for v in res.values() if v.get('uses_external_api')),
 "subgraph_dependent":sum(1 for v in res.values() if v.get('uses_subgraph')),
 "flagged_stale":sum(1 for v in res.values() if v.get('looks_stale'))},indent=2,default=str))
