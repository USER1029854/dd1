#!/usr/bin/env python3
import json,collections,os,csv
B='/home/user/dd1/incident-intelligence'
cfg=json.load(open(f'{B}/run_config.json'))
crawl=json.load(open(f'{B}/sources/slowmist/crawl_log_all.json'))
raw=[json.loads(l) for l in open(f'{B}/incidents/all_raw.jsonl')]
inw=[r for r in raw if r['in_window']]
inc=[json.loads(l) for l in open(f'{B}/incidents/included.jsonl')]
prov=[json.loads(l) for l in open(f'{B}/incidents/provisional.jsonl')]
exc=[json.loads(l) for l in open(f'{B}/incidents/excluded.jsonl')]
F=json.load(open(f'{B}/families/families.json'))
dup=json.load(open(f'{B}/incidents/duplicate_groups.json'))
U=json.load(open(f'{B}/protocols/defillama_universe.json'))
el=json.load(open(f'{B}/protocols/eligibility.json'))
AD=json.load(open(f'{B}/protocols/adapters_index.json'))
D=[json.loads(l) for l in open(f'{B}/protocols/deep_screened.jsonl')]
pairs=json.load(open(f'{B}/protocols/pairs_l0.json'))
NS=json.load(open(f'{B}/protocols/families_not_screenable_in_universe.json'))
live=[d for d in D if not d['killed']]
rowsA=list(csv.DictReader(open(f'{B}/results/candidates_all.csv')))
finals=[r for r in rowsA if r['in_final_20']=='YES']
def usd(v): return f"${v:,.0f}" if v else "n/a"
loss=sum(i['reported_loss_usd'] or 0 for i in inc)
# unique root causes at incident level: 110 minus collapsed lineage members
collapse=sum(len(l['incident_ids'])-l['unique_root_causes'] for l in dup['clone_and_repeat_lineages']
             if l['type'] in ('REPEAT_SAME_UNREMEDIATED_ROOT_CAUSE','FORK_CLONE_SHARED_CODEBASE','SAME_OPERATOR_TEMPLATE'))
urc=len(inc)-collapse
L=[]
L.append("# Run summary\n")
L.append(f"**Run:** `{cfg['run_id']}`  ·  **Window:** {cfg['window_start']} to {cfg['window_end']} (inclusive, incident date not publication date)  ·  **Run date (UTC):** {cfg['run_date_utc']}\n")
L.append("## Incident corpus\n")
L.append("| Metric | Value |"); L.append("|---|---:|")
L.append(f"| Date window | {cfg['window_start']} → {cfg['window_end']} |")
L.append(f"| SlowMist pages fetched (all-category crawl) | {len(crawl['pages'])} |")
L.append(f"| Boundary proof on final page | `{crawl['pages'][-1]['status']}` (page {crawl['pages'][-1]['page']}: 0 in-window, {crawl['pages'][-1]['rows_older_than_window']}/{crawl['pages'][-1]['rows_parsed']} older than window start) |")
L.append(f"| Per-category crawls (category attribution) | 20 categories, all reaching back past window start |")
L.append(f"| Raw incident rows captured | {len(raw)} |")
L.append(f"| Incidents inside window | {len(inw)} |")
L.append(f"| Included, grade A | {sum(1 for i in inc if i['evidence_grade']=='A')} |")
L.append(f"| Included, grade B | {sum(1 for i in inc if i['evidence_grade']=='B')} |")
L.append(f"| Provisional (grade C) | {len(prov)} |")
L.append(f"| Excluded | {len(exc)} |")
L.append(f"| Duplicate/clone/repeat lineages | {len(dup['clone_and_repeat_lineages'])} |")
L.append(f"| Total included reported loss | {usd(loss)} |")
L.append(f"| Unique root causes (lineage-collapsed) | {urc} |")
L.append(f"| Mechanism families | {len(F)} |")
L.append(f"| Single-event families | {sum(1 for f in F if f.get('single_event_family'))} |")
L.append(f"| Date-unverified incidents | {sum(1 for r in inw if r['date_status']!='VERIFIED')} |")
L.append("\n### Exclusion counts by reason\n")
L.append("| Reason code | Count |"); L.append("|---|---:|")
for k,v in collections.Counter(e['exclusion_reason_code'] for e in exc).most_common():
    L.append(f"| `{k}` | {v} |")
L.append("\n### Largest families by incident count\n")
L.append("| Family | Incidents | Unique root causes | 6-month loss | Most recent |")
L.append("|---|---:|---:|---:|---|")
for f in F[:12]:
    L.append(f"| `{f['family_id']}` | {f['incident_count']} | {f['unique_root_cause_count']} | {usd(f['six_month_loss_usd'])} | {f['most_recent_event']} |")
L.append("\n## DefiLlama screen\n")
L.append("| Metric | Value |"); L.append("|---|---:|")
L.append(f"| Protocols fetched from /protocols | {len(U)} |")
L.append(f"| Protocols eligible (main queue, TVL ≥ ${cfg['operational_settings']['minimum_tvl_usd']:,}) | {sum(1 for r in el if r['_queue']=='MAIN')} |")
L.append(f"| Sub-threshold high-fit queue preserved | {sum(1 for r in el if r['_queue']=='HIGH_FIT_SUBTHRESHOLD')} |")
L.append(f"| Excluded from the universe | {sum(1 for r in el if r['_queue']=='OUT')} |")
L.append(f"| Protocol-family pairs generated | {len(pairs)} |")
L.append(f"| Families screened as protocol-family pairs | {len(set(p['family_id'] for p in pairs))} |")
L.append(f"| Families with no addressable population in this universe | {len(NS)} |")
L.append(f"| Protocols in the stratified deep-screen worklist | {len(set(d['protocol_slug'] for d in D))} |")
L.append(f"| Pairs deep-screened | {len(D)} (requirement: ≥ {cfg['operational_settings']['minimum_deep_screened_pairs']}) |")
L.append(f"| Adapters successfully read | {sum(1 for v in AD.values() if v['status'].startswith('READ'))} |")
L.append(f"| Adapters read via a shared registry | {sum(1 for v in AD.values() if v.get('shared_registry_adapter'))} |")
L.append(f"| Adapters missing | {sum(1 for v in AD.values() if not v['status'].startswith('READ'))} |")
L.append(f"| Dynamic adapters (factory/registry driven) | {sum(1 for v in AD.values() if v.get('uses_factory_or_registry'))} |")
L.append(f"| Adapters depending on an external API | {sum(1 for v in AD.values() if v.get('uses_external_api'))} |")
L.append(f"| Pairs killed by a mandatory precondition | {sum(1 for d in D if d.get('kill_reason')=='MANDATORY_PRECONDITION_PROVEN_ABSENT')} |")
L.append(f"| Pairs killed by a decisive guard | {sum(1 for d in D if d.get('kill_reason')=='DECISIVE_GUARD_FOUND')} |")
L.append(f"| Pairs killed for lack of a lawful disclosure recipient | {sum(1 for d in D if d.get('kill_reason')=='SANCTIONS_DESIGNATED_NO_LAWFUL_ENGAGEMENT')} |")
L.append(f"| Surviving pairs | {len(live)} |")
L.append(f"| Final candidates | {len(finals)} |")
L.append("\n### Candidates at each evidence level\n")
L.append("| Evidence level | Surviving pairs | Final candidates |"); L.append("|---|---:|---:|")
sc=collections.Counter(d['evidence_level'] for d in live); fc=collections.Counter(r['evidence_level'] for r in finals)
for lv in ('L0_METADATA','L1_ADAPTER','L2_DEPLOYMENT','L3_STATE','L4_GUARD_REVIEW'):
    L.append(f"| `{lv}` | {sc.get(lv,0)} | {fc.get(lv,0)} |")
L.append("\n## Quality\n")
L.append("| Metric | Value |"); L.append("|---|---|")
L.append("| Unresolved source contradictions | 1 — `INC-2026-04-01-DRI` (Drift Protocol, ~$285M): the index's attack-method label reads *Social Engineering* while its own description describes a vault exploit with no mechanism given. Graded D and excluded from pattern derivation. |")
L.append(f"| Corpus completeness gap | At least one in-window on-chain incident documented elsewhere is absent from the SlowMist index (STO token, 2026-02-23, pair-burn reserve manipulation, per DARKNAVY). The index is a lead source, not a census. |")
L.append(f"| Unresolved deployment mappings | {sum(1 for v in AD.values() if not v['status'].startswith('READ'))} adapter(s) unresolved; {sum(1 for d in D if d['evidence_level'] in ('L0_METADATA','L1_ADAPTER'))} pairs remain at metadata/adapter evidence |")
L.append(f"| Protocols capped by weak evidence | {sum(1 for d in live if d['evidence_level']=='L1_ADAPTER')} pairs capped at the 45-point adapter ceiling; {sum(1 for d in live if d['evidence_level']=='L0_METADATA')} at the 20-point metadata ceiling |")
L.append(f"| Prior-art searches incomplete | {sum(1 for r in finals if r['prior_art_status']=='PRIOR_ART_SEARCH_INCOMPLETE')} of {len(finals)} final candidates. `NO_PUBLIC_MATCH_FOUND` is never emitted, so no novelty is claimed anywhere in this run. |")
L.append("| Commands reproducible | `commands.sh` replays every retrieval and transformation step in execution order |")
L.append("| Manifest checker result | see `results/manifest_check.txt` |")
L.append("\n## Safety attestation\n")
L.append("- All production-chain access was read-only: `eth_call`, `eth_getStorageAt`, `eth_getCode`, explorer `getsourcecode`, and HTTP GET.\n"
         "- Zero transactions constructed, signed, simulated as a broadcast against live user state, or submitted.\n"
         "- Zero credentials recovered, derived or used. No private key material was touched.\n"
         "- No exploitation sequence, production calldata, or extraction optimisation was produced anywhere in this output.\n"
         "- Only contracts with a documented relationship to a selected DefiLlama protocol were read.\n"
         "- One protocol-family pair was withheld from candidate promotion because the entity is sanctions-designated and an authorized defensive engagement has no lawful disclosure recipient there.")
open(f'{B}/results/run_summary.md','w').write("\n".join(L)+"\n")
print("run_summary.md written")
print(json.dumps({"included":len(inc),"unique_root_causes":urc,"loss":loss,
 "deep_screened":len(D),"finals":len(finals)},indent=2))
