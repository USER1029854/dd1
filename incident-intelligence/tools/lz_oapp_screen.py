import json, subprocess, time, sys, os
K=os.environ["ETHERSCAN_API_KEY"]
CHAIN="1"
EP="0x1a44076050125825900e736c501f859c50fe728c"
TOPIC="0x6ee10e9ed4d6ce9742703a498707862f4b00f1396a87195eb93267b3d7983981"
HEAD=25858924
START=19200000   # ~LZ V2 endpoint deploy era on mainnet
def eget(url):
    for _ in range(5):
        p=subprocess.run(["curl","-sS","-m","45",url],capture_output=True,text=True)
        try:
            j=json.loads(p.stdout)
            if isinstance(j.get("result"),list) or j.get("message")=="No records found": return j
        except: pass
        time.sleep(1.2)
    return {}
oapps={}
cur=START
pages=0
while cur<=HEAD and pages<400:
    url=(f"https://api.etherscan.io/v2/api?chainid={CHAIN}&module=logs&action=getLogs"
         f"&address={EP}&topic0={TOPIC}&fromBlock={cur}&toBlock={HEAD}&page=1&offset=1000&apikey={K}")
    j=eget(url); res=j.get("result") or []
    if not isinstance(res,list) or not res: break
    last=cur
    for l in res:
        data=l["data"][2:]
        oapp="0x"+data[24:64]
        deleg="0x"+data[88:128]
        blk=int(l["blockNumber"],16)
        oapps[oapp.lower()]={"delegate":deleg.lower(),"block":blk}  # keep latest (ascending => last wins)
        last=blk
    pages+=1
    if pages%20==0: print(f"  ..blk {last} OApps={len(oapps)}",file=sys.stderr)
    if len(res)<1000: break
    cur=last+1
    time.sleep(0.2)
json.dump(oapps,open("sources/lz_screen/oapps_mainnet.json","w"))
print(f"mainnet OApps (distinct, set-delegate) = {len(oapps)}  pages={pages}")
