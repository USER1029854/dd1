#!/usr/bin/env python3
"""Phase 13-16: two rankings, near-miss library, candidate reports, handoff file."""
import json,sys,csv,collections,datetime
sys.path.insert(0,'/home/user/dd1/incident-intelligence/tools')
B='/home/user/dd1/incident-intelligence'
D=[json.loads(l) for l in open(f'{B}/protocols/deep_screened.jsonl')]
FAM={f['family_id']:f for f in json.load(open(f'{B}/families/families.json'))}
E={r['slug']:r for r in json.load(open(f'{B}/protocols/eligibility.json'))}
AD=json.load(open(f'{B}/protocols/adapters_index.json'))
PR=json.load(open(f'{B}/protocols/onchain_probes.json'))
PRIOR=json.load(open(f'{B}/protocols/prior_art.json')) if __import__('os').path.exists(f'{B}/protocols/prior_art.json') else {}
N=json.load(open(f'{B}/run_config.json'))['operational_settings']['final_candidate_count']
live=[o for o in D if not o['killed']]
killed=[o for o in D if o['killed']]

# ---------------- near-miss library ----------------
with open(f'{B}/families/near_miss_library.jsonl','w') as fh:
    for o in killed:
        fh.write(json.dumps({
          "protocol_slug":o['protocol_slug'],"family_id":o['family_id'],
          "initial_similarity":o['priority_evidence'],
          "decisive_guard":(", ".join(o.get('guards_found',[])) if o.get('kill_reason')=='DECISIVE_GUARD_FOUND'
                            else "n/a - killed by precondition, not by a guard"),
          "guard_evidence":o.get('notes',[]),
          "killed_conditions":o.get('killed_conditions',[]),
          "remaining_uncertainty":"; ".join(sorted({k for k,v in {**o.get('code',{}),**o.get('state',{})}.items() if v=='UNKNOWN'}))
                                 or "none recorded",
          "disposition":("PARTIAL" if (o.get('kill_reason')=='DECISIVE_GUARD_FOUND'
                          and (PRIOR.get(f"{o['protocol_slug']}|{o['family_id']}",{}).get('downgrade') or {}).get('disposition')=='PARTIAL')
                          else "KILLED"),
          "kill_reason":o.get('kill_reason')},ensure_ascii=False)+"\n")

# ---------------- rankings ----------------
byA=sorted(live,key=lambda x:(-x['MATCH_SCORE'],-x['PREVENTION_SCORE']))
byB=sorted(live,key=lambda x:(-x['PREVENTION_SCORE'],-x['MATCH_SCORE']))
# final candidate set: union of the two top-N lists, capped at N by best rank
rankA={ (o['protocol_slug'],o['family_id']):i+1 for i,o in enumerate(byA) }
rankB={ (o['protocol_slug'],o['family_id']):i+1 for i,o in enumerate(byB) }
def bestrank(o):
    k=(o['protocol_slug'],o['family_id']); return min(rankA[k],rankB[k])
# one entry per protocol (best-scoring family), then take N
per={}
for o in sorted(live,key=lambda x:(bestrank(x))):
    per.setdefault(o['protocol_slug'],o)
finals=sorted(per.values(),key=bestrank)[:N]

def prior_art(o):
    k=f"{o['protocol_slug']}|{o['family_id']}"
    if k in PRIOR: return PRIOR[k]
    fid=o['family_id']
    if fid=='ACC-DONATION-UNACCOUNTED-BALANCE' and (o.get('forked_from') or
        (PR.get(o['protocol_slug'],{}).get('compound',{}).get('registry_key'))):
        return {"status":"KNOWN_ISSUE_DEPLOYMENT_STATUS_UNKNOWN",
                "basis":"The Compound-fork donation/exchange-rate vector is publicly documented and was raised in "
                        "Venus's own Code4rena audit before the March 2026 THE-market exploit. Whether THIS deployment "
                        "carries a fix is not established by the read-only evidence collected here.",
                "search_scope":"family-level public prior art only; per-deployment audit-competition and advisory search NOT performed"}
    return {"status":"PRIOR_ART_SEARCH_INCOMPLETE",
            "basis":"No per-deployment search of published audits, audit competitions, upstream advisories, postmortems "
                    "and relevant forks was performed for this pair. Novelty is therefore NOT claimed and "
                    "NO_PUBLIC_MATCH_FOUND is deliberately not used.",
            "search_scope":"none performed for this pair"}

def block(o,rank,which):
    p=E.get(o['protocol_slug'],{}); f=FAM[o['family_id']]
    pa=prior_art(o)
    cs={**o.get('code',{}),**o.get('state',{})}
    pres=[k for k,v in cs.items() if v=='PRESENT']; unk=[k for k,v in cs.items() if v=='UNKNOWN']
    gs=o.get('guards',{})
    L=[]
    L.append(f"### {rank}. {o['protocol_name']}  —  `{o['family_id']}`\n")
    L.append(f"- **Rank ({which}):** {rank}")
    L.append(f"- **Protocol:** {o['protocol_name']} (`{o['protocol_slug']}`)")
    L.append(f"- **DefiLlama URL:** {o['defillama_url']}")
    L.append(f"- **Current TVL:** ${o['tvl']:,.0f}")
    L.append(f"- **Chains:** {', '.join(o['chains'][:8])}{' …' if len(o['chains'])>8 else ''}")
    L.append(f"- **Category:** {o['category']}")
    L.append(f"- **Matched family IDs:** `{o['family_id']}`"+
             (f" (other pairs generated for this protocol: "+", ".join(sorted({x['family_id'] for x in live
               if x['protocol_slug']==o['protocol_slug'] and x['family_id']!=o['family_id']}))+")" if any(
               x['protocol_slug']==o['protocol_slug'] and x['family_id']!=o['family_id'] for x in live) else ""))
    L.append("- **Ranking:**")
    L.append(f"    - MATCH_SCORE: **{o['MATCH_SCORE']}** / 100")
    L.append(f"    - EVIDENCE_CONFIDENCE: **{o['EVIDENCE_CONFIDENCE']}** / 100 "
             f"(mapping {o['evidence_confidence_components']['mapping_completeness']}, "
             f"deployment parity {o['evidence_confidence_components']['deployment_parity_confidence']}, "
             f"live state {o['evidence_confidence_components']['live_state_completeness']}, "
             f"corroboration {o['evidence_confidence_components']['source_corroboration']}, "
             f"guard review {o['evidence_confidence_components']['guard_review_depth']})")
    L.append(f"    - PREVENTION_SCORE: **{o['PREVENTION_SCORE']}** "
             f"= MATCH {o['MATCH_SCORE']} × CONF {o['EVIDENCE_CONFIDENCE']}/100 × EXPOSURE {o['EXPOSURE_INDEX']} "
             f"× RECENCY {o['FAMILY_RECENCY_FACTOR']} × RECURRENCE {o['RECURRENCE_MULTIPLIER']}")
    L.append(f"- **Evidence level:** `{o['evidence_level']}`")
    L.append(f"- **Why the family applies:** {f['broken_invariant']}")
    L.append(f"    - Screening evidence: {'; '.join(o['priority_evidence'][:5])}")
    if o.get('notes'): L.append(f"    - Deep-screen observations: {'; '.join(o['notes'])}")
    L.append(f"- **Mandatory preconditions PRESENT:** {', '.join(pres) if pres else 'none confirmed'}")
    L.append(f"- **Mandatory preconditions UNKNOWN:** {', '.join(unk) if unk else 'none'}")
    L.append(f"- **Decisive guards searched:** {', '.join(gs.keys()) if gs else 'none reachable at this evidence level'}")
    L.append(f"- **Decisive guards found:** {', '.join([k for k,v in gs.items() if v=='FOUND']) or 'none found in the reviewed path'}")
    L.append(f"- **Live value / authority / approval relevance:** exposure basis ${o['exposure_basis_usd']:,.0f}"
             + ("; "+"; ".join(o['authority_notes']) if o.get('authority_notes') else ""))
    dep=PR.get(o['protocol_slug'],{}).get('deployment',{})
    pp=PR.get(o['protocol_slug'],{})
    probe_bits=[]
    if pp.get('compound',{}).get('markets'): probe_bits.append(f"{len(pp['compound']['markets'])} lending market(s) read on-chain")
    if pp.get('aave',{}).get('providers'):   probe_bits.append(f"{len(pp['aave']['providers'])} addresses-provider(s) read")
    if pp.get('curator',{}).get('vault_reads'): probe_bits.append(f"{len(pp['curator']['vault_reads'])} curated vault(s) read")
    if dep.get('addresses_probed'):          probe_bits.append(f"{len(dep['addresses_probed'])} adapter address(es) probed")
    if pp.get('compound',{}).get('implementation_review'):
        probe_bits.append(f"{len(pp['compound']['implementation_review'])} proxy implementation(s) resolved and reviewed")
    L.append(f"- **Implementation and deployment status:** adapter `{AD.get(o['protocol_slug'],{}).get('module','n/a')}` "
             f"({AD.get(o['protocol_slug'],{}).get('status','n/a')}); "
             f"{'; '.join(probe_bits) if probe_bits else 'no live code reachable at the adapter addresses'}; "
             f"{'deprecated flag set' if p.get('_deprecated') else 'not flagged deprecated'}; "
             f"{'no audit link listed' if not p.get('_audit_links') else str(len(p.get('_audit_links')))+' audit link(s) listed'}")
    L.append(f"- **Prior-art status:** `{pa['status']}` — {pa['basis']} (search scope: {pa['search_scope']})")
    L.append(f"- **What would falsify the hypothesis:** "+ "; ".join(f['false_positive_killers'][:3]))
    L.append(f"- **Recommended audit focus:** {f['local_defensive_property']}")
    L.append(f"    - Questions: "+" · ".join(f['recommended_audit_questions'][:3]))
    ev=[f"protocols/deep_screened.jsonl#{o['protocol_slug']}|{o['family_id']}",
        f"protocols/adapters_index.json#{o['protocol_slug']}",
        f"protocols/onchain_probes.json#{o['protocol_slug']}",
        f"families/families.json#{o['family_id']}"]
    sn=AD.get(o['protocol_slug'],{}).get('snapshot')
    if sn: ev.append(f"sources/defillama/adapters/{sn}")
    L.append(f"- **Evidence paths:** "+", ".join(f"`{x}`" for x in ev))
    L.append(f"- **Responsible disclosure channel, if public:** {p.get('url') or 'not listed in DefiLlama metadata'}"
             + (f" · audits: {', '.join(p.get('_audit_links',[])[:2])}" if p.get('_audit_links') else ""))
    L.append("")
    return "\n".join(L)

HDR=("> **Discovery-stage output.** This file asserts no defect in any protocol named below. Each entry is a "
     "*high-priority defensive audit candidate*: evidence A, B and C match a family's prerequisites, evidence D "
     "remains unknown, and guard E would falsify the hypothesis. Every entry requires separate authorized "
     "verification in a local or pinned-fork environment before any conclusion is drawn. Selection here is a "
     "statement about where to look next, not about what will be found.\n")
for fn,order,which in ((f'{B}/results/candidates_by_match.md',byA,'Ranking A — mechanism match'),
                       (f'{B}/results/candidates_by_prevention.md',byB,'Ranking B — expected loss prevention')):
    seen=set(); out=[f"# Candidates — {which}\n",HDR]
    if 'Ranking A' in which:
        out.append("Ranking A answers: *which current protocols most strongly exhibit the observable prerequisites "
                   "of the recent vulnerability families?* It deliberately ignores size.\n")
    else:
        out.append("Ranking B answers: *where could a focused audit plausibly prevent the most loss?* It multiplies "
                   "technical fit by evidence confidence, live exposure, family recency and a capped recurrence "
                   "multiplier. It is a prioritisation heuristic, not a probability.\n")
    n=0
    for o in order:
        if o['protocol_slug'] in seen: continue
        seen.add(o['protocol_slug']); n+=1
        out.append(block(o,n,which))
        if n>=N: break
    open(fn,'w').write("\n".join(out))

# ---------------- CSV ----------------
with open(f'{B}/results/candidates_all.csv','w',newline='') as fh:
    w=csv.writer(fh)
    w.writerow(["rank_match","rank_prevention","protocol_slug","protocol_name","defillama_url","category",
                "chains","tvl_usd","family_id","MATCH_SCORE","EVIDENCE_CONFIDENCE","PREVENTION_SCORE",
                "EXPOSURE_INDEX","FAMILY_RECENCY_FACTOR","RECURRENCE_MULTIPLIER","evidence_level",
                "preconditions_present","preconditions_unknown","guards_searched","guards_found",
                "prior_art_status","in_final_20","deprecated","forked_from","adapter_status"])
    finalset={(o['protocol_slug'],o['family_id']) for o in finals}
    for o in byA:
        k=(o['protocol_slug'],o['family_id']); cs={**o.get('code',{}),**o.get('state',{})}
        w.writerow([rankA[k],rankB[k],o['protocol_slug'],o['protocol_name'],o['defillama_url'],o['category'],
          "|".join(o['chains'][:6]),round(o['tvl'],2),o['family_id'],o['MATCH_SCORE'],o['EVIDENCE_CONFIDENCE'],
          o['PREVENTION_SCORE'],o['EXPOSURE_INDEX'],o['FAMILY_RECENCY_FACTOR'],o['RECURRENCE_MULTIPLIER'],
          o['evidence_level'],
          "|".join(k2 for k2,v in cs.items() if v=='PRESENT'),
          "|".join(k2 for k2,v in cs.items() if v=='UNKNOWN'),
          "|".join(o.get('guards',{}).keys()),
          "|".join(k2 for k2,v in o.get('guards',{}).items() if v=='FOUND'),
          prior_art(o)['status'], "YES" if k in finalset else "NO",
          o.get('deprecated'), "|".join(o.get('forked_from',[])),
          AD.get(o['protocol_slug'],{}).get('status','')])

# ---------------- audit_variables.txt ----------------
def one_line(s): return " ".join(str(s).replace("|"," / ").replace("\n"," ").split())
with open(f'{B}/results/audit_variables.txt','w') as fh:
    for o in finals:
        f=FAM[o['family_id']]
        fams=sorted({x['family_id'] for x in live if x['protocol_slug']==o['protocol_slug']})
        hyp=one_line(f['broken_invariant'])[:400]
        guards=one_line("; ".join(f['false_positive_killers'][:3]))[:300]
        ev=f"protocols/deep_screened.jsonl#{o['protocol_slug']} , protocols/adapters_index.json#{o['protocol_slug']} , protocols/onchain_probes.json#{o['protocol_slug']} , families/families.json#{o['family_id']}"
        fh.write(f"TARGET={o['defillama_url']} || PATTERN_IDS={','.join(fams)} || "
                 f"PRIORITY_HYPOTHESES={hyp} || MATCH_EVIDENCE={one_line(ev)} || "
                 f"REQUIRED_GUARD_CHECKS={guards} || PINNED_CHAINS={','.join(o['chains'][:6])} || "
                 f"PRIOR_ART_STATUS={prior_art(o)['status']}\n")

# ---------------- excluded_protocols.md ----------------
elig=json.load(open(f'{B}/protocols/eligibility.json'))
cnt=collections.Counter(r['_eligibility_reason'] for r in elig if not r['_eligible'])
L=["# Excluded protocols and killed protocol-family pairs\n",
   "Exclusion here means *not carried into candidate ranking*. It is **never** a statement that a protocol is safe.\n",
   "## 1. Universe-level exclusions (Phase F eligibility)\n",
   "| Reason | Protocols |","|---|---:|"]
for k,v in cnt.most_common(): L.append(f"| `{k}` | {v} |")
L.append(f"\nOf the {sum(1 for r in elig if r['_eligibility_reason']=='BELOW_TVL_THRESHOLD')} protocols below the "
         f"$1,000,000 TVL threshold, "
         f"{sum(1 for r in elig if r['_queue']=='HIGH_FIT_SUBTHRESHOLD')} were preserved in the sub-threshold "
         "high-fit queue because they are deprecated, hold authority over external value, curate third-party vaults, "
         "operate routers that hold user approvals, or carry on-chain governance authority. TVL is not equated with "
         "total value at risk.\n")
L.append("## 2. Pairs killed at the mandatory-precondition gate\n")
L.append("| Protocol | Family | Kill reason | Condition proven absent / guard found |")
L.append("|---|---|---|---|")
for o in sorted(killed,key=lambda x:x['protocol_slug'])[:400]:
    det=", ".join(o.get('killed_conditions',[]) or o.get('guards_found',[])) or "-"
    L.append(f"| `{o['protocol_slug']}` | `{o['family_id']}` | {o['kill_reason']} | {det} |")
L.append("\nEvery killed pair is written in full to `families/near_miss_library.jsonl` with its initial similarity, "
         "the decisive guard or absent precondition, and the uncertainty that remains. Near misses are first-class "
         "results: they are what make the next pass more precise.\n")
L.append("## 3. Families with no addressable population in this universe\n")
NS=json.load(open(f'{B}/protocols/families_not_screenable_in_universe.json'))
L.append("| Family | Incidents | Why no protocol-family pair was generated |")
L.append("|---|---:|---|")
for k,v in sorted(NS.items(),key=lambda x:-x[1]['family_incident_count']):
    L.append(f"| `{k}` | {v['family_incident_count']} | {v['reason']} |")
open(f'{B}/results/excluded_protocols.md','w').write("\n".join(L)+"\n")

print(json.dumps({"live_pairs":len(live),"killed_pairs":len(killed),"finals":len(finals),
 "final_slugs":[o['protocol_slug'] for o in finals],
 "levels":collections.Counter(o['evidence_level'] for o in finals)},indent=2))
