#!/usr/bin/env python3
"""Expanded Phase H.1: conditions can create a pair on their own, not just re-rank one."""
import json,sys,collections,math
sys.path.insert(0,'/home/user/dd1/incident-intelligence/tools')
from matcher import APPLIC, NOT_SCREENABLE, APPLIC_SOURCE
from conditions import COND
B='/home/user/dd1/incident-intelligence'
E=json.load(open(f'{B}/protocols/eligibility.json'))
FAM={f['family_id']:f for f in json.load(open(f'{B}/families/families.json'))}
Q=[r for r in E if r['_queue']=='MAIN']   # hard $50k floor
import os
PR=json.load(open(f'{B}/protocols/onchain_probes.json')) if os.path.exists(f'{B}/protocols/onchain_probes.json') else {}
def has_deployed_code(slug):
    return bool(PR.get(slug,{}).get('deployment',{}).get('addresses_probed'))
def source_signals(slug,fid):
    return ((PR.get(slug,{}).get('source_sweep',{}).get('family_signals') or {}).get(fid) or {})
DEP_W={'UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY':16,'ACC-REWARD-INDEX-INIT-AND-ORDERING':7,
       'ACC-MULTI-PATH-CREDIT-DRIFT':7,'UPGRADE-INITIALIZER-REACHABLE-LIVE':5}
ORACLE_FAMS={'ORACLE-STALE-OR-SILENT-FALLBACK','ORACLE-SPOT-THIN-LIQUIDITY',
             'ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE','LIQUIDATION-ON-MANIPULABLE-VALUATION'}

def cond_families(p):
    """family_id -> [(condition_id, kind, weight, evidence)] contributed by conditions."""
    out=collections.defaultdict(list)
    for cid,d in (p.get('_condition_detail') or {}).items():
        fams=d.get('families')
        if not fams: continue
        _,kind,w,_desc=COND[cid]
        for f in fams:
            if f in FAM: out[f].append((cid,kind,w,d['evidence']))
    return out

def build_pair(p,fid,a,cf):
    s=0.0; ev=[]; lineage_bonus=0.0; cond_ids=[]
    txt=((p.get('description') or '')+' '+(p.get('_methodology') or '')+' '+(p.get('name') or '')).lower()
    cat_ok = (a is not None) and (a.get('cats') is None or p['_cat'] in a['cats'])
    if a is not None and a.get('requires_governance') and not p['_governance']: return None
    conds=cf.get(fid,[])
    if not cat_ok and not conds: return None
    if cat_ok:
        if a.get('cats') is None: s+=6; ev.append('archetype-agnostic family (applies to any archetype)')
        else: s+=20; ev.append(f"archetype applicable: category={p['_cat']}")
    else:
        s+=14; ev.append("pair created by an observed condition rather than by category: the condition IS the "
                         "applicability evidence for this family")
    for cid,kind,w,evd in conds:
        s+=w; cond_ids.append(cid)
        ev.append(f"[{kind}] {cid}: {evd}")
        if kind=='LINEAGE': lineage_bonus=max(lineage_bonus,min(15.0,w*0.9))
    if a is not None:
        hits=[k for k in a.get('prio_desc',()) if k and k in txt]
        if hits: s+=min(8,2.5*len(hits)); ev.append('description/methodology signals: '+', '.join(hits[:5]))
        fl=a.get('fork_lineage')
        if fl:
            f=[x for x in p['_forked_from'] if any(k in x.lower() for k in fl)]
            if f: s+=16; lineage_bonus=max(lineage_bonus,15.0); ev.append('fork lineage matches a family upstream: '+', '.join(f))
    if p['_deprecated']:
        w=DEP_W.get(fid,3); s+=w; ev.append(f'DefiLlama deprecated flag (weight {w}; ambiguous on its own)')
    if fid in ORACLE_FAMS and not p['_oracles']:
        s+=5; ev.append('no oracle declared in DefiLlama metadata')
    tvl=p['_tvl'] or 0
    s+=min(20, math.log10(max(tvl,1))*2.2); ev.append(f'exposure tilt from TVL ${tvl:,.0f}')
    return {"protocol_slug":p['slug'],"protocol_name":p['name'],
      "defillama_url":p['_defillama_url'],"category":p['_cat'],"chains":p['_chains'],
      "tvl":p['_tvl'],"family_id":fid,"screening_priority":round(s,2),"priority_evidence":ev,
      "conditions":cond_ids,"condition_lineage_bonus":round(lineage_bonus,1),
      "pair_origin":("CATEGORY" if cat_ok else "CONDITION"),
      "evidence_level":"L0_METADATA","match_score_cap_at_this_level":20,
      "queue":p['_queue'],"deprecated":p['_deprecated'],"dead_url":p['_dead_url'],
      "is_victim":p.get('_is_victim',False),
      "forked_from":p['_forked_from'],"oracles":p['_oracles'],"oracle_types":p.get('_oracle_types',[]),
      "audit_links":p['_audit_links'],"governance":p['_governance'],"tags":p.get('_tags',[]),
      "module":p['_module'],"tvlCodePath":p['_tvlCodePath'],"github":p.get('_github',[]),
      "methodology":(p.get('_methodology') or '')[:400]}

pairs=[]
for p in Q:
    cf=cond_families(p)
    fids=set(APPLIC)|set(cf)
    # Source-only families: a pair exists wherever deployed code was actually read, because the
    # deployed-source static-indicator sweep is the applicability evidence for these.
    if has_deployed_code(p['slug']): fids |= APPLIC_SOURCE
    for fid in fids:
        if fid not in FAM: continue
        r=build_pair(p,fid,APPLIC.get(fid),cf)
        if r is None and fid in APPLIC_SOURCE and has_deployed_code(p['slug']):
            sig=source_signals(p['slug'],fid)
            base=18.0+min(20,math.log10(max(p['_tvl'] or 1,1))*2.2)
            ev=["pair created because deployed code was read for this protocol and this family is screened "
                "by deployed-source static indicators rather than by category"]
            if sig:
                base+=10.0*sum(1 for h in sig.values() if h.get('match') and h.get('role')=='PRE')
                ev.append("source indicators matched: "+", ".join(k for k,h in sig.items() if h.get('match')))
            r={"protocol_slug":p['slug'],"protocol_name":p['name'],"defillama_url":p['_defillama_url'],
               "category":p['_cat'],"chains":p['_chains'],"tvl":p['_tvl'],"family_id":fid,
               "screening_priority":round(base,2),"priority_evidence":ev,
               "conditions":sorted(cf.get(fid,[]) and [c[0] for c in cf[fid]] or []),
               "condition_lineage_bonus":0.0,"pair_origin":"DEPLOYED_SOURCE",
               "evidence_level":"L0_METADATA","match_score_cap_at_this_level":20,
               "queue":p['_queue'],"deprecated":p['_deprecated'],"dead_url":p['_dead_url'],
               "is_victim":p.get('_is_victim',False),"forked_from":p['_forked_from'],
               "oracles":p['_oracles'],"oracle_types":p.get('_oracle_types',[]),
               "audit_links":p['_audit_links'],"governance":p['_governance'],"tags":p.get('_tags',[]),
               "module":p['_module'],"tvlCodePath":p['_tvlCodePath'],"github":p.get('_github',[]),
               "methodology":(p.get('_methodology') or '')[:400]}
        if r: pairs.append(r)
pairs.sort(key=lambda x:-x['screening_priority'])
json.dump(pairs,open(f'{B}/protocols/pairs_l0.json','w'))

def tier(t): return 'LARGE' if (t or 0)>=50_000_000 else ('MID' if (t or 0)>=1_000_000 else 'SMALL')
buckets=collections.defaultdict(list)
for p in pairs: buckets[(p['family_id'],tier(p['tvl']))].append(p)
work=[]; PER={'LARGE':8,'MID':7,'SMALL':6}
for (fid,tr),lst in buckets.items(): work += lst[:PER[tr]]
# always include every protocol carrying a high-signal condition
HIGH={'FORK_OF_WINDOW_VICTIM','IS_WINDOW_VICTIM_STILL_LIVE','DEAD_ADAPTER_WITH_RESIDUAL_TVL',
      'DECLARED_FALLBACK_ORACLE','TAG_HOOK_AMM','CO_CURATED_VAULTS','WRONG_LIQUIDITY_FLAG',
      'HALLMARK_PRIOR_INCIDENT','VERSION_SIBLING_LEGACY','RWA_PRICING_SURFACE'}
for p in pairs:
    if set(p['conditions']) & HIGH: work.append(p)
# every pair whose family the deployed-source sweep actually evaluated
for p in pairs:
    if source_signals(p['protocol_slug'],p['family_id']): work.append(p)
seen=set(); ws=[]
for w in sorted(work,key=lambda x:-x['screening_priority']):
    k=(w['protocol_slug'],w['family_id'])
    if k in seen: continue
    seen.add(k); ws.append(w)
json.dump(ws,open(f'{B}/protocols/deep_screen_worklist.json','w'))
print(json.dumps({"protocols_considered":len(Q),"pairs_generated":len(pairs),
 "pairs_created_by_condition_not_category":sum(1 for p in pairs if p['pair_origin']=='CONDITION'),
 "deep_screen_worklist":len(ws),"unique_protocols":len(set(w['protocol_slug'] for w in ws)),
 "families_covered":len(set(w['family_id'] for w in ws)),
 "by_tier":dict(collections.Counter(tier(w['tvl']) for w in ws)),
 "top12":[(w['protocol_slug'],w['family_id'],w['screening_priority'],f"${w['tvl']:,.0f}",w['pair_origin'])
          for w in ws[:12]]},indent=2))
