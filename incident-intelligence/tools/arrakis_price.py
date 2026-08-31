import json, subprocess
import os
RPC=os.environ.get("ETH_RPC_URL") or ("https://eth-mainnet.g.alchemy.com/v2/"+os.environ["ALCHEMY_API_KEY"])
SLOT="0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc"  # EIP-1967 impl
def rpc(method,params):
    p=subprocess.run(["curl","-sS","-m","30","-X","POST",RPC,"-H","Content-Type: application/json",
        "--data",json.dumps({"jsonrpc":"2.0","id":1,"method":method,"params":params})],capture_output=True,text=True)
    try: return json.loads(p.stdout).get("result")
    except: return None
def call(to,data): return rpc("eth_call",[{"to":to,"data":data},"latest"])
def addr(h): return "0x"+h[2:][24:64] if h and len(h)>=66 else None
def u(h): return int(h,16) if h and h!="0x" else 0
v=json.load(open('sources/arrakis/vaults.json'))
def dstr(h):
    if not h or h=='0x': return ''
    b=bytes.fromhex(h[2:])
    try:
        ln=int.from_bytes(b[32:64],'big'); return b[64:64+ln].decode('utf8','replace')
    except: return ''
for x in v:
    x['name']=dstr(x['name_hex'])
    x['impl']=addr(rpc("eth_getStorageAt",[x['vault'],SLOT,"latest"]))
    # balances of token0/token1 held by vault (idle) - main value is in the uni v3 position; use getUnderlyingBalances()
    ub=call(x['vault'],"0xe598c14a")  # getUnderlyingBalances() selector? compute below if wrong
json.dump(v,open('sources/arrakis/vaults.json','w'),indent=1)
import collections
print("impls:",collections.Counter(x['impl'] for x in v))
