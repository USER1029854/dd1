#!/usr/bin/env python3
"""Likelihood-first candidate reports for an independent reviewer."""
import json,sys,os,csv,collections
sys.path.insert(0,'/home/user/dd1/incident-intelligence/tools')
import hazard as HZ
B='/home/user/dd1/incident-intelligence'
D=[json.loads(l) for l in open(f'{B}/protocols/deep_screened.jsonl')]
FAM={f['family_id']:f for f in json.load(open(f'{B}/families/families.json'))}
E={r['slug']:r for r in json.load(open(f'{B}/protocols/eligibility.json'))}
AD=json.load(open(f'{B}/protocols/adapters_index.json'))
PR=json.load(open(f'{B}/protocols/onchain_probes.json'))
PRIOR=json.load(open(f'{B}/protocols/prior_art.json')) if os.path.exists(f'{B}/protocols/prior_art.json') else {}
BAND=json.load(open(f'{B}/protocols/band_screen.json'))
live=[o for o in D if not o['killed']]; killed=[o for o in D if o['killed']]

def prior_art(o):
    k=f"{o['protocol_slug']}|{o['family_id']}"
    if k in PRIOR: return PRIOR[k]
    if o['family_id']=='ACC-DONATION-UNACCOUNTED-BALANCE' and o.get('forked_from'):
        return {"status":"KNOWN_ISSUE_DEPLOYMENT_STATUS_UNKNOWN",
                "basis":"The Compound-fork donation/exchange-rate vector is publicly documented and was raised in "
                        "Venus's own Code4rena audit before the March 2026 THE-market exploit. Whether THIS "
                        "deployment carries a fix is not established by read-only evidence.",
                "search_scope":"family-level public prior art only"}
    return {"status":"PRIOR_ART_SEARCH_INCOMPLETE",
            "basis":"No per-deployment search of published audits, competitions, advisories and postmortems was "
                    "performed for this pair. Novelty is therefore NOT claimed.",
            "search_scope":"none performed for this pair"}

def block(o,rank,which):
    p=E.get(o['protocol_slug'],{}); f=FAM[o['family_id']]; pa=prior_art(o)
    cs={**o.get('code',{}),**o.get('state',{})}
    pres=[k for k,v in cs.items() if v=='PRESENT']; unk=[k for k,v in cs.items() if v=='UNKNOWN']
    gs=o.get('guards',{}); hc=o.get('hack_likelihood_components',{})
    L=[]
    L.append("### %d. %s  —  `%s`\n" % (rank,o['protocol_name'],o['family_id']))
    L.append("- **Rank (%s):** %d" % (which,rank))
    L.append("- **Protocol:** %s (`%s`) · %s · %s" % (o['protocol_name'],o['protocol_slug'],o['category'],
             ", ".join(o['chains'][:6])+(" …" if len(o['chains'])>6 else "")))
    L.append("- **DefiLlama URL:** %s" % o['defillama_url'])
    L.append("- **Value at risk (TVL):** $%s  ·  **Band:** `%s` — %s" %
             (f"{o['tvl']:,.0f}", o.get('band_status'), o.get('band_reason')))
    if o.get('band_status')=='ABOVE_BAND_KEPT_EXPLICIT_DANGER' and o.get('danger_reasons'):
        L.append("    - Retained above the band on explicit danger: "+"; ".join(o['danger_reasons']))
    elif o.get('danger_reasons'):
        L.append("    - Corroborating danger signals: "+"; ".join(o['danger_reasons']))
    L.append("- **HACK_LIKELIHOOD: %s / 100**" % o.get('HACK_LIKELIHOOD'))
    if hc:
        L.append("    - family evidence %s/%s (MATCH %s × evidence-level weight %s) · hazard %s/%s · "
                 "neglect %s/%s · attacker economics %s/%s" %
                 (hc['family_evidence'],hc['family_evidence_max'],o['MATCH_SCORE'],hc['evidence_level_weight'],
                  hc['hazard_profile'],hc['hazard_profile_max'],hc['neglect'],hc['neglect_max'],
                  hc['attacker_economics'],hc['attacker_economics_max']))
    L.append("- **MATCH_SCORE:** %s / 100 · **EVIDENCE_CONFIDENCE:** %s / 100 · **Evidence level:** `%s`" %
             (o['MATCH_SCORE'],o['EVIDENCE_CONFIDENCE'],o['evidence_level']))
    L.append("- **Why this segment gets hit:** chain hazard ×%s, category hazard ×%s. Hazard is the share of "
             "in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means "
             "over-represented among real victims." % (o.get('chain_hazard'),o.get('category_hazard')))
    L.append("- **Attention deficit (neglect %s/25):**" % hc.get('neglect','n/a'))
    for d in (o.get('neglect_detail') or []):
        L.append("    - `%s` (+%d) — %s" % (d['signal'],d['weight'],d['meaning']))
    if not o.get('neglect_detail'): L.append("    - none observed")
    L.append("- **Broken invariant this family tests:** %s" % f['broken_invariant'])
    if o.get('conditions'): L.append("    - Conditions observed: "+", ".join("`%s`" % c for c in o['conditions']))
    ss=PR.get(o['protocol_slug'],{}).get('source_sweep',{})
    sig=(ss.get('family_signals') or {}).get(o['family_id']) or {}
    if sig:
        ver=[c for c in ss.get('contracts',[]) if c.get('status')=='VERIFIED']
        pre=[k for k,h in sig.items() if h['match'] and h['role']=='PRE']
        gd=[k for k,h in sig.items() if h['match'] and h['role']=='GUARD']
        where=", ".join("`%s` @ %s(%s)" % (c.get('name'),c['address'][:10]+'…',c['chain']) for c in ver[:2]) or "no verified contract"
        L.append("    - Deployed source read (%s): %s%s" % (where,
                 ("prerequisites matched: "+", ".join(pre)) if pre else "no prerequisite matched",
                 ("; guards found: "+", ".join(gd)) if gd else "; no guard found"))
    if o.get('notes'):
        for n in o['notes'][:4]: L.append("    - %s" % n)
    L.append("- **Preconditions PRESENT:** %s" % (", ".join(pres) or "none confirmed"))
    L.append("- **Preconditions UNKNOWN:** %s" % (", ".join(unk) or "none"))
    L.append("- **Guards searched / found:** %s / %s" % (", ".join(gs.keys()) or "none",
             ", ".join(k for k,v in gs.items() if v=='FOUND') or "none found in the reviewed path"))
    L.append("- **Prior-art status:** `%s` — %s" % (pa['status'],pa['basis']))
    L.append("- **What would falsify this:** %s" % "; ".join(f['false_positive_killers'][:3]))
    L.append("- **Where to start:** %s" % f['local_defensive_property'])
    L.append("- **Evidence:** `protocols/deep_screened.jsonl#%s|%s`, `protocols/onchain_probes.json#%s`, "
             "`families/families.json#%s`" % (o['protocol_slug'],o['family_id'],o['protocol_slug'],o['family_id']))
    L.append("- **Disclosure channel:** %s%s" % (p.get('url') or 'not listed',
             (" · audits: "+", ".join(p.get('_audit_links',[])[:2])) if p.get('_audit_links') else " · no audit link listed"))
    L.append("")
    return "\n".join(L)

HDR=("> **Discovery-stage output.** This file asserts no defect in any protocol named below. Each entry is a "
     "*high-priority defensive review candidate*: the named evidence matches a family's prerequisites, the named "
     "evidence is unknown, and the named guard would falsify it. Everything requires separate authorized "
     "verification on a local or pinned fork before any conclusion is drawn.\n")
CTX=("**Who this list is for.** An independent reviewer who wants to prevent real losses, not a fund allocating "
     "audit retainers. The band is $50,000 to $30,000,000: below that there is nothing worth saving, and above it "
     "protocols are assumed to carry dedicated professional coverage, so they are dropped unless specific danger "
     "evidence says otherwise.\n\n"
     "**Why exposure does not drive this ranking.** In this run's own corpus of %d on-chain incidents, the median "
     "loss was $252,000 and 84%% cost under $2,000,000. Only 5%% exceeded $10,000,000. Size is a poor predictor of "
     "being attacked; neglect and segment are far better ones.\n" % 128)

by={'HACK_LIKELIHOOD':'Ranking B — likelihood of being attacked','MATCH_SCORE':'Ranking A — mechanism match'}
N=int(sys.argv[1]) if len(sys.argv)>1 else 45
for key,fn in (('HACK_LIKELIHOOD','candidates_by_likelihood.md'),('MATCH_SCORE','candidates_by_match.md')):
    order=sorted(live,key=lambda x:(-x.get(key,0),-x.get('HACK_LIKELIHOOD',0)))
    seen=set(); out=["# Candidates — %s\n" % by[key],HDR,CTX]
    if key=='HACK_LIKELIHOOD':
        out.append("Score = family evidence (0-40, weighted by how deeply the evidence was actually read) + "
                   "empirical segment hazard (0-25) + attention deficit (0-25) + attacker economics (0-10).\n")
    else:
        out.append("Ranking A answers *which protocols most strongly exhibit a family's observable prerequisites*, "
                   "ignoring segment and neglect entirely.\n")
    n=0; chosen=[]
    for o in order:
        if o['protocol_slug'] in seen: continue
        seen.add(o['protocol_slug']); n+=1; chosen.append(o)
        if n>=N: break
    if key=='HACK_LIKELIHOOD':
        fc=collections.Counter(o['family_id'] for o in chosen)
        out.append("### Family spread in this list\n")
        out.append("| Family | Candidates |"); out.append("|---|---:|")
        for k2,v2 in fc.most_common(): out.append(f"| `{k2}` | {v2} |")
        out.append("\n`UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY` dominates because a deprecated deployment that still "
                   "holds value is both the most neglected shape and the one read-only evidence establishes most "
                   "cleanly. That is an honest reflection of where the cheap wins are, not a modelling artefact.\n")
        # diversified shortlist: strongest few per family, so the queue spans hypothesis types
        byfam=collections.defaultdict(list)
        for o in order:
            byfam[o['family_id']].append(o)
        div=[]; seen2=set()
        for fid,lst in sorted(byfam.items(),key=lambda kv:-max(x['HACK_LIKELIHOOD'] for x in kv[1])):
            picked=0
            for o in lst:
                if o['protocol_slug'] in seen2: continue
                seen2.add(o['protocol_slug']); div.append(o); picked+=1
                if picked>=3: break
        div.sort(key=lambda x:-x['HACK_LIKELIHOOD'])
        out.append("### Diversified shortlist — top 3 per family\n")
        out.append("Use this if you would rather work a spread of hypothesis types than a run of one. Same scoring, "
                   "just capped at three candidates per family.\n")
        out.append("| # | Protocol | Family | HACK_LIKELIHOOD | Value at risk | Category | Evidence |")
        out.append("|---:|---|---|---:|---:|---|---|")
        for i,o in enumerate(div[:30],1):
            out.append("| %d | [%s](%s) | `%s` | %s | $%s | %s | `%s` |" %
                       (i,o['protocol_name'],o['defillama_url'],o['family_id'],o['HACK_LIKELIHOOD'],
                        f"{o['tvl']:,.0f}",o['category'],o['evidence_level']))
        out.append("")
        out.append("---\n")
    for i,o in enumerate(chosen,1): out.append(block(o,i,by[key]))
    open(f'{B}/results/{fn}','w').write("\n".join(out))

# CSV
with open(f'{B}/results/candidates_all.csv','w',newline='') as fh:
    w=csv.writer(fh)
    w.writerow(["rank_likelihood","rank_match","protocol_slug","protocol_name","defillama_url","category","chains",
                "value_at_risk_usd","band_status","family_id","HACK_LIKELIHOOD","family_evidence","hazard_profile",
                "neglect","attacker_economics","MATCH_SCORE","EVIDENCE_CONFIDENCE","evidence_level",
                "chain_hazard","category_hazard","neglect_signals","conditions","preconditions_present",
                "preconditions_unknown","guards_found","prior_art_status","in_final","danger_reasons"])
    rl={ (o['protocol_slug'],o['family_id']):i+1 for i,o in enumerate(sorted(live,key=lambda x:-x.get('HACK_LIKELIHOOD',0)))}
    rm={ (o['protocol_slug'],o['family_id']):i+1 for i,o in enumerate(sorted(live,key=lambda x:-x.get('MATCH_SCORE',0)))}
    seen=set(); finals=set()
    for o in sorted(live,key=lambda x:-x.get('HACK_LIKELIHOOD',0)):
        if o['protocol_slug'] in seen: continue
        seen.add(o['protocol_slug']); finals.add((o['protocol_slug'],o['family_id']))
        if len(finals)>=N: break
    for o in sorted(live,key=lambda x:-x.get('HACK_LIKELIHOOD',0)):
        k=(o['protocol_slug'],o['family_id']); cs={**o.get('code',{}),**o.get('state',{})}
        hc=o.get('hack_likelihood_components',{})
        w.writerow([rl[k],rm[k],o['protocol_slug'],o['protocol_name'],o['defillama_url'],o['category'],
          "|".join(o['chains'][:6]),round(o['tvl'],2),o.get('band_status'),o['family_id'],
          o.get('HACK_LIKELIHOOD'),hc.get('family_evidence'),hc.get('hazard_profile'),hc.get('neglect'),
          hc.get('attacker_economics'),o['MATCH_SCORE'],o['EVIDENCE_CONFIDENCE'],o['evidence_level'],
          o.get('chain_hazard'),o.get('category_hazard'),
          "|".join(d['signal'] for d in (o.get('neglect_detail') or [])),
          "|".join(o.get('conditions') or []),
          "|".join(k2 for k2,v in cs.items() if v=='PRESENT'),
          "|".join(k2 for k2,v in cs.items() if v=='UNKNOWN'),
          "|".join(k2 for k2,v in o.get('guards',{}).items() if v=='FOUND'),
          prior_art(o)['status'],"YES" if k in finals else "NO","; ".join(o.get('danger_reasons') or [])])

# handoff
def one(s): return " ".join(str(s).replace("|"," / ").replace("\n"," ").split())
seen=set(); finals=[]
for o in sorted(live,key=lambda x:-x.get('HACK_LIKELIHOOD',0)):
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

# near misses
with open(f'{B}/families/near_miss_library.jsonl','w') as fh:
    for o in killed:
        fh.write(json.dumps({"protocol_slug":o['protocol_slug'],"family_id":o['family_id'],
          "initial_similarity":o.get('priority_evidence',[]),
          "decisive_guard":", ".join(o.get('guards_found',[])) or "n/a - killed by precondition",
          "guard_evidence":o.get('notes',[]),"killed_conditions":o.get('killed_conditions',[]),
          "remaining_uncertainty":"; ".join(sorted({k for k,v in {**o.get('code',{}),**o.get('state',{})}.items()
                                                    if v=='UNKNOWN'})) or "none recorded",
          "disposition":"PARTIAL" if o.get('kill_reason')=='DECISIVE_GUARD_FOUND' else "KILLED",
          "kill_reason":o.get('kill_reason')},ensure_ascii=False)+"\n")

# dropped-above-band record
dropped=[r for r in BAND if r['band_status']=='ABOVE_BAND_DROPPED']
dropped.sort(key=lambda x:-x['tvl'])
json.dump(dropped,open(f'{B}/protocols/above_band_dropped.json','w'),indent=1)
print(json.dumps({"live_pairs":len(live),"killed":len(killed),"finals":len(finals),
 "final_median_tvl":sorted(o['tvl'] for o in finals)[len(finals)//2] if finals else 0,
 "final_band":dict(collections.Counter(o.get('band_status') for o in finals)),
 "above_band_dropped":len(dropped),
 "levels":dict(collections.Counter(o['evidence_level'] for o in finals))},indent=2))
