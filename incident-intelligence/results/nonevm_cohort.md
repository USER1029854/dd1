# The non-EVM cohort

> **Discovery stage.** Nothing here asserts a defect in any protocol named below. The one confirmed incident in this file, Maya Protocol, is a *past* event already in this run's corpus, and the source lines quoted for it are the published record of a disclosed exploit, not an attack procedure.

## Why this file exists

Every probe in the main screen is `eth_call`, `eth_getStorageAt`, `eth_getCode` and explorer `getsourcecode`. That is an EVM instrument, and it means **717 protocols above the $50,000 floor, 621 of them inside the $50k-$30M band, were invisible to it** — not judged safe, simply never looked at. Solana alone accounts for 169.

The last incident inside this run's window, four days before it closed, was on one of them.

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

| # | Protocol | Chain | Runtime | Value at risk | Public repo |
|---:|---|---|---|---:|---|
| 1 | [Decibel](https://defillama.com/protocol/decibel) | Aptos | `MOVE` | $29,817,175 | — |
| 2 | [Vaulta REX](https://defillama.com/protocol/vaulta-rex) | EOS | `OTHER_VM` | $29,505,988 | — |
| 3 | [Hydration Lending](https://defillama.com/protocol/hydration-lending) | HydraDX | `SUBSTRATE_RUST` | $29,416,512 | — |
| 4 | [Rhea Dex](https://defillama.com/protocol/rhea-dex) | Near | `OTHER_VM` | $28,466,339 | — |
| 5 | [Hydration DEX](https://defillama.com/protocol/hydration-dex) | HydraDX | `SUBSTRATE_RUST` | $27,425,114 | yes |
| 6 | [Pacifica Perps](https://defillama.com/protocol/pacifica-perps) | Solana | `SOLANA_RUST` | $26,681,528 | — |
| 7 | [STON.fi](https://defillama.com/protocol/ston.fi) | TON | `OTHER_VM` | $26,379,222 | — |
| 8 | [Stakee](https://defillama.com/protocol/stakee) | TON | `OTHER_VM` | $26,112,521 | — |
| 9 | [xALGO Liquid Staking](https://defillama.com/protocol/xalgo-liquid-staking) | Algorand | `OTHER_VM` | $25,798,016 | — |
| 10 | [wTAO](https://defillama.com/protocol/wtao) | Bittensor | `UNKNOWN_RUNTIME` | $25,426,400 | — |
| 11 | [Adrastea Validator](https://defillama.com/protocol/adrastea-validator) | Solana | `SOLANA_RUST` | $24,913,258 | — |
| 12 | [Cetus CLMM](https://defillama.com/protocol/cetus-clmm) | Sui | `MOVE` | $24,733,471 | — |
| 13 | [Hylo Protocol](https://defillama.com/protocol/hylo-protocol) | Solana | `SOLANA_RUST` | $24,463,053 | — |
| 14 | [Meteora DAMM V2](https://defillama.com/protocol/meteora-damm-v2) | Solana | `SOLANA_RUST` | $23,436,419 | — |
| 15 | [ObeliskBTC](https://defillama.com/protocol/obeliskbtc) | Bitcoin | `OTHER_VM` | $23,142,064 | — |
| 16 | [XION Finance](https://defillama.com/protocol/xion-finance) | XION | `UNKNOWN_RUNTIME` | $22,905,270 | — |
| 17 | [Folks Finance Lending](https://defillama.com/protocol/folks-finance-lending) | Algorand | `OTHER_VM` | $22,752,418 | — |
| 18 | [BULK](https://defillama.com/protocol/bulk) | Solana | `SOLANA_RUST` | $21,575,707 | — |
| 19 | [Vesta Equity](https://defillama.com/protocol/vesta-equity) | Algorand | `OTHER_VM` | $20,634,337 | — |
| 20 | [DeFindex](https://defillama.com/protocol/defindex) | Stellar | `OTHER_VM` | $19,520,573 | yes |
| 21 | [Volo LST](https://defillama.com/protocol/volo-lst) | Sui | `MOVE` | $19,367,619 | — |
| 22 | [Bluefin Spot](https://defillama.com/protocol/bluefin-spot) | Sui | `MOVE` | $19,013,777 | — |
| 23 | [Hylo LSTs](https://defillama.com/protocol/hylo-lsts) | Solana | `SOLANA_RUST` | $18,800,105 | — |
| 24 | [RHEA LST](https://defillama.com/protocol/rhea-lst) | Near | `OTHER_VM` | $18,027,614 | — |
| 25 | [CatFee Staking Vault](https://defillama.com/protocol/catfee-staking-vault) | Tron | `OTHER_VM` | $17,863,267 | — |
| 26 | [Manifest Trade](https://defillama.com/protocol/manifest-trade) | Solana | `SOLANA_RUST` | $17,774,671 | — |
| 27 | [AlphaFi Agg](https://defillama.com/protocol/alphafi-agg) | Sui | `MOVE` | $17,747,390 | — |
| 28 | [Realms](https://defillama.com/protocol/realms) | Solana | `SOLANA_RUST` | $17,610,438 | — |
| 29 | [Jito Restaking](https://defillama.com/protocol/jito-restaking) | Solana | `SOLANA_RUST` | $17,504,346 | — |
| 30 | [STRATO](https://defillama.com/protocol/strato) | Strato | `UNKNOWN_RUNTIME` | $17,418,780 | — |
| 31 | [Sceptre Liquid](https://defillama.com/protocol/sceptre-liquid) | Flare | `OTHER_VM` | $16,970,333 | — |
| 32 | [Bitget SOL](https://defillama.com/protocol/bitget-sol) | Solana | `SOLANA_RUST` | $16,569,126 | — |
| 33 | [Youves](https://defillama.com/protocol/youves) | Tezos | `OTHER_VM` | $16,467,964 | yes |
| 34 | [RISEx](https://defillama.com/protocol/risex) | RISE | `UNKNOWN_RUNTIME` | $16,163,762 | — |
| 35 | [Serum](https://defillama.com/protocol/serum) | Solana | `SOLANA_RUST` | $16,054,662 | yes |
| 36 | [Stellar DEX](https://defillama.com/protocol/stellar-dex) | Stellar | `OTHER_VM` | $15,827,041 | — |
| 37 | [SparkDEX V4](https://defillama.com/protocol/sparkdex-v4) | Flare | `OTHER_VM` | $15,566,559 | — |
| 38 | [Minswap DEX](https://defillama.com/protocol/minswap-dex) | Cardano | `OTHER_VM` | $15,256,659 | — |
| 39 | [Hubra Staked SOL](https://defillama.com/protocol/hubra-staked-sol) | Solana | `SOLANA_RUST` | $15,098,544 | — |
| 40 | [Qearn](https://defillama.com/protocol/qearn) | Qubic | `UNKNOWN_RUNTIME` | $14,801,351 | — |

## What would move this forward

One capability, not more analysis: the ability to enumerate a public repository's file tree. With it, the 121 in-band non-EVM protocols that publish source could be swept with the same indicator set that was validated against Maya and THORChain here — the indicators already exist in `tools/repo_indicators.py`, and `tools/repo_sweep.py` is written and tested against ground truth. It is a network-scope limit, not a missing method.

