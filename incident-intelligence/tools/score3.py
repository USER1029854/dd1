#!/usr/bin/env python3
"""Likelihood-first scoring for an independent reviewer.

Ranking A  MATCH_SCORE       - how much of a family's observable signature is confirmed.
Ranking B  HACK_LIKELIHOOD   - how likely this protocol is to actually be attacked, built from
                               the empirical victim profile of this run's own corpus.
VALUE_AT_RISK is reported alongside but never drives the ranking: the corpus says exposure is
a poor predictor of being hit (median in-window loss $252,000; 84% of incidents under $2M).
"""
import json,sys,os,collections,datetime,math
sys.path.insert(0,'/home/user/dd1/incident-intelligence/tools')
import score2 as S2
import hazard as HZ
B='/home/user/dd1/incident-intelligence'
W=json.load(open(f'{B}/protocols/deep_screen_worklist.json'))
FAM={f['family_id']:f for f in json.load(open(f'{B}/families/families.json'))}
E={r['slug']:r for r in json.load(open(f'{B}/protocols/eligibility.json'))}
PR=json.load(open(f'{B}/protocols/onchain_probes.json'))

def score(pair):
    base=S2.score(pair)
    slug=pair['protocol_slug']
    if base.get('killed'):
        base['band_status']=pair.get('band_status'); base['tvl']=pair.get('tvl')
        return base
    p=E.get(slug,{}); tvl=pair.get('tvl') or 0
    hp = pair.get('hazard_profile')
    if hp is None: hp,_ch,_ca = HZ.hazard_profile(p)
    ng = pair.get('neglect')
    ngd= pair.get('neglect_detail') or []
    if ng is None:
        ng,ngd = HZ.neglect(p,PR.get(slug),PR.get(slug,{}).get('source_sweep'))
    ae = pair.get('attacker_economics')
    aew= pair.get('economics_note')
    if ae is None: ae,aew = HZ.attacker_economics(tvl)
    # Family evidence, rescaled from MATCH_SCORE onto 0-40 and weighted by evidence level:
    # a match asserted from metadata is worth far less than one read out of deployed code.
    lvl_w={'L0_METADATA':0.35,'L1_ADAPTER':0.55,'L2_DEPLOYMENT':0.80,'L3_STATE':0.90,'L4_GUARD_REVIEW':1.0}
    fe = round(40.0*(base['MATCH_SCORE']/100.0)*lvl_w.get(base['evidence_level'],0.5),2)
    hl = round(fe+hp+ng+ae,2)
    base.update({
      "HACK_LIKELIHOOD":hl,
      "hack_likelihood_components":{
        "family_evidence":fe,"family_evidence_max":40,
        "hazard_profile":hp,"hazard_profile_max":25,
        "neglect":ng,"neglect_max":25,
        "attacker_economics":ae,"attacker_economics_max":10,
        "evidence_level_weight":lvl_w.get(base['evidence_level'],0.5)},
      "neglect_detail":ngd,"economics_note":aew,
      "chain_hazard":pair.get('chain_hazard'),"category_hazard":pair.get('category_hazard'),
      "VALUE_AT_RISK_USD":round(tvl,2),
      "band_status":pair.get('band_status'),"band_reason":pair.get('band_reason'),
      "danger_reasons":pair.get('danger_reasons') or [],
      "tvl":tvl})
    return base

out=[{**w,**score(w)} for w in W]
with open(f'{B}/protocols/deep_screened.jsonl','w') as fh:
    for o in out: fh.write(json.dumps(o,ensure_ascii=False)+"\n")
live=[o for o in out if not o['killed']]
def top(key,n=14):
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
 "band":dict(collections.Counter(o.get('band_status') for o in live)),
 "median_tvl_of_surviving":sorted(o['tvl'] for o in live)[len(live)//2] if live else 0,
 "top_hack_likelihood":[(o['protocol_slug'],o['family_id'],o['HACK_LIKELIHOOD'],
                         f"${o['tvl']:,.0f}",o['evidence_level']) for o in top('HACK_LIKELIHOOD')],
 "top_match":[(o['protocol_slug'],o['family_id'],o['MATCH_SCORE'],f"${o['tvl']:,.0f}") for o in top('MATCH_SCORE')]},
 indent=2))
