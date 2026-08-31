#!/usr/bin/env python3
"""Does the model actually rank real victims highly?

Takes protocols hacked by an on-chain defect since 2024 that are still listed, scores them
on the structural half of the model (segment hazard + attention deficit, both stable
characteristics), and compares that against the whole eligible population. If victims do not
sit materially above the median, the model has no signal and should not be trusted.

Honest limits: DefiLlama data is CURRENT, not pre-hack, so audits added afterwards and TVL
that moved post-incident both leak in. Treat this as a sanity check, not a proof.
"""
import json,collections,datetime,statistics,sys
sys.path.insert(0,'/home/user/dd1/incident-intelligence/tools')
import hazard as HZ
B='/home/user/dd1/incident-intelligence'
H=json.load(open(f'{B}/sources/defillama/hacks.json'))
P=json.load(open(f'{B}/sources/defillama/protocols.json'))
byid={str(r['id']):r for r in P}
E={r['slug']:r for r in json.load(open(f'{B}/protocols/eligibility.json')) if r['_queue']=='MAIN'}
PR=json.load(open(f'{B}/protocols/onchain_probes.json'))
OFFCHAIN={'Key Compromise','Frontend & Infrastructure','Social Engineering','Rugpull'}
def yr(t): return datetime.datetime.utcfromtimestamp(t).year

NOPRIOR='--no-prior' in sys.argv
if NOPRIOR: HZ.PRIOR_SIGNALS_ENABLED=False
FIRST={}   # slug -> ISO date of its earliest linked on-chain hack, for leakage-free scoring
def structural(p, before=None):
    hp,ch,ca=HZ.hazard_profile(p)
    ng,_=HZ.neglect(p,PR.get(p['slug']),PR.get(p['slug'],{}).get('source_sweep'),before_date=before)
    ae,_=HZ.attacker_economics(p.get('_tvl') or 0)
    return round(hp+ng+ae,2)

IN_BAND={s:p for s,p in E.items() if HZ.BAND_LO<=(p.get('_tvl') or 0)<=HZ.BAND_HI}
SCOPE=(E if '--all' in sys.argv else IN_BAND)
scope_name='whole eligible population' if '--all' in sys.argv else 'the $50k-$30M band only'
import datetime as _dt
for h in H:
    i=str(h.get('defillamaId') or '')
    if i in byid:
        d=_dt.datetime.utcfromtimestamp(h['date']).date().isoformat()
        sl=byid[i]['slug']
        if sl not in FIRST or d<FIRST[sl]: FIRST[sl]=d
pop={s:structural(p, FIRST.get(s)) for s,p in SCOPE.items()}
vals=sorted(pop.values())
print(f"scope: {scope_name}")
def pct(v):
    import bisect; return round(100.0*bisect.bisect_left(vals,v)/len(vals),1)

vict=set()
for h in H:
    if h.get('classification') in OFFCHAIN or h.get('targetType') in ('CEX','Wallet'): continue
    if yr(h['date'])<2024: continue
    i=str(h.get('defillamaId') or '')
    if i in byid and byid[i]['slug'] in SCOPE: vict.add(byid[i]['slug'])
vs=sorted(vict)
print(f"population (eligible, >=$50k): {len(pop)}   median structural score {statistics.median(vals):.1f}")
print(f"victims since 2024 still eligible: {len(vs)}")
vp=[pct(pop[s]) for s in vs]
print(f"\nvictim percentile within the population:")
print(f"  median  {statistics.median(vp):.1f}th")
print(f"  mean    {statistics.mean(vp):.1f}th")
print(f"  in top 25%  : {sum(1 for x in vp if x>=75)} of {len(vp)} ({sum(1 for x in vp if x>=75)/len(vp)*100:.0f}%)")
print(f"  in top 50%  : {sum(1 for x in vp if x>=50)} of {len(vp)} ({sum(1 for x in vp if x>=50)/len(vp)*100:.0f}%)")
print(f"  in bottom 25%: {sum(1 for x in vp if x<25)} of {len(vp)} ({sum(1 for x in vp if x<25)/len(vp)*100:.0f}%)")
lift=(sum(1 for x in vp if x>=75)/len(vp))/0.25
print(f"\n  LIFT in the top quartile: x{lift:.2f}  (x1.0 would mean the model is no better than chance)")
print("\n  highest-scoring victims (model would have flagged these):")
for s in sorted(vs,key=lambda x:-pop[x])[:12]:
    p=SCOPE[s]; print(f"   {pct(pop[s]):5.1f}th  score {pop[s]:5.1f}  ${p['_tvl']:>12,.0f}  {s[:30]:32s} {p['_cat']}")
print("\n  lowest-scoring victims (the model missed these):")
for s in sorted(vs,key=lambda x:pop[x])[:8]:
    p=SCOPE[s]; print(f"   {pct(pop[s]):5.1f}th  score {pop[s]:5.1f}  ${p['_tvl']:>12,.0f}  {s[:30]:32s} {p['_cat']}")
json.dump({"population":len(pop),"victims_tested":len(vs),
 "victim_percentile_median":statistics.median(vp),"victim_percentile_mean":round(statistics.mean(vp),1),
 "share_in_top_quartile":round(sum(1 for x in vp if x>=75)/len(vp),3),
 "top_quartile_lift":round(lift,2),
 "prior_hack_signals":("disabled" if NOPRIOR else "leakage-controlled: only hacks strictly before the protocol's first recorded incident"),
 "scope":scope_name,
 "victims":[{"slug":s,"score":pop[s],"percentile":pct(pop[s]),"tvl":SCOPE[s]['_tvl'],"category":SCOPE[s]['_cat']} for s in vs],
 "caveats":["DefiLlama data is current, not pre-hack: audits added after an incident and TVL that moved "
            "afterwards both leak into the score",
            "only the structural half of the model is tested (hazard + neglect + economics); family evidence "
            "requires a deep screen that was not run against the full population",
            "victims still listed are survivors; protocols that died after being hacked are absent"]},
 open(f'{B}/protocols/backtest.json','w'),indent=1)
