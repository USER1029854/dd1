#!/usr/bin/env python3
"""Production scoring, v4.

LIKELIHOOD    (0-100)  family evidence (0-50, discounted by how deeply it was read)
                       + learned attack surface (0-50, weights fitted on 2022-24 hacks and
                       validated out of sample on 2025-26: lift x2.32 on 95 unseen protocols).
ACTIONABILITY (0-100)  whether an independent reviewer can realistically act. The operator's
                       constraint, deliberately kept OUT of the likelihood number.
PRIORITY               LIKELIHOOD x ACTIONABILITY/100. This is the queue to work.

Value at risk is reported separately again, because bigger protocols are in fact MORE likely
to be hit (tvl_over_5m carries lift x1.75) while being LESS actionable. Folding the two
together is what produced the earlier misdirected rankings.
"""
import json,sys,os,collections
sys.path.insert(0,'/home/user/dd1/incident-intelligence/tools')
import score2 as S2, attack_surface as AS, hazard as HZ
B='/home/user/dd1/incident-intelligence'
W=json.load(open(f'{B}/protocols/deep_screen_worklist.json'))
FAM={f['family_id']:f for f in json.load(open(f'{B}/families/families.json'))}
E={r['slug']:r for r in json.load(open(f'{B}/protocols/eligibility.json'))}
PR=json.load(open(f'{B}/protocols/onchain_probes.json'))
AD=json.load(open(f'{B}/protocols/admin_posture.json')) if os.path.exists(f'{B}/protocols/admin_posture.json') else {}
LVLW={'L0_METADATA':0.30,'L1_ADAPTER':0.50,'L2_DEPLOYMENT':0.78,'L3_STATE':0.88,'L4_GUARD_REVIEW':1.0}

def score(pair):
    base=S2.score(pair)
    slug=pair['protocol_slug']; tvl=pair.get('tvl') or 0
    if base.get('killed'):
        base.update({"band_status":pair.get('band_status'),"tvl":tvl,
                     "VALUE_AT_RISK_USD":round(tvl,2)}); return base
    surf=pair.get('attack_surface')
    sigs=pair.get('surface_signals') or []
    if surf is None:
        from feature_lift_defs import feats
        surf,hits=AS.surface(feats(slug,E.get(slug,{}),PR,AD=AD)); sigs=AS.explain(hits)
    act=pair.get('actionability'); actwhy=pair.get('actionability_reason')
    if act is None:
        act,actwhy=AS.actionability(tvl)
    fe=round(50.0*(base['MATCH_SCORE']/100.0)*LVLW.get(base['evidence_level'],0.4),2)
    su=round(50.0*(surf/30.0),2)
    lik=round(min(100.0,fe+su),2)
    pri=round(lik*(act/100.0),2)
    rv=pair.get('repeat_victim_count') or 0
    base.update({
      "LIKELIHOOD":lik,
      "likelihood_components":{"family_evidence":fe,"family_evidence_max":50,
        "learned_attack_surface":su,"learned_attack_surface_max":50,
        "raw_surface":surf,"evidence_level_weight":LVLW.get(base['evidence_level'],0.4),
        "validation":AS.VALIDATION},
      "ACTIONABILITY":act,"actionability_reason":actwhy,
      "PRIORITY":pri,
      "surface_signals":sigs,
      "repeat_victim_count":rv,"prior_hacks":pair.get('prior_hacks') or [],
      "upgrade_authority":pair.get('upgrade_authority'),
      "upgrade_authority_detail":pair.get('upgrade_authority_detail'),
      "operational_flags":pair.get('operational_flags') or [],
      "chain_hazard":pair.get('chain_hazard'),"category_hazard":pair.get('category_hazard'),
      "VALUE_AT_RISK_USD":round(tvl,2),"tvl":tvl,
      "band_status":pair.get('band_status'),"band_reason":pair.get('band_reason'),
      "danger_reasons":pair.get('danger_reasons') or []})
    return base

out=[{**w,**score(w)} for w in W]
with open(f'{B}/protocols/deep_screened.jsonl','w') as fh:
    for o in out: fh.write(json.dumps(o,ensure_ascii=False)+"\n")
live=[o for o in out if not o['killed']]
def top(key,n=15):
    seen=set(); r=[]
    for o in sorted(live,key=lambda x:-x.get(key,0)):
        if o['protocol_slug'] in seen: continue
        seen.add(o['protocol_slug']); r.append(o)
        if len(r)>=n: break
    return r
print(json.dumps({"pairs":len(out),"killed":len(out)-len(live),
 "killed_by_precondition":sum(1 for o in out if o.get('kill_reason')=='MANDATORY_PRECONDITION_PROVEN_ABSENT'),
 "killed_by_guard":sum(1 for o in out if o.get('kill_reason')=='DECISIVE_GUARD_FOUND'),
 "surviving":len(live),"by_level":dict(collections.Counter(o['evidence_level'] for o in live)),
 "protocols":len(set(o['protocol_slug'] for o in live)),
 "repeat_victims_surviving":len({o['protocol_slug'] for o in live if (o.get('repeat_victim_count') or 0)>1}),
 "median_tvl":sorted(o['tvl'] for o in live)[len(live)//2],
 "top_priority":[(o['protocol_slug'],o['family_id'],o['PRIORITY'],o['LIKELIHOOD'],
                  f"${o['tvl']:,.0f}",o['evidence_level']) for o in top('PRIORITY')],
 "top_likelihood_any_size":[(o['protocol_slug'],o['family_id'],o['LIKELIHOOD'],f"${o['tvl']:,.0f}")
                            for o in top('LIKELIHOOD')]},indent=2))
