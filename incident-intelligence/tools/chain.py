# -*- coding: utf-8 -*-
"""Read-only chain access. eth_call / eth_getStorageAt / explorer source reads only.
No transaction is ever constructed, signed or broadcast."""
import json,subprocess,time
import os
# Credentials are read from the environment. Nothing is embedded in this file.
ALCH=os.environ.get("ALCHEMY_KEY","")
ES_KEYS=[k for k in (os.environ.get("ETHERSCAN_V2_KEY",""),
                     os.environ.get("ETHERSCAN_V2_KEY_2","")) if k]
BSC_RPC=os.environ.get("BSC_RPC","")
_esk=[0]
RPC={  # direct RPC where available
 "ethereum":f"https://eth-mainnet.g.alchemy.com/v2/{ALCH}",
 "arbitrum":f"https://arb-mainnet.g.alchemy.com/v2/{ALCH}",
 "base":f"https://base-mainnet.g.alchemy.com/v2/{ALCH}",
 "binance":BSC_RPC,
 "bsc":BSC_RPC,
}
RPC={k:v for k,v in RPC.items() if v and not v.endswith("/v2/")}
CHAINID={"ethereum":1,"optimism":10,"binance":56,"bsc":56,"xdai":100,"gnosis":100,
 "polygon":137,"fantom":250,"base":8453,"arbitrum":42161,"avax":43114,"avalanche":43114,
 "linea":59144,"scroll":534352,"mantle":5000,"metis":1088,"blast":81457,"sonic":146,
 "core":1116,"celo":42220,"moonbeam":1284,"kava":2222,"era":324,"zksync":324,
 "berachain":80094,"unichain":130,"sonicm":146,"taiko":167000,"fraxtal":252,"mode":34443}

SEL={"getAllMarkets":"0xb0772d0b","exchangeRateStored":"0x182df0f5","totalSupply":"0x18160ddd",
 "getCash":"0x3b1d21a2","underlying":"0x6f307dc3","supplyCaps":"0x86df31ee","borrowCaps":"0x4a584432",
 "decimals":"0x313ce567","symbol":"0x95d89b41","balanceOf":"0x70a08231","owner":"0x8da5cb5b",
 "paused":"0x5c975abb","totalAssets":"0x01e1d114","asset":"0x38d52e0f","convertToAssets":"0x07a2d13a",
 "implementation":"0x5c60da1b","totalBorrows":"0x47bd3718","totalReserves":"0x8f840ddd",
 "admin":"0xf851a440","comptroller":"0x5fe3b567","totalSupplyAssets":"0x01e1d114",
 "name":"0x06fdde03","allowance":"0xdd62ed3e","curator":"0xc1fe3e48","owner2":"0x893d20e8",
 "getPriceOracle":"0xfca513a8","getLendingPool":"0x0261bf8b","getPool":"0x026b1d5f",
 "getReservesList":"0xd1946dbc","getAllMarketsAlt":"0x52d84d1e","getAssetsIn":"0xabfceffc"}
SLOT_1967_IMPL="0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc"
SLOT_1967_ADMIN="0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103"
SLOT_1967_BEACON="0xa3f0ad74e5423aebfd80d3ef4346578335a9a72aeaee59ff6cb3582b35133d50"
SLOT_OZ5_INIT="0xf0c57e16840df040f15088dc2f81fe391c3923bec73e23a9662efc9c229c6a00"

def _post(url,payload,timeout=35):
    r=subprocess.run(["curl","-sS","-m",str(timeout),"-X","POST","-H","content-type: application/json",
                      "--data",json.dumps(payload),url],capture_output=True,text=True)
    try: return json.loads(r.stdout)
    except Exception: return {"error":{"message":(r.stdout or r.stderr)[:200]}}

def _es(chain,params,timeout=35):
    cid=CHAINID.get(chain)
    if not cid: return None
    for _ in range(len(ES_KEYS)):
        k=ES_KEYS[_esk[0]%len(ES_KEYS)]
        q="&".join(f"{a}={b}" for a,b in params.items())
        url=f"https://api.etherscan.io/v2/api?chainid={cid}&{q}&apikey={k}"
        r=subprocess.run(["curl","-sS","-m",str(timeout),url],capture_output=True,text=True)
        try: j=json.loads(r.stdout)
        except Exception: j=None
        if j and str(j.get("message","")).lower().find("rate limit")<0 and "result" in j:
            return j
        _esk[0]+=1; time.sleep(0.5)
    return None

def call(chain,to,data,tag="latest"):
    """eth_call - read only."""
    chain=chain.lower()
    if chain in RPC:
        j=_post(RPC[chain],{"jsonrpc":"2.0","id":1,"method":"eth_call",
                            "params":[{"to":to,"data":data},tag]})
        if isinstance(j,dict) and j.get("result") is not None: return j["result"]
        if isinstance(j,dict) and j.get("error"): return None
    j=_es(chain,{"module":"proxy","action":"eth_call","to":to,"data":data,"tag":tag})
    if j and isinstance(j.get("result"),str) and j["result"].startswith("0x"): return j["result"]
    return None

def storage(chain,to,slot):
    chain=chain.lower()
    if chain in RPC:
        j=_post(RPC[chain],{"jsonrpc":"2.0","id":1,"method":"eth_getStorageAt","params":[to,slot,"latest"]})
        if isinstance(j,dict) and j.get("result"): return j["result"]
    j=_es(chain,{"module":"proxy","action":"eth_getStorageAt","address":to,"position":slot,"tag":"latest"})
    return j.get("result") if j else None

def code_size(chain,to):
    chain=chain.lower()
    if chain in RPC:
        j=_post(RPC[chain],{"jsonrpc":"2.0","id":1,"method":"eth_getCode","params":[to,"latest"]})
        c=j.get("result") if isinstance(j,dict) else None
    else:
        j=_es(chain,{"module":"proxy","action":"eth_getCode","address":to,"tag":"latest"})
        c=j.get("result") if j else None
    return (len(c)-2)//2 if isinstance(c,str) and c.startswith("0x") else None

def source(chain,addr):
    j=_es(chain,{"module":"contract","action":"getsourcecode","address":addr})
    if not j or not isinstance(j.get("result"),list) or not j["result"]: return None
    r=j["result"][0]
    return {"ContractName":r.get("ContractName"),"Proxy":r.get("Proxy"),
            "Implementation":r.get("Implementation"),
            "verified":bool(r.get("SourceCode")),"source":r.get("SourceCode") or "",
            "CompilerVersion":r.get("CompilerVersion"),"Licence":r.get("LicenseType")}

# ---- decoding helpers ----
def dec_uint(h):
    if not h or h=="0x" or len(h)<3: return None
    try: return int(h[:66],16)
    except Exception: return None
def dec_addr(h):
    if not h or len(h)<66: return None
    return "0x"+h[26:66]
def dec_addr_array(h):
    if not h or len(h)<130: return []
    try:
        body=h[2:]; n=int(body[64:128],16)
        return ["0x"+body[128+i*64+24:128+(i+1)*64] for i in range(min(n,400))]
    except Exception: return []
def enc_addr(a): return a.lower().replace("0x","").rjust(64,"0")
