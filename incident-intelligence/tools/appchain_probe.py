#!/usr/bin/env python3
"""Targeted public-source probe for app-chains, with an honest account of coverage.

Scope limit, stated up front
----------------------------
This session's network policy binds the GitHub API to the session's own repository,
and blocks github.com HTML and codeload tarballs. Only raw.githubusercontent.com by
EXACT path is reachable, so a repository's file tree cannot be enumerated. GitLab's
API is reachable and is used where a project lives there.

The consequence is that a broad non-EVM source sweep is not achievable here, and it
is not attempted. What IS achievable, without guessing, is the Cosmos convention:
app/app.go names every module the chain wires in, so fetching that one file yields
the real module list, and the module layout inside x/<module>/ is conventional.
Protocols this cannot reach stay at metadata evidence and are reported as such.

Why only app-chains
-------------------
RUNTIME-STATE-COMMITTED-BEFORE-FUNDING-TRANSFER and RUNTIME-HANDLER-ERROR-NO-ROLLBACK
describe a handler writing state, failing, and the write surviving. That is a property
of the CHAIN's own Go modules. A CosmWasm contract deployed on Osmosis does not have
it: the wasm VM discards state on error just as the EVM does. Screening contracts with
these families would manufacture false candidates, so the applicability set is
app-chains and Substrate runtimes only.
"""
import json,os,re,sys,subprocess,collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import repo_indicators as RI
B='/home/user/dd1/incident-intelligence'
CACHE=f'{B}/sources/repos'
ROLLBACK_FAMS={'RUNTIME-STATE-COMMITTED-BEFORE-FUNDING-TRANSFER','RUNTIME-HANDLER-ERROR-NO-ROLLBACK'}
ALL_GO_FAMS=ROLLBACK_FAMS|{'RUNTIME-BATCHED-MESSAGE-SHARED-KEY-CLOBBER','RECONCILIATION-STRIDE-SKIPS-TRUE-VALUE'}
CONV=["keeper/keeper.go","keeper/msg_server.go","keeper/msg_server_impl.go","handler.go",
      "abci.go","keeper/hooks.go","keeper/grpc_query.go","module.go","keeper/store.go"]

def raw(o,r,ref,p):
    u=f"https://raw.githubusercontent.com/{o}/{r}/{ref}/{p}"
    x=subprocess.run(["curl","-sS","-m","25","-L","-w","\\n%{http_code}",u],capture_output=True,text=True)
    out=x.stdout.rsplit("\n",1)
    if len(out)!=2 or out[1].strip()!="200": return None
    return out[0]

def probe(owner,repo):
    """Return (ref, [(path, text)]) using app/app.go to discover real module names."""
    for ref in ("main","master","develop"):
        app=raw(owner,repo,ref,"app/app.go")
        if app: break
    else:
        return None,[]
    # Cosmos import paths are version-prefixed (github.com/org/chain/v27/x/gamm/...), so
    # match x/<module> anywhere in app.go rather than only at a quoted path boundary.
    mods=sorted(set(re.findall(r'\bx/([a-z0-9_]+)\b',app)))
    mods=[m for m in mods if m not in ('types','utils','common','client','simulation','testutil')][:14]
    files=[("app/app.go",app)]
    d=f"{CACHE}/{owner}__{repo}"; os.makedirs(d,exist_ok=True)
    open(f"{d}/app__app.go","w",errors="ignore").write(app)
    for m in mods:
        for c in CONV:
            p=f"x/{m}/{c}"
            fp=f"{d}/{p.replace('/','__')}"
            if os.path.exists(fp): t=open(fp,errors='ignore').read()
            else:
                t=raw(owner,repo,ref,p)
                if t is None: continue
                open(fp,"w",errors="ignore").write(t)
            files.append((p,t))
    return ref,files

def main():
    targets=json.load(open(f'{B}/protocols/appchain_targets.json'))
    out={}
    for t in targets:
        owner,repo=t['owner'],t['repo']
        ref,files=probe(owner,repo)
        rec={"slug":t['slug'],"repo":f"{owner}/{repo}","ref":ref,
             "files_read":len(files),"status":"PROBED" if files else "REPO_PATH_NOT_REACHABLE",
             "by_family":{}}
        hits=[]
        for p,txt in files:
            hits+= [dict(h,repo=f"{owner}/{repo}") for h in RI.scan(p,txt,{'.go'},ALL_GO_FAMS)]
        byf=collections.defaultdict(lambda:{"PRE":[],"GUARD":[],"WEAK":[]})
        for h in hits: byf[h['family']][h['role']].append(h)
        rec['by_family']={k:v for k,v in byf.items()}
        rec['unguarded_families']=sorted(k for k,v in byf.items() if v['PRE'] and not v['GUARD'])
        rec['guarded_families']=sorted(k for k,v in byf.items() if v['GUARD'])
        out[t['slug']]=rec
        print(f"  {t['slug']:22s} {rec['status']:24s} files={rec['files_read']:3d} "
              f"unguarded={rec['unguarded_families']}",flush=True)
    json.dump(out,open(f'{B}/protocols/appchain_probe.json','w'),indent=1)
    print(json.dumps({"probed":len(out),
      "reachable":sum(1 for v in out.values() if v['status']=='PROBED'),
      "files_read":sum(v['files_read'] for v in out.values()),
      "with_unguarded_family":sum(1 for v in out.values() if v['unguarded_families'])},indent=2))

if __name__=='__main__': main()
