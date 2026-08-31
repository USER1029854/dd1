import json, subprocess, time
import os
RPC=os.environ.get("ETH_RPC_URL") or ("https://eth-mainnet.g.alchemy.com/v2/"+os.environ["ALCHEMY_API_KEY"])
def rpc(m,p):
    r=subprocess.run(["curl","-sS","-m","30","-X","POST",RPC,"-H","Content-Type: application/json",
        "--data",json.dumps({"jsonrpc":"2.0","id":1,"method":m,"params":p})],capture_output=True,text=True)
    try: return json.loads(r.stdout).get("result")
    except: return None
def call(to,data): return rpc("eth_call",[{"to":to,"data":data},"latest"])
def u(h,i=0): 
    if not h or h=="0x": return 0
    b=h[2:]; return int(b[i*64:(i+1)*64],16)
def dstr(h):
    if not h or h=='0x': return ''
    b=bytes.fromhex(h[2:])
    try:
        ln=int.from_bytes(b[32:64],'big'); return b[64:64+ln].decode('utf8','replace')
    except:
        return b.rstrip(b'\x00').decode('utf8','replace')
v=json.load(open('sources/arrakis/vaults.json'))
live=[x for x in v if x['totalSupply']>0]
toks=set()
for x in live:
    for t in (x['token0'],x['token1']):
        if t: toks.add(t.lower())
# fetch prices from defillama
ids=",".join("ethereum:"+t for t in toks)
pr={}
import urllib.request
try:
    for chunk_start in range(0,len(list(toks)),40):
        sub=list(toks)[chunk_start:chunk_start+40]
        q=",".join("ethereum:"+t for t in sub)
        j=json.load(urllib.request.urlopen("https://coins.llama.fi/prices/current/"+q, timeout=40))
        for k,val in j.get("coins",{}).items():
            pr[k.split(":")[1].lower()]={"price":val.get("price"),"dec":val.get("decimals"),"sym":val.get("symbol")}
except Exception as e:
    print("price err",e)
out=[]
for x in live:
    ub=call(x['vault'],"0x1322d954")  # getUnderlyingBalances -> (amount0,amount1)
    a0=u(ub,0); a1=u(ub,1)
    t0=(x['token0'] or '').lower(); t1=(x['token1'] or '').lower()
    p0=pr.get(t0,{}); p1=pr.get(t1,{})
    d0=p0.get('dec'); d1=p1.get('dec')
    # decimals fallback via call
    if d0 is None: d0=u(call(x['token0'],"0x313ce567")) or 18
    if d1 is None: d1=u(call(x['token1'],"0x313ce567")) or 18
    usd0=(a0/10**d0)*p0['price'] if p0.get('price') else None
    usd1=(a1/10**d1)*p1['price'] if p1.get('price') else None
    tvl=(usd0 or 0)+(usd1 or 0)
    priced = (p0.get('price') is not None) and (p1.get('price') is not None)
    out.append({"vault":x['vault'],"impl":x['impl'],"name":x['name'],
        "sym0":p0.get('sym'),"sym1":p1.get('sym'),"amount0":a0,"amount1":a1,
        "usd0":usd0,"usd1":usd1,"tvl_usd":tvl,"priced":priced})
out.sort(key=lambda z:-z['tvl_usd'])
json.dump(out,open('sources/arrakis/vault_tvl.json','w'),indent=1)
HIT="0xd68b055fb444d136e3ac4df023f4c42334f06395"
print(f"{'vault':44s} {'impl?':6s} {'TVL$':>14s}  {'priced':6s} name")
for x in out:
    flag='HITIMPL' if x['impl']==HIT else x['impl'][:7]
    print(f"{x['vault']} {flag:8s} {x['tvl_usd']:>14,.0f}  {str(x['priced']):5s} {(x['name'] or '')[:34]}")
print(f"\nTOTAL live TVL across G-UNI V1: ${sum(x['tvl_usd'] for x in out):,.0f}")
print(f"TVL on HIT impl (d68b055): ${sum(x['tvl_usd'] for x in out if x['impl']==HIT):,.0f}")
