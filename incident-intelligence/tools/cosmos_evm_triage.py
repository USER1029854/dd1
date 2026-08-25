#!/usr/bin/env python3
"""Triage the Cosmos EVM precompile exposure surface against this run's universe.

What this file is, and deliberately is not
------------------------------------------
It is a CRITERIA-BASED TRIAGE over protocols already in this run's authorised scope.
It is NOT a roster of networks believed to be unpatched. The source report declines to
publish such a roster on the reasoning that the population is small enough that a public
list is a target list, and that patch status is unverifiable from outside without active
probing. Both hold here, so nothing below asserts that any chain is unremediated.

The honest position on the report's six risk archetypes is that most of them need
evidence this run cannot reach, and saying so is more useful than guessing:

  A  vendored / hard-forked cosmos/evm      NOT ASSESSABLE HERE -- needs the chain's
                                            repository tree; this session's network policy
                                            cannot enumerate arbitrary public repos
  B  mitigated by disabling, not upgrading  NOT ASSESSABLE HERE -- needs live Cosmos module
                                            parameters; no Cosmos RPC path is configured
  C  attested only by participation         ASSESSABLE -- the report names the collaborating
                                            organisations, and one of them was halted five
                                            months later
  D  migrated off evmOS onto pre-v0.6.0     NOT ASSESSABLE HERE -- needs upgrade announcements
  E  disabled but governance-reachable      NOT ASSESSABLE HERE -- needs parameters plus an
                                            on-chain governance path
  F  precompiles other than ICS20           PARTIALLY ASSESSABLE -- the vendor scope statement
                                            covers any Cosmos EVM chain using precompiles, so
                                            chain membership is the criterion, not a probe

Of the report's aggravating factors, exactly one is evidenced from this run's own data:
a prior on-chain incident within the last twelve months. That is computed below. The
others (validator-set size, native token used as collateral elsewhere) are not, and are
left unstated rather than estimated.
"""
import json,collections,datetime,os,sys
B=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')

# Chains the report scopes as running a Cosmos SDK stack with an EVM execution layer.
# Membership is the vendor's own scope criterion (any Cosmos EVM chain using precompiles),
# NOT a claim about any chain's patch state.
COSMOS_EVM={'Mantra','MANTRA','Tac','TAC','Saga','Evmos','Kava','Canto','Cronos','Injective',
            'Zeta','ZetaChain','Dymension','Berachain','Sei','Realio','Haqq','Planq',
            'Nibiru','Xion','Initia','Babylon','Lava','Stratos','Shido'}
# Organisations the vendor credited on the ASA-2026-002 remediation. Credited as
# investigation and remediation participants -- with the exception of Saga this is NOT a
# statement that any of them was exploited, and the report's central finding is that
# participation is not evidence of current patch state.
NAMED_PARTICIPANTS={'Saga','Mantra','MANTRA'}
ADVISORIES=[
 {"id":"ASA-2026-002 / GHSA-54gx-3cgr-7mfm / GO-2026-4677","component":"ICS20 precompile",
  "affected":"github.com/cosmos/evm < v0.6.0","patched":"v0.6.0","severity":"Critical",
  "mechanism":"state updates during recursive calls not reflected in the outer execution context; "
              "the same token balance can be used repeatedly within one transaction",
  "confirmed_exploitation":"Saga EVM, 2026-01-21, ~$7M (OUTSIDE this run's window)"},
 {"id":"GHSA-mjfq-3qr2-6g84","component":"any precompile","affected":"evmOS / Cosmos EVM using precompiles",
  "patched":"per-precompile atomic wrapper reverting partial state","severity":"High",
  "mechanism":"a lower EVM call gas limit lets a caller partially execute a precompile and error at a "
              "chosen point without reverting already-written state; also a liveness vector",
  "confirmed_exploitation":"none published"},
 {"id":"GHSA-8pfh-j44r-f654","component":"static and dynamic precompiles",
  "affected":"< v0.3.1 / v0.4.2 / v0.5.0","patched":"v0.3.1, v0.4.2, v0.5.0","severity":"Critical",
  "mechanism":"withheld at disclosure; the advisory states no workaround exists for chains using "
              "precompiles, so upgrading was the only remediation path",
  "confirmed_exploitation":"none published"}]

def prior_incidents(days=365):
    """Chains carrying an on-chain incident within the window. Evidenced, not assumed."""
    H=json.load(open(f'{B}/sources/defillama/hacks.json'))
    OFF={'Key Compromise','Frontend & Infrastructure','Social Engineering','Rugpull'}
    cutoff=datetime.datetime(2026,8,24,tzinfo=datetime.timezone.utc).timestamp()-days*86400
    by=collections.defaultdict(list)
    for h in H:
        if h.get('classification') in OFF or h.get('targetType') in ('CEX','Wallet'): continue
        if (h.get('date') or 0)<cutoff: continue
        for c in (h.get('chain') or h.get('chains') or []) or []:
            by[c].append({"date":datetime.datetime.utcfromtimestamp(h['date']).strftime('%Y-%m-%d'),
                          "amount":h.get('amount'),"technique":h.get('technique')})
    # this run's own in-window corpus, which the hacks dataset does not fully cover
    for f in ('included','provisional'):
        for l in open(f'{B}/incidents/{f}.jsonl'):
            d=json.loads(l)
            for c in (d.get('chains') or []):
                by[c].append({"date":d['event_date'],"amount":d.get('reported_loss_usd'),
                              "technique":"in-window corpus ("+f+")"})
    return by

def main():
    U=json.load(open(f'{B}/protocols/defillama_universe.json'))
    PRI=prior_incidents()
    rows=[]
    for u in U:
        t=u.get('_tvl') or 0
        if t<50_000: continue
        ch=set(u.get('_chains') or [])
        hit=sorted(ch & COSMOS_EVM)
        if not hit: continue
        pri=[]
        for c in hit: pri+= [dict(x,chain=c) for x in PRI.get(c,[])]
        rows.append({
          "slug":u['slug'],"name":u['name'],"tvl":t,"category":u.get('_cat'),
          "defillama_url":u.get('_defillama_url'),
          "cosmos_evm_chains":hit,"all_chains":sorted(ch)[:8],
          "in_band":50_000<=t<=30_000_000,
          "multichain":len(ch)>1,
          "archetype_C_named_participant_chain":sorted(set(hit)&NAMED_PARTICIPANTS) or None,
          "aggravating_prior_incident_12mo":sorted({x['date'] for x in pri})[-3:] or None,
          "patch_status":"NOT_DETERMINED",
          "patch_status_reason":("patch state is unverifiable from outside without active probing of "
                                 "live module parameters and the running binary; no such probe was run "
                                 "and none is asserted"),
        })
    rows.sort(key=lambda r:(not r['in_band'], -(len(r['aggravating_prior_incident_12mo'] or [])), -r['tvl']))
    band=[r for r in rows if r['in_band']]
    out={"generated":"2026-08-24","advisories":ADVISORIES,
         "scope_basis":"chain membership in a Cosmos EVM stack per the vendor scope statement",
         "explicitly_not":"a list of networks believed to be unpatched",
         "assessability":{"A_vendored_fork":"NOT_ASSESSABLE_HERE","B_disabled_not_upgraded":"NOT_ASSESSABLE_HERE",
                          "C_participation_only":"ASSESSABLE","D_migrated_off_evmos":"NOT_ASSESSABLE_HERE",
                          "E_governance_reachable":"NOT_ASSESSABLE_HERE","F_non_ics20_precompiles":"PARTIALLY_ASSESSABLE"},
         "protocols_on_cosmos_evm_chains":len(rows),"in_band":len(band),
         "rows":rows}
    json.dump(out,open(f'{B}/protocols/cosmos_evm_triage.json','w'),indent=1)
    bych=collections.Counter(c for r in rows for c in r['cosmos_evm_chains'])
    print(json.dumps({"protocols_on_cosmos_evm_chains":len(rows),"in_band":len(band),
      "with_prior_incident_12mo":sum(1 for r in band if r['aggravating_prior_incident_12mo']),
      "on_a_named_participant_chain":sum(1 for r in rows if r['archetype_C_named_participant_chain']),
      "by_chain":dict(bych.most_common(12))},indent=2))

if __name__=='__main__': main()
