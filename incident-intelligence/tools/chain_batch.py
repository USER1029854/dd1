# -*- coding: utf-8 -*-
"""Batched read-only JSON-RPC. One HTTP request carries many eth_call /
eth_getStorageAt / eth_getCode reads. Nothing here can write state."""
import json,subprocess,sys
sys.path.insert(0,'/home/user/dd1/incident-intelligence/tools')
import chain as C

def batch(chain, reqs, timeout=60):
    """reqs: list of (method, params). Returns list of results (None on error)."""
    chain=chain.lower()
    if not reqs: return []
    url=C.RPC.get(chain)
    if not url:                                   # explorer proxy has no batch: fall back
        out=[]
        for m,p in reqs:
            if m=="eth_call":       out.append(C.call(chain,p[0]["to"],p[0]["data"]))
            elif m=="eth_getStorageAt": out.append(C.storage(chain,p[0],p[1]))
            elif m=="eth_getCode":  out.append(C.code_size(chain,p[0]))
            else: out.append(None)
        return out
    payload=[{"jsonrpc":"2.0","id":i,"method":m,"params":p} for i,(m,p) in enumerate(reqs)]
    r=subprocess.run(["curl","-sS","-m",str(timeout),"-X","POST",
                      "-H","content-type: application/json","--data",json.dumps(payload),url],
                     capture_output=True,text=True)
    try: j=json.loads(r.stdout)
    except Exception: return [None]*len(reqs)
    if isinstance(j,dict): return [None]*len(reqs)
    out=[None]*len(reqs)
    for item in j:
        i=item.get("id")
        if isinstance(i,int) and 0<=i<len(out): out[i]=item.get("result")
    return out

def calls(chain, spec, timeout=60):
    """spec: list of ('call', to, data) | ('storage', addr, slot) | ('code', addr)."""
    reqs=[]
    for s in spec:
        if s[0]=='call':    reqs.append(("eth_call",[{"to":s[1],"data":s[2]},"latest"]))
        elif s[0]=='storage':reqs.append(("eth_getStorageAt",[s[1],s[2],"latest"]))
        elif s[0]=='code':  reqs.append(("eth_getCode",[s[1],"latest"]))
    res=batch(chain,reqs,timeout)
    out=[]
    for s,r in zip(spec,res):
        if s[0]=='code' and isinstance(r,str) and r.startswith('0x'): out.append((len(r)-2)//2)
        elif s[0]=='code': out.append(r if isinstance(r,int) else None)
        else: out.append(r)
    return out
