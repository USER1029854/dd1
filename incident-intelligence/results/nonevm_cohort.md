# The non-EVM cohort

> **Discovery stage.** Nothing here asserts a defect in any protocol named below. The one confirmed incident in this file, Maya Protocol, is a *past* event already in this run's corpus, and the source lines quoted for it are the published record of a disclosed exploit, not an attack procedure.

## Why this file exists

Every probe in the main screen is `eth_call`, `eth_getStorageAt`, `eth_getCode` and explorer `getsourcecode`. That is an EVM instrument, and it means **717 protocols above the $50,000 floor, 621 of them inside the $50k-$30M band, were invisible to it** — not judged safe, simply never looked at. Solana alone accounts for 169.

The last incident inside this run's window, four days before it closed, was on one of them.

## The correction that reshaped this cohort

The first version of this cohort was sized by **how many protocols each chain has**. That is a popularity measure, not a risk measure, and it produced a cohort that was 40% Solana. Measured against incidents that ordering is backwards.

`hazard = incident share / protocol share`, over DefiLlama's on-chain incidents using the same root-cause exclusions as this run's inclusion gate. Above 1 means over-represented among actual victims relative to how much of the universe the chain is.

| Chain | Hazard | Incidents | Protocols | Family | Was given |
|---|---:|---:|---:|---|---|
| EOS | **×7.02** | 15 | 18 | other | **never considered** |
| Acala | **×5.05** | 3 | 5 | Substrate | 10 slots (Substrate) |
| Terra | **×3.37** | 4 | 10 | Cosmos | 40 slots (Cosmos) |
| Secret | **×2.10** | 2 | 8 | Cosmos | 40 slots (Cosmos) |
| Osmosis | **×1.40** | 2 | 12 | Cosmos | 40 slots (Cosmos) |
| Stacks | **×1.12** | 2 | 15 | other | — |
| Hedera | **×1.10** | 3 | 23 | other | — |
| NEAR | **×1.09** | 4 | 31 | other | — |
| Solana | **×0.63** | 22 | 293 | other | **169 slots — the largest share** |
| Sui | **×0.59** | 6 | 86 | other | 102 slots (Move) |
| TON | **×0.34** | 2 | 50 | other | — |

Aggregated, the Cosmos family measures **×2.25** and everything else non-EVM **×0.74**. This run's own in-window corpus agrees independently: 6 Solana incidents against roughly 7 across Cosmos-family chains (Coreum, Quicksilver, Secret, Axelar, Osmosis, a THORChain fork, Dango), from a Solana protocol base an order of magnitude larger.

The cohort is now ordered by measured hazard. A chain below the support floor — fewer than 3 protocols or 2 incidents — is marked `UNMEASURED` and never promoted on a guess, because a ratio built on one incident is noise, not evidence.

**Frequency and severity disagree, and both are kept.** Bridges are the clearest case: by frequency the `Bridge` category is *under*-represented at ×0.80 (12 incidents across 108 protocols), yet it carries **$1.22bn** — the largest loss of any category — at roughly $102M per incident. For an operator working a $50k–$30M band that severity is out of reach by construction, and the band filter removes those protocols before scoring. So the ranking uses frequency and severity is reported beside it rather than folded in.

**Only 56 of the 621 in-band non-EVM protocols sit on a chain measuring hazard ≥ 1.** That, not 621, is the set worth attention.

## What Maya Protocol added to the library

`INC-2026-08-18-MAY` was already in the corpus, graded B on a one-line index record. Given a detailed technical account, this pass went and checked it: **5 of 6 claimed defects were confirmed at the exact file and line, against the project's live public source.** Under this run's grading rule that is deployed-code evidence, so the record moves to grade **A**. The per-claim record is `incidents/source_verification.json`.

| Defect | File | Line | Verdict |
|---|---|---:|---|
| batched MsgDeposit overwrites one voter keyed on the shared tx id | `x/mayachain/handler_deposit.go` | 283,287 | **CONFIRMED** |
| outbound matcher walks heights by a fixed stride and can skip the true height | `x/mayachain/handler_common_outbound.go` | 88-92 | **CONFIRMED** |
| subsidy value computed from a pool ratio with no cap by the pool's asset balance | `x/mayachain/helpers.go` | 224 | **CONFIRMED** |
| pool balance committed before the transfer meant to fund it | `x/mayachain/helpers.go` | ~250-266 | **CONFIRMED** |
| dispatcher logs the handler error and continues in the same context | `x/mayachain/handler_observed_txout.go` | 282-290 | **CONFIRMED** |
| pool unit dilution via near-zero-asset add liquidity | `pool unit math` | — | not verified here |

Four of those are a class of defect **the EVM cannot produce**. When an EVM call reverts, every write it made is unwound; there is no such thing as a credit that survives the failure of the transfer meant to fund it. On a Cosmos SDK handler there is. That is why the family library gained four entries that no amount of Solidity screening would ever have surfaced:

| Family | The invariant it breaks |
|---|---|
| `RUNTIME-STATE-COMMITTED-BEFORE-FUNDING-TRANSFER` | A balance may not be credited until the value backing it has actually moved. |
| `RUNTIME-HANDLER-ERROR-NO-ROLLBACK` | A failed operation must leave no trace. |
| `RUNTIME-BATCHED-MESSAGE-SHARED-KEY-CLOBBER` | Distinct logical operations must not share a mutable state key. |
| `RECONCILIATION-STRIDE-SKIPS-TRUE-VALUE` | A search for a record that exists must find it. |

## The obvious lead, and why it is dead

Maya Protocol is a hard fork of THORChain, and the defects are in THORChain-derived Go. THORChain holds **$61.9M** — far above this run's band, but the band has an explicit-danger exception and "upstream of a protocol exploited four days ago" is about as explicit as danger gets. So it was checked.

**Result: no match on any verified defect.** The two codebases have diverged materially.

- x/thorchain/helpers.go contains no subsidizePoolWithSlashBond* function; its AssetValueInRune call sites (937, 1078, 1286) are in unrelated functions, and SetPool(ctx, pool) appears once (line 317) outside a subsidy path.
- x/thorchain/handler_common_outbound.go does not use the plain stride loop. It computes a per-chain searchPeriod (xmrSigningPeriodMultiplier, evmAggregatorSigningPeriodMultiplier, evmTokenSigningPeriodMultiplier, lines 98-105) and its comment states the window is bounded by 'one signingTransPeriod ago, whichever is later'.
- x/thorchain/handler_deposit.go constructs its voter at lines 215-219 with different surrounding structure.
- x/thorchain/handler_observed_txout.go is 2,855 bytes against Maya's 12,418; the dispatcher shape differs.

The decisive difference is visible to the same indicator set that fires on Maya: THORChain's `helpers.go` carries `CacheContext()` — the guard that stages writes and commits them only on success — and Maya's does not. This compares the current develop branch of each repository. It establishes that these five shapes are not present there now. It is not a general safety statement about THORChain, and no other defect class was searched for.

This is recorded rather than dropped because a killed lead is a result. The one protocol most people would have put at the top of a list after this incident does not belong there.

## Runtime decides which families may be applied

Applying the runtime families everywhere would manufacture candidates. A CosmWasm contract on Osmosis does not have the rollback property — the wasm VM discards state on error exactly as the EVM does — so the rollback families apply to **chain-level modules, not to contracts deployed on those chains**.

| Runtime | Above floor | In band | Applicability |
|---|---:|---:|---|
| `OTHER_VM` | 255 | 219 | only the runtime-agnostic stride family is applied. |
| `SOLANA_RUST` | 169 | 127 | a failed instruction reverts the whole transaction, so the two rollback families do NOT apply. Shared-key clobber and stride do. |
| `UNKNOWN_RUNTIME` | 121 | 114 | execution semantics not established by this run; only the runtime-agnostic stride family is applied. |
| `MOVE` | 102 | 94 | abort unwinds the transaction. Rollback families do NOT apply; clobber and stride do. |
| `COSMOS_SDK_GO` | 40 | 38 | a handler can write state, return an error, and have the write survive unless the caller stages it in a cache context. All four runtime families apply. |
| `CAIRO` | 20 | 19 | only the runtime-agnostic stride family is applied. |
| `SUBSTRATE_RUST` | 10 | 10 | without #[transactional], a dispatchable's storage writes persist past an error. All four apply. |

## How far the source probe actually got — and where it stopped

This is a coverage statement, not a result. **This session's network policy binds the GitHub API to the session's own repository**, and blocks github.com HTML and codeload tarballs; only `raw.githubusercontent.com` by exact path is reachable. A repository's file tree therefore cannot be enumerated, so a broad non-EVM source sweep is **not achievable here and was not attempted**. GitLab's API is reachable, which is how Maya and THORChain were read.

What worked without guessing is the Cosmos convention: `app/app.go` names every module a chain wires in, so one fetch yields the real module list and the layout below `x/<module>/` is conventional. Of 9 candidate app-chains, **1 resolved** — and the 8 that did not are mostly CosmWasm contract protocols that correctly have no `app/app.go` at all, which is the applicability rule above doing its job rather than a failure.

| Protocol | Repository | Files read | Guards found | Unguarded families |
|---|---|---:|---|---|
| osmosis-dex | `osmosis-labs/osmosis` | 16 | `RECONCILIATION-STRIDE-SKIPS-TRUE-VALUE`, `RUNTIME-HANDLER-ERROR-NO-ROLLBACK` | none |

Osmosis read clean on the modules examined. That is a statement about 16 files in a large repository, not about Osmosis.

## The cohort, at metadata evidence

The remainder is delivered at what can honestly be claimed for it: DefiLlama metadata plus a runtime classification and the families that structurally apply. These are **not** ranked alongside the EVM candidates, because a metadata-level pair and a guard-reviewed deployed-source pair are not comparable evidence and folding them into one list would imply they are. Full rows in `protocols/nonevm_cohort.json`.

Ordered by measured chain hazard, then exposure.

| # | Protocol | Chain | Hazard | Runtime | Value at risk | Public repo |
|---:|---|---|---:|---|---:|---|
| 1 | [Vaulta REX](https://defillama.com/protocol/vaulta-rex) | EOS | ×7.02 | `OTHER_VM` | $29,505,988 | — |
| 2 | [WhaleEx](https://defillama.com/protocol/whaleex) | EOS | ×7.02 | `OTHER_VM` | $3,569,528 | — |
| 3 | [Vaulta RAM](https://defillama.com/protocol/vaulta-ram) | EOS | ×7.02 | `OTHER_VM` | $1,805,436 | — |
| 4 | [Alcor Exchange](https://defillama.com/protocol/alcor-exchange) | Wax | ×7.02 | `OTHER_VM` | $171,936 | — |
| 5 | [DMD Finance](https://defillama.com/protocol/dmd-finance) | EOS | ×7.02 | `OTHER_VM` | $138,719 | — |
| 6 | [PayCash](https://defillama.com/protocol/paycash) | EOS | ×7.02 | `OTHER_VM` | $112,093 | — |
| 7 | [Vigor](https://defillama.com/protocol/vigor) | EOS | ×7.02 | `OTHER_VM` | $110,209 | — |
| 8 | [DFS Network](https://defillama.com/protocol/dfs-network) | EOS | ×7.02 | `OTHER_VM` | $96,033 | yes |
| 9 | [Acala LCDOT](https://defillama.com/protocol/acala-lcdot) | Acala | ×5.05 | `SUBSTRATE_RUST` | $2,181,137 | — |
| 10 | [Acala Liquid Staking](https://defillama.com/protocol/acala-liquid-staking) | Acala | ×5.05 | `SUBSTRATE_RUST` | $1,911,243 | — |
| 11 | [Acala Euphrates](https://defillama.com/protocol/acala-euphrates) | Acala | ×5.05 | `SUBSTRATE_RUST` | $235,755 | — |
| 12 | [Taiga Acala](https://defillama.com/protocol/taiga-acala) | Acala | ×5.05 | `SUBSTRATE_RUST` | $69,168 | — |
| 13 | [Terraswap](https://defillama.com/protocol/terraswap) | Terra | ×3.37 | `COSMOS_SDK_GO` | $346,102 | — |
| 14 | [GarudaDefi](https://defillama.com/protocol/garudadefi) | Terra | ×3.37 | `COSMOS_SDK_GO` | $215,751 | — |
| 15 | [Terraport](https://defillama.com/protocol/terraport) | Terra | ×3.37 | `COSMOS_SDK_GO` | $113,858 | — |
| 16 | [ShadeLend](https://defillama.com/protocol/shadelend) | Secret | ×2.10 | `COSMOS_SDK_GO` | $253,105 | — |
| 17 | [SecretSwap](https://defillama.com/protocol/secretswap) | Secret | ×2.10 | `COSMOS_SDK_GO` | $239,103 | — |
| 18 | [BtnGroup](https://defillama.com/protocol/btngroup) | Secret | ×2.10 | `COSMOS_SDK_GO` | $164,613 | — |
| 19 | [ShadeSwap](https://defillama.com/protocol/shadeswap) | Secret | ×2.10 | `COSMOS_SDK_GO` | $159,953 | — |
| 20 | [SiennaSwap](https://defillama.com/protocol/siennaswap) | Secret | ×2.10 | `COSMOS_SDK_GO` | $141,963 | — |
| 21 | [SiennaLend](https://defillama.com/protocol/siennalend) | Secret | ×2.10 | `COSMOS_SDK_GO` | $113,461 | — |
| 22 | [stkd-SCRT](https://defillama.com/protocol/stkd-scrt) | Secret | ×2.10 | `COSMOS_SDK_GO` | $91,670 | — |
| 23 | [Osmosis DEX](https://defillama.com/protocol/osmosis-dex) | Osmosis | ×1.40 | `COSMOS_SDK_GO` | $13,244,904 | yes |
| 24 | [MilkyWay Liquid Staking](https://defillama.com/protocol/milkyway-liquid-staking) | Milkyway | ×1.40 | `COSMOS_SDK_GO` | $2,456,649 | — |
| 25 | [Nolus Protocol](https://defillama.com/protocol/nolus-protocol) | Osmosis | ×1.40 | `COSMOS_SDK_GO` | $299,018 | yes |
| 26 | [Margined Protocol](https://defillama.com/protocol/margined-protocol) | Osmosis | ×1.40 | `COSMOS_SDK_GO` | $265,205 | yes |
| 27 | [BackBone Labs](https://defillama.com/protocol/backbone-labs) | Terra2 | ×1.40 | `COSMOS_SDK_GO` | $187,944 | yes |
| 28 | [Granite](https://defillama.com/protocol/granite) | Stacks | ×1.12 | `OTHER_VM` | $8,270,726 | — |
| 29 | [Hermetica hBTC](https://defillama.com/protocol/hermetica-hbtc) | Stacks | ×1.12 | `OTHER_VM` | $3,626,165 | — |
| 30 | [Bitflow](https://defillama.com/protocol/bitflow) | Stacks | ×1.12 | `OTHER_VM` | $2,600,728 | yes |
| 31 | [Hermetica USDh](https://defillama.com/protocol/hermetica-usdh) | Stacks | ×1.12 | `OTHER_VM` | $1,999,515 | — |
| 32 | [Zest V1](https://defillama.com/protocol/zest-v1) | Stacks | ×1.12 | `OTHER_VM` | $1,610,451 | — |
| 33 | [CityCoins](https://defillama.com/protocol/citycoins) | Stacks | ×1.12 | `OTHER_VM` | $905,006 | yes |
| 34 | [ALEX](https://defillama.com/protocol/alex) | Stacks | ×1.12 | `OTHER_VM` | $700,136 | yes |
| 35 | [Arkadiko](https://defillama.com/protocol/arkadiko) | Stacks | ×1.12 | `OTHER_VM` | $459,209 | yes |
| 36 | [LISA](https://defillama.com/protocol/lisa) | Stacks | ×1.12 | `OTHER_VM` | $311,543 | — |
| 37 | [Velar AMM](https://defillama.com/protocol/velar-amm) | Stacks | ×1.12 | `OTHER_VM` | $276,423 | — |
| 38 | [StackingDAO](https://defillama.com/protocol/stackingdao) | Stacks | ×1.12 | `OTHER_VM` | $157,877 | yes |
| 39 | [StackSwap](https://defillama.com/protocol/stackswap) | Stacks | ×1.12 | `OTHER_VM` | $70,466 | yes |
| 40 | [SaucerSwap V1](https://defillama.com/protocol/saucerswap-v1) | Hedera | ×1.10 | `OTHER_VM` | $9,163,287 | — |

## What would move this forward

One capability, not more analysis: the ability to enumerate a public repository's file tree. With it, the 121 in-band non-EVM protocols that publish source could be swept with the same indicator set that was validated against Maya and THORChain here — the indicators already exist in `tools/repo_indicators.py`, and `tools/repo_sweep.py` is written and tested against ground truth. It is a network-scope limit, not a missing method.

