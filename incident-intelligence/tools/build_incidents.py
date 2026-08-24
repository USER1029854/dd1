#!/usr/bin/env python3
"""Phase C/D builder: normalized incident records, family library, guard library."""
import json,os, sys, collections
sys.path.insert(0,'/home/user/dd1/incident-intelligence/tools')
import classification as C
from incident_specifics import S
from families_a import FAM_A
from families_b import FAM_B
from families_c import FAM_C
from families_d import FAM_D
FAM = {**FAM_A, **FAM_B, **FAM_C, **FAM_D}
B = '/home/user/dd1/incident-intelligence'

raw = {json.loads(l)['incident_id']: json.loads(l) for l in open(f'{B}/incidents/all_raw.jsonl')}
refidx = json.load(open(f'{B}/sources/incident-references/reference_index.json'))
refs_by_inc = collections.defaultdict(list)
for r in refidx: refs_by_inc[r['incident_id']].append(r)

# incidents whose grade was raised by a retrieved independent technical source
CORROB = {"INC-2026-07-06-LAZ","INC-2026-03-15-VEN","INC-2026-05-05-EKU","INC-2026-06-10-SEC",
          "INC-2026-02-22-BLE","INC-2026-03-02-CUR","INC-2026-04-16-RHE","INC-2026-04-27-SIN",
          "INC-2026-05-18-VER","INC-2026-07-23-VER","INC-2026-06-19-JBX","INC-2026-04-28-JUD",
          "INC-2026-07-28-LUL","INC-2026-03-12-AMU","INC-2026-03-10-MTW"}
# Incidents whose grade rests on deployed-code evidence: the exact files and lines were
# read from the project's live public repository and the claimed defect confirmed there.
# The per-claim record is incidents/source_verification.json.
SRCVERIFY=json.load(open(f'{B}/incidents/source_verification.json'))['incidents'] \
          if os.path.exists(f'{B}/incidents/source_verification.json') else {}

def rec(iid):
    d, r = C.T[iid], raw[iid]
    disp, grade, reason, fams, chains, arch = d
    spec = S.get(iid, ([], FAM[fams[0]]['broken_invariant'] if fams else "", ""))
    fam0 = FAM[fams[0]] if fams else {}
    return {
      "incident_id": iid, "event_date": r['event_date'], "target": r['target'],
      "chains": chains, "protocol_archetype": arch,
      "reported_loss_usd": r['reported_loss_usd'],
      "net_loss_basis": r['reported_loss_raw'] or "not disclosed",
      "evidence_grade": grade, "gate_result": disp,
      "date_status": r['date_status'],
      "source_claims": [{"source":"SlowMist Hacked index","claim":r['description_raw'],
                         "url":r['slowmist_page_url'],"role":"index/lead (§2.1)"}],
      "corroboration": ("DEPLOYED_SOURCE_VERIFIED" if iid in SRCVERIFY
                        else "INDEPENDENT_TECHNICAL_SOURCE_RETRIEVED" if iid in CORROB
                        else ("REFERENCE_RETRIEVED" if any(x['status']=='RETRIEVED' for x in refs_by_inc[iid])
                              else "SLOWMIST_MECHANISM_RECORD_ONLY")),
      **({"source_verification": SRCVERIFY[iid]} if iid in SRCVERIFY else {}),
      "affected_contracts": [], "affected_functions": spec[0],
      "broken_invariant": spec[1],
      "root_cause": r['description_raw'],
      "unauthorized_transition": fam0.get('mechanism',''),
      "mandatory_preconditions": fam0.get('mandatory_preconditions',[]),
      "optional_amplifiers": fam0.get('optional_amplifiers',[]),
      "state_written_first": [], "state_read_later": [],
      "external_dependencies": [], "capital_or_liquidity_assumption":
        ("flash-loan or pre-accumulated capital used as amplifier" if 'flash' in r['description_raw'].lower()
         else "no external capital requirement identified"),
      "single_or_multi_transaction": ("single" if 'single transaction' in r['description_raw'].lower()
                                      or 'atomic' in r['description_raw'].lower() else "unspecified"),
      "time_or_epoch_dependency": ("epoch/settlement boundary" if 'SETTLEMENT-EPOCH-BOUNDARY-CREDIT' in fams else "none identified"),
      "decisive_missing_guard": spec[2],
      "guards_that_would_falsify": fam0.get('decisive_guards',[]),
      "static_indicators": fam0.get('static_indicators',[]),
      "runtime_state_indicators": fam0.get('runtime_state_indicators',[]),
      "adapter_indicators": fam0.get('adapter_indicators',[]),
      "false_positive_killers": fam0.get('false_positive_killers',[]),
      "fix_pattern": fam0.get('local_defensive_property',''),
      "family_candidates": fams,
      "slowmist_attack_method_label_NOT_USED_FOR_CLUSTERING": r['slowmist_attack_method'],
      "source_urls": r['reference_urls'],
      "reference_retrieval": [{"url":x['url'],"status":x['status'],"sha256":x['sha256'],
                               "snapshot":x['snapshot']} for x in refs_by_inc[iid]],
    }

inc, prov, exc = [], [], []
for iid, d in C.T.items():
    if d[0] == 'INCLUDE': inc.append(rec(iid))
    elif d[0] == 'PROVISIONAL': prov.append(rec(iid))
    else:
        r = raw[iid]
        exc.append({"incident_id":iid,"event_date":r['event_date'],"target":r['target'],
          "gate_result":"EXCLUDE","exclusion_reason_code":d[2],
          "exclusion_reason":C.EXC[d[2]],
          "excluded_component":r['description_raw'],
          "included_component":("none - no independent on-chain defect established"
              if d[2]!='PATTERN_EXC_GRADE_D' else
              "gate passed (on-chain defect) but mechanism unsupported; excluded from pattern derivation only"),
          "slowmist_attack_method":r['slowmist_attack_method'],
          "reported_loss_usd":r['reported_loss_usd'],"source_urls":r['reference_urls']})

for name, rows in (('included',inc),('provisional',prov),('excluded',exc)):
    with open(f'{B}/incidents/{name}.jsonl','w') as fh:
        for x in sorted(rows,key=lambda z:z['event_date'],reverse=True):
            fh.write(json.dumps(x,ensure_ascii=False)+"\n")

# ---- duplicate groups / clone lineages ----
dup = {
 "schema":"Groups of rows describing the same event, and clone/repeat lineages sharing one root cause.",
 "same_event_duplicate_rows": [],
 "note_no_duplicate_rows":"No two SlowMist rows in the window describe the same event; each row is a distinct incident.",
 "clone_and_repeat_lineages":[
  {"lineage_id":"LIN-VERUS-IMPORT","incident_ids":["INC-2026-05-18-VER","INC-2026-07-23-VER"],
   "type":"REPEAT_SAME_UNREMEDIATED_ROOT_CAUSE","unique_root_causes":1,
   "note":"Same checkCCEValues value-equality gap exploited twice; the flaw was not patched between May and July and reserves were redeposited on 8 July. Counts once toward unique root causes and toward family recurrence."},
  {"lineage_id":"LIN-DN404-BT404","incident_ids":["INC-2026-06-08-FLO","INC-2026-06-09-AST"],
   "type":"FORK_CLONE_SHARED_CODEBASE","unique_root_causes":1,
   "note":"Asterix Labs is a Flooring Protocol fork; both were hit through the same shared DN404/BT404 packed-ownership defect one day apart. One root cause, two deployments."},
  {"lineage_id":"LIN-AZTEC-DEPRECATED","incident_ids":["INC-2026-06-14-AZT","INC-2026-06-17-AZT"],
   "type":"SAME_ORG_DISTINCT_DEFECTS","unique_root_causes":2,
   "note":"Two different deprecated Aztec deployments (Connect Router; Private Rollup Bridge escape hatch) with distinct defects. Counted separately, but they share the deprecation precondition."},
  {"lineage_id":"LIN-COMPUTILITY","incident_ids":["INC-2026-04-07-TGA","INC-2026-05-29-YSD"],
   "type":"SAME_OPERATOR_TEMPLATE","unique_root_causes":1,
   "note":"Both Computility-associated BSC projects using the same reserve-manipulation template. One code lineage."},
  {"lineage_id":"LIN-THETANUTS","incident_ids":["INC-2026-04-20-THE","INC-2026-06-15-THE"],
   "type":"SAME_PROTOCOL_DISTINCT_DEFECTS","unique_root_causes":2,
   "note":"Same protocol, different vaults and different mechanisms (first-depositor inflation; legacy redemption math). Counted separately."},
  {"lineage_id":"LIN-BSC-DEFERRED-BURN-TEMPLATE",
   "incident_ids":["INC-2026-06-04-BYT","INC-2026-04-13-MON","INC-2026-04-02-SAS","INC-2026-04-04-BSC",
                   "INC-2026-05-26-SKP","INC-2026-03-10-MTW","INC-2026-03-12-AMU","INC-2026-03-23-BCE",
                   "INC-2026-06-20-LAB","INC-2026-06-17-LIT","INC-2026-04-07-TGA","INC-2026-06-19-JBX",
                   "INC-2026-04-28-JUD","INC-2026-07-28-LUL"],
   "type":"TEMPLATE_PROPAGATION_INDEPENDENT_DEPLOYMENTS","unique_root_causes":13,
   "note":"Independent token deployments reimplementing the same deferred-burn/pair-desync template rather than forking one codebase. Counted as independent root causes except the Computility pair, but the recurrence multiplier is capped because they share a template rather than representing 13 independent discoveries."}],
}
json.dump(dup, open(f'{B}/incidents/duplicate_groups.json','w'), indent=2)

# ---- families.json ----
fam_out = []
for fid, f in FAM.items():
    ids  = [i for i,d in C.T.items() if d[0]=='INCLUDE'      and fid in d[3]]
    pids = [i for i,d in C.T.items() if d[0]=='PROVISIONAL'  and fid in d[3]]
    # unique root causes: collapse lineages that share one root cause
    collapse = {frozenset(["INC-2026-05-18-VER","INC-2026-07-23-VER"]),
                frozenset(["INC-2026-06-08-FLO","INC-2026-06-09-AST"]),
                frozenset(["INC-2026-04-07-TGA","INC-2026-05-29-YSD"])}
    urc = len(ids)
    for grp in collapse:
        n = len(grp & set(ids))
        if n > 1: urc -= (n-1)
    loss = sum(raw[i]['reported_loss_usd'] or 0 for i in ids)
    o = {"family_id":fid, "title":f['title'], "broken_invariant":f['broken_invariant'],
         "mechanism":f['mechanism'],
         "mandatory_preconditions":f['mandatory_preconditions'],
         "optional_amplifiers":f['optional_amplifiers'],
         "applicable_protocol_archetypes":f['applicable_protocol_archetypes'],
         "static_indicators":f['static_indicators'],
         "adapter_indicators":f['adapter_indicators'],
         "runtime_state_indicators":f['runtime_state_indicators'],
         "cross_contract_indicators":f['cross_contract_indicators'],
         "decisive_guards":f['decisive_guards'],
         "false_positive_killers":f['false_positive_killers'],
         "local_defensive_property":f['local_defensive_property'],
         "recommended_audit_questions":f.get('recommended_audit_questions',
             ["Is every mandatory precondition present in the live deployment?",
              "Is any decisive guard present in the deployed bytecode, not just the repository?",
              "What live value, authority or approval is reachable through this path?",
              "What single observation would falsify the hypothesis?"]),
         "incident_ids":sorted(ids,reverse=True),
         "provisional_incident_ids":sorted(pids,reverse=True),
         "unique_root_cause_count":urc, "incident_count":len(ids),
         "six_month_loss_usd":round(loss,2) if loss else None,
         "most_recent_event":max([raw[i]['event_date'] for i in ids], default=None),
         "evidence_strength":f['evidence_strength'],
         **({"derivation":f['derivation']} if f.get('derivation') else {}),
         "propagation_notes":f['propagation_notes']}
    if len(ids) == 1: o["single_event_family"] = "SINGLE_EVENT_FAMILY"
    fam_out.append(o)
fam_out.sort(key=lambda x:(-x['incident_count'], -(x['six_month_loss_usd'] or 0)))
json.dump(fam_out, open(f'{B}/families/families.json','w'), indent=2, ensure_ascii=False)

# ---- guard_library.jsonl ----
with open(f'{B}/families/guard_library.jsonl','w') as fh:
    for f in fam_out:
        for g in f['decisive_guards']:
            fh.write(json.dumps({
              "family_id":f['family_id'],
              "guard_type":("code-invariant" if any(k in g.lower() for k in ("assert","invariant","require","property"))
                            else "configuration" if any(k in g.lower() for k in ("cap","timelock","registry","allowlist","bound"))
                            else "architectural"),
              "guard_description":g,
              "evidence_pattern":"; ".join(f['static_indicators'][:3]) or "n/a",
              "why_it_closes_the_mechanism":f['broken_invariant'],
              "limitations":["Presence in a repository does not establish presence in deployed bytecode",
                             "A guard on one path does not cover sibling paths reaching the same state",
                             "Configuration guards can be changed by whoever holds the setter role"],
              "source":"derived from incidents "+", ".join(f['incident_ids'][:4])},ensure_ascii=False)+"\n")

print(json.dumps({"included":len(inc),"provisional":len(prov),"excluded":len(exc),
  "families":len(fam_out),
  "single_event_families":sum(1 for f in fam_out if f.get('single_event_family')),
  "guards":sum(len(f['decisive_guards']) for f in fam_out),
  "total_included_loss_usd":round(sum(x['reported_loss_usd'] or 0 for x in inc),2),
  "unique_root_causes":sum(f['unique_root_cause_count'] for f in fam_out)},indent=2))
