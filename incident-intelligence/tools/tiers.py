#!/usr/bin/env python3
"""Assign each protocol its highest urgency tier, from evidence this run holds.

Tier 1  UNREMEDIATED-KNOWN      a public technique exists for THIS code or its upstream,
                                and the fix is not in the deployed artifact
Tier 2  SHARED-DEPENDENCY       an advisory or template live across a POPULATION with no
                                patch-compliance mechanism binding them
Tier 3  DEPENDENCY-IMPAIRMENT   the target holds / is backed by an external system that is
                                itself exposed; the target's own code can be flawless
Tier 4  FORK-OF-RECENT-VICTIM   forked from a protocol exploited in the recent window
Tier 5  NOVEL-HIGH-FIT          strong architecture + live-precondition match, no public
                                disclosure for this deployment (= the old likelihood-first)

Honesty rule carried from the spec: Tier 1 at FULL strength requires confirming the fixed
line is absent from the runtime artifact. This run has not run that per-protocol check, so
Tier-1 rows here carry KNOWN_ISSUE_STATUS_UNKNOWN and the 28-point band, not 40. The
decisive check is named per row so it can be run first.
"""
import json,os,sys,collections,datetime
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import hazard as HZ, urgency as URG
B=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')

def load():
    U={u['slug']:u for u in json.load(open(f'{B}/protocols/defillama_universe.json'))}
    D=[json.loads(l) for l in open(f'{B}/protocols/deep_screened.jsonl')]
    try: CT={r['slug']:r for r in json.load(open(f'{B}/protocols/cosmos_evm_triage.json'))['rows']}
    except Exception: CT={}
    inc=[json.loads(l) for l in open(f'{B}/incidents/included.jsonl')]
    prov=[json.loads(l) for l in open(f'{B}/incidents/provisional.jsonl')]
    return U,D,CT,inc+prov

def window_victim_names(corpus):
    """Targets exploited inside the window, lowercased, for fork/sibling matching."""
    out={}
    for i in corpus:
        t=(i.get('target') or '').strip().lower()
        if t: out[t]=i['event_date']
    return out

ORACLE_PREVALENCE_CAP=40   # above this, one incident cannot make the whole population urgent

def implicated_providers(corpus):
    """Dependency providers named in in-window incidents -> (count, most recent date)."""
    NAMES=['Supra','Reflector','Chainlink','Pyth','API3','RedStone','Chronicle','DIA',
           'Band','Umbrella','Switchboard','Tellor','Stork','eOracle']
    out={}
    for i in corpus:
        blob=(i.get('root_cause') or '')+' '+(i.get('target') or '')
        for n in NAMES:
            if n in blob:
                c,last=out.get(n,(0,''))
                out[n]=(c+1,max(last,i.get('event_date') or ''))
    return out

def build():
    U,D,CT,corpus = load()
    WV = window_victim_names(corpus)
    IMPLICATED = implicated_providers(corpus)
    ORACLE_POP = collections.Counter()
    for x in U.values():
        if (x.get('_tvl') or 0)>=50_000:
            for o in (x.get('_oracles') or []): ORACLE_POP[o]+=1
    # template/dependency populations: how many independent deployments carry each family
    FAM={f['family_id']:f for f in json.load(open(f'{B}/families/families.json'))}
    POP={fid:f['incident_count'] for fid,f in FAM.items()}
    # most recent public technique date per family
    RECENT={fid:f.get('most_recent_event') for fid,f in FAM.items()}

    rows=[]
    for pair in D:
        if pair.get('killed'): continue
        slug=pair['protocol_slug']; u=U.get(slug,{})
        tvl=pair.get('tvl') or 0
        fid=pair['family_id']
        tier=5; rem=URG.NO_PUBLIC_MATCH; why=[]; decisive=None
        tech_date=RECENT.get(fid); population=POP.get(fid,0)

        # ---- Tier 1: a public technique exists for THIS protocol's own code ----
        ph=HZ.PRIOR_HACKS.get(slug) or []
        if ph and tvl>=50_000:
            latest=sorted(ph,key=lambda h:h.get('date') or '',reverse=True)[0]
            tier=1; rem=URG.KNOWN_ISSUE_STATUS_UNKNOWN
            tech_date=latest.get('date') or tech_date
            population=max(population,len(ph))
            why.append("this protocol has %d recorded public incident(s), most recently %s for $%s [%s], "
                       "and still holds $%s" % (len(ph),latest.get('date'),
                       f"{latest.get('amount') or 0:,.0f}",latest.get('technique'),f"{tvl:,.0f}"))
            decisive=("Confirm in the DEPLOYED artifact whether the fix described in the %s postmortem is "
                      "present at the live address. Present -> drop. Absent -> Tier 1, act now." % latest.get('date'))

        # ---- Tier 2: shared dependency / propagating template ----
        if tier>2:
            if slug in CT:
                tier=2; rem=URG.KNOWN_ISSUE_STATUS_UNKNOWN
                population=max(population,len(CT))
                why.append("deployed on %s, a chain running a Cosmos EVM stack covered by the "
                           "ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state "
                           "NOT_DETERMINED" % ", ".join(CT[slug].get('cosmos_evm_chains') or []))
                decisive=("Pin the chain's running github.com/cosmos/evm version AND query live module "
                          "params for the enabled static precompile set -- do not infer either from "
                          "release notes. A vendored x/evm tree will not appear in a dependency scan.")
            elif population>=10 and fid in ('TOKEN-DEFERRED-BURN-LP-RESERVE-DESYNC',
                                            'TOKEN-TRANSFER-INTENT-HEURISTIC-FORGEABLE'):
                tier=2; rem=URG.KNOWN_ISSUE_STATUS_UNKNOWN
                why.append("carries the deferred-burn / transfer-intent template that produced %d "
                           "independent in-window incidents and is still propagating" % population)
                decisive=("Read _transfer in the deployed token: does it burn, reflect or move balance "
                          "already held BY THE PAIR, and is the buy/sell branch decided from a value the "
                          "caller can fabricate? Then check whether sync()/skim() is reachable after it.")

        # ---- Tier 3: dependency impairment (the target's own code can be flawless) ----
        # The exemplar is Blend on Stellar: its contracts were not at fault, but its
        # BACKSTOP is composed of Comet BLND-USDC LP shares, so backstop depositors were
        # impaired by a system Blend does not control. The call-graph never shows this --
        # the protocol merely HOLDS the token.
        #
        # Coverage limit, stated rather than papered over: this run does not carry a
        # per-protocol holdings model, so the only dependency it can evidence is the
        # DECLARED oracle. Prevalence discipline applies -- a provider implicated once and
        # used by 245 protocols does not make 245 protocols urgent, so a provider is only
        # a Tier-3 basis when its user population is small enough for the association to
        # mean something. Backing/collateral/LP holdings are NOT resolved here.
        if tier>3:
            for prov,(n_inc,last) in IMPLICATED.items():
                if prov not in (u.get('_oracles') or []): continue
                if ORACLE_POP.get(prov,0)>ORACLE_PREVALENCE_CAP: continue
                tier=3; rem=URG.KNOWN_ISSUE_STATUS_UNKNOWN
                tech_date=last or tech_date
                population=max(population,ORACLE_POP.get(prov,0))
                why.append("declares %s as an oracle; %s was implicated in %d in-window incident(s), "
                           "most recently %s, and is declared by only %d protocols above the floor -- "
                           "this target inherits its issuer's clock even if its own code is clean"
                           % (prov,prov,n_inc,last,ORACLE_POP.get(prov,0)))
                decisive=("Resolve which price feed / contract the deployment actually calls (declared "
                          "metadata is not code), then carry %s's own remediation status onto this "
                          "target." % prov)
                break

        # ---- Tier 4: fork of an in-window victim ----
        if tier>4:
            fk=(u.get('_forkedFrom') or [])
            hit=[f for f in fk if (f or '').strip().lower() in WV]
            if hit:
                tier=4; rem=URG.KNOWN_ISSUE_STATUS_UNKNOWN
                tech_date=WV[hit[0].strip().lower()]
                why.append("forked from %s, exploited in-window on %s; forks inherit the parent's bug "
                           "and rarely the parent's fix" % (hit[0],tech_date))
                decisive=("Diff the deployed fork against the parent's FIXED version at the specific "
                          "guard the incident turned on. A missing or removed guard is the finding.")
            elif 'FORK_OF_WINDOW_VICTIM' in (u.get('_conditions') or []):
                tier=4; rem=URG.KNOWN_ISSUE_STATUS_UNKNOWN
                why.append("condition FORK_OF_WINDOW_VICTIM: shares lineage with a protocol exploited in-window")
                decisive=("Diff the deployed fork against the parent's fixed version at the guard the "
                          "incident turned on.")

        if tier==5:
            why.append("no public disclosure found for this deployment; ranked on architecture and "
                       "live-precondition match only -- the clock has not started")
            decisive=("Confirm the family's mandatory preconditions in live state, then search for the "
                      "decisive guard in the deployed source.")

        days=URG._days(tech_date) if tech_date else None
        impl_unresolved=any(c.get('status')=='IMPLEMENTATION_NOT_VERIFIED'
                            for c in ((json.loads('{}') if False else {}) or {}).get('x',[])) if False else False
        sc=URG.score(pair,tier,rem,days,population,impl_unresolved)
        rows.append({**sc,"protocol_slug":slug,"protocol_name":pair.get('protocol_name'),
                     "family_id":fid,"tvl":tvl,"evidence_level":pair.get('evidence_level'),
                     "MATCH_SCORE":pair.get('MATCH_SCORE'),
                     "EVIDENCE_CONFIDENCE":pair.get('EVIDENCE_CONFIDENCE'),
                     "defillama_url":pair.get('defillama_url'),"category":pair.get('category'),
                     "chains":pair.get('chains'),"band_status":pair.get('band_status'),
                     "why_clock_is_hot":why,"decisive_check":decisive,
                     "technique_date":tech_date,"technique_days_old":days,"population":population,
                     "prior_hacks":ph})
    rows.sort(key=lambda r:(r['tier'],-r['URGENCY']))
    return rows

if __name__=='__main__':
    rows=build()
    json.dump(rows,open(f'{B}/protocols/urgency_pairs.json','w'))
    c=collections.Counter(r['tier'] for r in rows)
    prot=collections.defaultdict(set)
    for r in rows: prot[r['tier']].add(r['protocol_slug'])
    print(json.dumps({"pairs":len(rows),
      "pairs_by_tier":{f"T{k}":v for k,v in sorted(c.items())},
      "protocols_by_tier":{f"T{k}":len(v) for k,v in sorted(prot.items())},
      "top_urgency":[(r['protocol_slug'],f"T{r['tier']}",r['URGENCY'],r['family_id'][:34],
                      f"${r['tvl']:,.0f}") for r in rows[:10]]},indent=2))
