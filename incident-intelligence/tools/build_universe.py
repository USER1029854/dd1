#!/usr/bin/env python3
"""Phase F/G: DefiLlama universe -> eligibility -> L0 feature rows."""
import json, re, collections
B='/home/user/dd1/incident-intelligence'
P=json.load(open(f'{B}/sources/defillama/protocols.json'))
CFG=json.load(open(f'{B}/run_config.json'))['operational_settings']
MIN=CFG['minimum_tvl_usd']

# id -> name for fork lineage resolution
byid={str(r['id']):r for r in P}
NONPROTOCOL={'CEX','Chain','Bridge Aggregator','Wallets','Portfolio','Payments'}
NONPROTO_CAT={'CEX'}

def norm(r):
    o=dict(r)  # preserve every returned key
    o['_tvl']=r.get('tvl') or 0
    o['_cat']=r.get('category') or ''
    o['_chains']=r.get('chains') or []
    o['_defillama_url']=f"https://defillama.com/protocol/{r.get('slug')}"
    fids=r.get('forkedFromIds') or []
    o['_forked_from']=[byid[str(f)]['name'] for f in fids if str(f) in byid]
    o['_oracles']=[x.get('name') for x in (r.get('oraclesBreakdown') or [])] or (r.get('oracles') or [])
    o['_oracle_types']={x.get('name'):x.get('type') for x in (r.get('oraclesBreakdown') or [])}
    o['_deprecated']=bool(r.get('deprecated'))
    o['_rugged']=bool(r.get('rugged'))
    o['_dead_url']=bool(r.get('deadUrl'))
    o['_audits_n']=r.get('audits')
    o['_audit_links']=r.get('audit_links') or []
    o['_github']=r.get('github') or []
    o['_governance']=r.get('governanceID') or []
    o['_hallmarks']=r.get('hallmarks') or []
    o['_warnings']=r.get('warningBanners') or []
    o['_prev_names']=r.get('previousNames') or []
    o['_parent']=r.get('parentProtocolSlug')
    o['_module']=r.get('module')
    o['_tvlCodePath']=r.get('tvlCodePath')
    o['_methodology']=r.get('methodology') or ''
    o['_misrep']=bool(r.get('misrepresentedTokens'))
    o['_listedAt']=r.get('listedAt')
    return o

U=[norm(r) for r in P]
json.dump(U, open(f'{B}/protocols/defillama_universe.json','w'))

# ---- eligibility ----
def eligible(o):
    if o['_cat'] in NONPROTO_CAT: return False,'EXCLUDED_CEX_OR_NON_PROTOCOL'
    if o['_cat'] in ('Chain',):   return False,'EXCLUDED_NON_PROTOCOL_CHAIN_ENTRY'
    if o['_rugged']:              return False,'EXCLUDED_FLAGGED_RUGGED'
    if o['_tvl']>=MIN:            return True,'ELIGIBLE_TVL'
    return False,'BELOW_TVL_THRESHOLD'

# high-fit queue for sub-threshold protocols (§10.2)
def high_fit(o):
    r=[]
    if o['_deprecated']:                       r.append('deprecated_deployment_may_retain_live_exposure')
    if o['_dead_url'] and o['_tvl']>50000:     r.append('dead_front_end_with_residual_tvl')
    if o['_warnings']:                         r.append('defillama_warning_banner')
    if o['_cat'] in ('Bridge','Canonical Bridge','Cross Chain Bridge') and o['_tvl']>100000:
                                               r.append('bridge_authority_over_external_value')
    if o['_cat'] in ('Risk Curators','Onchain Capital Allocator') and o['_tvl']>100000:
                                               r.append('curator_authority_over_third_party_vaults')
    if o['_cat'] in ('Dexs','DEX Aggregator','Services') and o['_tvl']>0 and any(
        k in (o.get('description') or '').lower() for k in ('router','aggregat','multicall','execut')):
                                               r.append('router_or_executor_holds_user_approvals')
    if o['_governance'] and o['_tvl']>100000:  r.append('onchain_governance_authority')
    return r

rows=[]
for o in U:
    ok,why=eligible(o)
    hf=high_fit(o)
    rows.append({**{k:v for k,v in o.items() if k.startswith('_') or k in
                    ('id','name','slug','category','chains','tvl','description','methodology')},
                 '_eligible':ok,'_eligibility_reason':why,'_high_fit_flags':hf,
                 '_queue':('MAIN' if ok else ('HIGH_FIT_SUBTHRESHOLD' if hf and o['_tvl']>0 else 'OUT'))})
json.dump(rows, open(f'{B}/protocols/eligibility.json','w'))

c=collections.Counter(r['_queue'] for r in rows)
print(json.dumps({
 "universe":len(U),"main_queue":c['MAIN'],"high_fit_subthreshold":c['HIGH_FIT_SUBTHRESHOLD'],
 "out":c['OUT'],
 "excl_reasons":collections.Counter(r['_eligibility_reason'] for r in rows if not r['_eligible']),
 "deprecated_flagged":sum(1 for r in rows if r['_deprecated']),
 "with_fork_lineage":sum(1 for r in rows if r['_forked_from']),
 "with_governance":sum(1 for r in rows if r['_governance']),
 "no_audit_listed":sum(1 for r in rows if r['_queue']=='MAIN' and not r['_audit_links']),
 "with_oracles_declared":sum(1 for r in rows if r['_oracles']),
},indent=2,default=str))
