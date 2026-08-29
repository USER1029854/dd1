import json, subprocess, sys
import os
RPC=os.environ.get("ETH_RPC_URL") or ("https://eth-mainnet.g.alchemy.com/v2/"+os.environ["ALCHEMY_API_KEY"])
F="0xea1aff9dbffd1580f6b81a3ad3589e66652db7d9"
def call(to,data,tag='latest'):
    p=subprocess.run(["curl","-sS","-m","30","-X","POST",RPC,"-H","Content-Type: application/json",
        "--data",json.dumps({"jsonrpc":"2.0","id":1,"method":"eth_call","params":[{"to":to,"data":data},tag]})],
        capture_output=True,text=True)
    try: return json.loads(p.stdout)["result"]
    except: return None
def dec_addr_array(hexstr):
    if not hexstr or hexstr=="0x": return []
    b=hexstr[2:]
    # offset(32) len(32) then items
    n=int(b[64:128],16)
    out=[]
    for i in range(n):
        w=b[128+i*64:128+i*64+64]
        out.append("0x"+w[24:])
    return out
def dec_addr(hexstr):
    if not hexstr or len(hexstr)<66: return None
    return "0x"+hexstr[2:][24:64]
def dec_uint(hexstr):
    if not hexstr or hexstr=="0x": return 0
    return int(hexstr,16)
# deployers
deployers=dec_addr_array(call(F,"0x607c12b5"))
print("deployers:",deployers, file=sys.stderr)
pools=[]
for d in deployers:
    # getPools(address)
    data="0x5c39f467"+d[2:].rjust(64,'0')
    ps=dec_addr_array(call(F,data))
    for p in ps: pools.append((p,d))
# also gelato pools
gp=dec_addr_array(call(F,"0x562b8103"))
seen={p for p,_ in pools}
for p in gp:
    if p not in seen: pools.append((p,"gelato"))
print("total pools enumerated:",len(pools), file=sys.stderr)
res=[]
for p,d in pools:
    impl=dec_addr(call(p,"0x5c60da1b"))  # implementation()
    t0=dec_addr(call(p,"0x0dfe1681"))
    t1=dec_addr(call(p,"0xd21220a7"))
    ts=dec_uint(call(p,"0x18160ddd"))
    name=call(p,"0x06fdde03")
    res.append({"vault":p,"deployer":d,"impl":impl,"token0":t0,"token1":t1,"totalSupply":ts,"name_hex":name})
json.dump(res,open("sources/arrakis/vaults.json","w"),indent=1)
print("written",len(res),"vaults")
