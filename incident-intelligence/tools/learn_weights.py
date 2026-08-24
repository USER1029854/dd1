#!/usr/bin/env python3
"""Learn signal weights from data, then validate them out of sample.

Weights are fitted on hacks from a TRAIN window and scored against hacks from a later TEST
window, so the reported lift is not the model grading its own homework. Population is the
full listed universe rather than survivors only, because unaudited victims fall below the
floor after being hit and would otherwise be censored out.
"""
import json,collections,datetime,math,sys
sys.path.insert(0,'/home/user/dd1/incident-intelligence/tools')
import hazard as HZ
from feature_lift_defs import feats, ORDERING_ONLY, EXCLUDED_BY_ABLATION, NOT_FITTED
B='/home/user/dd1/incident-intelligence'
H=json.load(open(f'{B}/sources/defillama/hacks.json'))
byid={str(r['id']):r for r in json.load(open(f'{B}/sources/defillama/protocols.json'))}
U={r['slug']:r for r in json.load(open(f'{B}/protocols/defillama_universe.json')) if (r.get('_tvl') or 0)>0}
PR=json.load(open(f'{B}/protocols/onchain_probes.json'))
try: AD=json.load(open(f'{B}/protocols/admin_posture.json'))
except Exception: AD={}
OFF={'Key Compromise','Frontend & Infrastructure','Social Engineering','Rugpull'}
def yr(t): return datetime.datetime.utcfromtimestamp(t).year

HACKDATE={}                                # slug -> earliest qualifying incident timestamp
def victims(y0,y1):
    v=set()
    for h in H:
        if h.get('classification') in OFF or h.get('targetType') in ('CEX','Wallet'): continue
        if not (y0<=yr(h['date'])<=y1): continue
        i=str(h.get('defillamaId') or '')
        if i in byid and byid[i]['slug'] in U:
            s=byid[i]['slug']; v.add(s)
            HACKDATE[s]=min(HACKDATE.get(s,h['date']),h['date'])
    return v

_all=victims(1970,2100)                    # populate HACKDATE before features are built
# Age is evaluated at the moment each protocol was judged: a victim's own incident
# date, a survivor's today. Every other feature is time-invariant or explicitly
# marked ORDERING_ONLY and excluded from fitting below.
FE={s:feats(s,p,PR,asof=HACKDATE.get(s),AD=AD) for s,p in U.items()}
keys=[k for k in sorted(next(iter(FE.values()))) if k not in NOT_FITTED]
def fit(train):
    W={}
    for k in keys:
        pv=sum(1 for f in FE.values() if f[k]); pr=pv/len(FE)
        vv=sum(1 for s in train if FE[s][k]); vr=vv/max(len(train),1)
        if pv<40 or vv<4 or pr==0: continue          # require support on both sides
        lift=vr/pr
        if 0.7<lift<1.35: continue                    # uninformative band
        W[k]={"lift":round(lift,3),"weight":round(math.log(lift),3),
              "victims_with":vv,"victims_total":len(train),"population_with":pv}
    return W
def score(s,W): return sum(w["weight"] for k,w in W.items() if FE[s][k])

TRAIN_Y=(2022,2024); TEST_Y=(2025,2026)
train=victims(*TRAIN_Y); test=victims(*TEST_Y)
test_only=test-train                                  # never seen while fitting
W=fit(train)
print(f"train victims {sorted(TRAIN_Y)}: {len(train)}   test victims {sorted(TEST_Y)}: {len(test)}  "
      f"(unseen in train: {len(test_only)})")
print(f"signals kept: {len(W)} of {len(keys)}\n")
for k,w in sorted(W.items(),key=lambda x:-abs(x[1]['weight'])):
    print(f"  {k:32s} lift {w['lift']:5.2f}  weight {w['weight']:+.3f}   {w['victims_with']}/{w['victims_total']} victims")
sc={s:score(s,W) for s in U}
vals=sorted(sc.values())
import bisect
def pct(v): return 100.0*bisect.bisect_left(vals,v)/len(vals)
def report(name,V):
    if not V: return None
    ps=[pct(sc[s]) for s in V]
    top=sum(1 for x in ps if x>=75)/len(ps)
    print(f"\n  {name}: n={len(V)}  median percentile {sorted(ps)[len(ps)//2]:.1f}th  "
          f"top-quartile share {top*100:.0f}%  LIFT x{top/0.25:.2f}")
    return {"n":len(V),"median_percentile":round(sorted(ps)[len(ps)//2],1),
            "top_quartile_share":round(top,3),"lift":round(top/0.25,2)}
print("\n=== OUT-OF-SAMPLE VALIDATION ===")
r_in =report("in-sample (train victims)",train)
r_out=report("OUT-OF-SAMPLE (test victims)",test)
r_new=report("OUT-OF-SAMPLE, unseen protocols only",test_only)
json.dump({"train_window":TRAIN_Y,"test_window":TEST_Y,"weights":W,
 "in_sample":r_in,"out_of_sample":r_out,"out_of_sample_unseen":r_new,
 "population":len(U),
 "method":("weights = ln(lift) measured on TRAIN victims against the full listed universe; "
           "signals needing >=40 population support, >=4 train victims, and lift outside 0.70-1.35"),
 "excluded_from_fitting_leakage":sorted(ORDERING_ONLY),
 "excluded_from_fitting_ablation":sorted(EXCLUDED_BY_ABLATION),
 "caveats":["population is current DefiLlama data, so post-hack changes leak in",
            "admin posture was measured, ablated and then dropped: it did not improve "
            "out-of-sample prediction (x2.19 -> x2.15) and measures ~1.0 over the full "
            "window, so custody exposure is reported separately instead of scored here",
            "exposure age is the one v4 addition that earned its place: x2.19 -> x2.32",
            "protocols delisted entirely are absent from both victim and population sets",
            "lift is a marginal association, not a causal claim, and several signals are proxies for size"]},
 open(f'{B}/protocols/learned_weights.json','w'),indent=1)
