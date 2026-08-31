#!/usr/bin/env python3
"""Content-safe deduplication of adapter snapshots, plus pair-index compaction.

Protocols covered by a shared registry adapter each saved a byte-identical copy of the
same file. This keeps exactly one canonical copy per distinct content and repoints every
index entry at it. Grouping is done on the ACTUAL bytes on disk, never on a hash recorded
elsewhere, and a duplicate is only removed once its canonical twin is confirmed present.
"""
import json,os,hashlib,collections
B='/home/user/dd1/incident-intelligence'; AD=f'{B}/sources/defillama/adapters'

def h(p):
    with open(p,'rb') as fh: return hashlib.sha256(fh.read()).hexdigest()

groups=collections.defaultdict(list)
for f in sorted(os.listdir(AD)):
    p=os.path.join(AD,f)
    if os.path.isfile(p): groups[h(p)].append(f)

rename={}          # old filename -> canonical filename
freed=0; removed=0
for digest,files in groups.items():
    if len(files)==1:
        rename[files[0]]=files[0]; continue
    shared=[f for f in files if '__registries__' in f or f.startswith(('_shared__','_registry__'))]
    if shared:
        canon='_shared__'+shared[0].split('__',1)[1] if not shared[0].startswith(('_shared__','_registry__')) else shared[0]
    else:
        canon=min(files,key=len)
    cp=os.path.join(AD,canon)
    if not os.path.exists(cp):
        os.rename(os.path.join(AD,files[0]),cp)
        rename[files[0]]=canon
    for f in files:
        rename[f]=canon
        fp=os.path.join(AD,f)
        if f!=canon and os.path.exists(fp) and os.path.exists(cp):
            freed+=os.path.getsize(fp); os.remove(fp); removed+=1

idx=json.load(open(f'{B}/protocols/adapters_index.json'))
repoint=0
for slug,v in idx.items():
    sn=v.get('snapshot')
    if not sn: continue
    tgt=rename.get(sn)
    if tgt and tgt!=sn:
        v['snapshot']=tgt; repoint+=1
        v.setdefault('snapshot_note',"shared registry adapter: one canonical copy is kept and referenced by "
                                     "every protocol it covers")
json.dump(idx,open(f'{B}/protocols/adapters_index.json','w'),indent=1)

W={(w['protocol_slug'],w['family_id']) for w in json.load(open(f'{B}/protocols/deep_screen_worklist.json'))}
KEEP=('protocol_slug','protocol_name','defillama_url','category','tvl','family_id','screening_priority',
      'pair_origin','conditions','queue','band_status')
pp=f'{B}/protocols/pairs_l0.json'
if os.path.exists(pp):
    pairs=json.load(open(pp)); out=[]
    for p in pairs:
        if (p['protocol_slug'],p['family_id']) in W: out.append(p)
        else:
            r={k:p.get(k) for k in KEEP}
            r['_compact']="not selected for deep screening; full evidence recomputable via tools/gen_pairs4.py"
            out.append(r)
    json.dump(out,open(pp,'w'))
else: out=[]

dangling=[(k,v['snapshot']) for k,v in idx.items() if v.get('snapshot')
          and not os.path.exists(os.path.join(AD,v['snapshot']))]
missing=[k for k,v in idx.items() if v.get('status','').startswith('READ') and not v.get('snapshot')]
print(json.dumps({"duplicate_files_removed":removed,"freed_mb":round(freed/1048576,1),
 "index_entries_repointed":repoint,"adapter_files_remaining":len(os.listdir(AD)),
 "dangling_refs":len(dangling),"read_entries_without_snapshot":len(missing),
 "pairs_rows":len(out)},indent=2))
assert not dangling, f"dangling snapshot refs: {dangling[:5]}"
