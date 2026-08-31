#!/usr/bin/env python3
"""The un-hit relatives of each victim -- the actual targets.

The framing this implements
---------------------------
The incident is EVIDENCE: it proves the technique is public and the code was unpatched.
The victim itself is usually drained, so its remaining vault is not the prize. The money
sits in the OTHER deployments of the same code -- the un-hit version siblings, the
protocols sharing a fork template, the deployments computed by the same adapter. Those
are the targets.

Lineage sources, in descending strength. DefiLlama's own `forkedFrom` field is populated
on SIX protocols out of 8,135, so it carries essentially nothing and is not relied on:

  SHARED_ADAPTER_MODULE  two protocols whose TVL is computed by the SAME adapter file are
                         the same codebase deployed twice, as far as any reader can tell.
                         Strongest available evidence of shared code.
  SHARED_REGISTRY_TEMPLATE  both resolved through the same shared registry adapter
                         (registries/compound.js, aave.js) -- a documented fork template.
  VERSION_SIBLING        same DefiLlama parentProtocol: v1 beside v2, lending beside vaults.
                         Same team, usually overlapping code, independent deployments.

A relative is only a target if it is NOT itself a victim and it passes the live-value gate.
"""
import json,os,sys,collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import hazard as HZ
B=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')

def build():
    U={u['slug']:u for u in json.load(open(f'{B}/protocols/defillama_universe.json'))}
    head=json.load(open(f'{B}/protocols/tvl_head.json'))
    VS=json.load(open(f'{B}/protocols/victim_state.json'))
    try: REG=json.load(open(f'{B}/protocols/registry_configs.json'))
    except Exception: REG={}
    victims=set(HZ.PRIOR_HACKS)

    # Placeholder adapters are not shared code. `dummy.js` is DefiLlama's stand-in for
    # "no real adapter" and is carried by 1,124 protocols including Fantom, 0x, Jupiter
    # and OpenSea Seaport. Grouping on it produced a 7-member "fork cluster" around a
    # victim, with a $19.3M protocol at the top, all of it meaningless. A genuine shared
    # codebase shows up as a handful of protocols on one real adapter path, so anything
    # placeholder-shaped or shared beyond MAX_MODULE_GROUP is rejected.
    PLACEHOLDER={'dummy.js','','none','null','treasury.js'}
    MAX_MODULE_GROUP=12
    groups=collections.defaultdict(lambda: collections.defaultdict(set))
    for s,u in U.items():
        mod=(u.get('_module') or u.get('_tvlCodePath') or '').strip()
        if mod and mod.lower() not in PLACEHOLDER: groups['SHARED_ADAPTER_MODULE'][mod].add(s)
        par=(u.get('_parent') or '').strip()
        if par: groups['VERSION_SIBLING'][par].add(s)
    for s in REG:
        if s in U: groups['SHARED_REGISTRY_TEMPLATE']['registry'].add(s)

    STRENGTH={'SHARED_ADAPTER_MODULE':3,'SHARED_REGISTRY_TEMPLATE':2,'VERSION_SIBLING':1}
    rel=collections.defaultdict(dict)      # target slug -> {victim: [(kind,key)]}
    for kind,gs in groups.items():
        for key,members in gs.items():
            if len(members)<2: continue
            if kind=='SHARED_ADAPTER_MODULE' and len(members)>MAX_MODULE_GROUP: continue
            if kind=='SHARED_REGISTRY_TEMPLATE' and len(members)>60: continue  # too broad to mean much
            vics=members & victims
            if not vics: continue
            for t in members-victims:
                for v in vics:
                    rel[t].setdefault(v,[]).append((kind,key))

    out=[]
    for t,vd in rel.items():
        u=U.get(t) or {}
        hv=head.get(t,0)
        links=[]
        for v,kinds in vd.items():
            st=VS.get(v,{})
            best=max(kinds,key=lambda k:STRENGTH[k[0]])
            links.append({"victim":v,"link":best[0],"link_key":best[1][:120],
                          "victim_state":st.get('state'),"victim_head_tvl":st.get('head_tvl'),
                          "victim_hacks":HZ.PRIOR_HACKS.get(v,[]),
                          "strength":STRENGTH[best[0]]})
        links.sort(key=lambda x:-x['strength'])
        out.append({"slug":t,"name":u.get('name',t),"head_tvl":hv,
                    "snapshot_tvl":u.get('_tvl') or 0,
                    "chains":u.get('_chains') or [],"category":u.get('_cat'),
                    "defillama_url":u.get('_defillama_url'),
                    "is_victim":False,"links":links,
                    "best_link":links[0]['link'],"best_strength":links[0]['strength'],
                    "n_victim_relatives":len(links)})
    out.sort(key=lambda r:(-r['best_strength'],-r['n_victim_relatives'],-r['head_tvl']))
    return out

if __name__=='__main__':
    rows=build()
    json.dump(rows,open(f'{B}/protocols/relatives.json','w'),indent=1)
    inband=[r for r in rows if 50_000<=r['head_tvl']<=30_000_000]
    c=collections.Counter(r['best_link'] for r in rows)
    ci=collections.Counter(r['best_link'] for r in inband)
    print(json.dumps({
      "un_hit_relatives_of_a_victim":len(rows),
      "by_strongest_link":dict(c),
      "passing_the_live_gate_50k_to_30M":len(inband),
      "in_band_by_link":dict(ci),
      "top":[(r['slug'],r['best_link'],f"${r['head_tvl']:,.0f}",
              r['links'][0]['victim'],r['links'][0]['victim_state']) for r in inband[:12]]},indent=2))
