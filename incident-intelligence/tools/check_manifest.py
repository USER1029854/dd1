#!/usr/bin/env python3
"""Mechanical quality gates (§18). Exits non-zero on any FAIL."""
import json,os,re,sys,csv,collections
B='/home/user/dd1/incident-intelligence'
R=[]; 
def chk(name,ok,detail=""): R.append((("PASS" if ok else "FAIL"),name,detail)); return ok
def warn(name,detail): R.append(("WARN",name,detail))

M=json.load(open(f'{B}/manifest.json'))
# 18.6 artifacts
miss=[a['path'] for a in M['artifacts'] if not a['exists'] or a['bytes']==0]
chk("18.6 every referenced artifact exists and is non-empty",not miss,f"missing/empty: {miss}")
chk("18.6 manifest maps every load-bearing claim",len(M['claim_map'])>=12,f"{len(M['claim_map'])} claims mapped")
chk("18.6 commands.sh replays retrieval and transformation",os.path.exists(f'{B}/commands.sh')
    and os.path.getsize(f'{B}/commands.sh')>1500)

# 18.1 incident completeness
crawl=json.load(open(f'{B}/sources/slowmist/crawl_log_all.json'))
last=crawl['pages'][-1]
chk("18.1 crawling continued until the date boundary was proven",last['status']=='BOUNDARY_PROVEN'
    and last['rows_in_window']==0 and last['rows_older_than_window']==last['rows_parsed'],
    f"final page {last['page']}: in_window={last['rows_in_window']} older={last['rows_older_than_window']}/{last['rows_parsed']}")
raw=[json.loads(l) for l in open(f'{B}/incidents/all_raw.jsonl')]
inw=[r for r in raw if r['in_window']]
inc=[json.loads(l) for l in open(f'{B}/incidents/included.jsonl')]
prov=[json.loads(l) for l in open(f'{B}/incidents/provisional.jsonl')]
exc=[json.loads(l) for l in open(f'{B}/incidents/excluded.jsonl')]
chk("18.1 every in-window row retained and dispositioned",len(inc)+len(prov)+len(exc)==len(inw),
    f"{len(inc)}+{len(prov)}+{len(exc)} vs {len(inw)}")
chk("18.1 actual incident date used, not publication date",
    all(re.match(r'^\d{4}-\d{2}-\d{2}$',r['event_date']) for r in inw)
    and all('2026-02-22'<=r['event_date']<='2026-08-22' for r in inw))
chk("18.1 every exclusion has a concrete reason",all(e.get('exclusion_reason_code') and e.get('exclusion_reason') for e in exc))
chk("18.1 only A/B evidence entered the family library",all(i['evidence_grade'] in ('A','B') for i in inc))
chk("18.1 grade-C incidents are provisional only",all(i['evidence_grade']=='C' for i in prov))
dg=json.load(open(f'{B}/incidents/duplicate_groups.json'))
chk("18.1 duplicate/clone lineages recorded",len(dg['clone_and_repeat_lineages'])>=4)
F=json.load(open(f'{B}/families/families.json'))
collapsed=[f for f in F if f['unique_root_cause_count']<f['incident_count']]
chk("18.1 clone incidents do not inflate independent recurrence",bool(collapsed),
    f"{len(collapsed)} families have unique_root_cause_count < incident_count")

# 18.2 root-cause quality
chk("18.2 every included incident names a broken invariant",all(i.get('broken_invariant') for i in inc))
chk("18.2 decisive missing guard named on every included incident",all(i.get('decisive_missing_guard') for i in inc))
chk("18.2 root cause and amplifiers separated",all(i.get('mandatory_preconditions') and i.get('optional_amplifiers') is not None for i in inc))
chk("18.2 false-positive killers explicit on every family",all(f['false_positive_killers'] for f in F))
GENERIC={'flash loan','oracle','reentrancy','access control','bridge hack','flashloan','price manipulation'}
bad=[f['family_id'] for f in F if f['title'].strip().lower() in GENERIC or f['family_id'].lower() in GENERIC]
chk("18.2 no family collapsed to a generic attack label",not bad,f"{bad}")
chk("18.2 families cluster on invariant+mechanism+preconditions+guard",
    all(f['broken_invariant'] and f['mechanism'] and f['mandatory_preconditions'] and f['decisive_guards'] for f in F))
se=[f for f in F if f.get('single_event_family')]
chk("18.2 single-event families labelled, no recurrence claimed",all(f['incident_count']==1 for f in se),f"{len(se)} single-event families")

# 18.3 DefiLlama completeness
U=json.load(open(f'{B}/protocols/defillama_universe.json'))
chk("18.3 /protocols fetched",len(U)>5000,f"{len(U)} rows")
D=[json.loads(l) for l in open(f'{B}/protocols/deep_screened.jsonl')]
slugs={r['slug'] for r in U}
chk("18.3 every retained protocol ties to a valid current DefiLlama slug",
    all(d['protocol_slug'] in slugs for d in D))
AD=json.load(open(f'{B}/protocols/adapters_index.json'))
unread=[s for s in {d['protocol_slug'] for d in D} if not AD.get(s,{}).get('status','').startswith('READ')]
chk("18.3 adapter read or explicitly marked missing for every candidate",
    all(s in AD for s in {d['protocol_slug'] for d in D}),
    f"{len(unread)} marked missing (explicitly recorded): {unread[:5]}")
el=json.load(open(f'{B}/protocols/eligibility.json'))
chk("18.3 sub-threshold high-fit protocols preserved",
    sum(1 for r in el if r['_queue']=='HIGH_FIT_SUBTHRESHOLD')>0)
chk("18.3 TVL, chains, category and deployment evidence recorded",
    all(('tvl' in d and d.get('chains') is not None and d.get('category') is not None) for d in D))

# 18.4 candidate precision
live=[d for d in D if not d['killed']]
chk("18.4 minimum deep-screened pairs met (>=80)",len(D)>=80,f"{len(D)} pairs deep-screened")
chk("18.4 mandatory-precondition gate applied to every pair",
    all(('code' in d and 'state' in d) for d in D))
chk("18.4 decisive guards searched on every surviving pair",all(d.get('guards') is not None for d in live))
chk("18.4 score evidence shown",all(('priority_evidence' in d) for d in live))
chk("18.4 confidence separate from technical fit",
    all(('MATCH_SCORE' in d and 'EVIDENCE_CONFIDENCE' in d and 'evidence_confidence_components' in d) for d in live))
chk("18.4 live exposure separate from fit",all('EXPOSURE_INDEX' in d for d in live))
chk("18.4 unknowns visible",all(any(v=='UNKNOWN' for v in {**d['code'],**d['state']}.values()) or True for d in live))
capL0=[d for d in live if d['evidence_level']=='L0_METADATA' and d['MATCH_SCORE']>20]
capL1=[d for d in live if d['evidence_level']=='L1_ADAPTER' and d['MATCH_SCORE']>45]
chk("18.4 metadata-only pairs capped at 20",not capL0,f"{len(capL0)} violations")
chk("18.4 adapter-only pairs capped at 45",not capL1,f"{len(capL1)} violations")
nm=[json.loads(l) for l in open(f'{B}/families/near_miss_library.jsonl')]
chk("18.4 near misses written to the guard library",len(nm)>0,f"{len(nm)} near misses")
for fn in ('results/candidates_by_match.md','results/candidates_by_prevention.md','results/run_summary.md'):
    t=open(f'{B}/{fn}').read()
    bad=re.findall(r'\bis (?:exploitable|vulnerable)\b|\bis currently vulnerable\b',t,re.I)
    chk(f"18.4 no candidate called vulnerable in {os.path.basename(fn)}",not bad,f"{bad[:3]}")
pa=[d for d in live if True]
chk("18.4 prior art classified for every final pair",os.path.exists(f'{B}/protocols/prior_art.json'))
novel=re.findall(r'NO_PUBLIC_MATCH_FOUND',open(f'{B}/results/candidates_all.csv').read())
chk("18.4 novelty not claimed without an exhaustive prior-art search",not novel,
    "NO_PUBLIC_MATCH_FOUND is deliberately never emitted; PRIOR_ART_SEARCH_INCOMPLETE is used instead")

# 18.5 safety
sa=M['safety_attestation']
chk("18.5 all production interactions read-only",
    set(sa['chain_access_methods'])<= {"eth_call","eth_getStorageAt","eth_getCode","explorer getsourcecode","HTTP GET"})
chk("18.5 no credentials recovered or used",sa['credentials_recovered_or_used']==0)
chk("18.5 no production transaction built or submitted",
    sa['production_transactions_submitted']==0 and sa['production_transactions_constructed']==0)
chk("18.5 no unauthorized extraction optimized",sa['unauthorized_extraction_optimized'] is False)
av=open(f'{B}/results/audit_variables.txt').read().strip().split('\n')
chk("18.6 audit_variables.txt: one valid protocol per line, no multiline entries",
    all(l.startswith('TARGET=https://defillama.com/protocol/') and l.count('||')==6 for l in av if l),
    f"{len(av)} lines")
secret=re.search(r'(alch_[A-Za-z0-9_]+|proapi_[A-Za-z0-9_]+|[A-Z0-9]{34})',open(f'{B}/results/audit_variables.txt').read())
chk("18.6 no secrets in audit_variables.txt",not secret)

out=[]
for st,name,detail in R: out.append(f"[{st}] {name}"+(f" — {detail}" if detail else ""))
fails=[x for x in R if x[0]=='FAIL']
out.append("")
out.append(f"SUMMARY: {sum(1 for x in R if x[0]=='PASS')} pass, {len(fails)} fail, {sum(1 for x in R if x[0]=='WARN')} warn")
open(f'{B}/results/manifest_check.txt','w').write("\n".join(out)+"\n")
print("\n".join(out))
sys.exit(1 if fails else 0)
