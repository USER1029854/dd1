#!/usr/bin/env python3
"""Expanded Phase F/G: $50k floor + creative condition layer."""
import json,re,collections,sys
sys.path.insert(0,'/home/user/dd1/incident-intelligence/tools')
from conditions import build, COND
B='/home/user/dd1/incident-intelligence'
P=json.load(open(f'{B}/sources/defillama/protocols.json'))
cfg=json.load(open(f'{B}/run_config.json'))
FLOOR=50_000
dead=json.load(open(f'{B}/protocols/dead_adapters.json'))
DM=json.load(open(f'{B}/protocols/dead_adapter_slug_map.json'))
REG=json.load(open(f'{B}/protocols/registry_configs.json'))
inc=[json.loads(l) for l in open(f'{B}/incidents/included.jsonl')]
prov=[json.loads(l) for l in open(f'{B}/incidents/provisional.jsonl')]

def norm(s): return re.sub(r'[^a-z0-9]','',(s or '').lower())
byname=collections.defaultdict(list)
for r in P:
    byname[norm(r['name'])].append(r); byname[norm(r.get('slug'))].append(r)
    for pn in (r.get('previousNames') or []): byname[norm(pn)].append(r)
victim_slugs=set(); victim_families=collections.defaultdict(set); victim_map={}
for i in inc+prov:
    t=i['target']; cands=set()
    for key in (norm(t), norm(t.split('(')[0])):
        for r in byname.get(key,[]): cands.add(r['slug'])
    for s in cands:
        victim_slugs.add(s); victim_families[s].update(i['family_candidates'])
        victim_map.setdefault(s,[]).append(i['incident_id'])
victim_families={k:sorted(v) for k,v in victim_families.items()}
json.dump({"victim_slugs":sorted(victim_slugs),"victim_families":victim_families,
           "slug_to_incidents":victim_map},open(f'{B}/protocols/victim_map.json','w'),indent=1)

CONDS=build(P,DM,victim_slugs,victim_families,REG)
json.dump(CONDS,open(f'{B}/protocols/conditions.json','w'))

byid={str(r['id']):r for r in P}
NONPROTO={'CEX','Chain'}
rows=[]
for r in P:
    tvl=r.get('tvl') or 0
    c=CONDS.get(r['slug'],{})
    o={k:v for k,v in r.items() if k not in ('chainTvls','logo','tokenBreakdowns','dimensions')}
    o['_tvl']=tvl; o['_cat']=r.get('category') or ''
    o['_chains']=r.get('chains') or []
    o['_defillama_url']=f"https://defillama.com/protocol/{r.get('slug')}"
    o['_forked_from']=[byid[str(f)]['name'] for f in (r.get('forkedFromIds') or []) if str(f) in byid]
    o['_oracles']=[x.get('name') for x in (r.get('oraclesBreakdown') or [])] or (r.get('oracles') or [])
    o['_oracle_types']=sorted({x.get('type') for x in (r.get('oraclesBreakdown') or []) if x.get('type')})
    o['_deprecated']=bool(r.get('deprecated')); o['_rugged']=bool(r.get('rugged'))
    o['_dead_url']=bool(r.get('deadUrl')); o['_dead_from']=r.get('deadFrom')
    o['_audit_links']=r.get('audit_links') or []; o['_github']=r.get('github') or []
    o['_governance']=r.get('governanceID') or []; o['_hallmarks']=r.get('hallmarks') or []
    o['_warnings']=r.get('warningBanners') or []; o['_prev_names']=r.get('previousNames') or []
    o['_parent']=r.get('parentProtocolSlug'); o['_module']=r.get('module')
    o['_tvlCodePath']=r.get('tvlCodePath'); o['_methodology']=r.get('methodology') or ''
    o['_misrep']=bool(r.get('misrepresentedTokens')); o['_tags']=r.get('tags') or []
    o['_conditions']=sorted(c.keys())
    o['_condition_detail']=c
    o['_is_victim']=r['slug'] in victim_slugs
    # eligibility at the $50k floor
    if r.get('category') in NONPROTO:   ok,why=False,'EXCLUDED_CEX_OR_NON_PROTOCOL_CHAIN_ENTRY'
    elif r.get('rugged'):               ok,why=False,'EXCLUDED_FLAGGED_RUGGED'
    elif tvl>=FLOOR:                    ok,why=True,'ELIGIBLE_ABOVE_50K_FLOOR'
    else:                               ok,why=False,'BELOW_50K_FLOOR'
    # sub-floor protocols are only kept when they carry authority over value elsewhere
    authority=[k for k in c if k in ('DEAD_ADAPTER_WITH_RESIDUAL_TVL','IS_WINDOW_VICTIM_STILL_LIVE',
              'AUTHORITY_ADDRESSES_BEYOND_TVL','CO_CURATED_VAULTS','FORK_OF_WINDOW_VICTIM')]
    o['_eligible']=ok; o['_eligibility_reason']=why
    # Operator directive: hard $50,000 floor. Sub-floor protocols are recorded with their
    # authority flags so the information is not lost, but they are never screened or ranked.
    o['_queue']=('MAIN' if ok else 'OUT')
    o['_subfloor_authority_deferred']=bool(authority and tvl>0 and not ok)
    o['_authority_flags']=authority
    rows.append(o)
json.dump(rows,open(f'{B}/protocols/defillama_universe.json','w'))
json.dump([{k:v for k,v in r.items() if k.startswith('_') or k in
            ('id','name','slug','category','chains','tvl','description','methodology','url',
             'change_1d','change_7d','change_1h','mcap','listedAt','address','audits','symbol')} for r in rows],
          open(f'{B}/protocols/eligibility.json','w'))
defer=[{"slug":r['slug'],"name":r['name'],"tvl":r['_tvl'],"category":r['_cat'],
        "authority_flags":r['_authority_flags'],"conditions":r['_conditions'],
        "reason":"below the $50,000 floor; identified as authority-bearing but deliberately not screened"}
       for r in rows if r.get('_subfloor_authority_deferred')]
defer.sort(key=lambda x:-x['tvl'])
json.dump(defer,open(f'{B}/protocols/subfloor_authority_deferred.json','w'),indent=1)
q=collections.Counter(r['_queue'] for r in rows)
cc=collections.Counter()
for r in rows:
    if r['_queue']!='OUT': cc.update(r['_conditions'])
print(json.dumps({"universe":len(rows),"floor_usd":FLOOR,
 "main_queue":q['MAIN'],"subfloor_authority_deferred_not_screened":len(defer),"out":q['OUT'],
 "victims_mapped_to_live_slug":len(victim_slugs),
 "protocols_with_conditions":sum(1 for r in rows if r['_conditions'] and r['_queue']!='OUT'),
 "condition_histogram":dict(cc.most_common())},indent=2))
