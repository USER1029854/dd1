# -*- coding: utf-8 -*-
"""Attack surface from LEARNED weights, plus an explicit actionability term.

Two things were being conflated and are now separated:

  LIKELIHOOD    how likely this protocol is to be attacked. Built from weights fitted on
                2022-24 hacks and validated out of sample on 2025-26 hacks (lift x2.32 on
                95 protocols unseen during fitting).
  ACTIONABILITY whether an independent reviewer can realistically do anything about it.
                This is the operator's constraint, not a prediction, and it is kept out of
                the likelihood number so neither quietly contaminates the other.

Honest reading of the weights: several are proxies for size and integration rather than
causes. `has_2plus_audits` is positive because audited protocols are the ones large enough
to be worth auditing and worth attacking. `owner_is_eoa` and `owner_is_contract` are both
positive because what they really encode is that a live owner was readable at all.

`age_under_1y` is the one v4 addition that improved out-of-sample prediction (x2.19 ->
x2.32 under ablation), and it is the weight that contradicts the obvious intuition: it is
not the abandoned, forgotten deployments that get hit. Over three years old measures x0.33.
Custody posture was measured the same way and DROPPED -- it did not help (x2.19 -> x2.15)
and it is reported on its own in results/upgrade_authority_exposure.md instead.
"""
import json,os,math
_W=os.path.join(os.path.dirname(__file__),'..','protocols','learned_weights.json')
_D=json.load(open(_W)) if os.path.exists(_W) else {}
WEIGHTS={k:v['weight'] for k,v in (_D.get('weights') or {}).items()}
LIFTS={k:v['lift'] for k,v in (_D.get('weights') or {}).items()}
VALIDATION=_D.get('out_of_sample_unseen') or {}
_pos=sum(w for w in WEIGHTS.values() if w>0) or 1.0
_neg=sum(-w for w in WEIGHTS.values() if w<0) or 1.0

def surface(features, cap=30.0):
    """0..cap. Sum of learned weights for the signals this protocol carries."""
    hits=[(k,WEIGHTS[k]) for k in WEIGHTS if features.get(k)]
    raw=sum(w for _k,w in hits)
    norm=(raw+_neg)/(_pos+_neg)                     # map [-neg, +pos] onto [0,1]
    return round(max(0.0,min(1.0,norm))*cap,2), sorted(hits,key=lambda x:-abs(x[1]))

def explain(hits):
    out=[]
    for k,w in hits:
        out.append({"signal":k,"weight":round(w,3),"measured_lift":LIFTS.get(k),
                    "direction":"raises likelihood" if w>0 else "lowers likelihood"})
    return out

# ---- actionability: the operator's constraint, deliberately separate ----
BAND_LO=50_000; BAND_HI=30_000_000
def actionability(tvl, has_disclosure_channel=True, cap=100.0):
    t=tvl or 0
    if t<BAND_LO:  base,why=0.0,"below the $50,000 floor: nothing worth saving"
    elif t<=1_000_000: base,why=100.0,"small enough to be unwatched, large enough to matter"
    elif t<=10_000_000: base,why=85.0,"mid-band: a team of this size will usually take an outside report"
    elif t<=BAND_HI: base,why=60.0,"upper band: may already retain reviewers"
    elif t<=100_000_000: base,why=20.0,"above the band: assume dedicated professional coverage"
    else: base,why=5.0,"far above the band: continuous professional coverage assumed"
    if not has_disclosure_channel: base*=0.75; why+="; no public disclosure channel listed"
    return round(min(cap,base),1), why
