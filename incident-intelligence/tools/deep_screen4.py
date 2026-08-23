#!/usr/bin/env python3
"""Batched read-only deep screen over the expanded worklist.
One JSON-RPC batch per (protocol, chain). eth_call / eth_getStorageAt / eth_getCode only."""
import json,sys,os,time,collections,re
sys.path.insert(0,'/home/user/dd1/incident-intelligence/tools')
import chain as C, chain_batch as CB
B='/home/user/dd1/incident-intelligence'
W=json.load(open(f'{B}/protocols/deep_screen_worklist.json'))
AD=json.load(open(f'{B}/protocols/adapters_index.json'))
REG=json.load(open(f'{B}/protocols/registry_configs.json'))
RM=json.load(open(f'{B}/protocols/registry_slug_map.json'))
E={r['slug']:r for r in json.load(open(f'{B}/protocols/eligibility.json'))}
PR=json.load(open(f'{B}/protocols/onchain_probes.json')) if os.path.exists(f'{B}/protocols/onchain_probes.json') else {}
ALIAS={'binance':'bsc','avax':'avalanche','xdai':'gnosis','bnb':'bsc'}
Z40="0x"+"0"*40; Z64="0x"+"0"*64
BUDGET=int(sys.argv[1]) if len(sys.argv)>1 else 650

def chains_for(slug):
    out=[]
    for c in (E.get(slug,{}).get('_chains') or []):
        c=ALIAS.get(c.lower(),c.lower())
        if c in C.RPC and c not in out: out.append(c)     # batchable chains first
    for c in (E.get(slug,{}).get('_chains') or []):
        c=ALIAS.get(c.lower(),c.lower())
        if c in C.CHAINID and c not in out: out.append(c)
    return out[:3]

def addresses_for(slug):
    a=[]
    ad=AD.get(slug,{})
    a+= (ad.get('hardcoded_addresses') or [])[:8]
    rk=RM.get(slug)
    if rk:
        for k,v in (REG.get(rk,{}).get('addresses') or {}).items():
            if isinstance(v,list): a+=v[:4]
    top=E.get(slug,{}).get('address')
    if isinstance(top,str) and top.startswith('0x') and len(top)==42: a.append(top)
    seen=set(); out=[]
    for x in a:
        if isinstance(x,str) and x.lower().startswith('0x') and len(x)==42 and x.lower() not in seen:
            seen.add(x.lower()); out.append(x)
    return out[:8]

def probe(slug):
    addrs=addresses_for(slug); chains=chains_for(slug)
    out={"addresses_considered":len(addrs),"chains_tried":chains,"addresses_probed":[],
         "batched":True}
    if not addrs or not chains: out["status"]="NO_ADDRESSES_OR_CHAIN"; return out
    found={}
    for ch in chains:
        if ch not in C.RPC: continue
        spec=[('code',a) for a in addrs]
        cs=CB.calls(ch,spec)
        live=[(a,s) for a,s in zip(addrs,cs) if isinstance(s,int) and s>0]
        if not live: continue
        spec2=[]
        for a,_ in live:
            spec2 += [('storage',a,C.SLOT_1967_IMPL),('storage',a,C.SLOT_1967_ADMIN),
                      ('storage',a,C.SLOT_1967_BEACON),('storage',a,C.SLOT_OZ5_INIT),
                      ('call',a,C.SEL['owner']),('call',a,C.SEL['paused']),
                      ('call',a,C.SEL['implementation']),('call',a,C.SEL['totalAssets']),
                      ('call',a,C.SEL['getPriceOracle'])]
        r=CB.calls(ch,spec2)
        for i,(a,size) in enumerate(live):
            imp,adm,bea,ozi,own,pau,impfn,ta,orc = r[i*9:(i+1)*9]
            nz=lambda h: isinstance(h,str) and h.startswith('0x') and h!=Z64
            da=lambda h: C.dec_addr(h) if nz(h) else None
            ownr=C.dec_addr(own) if isinstance(own,str) and len(own)>=66 else None
            found[a]={"address":a,"chain":ch,"code_size":size,
              "erc1967_implementation":da(imp),"erc1967_admin":da(adm),"erc1967_beacon":da(bea),
              "oz5_initializable_slot":ozi if nz(ozi) else None,
              "implementation_fn":(C.dec_addr(impfn) if isinstance(impfn,str) and len(impfn)>=66 else None),
              "is_proxy":bool(da(imp) or da(bea) or (isinstance(impfn,str) and len(impfn)>=66 and C.dec_addr(impfn) not in (None,Z40))),
              "owner":ownr if ownr and ownr!=Z40 else None,
              "owner_is_zero":(ownr==Z40) if ownr else None,
              "paused":(bool(C.dec_uint(pau)) if isinstance(pau,str) and len(pau)>=3 and pau!='0x' else None),
              "totalAssets":(C.dec_uint(ta) if isinstance(ta,str) and len(ta)>=3 and ta!='0x' else None),
              "priceOracle":(C.dec_addr(orc) if isinstance(orc,str) and len(orc)>=66 and C.dec_addr(orc)!=Z40 else None)}
        if found: break
    out["addresses_probed"]=list(found.values())
    out["status"]="PROBED" if found else "NO_LIVE_CODE_AT_KNOWN_ADDRESSES"
    return out

order=list(dict.fromkeys(w['protocol_slug'] for w in W))[:BUDGET]
todo=[s for s in order if (PR.get(s,{}).get('deployment',{}).get('status') not in ('PROBED',))]
print(f"worklist {len(order)} | already probed {len(order)-len(todo)} | to probe {len(todo)}",flush=True)
t0=time.time()
for i,slug in enumerate(todo):
    try: PR.setdefault(slug,{})["deployment"]=probe(slug)
    except Exception as ex: PR.setdefault(slug,{})["deployment"]={"status":"ERROR","error":str(ex)[:160]}
    if i%40==0:
        json.dump(PR,open(f'{B}/protocols/onchain_probes.json','w'))
        el=time.time()-t0
        print(f"  [{i}/{len(todo)}] {slug} -> {PR[slug]['deployment']['status']} ({el:.0f}s, {el/max(i,1):.2f}s/protocol)",flush=True)
json.dump(PR,open(f'{B}/protocols/onchain_probes.json','w'))
c=collections.Counter(v.get('deployment',{}).get('status') for v in PR.values())
print(json.dumps({"protocols_in_probe_index":len(PR),"by_status":dict(c),
 "addresses_probed_total":sum(len(v.get('deployment',{}).get('addresses_probed',[])) for v in PR.values()),
 "proxies_found":sum(1 for v in PR.values() for a in v.get('deployment',{}).get('addresses_probed',[]) if a.get('is_proxy')),
 "zero_owner_with_code":sum(1 for v in PR.values() for a in v.get('deployment',{}).get('addresses_probed',[]) if a.get('owner_is_zero')),
 "paused_true":sum(1 for v in PR.values() for a in v.get('deployment',{}).get('addresses_probed',[]) if a.get('paused'))},indent=2))
