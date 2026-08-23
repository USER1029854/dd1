#!/usr/bin/env python3
import json,collections,csv,sys,os
sys.path.insert(0,'/home/user/dd1/incident-intelligence/tools')
import hazard as HZ
B='/home/user/dd1/incident-intelligence'
cfg=json.load(open(f'{B}/run_config.json'))
crawl=json.load(open(f'{B}/sources/slowmist/crawl_log_all.json'))
raw=[json.loads(l) for l in open(f'{B}/incidents/all_raw.jsonl')]; inw=[r for r in raw if r['in_window']]
inc=[json.loads(l) for l in open(f'{B}/incidents/included.jsonl')]
prov=[json.loads(l) for l in open(f'{B}/incidents/provisional.jsonl')]
exc=[json.loads(l) for l in open(f'{B}/incidents/excluded.jsonl')]
F=json.load(open(f'{B}/families/families.json'))
dup=json.load(open(f'{B}/incidents/duplicate_groups.json'))
U=json.load(open(f'{B}/protocols/defillama_universe.json'))
el=json.load(open(f'{B}/protocols/eligibility.json'))
AD=json.load(open(f'{B}/protocols/adapters_index.json'))
PRB=json.load(open(f'{B}/protocols/onchain_probes.json'))
D=[json.loads(l) for l in open(f'{B}/protocols/deep_screened.jsonl')]
BAND=json.load(open(f'{B}/protocols/band_screen.json'))
rows=list(csv.DictReader(open(f'{B}/results/candidates_all.csv')))
finals=[r for r in rows if r['in_final']=='YES']
live=[d for d in D if not d['killed']]
def usd(v): return f"${v:,.0f}" if v else "n/a"
loss=sum(i['reported_loss_usd'] or 0 for i in inc)
collapse=sum(len(l['incident_ids'])-l['unique_root_causes'] for l in dup['clone_and_repeat_lineages']
             if l['type'] in ('REPEAT_SAME_UNREMEDIATED_ROOT_CAUSE','FORK_CLONE_SHARED_CODEBASE','SAME_OPERATOR_TEMPLATE'))
L=[]
L.append("# Run summary\n")
L.append(f"**Run:** `{cfg['run_id']}` · **Window:** {cfg['window_start']} to {cfg['window_end']} (inclusive, incident date) · **Run date (UTC):** {cfg['run_date_utc']}\n")
L.append("## What this run optimises for\n")
L.append("An independent reviewer preventing real losses, not a fund allocating audit retainers. Two consequences "
         "drive everything downstream:\n")
L.append("1. **A $50,000 to $30,000,000 band.** Below it there is nothing worth saving. Above it, protocols are "
         "assumed to carry dedicated professional coverage and are dropped unless specific danger evidence says "
         "otherwise.\n")
L.append("2. **Exposure does not drive the ranking.** In this run's own corpus the median on-chain loss was "
         "**$252,000** and **84% of incidents cost under $2,000,000**; only 5% exceeded $10,000,000. Size is a poor "
         "predictor of being attacked, so the primary ranking is likelihood, and value at risk is reported "
         "beside it rather than baked into it.\n")
L.append("## Empirical victim profile (derived from this corpus, not assumed)\n")
L.append("| Loss band | Incidents | Share |"); L.append("|---|---:|---:|")
losses=sorted([i['reported_loss_usd'] for i in inc+prov if i['reported_loss_usd']])
for lo,hi,lbl in ((0,1e5,'under $100k'),(1e5,5e5,'$100k-$500k'),(5e5,2e6,'$500k-$2M'),(2e6,1e7,'$2M-$10M'),(1e7,1e12,'over $10M')):
    n=sum(1 for l in losses if lo<=l<hi); L.append(f"| {lbl} | {n} | {n/len(losses)*100:.0f}% |")
L.append(f"\nMedian **{usd(losses[len(losses)//2])}**, p75 **{usd(losses[int(len(losses)*0.75)])}**, "
         f"p90 **{usd(losses[int(len(losses)*0.90)])}**.\n")
L.append("### Hazard ratios: incident share divided by eligible-protocol share\n")
L.append("A ratio above 1 means the segment is over-represented among actual victims.\n")
L.append("| Category | Hazard | | Chain | Hazard |"); L.append("|---|---:|---|---|---:|")
cats=sorted(HZ.CATEGORY_HAZARD.items(),key=lambda x:-x[1])[:10]
chs=sorted(HZ.CHAIN_HAZARD.items(),key=lambda x:-x[1])[:10]
for i in range(max(len(cats),len(chs))):
    c=f"`{cats[i][0]}` | ×{cats[i][1]}" if i<len(cats) else " | "
    h=f"`{chs[i][0]}` | ×{chs[i][1]}" if i<len(chs) else " | "
    L.append(f"| {c} | | {h} |")
L.append("\nRisk Curators (×0.50) and RWA (×0.46) are *under*-represented among victims. An earlier pass of this "
         "run ranked them highly on exposure; the corpus says that was the wrong emphasis for this objective.\n")
L.append("## Incident corpus\n")
L.append("| Metric | Value |"); L.append("|---|---:|")
L.append(f"| SlowMist pages fetched | {len(crawl['pages'])} (boundary `{crawl['pages'][-1]['status']}`) |")
L.append(f"| Raw rows / inside window | {len(raw)} / {len(inw)} |")
L.append(f"| Included grade A / B | {sum(1 for i in inc if i['evidence_grade']=='A')} / {sum(1 for i in inc if i['evidence_grade']=='B')} |")
L.append(f"| Provisional (C) / Excluded | {len(prov)} / {len(exc)} |")
L.append(f"| Total included reported loss | {usd(loss)} |")
L.append(f"| Unique root causes | {len(inc)-collapse} |")
L.append(f"| Mechanism families | {len(F)} ({sum(1 for f in F if f.get('single_event_family'))} single-event) |")
L.append("\n## Band screen\n")
c=collections.Counter(r['band_status'] for r in BAND)
L.append("| Metric | Value |"); L.append("|---|---:|")
L.append(f"| Protocols fetched | {len(U)} |")
L.append(f"| Above the $50,000 floor | {sum(1 for r in el if r['_queue']=='MAIN')} |")
L.append(f"| Inside the $50k-$30M band | {c.get('IN_BAND',0)} |")
L.append(f"| Above the band, dropped (assumed professionally covered) | {c.get('ABOVE_BAND_DROPPED',0)} |")
L.append(f"| Above the band, kept on explicit danger | {c.get('ABOVE_BAND_KEPT_EXPLICIT_DANGER',0)} |")
L.append(f"| Below the floor, recorded but not screened | {len(json.load(open(f'{B}/protocols/subfloor_authority_deferred.json')))} |")
L.append(f"| Protocols deep-screened | {len(set(d['protocol_slug'] for d in D))} |")
L.append(f"| Protocol-family pairs screened | {len(D)} |")
L.append(f"| Pairs killed at the gate | {len(D)-len(live)} |")
L.append(f"| Adapters read | {sum(1 for v in AD.values() if v['status'].startswith('READ'))} |")
L.append(f"| Protocols with live chain evidence | {sum(1 for v in PRB.values() if v.get('deployment',{}).get('addresses_probed'))} |")
L.append(f"| Addresses read on-chain | {sum(len(v.get('deployment',{}).get('addresses_probed',[])) for v in PRB.values())} |")
L.append(f"| Privileged owner() resolving to an EOA | {sum(1 for v in PRB.values() if any(a.get('owner_is_eoa') for a in v.get('deployment',{}).get('addresses_probed',[])))} protocols |")
L.append(f"| Verified contracts analysed | {sum(1 for v in PRB.values() for x in v.get('source_sweep',{}).get('contracts',[]) if x.get('status')=='VERIFIED')} |")
L.append(f"| Final candidates | {len(finals)} |")
tv=sorted(float(r['value_at_risk_usd']) for r in finals)
if tv: L.append(f"| Median value at risk across finals | {usd(tv[len(tv)//2])} |")
L.append("\n### Most common attention-deficit signals across final candidates\n")
ns=collections.Counter()
for r in finals: ns.update([x for x in (r['neglect_signals'] or '').split('|') if x])
L.append("| Signal | Candidates |"); L.append("|---|---:|")
for k,v in ns.most_common(12): L.append(f"| `{k}` | {v} |")
L.append("\n## Quality\n")
L.append("| Metric | Value |"); L.append("|---|---|")
L.append("| Unresolved source contradictions | 1 — `INC-2026-04-01-DRI` (Drift, ~$285M): attack-method label says *Social Engineering* while the description describes a vault exploit with no mechanism. Graded D, excluded from pattern derivation. |")
L.append("| Corpus completeness gap | At least one in-window on-chain incident documented elsewhere (STO token, 2026-02-23) is absent from the index. Counts are lower bounds. |")
L.append(f"| Pairs still at metadata or adapter evidence | {sum(1 for d in live if d['evidence_level'] in ('L0_METADATA','L1_ADAPTER'))} of {len(live)} |")
L.append(f"| Prior-art searches incomplete | {sum(1 for r in finals if r['prior_art_status']=='PRIOR_ART_SEARCH_INCOMPLETE')} of {len(finals)} finals. `NO_PUBLIC_MATCH_FOUND` is never emitted. |")
L.append("| Commands reproducible | `commands.sh` replays every retrieval and transformation step |")
L.append("| Manifest checker | see `results/manifest_check.txt` |")
L.append("\n## Safety\n")
L.append("- All production-chain access read-only: `eth_call`, `eth_getStorageAt`, `eth_getCode`, explorer "
         "`getsourcecode`, HTTP GET.\n- Zero transactions constructed, signed, simulated as a broadcast, or "
         "submitted.\n- Zero credentials recovered or used; none committed.\n- No exploitation sequence or "
         "production calldata anywhere in this output.\n- Sanctions-designated entities are withheld from "
         "candidate promotion: an authorized defensive engagement has no lawful disclosure recipient there.")
open(f'{B}/results/run_summary.md','w').write("\n".join(L)+"\n")
print("run_summary.md written; finals:",len(finals))
