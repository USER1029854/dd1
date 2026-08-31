#!/usr/bin/env python3
"""Fetch adapters for the expanded worklist (module path, then authoritative tvlCodePath)."""
import json,os,re,subprocess,time,hashlib,collections
B='/home/user/dd1/incident-intelligence'; OUT=f'{B}/sources/defillama/adapters'
os.makedirs(OUT,exist_ok=True)
W=json.load(open(f'{B}/protocols/deep_screen_worklist.json'))
E={r['slug']:r for r in json.load(open(f'{B}/protocols/eligibility.json'))}
A=json.load(open(f'{B}/protocols/adapters_index.json')) if os.path.exists(f'{B}/protocols/adapters_index.json') else {}
RAW="https://raw.githubusercontent.com/DefiLlama/DefiLlama-Adapters/main/projects/"
slugs=list(dict.fromkeys(w['protocol_slug'] for w in W))
def analyze(src):
    a=sorted(set(re.findall(r'0x[a-fA-F0-9]{40}',src)))
    return {"hardcoded_addresses":a[:60],"hardcoded_address_count":len(a),
     "uses_factory_or_registry":bool(re.search(r'factory|registry|allPairs|allMarkets|getAllMarkets|poolLength|comptroller',src,re.I)),
     "uses_external_api":bool(re.search(r'https?://(?!raw\.githubusercontent)',src)),
     "external_endpoints":sorted(set(re.findall(r'https?://[^\s\'"`,\)]+',src)))[:8],
     "uses_subgraph":bool(re.search(r'subgraph|graphql|thegraph',src,re.I)),
     "uses_event_logs":bool(re.search(r'getLogs|eventAbi|topic',src,re.I)),
     "mentions_v1_v2_legacy":sorted(set(re.findall(r'\b(v1|v2|v3|v4|legacy|deprecated|old|migrat\w*)\b',src,re.I)))[:10],
     "vault_or_share_terms":sorted(set(re.findall(r'\b(vault|share|totalAssets|pricePerShare|convertToAssets|exchangeRate|nav|ark|silo|strateg\w*|curator|hook)\b',src,re.I)))[:12],
     "lending_terms":sorted(set(re.findall(r'\b(cToken|vToken|aToken|comptroller|unitroller|market\w*|borrow\w*|collateral|addressesProvider)\b',src,re.I)))[:12],
     "bridge_terms":sorted(set(re.findall(r'\b(bridge|escrow|lock\w*|mint\w*|wrapped|peer|endpoint)\b',src,re.I)))[:10],
     "looks_stale":bool(re.search(r'//\s*(TODO|FIXME|broken|disabled|deprecated)',src,re.I))}
def get(url,dest):
    r=subprocess.run(["curl","-sSL","-m","25","-o",dest,"-w","%{http_code}",url],capture_output=True,text=True)
    return (r.stdout or "").strip()[-3:]
new=0
for i,slug in enumerate(slugs):
    if A.get(slug,{}).get('status','').startswith('READ'): continue
    r=E.get(slug,{}); mod=r.get('_module') or ''
    cands=[mod] if mod.endswith('.js') else [mod+'/index.js',mod+'.js']
    got=None
    for c in cands:
        d=f"{OUT}/{slug}__{c.replace('/','__')}"
        if get(RAW+c,d)=="200" and os.path.getsize(d)>20: got=(c,d,False); break
        if os.path.exists(d): os.remove(d)
    if not got and r.get('_tvlCodePath'):
        raw=r['_tvlCodePath'].replace('https://github.com/','https://raw.githubusercontent.com/').replace('/blob/','/')
        fn=slug+'__'+raw.split('/main/')[-1].replace('/','__'); d=f"{OUT}/{fn}"
        if get(raw,d)=="200" and os.path.getsize(d)>20: got=(raw.split('/main/')[-1],d,'/registries/' in raw)
        elif os.path.exists(d): os.remove(d)
    if got:
        c,d,reg=got; src=open(d,encoding='utf-8',errors='replace').read()
        A[slug]={"status":"READ_VIA_REGISTRY" if reg else "READ","module":c,
                 "snapshot":os.path.basename(d),"sha256":hashlib.sha256(src.encode()).hexdigest(),
                 "bytes":len(src),"shared_registry_adapter":bool(reg),**analyze(src)}; new+=1
    else:
        A[slug]={"status":"ADAPTER_MISSING","module":mod,"tvlCodePath":r.get('_tvlCodePath')}
    if i%75==0: print(f"  [{i}/{len(slugs)}] new={new}",flush=True); json.dump(A,open(f'{B}/protocols/adapters_index.json','w'))
    time.sleep(0.12)
json.dump(A,open(f'{B}/protocols/adapters_index.json','w'))
c=collections.Counter(v['status'] for v in A.values())
print(json.dumps({"worklist_protocols":len(slugs),"newly_fetched":new,"index_size":len(A),
 "by_status":dict(c),
 "worklist_read":sum(1 for s in slugs if A.get(s,{}).get('status','').startswith('READ')),
 "worklist_missing":sum(1 for s in slugs if not A.get(s,{}).get('status','').startswith('READ'))},indent=2))
