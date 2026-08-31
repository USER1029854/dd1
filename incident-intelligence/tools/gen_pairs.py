#!/usr/bin/env python3
"""Phase H.1: generate protocol-family pairs, family-conditional screening priority,
then stratify a deep-screen worklist across families and exposure tiers."""
import json,sys,collections,math
sys.path.insert(0,'/home/user/dd1/incident-intelligence/tools')
from matcher import APPLIC, NOT_SCREENABLE
B='/home/user/dd1/incident-intelligence'
E=json.load(open(f'{B}/protocols/eligibility.json'))
FAM={f['family_id']:f for f in json.load(open(f'{B}/families/families.json'))}
Q=[r for r in E if r['_queue'] in ('MAIN','HIGH_FIT_SUBTHRESHOLD')]

# Deprecation is a *mandatory precondition* only for the legacy-deployment family;
# elsewhere it is a weak prioritisation signal.
DEP_W={'UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY':16,'ACC-REWARD-INDEX-INIT-AND-ORDERING':7,
       'ACC-MULTI-PATH-CREDIT-DRIFT':7,'UPGRADE-INITIALIZER-REACHABLE-LIVE':5}
ORACLE_FAMS={'ORACLE-STALE-OR-SILENT-FALLBACK','ORACLE-SPOT-THIN-LIQUIDITY',
             'ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE','LIQUIDATION-ON-MANIPULABLE-VALUATION'}

def prio(p,fid,a):
    s=0.0; ev=[]
    txt=((p.get('description') or '')+' '+(p.get('_methodology') or '')+' '+(p.get('name') or '')).lower()
    if a.get('cats') is None: s+=6; ev.append('archetype-agnostic family (applies to any archetype)')
    elif p['_cat'] in a['cats']: s+=20; ev.append(f"archetype applicable: category={p['_cat']}")
    else: return None
    if a.get('requires_governance') and not p['_governance']: return None
    hits=[k for k in a.get('prio_desc',()) if k and k in txt]
    if hits: s+=min(10,3*len(hits)); ev.append('description/methodology signals: '+', '.join(hits[:5]))
    fl=a.get('fork_lineage')
    if fl:
        f=[x for x in p['_forked_from'] if any(k in x.lower() for k in fl)]
        if f: s+=16; ev.append('fork lineage matches a family upstream: '+', '.join(f))
    if p['_deprecated']:
        w=DEP_W.get(fid,3); s+=w; ev.append(f'DefiLlama deprecated flag (weight {w} for this family)')
    if p['_dead_url'] and (p['_tvl'] or 0)>10000:
        w=8 if fid=='UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY' else 3
        s+=w; ev.append('dead front end with residual TVL')
    if p['_warnings']: s+=5; ev.append('DefiLlama warning banner')
    if not p['_audit_links']: s+=5; ev.append('no audit link listed (prioritisation signal only, never evidence of a defect)')
    if p['_misrep']: s+=4; ev.append('misrepresentedTokens flag')
    if p['_high_fit_flags']: s+=6; ev.append('sub-threshold high-fit: '+', '.join(p['_high_fit_flags']))
    if len(p['_chains'])>3: s+=4; ev.append(f"multi-chain surface ({len(p['_chains'])} chains)")
    if fid in ORACLE_FAMS:
        if not p['_oracles']: s+=6; ev.append('no oracle declared in DefiLlama metadata (unknown pricing path)')
        elif len(p['_oracles'])==1: s+=4; ev.append(f"single declared oracle: {p['_oracles'][0]}")
    if fid=='GOV-CHEAP-CONTROL-NO-TIMELOCK' and p['_governance']:
        s+=10; ev.append('on-chain governance registered: '+', '.join(map(str,p['_governance'][:2])))
    tvl=p['_tvl'] or 0
    s+=min(20, math.log10(max(tvl,1))*2.2); ev.append(f'exposure tilt from TVL ${tvl:,.0f}')
    return round(s,2),ev

pairs=[]
for p in Q:
    for fid,a in APPLIC.items():
        r=prio(p,fid,a)
        if not r: continue
        s,ev=r
        pairs.append({"protocol_slug":p['slug'],"protocol_name":p['name'],
          "defillama_url":p['_defillama_url'],"category":p['_cat'],"chains":p['_chains'],
          "tvl":p['_tvl'],"family_id":fid,"screening_priority":s,"priority_evidence":ev,
          "evidence_level":"L0_METADATA","match_score_cap_at_this_level":20,
          "queue":p['_queue'],"deprecated":p['_deprecated'],"dead_url":p['_dead_url'],
          "forked_from":p['_forked_from'],"oracles":p['_oracles'],
          "audit_links":p['_audit_links'],"governance":p['_governance'],
          "module":p['_module'],"tvlCodePath":p['_tvlCodePath'],
          "github":p.get('_github',[]),"methodology":(p.get('_methodology') or '')[:400]})
pairs.sort(key=lambda x:-x['screening_priority'])
json.dump(pairs,open(f'{B}/protocols/pairs_l0.json','w'))

# ---- stratified deep-screen worklist: per family x exposure tier ----
def tier(t): return 'LARGE' if (t or 0)>=50_000_000 else ('MID' if (t or 0)>=1_000_000 else 'SMALL')
buckets=collections.defaultdict(list)
for p in pairs: buckets[(p['family_id'],tier(p['tvl']))].append(p)
work=[]; PER={'LARGE':4,'MID':3,'SMALL':2}
for (fid,tr),lst in buckets.items(): work += lst[:PER[tr]]
# de-duplicate identical (slug,family)
seen=set(); ws=[]
for w in sorted(work,key=lambda x:-x['screening_priority']):
    k=(w['protocol_slug'],w['family_id'])
    if k in seen: continue
    seen.add(k); ws.append(w)
json.dump(ws,open(f'{B}/protocols/deep_screen_worklist.json','w'),indent=1)
json.dump({k:{"reason":v,"family_incident_count":FAM[k]['incident_count'],
              "family_loss_usd":FAM[k]['six_month_loss_usd'],
              "handled_as":"read-only sweep over deep-screened deployments"}
           for k,v in NOT_SCREENABLE.items()},
          open(f'{B}/protocols/families_not_screenable_in_universe.json','w'),indent=2)
print(json.dumps({"protocols_considered":len(Q),"pairs_generated":len(pairs),
 "deep_screen_worklist":len(ws),"unique_protocols_in_worklist":len(set(w['protocol_slug'] for w in ws)),
 "families_covered":len(set(w['family_id'] for w in ws)),
 "by_tier":collections.Counter(tier(w['tvl']) for w in ws),
 "top15":[(w['protocol_slug'],w['family_id'],w['screening_priority'],f"${w['tvl']:,.0f}") for w in ws[:15]]},indent=2))
