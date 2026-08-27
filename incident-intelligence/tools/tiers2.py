#!/usr/bin/env python3
"""Urgency tiers, corrected: the incident is evidence, the un-hit relative is the target.

What changed from tiers.py
--------------------------
The first version put the VICTIM in Tier 1. That was backwards. A drained victim's value
is gone -- a hot clock over an empty vault is not a candidate. Measured: 155 of 283
recorded victims hold less than the floor today. The old Tier-1 list was mostly empty
vaults, and the ones that were not empty were giants (aave-v3 at $17.4bn, venus at
$1.27bn) -- exactly the exposure-weighted noise the operator rejected.

Now:
  * the victim supplies the EVIDENCE (technique public, code was unpatched)
  * its un-hit relatives on the same code are the TARGETS
  * the only victims that remain candidates are those in the RESTORE WINDOW -- restarted,
    refunded or whitehat-restored, holding real money again on the same open door

Three rules, in this order:
  1. GATE on live value read at head. Never historical TVL, never the amount a past
     incident moved. Empty -> out, before anything is scored.
  2. SCORE on reachability, never on magnitude. A small wide-open vault outranks a large
     hard-to-reach one. Putting dollar-size back into the score would re-introduce the
     exposure weighting that made a $3bn protocol top a list for being big.
  3. TIEBREAK on magnitude -- among equals on the same code, prefer the fuller sibling.
"""
import json,os,sys,collections,datetime
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import hazard as HZ, urgency as URG
B=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')
FLOOR=50_000; CEIL=30_000_000

def main():
    U={u['slug']:u for u in json.load(open(f'{B}/protocols/defillama_universe.json'))}
    HEAD=json.load(open(f'{B}/protocols/tvl_head.json'))
    READAT=open(f'{B}/sources/defillama/protocols_head.readat').read().strip()
    VS=json.load(open(f'{B}/protocols/victim_state.json'))
    REL={r['slug']:r for r in json.load(open(f'{B}/protocols/relatives.json'))}
    D=[json.loads(l) for l in open(f'{B}/protocols/deep_screened.jsonl')]
    try: CT={r['slug']:r for r in json.load(open(f'{B}/protocols/cosmos_evm_triage.json'))['rows']}
    except Exception: CT={}
    FAM={f['family_id']:f for f in json.load(open(f'{B}/families/families.json'))}
    POP={fid:f['incident_count'] for fid,f in FAM.items()}
    RECENT={fid:f.get('most_recent_event') for fid,f in FAM.items()}
    victims=set(HZ.PRIOR_HACKS)

    gate_log=collections.Counter()
    rows=[]
    for pair in D:
        if pair.get('killed'): continue
        slug=pair['protocol_slug']
        live=HEAD.get(slug,0)

        # ---------- RULE 1: hard gate on live value, BEFORE any scoring ----------
        if live<FLOOR:
            gate_log['EXCLUDED_EMPTY_OR_BELOW_FLOOR']+=1; continue
        is_victim = slug in victims
        vstate = (VS.get(slug) or {}).get('state')
        if is_victim and vstate!='RESTORED':
            gate_log['EXCLUDED_VICTIM_NOT_IN_RESTORE_WINDOW']+=1; continue

        rel=REL.get(slug)
        hot_dep = slug in CT or (POP.get(pair['family_id'],0)>=10 and
                   pair['family_id'] in ('TOKEN-DEFERRED-BURN-LP-RESERVE-DESYNC',
                                         'TOKEN-TRANSFER-INTENT-HEURISTIC-FORGEABLE'))
        if live>CEIL and not (rel or hot_dep or vstate=='RESTORED'):
            gate_log['EXCLUDED_ABOVE_BAND_NO_EXPLICIT_DANGER']+=1; continue

        fid=pair['family_id']
        tier=5; rem=URG.NO_PUBLIC_MATCH; why=[]; decisive=None
        tech_date=RECENT.get(fid); population=POP.get(fid,0)

        # ---------- restore window: the highest-sensitivity moment in the model ----------
        if vstate=='RESTORED':
            st=VS[slug]
            tier=1; rem=URG.KNOWN_ISSUE_STATUS_UNKNOWN
            h=sorted(HZ.PRIOR_HACKS[slug],key=lambda x:x.get('date') or '',reverse=True)[0]
            tech_date=h.get('date') or tech_date
            population=max(population,len(HZ.PRIOR_HACKS[slug]))
            why.append("RESTORE WINDOW: %s. It is holding real money again; if the fix is not in "
                       "the deployed artifact it is the same open door." % st['basis'])
            decisive=("Confirm the fix from the %s postmortem is present in the DEPLOYED artifact at "
                      "the live address, not merely in the repo or a release note. Absent -> act now."
                      % h.get('date'))

        # ---------- T1: un-hit protocol running the same code as a hit sibling ----------
        if tier>1 and rel and rel['best_strength']>=2:
            L=rel['links'][0]
            tier=1; rem=URG.KNOWN_ISSUE_STATUS_UNKNOWN
            vh=sorted(L['victim_hacks'],key=lambda x:x.get('date') or '',reverse=True)
            if vh: tech_date=vh[0].get('date') or tech_date
            population=max(population,rel['n_victim_relatives'])
            why.append("un-hit deployment on the same code as %s (%s), which was exploited%s. That "
                       "sibling is %s; this one holds $%s. The incident is the evidence, this is the target."
                       % (L['victim'],L['link'].replace('_',' ').lower(),
                          (" on "+vh[0].get('date')) if vh else "",
                          (L['victim_state'] or 'state unknown').replace('_',' ').lower(),
                          f"{live:,.0f}"))
            decisive=("Diff this deployment against the sibling's FIXED version at the exact guard the "
                      "%s incident turned on, in the deployed artifact. Guard present -> drop. Absent -> act."
                      % (vh[0].get('date') if vh else 'sibling'))

        # ---------- T2: shared dependency / propagating template ----------
        if tier>2 and hot_dep:
            tier=2; rem=URG.KNOWN_ISSUE_STATUS_UNKNOWN
            if slug in CT:
                population=max(population,len(CT))
                why.append("deployed on %s, a chain running a Cosmos EVM stack covered by the "
                           "ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state "
                           "NOT_DETERMINED" % ", ".join(CT[slug].get('cosmos_evm_chains') or []))
                decisive=("Pin the chain's running github.com/cosmos/evm version AND query live module "
                          "params for the enabled precompile set. A vendored x/evm tree will not appear "
                          "in a dependency scan.")
            else:
                why.append("carries the deferred-burn / transfer-intent template behind %d independent "
                           "in-window incidents, still propagating (FH token, ~3 days after the window "
                           "closed)" % population)
                decisive=("Read _transfer in the deployed token: does it burn or move balance already held "
                          "BY THE PAIR, and is the buy/sell branch decided from a value the caller can "
                          "fabricate? Then check sync()/skim() reachability.")

        # ---------- T4: version sibling of a recent-window victim ----------
        if tier>4 and rel:
            L=rel['links'][0]
            vh=sorted(L['victim_hacks'],key=lambda x:x.get('date') or '',reverse=True)
            tier=4; rem=URG.KNOWN_ISSUE_STATUS_UNKNOWN
            if vh: tech_date=vh[0].get('date') or tech_date
            population=max(population,rel['n_victim_relatives'])
            why.append("version sibling of %s, exploited%s; forks and siblings inherit the parent's bug "
                       "and rarely the parent's fix. That sibling is %s; this one holds $%s."
                       % (L['victim'],(" on "+vh[0].get('date')) if vh else "",
                          (L['victim_state'] or 'state unknown').replace('_',' ').lower(),f"{live:,.0f}"))
            decisive=("Diff this deployment against the sibling at the guard the incident turned on. A "
                      "missing or REMOVED guard is the finding.")

        if tier==5:
            why.append("no public disclosure for this deployment and no hit relative found; the clock "
                       "has not started")
            decisive=("Confirm the family's mandatory preconditions in live state, then search the "
                      "deployed source for the decisive guard.")

        days=URG._days(tech_date) if tech_date else None
        pv=dict(pair); pv['tvl']=live          # score reads live value only for reporting, never for points
        sc=URG.score(pv,tier,rem,days,population)
        rows.append({**sc,"protocol_slug":slug,"protocol_name":pair.get('protocol_name'),
                     "family_id":fid,"live_value_usd":live,"live_read_at":READAT,
                     "snapshot_tvl":pair.get('tvl'),
                     "evidence_level":pair.get('evidence_level'),"MATCH_SCORE":pair.get('MATCH_SCORE'),
                     "EVIDENCE_CONFIDENCE":pair.get('EVIDENCE_CONFIDENCE'),
                     "defillama_url":pair.get('defillama_url'),"category":pair.get('category'),
                     "chains":pair.get('chains'),
                     "is_restored_victim":vstate=='RESTORED',
                     "relative_of":[{"victim":l['victim'],"link":l['link'],
                                     "victim_state":l['victim_state'],
                                     "victim_holds_now":l['victim_head_tvl']}
                                    for l in (rel['links'][:3] if rel else [])],
                     "why_clock_is_hot":why,"decisive_check":decisive,
                     "technique_date":tech_date,"technique_days_old":days,"population":population})

    # RULE 3: magnitude is the TIEBREAK only -- among equals, prefer the fuller sibling
    rows.sort(key=lambda r:(r['tier'],-r['URGENCY'],-r['live_value_usd']))
    json.dump(rows,open(f'{B}/protocols/urgency_pairs.json','w'))
    prot=collections.defaultdict(set)
    for r in rows: prot[r['tier']].add(r['protocol_slug'])
    print(json.dumps({"live_read_at":READAT,"pairs_after_gate":len(rows),
      "gate_exclusions":dict(gate_log),
      "protocols_by_tier":{f"T{k}":len(v) for k,v in sorted(prot.items())},
      "restore_window_protocols":sorted({r['protocol_slug'] for r in rows if r['is_restored_victim']}),
      "top":[(r['protocol_slug'],f"T{r['tier']}",r['URGENCY'],f"${r['live_value_usd']:,.0f}",
              (r['relative_of'][0]['victim'] if r['relative_of'] else '-')) for r in rows[:10]]},indent=2))

if __name__=='__main__': main()
