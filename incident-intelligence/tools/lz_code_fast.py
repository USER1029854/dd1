import json, subprocess, time, sys, os
CHAIN=sys.argv[1]
RPC={"base":os.environ.get("BASE_RPC_URL") or ("https://base-mainnet.g.alchemy.com/v2/"+os.environ["ALCHEMY_API_KEY"]),
     "mainnet":os.environ.get("ETH_RPC_URL") or ("https://eth-mainnet.g.alchemy.com/v2/"+os.environ["ALCHEMY_API_KEY"])}[CHAIN]
src={"base":"sources/lz_screen/oapps_base.json","mainnet":"sources/lz_screen/oapps_mainnet.json"}[CHAIN]
obj=json.load(open(src)); addrs=obj if isinstance(obj,list) else list(obj.keys())
SEL={"approveAndCall":"cae9ca51","paidCall":"bb1e23cb","execute_ab":"1cff79cd",
     "execute_aub":"b61d27f6","functionCall":"a0b5ffb0","transferAndCall":"4000aea0"}
def batch(calls):
    payload=[{"jsonrpc":"2.0","id":i,"method":"eth_getCode","params":[a,"latest"]} for i,a in enumerate(calls)]
    p=subprocess.run(["curl","-sS","-m","40","-X","POST",RPC,"-H","Content-Type: application/json",
        "--data",json.dumps(payload)],capture_output=True,text=True)
    try:
        j=json.loads(p.stdout)
        if isinstance(j,list): return {c['id']:c['result'] for c in j if isinstance(c.get('result'),str)}
    except: pass
    return {}
codes={}; B=25
for pass_no in range(4):
    todo=[a for a in addrs if a not in codes]
    if not todo: break
    for i in range(0,len(todo),B):
        sub=todo[i:i+B]; r=batch(sub)
        for j,a in enumerate(sub):
            if j in r: codes[a]=r[j]
        time.sleep(0.05)
    print(f"pass{pass_no}: covered {len(codes)}/{len(addrs)}",flush=True)
hits=[]; empty=0
for a in addrs:
    c=codes.get(a,"")
    if c in ("","0x"): empty+=1; continue
    f=[n for n,s in SEL.items() if s in c]
    if f: hits.append({"oapp":a,"selectors":f,"codelen":len(c)})
from collections import Counter
res={"chain":CHAIN,"screened":len(addrs),"covered":len(codes),"missing":len(addrs)-len(codes),
     "empty_code":empty,"hits":hits,"by_selector":dict(Counter(s for h in hits for s in h['selectors']))}
json.dump(res,open(f"sources/lz_screen/{CHAIN}_screen_result.json","w"),indent=1)
print(f"DONE [{CHAIN}] covered={len(codes)}/{len(addrs)} empty={empty} HITS={len(hits)} {res['by_selector']}")
