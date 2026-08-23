#!/usr/bin/env python3
"""Archive every reference URL for gate-passing incidents with retrieval provenance."""
import hashlib, json, os, re, subprocess, sys, time
sys.path.insert(0,'/home/user/dd1/incident-intelligence/tools'); import classification as C
OUT="/home/user/dd1/incident-intelligence/sources/incident-references"; os.makedirs(OUT,exist_ok=True)
rows=[json.loads(l) for l in open('/home/user/dd1/incident-intelligence/incidents/all_raw.jsonl') if json.loads(l)['in_window']]
JS_SHELL=("x.com","twitter.com","t.me","telemetr.io")
idx=[]
for r in rows:
    if C.T[r['incident_id']][0] not in ("INCLUDE","PROVISIONAL"): continue
    for i,u in enumerate(r['reference_urls']):
        host=u.split('/')[2].lower() if '://' in u else ''
        rec={"incident_id":r['incident_id'],"url":u,"host":host,
             "retrieved_utc":time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime())}
        if any(h in host for h in JS_SHELL):
            rec.update({"status":"LEAD_ONLY_CLIENT_RENDERED",
                        "evidence_role":"lead (SlowMist §2.2 rank 7: social post) - body not machine-retrievable",
                        "http":None,"sha256":None,"snapshot":None})
        else:
            fn=f"{r['incident_id']}_ref{i}_{re.sub(r'[^a-z0-9]','_',host)}.html"
            p=os.path.join(OUT,fn)
            pr=subprocess.run(["curl","-sSL","-m","35","-o",p,"-w","%{http_code}",
                               "-A","Mozilla/5.0 (defensive-security-research; read-only)",u],
                              capture_output=True,text=True)
            code=(pr.stdout or "").strip()[-3:]
            ok=code=="200" and os.path.exists(p) and os.path.getsize(p)>500
            rec.update({"status":"RETRIEVED" if ok else "RETRIEVAL_FAILED","http":code,
                        "evidence_role":"corroborating source (§2.2 rank 3/6)",
                        "sha256":hashlib.sha256(open(p,'rb').read()).hexdigest() if ok else None,
                        "snapshot":fn if ok else None,
                        "bytes":os.path.getsize(p) if ok else 0})
            if not ok and os.path.exists(p): os.remove(p)
            time.sleep(0.4)
        idx.append(rec)
json.dump(idx,open(f"{OUT}/reference_index.json","w"),indent=2)
from collections import Counter
print(json.dumps({"refs":len(idx),"by_status":Counter(r['status'] for r in idx),
                  "incidents_covered":len(set(r['incident_id'] for r in idx))},indent=2,default=str))
