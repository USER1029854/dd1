import json, subprocess, time, sys, os
BK=os.environ["BLOCKSCOUT_API_KEY"]
EP="0x1a44076050125825900e736c501f859c50fe728c"
TOPIC="0x6ee10e9ed4d6ce9742703a498707862f4b00f1396a87195eb93267b3d7983981"
HEAD=50596624
START=int(sys.argv[1]) if len(sys.argv)>1 else 15000000
WIN=400000
def get(url):
    for _ in range(4):
        p=subprocess.run(["curl","-sS","-m","45",url],capture_output=True,text=True)
        try: return json.loads(p.stdout)
        except: time.sleep(1)
    return {}
oapps={}
lo=START; wins=0
while lo<=HEAD:
    hi=min(lo+WIN,HEAD)
    page=1
    while True:
        url=(f"https://base.blockscout.com/api?module=logs&action=getLogs&fromBlock={lo}&toBlock={hi}"
             f"&address={EP}&topic0={TOPIC}&page={page}&offset=1000&apikey={BK}")
        j=get(url); res=j.get("result")
        if not isinstance(res,list) or not res: break
        for l in res:
            data=l["data"][2:]
            oapps["0x"+data[24:64]]=1
        if len(res)<1000: break
        page+=1; time.sleep(0.15)
    wins+=1
    if wins%15==0: print(f"  ..blk {hi} OApps={len(oapps)}",file=sys.stderr)
    lo=hi+1; time.sleep(0.1)
json.dump(sorted(oapps),open("sources/lz_screen/oapps_base.json","w"))
print(f"Base OApps distinct={len(oapps)} windows={wins} range[{START},{HEAD}]")
