#!/usr/bin/env python3
"""Read-only public-source sweep for the non-EVM cohort.

The EVM screen reads deployed bytecode and verified explorer source. On Cosmos SDK,
Substrate, Solana, Move and the rest there is no equivalent per-address verified
source, so the readable artifact is the project's own public repository. That is a
weaker evidence level and is scored as such: these pairs cap at L2_DEPLOYMENT,
never L3/L4, because a repository is not proof of what is running on chain.

Only public HTTP GET is used. Nothing is cloned, executed, or written anywhere but
this run's cache.
"""
import json,os,sys,time,urllib.parse,subprocess,collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import repo_indicators as RI
from nonevm_cohort import RUNTIME_FAMILIES, EXT

B='/home/user/dd1/incident-intelligence'
CACHE=f'{B}/sources/repos'
TOK=os.environ.get('GITHUB_TOKEN') or os.environ.get('GH_TOKEN') or ''
LANG_FOR={'COSMOS_SDK_GO':{'Go'},'SUBSTRATE_RUST':{'Rust'},'SOLANA_RUST':{'Rust'},
          'MOVE':{'Move'},'CAIRO':{'Cairo'},'OTHER_VM':{'Rust','Go','TypeScript','Python','Haskell','C++'},
          'UNKNOWN_RUNTIME':{'Rust','Go','Move','TypeScript'}}
# paths most likely to hold handler / keeper / program logic
HOT=('x/','keeper','handler','module','pallet','programs/','sources/','contracts/','src/','msg','tx')
MAXREPO=2; MAXFILES=90; MAXBYTES=400_000

def api(url):
    cmd=["curl","-sS","-m","30","-H","Accept: application/vnd.github+json"]
    if TOK: cmd+=["-H",f"Authorization: Bearer {TOK}"]
    r=subprocess.run(cmd+[url],capture_output=True,text=True)
    try: return json.loads(r.stdout)
    except Exception: return None

def raw(owner,repo,ref,path):
    u=f"https://raw.githubusercontent.com/{owner}/{repo}/{ref}/{urllib.parse.quote(path)}"
    r=subprocess.run(["curl","-sS","-m","30","-L",u],capture_output=True,text=True)
    return r.stdout if r.returncode==0 else None

def pick_repos(org, runtime):
    langs=LANG_FOR.get(runtime,set())
    for kind in ("orgs","users"):
        d=api(f"https://api.github.com/{kind}/{org}/repos?per_page=100&sort=updated")
        if isinstance(d,list) and d: break
    else: return []
    cand=[]
    for r in d:
        if r.get('fork') or r.get('archived'): continue
        lang=r.get('language')
        score=(3 if lang in langs else 0)+(1 if any(h in (r.get('name') or '').lower()
               for h in ('core','node','chain','protocol','contract','program','pallet')) else 0)
        if score==0: continue
        cand.append((score,r.get('stargazers_count') or 0,r['name'],r.get('default_branch') or 'main'))
    cand.sort(reverse=True)
    return [(n,b) for _s,_st,n,b in cand[:MAXREPO]]

def tree_files(owner,repo,ref,exts):
    d=api(f"https://api.github.com/repos/{owner}/{repo}/git/trees/{ref}?recursive=1")
    if not isinstance(d,dict) or 'tree' not in d: return []
    out=[]
    for n in d['tree']:
        if n.get('type')!='blob': continue
        p=n['path']
        if not any(p.endswith(e) for e in exts): continue
        if (n.get('size') or 0)>MAXBYTES: continue
        if RI.VIEW_ONLY.search(p): continue
        out.append((1 if any(h in p.lower() for h in HOT) else 0, -(n.get('size') or 0), p))
    out.sort(reverse=True)
    return [p for _h,_s,p in out[:MAXFILES]]

def sweep_protocol(rec):
    rt=rec['runtime']; exts=EXT[rt]
    fams=set(rec['screenable_families'])
    res={"slug":rec['slug'],"runtime":rt,"repos":[],"files_read":0,
         "hits":[], "status":"NO_REPO_RESOLVED"}
    for org in rec['github'][:2]:
        for repo,ref in pick_repos(org,rt):
            paths=tree_files(org,repo,ref,exts)
            if not paths: continue
            res['repos'].append({"owner":org,"repo":repo,"ref":ref,"files":len(paths)})
            d=f"{CACHE}/{rec['slug']}__{org}__{repo}"
            os.makedirs(d,exist_ok=True)
            for p in paths:
                fp=os.path.join(d,p.replace('/','__'))
                if os.path.exists(fp):
                    txt=open(fp,errors='ignore').read()
                else:
                    txt=raw(org,repo,ref,p)
                    if txt is None: continue
                    open(fp,'w',errors='ignore').write(txt)
                res['files_read']+=1
                for h in RI.scan(p,txt,set(exts),fams):
                    h['repo']=f"{org}/{repo}"; res['hits'].append(h)
            if res['files_read']: res['status']="SWEPT"
        if res['status']=="SWEPT": break
    byfam=collections.defaultdict(lambda:{"PRE":[],"GUARD":[],"WEAK":[]})
    for h in res['hits']: byfam[h['family']][h['role']].append(h)
    res['by_family']={k:{r:v[r] for r in ('PRE','GUARD','WEAK')} for k,v in byfam.items()}
    res['hits']=len(res['hits'])
    return res

def main():
    limit=int(sys.argv[1]) if len(sys.argv)>1 else 10**9
    force='--force' in sys.argv
    C=[r for r in json.load(open(f'{B}/protocols/nonevm_cohort.json')) if r['in_band'] and r['github']]
    outp=f'{B}/protocols/nonevm_source_sweep.json'
    done=json.load(open(outp)) if (os.path.exists(outp) and not force) else {}
    todo=[r for r in C if r['slug'] not in done][:limit]
    print(f"non-EVM source sweep over {len(todo)} protocols (done {len(done)})",flush=True)
    t0=time.time()
    for i,rec in enumerate(todo):
        try: done[rec['slug']]=sweep_protocol(rec)
        except Exception as e: done[rec['slug']]={"slug":rec['slug'],"status":"ERROR","error":str(e)[:200]}
        if i%10==0:
            el=time.time()-t0
            print(f"  [{i}/{len(todo)}] {rec['slug']} -> {done[rec['slug']]['status']} "
                  f"({done[rec['slug']].get('files_read',0)} files, {el:.0f}s)",flush=True)
            json.dump(done,open(outp,'w'))
    json.dump(done,open(outp,'w'))
    st=collections.Counter(v['status'] for v in done.values())
    fam=collections.Counter()
    for v in done.values():
        for f,roles in (v.get('by_family') or {}).items():
            if roles['PRE'] and not roles['GUARD']: fam[f]+=1
    print(json.dumps({"protocols":len(done),"by_status":dict(st),
      "files_read":sum(v.get('files_read',0) for v in done.values()),
      "protocols_with_unguarded_PRE_by_family":dict(fam)},indent=2))

if __name__=='__main__': main()
