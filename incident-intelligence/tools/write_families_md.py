#!/usr/bin/env python3
import json,sys
B='/home/user/dd1/incident-intelligence'
F=json.load(open(f'{B}/families/families.json'))
NS=json.load(open(f'{B}/protocols/families_not_screenable_in_universe.json'))
RAW={json.loads(l)['incident_id']:json.loads(l) for l in open(f'{B}/incidents/all_raw.jsonl')}
def usd(v): return f"${v:,.0f}" if v else "not disclosed"
L=[]
L.append("# Mechanism Family Library — six-month window 2026-02-22 to 2026-08-22\n")
L.append("Families are clustered by **broken invariant + mechanism + mandatory prerequisite signature + "
         "decisive missing guard**, never by the source database's attack-method label. "
         "The SlowMist `Attack method` string is carried on each incident record only as "
         "`slowmist_attack_method_label_NOT_USED_FOR_CLUSTERING`.\n")
L.append(f"**{len(F)} families** derived from 110 grade-A/B incidents. "
         f"{sum(1 for f in F if f.get('single_event_family'))} are single-event families "
         "and are labelled as such: they make no recurrence claim.\n")
L.append("## Index\n")
L.append("| Family | Incidents | Unique root causes | 6-month loss | Most recent | Evidence |")
L.append("|---|---:|---:|---:|---|---|")
for f in F:
    se=" *(single-event)*" if f.get('single_event_family') else ""
    L.append(f"| `{f['family_id']}`{se} | {f['incident_count']} | {f['unique_root_cause_count']} | "
             f"{usd(f['six_month_loss_usd'])} | {f['most_recent_event']} | {f['evidence_strength']} |")
L.append("")
for f in F:
    L.append(f"\n---\n\n## `{f['family_id']}`")
    if f.get('single_event_family'): L.append("\n> **SINGLE_EVENT_FAMILY** — one verified incident. No recurrence is claimed.")
    L.append(f"\n**{f['title']}**\n")
    L.append(f"- **Incidents:** {f['incident_count']} (unique root causes: {f['unique_root_cause_count']}) · "
             f"**6-month loss:** {usd(f['six_month_loss_usd'])} · **Most recent:** {f['most_recent_event']} · "
             f"**Evidence strength:** {f['evidence_strength']}")
    L.append(f"\n### Broken invariant\n{f['broken_invariant']}")
    L.append(f"\n### Mechanism\n{f['mechanism']}")
    L.append("\n### Mandatory preconditions (all must hold; any proven absent kills the hypothesis)")
    for x in f['mandatory_preconditions']: L.append(f"- {x}")
    L.append("\n### Optional amplifiers (never the root cause)")
    for x in f['optional_amplifiers']: L.append(f"- {x}")
    L.append("\n### Applicable protocol archetypes\n"+", ".join(f['applicable_protocol_archetypes']))
    L.append("\n### Observable indicators")
    for label,key in (("Static (code)","static_indicators"),("Adapter","adapter_indicators"),
                      ("Runtime state","runtime_state_indicators"),("Cross-contract","cross_contract_indicators")):
        if f.get(key):
            L.append(f"\n**{label}**")
            for x in f[key]: L.append(f"- {x}")
    L.append("\n### Decisive guards (presence normally kills the hypothesis)")
    for x in f['decisive_guards']: L.append(f"- {x}")
    L.append("\n### False-positive killers")
    for x in f['false_positive_killers']: L.append(f"- {x}")
    L.append(f"\n### Local defensive property (fork-only test)\n{f['local_defensive_property']}")
    L.append("\n### Recommended audit questions")
    for x in f['recommended_audit_questions']: L.append(f"- {x}")
    L.append("\n### Incidents")
    for i in f['incident_ids']:
        r=RAW[i]; L.append(f"- `{i}` — {r['event_date']} — **{r['target']}** — {usd(r['reported_loss_usd'])}")
    if f['provisional_incident_ids']:
        L.append("\n**Provisional (grade C, not counted in statistics or ranking weight):**")
        for i in f['provisional_incident_ids']:
            r=RAW[i]; L.append(f"- `{i}` — {r['event_date']} — {r['target']}")
    L.append(f"\n### Propagation\n{f['propagation_notes']}")
    if f['family_id'] in NS:
        L.append(f"\n> **Not screenable as a protocol-family pair in the DefiLlama universe.** {NS[f['family_id']]['reason']}")
L.append("\n---\n\n## Families with no addressable population in the DefiLlama universe\n")
L.append("These families are real and evidenced, but their live prerequisite base is not a set of "
         "DefiLlama-listed protocols. They are handled as read-only sweeps over the deployments that "
         "deep screening already touches, and are recorded here so the gap is explicit rather than silent.\n")
L.append("| Family | Incidents | 6-month loss | Why it is not a protocol-family pair |")
L.append("|---|---:|---:|---|")
for k,v in sorted(NS.items(),key=lambda x:-x[1]['family_incident_count']):
    L.append(f"| `{k}` | {v['family_incident_count']} | {usd(v['family_loss_usd'])} | {v['reason']} |")
open(f'{B}/families/families.md','w').write("\n".join(L)+"\n")
print("families.md written:",sum(len(x) for x in L),"chars,",len(F),"families")
