#!/usr/bin/env python3
"""Resolve remaining adapters via the authoritative tvlCodePath (blob -> raw)."""
import json,os,re,subprocess,time,hashlib,collections,sys
sys.path.insert(0,'/home/user/dd1/incident-intelligence/tools')
B='/home/user/dd1/incident-intelligence'; OUT=f'{B}/sources/defillama/adapters'
A=json.load(open(f'{B}/protocols/adapters_index.json'))
E={r['slug']:r for r in json.load(open(f'{B}/protocols/eligibility.json'))}

def analyze(src):
    addrs=sorted(set(re.findall(r'0x[a-fA-F0-9]{40}',src)))
    return {"hardcoded_addresses":addrs[:80],"hardcoded_address_count":len(addrs),
      "uses_factory_or_registry":bool(re.search(r'factory|registry|allPairs|allMarkets|getAllMarkets|poolLength|comptroller',src,re.I)),
      "uses_external_api":bool(re.search(r'https?://(?!raw\.githubusercontent)',src)),
      "external_endpoints":sorted(set(re.findall(r'https?://[^\s\'"`,\)]+',src)))[:12],
      "uses_subgraph":bool(re.search(r'subgraph|graphql|thegraph',src,re.I)),
      "uses_event_logs":bool(re.search(r'getLogs|eventAbi|topic',src,re.I)),
      "mentions_v1_v2_legacy":sorted(set(re.findall(r'\b(v1|v2|v3|v4|legacy|deprecated|old|migrat\w*)\b',src,re.I)))[:12],
      "vault_or_share_terms":sorted(set(re.findall(r'\b(vault|share|totalAssets|pricePerShare|convertToAssets|exchangeRate|nav|ark|silo|strateg\w*|curator)\b',src,re.I)))[:14],
      "lending_terms":sorted(set(re.findall(r'\b(cToken|vToken|aToken|comptroller|unitroller|market\w*|borrow\w*|collateral)\b',src,re.I)))[:14],
      "bridge_terms":sorted(set(re.findall(r'\b(bridge|escrow|lock\w*|mint\w*|wrapped|peer|endpoint)\b',src,re.I)))[:12],
      "chains_referenced":sorted(set(re.findall(r"\b(ethereum|arbitrum|optimism|base|bsc|polygon|avax|avalanche|solana|sui|linea|scroll|blast|mantle|sonic|hyperliquid|berachain)\b",src,re.I)))[:16],
      "looks_stale":bool(re.search(r'//\s*(TODO|FIXME|broken|disabled|deprecated)',src,re.I))}

fixed=0
for slug,v in A.items():
    if v['status']=='READ': continue
    p=(E.get(slug) or {}).get('_tvlCodePath')
    if not p: v['status']='ADAPTER_MISSING_NO_CODEPATH'; continue
    raw=p.replace('https://github.com/','https://raw.githubusercontent.com/').replace('/blob/','/')
    fn=slug+'__'+raw.split('/DefiLlama-Adapters/main/')[-1].replace('/','__')
    dest=f'{OUT}/{fn}'
    r=subprocess.run(["curl","-sSL","-m","30","-o",dest,"-w","%{http_code}",raw],capture_output=True,text=True)
    if (r.stdout or '').strip()[-3:]=='200' and os.path.getsize(dest)>20:
        src=open(dest,encoding='utf-8',errors='replace').read()
        v.update({"status":"READ_VIA_REGISTRY" if '/registries/' in raw else "READ",
                  "module":raw.split('/main/')[-1],"resolved_via":"tvlCodePath",
                  "snapshot":fn,"sha256":hashlib.sha256(src.encode()).hexdigest(),
                  "bytes":len(src),
                  "shared_registry_adapter":'/registries/' in raw,
                  **analyze(src)}); fixed+=1
    else:
        if os.path.exists(dest): os.remove(dest)
        v['status']='ADAPTER_MISSING'; v['tvlCodePath']=p
    time.sleep(0.25)
json.dump(A,open(f'{B}/protocols/adapters_index.json','w'),indent=1)
c=collections.Counter(v['status'] for v in A.values())
print(json.dumps({"resolved_now":fixed,"by_status":c,
 "shared_registry":sum(1 for v in A.values() if v.get('shared_registry_adapter')),
 "dynamic":sum(1 for v in A.values() if v.get('uses_factory_or_registry')),
 "external_api":sum(1 for v in A.values() if v.get('uses_external_api'))},indent=2,default=str))
