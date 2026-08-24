# Candidates — Ranking C — mechanism match only

> **Discovery stage.** This file asserts no defect in any protocol named below. Each entry is a *review candidate*: named evidence matches a family's prerequisites, named evidence is unknown, and a named guard would falsify it. Verify on a local or pinned fork before concluding anything.

**How these are scored** is set out once, at the top of [`candidates_by_priority.md`](candidates_by_priority.md): the out-of-sample validation, why likelihood and actionability are kept apart, and why custody exposure is reported separately.

### The ranking

Full write-ups below for the 15 entries that `candidates_by_priority.md` does not already cover; the other 45 are listed here and written up in full there, under the same `protocol — family` heading.

| # | Protocol | Family | MATCH_SCORE | At risk | Write-up |
|---:|---|---|---:|---:|---|
| 1 | [Arcade.xyz](https://defillama.com/protocol/arcade.xyz) | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | 85.0 | $210,561 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 2 | [Kokonut Swap](https://defillama.com/protocol/kokonut-swap) | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | 85.0 | $610,365 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 3 | [TermFinance Vaults](https://defillama.com/protocol/termfinance-vaults) | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | 85.0 | $12,450,703 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 4 | [Fuji V1](https://defillama.com/protocol/fuji-v1) | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | 75.0 | $197,607 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 5 | [Cook Finance](https://defillama.com/protocol/cook-finance) | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | 75.0 | $51,767 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 6 | [ValueDefi](https://defillama.com/protocol/valuedefi) | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | 75.0 | $467,702 | below |
| 7 | [Ideamarket](https://defillama.com/protocol/ideamarket) | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | 75.0 | $163,257 | below |
| 8 | [Sumer.money](https://defillama.com/protocol/sumer.money) | `ACC-DONATION-UNACCOUNTED-BALANCE` | 75.0 | $1,222,366 | below |
| 9 | [Sperax USD](https://defillama.com/protocol/sperax-usd) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 73.8 | $520,189 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 10 | [Radiant V2](https://defillama.com/protocol/radiant-v2) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 73.8 | $693,778 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 11 | [Revest Finance](https://defillama.com/protocol/revest-finance) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $107,916 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 12 | [Cytonic Airdrop Campaign](https://defillama.com/protocol/cytonic-airdrop-campaign) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $169,482 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 13 | [SMARDEX AMM](https://defillama.com/protocol/smardex-amm) | `ACC-QUOTE-STALE-ACROSS-OWN-SWAP` | 73.8 | $153,633 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 14 | [RadioShack](https://defillama.com/protocol/radioshack) | `ACC-QUOTE-STALE-ACROSS-OWN-SWAP` | 73.8 | $453,693 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 15 | [Bridge Mutual](https://defillama.com/protocol/bridge-mutual) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $56,267 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 16 | [Tetu Earn](https://defillama.com/protocol/tetu-earn) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $482,134 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 17 | [VaultCraft](https://defillama.com/protocol/vaultcraft) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 73.8 | $557,157 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 18 | [KyberSwap Elastic](https://defillama.com/protocol/kyberswap-elastic) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $127,719 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 19 | [Zunami Protocol](https://defillama.com/protocol/zunami-protocol) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $548,289 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 20 | [Tarot](https://defillama.com/protocol/tarot) | `ORACLE-SPOT-THIN-LIQUIDITY` | 73.8 | $583,969 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 21 | [EZMoney](https://defillama.com/protocol/ezmoney) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 73.8 | $64,000 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 22 | [Pell Network](https://defillama.com/protocol/pell-network) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 73.8 | $224,044 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 23 | [xWin Finance](https://defillama.com/protocol/xwin-finance) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $205,238 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 24 | [Aavegotchi](https://defillama.com/protocol/aavegotchi) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $207,363 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 25 | [Loop](https://defillama.com/protocol/loop) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $76,962 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 26 | [Bunni V2](https://defillama.com/protocol/bunni-v2) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $213,436 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 27 | [BiFi](https://defillama.com/protocol/bifi) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $4,905,718 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 28 | [Impermax V2](https://defillama.com/protocol/impermax-v2) | `ORACLE-SPOT-THIN-LIQUIDITY` | 73.8 | $596,796 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 29 | [MoneyFi](https://defillama.com/protocol/moneyfi) | `ACC-QUOTE-STALE-ACROSS-OWN-SWAP` | 73.8 | $117,775 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 30 | [Bunny](https://defillama.com/protocol/bunny) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $3,597,277 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 31 | [GrizzlyFi Hives](https://defillama.com/protocol/grizzlyfi-hives) | `ACC-QUOTE-STALE-ACROSS-OWN-SWAP` | 73.8 | $522,590 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 32 | [Wombex Finance](https://defillama.com/protocol/wombex-finance) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $479,094 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 33 | [Varen](https://defillama.com/protocol/varen) | `ACC-QUOTE-STALE-ACROSS-OWN-SWAP` | 73.8 | $135,783 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 34 | [Accumulated Finance Liquid Staking](https://defillama.com/protocol/accumulated-finance-liquid-staking) | `SIG-VERIFIER-DEFEATABLE` | 73.8 | $622,677 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 35 | [Stabull Finance](https://defillama.com/protocol/stabull-finance) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 73.8 | $58,208 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 36 | [YieldWolf](https://defillama.com/protocol/yieldwolf) | `ACC-QUOTE-STALE-ACROSS-OWN-SWAP` | 73.8 | $62,846 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 37 | [Cakepie](https://defillama.com/protocol/cakepie) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $237,912 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 38 | [Shift Protocol](https://defillama.com/protocol/shift-protocol) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 73.8 | $834,205 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 39 | [Goldsand by InshAllah](https://defillama.com/protocol/goldsand-by-inshallah) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 73.8 | $337,796 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 40 | [PoolTogether V4](https://defillama.com/protocol/pooltogether-v4) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $738,116 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 41 | [StoneDefi](https://defillama.com/protocol/stonedefi) | `ACC-QUOTE-STALE-ACROSS-OWN-SWAP` | 73.8 | $75,186 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 42 | [Elk](https://defillama.com/protocol/elk) | `ACC-QUOTE-STALE-ACROSS-OWN-SWAP` | 73.8 | $160,743 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 43 | [Ante Finance](https://defillama.com/protocol/ante-finance) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $492,714 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 44 | [Rubicon](https://defillama.com/protocol/rubicon) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 73.8 | $247,341 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 45 | [Conic Finance](https://defillama.com/protocol/conic-finance) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 73.8 | $63,068 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 46 | [yAxis](https://defillama.com/protocol/yaxis) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $524,050 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 47 | [PrismaLST](https://defillama.com/protocol/prismalst) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $331,656 | below |
| 48 | [Fungify](https://defillama.com/protocol/fungify) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $131,456 | below |
| 49 | [SectorOne DLMM](https://defillama.com/protocol/sectorone-dlmm) | `ACC-QUOTE-STALE-ACROSS-OWN-SWAP` | 73.8 | $253,917 | below |
| 50 | [Wasabix](https://defillama.com/protocol/wasabix) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $210,765 | below |
| 51 | [Hunny Finance](https://defillama.com/protocol/hunny-finance) | `ACC-QUOTE-STALE-ACROSS-OWN-SWAP` | 73.8 | $528,141 | below |
| 52 | [Sturdy V2](https://defillama.com/protocol/sturdy-v2) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 73.8 | $266,989 | below |
| 53 | [DDEX](https://defillama.com/protocol/ddex) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $318,885 | below |
| 54 | [Idle](https://defillama.com/protocol/idle) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 73.8 | $1,567,483 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 55 | [SOFA.org](https://defillama.com/protocol/sofa.org) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 73.8 | $1,046,794 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 56 | [basedbid](https://defillama.com/protocol/basedbid) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 73.8 | $59,576 | below |
| 57 | [Landshare](https://defillama.com/protocol/landshare) | `ACC-QUOTE-STALE-ACROSS-OWN-SWAP` | 73.8 | $621,293 | below |
| 58 | [Preon Finance](https://defillama.com/protocol/preon-finance) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $244,291 | below |
| 59 | [Magic Eden](https://defillama.com/protocol/magic-eden) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 73.8 | $139,096 | below |
| 60 | [TreeDefi](https://defillama.com/protocol/treedefi) | `ACC-QUOTE-STALE-ACROSS-OWN-SWAP` | 73.8 | $71,298 | below |

---

### 6. ValueDefi  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking C — mechanism match only):** 6
- **Protocol:** ValueDefi (`valuedefi`) · Dexs · Binance
- **DefiLlama:** https://defillama.com/protocol/valuedefi
- **PRIORITY 48.38**  =  LIKELIHOOD 48.38 × ACTIONABILITY 100.0%
    - likelihood = family evidence 37.5/50 (MATCH 75.0 × evidence weight 1.0) + learned attack surface 10.88/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $467,702 · **Band:** `IN_BAND`
- **REPEAT VICTIM — 3 recorded hacks.** 
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 75.0 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** After deployment, no caller may (re)establish ownership, admin, or implementation wiring. Initialization state must be provably consumed.
    - Deployed source (`ValueLiquidFactory` @ 0x1b8e12f8…(bsc), `StableSwapFactory` @ 0xae63a206…(bsc)): prerequisites matched: initialize_without_modifier; no guard found
    - deployed source read for ValueLiquidFactory@0x1b8e12f8…(bsc), StableSwapFactory@0xae63a206…(bsc); indicators matched: initialize_without_modifier
    - 1/1 live proxies read a zero ERC-7201 Initializable slot (inconclusive alone: older OZ versions store the flag elsewhere)
- **Preconditions PRESENT / UNKNOWN:** src::initialize_without_modifier, upgradeable_architecture, initializer_flag_unset, live_value_or_approvals / none
- **Guards searched / found:** initializer_modifier_present, upgrade_timelocked / upgrade_timelocked
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **one externally-owned account** (`EOA_SINGLE_KEY`) — a code fix here does not remove that exposure, and it is the cheaper thing to raise first
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Simulated re-initialization reverts (kills the pair); Contract is non-upgradeable and holds no approvals
- **Where to start:** Read the initialization slot on every live proxy/facet and simulate re-initialization from an unprivileged address; it must revert.
- **Evidence:** `protocols/deep_screened.jsonl#valuedefi|UPGRADE-INITIALIZER-REACHABLE-LIVE`, `protocols/onchain_probes.json#valuedefi`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://valuedefi.io/audit

### 7. Ideamarket  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking C — mechanism match only):** 7
- **Protocol:** Ideamarket (`ideamarket`) · Derivatives · Arbitrum
- **DefiLlama:** https://defillama.com/protocol/ideamarket
- **PRIORITY 48.2**  =  LIKELIHOOD 48.2 × ACTIONABILITY 100.0%
    - likelihood = family evidence 37.5/50 (MATCH 75.0 × evidence weight 1.0) + learned attack surface 10.7/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $163,257 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 75.0 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** After deployment, no caller may (re)establish ownership, admin, or implementation wiring. Initialization state must be provably consumed.
    - Deployed source (`InterestManagerStateTransferAVM` @ 0xa1c56f8c…(arbitrum)): prerequisites matched: initialize_without_modifier; no guard found
    - deployed source read for InterestManagerStateTransferAVM@0xa1c56f8c…(arbitrum); indicators matched: initialize_without_modifier
    - 1/1 live proxies read a zero ERC-7201 Initializable slot (inconclusive alone: older OZ versions store the flag elsewhere)
- **Preconditions PRESENT / UNKNOWN:** src::initialize_without_modifier, upgradeable_architecture, initializer_flag_unset, live_value_or_approvals / none
- **Guards searched / found:** initializer_modifier_present, upgrade_timelocked / upgrade_timelocked
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Simulated re-initialization reverts (kills the pair); Contract is non-upgradeable and holds no approvals
- **Where to start:** Read the initialization slot on every live proxy/facet and simulate re-initialization from an unprivileged address; it must revert.
- **Evidence:** `protocols/deep_screened.jsonl#ideamarket|UPGRADE-INITIALIZER-REACHABLE-LIVE`, `protocols/onchain_probes.json#ideamarket`
- **Disclosure:** https://ideamarket.io · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.ideamarket.io/contracts/audit

### 8. Sumer.money  —  `ACC-DONATION-UNACCOUNTED-BALANCE`

- **Rank (Ranking C — mechanism match only):** 8
- **Protocol:** Sumer.money (`sumer.money`) · Lending · Berachain, CORE, Meter, Arbitrum, Goat, Base …
- **DefiLlama:** https://defillama.com/protocol/sumer.money
- **PRIORITY 45.35**  =  LIKELIHOOD 53.35 × ACTIONABILITY 85.0%
    - likelihood = family evidence 37.5/50 (MATCH 75.0 × evidence weight 1.0) + learned attack surface 15.85/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,222,366 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 75.0 · CONFIDENCE 76.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A share price, exchange rate or totalAssets must be a function of value the protocol accounted for on entry. Reading a raw balance makes any direct transfer into the accounting boundary an unpriced increase in every holder's claim.
    - Deployed source (`TransparentUpgradeableProxy` @ 0x0385F851…(arbitrum), `AErc20Delegator` @ 0x03ef96f5…(arbitrum)): no prerequisite matched; no guard found
    - RELEVANCE GATE: the contract(s) actually read (TransparentUpgradeableProxy, AErc20Delegator) show no distinguishing indicator for this family, so they are probably not the contracts that implement it. Every source-derived signal is therefore UNKNOWN, including the absence of a guard: not finding a staleness check in a data-provider contract says nothing about the oracle.
    - market implementation(s) resolved: CErc20
    - 4 live market(s) read on-chain
- **Preconditions PRESENT / UNKNOWN:** rate_reads_raw_balance, unprivileged_inbound_transfer_possible, inflated_rate_consumed_by_value_decision, third_party_claims_exposed / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `KNOWN_ISSUE_DEPLOYMENT_STATUS_UNKNOWN` — The Compound-fork donation vector is publicly documented and was raised in Venus's own Code4rena audit before the March 2026 exploit.
- **Falsified by:** totalAssets derived from an internal counter, not balanceOf (kills the pair); Rate is monotonic and rate-limited per block; Inbound transfers to the accounting boundary are rejected or swept to a reserve
- **Where to start:** On a fork, transfer an arbitrary amount of each counted asset directly into every accounting boundary; the share price, exchange rate and derived borrow power must not change.
- **Evidence:** `protocols/deep_screened.jsonl#sumer.money|ACC-DONATION-UNACCOUNTED-BALANCE`, `protocols/onchain_probes.json#sumer.money`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.sumer.money/security/audits

### 47. PrismaLST  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking C — mechanism match only):** 47
- **Protocol:** PrismaLST (`prismalst`) · CDP · Ethereum
- **DefiLlama:** https://defillama.com/protocol/prismalst
- **PRIORITY 52.02**  =  LIKELIHOOD 52.02 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 15.12/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $331,656 · **Band:** `IN_BAND`
- **Previously hacked:** 2024-03-28 for $11,600,000 [Missing Input Validation]
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`Factory` @ 0x70b66e20…(ethereum), `PrismaToken` @ 0xda47862a…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for Factory@0x70b66e20…(ethereum), PrismaToken@0xda47862a…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `KNOWN_ISSUE_DEPLOYMENT_STATUS_UNKNOWN` — DefiLlama's hacks dataset records 1 prior on-chain incident(s) on this protocol, most recently 2024-03-28 for $11,600,000 [Missing Input Validation]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#prismalst|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#prismalst`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/prisma-fi/audits/blob/main/audit-nomoi.pdf, https://github.com/prisma-fi/audits/blob/main/audit-zellic.pdf

### 48. Fungify  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking C — mechanism match only):** 48
- **Protocol:** Fungify (`fungify`) · Lending · Ethereum
- **DefiLlama:** https://defillama.com/protocol/fungify
- **PRIORITY 51.92**  =  LIKELIHOOD 51.92 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 15.02/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $131,456 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`Unitroller` @ 0xf9c70750…(ethereum), `FungTokenProxy` @ 0x0e4e7f2a…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for Unitroller@0xf9c70750…(ethereum), FungTokenProxy@0x0e4e7f2a…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#fungify|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#fungify`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.fungify.it/governance/security

### 49. SectorOne DLMM  —  `ACC-QUOTE-STALE-ACROSS-OWN-SWAP`

- **Rank (Ranking C — mechanism match only):** 49
- **Protocol:** SectorOne DLMM (`sectorone-dlmm`) · Dexs · Robinhood Chain, Base, MegaETH, Ethereum
- **DefiLlama:** https://defillama.com/protocol/sectorone-dlmm
- **PRIORITY 51.82**  =  LIKELIHOOD 51.82 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 14.92/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $253,917 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
- **Broken invariant tested:** A value used for minting, crediting or reward must be derived from what the protocol actually received, not from a quote taken before the protocol itself moved the market. Where the protocol's own action changes the price it just read, the value must be recomputed after the fact.
    - Deployed source (`LBFactory` @ 0x20918F4B…(base), `TransparentUpgradeableProxy` @ 0x304BaEB3…(base)): prerequisites matched: quote_then_own_swap; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): referral_reward_with_mint=no
    - deployed source read for LBFactory@0x20918F4B…(base), TransparentUpgradeableProxy@0x304BaEB3…(base); indicators matched: quote_then_own_swap
- **Preconditions PRESENT / UNKNOWN:** src::quote_then_own_swap, live_value_present, deployment_reachable_on_chain / src::quote_then_addliquidity
- **Guards searched / found:** lp_delta_measured, twap_or_feed_for_accounting / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `EOA_SINGLE_KEY`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** The minted amount is derived from the LP balance delta or from a TWAP (kills the pair); The protocol's swap is bounded so it cannot move reserves materially; Rewards settle in a later block against re-measured backing
- **Where to start:** On a fork, run the bonding path with a flash-funded swap sized to skew the pair, then assert that the minted or credited amount tracks the LP tokens actually received rather than the pre-swap quote.
- **Evidence:** `protocols/deep_screened.jsonl#sectorone-dlmm|ACC-QUOTE-STALE-ACROSS-OWN-SWAP`, `protocols/onchain_probes.json#sectorone-dlmm`
- **Disclosure:** https://sectorone.xyz · no audit link listed

### 50. Wasabix  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking C — mechanism match only):** 50
- **Protocol:** Wasabix (`wasabix`) · Yield · Ethereum, Polygon, Binance
- **DefiLlama:** https://defillama.com/protocol/wasabix
- **PRIORITY 51.78**  =  LIKELIHOOD 51.78 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 14.88/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $210,765 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`BunnyVaultAdapter` @ 0x3d244d67…(bsc), `StakingPoolsV2` @ 0x4A808641…(bsc)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for BunnyVaultAdapter@0x3d244d67…(bsc), StakingPoolsV2@0x4A808641…(bsc); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#wasabix|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#wasabix`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://wasabix-finance.gitbook.io/wasabix_finance/code/certik-audit-report

### 51. Hunny Finance  —  `ACC-QUOTE-STALE-ACROSS-OWN-SWAP`

- **Rank (Ranking C — mechanism match only):** 51
- **Protocol:** Hunny Finance (`hunny-finance`) · Yield · Binance
- **DefiLlama:** https://defillama.com/protocol/hunny-finance
- **PRIORITY 51.75**  =  LIKELIHOOD 51.75 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 14.85/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $528,141 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A value used for minting, crediting or reward must be derived from what the protocol actually received, not from a quote taken before the protocol itself moved the market. Where the protocol's own action changes the price it just read, the value must be recomputed after the fact.
    - Deployed source (`CakeFlipVault` @ 0x12180BB3…(bsc), `VaultHunny` @ 0x09fd83e5…(bsc)): prerequisites matched: quote_then_own_swap; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): referral_reward_with_mint=no
    - deployed source read for CakeFlipVault@0x12180BB3…(bsc), VaultHunny@0x09fd83e5…(bsc); indicators matched: quote_then_own_swap
- **Preconditions PRESENT / UNKNOWN:** src::quote_then_own_swap, live_value_present, deployment_reachable_on_chain / src::quote_then_addliquidity
- **Guards searched / found:** lp_delta_measured, twap_or_feed_for_accounting / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** The minted amount is derived from the LP balance delta or from a TWAP (kills the pair); The protocol's swap is bounded so it cannot move reserves materially; Rewards settle in a later block against re-measured backing
- **Where to start:** On a fork, run the bonding path with a flash-funded swap sized to skew the pair, then assert that the minted or credited amount tracks the LP tokens actually received rather than the pre-swap quote.
- **Evidence:** `protocols/deep_screened.jsonl#hunny-finance|ACC-QUOTE-STALE-ACROSS-OWN-SWAP`, `protocols/onchain_probes.json#hunny-finance`
- **Disclosure:** https://hunny.finance · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://www.certik.org/projects/pancakehunny

### 52. Sturdy V2  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking C — mechanism match only):** 52
- **Protocol:** Sturdy V2 (`sturdy-v2`) · Lending · Mode, Ethereum, Linea, Optimism, Flow, Sei
- **DefiLlama:** https://defillama.com/protocol/sturdy-v2
- **PRIORITY 51.68**  =  LIKELIHOOD 51.68 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 14.78/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $266,989 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
- **Broken invariant tested:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source (`HypERC4626OwnerCollateral` @ 0x49b50F50…(ethereum), `AggregatorDataProvider` @ 0x69764E3e…(ethereum)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for HypERC4626OwnerCollateral@0x49b50F50…(ethereum), AggregatorDataProvider@0x69764E3e…(ethereum); indicators matched: unsafe_cross_sign_cast
- **Preconditions PRESENT / UNKNOWN:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** safecast_used / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#sturdy-v2|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#sturdy-v2`
- **Disclosure:** https://v2.sturdy.finance/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/Zellic/publications/blob/master/Sturdy%20-%20Zellic%20Audit%20Report.pdf, https://chainsecurity.com/security-audit/sturdy-aggregator-smart-contracts/

### 53. DDEX  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking C — mechanism match only):** 53
- **Protocol:** DDEX (`ddex`) · Dexs · Ethereum
- **DefiLlama:** https://defillama.com/protocol/ddex
- **PRIORITY 51.63**  =  LIKELIHOOD 51.63 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 14.73/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $318,885 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`Hydro` @ 0x241e82c7…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for Hydro@0x241e82c7…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#ddex|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#ddex`
- **Disclosure:** https://ddex.io/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/HydroProtocol/audit-reports/blob/master/2.0/hydro_audit_report_2019_14_en_1_0.pdf

### 56. basedbid  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking C — mechanism match only):** 56
- **Protocol:** basedbid (`basedbid`) · Launchpad · Robinhood Chain, Solana, Base, Binance, Ethereum, MegaETH
- **DefiLlama:** https://defillama.com/protocol/basedbid
- **PRIORITY 51.42**  =  LIKELIHOOD 51.42 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 14.52/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $59,576 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
- **Broken invariant tested:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source (`NonfungiblePositionManager` @ 0x03a520b3…(base), `NonfungiblePositionManager` @ 0x46A15B0b…(base)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for NonfungiblePositionManager@0x03a520b3…(base), NonfungiblePositionManager@0x46A15B0b…(base); indicators matched: unsafe_cross_sign_cast
- **Preconditions PRESENT / UNKNOWN:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** safecast_used / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#basedbid|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#basedbid`
- **Disclosure:**   · no audit link listed

### 57. Landshare  —  `ACC-QUOTE-STALE-ACROSS-OWN-SWAP`

- **Rank (Ranking C — mechanism match only):** 57
- **Protocol:** Landshare (`landshare`) · RWA · Binance
- **DefiLlama:** https://defillama.com/protocol/landshare
- **PRIORITY 51.38**  =  LIKELIHOOD 51.38 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 14.48/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $621,293 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A value used for minting, crediting or reward must be derived from what the protocol actually received, not from a quote taken before the protocol itself moved the market. Where the protocol's own action changes the price it just read, the value must be recomputed after the fact.
    - Deployed source (`PancakePair` @ 0x13f80c53…(bsc), `MasterChef` @ 0x3f945889…(bsc)): prerequisites matched: quote_then_own_swap; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): referral_reward_with_mint=no
    - deployed source read for PancakePair@0x13f80c53…(bsc), MasterChef@0x3f945889…(bsc); indicators matched: quote_then_own_swap
- **Preconditions PRESENT / UNKNOWN:** src::quote_then_own_swap, live_value_present, deployment_reachable_on_chain / src::quote_then_addliquidity
- **Guards searched / found:** lp_delta_measured, twap_or_feed_for_accounting / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** The minted amount is derived from the LP balance delta or from a TWAP (kills the pair); The protocol's swap is bounded so it cannot move reserves materially; Rewards settle in a later block against re-measured backing
- **Where to start:** On a fork, run the bonding path with a flash-funded swap sized to skew the pair, then assert that the minted or credited amount tracks the LP tokens actually received rather than the pre-swap quote.
- **Evidence:** `protocols/deep_screened.jsonl#landshare|ACC-QUOTE-STALE-ACROSS-OWN-SWAP`, `protocols/onchain_probes.json#landshare`
- **Disclosure:** https://landshare.io · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://landshare.io/wp-content/uploads/2022/06/Audit.pdf

### 58. Preon Finance  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking C — mechanism match only):** 58
- **Protocol:** Preon Finance (`preon-finance`) · CDP · Arbitrum, Polygon, Base
- **DefiLlama:** https://defillama.com/protocol/preon-finance
- **PRIORITY 51.27**  =  LIKELIHOOD 51.27 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 14.37/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $244,291 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`StrategySplitter` @ 0x55dce0e1…(arbitrum), `ATokenInstance` @ 0xadcb7e98…(arbitrum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for StrategySplitter@0x55dce0e1…(arbitrum), ATokenInstance@0xadcb7e98…(arbitrum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a Safe requiring several signatures** (`SAFE_M_OF_N`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#preon-finance|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#preon-finance`
- **Disclosure:** https://app.preon.finance/borrow · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.preon.finance/information/security#audits

### 59. Magic Eden  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking C — mechanism match only):** 59
- **Protocol:** Magic Eden (`magic-eden`) · NFT Marketplace · Bitcoin, Solana, Arbitrum, Base, Ethereum
- **DefiLlama:** https://defillama.com/protocol/magic-eden
- **PRIORITY 51.18**  =  LIKELIHOOD 51.18 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 14.28/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $139,096 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
- **Broken invariant tested:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source (`TrustedForwarder` @ 0x5ebc127f…(base)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for TrustedForwarder@0x5ebc127f…(base); indicators matched: unsafe_cross_sign_cast
- **Preconditions PRESENT / UNKNOWN:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** safecast_used / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#magic-eden|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#magic-eden`
- **Disclosure:** https://magiceden.io · no audit link listed

### 60. TreeDefi  —  `ACC-QUOTE-STALE-ACROSS-OWN-SWAP`

- **Rank (Ranking C — mechanism match only):** 60
- **Protocol:** TreeDefi (`treedefi`) · Yield · Binance
- **DefiLlama:** https://defillama.com/protocol/treedefi
- **PRIORITY 51.08**  =  LIKELIHOOD 51.08 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 14.18/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $71,298 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A value used for minting, crediting or reward must be derived from what the protocol actually received, not from a quote taken before the protocol itself moved the market. Where the protocol's own action changes the price it just read, the value must be recomputed after the fact.
    - Deployed source (`MeatToken` @ 0x00438AE9…(bsc), `MasterChef` @ 0x0283527f…(bsc)): prerequisites matched: quote_then_own_swap; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): referral_reward_with_mint=no
    - deployed source read for MeatToken@0x00438AE9…(bsc), MasterChef@0x0283527f…(bsc); indicators matched: quote_then_own_swap
- **Preconditions PRESENT / UNKNOWN:** src::quote_then_own_swap, live_value_present, deployment_reachable_on_chain / src::quote_then_addliquidity
- **Guards searched / found:** lp_delta_measured, twap_or_feed_for_accounting / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `EOA_SINGLE_KEY`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** The minted amount is derived from the LP balance delta or from a TWAP (kills the pair); The protocol's swap is bounded so it cannot move reserves materially; Rewards settle in a later block against re-measured backing
- **Where to start:** On a fork, run the bonding path with a flash-funded swap sized to skew the pair, then assert that the minted or credited amount tracks the LP tokens actually received rather than the pre-swap quote.
- **Evidence:** `protocols/deep_screened.jsonl#treedefi|ACC-QUOTE-STALE-ACROSS-OWN-SWAP`, `protocols/onchain_probes.json#treedefi`
- **Disclosure:** https://treedefi.com · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://www.certik.org/projects/treedefi
