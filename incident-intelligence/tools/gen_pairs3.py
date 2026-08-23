#!/usr/bin/env python3
"""Band-targeted pair generation for an independent reviewer.

Ranks by likelihood of being attacked, not by exposure. Applies the $50k-$30M band with
an explicit-danger override above it, and orders by empirical hazard x neglect.
"""
import json,sys,os,collections,math
sys.path.insert(0,'/home/user/dd1/incident-intelligence/tools')
from matcher import APPLIC, NOT_SCREENABLE, APPLIC_SOURCE
from conditions import COND
import hazard as HZ
B='/home/user/dd1/incident-intelligence'
E=[r for r in json.load(open(f'{B}/protocols/eligibility.json')) if r['_queue']=='MAIN']
FAM={f['family_id']:f for f in json.load(open(f'{B}/families/families.json'))}
PR=json.load(open(f'{B}/protocols/onchain_probes.json')) if os.path.exists(f'{B}/protocols/onchain_probes.json') else {}
DEEP={}
if os.path.exists(f'{B}/protocols/deep_screened.jsonl'):
    for l in open(f'{B}/protocols/deep_screened.jsonl'):
        d=json.loads(l)
        if not d.get('killed'): DEEP[(d['protocol_slug'],d['family_id'])]=d

DANGER_CONDS={'IS_WINDOW_VICTIM_STILL_LIVE','FORK_OF_WINDOW_VICTIM','DEAD_ADAPTER_WITH_RESIDUAL_TVL',
              'HALLMARK_PRIOR_INCIDENT'}
def explicit_danger(p):
    """Above the band, a protocol is only kept on specific evidence, never on category fit."""
    reasons=[]
    conds=set(p.get('_conditions') or [])
    for c in sorted(conds & DANGER_CONDS): reasons.append(f"condition {c}")
    pr=PR.get(p['slug'],{})
    if any(c.get('status')=='IMPLEMENTATION_NOT_VERIFIED' for c in pr.get('source_sweep',{}).get('contracts',[])):
        reasons.append("an implementation behind a live proxy is unverified on the explorer")
    best=[d for (s,f),d in DEEP.items() if s==p['slug'] and d.get('evidence_level')=='L4_GUARD_REVIEW'
          and d.get('MATCH_SCORE',0)>=70]
    if best: reasons.append(f"a deployed-source pair already scores {max(d['MATCH_SCORE'] for d in best)} at L4 guard review")
    return reasons

def cond_families(p):
    out=collections.defaultdict(list)
    for cid,d in (p.get('_condition_detail') or {}).items():
        fams=d.get('families')
        if not fams: continue
        _f,kind,w,_desc=COND[cid]
        for f in fams:
            if f in FAM: out[f].append((cid,kind,w,d['evidence']))
    return out

rows=[]
for p in E:
    tvl=p.get('_tvl') or 0
    dz=explicit_danger(p)
    status,why=HZ.band_status(tvl,bool(dz))
    if status in ('BELOW_FLOOR','ABOVE_BAND_DROPPED'):
        rows.append({"slug":p['slug'],"band_status":status,"reason":why,"tvl":tvl,
                     "danger_reasons":dz}); continue
    hp,ch,ca=HZ.hazard_profile(p)
    ng,ngd=HZ.neglect(p,PR.get(p['slug']),PR.get(p['slug'],{}).get('source_sweep'))
    ae,aew=HZ.attacker_economics(tvl)
    rows.append({"slug":p['slug'],"band_status":status,"reason":why,"tvl":tvl,"danger_reasons":dz,
                 "hazard_profile":hp,"chain_hazard":ch,"category_hazard":ca,
                 "neglect":ng,"neglect_detail":ngd,"attacker_economics":ae,"economics_note":aew,
                 "screen_priority":round(hp+ng+ae,2)})
json.dump(rows,open(f'{B}/protocols/band_screen.json','w'),indent=1)
keep=[r for r in rows if r['band_status'] in ('IN_BAND','ABOVE_BAND_KEPT_EXPLICIT_DANGER')]
keep.sort(key=lambda x:-x['screen_priority'])
BUDGET=int(sys.argv[1]) if len(sys.argv)>1 else 700
targets={r['slug'] for r in keep[:BUDGET]}
Emap={r['slug']:r for r in E}

pairs=[]
for slug in targets:
    p=Emap[slug]; cf=cond_families(p); band=next(r for r in keep if r['slug']==slug)
    fids=set(APPLIC)|set(cf)
    if PR.get(slug,{}).get('deployment',{}).get('addresses_probed'): fids |= APPLIC_SOURCE
    for fid in fids:
        if fid not in FAM: continue
        a=APPLIC.get(fid)
        cat_ok = a is not None and (a.get('cats') is None or p['_cat'] in a['cats'])
        conds=cf.get(fid,[])
        src=bool(((PR.get(slug,{}).get('source_sweep',{}).get('family_signals') or {}).get(fid)))
        if not (cat_ok or conds or (src and fid in APPLIC_SOURCE)): continue
        if a is not None and a.get('requires_governance') and not p['_governance']: continue
        ev=[]; lin=0.0
        if cat_ok: ev.append(f"archetype applicable: category={p['_cat']} (empirical category hazard x{band['category_hazard']})")
        else: ev.append("pair created by an observed condition or a deployed-source indicator rather than by category")
        for cid,kind,w,evd in conds:
            ev.append(f"[{kind}] {cid}: {evd}")
            if kind=='LINEAGE': lin=max(lin,min(15.0,w*0.9))
        ev.append(f"chain hazard x{band['chain_hazard']} (max over {', '.join((p['_chains'] or [])[:4])})")
        ev.append(f"neglect {band['neglect']}/25: "+", ".join(d['signal'] for d in band['neglect_detail']) if band['neglect_detail']
                  else f"neglect {band['neglect']}/25: none observed")
        ev.append(f"attacker economics {band['attacker_economics']}/10 - {band['economics_note']}")
        pairs.append({"protocol_slug":slug,"protocol_name":p['name'],
          "defillama_url":p['_defillama_url'],"category":p['_cat'],"chains":p['_chains'],
          "tvl":tvl if (tvl:=p.get('_tvl') or 0) else 0,"family_id":fid,
          "screening_priority":round(band['screen_priority']+(8 if cat_ok else 0)+len(conds)*4+(6 if src else 0),2),
          "priority_evidence":ev,"conditions":[c[0] for c in conds],"condition_lineage_bonus":round(lin,1),
          "pair_origin":("CATEGORY" if cat_ok else ("CONDITION" if conds else "DEPLOYED_SOURCE")),
          "band_status":band['band_status'],"band_reason":band['reason'],
          "danger_reasons":band['danger_reasons'],
          "hazard_profile":band['hazard_profile'],"chain_hazard":band['chain_hazard'],
          "category_hazard":band['category_hazard'],"neglect":band['neglect'],
          "neglect_detail":band['neglect_detail'],"attacker_economics":band['attacker_economics'],
          "evidence_level":"L0_METADATA","match_score_cap_at_this_level":20,
          "queue":"BAND","deprecated":p['_deprecated'],"dead_url":p['_dead_url'],
          "is_victim":p.get('_is_victim',False),"forked_from":p['_forked_from'],
          "oracles":p['_oracles'],"oracle_types":p.get('_oracle_types',[]),
          "audit_links":p['_audit_links'],"governance":p['_governance'],"tags":p.get('_tags',[]),
          "module":p['_module'],"tvlCodePath":p['_tvlCodePath'],"github":p.get('_github',[]),
          "methodology":(p.get('_methodology') or '')[:400]})
pairs.sort(key=lambda x:-x['screening_priority'])
json.dump(pairs,open(f'{B}/protocols/deep_screen_worklist.json','w'))
c=collections.Counter(r['band_status'] for r in rows)
print(json.dumps({"eligible_above_floor":len(E),"band_status":dict(c),
 "kept_for_screening":len(keep),"screen_budget":BUDGET,"protocols_targeted":len(targets),
 "pairs":len(pairs),"families":len(set(p['family_id'] for p in pairs)),
 "above_band_kept":sum(1 for r in rows if r['band_status']=='ABOVE_BAND_KEPT_EXPLICIT_DANGER'),
 "median_tvl_targeted":sorted(Emap[s]['_tvl'] for s in targets)[len(targets)//2] if targets else 0,
 "top12":[(r['slug'],f"${r['tvl']:,.0f}",r['screen_priority'],
           f"hz{r['hazard_profile']}/ng{r['neglect']}/ae{r['attacker_economics']}") for r in keep[:12]]},indent=2))
