#!/usr/bin/env python3
"""Measure each candidate signal's real discriminative power instead of assuming a weight.

For every binary signal: lift = P(signal | victim) / P(signal | population).
Lift near 1 means the signal carries no information and should not be scored.
Victims are protocols hacked by an on-chain defect since 2024 that are still listed.

Age is evaluated at the instant that matters -- a victim's own incident date, a
survivor's today -- so "how old was it when it was hit" is compared against "how old
is it having survived". Every other feature comes from tools/feature_lift_defs.py,
which is the single definition shared with production scoring.
"""
import json,collections,datetime,math,sys
sys.path.insert(0,'/home/user/dd1/incident-intelligence/tools')
import hazard as HZ
from feature_lift_defs import feats as FEATS, ORDERING_ONLY
B='/home/user/dd1/incident-intelligence'
H=json.load(open(f'{B}/sources/defillama/hacks.json'))
P=json.load(open(f'{B}/sources/defillama/protocols.json'))
byid={str(r['id']):r for r in P}
E={r['slug']:r for r in json.load(open(f'{B}/protocols/eligibility.json')) if r['_queue']=='MAIN'}
PR=json.load(open(f'{B}/protocols/onchain_probes.json'))
try: AD=json.load(open(f'{B}/protocols/admin_posture.json'))
except Exception: AD={}
# Censoring correction: measuring only against survivors makes neglect look protective,
# because unaudited victims fall below the floor and leave the population. 62.5% of victims
# that dropped under $50k had no audit, against 20.9% of those still in band. So the
# comparison must run over the full listed universe, with every linked victim retained.
ALLU={r['slug']:r for r in json.load(open(f'{B}/protocols/defillama_universe.json')) if (r.get('_tvl') or 0)>0}
BAND=ALLU if '--uncensored' in sys.argv else {s:p for s,p in E.items() if HZ.BAND_LO<=(p.get('_tvl') or 0)<=HZ.BAND_HI}
OFF={'Key Compromise','Frontend & Infrastructure','Social Engineering','Rugpull'}
def yr(t): return datetime.datetime.utcfromtimestamp(t).year
vict={}                                     # slug -> earliest qualifying incident timestamp
for h in H:
    if h.get('classification') in OFF or h.get('targetType') in ('CEX','Wallet'): continue
    if yr(h['date'])<2024: continue
    i=str(h.get('defillamaId') or '')
    if i in byid and byid[i]['slug'] in BAND:
        s=byid[i]['slug']
        vict[s]=min(vict.get(s,h['date']),h['date'])

if __name__!='__main__':
    raise SystemExit
pop=[(s,FEATS(s,p,PR,asof=vict.get(s),AD=AD)) for s,p in BAND.items()]
keys=sorted(pop[0][1])
rows=[]
for k in keys:
    pv=sum(1 for s,f in pop if f[k]); pr_=pv/len(pop)
    vv=sum(1 for s,f in pop if s in vict and f[k]); vr=vv/max(len(vict),1)
    if pv<20: continue
    lift=vr/pr_ if pr_ else 0
    rows.append((lift,k,vv,len(vict),pv,len(pop)))
rows.sort(reverse=True)
scope='FULL LISTED UNIVERSE (censoring-corrected)' if '--uncensored' in sys.argv else 'band only (censored)'
print(f"scope: {scope}\npopulation {len(pop)} | victims since 2024 {len(vict)}\n")
print(f"{'signal':34s} {'lift':>6} {'P(sig|victim)':>14} {'P(sig|pop)':>11}  victims/pop")
print("-"*92)
for lift,k,vv,nv,pv,np_ in rows:
    star='  <-- informative' if (lift>=1.4 and vv>=6) or (lift<=0.6 and pv>=100) else ''
    if k in ORDERING_ONLY: star='  [ordering only, not fitted]'
    print(f"{k:34s} {lift:6.2f} {vv/max(nv,1)*100:13.1f}% {pv/np_*100:10.1f}%  {vv}/{pv}{star}")
json.dump({"scope":scope,"population":len(pop),"victims":len(vict),
 "ordering_only":sorted(ORDERING_ONLY),
 "signals":[{"signal":k,"lift":round(l,3),"victims_with":vv,"victims_total":nv,
             "population_with":pv,"population_total":np_,"fitted":k not in ORDERING_ONLY}
            for l,k,vv,nv,pv,np_ in rows]},
 open(f'{B}/protocols/feature_lift{"_uncensored" if "--uncensored" in sys.argv else ""}.json','w'),indent=1)
