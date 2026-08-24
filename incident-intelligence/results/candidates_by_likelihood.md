# Candidates — Ranking B — likelihood, ignoring actionability

> **Discovery stage.** This file asserts no defect in any protocol named below. Each entry is a *review candidate*: named evidence matches a family's prerequisites, named evidence is unknown, and a named guard would falsify it. Verify on a local or pinned fork before concluding anything.

**How these are scored** is set out once, at the top of [`candidates_by_priority.md`](candidates_by_priority.md): the out-of-sample validation, why likelihood and actionability are kept apart, and why custody exposure is reported separately.

### The ranking

Full write-ups below for the 40 entries that `candidates_by_priority.md` does not already cover; the other 20 are listed here and written up in full there, under the same `protocol — family` heading.

| # | Protocol | Family | LIKELIHOOD | At risk | Write-up |
|---:|---|---|---:|---:|---|
| 1 | [SMARDEX AMM](https://defillama.com/protocol/smardex-amm) | `ACC-QUOTE-STALE-ACROSS-OWN-SWAP` | 58.88 | $153,633 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 2 | [KyberSwap Elastic](https://defillama.com/protocol/kyberswap-elastic) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 57.23 | $127,719 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 3 | [Silo V3](https://defillama.com/protocol/silo-v3) | `ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE` | 54.68 | $1,744,058 | below |
| 4 | [Equilibria](https://defillama.com/protocol/equilibria) | `ACC-DUPLICATE-ID-ACCUMULATION` | 54.53 | $11,256,299 | below |
| 5 | [MoneyFi](https://defillama.com/protocol/moneyfi) | `ACC-QUOTE-STALE-ACROSS-OWN-SWAP` | 54.47 | $117,775 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 6 | [Moonwell Lending](https://defillama.com/protocol/moonwell-lending) | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | 54.12 | $52,209,288 | below |
| 7 | [Varen](https://defillama.com/protocol/varen) | `ACC-QUOTE-STALE-ACROSS-OWN-SWAP` | 53.82 | $135,783 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 8 | [Privacy Cash](https://defillama.com/protocol/privacy-cash) | `AUTH-ZERO-ADDRESS-ACCEPTED` | 53.7 | $2,032,171 | below |
| 9 | [MCDEX](https://defillama.com/protocol/mcdex) | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | 53.53 | $1,361,624 | below |
| 10 | [Swaap Maker V2](https://defillama.com/protocol/swaap-maker-v2) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 53.28 | $7,049,096 | below |
| 11 | [Singular Farm](https://defillama.com/protocol/singular-farm) | `ACC-QUOTE-STALE-ACROSS-OWN-SWAP` | 53.12 | $2,079,500 | below |
| 12 | [YieldNest](https://defillama.com/protocol/yieldnest) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 52.8 | $23,833,613 | below |
| 13 | [Ankr](https://defillama.com/protocol/ankr) | `AUTH-ZERO-ADDRESS-ACCEPTED` | 52.73 | $25,346,137 | below |
| 14 | [Hop Protocol](https://defillama.com/protocol/hop-protocol) | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | 52.5 | $3,786,525 | below |
| 15 | [SunX Bridge](https://defillama.com/protocol/sunx-bridge) | `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY` | 52.5 | $26,479,035 | below |
| 16 | [Harvest Finance](https://defillama.com/protocol/harvest-finance) | `AUTH-ZERO-ADDRESS-ACCEPTED` | 52.5 | $18,484,326 | below |
| 17 | [Elk](https://defillama.com/protocol/elk) | `ACC-QUOTE-STALE-ACROSS-OWN-SWAP` | 52.45 | $160,743 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 18 | [Vault Street primeUSD](https://defillama.com/protocol/vault-street-primeusd) | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | 52.42 | $6,374,323 | below |
| 19 | [Overtime](https://defillama.com/protocol/overtime) | `AUTH-ZERO-ADDRESS-ACCEPTED` | 52.42 | $1,159,711 | below |
| 20 | [Orbit Bridge](https://defillama.com/protocol/orbit-bridge) | `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY` | 52.2 | $18,334,933 | below |
| 21 | [Gnosis Protocol v1](https://defillama.com/protocol/gnosis-protocol-v1) | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | 52.05 | $2,429,436 | below |
| 22 | [SparkLend](https://defillama.com/protocol/sparklend) | `LIQUIDATION-ON-MANIPULABLE-VALUATION` | 52.03 | $4,781,673,048 | below |
| 23 | [SectorOne DLMM](https://defillama.com/protocol/sectorone-dlmm) | `ACC-QUOTE-STALE-ACROSS-OWN-SWAP` | 51.82 | $253,917 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 24 | [Reservoir Protocol](https://defillama.com/protocol/reservoir-protocol) | `AUTH-ZERO-ADDRESS-ACCEPTED` | 51.77 | $26,793,977 | below |
| 25 | [Hunny Finance](https://defillama.com/protocol/hunny-finance) | `ACC-QUOTE-STALE-ACROSS-OWN-SWAP` | 51.75 | $528,141 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 26 | [Makina](https://defillama.com/protocol/makina) | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | 51.75 | $42,438,316 | below |
| 27 | [B.Protocol](https://defillama.com/protocol/b.protocol) | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | 51.6 | $1,824,523 | below |
| 28 | [Wing Finance](https://defillama.com/protocol/wing-finance) | `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY` | 51.57 | $5,173,532 | below |
| 29 | [Mountain Protocol](https://defillama.com/protocol/mountain-protocol) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 51.5 | $1,402,690 | below |
| 30 | [Steer Protocol](https://defillama.com/protocol/steer-protocol) | `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY` | 51.5 | $20,439,704 | below |
| 31 | [LendFlare](https://defillama.com/protocol/lendflare) | `AUTH-ZERO-ADDRESS-ACCEPTED` | 51.47 | $1,171,712 | below |
| 32 | [basedbid](https://defillama.com/protocol/basedbid) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 51.42 | $59,576 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 33 | [De1](https://defillama.com/protocol/de1) | `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY` | 51.4 | $130,275 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 34 | [Landshare](https://defillama.com/protocol/landshare) | `ACC-QUOTE-STALE-ACROSS-OWN-SWAP` | 51.38 | $621,293 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 35 | [Unitus](https://defillama.com/protocol/unitus) | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | 51.33 | $6,337,750 | below |
| 36 | [SmartCredit](https://defillama.com/protocol/smartcredit) | `ORACLE-SPOT-THIN-LIQUIDITY` | 51.3 | $204,900 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 37 | [ICHI](https://defillama.com/protocol/ichi) | `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY` | 51.27 | $7,949,093 | below |
| 38 | [TAU Labs](https://defillama.com/protocol/tau-labs) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 51.23 | $8,297,367 | below |
| 39 | [Spectra MetaVaults Outside V2](https://defillama.com/protocol/spectra-metavaults-outside-v2) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 51.23 | $3,562,036 | below |
| 40 | [Krystal Community Vault](https://defillama.com/protocol/krystal-community-vault) | `ACC-DUPLICATE-ID-ACCUMULATION` | 51.18 | $229,978 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 41 | [TreeDefi](https://defillama.com/protocol/treedefi) | `ACC-QUOTE-STALE-ACROSS-OWN-SWAP` | 51.08 | $71,298 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 42 | [Nomiswap](https://defillama.com/protocol/nomiswap) | `ACC-QUOTE-STALE-ACROSS-OWN-SWAP` | 51.08 | $1,364,610 | below |
| 43 | [Aave V1](https://defillama.com/protocol/aave-v1) | `ORACLE-SPOT-THIN-LIQUIDITY` | 51.07 | $7,651,606 | below |
| 44 | [Cronos zkEVM Bridge](https://defillama.com/protocol/cronos-zkevm-bridge) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 51.07 | $20,070,907 | below |
| 45 | [Asseto CASH+](https://defillama.com/protocol/asseto-cash+) | `ACC-DUPLICATE-ID-ACCUMULATION` | 50.9 | $1,501,710 | below |
| 46 | [PoolTogether V5](https://defillama.com/protocol/pooltogether-v5) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 50.85 | $5,567,621 | below |
| 47 | [xToken](https://defillama.com/protocol/xtoken) | `AUTH-ZERO-ADDRESS-ACCEPTED` | 50.83 | $931,371 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 48 | [Peapods Finance](https://defillama.com/protocol/peapods-finance) | `AUTH-ZERO-ADDRESS-ACCEPTED` | 50.63 | $2,030,459 | below |
| 49 | [Yearn Finance](https://defillama.com/protocol/yearn-finance) | `SIG-VERIFIER-DEFEATABLE` | 50.55 | $186,365,987 | below |
| 50 | [Kromatika](https://defillama.com/protocol/kromatika) | `AUTH-ZERO-ADDRESS-ACCEPTED` | 50.33 | $1,178,668 | below |
| 51 | [Clipper](https://defillama.com/protocol/clipper) | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | 50.32 | $781,257 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 52 | [Unslashed](https://defillama.com/protocol/unslashed) | `AUTH-ZERO-ADDRESS-ACCEPTED` | 50.28 | $3,596,677 | below |
| 53 | [Antfarm finance](https://defillama.com/protocol/antfarm-finance) | `SIG-VERIFIER-DEFEATABLE` | 50.15 | $179,394 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 54 | [Joe DEX](https://defillama.com/protocol/joe-dex) | `ACC-QUOTE-STALE-ACROSS-OWN-SWAP` | 50.02 | $9,610,102 | below |
| 55 | [Astaria V2](https://defillama.com/protocol/astaria-v2) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 49.95 | $60,757 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 56 | [Swapr V2](https://defillama.com/protocol/swapr-v2) | `ACC-QUOTE-STALE-ACROSS-OWN-SWAP` | 49.95 | $335,996 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 57 | [Yield Protocol](https://defillama.com/protocol/yield-protocol) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 49.95 | $203,354 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 58 | [Stafi](https://defillama.com/protocol/stafi) | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | 49.92 | $3,579,497 | below |
| 59 | [Orderly Bridge](https://defillama.com/protocol/orderly-bridge) | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | 49.92 | $28,007,293 | below |
| 60 | [MIM Swap](https://defillama.com/protocol/mim-swap) | `AUTH-ZERO-ADDRESS-ACCEPTED` | 49.87 | $123,612 | [in `candidates_by_priority.md`](candidates_by_priority.md) |

---

### 3. Silo V3  —  `ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE`

- **Rank (Ranking B — likelihood, ignoring actionability):** 3
- **Protocol:** Silo V3 (`silo-v3`) · Lending · Avalanche, Ethereum, XDC, Arbitrum, Sonic, MegaETH
- **DefiLlama:** https://defillama.com/protocol/silo-v3
- **PRIORITY 46.48**  =  LIKELIHOOD 54.68 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 22.78/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,744,058 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A vault share rate is an accounting quantity of another protocol, not a market price. Using it as a feed imports every way that vault's rate can be moved, including donation inflation and same-transaction redemption effects.
    - Deployed source (`ShareProtectedCollateralToken` @ 0x1dab4a31…(arbitrum), `DynamicKinkModel` @ 0x95a7bc57…(arbitrum)): prerequisites matched: rate_used_as_price; no guard found
    - deployed source read for ShareProtectedCollateralToken@0x1dab4a31…(arbitrum), DynamicKinkModel@0x95a7bc57…(arbitrum); indicators matched: rate_used_as_price
    - only one oracle (or none) is declared in DefiLlama metadata; this is a prioritisation signal about disclosure, not evidence that no cross-source deviation bound exists in code
    - declared oracles: none declared
- **Preconditions PRESENT / UNKNOWN:** src::rate_used_as_price, value_decision_reads_configured_feed, live_positions_exposed / feed_selection_is_configuration
- **Guards searched / found:** deviation_bound_vs_independent_source / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Growth-capped rate adapter in the deployed oracle (kills the pair); Wrapper's own rate is monotonic and rate-limited; Collateral priced by an independent market feed instead
- **Where to start:** On a fork, donate to and cycle the underlying vault; assert the lending market's reported collateral price moves no more than the configured cap.
- **Evidence:** `protocols/deep_screened.jsonl#silo-v3|ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE`, `protocols/onchain_probes.json#silo-v3`
- **Disclosure:** https://app.silo.finance · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.silo.finance/audits-and-tests

### 4. Equilibria  —  `ACC-DUPLICATE-ID-ACCUMULATION`

- **Rank (Ranking B — likelihood, ignoring actionability):** 4
- **Protocol:** Equilibria (`equilibria`) · Yield · Ethereum, Binance, Arbitrum, Base, Sonic, Mantle …
- **DefiLlama:** https://defillama.com/protocol/equilibria
- **PRIORITY 32.72**  =  LIKELIHOOD 54.53 × ACTIONABILITY 60.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 22.63/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $11,256,299 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** An entitlement attached to an identifier may be counted at most once per period. A caller-supplied ID list must be deduplicated, or each ID's claim state consumed before the next read.
    - Deployed source (`VlEqb` @ 0x660e0d05…(bsc), `EqbMsgSendEndpoint` @ 0xb14f643d…(bsc)): prerequisites matched: id_array_loop_without_dedup; no guard found
    - deployed source read for VlEqb@0x660e0d05…(bsc), EqbMsgSendEndpoint@0xb14f643d…(bsc); indicators matched: id_array_loop_without_dedup
- **Preconditions PRESENT / UNKNOWN:** src::id_array_loop_without_dedup, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Consumed marker written inside the loop (kills the pair); IDs required strictly increasing
- **Where to start:** On a fork, call the batch function with one ID repeated k times; payout must equal the single-ID payout.
- **Evidence:** `protocols/deep_screened.jsonl#equilibria|ACC-DUPLICATE-ID-ACCUMULATION`, `protocols/onchain_probes.json#equilibria`
- **Disclosure:** https://equilibria.fi/home · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.equilibria.fi/security-and-risk/audit-report

### 6. Moonwell Lending  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking B — likelihood, ignoring actionability):** 6
- **Protocol:** Moonwell Lending (`moonwell-lending`) · Lending · Base, Ethereum, Optimism, Moonbeam
- **DefiLlama:** https://defillama.com/protocol/moonwell-lending
- **PRIORITY 10.82**  =  LIKELIHOOD 54.12 × ACTIONABILITY 20.0%
    - likelihood = family evidence 30.0/50 (MATCH 60 × evidence weight 1.0) + learned attack surface 24.12/50
    - actionability: above the band: assume dedicated professional coverage
- **Value at risk:** $52,209,288 · **Band:** `ABOVE_BAND_KEPT_EXPLICIT_DANGER`
- **REPEAT VICTIM — 2 recorded hacks.** 2026-02-15 $1,780,000 [Oracle Misconfiguration]; 2025-11-04 $1,000,000 [Spot Price Manipulation]
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 60 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `unverified_implementation` — raises likelihood, measured lift ×2.062 (weight +0.72)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
- **Broken invariant tested:** After deployment, no caller may (re)establish ownership, admin, or implementation wiring. Initialization state must be provably consumed.
    - Deployed source (`CErc20Immutable` @ 0x004c0908…(ethereum)): prerequisites matched: initialize_without_modifier; no guard found
    - deployed source read for CErc20Immutable@0x004c0908…(ethereum); indicators matched: initialize_without_modifier
    - 1 implementation(s) behind a proxy are NOT verified on the explorer: implementation identity unresolved, score capped at 60
    - 1/1 live proxies read a zero ERC-7201 Initializable slot (inconclusive alone: older OZ versions store the flag elsewhere)
- **Preconditions PRESENT / UNKNOWN:** src::initialize_without_modifier, upgradeable_architecture, initializer_flag_unset, live_value_or_approvals / none
- **Guards searched / found:** initializer_modifier_present, upgrade_timelocked / upgrade_timelocked
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `UNREMEDIATED_KNOWN_ISSUE` — DefiLlama's hacks dataset records 2 prior on-chain incident(s) on this protocol, most recently 2026-02-15 for $1,780,000 [Oracle Misconfiguration]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** Simulated re-initialization reverts (kills the pair); Contract is non-upgradeable and holds no approvals
- **Where to start:** Read the initialization slot on every live proxy/facet and simulate re-initialization from an unprivileged address; it must revert.
- **Evidence:** `protocols/deep_screened.jsonl#moonwell-lending|UPGRADE-INITIALIZER-REACHABLE-LIVE`, `protocols/onchain_probes.json#moonwell-lending`
- **Disclosure:** https://moonwell.fi · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/HalbornSecurity/PublicReports/blob/master/Solidity%20Smart%20Contract%20Audits/Moonwell_Finance_Smart_Contract_Security_Audit_Report_Halborn_Final.pdf, https://github.com/HalbornSecurity/PublicReports/blob/master/Solidity%20Smart%20Contract%20Audits/Moonwell_Finance_Safety_Module_Smart_Contract_Security_Audit_Report_Halborn_Final.pdf

### 8. Privacy Cash  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking B — likelihood, ignoring actionability):** 8
- **Protocol:** Privacy Cash (`privacy-cash`) · Privacy · Solana, Ethereum, Base, Robinhood Chain, Binance
- **DefiLlama:** https://defillama.com/protocol/privacy-cash
- **PRIORITY 45.65**  =  LIKELIHOOD 53.7 × ACTIONABILITY 85.0%
    - likelihood = family evidence 30.0/50 (MATCH 60 × evidence weight 1.0) + learned attack surface 23.7/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $2,032,171 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 60 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `unverified_implementation` — raises likelihood, measured lift ×2.062 (weight +0.72)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`EtherPool` @ 0xec5266c9…(ethereum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for EtherPool@0xec5266c9…(ethereum); indicators matched: owner_compare_without_nonzero
    - 1 implementation(s) behind a proxy are NOT verified on the explorer: implementation identity unresolved, score capped at 60
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#privacy-cash|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#privacy-cash`
- **Disclosure:** https://privacycash.org/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/Privacy-Cash/privacy-cash/tree/main/audits

### 9. MCDEX  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking B — likelihood, ignoring actionability):** 9
- **Protocol:** MCDEX (`mcdex`) · Dexs · Ethereum, Binance, Arbitrum
- **DefiLlama:** https://defillama.com/protocol/mcdex
- **PRIORITY 45.5**  =  LIKELIHOOD 53.53 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 21.63/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,361,624 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`Perpetual` @ 0x220a9f0D…(ethereum), `EthMCBv2` @ 0xcbe10aa4…(ethereum)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for Perpetual@0x220a9f0D…(ethereum), EthMCBv2@0xcbe10aa4…(ethereum); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#mcdex|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#mcdex`
- **Disclosure:** https://mux.network/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://www.certik.com/projects/mux-protocol

### 10. Swaap Maker V2  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 10
- **Protocol:** Swaap Maker V2 (`swaap-maker-v2`) · Dexs · Ethereum, Base, Arbitrum, Binance, Polygon, Optimism …
- **DefiLlama:** https://defillama.com/protocol/swaap-maker-v2
- **PRIORITY 45.29**  =  LIKELIHOOD 53.28 × ACTIONABILITY 85.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 16.38/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $7,049,096 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`SafeguardFactory` @ 0x03c01aca…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for SafeguardFactory@0x03c01aca…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#swaap-maker-v2|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#swaap-maker-v2`
- **Disclosure:** https://www.swaap.finance · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://chainsecurity.com/security-audit/swaap-finance-safeguardpool/, https://runtimeverification.com/blog/runtime-verification-audits-swaap-s-pool-smart-contracts

### 11. Singular Farm  —  `ACC-QUOTE-STALE-ACROSS-OWN-SWAP`

- **Rank (Ranking B — likelihood, ignoring actionability):** 11
- **Protocol:** Singular Farm (`singular-farm`) · Yield · Binance, Polygon, Avalanche, Fantom
- **DefiLlama:** https://defillama.com/protocol/singular-farm
- **PRIORITY 45.15**  =  LIKELIHOOD 53.12 × ACTIONABILITY 85.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 16.22/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $2,079,500 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A value used for minting, crediting or reward must be derived from what the protocol actually received, not from a quote taken before the protocol itself moved the market. Where the protocol's own action changes the price it just read, the value must be recomputed after the fact.
    - Deployed source (`SingToken` @ 0x23894C0c…(bsc), `MasterSing` @ 0x31B05a72…(bsc)): prerequisites matched: quote_then_own_swap; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): referral_reward_with_mint=no
    - deployed source read for SingToken@0x23894C0c…(bsc), MasterSing@0x31B05a72…(bsc); indicators matched: quote_then_own_swap
- **Preconditions PRESENT / UNKNOWN:** src::quote_then_own_swap, live_value_present, deployment_reachable_on_chain / src::quote_then_addliquidity
- **Guards searched / found:** lp_delta_measured, twap_or_feed_for_accounting / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `EOA_SINGLE_KEY`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** The minted amount is derived from the LP balance delta or from a TWAP (kills the pair); The protocol's swap is bounded so it cannot move reserves materially; Rewards settle in a later block against re-measured backing
- **Where to start:** On a fork, run the bonding path with a flash-funded swap sized to skew the pair, then assert that the minted or credited amount tracks the LP tokens actually received rather than the pre-swap quote.
- **Evidence:** `protocols/deep_screened.jsonl#singular-farm|ACC-QUOTE-STALE-ACROSS-OWN-SWAP`, `protocols/onchain_probes.json#singular-farm`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://solidity.finance/audits/MasterSing

### 12. YieldNest  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking B — likelihood, ignoring actionability):** 12
- **Protocol:** YieldNest (`yieldnest`) · Onchain Capital Allocator · Ethereum, Binance
- **DefiLlama:** https://defillama.com/protocol/yieldnest
- **PRIORITY 31.68**  =  LIKELIHOOD 52.8 × ACTIONABILITY 60.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 15.9/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $23,833,613 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source (`KernelStrategy` @ 0x835349a9…(bsc), `KernelStrategy` @ 0x0e64643d…(bsc)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for KernelStrategy@0x835349a9…(bsc), KernelStrategy@0x0e64643d…(bsc); indicators matched: unsafe_cross_sign_cast
- **Preconditions PRESENT / UNKNOWN:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** safecast_used / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a timelock with a real delay** (`TIMELOCK`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#yieldnest|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#yieldnest`
- **Disclosure:** https://yieldnest.finance/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/yieldnest/Publications/tree/main/audits

### 13. Ankr  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking B — likelihood, ignoring actionability):** 13
- **Protocol:** Ankr (`ankr`) · Liquid Staking · Ethereum, Flow, Binance, Avalanche, Polkadot, Fantom …
- **DefiLlama:** https://defillama.com/protocol/ankr
- **PRIORITY 31.64**  =  LIKELIHOOD 52.73 × ACTIONABILITY 60.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 20.83/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $25,346,137 · **Band:** `IN_BAND`
- **Previously hacked:** 2022-12-02 for $5,000,000 [Improper Access Control]
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`TransparentUpgradeableProxy` @ 0x26dcfbfa…(ethereum), `GlobalPool_R42` @ 0x52F24a5e…(ethereum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for TransparentUpgradeableProxy@0x26dcfbfa…(ethereum), GlobalPool_R42@0x52F24a5e…(ethereum); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `KNOWN_ISSUE_DEPLOYMENT_STATUS_UNKNOWN` — DefiLlama's hacks dataset records 1 prior on-chain incident(s) on this protocol, most recently 2022-12-02 for $5,000,000 [Improper Access Control]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#ankr|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#ankr`
- **Disclosure:** https://www.ankr.com/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://assets.ankr.com/files/stkr_smart_contract_auditing_report.pdf

### 14. Hop Protocol  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking B — likelihood, ignoring actionability):** 14
- **Protocol:** Hop Protocol (`hop-protocol`) · Cross Chain Bridge · Ethereum, Optimism, Arbitrum, Polygon, Base, xDai …
- **DefiLlama:** https://defillama.com/protocol/hop-protocol
- **PRIORITY 44.62**  =  LIKELIHOOD 52.5 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 20.6/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $3,786,525 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 84.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`L2_HOPToken` @ 0xc5102fe9…(base)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for L2_HOPToken@0xc5102fe9…(base); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#hop-protocol|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#hop-protocol`
- **Disclosure:** https://hop.exchange · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.hop.exchange/faq#are-hop-contracts-audited

### 15. SunX Bridge  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 15
- **Protocol:** SunX Bridge (`sunx-bridge`) · Bridge · Tron, Ethereum, Binance, Arbitrum
- **DefiLlama:** https://defillama.com/protocol/sunx-bridge
- **PRIORITY 31.5**  =  LIKELIHOOD 52.5 × ACTIONABILITY 60.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 26.1/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $26,479,035 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - Conditions: `REBRANDED_DEPLOYMENT`
    - condition REBRANDED_DEPLOYMENT (PRIORITY): Operated under previous names, so contracts deployed under the old identity may still be live and unwatched.
    - 6 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** prior_version_still_callable, still_holds_value_or_authority / unmaintained_or_differing_code_path, not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#sunx-bridge|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#sunx-bridge`
- **Disclosure:** https://www.sunx.io/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/slowmist/Knowledge-Base/blob/master/open-report-V2/smart-contract/Sunperp%20Dex%20-%20SlowMist%20Audit%20Report.pdf

### 16. Harvest Finance  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking B — likelihood, ignoring actionability):** 16
- **Protocol:** Harvest Finance (`harvest-finance`) · Yield Aggregator · Base, Ethereum, Arbitrum, Polygon, zkSync Era
- **DefiLlama:** https://defillama.com/protocol/harvest-finance
- **PRIORITY 31.5**  =  LIKELIHOOD 52.5 × ACTIONABILITY 60.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 20.6/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $18,484,326 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 79.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`RewardToken` @ 0xa0246c90…(ethereum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for RewardToken@0xa0246c90…(ethereum); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#harvest-finance|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#harvest-finance`
- **Disclosure:** https://harvest.finance/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/harvest-finance/harvest/tree/master/audits

### 18. Vault Street primeUSD  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking B — likelihood, ignoring actionability):** 18
- **Protocol:** Vault Street primeUSD (`vault-street-primeusd`) · RWA · Ethereum
- **DefiLlama:** https://defillama.com/protocol/vault-street-primeusd
- **PRIORITY 44.56**  =  LIKELIHOOD 52.42 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 20.52/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $6,374,323 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`PermissionedToken` @ 0xb0b01a72…(ethereum), `PriceStorage` @ 0x03e0116b…(ethereum)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for PermissionedToken@0xb0b01a72…(ethereum), PriceStorage@0x03e0116b…(ethereum); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#vault-street-primeusd|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#vault-street-primeusd`
- **Disclosure:** https://www.vaultstreet.com/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.vaultstreet.com/resources/security-and-audits

### 19. Overtime  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking B — likelihood, ignoring actionability):** 19
- **Protocol:** Overtime (`overtime`) · Prediction Market · Arbitrum, Optimism, Base, Polygon, Ethereum, Binance
- **DefiLlama:** https://defillama.com/protocol/overtime
- **PRIORITY 44.56**  =  LIKELIHOOD 52.42 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 20.52/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,159,711 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 79.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`OverToken` @ 0x90ce5720…(ethereum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for OverToken@0x90ce5720…(ethereum); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `EOA_SINGLE_KEY`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#overtime|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#overtime`
- **Disclosure:** https://www.overtimemarkets.xyz · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://iosiro.com/audits/thales-airdrop-and-staking-smart-contract-audit, https://github.com/decurity/audits/blob/master/ThalesMarket/thales-market-speedmarkets-audit-report-1.1.pdf

### 20. Orbit Bridge  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 20
- **Protocol:** Orbit Bridge (`orbit-bridge`) · Bridge · Silicon zkEVM, Ripple, Binance, Klaytn, WEMIX, Ethereum …
- **DefiLlama:** https://defillama.com/protocol/orbit-bridge
- **PRIORITY 31.32**  =  LIKELIHOOD 52.2 × ACTIONABILITY 60.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 25.8/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $18,334,933 · **Band:** `IN_BAND`
- **Previously hacked:** 2023-12-31 for $81,700,000 [Signature Verification Flaw]
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `unverified_implementation` — raises likelihood, measured lift ×2.062 (weight +0.72)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - Conditions: `MULTICHAIN_VERSION_DRIFT`
    - condition MULTICHAIN_VERSION_DRIFT (PRIORITY): Deployed across many chains, where per-chain deployments drift and the least-watched chain sets the risk.
    - 4 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** prior_version_still_callable, still_holds_value_or_authority / unmaintained_or_differing_code_path, not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `KNOWN_ISSUE_DEPLOYMENT_STATUS_UNKNOWN` — DefiLlama's hacks dataset records 1 prior on-chain incident(s) on this protocol, most recently 2023-12-31 for $81,700,000 [Signature Verification Flaw]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#orbit-bridge|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#orbit-bridge`
- **Disclosure:** https://bridge.orbitchain.io · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/orbit-chain/bridge-contract/blob/master/audit/Theori_OrbitBridge_2022_1Q.pdf

### 21. Gnosis Protocol v1  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking B — likelihood, ignoring actionability):** 21
- **Protocol:** Gnosis Protocol v1 (`gnosis-protocol-v1`) · Prediction Market · Ethereum
- **DefiLlama:** https://defillama.com/protocol/gnosis-protocol-v1
- **PRIORITY 44.24**  =  LIKELIHOOD 52.05 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 20.15/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $2,429,436 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`Api3Token` @ 0x0b38210e…(ethereum), `BaseToken` @ 0x22eEab2f…(ethereum)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for Api3Token@0x0b38210e…(ethereum), BaseToken@0x22eEab2f…(ethereum); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#gnosis-protocol-v1|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#gnosis-protocol-v1`
- **Disclosure:** https://gnosis.io/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.gnosis.io/safe/docs/intro_audits/

### 22. SparkLend  —  `LIQUIDATION-ON-MANIPULABLE-VALUATION`

- **Rank (Ranking B — likelihood, ignoring actionability):** 22
- **Protocol:** SparkLend (`sparklend`) · Lending · Ethereum, xDai
- **DefiLlama:** https://defillama.com/protocol/sparklend
- **PRIORITY 2.6**  =  LIKELIHOOD 52.03 × ACTIONABILITY 5.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 25.63/50
    - actionability: far above the band: continuous professional coverage assumed
- **Value at risk:** $4,781,673,048 · **Band:** `ABOVE_BAND_KEPT_EXPLICIT_DANGER`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 69.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A position may be liquidated only on a valuation that the liquidator cannot move, and the discount captured must not exceed the cost of moving the price.
    - Conditions: `FORK_OF_WINDOW_VICTIM`
    - condition FORK_OF_WINDOW_VICTIM (LINEAGE): Forked from a protocol that was exploited inside the six-month window: the fork inherits the upstream defect until the patch is proven present in ITS deployed bytecode.
    - price oracle resolved on-chain: 0x01b76559… -> 0x8a4236f5ef…
    - declared oracles: Chainlink, Chronicle, RedStone (types: Aggregator)
- **Preconditions PRESENT / UNKNOWN:** value_decision_reads_configured_feed, feed_selection_is_configuration, oracle_contract_resolved_on_chain, live_positions_exposed / none
- **Guards searched / found:** deviation_bound_vs_independent_source / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Deviation-capped, independently sourced price plus a grace period (kills the pair); Liquidations rate-limited per block; Collateral only in deep assets with caps sized to depth
- **Where to start:** On a fork, execute the largest flash-funded move available on each pricing venue and assert that no position becomes liquidatable beyond the configured deviation bound.
- **Evidence:** `protocols/deep_screened.jsonl#sparklend|LIQUIDATION-ON-MANIPULABLE-VALUATION`, `protocols/onchain_probes.json#sparklend`
- **Disclosure:** https://spark.finance/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://devs.spark.fi/security/security-and-audits

### 24. Reservoir Protocol  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking B — likelihood, ignoring actionability):** 24
- **Protocol:** Reservoir Protocol (`reservoir-protocol`) · CDP · Ethereum, Plasma, Monad, World Chain, Berachain, Binance …
- **DefiLlama:** https://defillama.com/protocol/reservoir-protocol
- **PRIORITY 31.06**  =  LIKELIHOOD 51.77 × ACTIONABILITY 60.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 19.87/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $26,793,977 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`DolomiteMargin` @ 0x003ca23f…(bsc)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for DolomiteMargin@0x003ca23f…(bsc); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#reservoir-protocol|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#reservoir-protocol`
- **Disclosure:** https://app.reservoir.xyz · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://www.halborn.com/audits/fortunafi/reservoir-updated

### 26. Makina  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking B — likelihood, ignoring actionability):** 26
- **Protocol:** Makina (`makina`) · Onchain Capital Allocator · Ethereum
- **DefiLlama:** https://defillama.com/protocol/makina
- **PRIORITY 10.35**  =  LIKELIHOOD 51.75 × ACTIONABILITY 20.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 19.85/50
    - actionability: above the band: assume dedicated professional coverage
- **Value at risk:** $42,438,316 · **Band:** `ABOVE_BAND_KEPT_EXPLICIT_DANGER`
- **Previously hacked:** 2026-01-19 for $4,200,000 [Spot Price Manipulation]
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`MachineShare` @ 0x1004D230…(ethereum), `MachineShare` @ 0x871ab8e3…(ethereum)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for MachineShare@0x1004D230…(ethereum), MachineShare@0x871ab8e3…(ethereum); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `KNOWN_ISSUE_DEPLOYMENT_STATUS_UNKNOWN` — DefiLlama's hacks dataset records 1 prior on-chain incident(s) on this protocol, most recently 2026-01-19 for $4,200,000 [Spot Price Manipulation]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#makina|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#makina`
- **Disclosure:** https://app.makina.finance/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.makina.finance/concepts/security/audits

### 27. B.Protocol  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking B — likelihood, ignoring actionability):** 27
- **Protocol:** B.Protocol (`b.protocol`) · Liquidations · Ethereum, Arbitrum, Polygon, Fantom
- **DefiLlama:** https://defillama.com/protocol/b.protocol
- **PRIORITY 43.86**  =  LIKELIHOOD 51.6 × ACTIONABILITY 85.0%
    - likelihood = family evidence 30.0/50 (MATCH 60 × evidence weight 1.0) + learned attack surface 21.6/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,824,523 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 60 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `unverified_implementation` — raises likelihood, measured lift ×2.062 (weight +0.72)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** After deployment, no caller may (re)establish ownership, admin, or implementation wiring. Initialization state must be provably consumed.
    - Deployed source (`CErc20Delegate` @ 0xbb93c7f3…(ethereum)): prerequisites matched: initialize_without_modifier; no guard found
    - deployed source read for CErc20Delegate@0xbb93c7f3…(ethereum); indicators matched: initialize_without_modifier
    - 1 implementation(s) behind a proxy are NOT verified on the explorer: implementation identity unresolved, score capped at 60
    - 1/1 live proxies read a zero ERC-7201 Initializable slot (inconclusive alone: older OZ versions store the flag elsewhere)
- **Preconditions PRESENT / UNKNOWN:** src::initialize_without_modifier, upgradeable_architecture, initializer_flag_unset, live_value_or_approvals / none
- **Guards searched / found:** initializer_modifier_present, upgrade_timelocked / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Simulated re-initialization reverts (kills the pair); Contract is non-upgradeable and holds no approvals
- **Where to start:** Read the initialization slot on every live proxy/facet and simulate re-initialization from an unprivileged address; it must revert.
- **Evidence:** `protocols/deep_screened.jsonl#b.protocol|UPGRADE-INITIALIZER-REACHABLE-LIVE`, `protocols/onchain_probes.json#b.protocol`
- **Disclosure:** https://app.bprotocol.org/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.bprotocol.org/technical-documentation/bug-bounty

### 28. Wing Finance  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 28
- **Protocol:** Wing Finance (`wing-finance`) · Lending · Ontology, Ethereum, Binance, OKExChain, OntologyEVM
- **DefiLlama:** https://defillama.com/protocol/wing-finance
- **PRIORITY 43.83**  =  LIKELIHOOD 51.57 × ACTIONABILITY 85.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 25.17/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $5,173,532 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `unverified_implementation` — raises likelihood, measured lift ×2.062 (weight +0.72)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - 6 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** prior_version_still_callable, still_holds_value_or_authority / unmaintained_or_differing_code_path, not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **one externally-owned account** (`EOA_SINGLE_KEY`) — a code fix here does not remove that exposure, and it is the cheaper thing to raise first
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#wing-finance|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#wing-finance`
- **Disclosure:** https://wing.finance · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.wing.finance/#audits

### 29. Mountain Protocol  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking B — likelihood, ignoring actionability):** 29
- **Protocol:** Mountain Protocol (`mountain-protocol`) · RWA · Ethereum, zkSync Era, Arbitrum, Base, Optimism, Polygon
- **DefiLlama:** https://defillama.com/protocol/mountain-protocol
- **PRIORITY 43.77**  =  LIKELIHOOD 51.5 × ACTIONABILITY 85.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 14.6/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,402,690 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 84.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source (`USDM` @ 0x7f2f92c4…(ethereum)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for USDM@0x7f2f92c4…(ethereum); indicators matched: unsafe_cross_sign_cast
- **Preconditions PRESENT / UNKNOWN:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** safecast_used / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#mountain-protocol|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#mountain-protocol`
- **Disclosure:** https://mountainprotocol.com · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/mountainprotocol/audits/blob/main/OpenZeppelin%20Mountain%20Protocol%20USDM%20-%20Audit%20Report%20Jun%202023.pdf

### 30. Steer Protocol  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 30
- **Protocol:** Steer Protocol (`steer-protocol`) · Liquidity Manager · Binance, Katana, Flare, Base, Ethereum, Polygon …
- **DefiLlama:** https://defillama.com/protocol/steer-protocol
- **PRIORITY 30.9**  =  LIKELIHOOD 51.5 × ACTIONABILITY 60.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 25.1/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $20,439,704 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - Conditions: `MULTICHAIN_VERSION_DRIFT`
    - condition MULTICHAIN_VERSION_DRIFT (PRIORITY): Deployed across many chains, where per-chain deployments drift and the least-watched chain sets the risk.
    - 2 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** prior_version_still_callable, still_holds_value_or_authority, not_paused / unmaintained_or_differing_code_path
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#steer-protocol|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#steer-protocol`
- **Disclosure:** https://app.steer.finance · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.steer.finance/audit-reports

### 31. LendFlare  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking B — likelihood, ignoring actionability):** 31
- **Protocol:** LendFlare (`lendflare`) · Lending · Ethereum
- **DefiLlama:** https://defillama.com/protocol/lendflare
- **PRIORITY 43.75**  =  LIKELIHOOD 51.47 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 19.57/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,171,712 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`VirtualBalanceWrapper` @ 0x10A377BA…(ethereum), `VirtualBalanceWrapper` @ 0x2FbE41e4…(ethereum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for VirtualBalanceWrapper@0x10A377BA…(ethereum), VirtualBalanceWrapper@0x2FbE41e4…(ethereum); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **one externally-owned account** (`EOA_SINGLE_KEY`) — a code fix here does not remove that exposure, and it is the cheaper thing to raise first
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#lendflare|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#lendflare`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://www.certik.com/projects/lend-flare

### 35. Unitus  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking B — likelihood, ignoring actionability):** 35
- **Protocol:** Unitus (`unitus`) · Lending · Conflux, Ethereum, Binance, Arbitrum, Polygon, Optimism …
- **DefiLlama:** https://defillama.com/protocol/unitus
- **PRIORITY 43.63**  =  LIKELIHOOD 51.33 × ACTIONABILITY 85.0%
    - likelihood = family evidence 30.0/50 (MATCH 60 × evidence weight 1.0) + learned attack surface 21.33/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $6,337,750 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 60 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `unverified_implementation` — raises likelihood, measured lift ×2.062 (weight +0.72)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
- **Broken invariant tested:** After deployment, no caller may (re)establish ownership, admin, or implementation wiring. Initialization state must be provably consumed.
    - Deployed source (`CErc20Immutable` @ 0x004c0908…(ethereum)): prerequisites matched: initialize_without_modifier; no guard found
    - deployed source read for CErc20Immutable@0x004c0908…(ethereum); indicators matched: initialize_without_modifier
    - 1 implementation(s) behind a proxy are NOT verified on the explorer: implementation identity unresolved, score capped at 60
    - 1/1 live proxies read a zero ERC-7201 Initializable slot (inconclusive alone: older OZ versions store the flag elsewhere)
- **Preconditions PRESENT / UNKNOWN:** src::initialize_without_modifier, upgradeable_architecture, initializer_flag_unset, live_value_or_approvals / none
- **Guards searched / found:** initializer_modifier_present, upgrade_timelocked / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Simulated re-initialization reverts (kills the pair); Contract is non-upgradeable and holds no approvals
- **Where to start:** Read the initialization slot on every live proxy/facet and simulate re-initialization from an unprivileged address; it must revert.
- **Evidence:** `protocols/deep_screened.jsonl#unitus|UPGRADE-INITIALIZER-REACHABLE-LIVE`, `protocols/onchain_probes.json#unitus`
- **Disclosure:** https://unitus.finance/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/dforce-network/documents/tree/master/audit_report/Lending

### 37. ICHI  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 37
- **Protocol:** ICHI (`ichi`) · Liquidity Manager · Hedera, Base, Ethereum, Binance, Sonic, Flare …
- **DefiLlama:** https://defillama.com/protocol/ichi
- **PRIORITY 43.58**  =  LIKELIHOOD 51.27 × ACTIONABILITY 85.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 24.87/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $7,949,093 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `unverified_implementation` — raises likelihood, measured lift ×2.062 (weight +0.72)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - Conditions: `MULTICHAIN_VERSION_DRIFT`
    - condition MULTICHAIN_VERSION_DRIFT (PRIORITY): Deployed across many chains, where per-chain deployments drift and the least-watched chain sets the risk.
    - 3 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** prior_version_still_callable, still_holds_value_or_authority / unmaintained_or_differing_code_path, not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#ichi|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#ichi`
- **Disclosure:** https://www.ichi.org · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.ichi.org/home/technical-resources/audits

### 38. TAU Labs  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 38
- **Protocol:** TAU Labs (`tau-labs`) · Risk Curators · Base, Ethereum, Plasma, Flow
- **DefiLlama:** https://defillama.com/protocol/tau-labs
- **PRIORITY 43.55**  =  LIKELIHOOD 51.23 × ACTIONABILITY 85.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 14.33/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $8,297,367 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`GnosisSafeProxy` @ 0x0000aeB7…(base), `PlasmaVault` @ 0x01a6ff6e…(base)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for GnosisSafeProxy@0x0000aeB7…(base), PlasmaVault@0x01a6ff6e…(base); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#tau-labs|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#tau-labs`
- **Disclosure:** https://www.628labs.xyz/ · no audit link listed

### 39. Spectra MetaVaults Outside V2  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 39
- **Protocol:** Spectra MetaVaults Outside V2 (`spectra-metavaults-outside-v2`) · Onchain Capital Allocator · Base, Flare, Katana, Avalanche, Ethereum, Arbitrum
- **DefiLlama:** https://defillama.com/protocol/spectra-metavaults-outside-v2
- **PRIORITY 43.55**  =  LIKELIHOOD 51.23 × ACTIONABILITY 85.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 14.33/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $3,562,036 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`MetavaultsRegistry` @ 0x16b28223…(arbitrum), `TransparentUpgradeableProxy` @ 0x2154a519…(arbitrum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for MetavaultsRegistry@0x16b28223…(arbitrum), TransparentUpgradeableProxy@0x2154a519…(arbitrum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#spectra-metavaults-outside-v2|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#spectra-metavaults-outside-v2`
- **Disclosure:** https://app.spectra.finance/metavaults · no audit link listed

### 42. Nomiswap  —  `ACC-QUOTE-STALE-ACROSS-OWN-SWAP`

- **Rank (Ranking B — likelihood, ignoring actionability):** 42
- **Protocol:** Nomiswap (`nomiswap`) · Dexs · Binance
- **DefiLlama:** https://defillama.com/protocol/nomiswap
- **PRIORITY 43.42**  =  LIKELIHOOD 51.08 × ACTIONABILITY 85.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 14.18/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,364,610 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A value used for minting, crediting or reward must be derived from what the protocol actually received, not from a quote taken before the protocol itself moved the market. Where the protocol's own action changes the price it just read, the value must be recomputed after the fact.
    - Deployed source (`NomiswapStableFactory` @ 0xC6B7ee49…(bsc), `NomiswapFactory` @ 0xd6715A8b…(bsc)): prerequisites matched: quote_then_own_swap; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): referral_reward_with_mint=no
    - deployed source read for NomiswapStableFactory@0xC6B7ee49…(bsc), NomiswapFactory@0xd6715A8b…(bsc); indicators matched: quote_then_own_swap
- **Preconditions PRESENT / UNKNOWN:** src::quote_then_own_swap, live_value_present, deployment_reachable_on_chain / src::quote_then_addliquidity
- **Guards searched / found:** lp_delta_measured, twap_or_feed_for_accounting / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** The minted amount is derived from the LP balance delta or from a TWAP (kills the pair); The protocol's swap is bounded so it cannot move reserves materially; Rewards settle in a later block against re-measured backing
- **Where to start:** On a fork, run the bonding path with a flash-funded swap sized to skew the pair, then assert that the minted or credited amount tracks the LP tokens actually received rather than the pre-swap quote.
- **Evidence:** `protocols/deep_screened.jsonl#nomiswap|ACC-QUOTE-STALE-ACROSS-OWN-SWAP`, `protocols/onchain_probes.json#nomiswap`
- **Disclosure:** https://nomiswap.io · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://www.certik.com/projects/nomiswap

### 43. Aave V1  —  `ORACLE-SPOT-THIN-LIQUIDITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 43
- **Protocol:** Aave V1 (`aave-v1`) · Lending · Ethereum
- **DefiLlama:** https://defillama.com/protocol/aave-v1
- **PRIORITY 43.41**  =  LIKELIHOOD 51.07 × ACTIONABILITY 85.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 14.17/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $7,651,606 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `version_sibling_legacy` — raises likelihood, measured lift ×1.699 (weight +0.53)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** Borrowing capacity, mint size, reward size or collateral value must not be derived from a price that a single actor can move within the manipulation window, and the value unlocked must never exceed the cost of moving that price.
    - Conditions: `SINGLE_PRIMARY_ORACLE_NO_CROSSCHECK`, `WRONG_LIQUIDITY_FLAG`
    - Deployed source (`InitializableAdminUpgradeabilityProxy` @ 0x1012cfF8…(ethereum), `InitializableAdminUpgradeabilityProxy` @ 0x7fc66500…(ethereum)): prerequisites matched: spot_without_twap; no guard found
    - deployed source read for InitializableAdminUpgradeabilityProxy@0x1012cfF8…(ethereum), InitializableAdminUpgradeabilityProxy@0x7fc66500…(ethereum); indicators matched: spot_without_twap
    - condition SINGLE_PRIMARY_ORACLE_NO_CROSSCHECK (PRIORITY): Exactly one declared oracle and no declared secondary, so no cross-source deviation bound is declared.
    - condition WRONG_LIQUIDITY_FLAG (PRIORITY): DefiLlama flags this protocol's liquidity figures as wrong, so depth-derived assumptions are unreliable.
- **Preconditions PRESENT / UNKNOWN:** src::spot_without_twap, value_decision_reads_configured_feed, live_positions_exposed / feed_selection_is_configuration
- **Guards searched / found:** twap_present, supply_cap_present, deviation_bound_vs_independent_source / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** All collateral priced by a deep aggregated feed with a deviation cap (kills the pair); Caps are set from measured venue depth and enforced on-chain; The action is sized from realised transfer amounts, so price is never an input
- **Where to start:** On a fork, execute a max-size flash-funded swap against every venue in the pricing path and assert that no value-bearing entrypoint changes its output beyond the configured deviation bound.
- **Evidence:** `protocols/deep_screened.jsonl#aave-v1|ORACLE-SPOT-THIN-LIQUIDITY`, `protocols/onchain_probes.json#aave-v1`
- **Disclosure:** https://aave.com · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://aave.com/security

### 44. Cronos zkEVM Bridge  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking B — likelihood, ignoring actionability):** 44
- **Protocol:** Cronos zkEVM Bridge (`cronos-zkevm-bridge`) · Canonical Bridge · Ethereum
- **DefiLlama:** https://defillama.com/protocol/cronos-zkevm-bridge
- **PRIORITY 30.64**  =  LIKELIHOOD 51.07 × ACTIONABILITY 60.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 14.17/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $20,070,907 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source (`L1NativeTokenVault` @ 0x2fc2a2db…(ethereum), `StakedZentry` @ 0xa694c051…(ethereum)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for L1NativeTokenVault@0x2fc2a2db…(ethereum), StakedZentry@0xa694c051…(ethereum); indicators matched: unsafe_cross_sign_cast
- **Preconditions PRESENT / UNKNOWN:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** safecast_used / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **one externally-owned account** (`EOA_SINGLE_KEY`) — a code fix here does not remove that exposure, and it is the cheaper thing to raise first
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#cronos-zkevm-bridge|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#cronos-zkevm-bridge`
- **Disclosure:** https://zkevm.cronos.org/ · no audit link listed

### 45. Asseto CASH+  —  `ACC-DUPLICATE-ID-ACCUMULATION`

- **Rank (Ranking B — likelihood, ignoring actionability):** 45
- **Protocol:** Asseto CASH+ (`asseto-cash+`) · RWA · Binance, Ethereum
- **DefiLlama:** https://defillama.com/protocol/asseto-cash+
- **PRIORITY 43.27**  =  LIKELIHOOD 50.9 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 19.0/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,501,710 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** An entitlement attached to an identifier may be counted at most once per period. A caller-supplied ID list must be deduplicated, or each ID's claim state consumed before the next read.
    - Deployed source (`SAmMMF` @ 0x22f70221…(bsc)): prerequisites matched: id_array_loop_without_dedup; no guard found
    - deployed source read for SAmMMF@0x22f70221…(bsc); indicators matched: id_array_loop_without_dedup
- **Preconditions PRESENT / UNKNOWN:** src::id_array_loop_without_dedup, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Consumed marker written inside the loop (kills the pair); IDs required strictly increasing
- **Where to start:** On a fork, call the batch function with one ID repeated k times; payout must equal the single-ID payout.
- **Evidence:** `protocols/deep_screened.jsonl#asseto-cash+|ACC-DUPLICATE-ID-ACCUMULATION`, `protocols/onchain_probes.json#asseto-cash+`
- **Disclosure:** https://asseto.finance/#invest · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://reale-assets.gitbook.io/reale/smart-contract-audit

### 46. PoolTogether V5  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 46
- **Protocol:** PoolTogether V5 (`pooltogether-v5`) · Yield Lottery · Base, Optimism, Ethereum, xDai, World Chain, Arbitrum …
- **DefiLlama:** https://defillama.com/protocol/pooltogether-v5
- **PRIORITY 43.22**  =  LIKELIHOOD 50.85 × ACTIONABILITY 85.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 13.95/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $5,567,621 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 79.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`Pool` @ 0x0cec1a91…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for Pool@0x0cec1a91…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#pooltogether-v5|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#pooltogether-v5`
- **Disclosure:** https://pooltogether.com/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.pooltogether.com/security/audits

### 48. Peapods Finance  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking B — likelihood, ignoring actionability):** 48
- **Protocol:** Peapods Finance (`peapods-finance`) · Yield · Ethereum, Base, Sonic, Arbitrum, Berachain, Mode
- **DefiLlama:** https://defillama.com/protocol/peapods-finance
- **PRIORITY 43.04**  =  LIKELIHOOD 50.63 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 18.73/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $2,030,459 · **Band:** `IN_BAND`
- **Previously hacked:** 2023-12-13 for $231,192 [Reentrancy]
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`PEAS` @ 0x02f92800…(ethereum), `IndexManager` @ 0x0Bb39ba2…(ethereum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for PEAS@0x02f92800…(ethereum), IndexManager@0x0Bb39ba2…(ethereum); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `EOA_SINGLE_KEY`; no ERC-1967 admin chain was proven
- **Prior art:** `KNOWN_ISSUE_DEPLOYMENT_STATUS_UNKNOWN` — DefiLlama's hacks dataset records 1 prior on-chain incident(s) on this protocol, most recently 2023-12-13 for $231,192 [Reentrancy]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#peapods-finance|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#peapods-finance`
- **Disclosure:** https://peapods.finance · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://sourcehat.com/audits/PeapodsFinance/

### 49. Yearn Finance  —  `SIG-VERIFIER-DEFEATABLE`

- **Rank (Ranking B — likelihood, ignoring actionability):** 49
- **Protocol:** Yearn Finance (`yearn-finance`) · Yield Aggregator · Ethereum, Katana, Optimism, Base, Polygon, Arbitrum …
- **DefiLlama:** https://defillama.com/protocol/yearn-finance
- **PRIORITY 2.53**  =  LIKELIHOOD 50.55 × ACTIONABILITY 5.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 13.65/50
    - actionability: far above the band: continuous professional coverage assumed
- **Value at risk:** $186,365,987 · **Band:** `ABOVE_BAND_KEPT_EXPLICIT_DANGER`
- **REPEAT VICTIM — 3 recorded hacks.** 2025-12-16 $300,000 [Donation Attack]; 2023-04-13 $11,539,000 [Oracle Misconfiguration]
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A verification routine must reject malformed, empty or zero-recovered signatures, and must never treat address(0) as a match.
    - Deployed source (`Yearn V3 Vault` @ 0x028ec733…(ethereum), `yVault` @ 0x03403154…(ethereum)): prerequisites matched: ecrecover_without_zero_check; no guard found
    - deployed source read for Yearn V3 Vault@0x028ec733…(ethereum), yVault@0x03403154…(ethereum); indicators matched: ecrecover_without_zero_check
- **Preconditions PRESENT / UNKNOWN:** src::ecrecover_without_zero_check, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** uses_oz_ecdsa / none in the reviewed path
- **Prior art:** `UNREMEDIATED_KNOWN_ISSUE` — DefiLlama's hacks dataset records 2 prior on-chain incident(s) on this protocol, most recently 2025-12-16 for $300,000 [Donation Attack]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** OZ ECDSA library in the deployed bytecode (kills the ecrecover-zero shape); Signer address immutable and non-zero
- **Where to start:** On a fork, submit r=0,s=0,v=27 and an empty signature to every signature-gated entrypoint; all must revert.
- **Evidence:** `protocols/deep_screened.jsonl#yearn-finance|SIG-VERIFIER-DEFEATABLE`, `protocols/onchain_probes.json#yearn-finance`
- **Disclosure:** https://yearn.fi/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/yearn/yearn-security/tree/master/audits

### 50. Kromatika  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking B — likelihood, ignoring actionability):** 50
- **Protocol:** Kromatika (`kromatika`) · Dexs · Optimism, Ethereum, Arbitrum, Polygon
- **DefiLlama:** https://defillama.com/protocol/kromatika
- **PRIORITY 42.78**  =  LIKELIHOOD 50.33 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 18.43/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,178,668 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`Kromatika` @ 0x3af33bef…(ethereum), `LimitOrderManagerV3` @ 0x3f5696c4…(ethereum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for Kromatika@0x3af33bef…(ethereum), LimitOrderManagerV3@0x3f5696c4…(ethereum); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#kromatika|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#kromatika`
- **Disclosure:** https://app.kromatika.finance/limitorder#/pool · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://skynet.certik.com/projects/kromatika

### 52. Unslashed  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking B — likelihood, ignoring actionability):** 52
- **Protocol:** Unslashed (`unslashed`) · Insurance · Ethereum
- **DefiLlama:** https://defillama.com/protocol/unslashed
- **PRIORITY 42.74**  =  LIKELIHOOD 50.28 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 18.38/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $3,596,677 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`VaultLib` @ 0x891dee04…(ethereum), `USF` @ 0xe0e05c43…(ethereum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for VaultLib@0x891dee04…(ethereum), USF@0xe0e05c43…(ethereum); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#unslashed|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#unslashed`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://documentation.unslashed.finance/risks-and-security/audits

### 54. Joe DEX  —  `ACC-QUOTE-STALE-ACROSS-OWN-SWAP`

- **Rank (Ranking B — likelihood, ignoring actionability):** 54
- **Protocol:** Joe DEX (`joe-dex`) · Dexs · Avalanche, Monad, Arbitrum, Binance
- **DefiLlama:** https://defillama.com/protocol/joe-dex
- **PRIORITY 42.52**  =  LIKELIHOOD 50.02 × ACTIONABILITY 85.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 13.12/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $9,610,102 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A value used for minting, crediting or reward must be derived from what the protocol actually received, not from a quote taken before the protocol itself moved the market. Where the protocol's own action changes the price it just read, the value must be recomputed after the fact.
    - Deployed source (`JoeFactory` @ 0xaE4EC990…(arbitrum)): prerequisites matched: quote_then_own_swap; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): referral_reward_with_mint=no
    - deployed source read for JoeFactory@0xaE4EC990…(arbitrum); indicators matched: quote_then_own_swap
- **Preconditions PRESENT / UNKNOWN:** src::quote_then_own_swap, live_value_present, deployment_reachable_on_chain / src::quote_then_addliquidity
- **Guards searched / found:** lp_delta_measured, twap_or_feed_for_accounting / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** The minted amount is derived from the LP balance delta or from a TWAP (kills the pair); The protocol's swap is bounded so it cannot move reserves materially; Rewards settle in a later block against re-measured backing
- **Where to start:** On a fork, run the bonding path with a flash-funded swap sized to skew the pair, then assert that the minted or credited amount tracks the LP tokens actually received rather than the pre-swap quote.
- **Evidence:** `protocols/deep_screened.jsonl#joe-dex|ACC-QUOTE-STALE-ACROSS-OWN-SWAP`, `protocols/onchain_probes.json#joe-dex`
- **Disclosure:** https://lfj.gg/avalanche · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.lfj.gg/audits

### 58. Stafi  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking B — likelihood, ignoring actionability):** 58
- **Protocol:** Stafi (`stafi`) · Liquid Staking · Ethereum, Solana, Binance, Cosmos, Stafi
- **DefiLlama:** https://defillama.com/protocol/stafi
- **PRIORITY 42.43**  =  LIKELIHOOD 49.92 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 18.02/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $3,579,497 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`Bridge` @ 0xef3A930e…(bsc)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for Bridge@0xef3A930e…(bsc); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#stafi|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#stafi`
- **Disclosure:** https://www.stafi.io/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/stafiprotocol/stafi-bootstrap/tree/master/audits

### 59. Orderly Bridge  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking B — likelihood, ignoring actionability):** 59
- **Protocol:** Orderly Bridge (`orderly-bridge`) · Bridge · Solana, Ethereum, Arbitrum, Binance, Berachain, Avalanche …
- **DefiLlama:** https://defillama.com/protocol/orderly-bridge
- **PRIORITY 29.95**  =  LIKELIHOOD 49.92 × ACTIONABILITY 60.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 18.02/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $28,007,293 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`TransparentUpgradeableProxy` @ 0x816f7224…(ethereum), `OrderToken` @ 0xabd4c63d…(ethereum)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for TransparentUpgradeableProxy@0x816f7224…(ethereum), OrderToken@0xabd4c63d…(ethereum); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#orderly-bridge|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#orderly-bridge`
- **Disclosure:** https://orderly.network · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/OrderlyNetwork/Audits
