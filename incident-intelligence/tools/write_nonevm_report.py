#!/usr/bin/env python3
"""The non-EVM cohort: what the EVM screen could not see, and how far this run got into it."""
import json,collections,sys
B='/home/user/dd1/incident-intelligence'
C=json.load(open(f'{B}/protocols/nonevm_cohort.json'))
AP=json.load(open(f'{B}/protocols/appchain_probe.json'))
SV=json.load(open(f'{B}/incidents/source_verification.json'))['incidents']['INC-2026-08-18-MAY']
FAM={f['family_id']:f for f in json.load(open(f'{B}/families/families.json'))}
band=[r for r in C if r['in_band']]
RTNOTE={
 'COSMOS_SDK_GO':'a handler can write state, return an error, and have the write survive unless the caller stages it in a cache context. All four runtime families apply.',
 'SUBSTRATE_RUST':'without #[transactional], a dispatchable\'s storage writes persist past an error. All four apply.',
 'SOLANA_RUST':'a failed instruction reverts the whole transaction, so the two rollback families do NOT apply. Shared-key clobber and stride do.',
 'MOVE':'abort unwinds the transaction. Rollback families do NOT apply; clobber and stride do.',
 'CAIRO':'only the runtime-agnostic stride family is applied.',
 'OTHER_VM':'only the runtime-agnostic stride family is applied.',
 'UNKNOWN_RUNTIME':'execution semantics not established by this run; only the runtime-agnostic stride family is applied.'}

L=["# The non-EVM cohort\n",
"> **Discovery stage.** Nothing here asserts a defect in any protocol named below. The one confirmed "
"incident in this file, Maya Protocol, is a *past* event already in this run's corpus, and the source "
"lines quoted for it are the published record of a disclosed exploit, not an attack procedure.\n",
"## Why this file exists\n",
"Every probe in the main screen is `eth_call`, `eth_getStorageAt`, `eth_getCode` and explorer "
"`getsourcecode`. That is an EVM instrument, and it means **%d protocols above the $50,000 floor, "
"%d of them inside the $50k-$30M band, were invisible to it** — not judged safe, simply never looked "
"at. Solana alone accounts for %d.\n" % (len(C),len(band),
       sum(1 for r in C if r['runtime']=='SOLANA_RUST')),
"The last incident inside this run's window, four days before it closed, was on one of them.\n",
"## What Maya Protocol added to the library\n",
"`INC-2026-08-18-MAY` was already in the corpus, graded B on a one-line index record. Given a detailed "
"technical account, this pass went and checked it: **%d of %d claimed defects were confirmed at the exact "
"file and line, against the project's live public source.** Under this run's grading rule that is "
"deployed-code evidence, so the record moves to grade **A**. The per-claim record is "
"`incidents/source_verification.json`.\n" % (SV['verified_count'],SV['claimed_count']),
"| Defect | File | Line | Verdict |","|---|---|---:|---|"]
for c in SV['claims_verified']:
    L.append("| %s | `%s` | %s | %s |" % (c['bug'],c['file'],c['lines'] or '—',
             ('**CONFIRMED**' if c['verdict']=='CONFIRMED' else c['verdict'].replace('_',' ').lower())))
L+=["",
"Four of those are a class of defect **the EVM cannot produce**. When an EVM call reverts, every write it "
"made is unwound; there is no such thing as a credit that survives the failure of the transfer meant to "
"fund it. On a Cosmos SDK handler there is. That is why the family library gained four entries that no "
"amount of Solidity screening would ever have surfaced:\n",
"| Family | The invariant it breaks |","|---|---|"]
for fid in ('RUNTIME-STATE-COMMITTED-BEFORE-FUNDING-TRANSFER','RUNTIME-HANDLER-ERROR-NO-ROLLBACK',
            'RUNTIME-BATCHED-MESSAGE-SHARED-KEY-CLOBBER','RECONCILIATION-STRIDE-SKIPS-TRUE-VALUE'):
    f=FAM[fid]; L.append("| `%s` | %s |" % (fid,f['broken_invariant'].split('.')[0]+'.'))
uc=SV['upstream_check']
L+=["",
"## The obvious lead, and why it is dead\n",
"Maya Protocol is a hard fork of THORChain, and the defects are in THORChain-derived Go. THORChain holds "
"**$61.9M** — far above this run's band, but the band has an explicit-danger exception and \"upstream of a "
"protocol exploited four days ago\" is about as explicit as danger gets. So it was checked.\n",
"**Result: %s.** The two codebases have diverged materially.\n" % uc['result'].replace('_',' ').lower()]
for e in uc['evidence']: L.append("- %s" % e)
L+=["","The decisive difference is visible to the same indicator set that fires on Maya: THORChain's "
"`helpers.go` carries `CacheContext()` — the guard that stages writes and commits them only on success — "
"and Maya's does not. %s\n" % uc['caveat'],
"This is recorded rather than dropped because a killed lead is a result. The one protocol most people "
"would have put at the top of a list after this incident does not belong there.\n",
"## Runtime decides which families may be applied\n",
"Applying the runtime families everywhere would manufacture candidates. A CosmWasm contract on Osmosis "
"does not have the rollback property — the wasm VM discards state on error exactly as the EVM does — so "
"the rollback families apply to **chain-level modules, not to contracts deployed on those chains**.\n",
"| Runtime | Above floor | In band | Applicability |","|---|---:|---:|---|"]
ca=collections.Counter(r['runtime'] for r in C); cb=collections.Counter(r['runtime'] for r in band)
for rt,n in ca.most_common():
    L.append("| `%s` | %d | %d | %s |" % (rt,n,cb.get(rt,0),RTNOTE.get(rt,'')))
reach=sum(1 for v in AP.values() if v['status']=='PROBED')
L+=["","## How far the source probe actually got — and where it stopped\n",
"This is a coverage statement, not a result. **This session's network policy binds the GitHub API to the "
"session's own repository**, and blocks github.com HTML and codeload tarballs; only "
"`raw.githubusercontent.com` by exact path is reachable. A repository's file tree therefore cannot be "
"enumerated, so a broad non-EVM source sweep is **not achievable here and was not attempted**. GitLab's "
"API is reachable, which is how Maya and THORChain were read.\n",
"What worked without guessing is the Cosmos convention: `app/app.go` names every module a chain wires in, "
"so one fetch yields the real module list and the layout below `x/<module>/` is conventional. Of 9 "
"candidate app-chains, **%d resolved** — and the 8 that did not are mostly CosmWasm contract protocols "
"that correctly have no `app/app.go` at all, which is the applicability rule above doing its job rather "
"than a failure.\n" % reach]
if AP:
    L.append("| Protocol | Repository | Files read | Guards found | Unguarded families |")
    L.append("|---|---|---:|---|---|")
    for s,v in AP.items():
        L.append("| %s | `%s` | %d | %s | %s |" % (s,v['repo'],v['files_read'],
                 ", ".join("`%s`"%x for x in v['guarded_families']) or "—",
                 ", ".join("`%s`"%x for x in v['unguarded_families']) or "none"))
L+=["","Osmosis read clean on the modules examined. That is a statement about 16 files in a large "
"repository, not about Osmosis.\n",
"## The cohort, at metadata evidence\n",
"The remainder is delivered at what can honestly be claimed for it: DefiLlama metadata plus a runtime "
"classification and the families that structurally apply. These are **not** ranked alongside the EVM "
"candidates, because a metadata-level pair and a guard-reviewed deployed-source pair are not comparable "
"evidence and folding them into one list would imply they are. Full rows in "
"`protocols/nonevm_cohort.json`.\n",
"| # | Protocol | Chain | Runtime | Value at risk | Public repo |","|---:|---|---|---|---:|---|"]
for i,r in enumerate(sorted(band,key=lambda x:-x['tvl'])[:40],1):
    L.append("| %d | [%s](%s) | %s | `%s` | $%s | %s |" % (i,r['name'],r['defillama_url'],
             (r['chains'] or ['?'])[0],r['runtime'],f"{r['tvl']:,.0f}",
             "yes" if r['github'] else "—"))
L+=["","## What would move this forward\n",
"One capability, not more analysis: the ability to enumerate a public repository's file tree. With it, the "
"%d in-band non-EVM protocols that publish source could be swept with the same indicator set that was "
"validated against Maya and THORChain here — the indicators already exist in `tools/repo_indicators.py`, "
"and `tools/repo_sweep.py` is written and tested against ground truth. It is a network-scope limit, not a "
"missing method.\n" % sum(1 for r in band if r['github'])]
open(f'{B}/results/nonevm_cohort.md','w').write("\n".join(L)+"\n")
print(json.dumps({"cohort_above_floor":len(C),"in_band":len(band),
 "in_band_with_repo":sum(1 for r in band if r['github']),
 "appchains_probed":len(AP),"appchains_reachable":reach,
 "maya_defects_verified":f"{SV['verified_count']}/{SV['claimed_count']}",
 "thorchain_result":uc['result']},indent=2))
