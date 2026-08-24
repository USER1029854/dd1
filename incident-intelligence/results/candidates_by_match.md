# Candidates — Ranking C — mechanism match only

> **Discovery stage.** This file asserts no defect in any protocol named below. Each entry is a *review candidate*: named evidence matches a family's prerequisites, named evidence is unknown, and a named guard would falsify it. Verify on a local or pinned fork before concluding anything.

**How these are scored** is set out once, at the top of [`candidates_by_priority.md`](candidates_by_priority.md): the out-of-sample validation, why likelihood and actionability are kept apart, and why custody exposure is reported separately.

### The ranking

Full write-ups below for the 19 entries that `candidates_by_priority.md` does not already cover; the other 41 are listed here and written up in full there, under the same `protocol — family` heading.

| # | Protocol | Family | MATCH_SCORE | At risk | Write-up |
|---:|---|---|---:|---:|---|
| 1 | [Arcade.xyz](https://defillama.com/protocol/arcade.xyz) | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | 85.0 | $210,561 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 2 | [Kine Finance](https://defillama.com/protocol/kine-finance) | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | 85.0 | $1,120,759 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 3 | [Kokonut Swap](https://defillama.com/protocol/kokonut-swap) | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | 85.0 | $610,365 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 4 | [Capyfi](https://defillama.com/protocol/capyfi) | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | 85.0 | $6,641,113 | below |
| 5 | [TermFinance Vaults](https://defillama.com/protocol/termfinance-vaults) | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | 85.0 | $12,450,703 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 6 | [Sumer.money](https://defillama.com/protocol/sumer.money) | `ACC-DONATION-UNACCOUNTED-BALANCE` | 77.5 | $1,222,366 | below |
| 7 | [Cook Finance](https://defillama.com/protocol/cook-finance) | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | 75.0 | $51,767 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 8 | [ValueDefi](https://defillama.com/protocol/valuedefi) | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | 75.0 | $467,702 | below |
| 9 | [Ideamarket](https://defillama.com/protocol/ideamarket) | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | 75.0 | $163,257 | below |
| 10 | [Sperax USD](https://defillama.com/protocol/sperax-usd) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 73.8 | $520,189 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 11 | [Radiant V2](https://defillama.com/protocol/radiant-v2) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $693,778 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 12 | [Revest Finance](https://defillama.com/protocol/revest-finance) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $107,916 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 13 | [Cytonic Airdrop Campaign](https://defillama.com/protocol/cytonic-airdrop-campaign) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $169,482 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 14 | [Bridge Mutual](https://defillama.com/protocol/bridge-mutual) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $56,267 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 15 | [Tetu Earn](https://defillama.com/protocol/tetu-earn) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $482,134 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 16 | [VaultCraft](https://defillama.com/protocol/vaultcraft) | `SIG-VERIFIER-DEFEATABLE` | 73.8 | $557,157 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 17 | [Tarot](https://defillama.com/protocol/tarot) | `ORACLE-SPOT-THIN-LIQUIDITY` | 73.8 | $583,969 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 18 | [EZMoney](https://defillama.com/protocol/ezmoney) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 73.8 | $64,000 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 19 | [Pell Network](https://defillama.com/protocol/pell-network) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 73.8 | $224,044 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 20 | [xWin Finance](https://defillama.com/protocol/xwin-finance) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $205,238 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 21 | [Aavegotchi](https://defillama.com/protocol/aavegotchi) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $207,363 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 22 | [Bunni V2](https://defillama.com/protocol/bunni-v2) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $213,436 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 23 | [BiFi](https://defillama.com/protocol/bifi) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $4,905,718 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 24 | [Impermax V2](https://defillama.com/protocol/impermax-v2) | `ORACLE-SPOT-THIN-LIQUIDITY` | 73.8 | $596,796 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 25 | [Bunny](https://defillama.com/protocol/bunny) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $3,597,277 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 26 | [GrizzlyFi Hives](https://defillama.com/protocol/grizzlyfi-hives) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $522,590 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 27 | [Wombex Finance](https://defillama.com/protocol/wombex-finance) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $479,094 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 28 | [Accumulated Finance Liquid Staking](https://defillama.com/protocol/accumulated-finance-liquid-staking) | `SIG-VERIFIER-DEFEATABLE` | 73.8 | $622,677 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 29 | [Stabull Finance](https://defillama.com/protocol/stabull-finance) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 73.8 | $58,208 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 30 | [YieldWolf](https://defillama.com/protocol/yieldwolf) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $62,846 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 31 | [Cakepie](https://defillama.com/protocol/cakepie) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $237,912 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 32 | [Shift Protocol](https://defillama.com/protocol/shift-protocol) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $834,205 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 33 | [FinNexus](https://defillama.com/protocol/finnexus) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $232,179 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 34 | [Goldsand by InshAllah](https://defillama.com/protocol/goldsand-by-inshallah) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 73.8 | $337,796 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 35 | [PoolTogether V4](https://defillama.com/protocol/pooltogether-v4) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $738,116 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 36 | [StoneDefi](https://defillama.com/protocol/stonedefi) | `SIG-VERIFIER-DEFEATABLE` | 73.8 | $75,186 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 37 | [Ante Finance](https://defillama.com/protocol/ante-finance) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $492,714 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 38 | [Rubicon](https://defillama.com/protocol/rubicon) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 73.8 | $247,341 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 39 | [Conic Finance](https://defillama.com/protocol/conic-finance) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $63,068 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 40 | [yAxis](https://defillama.com/protocol/yaxis) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $524,050 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 41 | [PrismaLST](https://defillama.com/protocol/prismalst) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $331,656 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 42 | [Fungify](https://defillama.com/protocol/fungify) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $131,456 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 43 | [Wasabix](https://defillama.com/protocol/wasabix) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $210,765 | below |
| 44 | [Sturdy V2](https://defillama.com/protocol/sturdy-v2) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $266,989 | below |
| 45 | [DDEX](https://defillama.com/protocol/ddex) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $318,885 | below |
| 46 | [Idle](https://defillama.com/protocol/idle) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $1,567,483 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 47 | [SOFA.org](https://defillama.com/protocol/sofa.org) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $1,046,794 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 48 | [Preon Finance](https://defillama.com/protocol/preon-finance) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $244,291 | below |
| 49 | [Magic Eden](https://defillama.com/protocol/magic-eden) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 73.8 | $139,096 | below |
| 50 | [Contango V1](https://defillama.com/protocol/contango-v1) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 73.8 | $290,609 | below |
| 51 | [Velvet V3](https://defillama.com/protocol/velvet-v3) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $283,971 | below |
| 52 | [MochiFi](https://defillama.com/protocol/mochifi) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $414,425 | below |
| 53 | [Caviar V1](https://defillama.com/protocol/caviar-v1) | `SIG-VERIFIER-DEFEATABLE` | 73.8 | $61,437 | below |
| 54 | [Aloe](https://defillama.com/protocol/aloe) | `SIG-VERIFIER-DEFEATABLE` | 73.8 | $71,560 | below |
| 55 | [YieldFlow Yield Farming](https://defillama.com/protocol/yieldflow-yield-farming) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $260,113 | below |
| 56 | [Abracadabra Spell](https://defillama.com/protocol/abracadabra-spell) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $4,667,807 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 57 | [Theoriq AlphaVault ETH](https://defillama.com/protocol/theoriq-alphavault-eth) | `SIG-VERIFIER-DEFEATABLE` | 73.8 | $201,442 | below |
| 58 | [Ajna V1](https://defillama.com/protocol/ajna-v1) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $491,042 | below |
| 59 | [SIR](https://defillama.com/protocol/sir) | `SIG-VERIFIER-DEFEATABLE` | 73.8 | $106,823 | below |
| 60 | [pSTAKE LSD](https://defillama.com/protocol/pstake-lsd) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 73.8 | $192,828 | below |

---

### 4. Capyfi  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking C — mechanism match only):** 4
- **Protocol:** Capyfi (`capyfi`) · Lending · Ethereum, LaChain Network, World Chain
- **DefiLlama:** https://defillama.com/protocol/capyfi
- **PRIORITY 44.88**  =  LIKELIHOOD 52.8 × ACTIONABILITY 85.0%
    - likelihood = family evidence 42.5/50 (MATCH 85.0 × evidence weight 1.0) + learned attack surface 10.3/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $6,641,113 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 85.0 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
- **Broken invariant tested:** After deployment, no caller may (re)establish ownership, admin, or implementation wiring. Initialization state must be provably consumed.
    - Deployed source (`CErc20Immutable` @ 0x004c0908…(ethereum), `TransparentUpgradeableProxy` @ 0x02451015…(ethereum)): prerequisites matched: initialize_without_modifier; no guard found
    - deployed source read for CErc20Immutable@0x004c0908…(ethereum), TransparentUpgradeableProxy@0x02451015…(ethereum); indicators matched: initialize_without_modifier
    - 1/1 live proxies read a zero ERC-7201 Initializable slot (inconclusive alone: older OZ versions store the flag elsewhere)
- **Preconditions PRESENT / UNKNOWN:** src::initialize_without_modifier, upgradeable_architecture, initializer_flag_unset, live_value_or_approvals / none
- **Guards searched / found:** initializer_modifier_present, upgrade_timelocked / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Simulated re-initialization reverts (kills the pair); Contract is non-upgradeable and holds no approvals
- **Where to start:** Read the initialization slot on every live proxy/facet and simulate re-initialization from an unprivileged address; it must revert.
- **Evidence:** `protocols/deep_screened.jsonl#capyfi|UPGRADE-INITIALIZER-REACHABLE-LIVE`, `protocols/onchain_probes.json#capyfi`
- **Disclosure:** https://capyfi.com/ · no audit link listed

### 6. Sumer.money  —  `ACC-DONATION-UNACCOUNTED-BALANCE`

- **Rank (Ranking C — mechanism match only):** 6
- **Protocol:** Sumer.money (`sumer.money`) · Lending · Berachain, CORE, Meter, Arbitrum, Goat, Base …
- **DefiLlama:** https://defillama.com/protocol/sumer.money
- **PRIORITY 46.41**  =  LIKELIHOOD 54.6 × ACTIONABILITY 85.0%
    - likelihood = family evidence 38.75/50 (MATCH 77.5 × evidence weight 1.0) + learned attack surface 15.85/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,222,366 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 77.5 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A share price, exchange rate or totalAssets must be a function of value the protocol accounted for on entry. Reading a raw balance makes any direct transfer into the accounting boundary an unpriced increase in every holder's claim.
    - Deployed source (`CErc20Immutable` @ 0x004c0908…(ethereum), `TransparentUpgradeableProxy` @ 0x02451015…(ethereum)): prerequisites matched: getCashPrior_balanceOf; no guard found
    - deployed source read for CErc20Immutable@0x004c0908…(ethereum), TransparentUpgradeableProxy@0x02451015…(ethereum); indicators matched: getCashPrior_balanceOf
    - market implementation(s) resolved: CErc20
    - 4 live market(s) read on-chain
- **Preconditions PRESENT / UNKNOWN:** src::getCashPrior_balanceOf, rate_reads_raw_balance, unprivileged_inbound_transfer_possible, inflated_rate_consumed_by_value_decision, third_party_claims_exposed / src::totalAssets_reads_balanceOf
- **Guards searched / found:** internal_cash_counter / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `KNOWN_ISSUE_DEPLOYMENT_STATUS_UNKNOWN` — The Compound-fork donation vector is publicly documented and was raised in Venus's own Code4rena audit before the March 2026 exploit.
- **Falsified by:** totalAssets derived from an internal counter, not balanceOf (kills the pair); Rate is monotonic and rate-limited per block; Inbound transfers to the accounting boundary are rejected or swept to a reserve
- **Where to start:** On a fork, transfer an arbitrary amount of each counted asset directly into every accounting boundary; the share price, exchange rate and derived borrow power must not change.
- **Evidence:** `protocols/deep_screened.jsonl#sumer.money|ACC-DONATION-UNACCOUNTED-BALANCE`, `protocols/onchain_probes.json#sumer.money`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.sumer.money/security/audits

### 8. ValueDefi  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking C — mechanism match only):** 8
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

### 9. Ideamarket  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking C — mechanism match only):** 9
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

### 43. Wasabix  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking C — mechanism match only):** 43
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
    - Deployed source (`StakingPools` @ 0x0EdA8090…(ethereum), `Transmuter` @ 0x219de705…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for StakingPools@0x0EdA8090…(ethereum), Transmuter@0x219de705…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#wasabix|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#wasabix`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://wasabix-finance.gitbook.io/wasabix_finance/code/certik-audit-report

### 44. Sturdy V2  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking C — mechanism match only):** 44
- **Protocol:** Sturdy V2 (`sturdy-v2`) · Lending · Mode, Ethereum, Linea, Optimism, Flow, Sei
- **DefiLlama:** https://defillama.com/protocol/sturdy-v2
- **PRIORITY 51.68**  =  LIKELIHOOD 51.68 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 14.78/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $266,989 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`HypERC4626OwnerCollateral` @ 0x49b50F50…(ethereum), `AggregatorDataProvider` @ 0x69764E3e…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for HypERC4626OwnerCollateral@0x49b50F50…(ethereum), AggregatorDataProvider@0x69764E3e…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#sturdy-v2|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#sturdy-v2`
- **Disclosure:** https://v2.sturdy.finance/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/Zellic/publications/blob/master/Sturdy%20-%20Zellic%20Audit%20Report.pdf, https://chainsecurity.com/security-audit/sturdy-aggregator-smart-contracts/

### 45. DDEX  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking C — mechanism match only):** 45
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

### 48. Preon Finance  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking C — mechanism match only):** 48
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

### 49. Magic Eden  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking C — mechanism match only):** 49
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

### 50. Contango V1  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking C — mechanism match only):** 50
- **Protocol:** Contango V1 (`contango-v1`) · Derivatives · Arbitrum, Ethereum
- **DefiLlama:** https://defillama.com/protocol/contango-v1
- **PRIORITY 51.1**  =  LIKELIHOOD 51.1 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 14.2/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $290,609 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `version_sibling_legacy` — raises likelihood, measured lift ×1.699 (weight +0.53)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
- **Broken invariant tested:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source (`ERC1967Proxy` @ 0x30E73481…(arbitrum), `ContangoLadle` @ 0x93343c08…(arbitrum)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for ERC1967Proxy@0x30E73481…(arbitrum), ContangoLadle@0x93343c08…(arbitrum); indicators matched: unsafe_cross_sign_cast
- **Preconditions PRESENT / UNKNOWN:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** safecast_used / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#contango-v1|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#contango-v1`
- **Disclosure:** https://contango.xyz/ · no audit link listed

### 51. Velvet V3  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking C — mechanism match only):** 51
- **Protocol:** Velvet V3 (`velvet-v3`) · Yield · Base, Ethereum, Binance
- **DefiLlama:** https://defillama.com/protocol/velvet-v3
- **PRIORITY 51.08**  =  LIKELIHOOD 51.08 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 14.18/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $283,971 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`ERC1967Proxy` @ 0x7c530c9E…(ethereum), `PortfolioFactory` @ 0x6d135efd…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for ERC1967Proxy@0x7c530c9E…(ethereum), PortfolioFactory@0x6d135efd…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#velvet-v3|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#velvet-v3`
- **Disclosure:** https://dapp.velvet.capital/Referred/6956901b440d4fc522b2eb7b · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/Velvet-Capital/audits

### 52. MochiFi  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking C — mechanism match only):** 52
- **Protocol:** MochiFi (`mochifi`) · Lending · Ethereum
- **DefiLlama:** https://defillama.com/protocol/mochifi
- **PRIORITY 51.05**  =  LIKELIHOOD 51.05 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 14.15/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $414,425 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`AdminUpgradeabilityProxy` @ 0x60ef10ed…(ethereum), `MochiVaultFactory` @ 0x96076026…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for AdminUpgradeabilityProxy@0x60ef10ed…(ethereum), MochiVaultFactory@0x96076026…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#mochifi|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#mochifi`
- **Disclosure:** https://mochi.fi · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.mochi.fi/audits

### 53. Caviar V1  —  `SIG-VERIFIER-DEFEATABLE`

- **Rank (Ranking C — mechanism match only):** 53
- **Protocol:** Caviar V1 (`caviar-v1`) · NFT Marketplace · Ethereum
- **DefiLlama:** https://defillama.com/protocol/caviar-v1
- **PRIORITY 50.9**  =  LIKELIHOOD 50.9 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 14.0/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $61,437 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `version_sibling_legacy` — raises likelihood, measured lift ×1.699 (weight +0.53)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A verification routine must reject malformed, empty or zero-recovered signatures, and must never treat address(0) as a match.
    - Deployed source (`Caviar` @ 0xa964d6e8…(ethereum)): prerequisites matched: ecrecover_without_zero_check; no guard found
    - deployed source read for Caviar@0xa964d6e8…(ethereum); indicators matched: ecrecover_without_zero_check
- **Preconditions PRESENT / UNKNOWN:** src::ecrecover_without_zero_check, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** uses_oz_ecdsa / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `EOA_SINGLE_KEY`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** OZ ECDSA library in the deployed bytecode (kills the ecrecover-zero shape); Signer address immutable and non-zero
- **Where to start:** On a fork, submit r=0,s=0,v=27 and an empty signature to every signature-gated entrypoint; all must revert.
- **Evidence:** `protocols/deep_screened.jsonl#caviar-v1|SIG-VERIFIER-DEFEATABLE`, `protocols/onchain_probes.json#caviar-v1`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://code4rena.com/reports/2022-12-caviar

### 54. Aloe  —  `SIG-VERIFIER-DEFEATABLE`

- **Rank (Ranking C — mechanism match only):** 54
- **Protocol:** Aloe (`aloe`) · Lending · Arbitrum, Base, Optimism, Linea, Ethereum
- **DefiLlama:** https://defillama.com/protocol/aloe
- **PRIORITY 50.85**  =  LIKELIHOOD 50.85 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 13.95/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $71,560 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A verification routine must reject malformed, empty or zero-recovered signatures, and must never treat address(0) as a match.
    - Deployed source (`Factory` @ 0x00000000…(arbitrum)): prerequisites matched: ecrecover_without_zero_check; no guard found
    - deployed source read for Factory@0x00000000…(arbitrum); indicators matched: ecrecover_without_zero_check
- **Preconditions PRESENT / UNKNOWN:** src::ecrecover_without_zero_check, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** uses_oz_ecdsa / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** OZ ECDSA library in the deployed bytecode (kills the ecrecover-zero shape); Signer address immutable and non-zero
- **Where to start:** On a fork, submit r=0,s=0,v=27 and an empty signature to every signature-gated entrypoint; all must revert.
- **Evidence:** `protocols/deep_screened.jsonl#aloe|SIG-VERIFIER-DEFEATABLE`, `protocols/onchain_probes.json#aloe`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/aloelabs/aloe-ii/tree/master/audits

### 55. YieldFlow Yield Farming  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking C — mechanism match only):** 55
- **Protocol:** YieldFlow Yield Farming (`yieldflow-yield-farming`) · Liquidity Manager · Arbitrum, Ethereum
- **DefiLlama:** https://defillama.com/protocol/yieldflow-yield-farming
- **PRIORITY 50.82**  =  LIKELIHOOD 50.82 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 13.92/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $260,113 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`RangePositionManager` @ 0x034a5fC7…(arbitrum), `RangePositionManager` @ 0x0994b93a…(arbitrum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for RangePositionManager@0x034a5fC7…(arbitrum), RangePositionManager@0x0994b93a…(arbitrum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#yieldflow-yield-farming|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#yieldflow-yield-farming`
- **Disclosure:** https://yieldflow.com · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://skynet.certik.com/projects/yieldflow

### 57. Theoriq AlphaVault ETH  —  `SIG-VERIFIER-DEFEATABLE`

- **Rank (Ranking C — mechanism match only):** 57
- **Protocol:** Theoriq AlphaVault ETH (`theoriq-alphavault-eth`) · Onchain Capital Allocator · Ethereum
- **DefiLlama:** https://defillama.com/protocol/theoriq-alphavault-eth
- **PRIORITY 50.67**  =  LIKELIHOOD 50.67 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 13.77/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $201,442 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A verification routine must reject malformed, empty or zero-recovered signatures, and must never treat address(0) as a match.
    - Deployed source (`AToken` @ 0x6175ddec…(ethereum), `VariableDebtToken` @ 0x86c71796…(ethereum)): prerequisites matched: ecrecover_without_zero_check; no guard found
    - deployed source read for AToken@0x6175ddec…(ethereum), VariableDebtToken@0x86c71796…(ethereum); indicators matched: ecrecover_without_zero_check
- **Preconditions PRESENT / UNKNOWN:** src::ecrecover_without_zero_check, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** uses_oz_ecdsa / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** OZ ECDSA library in the deployed bytecode (kills the ecrecover-zero shape); Signer address immutable and non-zero
- **Where to start:** On a fork, submit r=0,s=0,v=27 and an empty signature to every signature-gated entrypoint; all must revert.
- **Evidence:** `protocols/deep_screened.jsonl#theoriq-alphavault-eth|SIG-VERIFIER-DEFEATABLE`, `protocols/onchain_probes.json#theoriq-alphavault-eth`
- **Disclosure:** https://theoriq.ai/ · no audit link listed

### 58. Ajna V1  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking C — mechanism match only):** 58
- **Protocol:** Ajna V1 (`ajna-v1`) · Lending · Ethereum
- **DefiLlama:** https://defillama.com/protocol/ajna-v1
- **PRIORITY 50.32**  =  LIKELIHOOD 50.32 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 13.42/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $491,042 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `version_sibling_legacy` — raises likelihood, measured lift ×1.699 (weight +0.53)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`ERC20PoolFactory` @ 0xe6f4d971…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for ERC20PoolFactory@0xe6f4d971…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#ajna-v1|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#ajna-v1`
- **Disclosure:** https://www.ajna.finance/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/ajna-finance/audits

### 59. SIR  —  `SIG-VERIFIER-DEFEATABLE`

- **Rank (Ranking C — mechanism match only):** 59
- **Protocol:** SIR (`sir`) · Derivatives · Ethereum, MegaETH, Hyperliquid L1
- **DefiLlama:** https://defillama.com/protocol/sir
- **PRIORITY 50.07**  =  LIKELIHOOD 50.07 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 13.17/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $106,823 · **Band:** `IN_BAND`
- **Previously hacked:** 2025-03-30 for $355,000 [Proxy Upgrade Hijack]
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A verification routine must reject malformed, empty or zero-recovered signatures, and must never treat address(0) as a match.
    - Deployed source (`Vault` @ 0x7Dad75dD…(ethereum), `SystemControl` @ 0x8d694D1b…(ethereum)): prerequisites matched: ecrecover_without_zero_check; no guard found
    - deployed source read for Vault@0x7Dad75dD…(ethereum), SystemControl@0x8d694D1b…(ethereum); indicators matched: ecrecover_without_zero_check
- **Preconditions PRESENT / UNKNOWN:** src::ecrecover_without_zero_check, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** uses_oz_ecdsa / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `KNOWN_ISSUE_DEPLOYMENT_STATUS_UNKNOWN` — DefiLlama's hacks dataset records 1 prior on-chain incident(s) on this protocol, most recently 2025-03-30 for $355,000 [Proxy Upgrade Hijack]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** OZ ECDSA library in the deployed bytecode (kills the ecrecover-zero shape); Signer address immutable and non-zero
- **Where to start:** On a fork, submit r=0,s=0,v=27 and an empty signature to every signature-gated entrypoint; all must revert.
- **Evidence:** `protocols/deep_screened.jsonl#sir|SIG-VERIFIER-DEFEATABLE`, `protocols/onchain_probes.json#sir`
- **Disclosure:** https://www.sir.trading · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/Egis-Security/audits/blob/main/reports/SIR-Trading.pdf

### 60. pSTAKE LSD  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking C — mechanism match only):** 60
- **Protocol:** pSTAKE LSD (`pstake-lsd`) · Liquid Staking · Binance, Persistence
- **DefiLlama:** https://defillama.com/protocol/pstake-lsd
- **PRIORITY 49.98**  =  LIKELIHOOD 49.98 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 13.08/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $192,828 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`StakePool` @ 0xc54a9c4a…(bsc)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for StakePool@0xc54a9c4a…(bsc); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a timelock with a real delay** (`TIMELOCK`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#pstake-lsd|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#pstake-lsd`
- **Disclosure:** https://pstake.finance · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://consensys.net/diligence/audits/private/61fqr5mouh4oq8/, https://github.com/persistenceOne/pStake-auditReports
