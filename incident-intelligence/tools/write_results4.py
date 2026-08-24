#!/usr/bin/env python3
"""Candidate reports for v4: likelihood, actionability and priority kept distinct."""
import json,sys,os,csv,collections
sys.path.insert(0,'/home/user/dd1/incident-intelligence/tools')
import attack_surface as AS
B='/home/user/dd1/incident-intelligence'
D=[json.loads(l) for l in open(f'{B}/protocols/deep_screened.jsonl')]
FAM={f['family_id']:f for f in json.load(open(f'{B}/families/families.json'))}
E={r['slug']:r for r in json.load(open(f'{B}/protocols/eligibility.json'))}
AD=json.load(open(f'{B}/protocols/adapters_index.json'))
PR=json.load(open(f'{B}/protocols/onchain_probes.json'))
PRIOR=json.load(open(f'{B}/protocols/prior_art.json')) if os.path.exists(f'{B}/protocols/prior_art.json') else {}
AUTH={r['slug']:r for r in json.load(open(f'{B}/protocols/authority_exposure.json'))} \
      if os.path.exists(f'{B}/protocols/authority_exposure.json') else {}
ABL=json.load(open(f'{B}/protocols/ablation.json')) if os.path.exists(f'{B}/protocols/ablation.json') else {}
AUTHDESC={'EOA_SINGLE_KEY':'one externally-owned account','SAFE_1_OF_N':'a Safe with threshold 1',
          'SAFE_M_OF_N':'a Safe requiring several signatures','TIMELOCK':'a timelock with a real delay',
          'TIMELOCK_ZERO_DELAY':'a timelock with zero delay','GOVERNOR':'an on-chain governor',
          'UNKNOWN_CONTRACT':'a contract not fingerprinted by this run',
          'NONE_FOUND':'no authority slot or owner() exposed'}
BT=json.load(open(f'{B}/protocols/learned_weights.json')) if os.path.exists(f'{B}/protocols/learned_weights.json') else {}
# A candidate list is work to be done, not a leaderboard. Anything handed over in a
# previous run is withheld here, so every run delivers protocols the operator has not
# already been given. The ledger is reconstructed from git history by
# tools/build_ledger.py and is cumulative across runs.
_LED=json.load(open(f'{B}/protocols/delivered_ledger.json')) if os.path.exists(f'{B}/protocols/delivered_ledger.json') else {"ledger":{},"runs":[]}
DELIVERED=set(_LED.get('ledger',{}))
PAST_RUNS=_LED.get('runs',[])
live_all=[o for o in D if not o['killed']]; killed=[o for o in D if o['killed']]
live=[o for o in live_all if o['protocol_slug'] not in DELIVERED]
WITHHELD=sorted({o['protocol_slug'] for o in live_all if o['protocol_slug'] in DELIVERED})
N=int(sys.argv[1]) if len(sys.argv)>1 else 60

def _by_date_desc(hs):
    """DefiLlama lists incidents oldest-first; every 'most recent' claim needs this."""
    return sorted(hs or [],key=lambda h:h.get('date') or '',reverse=True)

def prior_art(o):
    k=f"{o['protocol_slug']}|{o['family_id']}"
    if k in PRIOR: return PRIOR[k]
    if o.get('prior_hacks'):
        h=_by_date_desc(o['prior_hacks'])[0]
        return {"status":"UNREMEDIATED_KNOWN_ISSUE" if (o.get('repeat_victim_count') or 0)>1
                          else "KNOWN_ISSUE_DEPLOYMENT_STATUS_UNKNOWN",
                "basis":(f"DefiLlama's hacks dataset records {len(o['prior_hacks'])} prior on-chain incident(s) on "
                         f"this protocol, most recently {h.get('date')} for ${h.get('amount') or 0:,.0f} "
                         f"[{h.get('technique')}]. Whether the deployment in scope carries the fix is not "
                         f"established by read-only evidence."),
                "search_scope":"DefiLlama hacks dataset only; no per-deployment advisory search"}
    if o['family_id']=='ACC-DONATION-UNACCOUNTED-BALANCE' and o.get('forked_from'):
        return {"status":"KNOWN_ISSUE_DEPLOYMENT_STATUS_UNKNOWN",
                "basis":"The Compound-fork donation vector is publicly documented and was raised in Venus's own "
                        "Code4rena audit before the March 2026 exploit.",
                "search_scope":"family-level public prior art only"}
    return {"status":"PRIOR_ART_SEARCH_INCOMPLETE",
            "basis":"No per-deployment search of published audits, competitions, advisories and postmortems was "
                    "performed. Novelty is therefore NOT claimed.","search_scope":"none performed for this pair"}

def block(o,rank,which):
    p=E.get(o['protocol_slug'],{}); f=FAM[o['family_id']]; pa=prior_art(o)
    cs={**o.get('code',{}),**o.get('state',{})}
    pres=[k for k,v in cs.items() if v=='PRESENT']; unk=[k for k,v in cs.items() if v=='UNKNOWN']
    gs=o.get('guards',{}); lc=o.get('likelihood_components',{})
    L=[]
    L.append("### %d. %s  —  `%s`\n" % (rank,o['protocol_name'],o['family_id']))
    L.append("- **Rank (%s):** %d" % (which,rank))
    L.append("- **Protocol:** %s (`%s`) · %s · %s" % (o['protocol_name'],o['protocol_slug'],o['category'],
             ", ".join(o['chains'][:6])+(" …" if len(o['chains'])>6 else "")))
    L.append("- **DefiLlama:** %s" % o['defillama_url'])
    L.append("- **PRIORITY %s**  =  LIKELIHOOD %s × ACTIONABILITY %s%%" %
             (o.get('PRIORITY'),o.get('LIKELIHOOD'),o.get('ACTIONABILITY')))
    L.append("    - likelihood = family evidence %s/50 (MATCH %s × evidence weight %s) + learned attack surface %s/50"
             % (lc.get('family_evidence'),o['MATCH_SCORE'],lc.get('evidence_level_weight'),
                lc.get('learned_attack_surface')))
    L.append("    - actionability: %s" % o.get('actionability_reason'))
    L.append("- **Value at risk:** $%s · **Band:** `%s`" % (f"{o['tvl']:,.0f}",o.get('band_status')))
    if (o.get('repeat_victim_count') or 0)>1:
        L.append("- **REPEAT VICTIM — %d recorded hacks.** %s" % (o['repeat_victim_count'],
                 "; ".join("%s $%s [%s]" % (h.get('date'),f"{h.get('amount') or 0:,.0f}",h.get('technique'))
                           for h in _by_date_desc(o.get('prior_hacks'))[:4])))
    elif o.get('prior_hacks'):
        h=_by_date_desc(o['prior_hacks'])[0]
        L.append("- **Previously hacked:** %s for $%s [%s]" % (h.get('date'),f"{h.get('amount') or 0:,.0f}",h.get('technique')))
    L.append("- **Evidence level:** `%s` · MATCH %s · CONFIDENCE %s" %
             (o['evidence_level'],o['MATCH_SCORE'],o['EVIDENCE_CONFIDENCE']))
    L.append("- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):")
    for s in (o.get('surface_signals') or [])[:8]:
        L.append("    - `%s` — %s, measured lift ×%s (weight %+.2f)" %
                 (s['signal'],s['direction'],s.get('measured_lift'),s['weight']))
    if not o.get('surface_signals'): L.append("    - none carried")
    L.append("- **Broken invariant tested:** %s" % f['broken_invariant'])
    if o.get('conditions'): L.append("    - Conditions: "+", ".join("`%s`" % c for c in o['conditions']))
    ss=PR.get(o['protocol_slug'],{}).get('source_sweep',{})
    sig=(ss.get('family_signals') or {}).get(o['family_id']) or {}
    if sig:
        ver=[c for c in ss.get('contracts',[]) if c.get('status')=='VERIFIED']
        pre=[k for k,h in sig.items() if h['match'] and h['role']=='PRE']
        gd=[k for k,h in sig.items() if h['match'] and h['role']=='GUARD']
        where=", ".join("`%s` @ %s(%s)" % (c.get('name'),c['address'][:10]+'…',c['chain']) for c in ver[:2]) or "no verified contract"
        L.append("    - Deployed source (%s): %s%s" % (where,
                 ("prerequisites matched: "+", ".join(pre)) if pre else "no prerequisite matched",
                 ("; guards found: "+", ".join(gd)) if gd else "; no guard found"))
    for n in (o.get('notes') or [])[:3]: L.append("    - %s" % n)
    L.append("- **Preconditions PRESENT / UNKNOWN:** %s / %s" % (", ".join(pres) or "none", ", ".join(unk) or "none"))
    L.append("- **Guards searched / found:** %s / %s" % (", ".join(gs.keys()) or "none",
             ", ".join(k for k,v in gs.items() if v=='FOUND') or "none in the reviewed path"))
    a=AUTH.get(o['protocol_slug'])
    if a and a.get('posture'):
        up=a.get('upgrade_authority_posture')
        line="- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** "
        if up:
            line+="the ERC-1967 upgrade authority terminates in **%s** (`%s`)" % (AUTHDESC.get(up,up),up)
            if up in ('EOA_SINGLE_KEY','SAFE_1_OF_N'):
                line+=" — a code fix here does not remove that exposure, and it is the cheaper thing to raise first"
        else:
            line+="weakest privileged role reads as `%s`; no ERC-1967 admin chain was proven" % a['posture']
        L.append(line)
    if o.get('operational_flags'):
        L.append("- **Operational flags** (not fitted — today's values partly reflect an incident's own "
                 "aftermath, so they order but never score): %s" % ", ".join("`%s`" % x for x in o['operational_flags']))
    L.append("- **Prior art:** `%s` — %s" % (pa['status'],pa['basis']))
    L.append("- **Falsified by:** %s" % "; ".join(f['false_positive_killers'][:3]))
    L.append("- **Where to start:** %s" % f['local_defensive_property'])
    L.append("- **Evidence:** `protocols/deep_screened.jsonl#%s|%s`, `protocols/onchain_probes.json#%s`" %
             (o['protocol_slug'],o['family_id'],o['protocol_slug']))
    L.append("- **Disclosure:** %s%s" % (p.get('url') or 'not listed',
             (" · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork "
              "lineages they sometimes point at a sibling protocol): "+", ".join(p.get('_audit_links',[])[:2]))
             if p.get('_audit_links') else " · no audit link listed"))
    L.append("")
    return "\n".join(L)

v=BT.get('out_of_sample_unseen') or {}
HDR=("> **Discovery stage.** This file asserts no defect in any protocol named below. Each entry is a "
     "*review candidate*: named evidence matches a family's prerequisites, named evidence is unknown, and a named "
     "guard would falsify it. Verify on a local or pinned fork before concluding anything.\n")
CTX=("**Scoring is now validated, not asserted.** Attack-surface weights were fitted on 2022-24 hacks and tested "
     "against 2025-26 hacks: %d protocols unseen during fitting, median victim landing at the **%sth percentile**, "
     "**%.0f%%** of future victims in the model's top quartile — a **×%s lift** over chance.\n\n"
     "**Likelihood and actionability are kept apart.** Bigger protocols are *more* likely to be attacked "
     "(`tvl_over_5m` carries lift ×1.75) and *less* actionable for an independent reviewer. Folding those together "
     "is what produced earlier rankings full of protocols you cannot help. PRIORITY multiplies them explicitly so "
     "you can see both halves.\n\n"
     "**Exposure age beat every other addition, and it contradicts the obvious intuition.** Protocols under a "
     "year old carry lift ×1.87; protocols over three years old carry ×0.33. It is not the abandoned "
     "deployments that get hit — it is the new ones. Ablation attributes the whole out-of-sample gain to this "
     "one group (×2.19 → ×2.32).\n\n"
     "**Custody posture was measured and then deliberately dropped from the score.** A single-key upgrade "
     "authority does not predict a code defect (measured ×0.98 over the full window; adding it moved "
     "out-of-sample lift ×2.19 → ×2.15, i.e. slightly worse). That is the expected answer, since key "
     "compromise is an excluded root cause here — so it is reported on its own in "
     "`results/upgrade_authority_exposure.md`, where 23 protocols holding $56.4M have an ERC-1967 upgrade "
     "authority terminating in a single key. Often the cheapest thing on this whole list to fix.\n\n"
     "**A finding that overturned the earlier model:** measured against survivors only, neglect looked protective. "
     "It is not — 62.5%% of victims that fell below $50k had no audit, versus 20.9%% of those still listed. The "
     "population was censored by the very outcome being predicted. Weights are now fitted against the full listed "
     "universe.\n" % (v.get('n',0),v.get('median_percentile','?'),(v.get('top_quartile_share') or 0)*100,v.get('lift','?')))

# Ranking A carries the full write-up for every protocol it lists. B and C are
# genuinely different orderings over a heavily overlapping set, so re-rendering the
# same block three times added ~69 duplicate write-ups and no information. They now
# show the complete ranking as a table, a full block for each protocol A does not
# already cover, and a one-line pointer for the rest.
_full_written=set()
for key,fn,title in (('PRIORITY','candidates_by_priority.md','Ranking A — priority (likelihood × actionability)'),
                     ('LIKELIHOOD','candidates_by_likelihood.md','Ranking B — likelihood, ignoring actionability'),
                     ('MATCH_SCORE','candidates_by_match.md','Ranking C — mechanism match only')):
    order=sorted(live,key=lambda x:(-x.get(key,0),-x.get('PRIORITY',0)))
    # HDR is a safety notice and belongs on every file. CTX is the methodology, and
    # it is written once, in Ranking A, which the other two link to.
    _ctx=CTX if key=='PRIORITY' else ("**How these are scored** is set out once, at the top of "
         "[`candidates_by_priority.md`](candidates_by_priority.md): the out-of-sample validation, why "
         "likelihood and actionability are kept apart, and why custody exposure is reported separately.\n")
    seen=set(); out=["# Candidates — %s\n" % title,HDR,_ctx]; n=0; chosen=[]
    for o in order:
        if o['protocol_slug'] in seen: continue
        seen.add(o['protocol_slug']); n+=1; chosen.append(o)
        if n>=N: break
    if key=='PRIORITY':
        rv=[o for o in chosen if (o.get('repeat_victim_count') or 0)>1]
        ph=[o for o in chosen if o.get('prior_hacks')]
        out.append("### At a glance\n")
        out.append("| | |\n|---|---:|")
        out.append("| Candidates | %d |" % len(chosen))
        out.append("| Previously hacked | %d |" % len(ph))
        out.append("| Repeat victims (2+ recorded hacks) | %d |" % len(rv))
        out.append("| Median value at risk | $%s |" % f"{sorted(o['tvl'] for o in chosen)[len(chosen)//2]:,.0f}")
        out.append("| Total value at risk | $%s |" % f"{sum(o['tvl'] for o in chosen):,.0f}")
        out.append("| At L4 guard review | %d |" % sum(1 for o in chosen if o['evidence_level']=='L4_GUARD_REVIEW'))
        out.append("| Previously delivered (withheld from this list) | %d |" % len(WITHHELD))
        out.append("")
        out.append("### Every protocol here is one you have not been given before\n")
        out.append("A candidate list is a queue of work, not a leaderboard. **%d protocols that survive "
                   "screening were withheld from this run because earlier runs already handed them over** "
                   "across %d previous deliveries. They are not resolved and not ruled out — they were "
                   "already given to you, so repeating them would hand you no new work.\n"
                   % (len(WITHHELD),len(PAST_RUNS)))
        if PAST_RUNS:
            out.append("| Previous delivery | Protocols handed over |"); out.append("|---|---:|")
            for r in PAST_RUNS:
                out.append("| `%s` — %s | %d |" % (r['commit'],r['subject'][:64],r['protocols']))
            out.append("")
        out.append("The full ledger is `protocols/delivered_ledger.json`, reconstructed from git history "
                   "rather than from anything remembered between runs. Every withheld protocol still "
                   "appears in `candidates_all.csv` with `previously_delivered=YES` and the run that "
                   "delivered it, so nothing is hidden — it is only kept out of the queue.\n")
        if WITHHELD:
            out.append("<details><summary>The %d withheld protocols</summary>\n" % len(WITHHELD))
            out.append(", ".join("`%s`" % w for w in WITHHELD))
            out.append("\n</details>\n")
        if rv:
            out.append("### Repeat victims in this list\n")
            out.append("Whatever allowed a second incident has not necessarily been removed. These are the "
                       "highest-conviction entries in the set.\n")
            out.append("| Protocol | Hacks | Family | Priority | At risk |"); out.append("|---|---:|---|---:|---:|")
            for o in sorted(rv,key=lambda x:-x['PRIORITY']):
                out.append("| [%s](%s) | %d | `%s` | %s | $%s |" % (o['protocol_name'],o['defillama_url'],
                           o['repeat_victim_count'],o['family_id'],o['PRIORITY'],f"{o['tvl']:,.0f}"))
            out.append("")
        byfam=collections.defaultdict(list)
        for o in order: byfam[o['family_id']].append(o)
        div=[]; seen2=set()
        for fid,lst in sorted(byfam.items(),key=lambda kv:-max(x.get('PRIORITY',0) for x in kv[1])):
            k=0
            for o in lst:
                if o['protocol_slug'] in seen2: continue
                seen2.add(o['protocol_slug']); div.append(o); k+=1
                if k>=3: break
        div.sort(key=lambda x:-x['PRIORITY'])
        out.append("### Diversified shortlist — top 3 per family\n")
        out.append("| # | Protocol | Family | Priority | Likelihood | At risk | Evidence |")
        out.append("|---:|---|---|---:|---:|---:|---|")
        for i,o in enumerate(div[:30],1):
            out.append("| %d | [%s](%s) | `%s` | %s | %s | $%s | `%s` |" % (i,o['protocol_name'],o['defillama_url'],
                       o['family_id'],o['PRIORITY'],o['LIKELIHOOD'],f"{o['tvl']:,.0f}",o['evidence_level']))
        out.append("\n---\n")
    if key!='PRIORITY':
        dup=[o for o in chosen if o['protocol_slug'] in _full_written]
        out.append("### The ranking\n")
        out.append("Full write-ups below for the %d entries that `candidates_by_priority.md` does not already "
                   "cover; the other %d are listed here and written up in full there, under the same "
                   "`protocol — family` heading.\n" % (len(chosen)-len(dup),len(dup)))
        out.append("| # | Protocol | Family | %s | At risk | Write-up |" % key)
        out.append("|---:|---|---|---:|---:|---|")
        for i,o in enumerate(chosen,1):
            where=("[in `candidates_by_priority.md`](candidates_by_priority.md)"
                   if o['protocol_slug'] in _full_written else "below")
            out.append("| %d | [%s](%s) | `%s` | %s | $%s | %s |" % (i,o['protocol_name'],o['defillama_url'],
                       o['family_id'],o.get(key),f"{o['tvl']:,.0f}",where))
        out.append("\n---\n")
    for i,o in enumerate(chosen,1):
        if key!='PRIORITY' and o['protocol_slug'] in _full_written: continue
        out.append(block(o,i,title))
    _full_written.update(o['protocol_slug'] for o in chosen)
    open(f'{B}/results/{fn}','w').write("\n".join(out))

with open(f'{B}/results/candidates_all.csv','w',newline='') as fh:
    w=csv.writer(fh)
    w.writerow(["rank_priority","protocol_slug","protocol_name","defillama_url","category","chains",
                "value_at_risk_usd","band_status","family_id","PRIORITY","LIKELIHOOD","ACTIONABILITY",
                "family_evidence","learned_attack_surface","MATCH_SCORE","EVIDENCE_CONFIDENCE","evidence_level",
                "repeat_victim_count","prior_hack_dates","surface_signals","conditions",
                "preconditions_present","guards_found","prior_art_status","in_final",
                "previously_delivered","first_delivered_in"])
    order=sorted(live_all,key=lambda x:-x.get('PRIORITY',0))
    seen=set(); finals=set()
    _fin_order=[o for o in order if o['protocol_slug'] not in DELIVERED]
    for o in _fin_order:
        if o['protocol_slug'] in seen: continue
        seen.add(o['protocol_slug']); finals.add((o['protocol_slug'],o['family_id']))
        if len(finals)>=N: break
    for i,o in enumerate(order,1):
        k=(o['protocol_slug'],o['family_id']); cs={**o.get('code',{}),**o.get('state',{})}
        lc=o.get('likelihood_components',{})
        w.writerow([i,o['protocol_slug'],o['protocol_name'],o['defillama_url'],o['category'],
          "|".join(o['chains'][:6]),round(o['tvl'],2),o.get('band_status'),o['family_id'],
          o.get('PRIORITY'),o.get('LIKELIHOOD'),o.get('ACTIONABILITY'),lc.get('family_evidence'),
          lc.get('learned_attack_surface'),o['MATCH_SCORE'],o['EVIDENCE_CONFIDENCE'],o['evidence_level'],
          o.get('repeat_victim_count'),"|".join(h.get('date','') for h in (o.get('prior_hacks') or [])),
          "|".join(s['signal'] for s in (o.get('surface_signals') or [])),
          "|".join(o.get('conditions') or []),
          "|".join(k2 for k2,v2 in cs.items() if v2=='PRESENT'),
          "|".join(k2 for k2,v2 in o.get('guards',{}).items() if v2=='FOUND'),
          prior_art(o)['status'],"YES" if k in finals else "NO",
          "YES" if o['protocol_slug'] in DELIVERED else "NO",
          (_LED.get('ledger',{}).get(o['protocol_slug'],{}) or {}).get('first_delivered_in','')])

def one(s): return " ".join(str(s).replace("|"," / ").replace("\n"," ").split())
seen=set(); finals=[]
for o in sorted(live,key=lambda x:-x.get('PRIORITY',0)):
    if o['protocol_slug'] in seen: continue
    seen.add(o['protocol_slug']); finals.append(o)
    if len(finals)>=N: break
with open(f'{B}/results/audit_variables.txt','w') as fh:
    for o in finals:
        f=FAM[o['family_id']]
        fams=sorted({x['family_id'] for x in live if x['protocol_slug']==o['protocol_slug']})[:6]
        fh.write("TARGET=%s || PATTERN_IDS=%s || PRIORITY_HYPOTHESES=%s || MATCH_EVIDENCE=%s || "
                 "REQUIRED_GUARD_CHECKS=%s || PINNED_CHAINS=%s || PRIOR_ART_STATUS=%s\n" %
                 (o['defillama_url'],",".join(fams),one(f['broken_invariant'])[:400],
                  one("protocols/deep_screened.jsonl#%s , protocols/onchain_probes.json#%s , families/families.json#%s"
                      % (o['protocol_slug'],o['protocol_slug'],o['family_id'])),
                  one("; ".join(f['false_positive_killers'][:3]))[:300],
                  ",".join(o['chains'][:6]),prior_art(o)['status']))
with open(f'{B}/families/near_miss_library.jsonl','w') as fh:
    for o in killed:
        fh.write(json.dumps({"protocol_slug":o['protocol_slug'],"family_id":o['family_id'],
          "initial_similarity":o.get('priority_evidence',[]),
          "decisive_guard":", ".join(o.get('guards_found',[])) or "n/a - killed by precondition",
          "guard_evidence":o.get('notes',[]),"killed_conditions":o.get('killed_conditions',[]),
          "remaining_uncertainty":"; ".join(sorted({k for k,v2 in {**o.get('code',{}),**o.get('state',{})}.items()
                                                    if v2=='UNKNOWN'})) or "none recorded",
          "disposition":"PARTIAL" if o.get('kill_reason')=='DECISIVE_GUARD_FOUND' else "KILLED",
          "kill_reason":o.get('kill_reason')},ensure_ascii=False)+"\n")
print(json.dumps({"live":len(live),"killed":len(killed),"finals":len(finals),
 "final_median_tvl":sorted(o['tvl'] for o in finals)[len(finals)//2],
 "final_total_tvl":round(sum(o['tvl'] for o in finals),2),
 "repeat_victims_in_finals":sum(1 for o in finals if (o.get('repeat_victim_count') or 0)>1),
 "previously_hacked_in_finals":sum(1 for o in finals if o.get('prior_hacks')),
 "levels":dict(collections.Counter(o['evidence_level'] for o in finals))},indent=2))
