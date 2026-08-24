#!/usr/bin/env python3
"""Worklist prioritised by the LEARNED attack-surface model (out-of-sample lift x2.32)."""
import json,sys,os,collections,math
sys.path.insert(0,'/home/user/dd1/incident-intelligence/tools')
from matcher import APPLIC, APPLIC_SOURCE
from conditions import COND
import hazard as HZ, attack_surface as AS
from feature_lift_defs import feats, ORDERING_ONLY
B='/home/user/dd1/incident-intelligence'
E=[r for r in json.load(open(f'{B}/protocols/eligibility.json')) if r['_queue']=='MAIN']
FAM={f['family_id']:f for f in json.load(open(f'{B}/families/families.json'))}
PR=json.load(open(f'{B}/protocols/onchain_probes.json')) if os.path.exists(f'{B}/protocols/onchain_probes.json') else {}
AD=json.load(open(f'{B}/protocols/admin_posture.json')) if os.path.exists(f'{B}/protocols/admin_posture.json') else {}
DEEP={}
if os.path.exists(f'{B}/protocols/deep_screened.jsonl'):
    for l in open(f'{B}/protocols/deep_screened.jsonl'):
        d=json.loads(l)
        if not d.get('killed'): DEEP.setdefault(d['protocol_slug'],[]).append(d)
DANGER={'IS_WINDOW_VICTIM_STILL_LIVE','FORK_OF_WINDOW_VICTIM','DEAD_ADAPTER_WITH_RESIDUAL_TVL','HALLMARK_PRIOR_INCIDENT'}
def danger(p):
    r=[f"condition {c}" for c in sorted(set(p.get('_conditions') or []) & DANGER)]
    pr=PR.get(p['slug'],{})
    if any(c.get('status')=='IMPLEMENTATION_NOT_VERIFIED' for c in pr.get('source_sweep',{}).get('contracts',[])):
        r.append("an implementation behind a live proxy is unverified on the explorer")
    b=[d for d in DEEP.get(p['slug'],[]) if d.get('evidence_level')=='L4_GUARD_REVIEW' and d.get('MATCH_SCORE',0)>=70]
    if b: r.append(f"a deployed-source pair already scores {max(d['MATCH_SCORE'] for d in b)} at L4 guard review")
    if HZ.REPEAT_VICTIMS.get(p['slug'],0)>1:
        r.append(f"repeat victim: {HZ.REPEAT_VICTIMS[p['slug']]} recorded hacks")
    return r
def cond_families(p):
    out=collections.defaultdict(list)
    for cid,d in (p.get('_condition_detail') or {}).items():
        if not d.get('families'): continue
        _f,kind,w,_desc=COND[cid]
        for f in d['families']:
            if f in FAM: out[f].append((cid,kind,w,d['evidence']))
    return out

rows=[]
for p in E:
    tvl=p.get('_tvl') or 0
    dz=danger(p)
    status,why=HZ.band_status(tvl,bool(dz))
    f=feats(p['slug'],p,PR,AD=AD)
    surf,hits=AS.surface(f)
    act,actwhy=AS.actionability(tvl, bool(p.get('_audit_links') or p.get('url')))
    rec={"slug":p['slug'],"band_status":status,"band_reason":why,"tvl":tvl,"danger_reasons":dz,
         "attack_surface":surf,"surface_signals":AS.explain(hits),
         "actionability":act,"actionability_reason":actwhy,
         "chain_hazard":HZ.chain_hazard(p.get('_chains')),"category_hazard":HZ.category_hazard(p.get('_cat')),
         "upgrade_authority":(AD.get(p['slug']) or {}).get('posture'),
         "upgrade_authority_detail":(AD.get(p['slug']) or {}).get('posture_detail'),
         "operational_flags":sorted(k for k in ORDERING_ONLY if f.get(k)),
         "repeat_victim_count":HZ.REPEAT_VICTIMS.get(p['slug'],0),
         "prior_hacks":HZ.PRIOR_HACKS.get(p['slug'],[])}
    rec["screen_priority"]=round(surf*(act/100.0)+ (6 if dz else 0),2)
    rows.append(rec)
json.dump(rows,open(f'{B}/protocols/band_screen.json','w'),indent=1)
keep=[r for r in rows if r['band_status'] in ('IN_BAND','ABOVE_BAND_KEPT_EXPLICIT_DANGER')]
keep.sort(key=lambda x:-x['screen_priority'])
BUDGET=int(sys.argv[1]) if len(sys.argv)>1 else 1200
targets={r['slug'] for r in keep[:BUDGET]}
Emap={r['slug']:r for r in E}; band={r['slug']:r for r in keep}
pairs=[]
for slug in targets:
    p=Emap[slug]; cf=cond_families(p); bd=band[slug]
    fids=set(APPLIC)|set(cf)
    if PR.get(slug,{}).get('deployment',{}).get('addresses_probed'): fids |= APPLIC_SOURCE
    for fid in fids:
        if fid not in FAM: continue
        a=APPLIC.get(fid)
        cat_ok = a is not None and (a.get('cats') is None or p['_cat'] in a['cats'])
        conds=cf.get(fid,[])
        # A pair may be created from deployed source only when a PRECONDITION actually
        # MATCHED. The sweep writes an entry for every family it evaluated, matched or
        # not, so testing for the entry's existence created a pair for every swept
        # protocol: 608 pairs on ACC-QUOTE-STALE-ACROSS-OWN-SWAP where 32 protocols
        # carried the indicator. The unmatched 576 scored ~zero and never reached the
        # finals, but they inflated every pair count in this run's reporting.
        _sig=((PR.get(slug,{}).get('source_sweep',{}).get('family_signals') or {}).get(fid)) or {}
        src=any(h.get('match') and h.get('role')=='PRE' for h in _sig.values())
        if not (cat_ok or conds or (src and fid in APPLIC_SOURCE)): continue
        if a is not None and a.get('requires_governance') and not p['_governance']: continue
        ev=[]; lin=0.0
        ev.append(f"archetype applicable: category={p['_cat']} (blended category hazard x{bd['category_hazard']})"
                  if cat_ok else "pair created by an observed condition or a deployed-source indicator, not by category")
        for cid,kind,w,evd in conds:
            ev.append(f"[{kind}] {cid}: {evd}")
            if kind=='LINEAGE': lin=max(lin,min(15.0,w*0.9))
        ev.append(f"learned attack surface {bd['attack_surface']}/30 from "
                  f"{len(bd['surface_signals'])} measured signals")
        if bd['repeat_victim_count']>1:
            ev.append(f"repeat victim: {bd['repeat_victim_count']} recorded hacks in DefiLlama's dataset")
        pairs.append({"protocol_slug":slug,"protocol_name":p['name'],"defillama_url":p['_defillama_url'],
          "category":p['_cat'],"chains":p['_chains'],"tvl":p.get('_tvl') or 0,"family_id":fid,
          "screening_priority":round(bd['screen_priority']+(8 if cat_ok else 0)+len(conds)*4+(6 if src else 0),2),
          "priority_evidence":ev,"conditions":[c[0] for c in conds],"condition_lineage_bonus":round(lin,1),
          "pair_origin":("CATEGORY" if cat_ok else ("CONDITION" if conds else "DEPLOYED_SOURCE")),
          "band_status":bd['band_status'],"band_reason":bd['band_reason'],"danger_reasons":bd['danger_reasons'],
          "attack_surface":bd['attack_surface'],"surface_signals":bd['surface_signals'],
          "actionability":bd['actionability'],"actionability_reason":bd['actionability_reason'],
          "chain_hazard":bd['chain_hazard'],"category_hazard":bd['category_hazard'],
          "repeat_victim_count":bd['repeat_victim_count'],"prior_hacks":bd['prior_hacks'],
          "evidence_level":"L0_METADATA","match_score_cap_at_this_level":20,"queue":"BAND",
          "deprecated":p['_deprecated'],"dead_url":p['_dead_url'],"is_victim":p.get('_is_victim',False),
          "forked_from":p['_forked_from'],"oracles":p['_oracles'],"oracle_types":p.get('_oracle_types',[]),
          "audit_links":p['_audit_links'],"governance":p['_governance'],"tags":p.get('_tags',[]),
          "module":p['_module'],"tvlCodePath":p['_tvlCodePath'],"github":p.get('_github',[]),
          "methodology":(p.get('_methodology') or '')[:400]})
pairs.sort(key=lambda x:-x['screening_priority'])
json.dump(pairs,open(f'{B}/protocols/deep_screen_worklist.json','w'))
print(json.dumps({"eligible":len(E),"band":dict(collections.Counter(r['band_status'] for r in rows)),
 "kept":len(keep),"targeted":len(targets),"pairs":len(pairs),
 "families":len(set(p['family_id'] for p in pairs)),
 "median_tvl_targeted":sorted(Emap[s]['_tvl'] for s in targets)[len(targets)//2],
 "repeat_victims_in_worklist":len({s for s in targets if HZ.REPEAT_VICTIMS.get(s,0)>1}),
 "top10":[(r['slug'],f"${r['tvl']:,.0f}",r['screen_priority'],f"surf{r['attack_surface']}/act{r['actionability']}")
          for r in keep[:10]]},indent=2))
