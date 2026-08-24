#!/usr/bin/env python3
"""Which of the v4 additions actually earned the out-of-sample improvement?

Refits and revalidates the model with feature groups held out, so the gain is
attributed to a group rather than assumed. Same temporal split as learn_weights:
fit on 2022-24 incidents, score 2025-26 incidents never seen while fitting.
"""
import json,datetime,math,bisect,sys,collections
sys.path.insert(0,'/home/user/dd1/incident-intelligence/tools')
from feature_lift_defs import feats, ORDERING_ONLY
B='/home/user/dd1/incident-intelligence'
H=json.load(open(f'{B}/sources/defillama/hacks.json'))
byid={str(r['id']):r for r in json.load(open(f'{B}/sources/defillama/protocols.json'))}
U={r['slug']:r for r in json.load(open(f'{B}/protocols/defillama_universe.json')) if (r.get('_tvl') or 0)>0}
PR=json.load(open(f'{B}/protocols/onchain_probes.json'))
AD=json.load(open(f'{B}/protocols/admin_posture.json'))
OFF={'Key Compromise','Frontend & Infrastructure','Social Engineering','Rugpull'}
def yr(t): return datetime.datetime.utcfromtimestamp(t).year
HACKDATE={}
def victims(y0,y1):
    v=set()
    for h in H:
        if h.get('classification') in OFF or h.get('targetType') in ('CEX','Wallet'): continue
        if not (y0<=yr(h['date'])<=y1): continue
        i=str(h.get('defillamaId') or '')
        if i in byid and byid[i]['slug'] in U:
            s=byid[i]['slug']; v.add(s); HACKDATE[s]=min(HACKDATE.get(s,h['date']),h['date'])
    return v
victims(1970,2100)
FE={s:feats(s,p,PR,asof=HACKDATE.get(s),AD=AD) for s,p in U.items()}
ALL=[k for k in sorted(next(iter(FE.values()))) if k not in ORDERING_ONLY]
AGE={'age_under_1y','age_1_3y','age_over_3y'}
ADM={'admin_terminal_eoa','admin_single_signature','admin_multisig','admin_timelocked','admin_no_delay_path'}
REPO={'no_public_repo'}
train=victims(2022,2024); test=victims(2025,2026); test_only=test-train

def run(keys):
    W={}
    for k in keys:
        pv=sum(1 for f in FE.values() if f[k]); pr=pv/len(FE)
        vv=sum(1 for s in train if FE[s][k])
        if pv<40 or vv<4 or pr==0: continue
        lift=(vv/len(train))/pr
        if 0.7<lift<1.35: continue
        W[k]=math.log(lift)
    sc={s:sum(w for k,w in W.items() if FE[s][k]) for s in U}
    vals=sorted(sc.values())
    def pct(v): return 100.0*bisect.bisect_left(vals,v)/len(vals)
    ps=sorted(pct(sc[s]) for s in test_only)
    top=sum(1 for x in ps if x>=75)/len(ps)
    return {"signals":len(W),"median_pct":round(ps[len(ps)//2],1),
            "top_quartile_share":round(top,3),"lift":round(top/0.25,2)}

base=[k for k in ALL if k not in AGE|ADM|REPO]
variants=[("baseline (v3 feature set)",base),
          ("+ exposure age",base+sorted(AGE)),
          ("+ admin posture",base+sorted(ADM)),
          ("+ public-repo flag",base+sorted(REPO)),
          ("+ all v4 additions",ALL)]
print(f"out-of-sample target: {len(test_only)} protocols hacked 2025-26 and unseen while fitting\n")
print(f"{'variant':28s} {'signals':>7} {'median pct':>11} {'top-quartile':>13} {'lift':>7}")
print("-"*72)
res={}
for name,keys in variants:
    r=run(keys); res[name]=r
    print(f"{name:28s} {r['signals']:7d} {r['median_pct']:10.1f}th {r['top_quartile_share']*100:12.0f}% {'x%.2f'%r['lift']:>7}")
json.dump({"out_of_sample_n":len(test_only),"variants":res,
 "note":("Each variant is refitted from scratch on 2022-24 incidents and scored against "
         "2025-26 incidents on protocols unseen during fitting. Lift is the share of future "
         "victims landing in the model's top quartile, divided by the 25% expected by chance.")},
 open(f'{B}/protocols/ablation.json','w'),indent=1)
