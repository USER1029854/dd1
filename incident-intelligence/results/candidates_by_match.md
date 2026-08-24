# Candidates — Ranking C — mechanism match only

> **Discovery stage.** This file asserts no defect in any protocol named below. Each entry is a *review candidate*: named evidence matches a family's prerequisites, named evidence is unknown, and a named guard would falsify it. Verify on a local or pinned fork before concluding anything.

**Scoring is now validated, not asserted.** Attack-surface weights were fitted on 2022-24 hacks and tested against 2025-26 hacks: 95 protocols unseen during fitting, median victim landing at the **78.6th percentile**, **58%** of future victims in the model's top quartile — a **×2.32 lift** over chance.

**Likelihood and actionability are kept apart.** Bigger protocols are *more* likely to be attacked (`tvl_over_5m` carries lift ×1.75) and *less* actionable for an independent reviewer. Folding those together is what produced earlier rankings full of protocols you cannot help. PRIORITY multiplies them explicitly so you can see both halves.

**Exposure age beat every other addition, and it contradicts the obvious intuition.** Protocols under a year old carry lift ×1.87; protocols over three years old carry ×0.33. It is not the abandoned deployments that get hit — it is the new ones. Ablation attributes the whole out-of-sample gain to this one group (×2.19 → ×2.32).

**Custody posture was measured and then deliberately dropped from the score.** A single-key upgrade authority does not predict a code defect (measured ×0.98 over the full window; adding it moved out-of-sample lift ×2.19 → ×2.15, i.e. slightly worse). That is the expected answer, since key compromise is an excluded root cause here — so it is reported on its own in `results/upgrade_authority_exposure.md`, where 23 protocols holding $56.4M have an ERC-1967 upgrade authority terminating in a single key. Often the cheapest thing on this whole list to fix.

**A finding that overturned the earlier model:** measured against survivors only, neglect looked protective. It is not — 62.5% of victims that fell below $50k had no audit, versus 20.9% of those still listed. The population was censored by the very outcome being predicted. Weights are now fitted against the full listed universe.

### 1. Arcade.xyz  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking C — mechanism match only):** 1
- **Protocol:** Arcade.xyz (`arcade.xyz`) · NFT Lending · Ethereum
- **DefiLlama:** https://defillama.com/protocol/arcade.xyz
- **PRIORITY 57.25**  =  LIKELIHOOD 57.25 × ACTIONABILITY 100.0%
    - likelihood = family evidence 42.5/50 (MATCH 85.0 × evidence weight 1.0) + learned attack surface 14.75/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $210,561 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 85.0 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** After deployment, no caller may (re)establish ownership, admin, or implementation wiring. Initialization state must be provably consumed.
    - Deployed source (`UniswapV2Pair` @ 0x06af8C35…(ethereum), `VaultFactory` @ 0x26936366…(ethereum)): prerequisites matched: initialize_without_modifier; no guard found
    - deployed source read for UniswapV2Pair@0x06af8C35…(ethereum), VaultFactory@0x26936366…(ethereum); indicators matched: initialize_without_modifier
    - 1/1 live proxies read a zero ERC-7201 Initializable slot (inconclusive alone: older OZ versions store the flag elsewhere)
- **Preconditions PRESENT / UNKNOWN:** src::initialize_without_modifier, upgradeable_architecture, initializer_flag_unset, live_value_or_approvals / none
- **Guards searched / found:** initializer_modifier_present, upgrade_timelocked / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Simulated re-initialization reverts (kills the pair); Contract is non-upgradeable and holds no approvals
- **Where to start:** Read the initialization slot on every live proxy/facet and simulate re-initialization from an unprivileged address; it must revert.
- **Evidence:** `protocols/deep_screened.jsonl#arcade.xyz|UPGRADE-INITIALIZER-REACHABLE-LIVE`, `protocols/onchain_probes.json#arcade.xyz`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.arcade.xyz/docs/audit-reports

### 2. Kine Finance  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking C — mechanism match only):** 2
- **Protocol:** Kine Finance (`kine-finance`) · Yield · Ethereum, Binance, Polygon, Avalanche
- **DefiLlama:** https://defillama.com/protocol/kine-finance
- **PRIORITY 56.04**  =  LIKELIHOOD 65.93 × ACTIONABILITY 85.0%
    - likelihood = family evidence 42.5/50 (MATCH 85.0 × evidence weight 1.0) + learned attack surface 23.43/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,120,759 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 85.0 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** After deployment, no caller may (re)establish ownership, admin, or implementation wiring. Initialization state must be provably consumed.
    - Deployed source (`KUSDMinter` @ 0x5fbe4eb5…(ethereum), `Unitroller` @ 0xbb7d94a4…(ethereum)): prerequisites matched: initialize_without_modifier; no guard found
    - deployed source read for KUSDMinter@0x5fbe4eb5…(ethereum), Unitroller@0xbb7d94a4…(ethereum); indicators matched: initialize_without_modifier
    - 2/2 live proxies read a zero ERC-7201 Initializable slot (inconclusive alone: older OZ versions store the flag elsewhere)
- **Preconditions PRESENT / UNKNOWN:** src::initialize_without_modifier, upgradeable_architecture, initializer_flag_unset, live_value_or_approvals / none
- **Guards searched / found:** initializer_modifier_present, upgrade_timelocked / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Simulated re-initialization reverts (kills the pair); Contract is non-upgradeable and holds no approvals
- **Where to start:** Read the initialization slot on every live proxy/facet and simulate re-initialization from an unprivileged address; it must revert.
- **Evidence:** `protocols/deep_screened.jsonl#kine-finance|UPGRADE-INITIALIZER-REACHABLE-LIVE`, `protocols/onchain_probes.json#kine-finance`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.kine.io/audit/peckshield

### 3. Kokonut Swap  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking C — mechanism match only):** 3
- **Protocol:** Kokonut Swap (`kokonut-swap`) · Dexs · Klaytn, Base, Polygon zkEVM
- **DefiLlama:** https://defillama.com/protocol/kokonut-swap
- **PRIORITY 55.15**  =  LIKELIHOOD 55.15 × ACTIONABILITY 100.0%
    - likelihood = family evidence 42.5/50 (MATCH 85.0 × evidence weight 1.0) + learned attack surface 12.65/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $610,365 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 85.0 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** After deployment, no caller may (re)establish ownership, admin, or implementation wiring. Initialization state must be provably consumed.
    - Deployed source (`TransparentUpgradeableProxy` @ 0x03173F63…(base), `UniswapV2Factory` @ 0x4Cf1284d…(base)): prerequisites matched: initialize_without_modifier; no guard found
    - deployed source read for TransparentUpgradeableProxy@0x03173F63…(base), UniswapV2Factory@0x4Cf1284d…(base); indicators matched: initialize_without_modifier
    - 1/1 live proxies read a zero ERC-7201 Initializable slot (inconclusive alone: older OZ versions store the flag elsewhere)
    - 1 proxy/proxies expose a non-zero owner()
- **Preconditions PRESENT / UNKNOWN:** src::initialize_without_modifier, upgradeable_architecture, initializer_flag_unset, live_value_or_approvals / none
- **Guards searched / found:** initializer_modifier_present, upgrade_timelocked / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Simulated re-initialization reverts (kills the pair); Contract is non-upgradeable and holds no approvals
- **Where to start:** Read the initialization slot on every live proxy/facet and simulate re-initialization from an unprivileged address; it must revert.
- **Evidence:** `protocols/deep_screened.jsonl#kokonut-swap|UPGRADE-INITIALIZER-REACHABLE-LIVE`, `protocols/onchain_probes.json#kokonut-swap`
- **Disclosure:** https://kokonutswap.finance · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://drive.google.com/file/d/1I0HnU8Rs88HHqBC6Y3aUcEKTPZfVTAZD/view

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

### 5. TermFinance Vaults  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking C — mechanism match only):** 5
- **Protocol:** TermFinance Vaults (`termfinance-vaults`) · Yield · Ethereum, Binance, Avalanche, Plasma, Arbitrum, Base
- **DefiLlama:** https://defillama.com/protocol/termfinance-vaults
- **PRIORITY 33.19**  =  LIKELIHOOD 55.32 × ACTIONABILITY 60.0%
    - likelihood = family evidence 42.5/50 (MATCH 85.0 × evidence weight 1.0) + learned attack surface 12.82/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $12,450,703 · **Band:** `IN_BAND`
- **Previously hacked:** 2026-08-23 for $8,500,000 [Malicious Proposal]
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 85.0 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
- **Broken invariant tested:** After deployment, no caller may (re)establish ownership, admin, or implementation wiring. Initialization state must be provably consumed.
    - Deployed source (`Strategy` @ 0x000ecfd7…(ethereum), `TokenizedStrategy` @ 0xbb51273d…(ethereum)): prerequisites matched: initialize_without_modifier; no guard found
    - deployed source read for Strategy@0x000ecfd7…(ethereum), TokenizedStrategy@0xbb51273d…(ethereum); indicators matched: initialize_without_modifier
    - 1/1 live proxies read a zero ERC-7201 Initializable slot (inconclusive alone: older OZ versions store the flag elsewhere)
- **Preconditions PRESENT / UNKNOWN:** src::initialize_without_modifier, upgradeable_architecture, initializer_flag_unset, live_value_or_approvals / none
- **Guards searched / found:** initializer_modifier_present, upgrade_timelocked / none in the reviewed path
- **Prior art:** `KNOWN_ISSUE_DEPLOYMENT_STATUS_UNKNOWN` — DefiLlama's hacks dataset records 1 prior on-chain incident(s) on this protocol, most recently 2026-08-23 for $8,500,000 [Malicious Proposal]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** Simulated re-initialization reverts (kills the pair); Contract is non-upgradeable and holds no approvals
- **Where to start:** Read the initialization slot on every live proxy/facet and simulate re-initialization from an unprivileged address; it must revert.
- **Evidence:** `protocols/deep_screened.jsonl#termfinance-vaults|UPGRADE-INITIALIZER-REACHABLE-LIVE`, `protocols/onchain_probes.json#termfinance-vaults`
- **Disclosure:** https://www.term.finance · no audit link listed

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

### 7. Cook Finance  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking C — mechanism match only):** 7
- **Protocol:** Cook Finance (`cook-finance`) · Indexes · Heco, Ethereum, Binance, Avalanche
- **DefiLlama:** https://defillama.com/protocol/cook-finance
- **PRIORITY 60.13**  =  LIKELIHOOD 60.13 × ACTIONABILITY 100.0%
    - likelihood = family evidence 37.5/50 (MATCH 75.0 × evidence weight 1.0) + learned attack surface 22.63/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $51,767 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 75.0 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** After deployment, no caller may (re)establish ownership, admin, or implementation wiring. Initialization state must be provably consumed.
    - Deployed source (`Oracle` @ 0x35bE7982…(ethereum), `CKToken` @ 0x43633bDb…(ethereum)): prerequisites matched: initialize_without_modifier; no guard found
    - deployed source read for Oracle@0x35bE7982…(ethereum), CKToken@0x43633bDb…(ethereum); indicators matched: initialize_without_modifier
    - 1/1 live proxies read a zero ERC-7201 Initializable slot (inconclusive alone: older OZ versions store the flag elsewhere)
- **Preconditions PRESENT / UNKNOWN:** src::initialize_without_modifier, upgradeable_architecture, initializer_flag_unset, live_value_or_approvals / none
- **Guards searched / found:** initializer_modifier_present, upgrade_timelocked / upgrade_timelocked
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **one externally-owned account** (`EOA_SINGLE_KEY`) — a code fix here does not remove that exposure, and it is the cheaper thing to raise first
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Simulated re-initialization reverts (kills the pair); Contract is non-upgradeable and holds no approvals
- **Where to start:** Read the initialization slot on every live proxy/facet and simulate re-initialization from an unprivileged address; it must revert.
- **Evidence:** `protocols/deep_screened.jsonl#cook-finance|UPGRADE-INITIALIZER-REACHABLE-LIVE`, `protocols/onchain_probes.json#cook-finance`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/CookFinance/cook-token/tree/master/audits

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

### 10. Sperax USD  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking C — mechanism match only):** 10
- **Protocol:** Sperax USD (`sperax-usd`) · Yield Aggregator · Arbitrum, Ethereum
- **DefiLlama:** https://defillama.com/protocol/sperax-usd
- **PRIORITY 61.08**  =  LIKELIHOOD 61.08 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 24.18/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $520,189 · **Band:** `IN_BAND`
- **Previously hacked:** 2023-02-04 for $250,000 [Unbacked Mint]
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
- **Broken invariant tested:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source (`veSPA` @ 0xd9595b93…(arbitrum), `SperaxTokenL2` @ 0x55755529…(arbitrum)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for veSPA@0xd9595b93…(arbitrum), SperaxTokenL2@0x55755529…(arbitrum); indicators matched: unsafe_cross_sign_cast
- **Preconditions PRESENT / UNKNOWN:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** safecast_used / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `KNOWN_ISSUE_DEPLOYMENT_STATUS_UNKNOWN` — DefiLlama's hacks dataset records 1 prior on-chain incident(s) on this protocol, most recently 2023-02-04 for $250,000 [Unbacked Mint]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#sperax-usd|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#sperax-usd`
- **Disclosure:** http://sperax.io · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/Sperax/Audit_Reports/blob/main/Sperax%20-%20USDs%20-%20Report%20(1).pdf, https://github.com/Sperax/Audit_Reports

### 11. Radiant V2  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking C — mechanism match only):** 11
- **Protocol:** Radiant V2 (`radiant-v2`) · Lending · Ethereum, Base, Arbitrum, Binance
- **DefiLlama:** https://defillama.com/protocol/radiant-v2
- **PRIORITY 59.7**  =  LIKELIHOOD 59.7 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 22.8/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $693,778 · **Band:** `IN_BAND`
- **REPEAT VICTIM — 2 recorded hacks.** 2024-01-02 $4,500,000 [Rounding Error]
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`RizLendingPool` @ 0xcdab9065…(base)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for RizLendingPool@0xcdab9065…(base); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Prior art:** `UNREMEDIATED_KNOWN_ISSUE` — DefiLlama's hacks dataset records 1 prior on-chain incident(s) on this protocol, most recently 2024-01-02 for $4,500,000 [Rounding Error]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#radiant-v2|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#radiant-v2`
- **Disclosure:** https://radiant.capital/#/markets · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://solidity.finance/audits/RadiantProtocol/

### 12. Revest Finance  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking C — mechanism match only):** 12
- **Protocol:** Revest Finance (`revest-finance`) · NFT Lending · Ethereum, Avalanche, Arbitrum, Polygon, Optimism, Fantom
- **DefiLlama:** https://defillama.com/protocol/revest-finance
- **PRIORITY 59.45**  =  LIKELIHOOD 59.45 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 22.55/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $107,916 · **Band:** `IN_BAND`
- **Previously hacked:** 2022-03-27 for $2,010,000 [Reentrancy]
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`RevestToken` @ 0x120a3879…(ethereum), `RevestA3_1` @ 0x209F3F77…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for RevestToken@0x120a3879…(ethereum), RevestA3_1@0x209F3F77…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `KNOWN_ISSUE_DEPLOYMENT_STATUS_UNKNOWN` — DefiLlama's hacks dataset records 1 prior on-chain incident(s) on this protocol, most recently 2022-03-27 for $2,010,000 [Reentrancy]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#revest-finance|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#revest-finance`
- **Disclosure:** https://revest.finance · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://solidity.finance/audits/Revest

### 13. Cytonic Airdrop Campaign  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking C — mechanism match only):** 13
- **Protocol:** Cytonic Airdrop Campaign (`cytonic-airdrop-campaign`) · Farm · Arbitrum, Base, Ethereum, Solana, Binance, Optimism …
- **DefiLlama:** https://defillama.com/protocol/cytonic-airdrop-campaign
- **PRIORITY 59.0**  =  LIKELIHOOD 59.0 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 22.1/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $169,482 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`BridgeDepositor` @ 0xce84c402…(arbitrum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for BridgeDepositor@0xce84c402…(arbitrum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#cytonic-airdrop-campaign|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#cytonic-airdrop-campaign`
- **Disclosure:** https://www.cytonic.com/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://file.cytonic.com/cytonic-fuzzland-report.pdf, https://file.cytonic.com/ZellicAuditReport.pdf

### 14. Bridge Mutual  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking C — mechanism match only):** 14
- **Protocol:** Bridge Mutual (`bridge-mutual`) · Insurance · Ethereum, Binance, Polygon
- **DefiLlama:** https://defillama.com/protocol/bridge-mutual
- **PRIORITY 58.05**  =  LIKELIHOOD 58.05 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 21.15/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $56,267 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`CapitalPool` @ 0x7783cf38…(bsc), `ClaimVoting` @ 0xcdb42c20…(bsc)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for CapitalPool@0x7783cf38…(bsc), ClaimVoting@0xcdb42c20…(bsc); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#bridge-mutual|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#bridge-mutual`
- **Disclosure:** https://www.bridgemutual.io · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://uploads-ssl.webflow.com/5fac3e348dbd5932a7578690/60da267d76850e5acfe4e4c2_Bridge%20Mutual%20SC%20Audit_%20ZOkyo.pdf, https://consensys.net/diligence/audits/2021/03/bridge-mutual/

### 15. Tetu Earn  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking C — mechanism match only):** 15
- **Protocol:** Tetu Earn (`tetu-earn`) · Yield · Polygon, Binance, Base, Ethereum, Fantom
- **DefiLlama:** https://defillama.com/protocol/tetu-earn
- **PRIORITY 58.03**  =  LIKELIHOOD 58.03 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 21.13/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $482,134 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`SwapLibrary` @ 0x6E4D8CAc…(bsc), `Bookkeeper` @ 0x43999b0a…(bsc)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for SwapLibrary@0x6E4D8CAc…(bsc), Bookkeeper@0x43999b0a…(bsc); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#tetu-earn|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#tetu-earn`
- **Disclosure:** http://tetu.io · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.tetu.io/tetu-io/security/audits

### 16. VaultCraft  —  `SIG-VERIFIER-DEFEATABLE`

- **Rank (Ranking C — mechanism match only):** 16
- **Protocol:** VaultCraft (`vaultcraft`) · Yield · Arbitrum, Ethereum, Polygon, Optimism, Base, Hemi …
- **DefiLlama:** https://defillama.com/protocol/vaultcraft
- **PRIORITY 57.73**  =  LIKELIHOOD 57.73 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 20.83/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $557,157 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A verification routine must reject malformed, empty or zero-recovered signatures, and must never treat address(0) as a match.
    - Deployed source (`StakingVault` @ 0x1F0a3bF1…(arbitrum), `StakingVaultFactory` @ 0x25172C73…(arbitrum)): prerequisites matched: ecrecover_without_zero_check; no guard found
    - deployed source read for StakingVault@0x1F0a3bF1…(arbitrum), StakingVaultFactory@0x25172C73…(arbitrum); indicators matched: ecrecover_without_zero_check
- **Preconditions PRESENT / UNKNOWN:** src::ecrecover_without_zero_check, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** uses_oz_ecdsa / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** OZ ECDSA library in the deployed bytecode (kills the ecrecover-zero shape); Signer address immutable and non-zero
- **Where to start:** On a fork, submit r=0,s=0,v=27 and an empty signature to every signature-gated entrypoint; all must revert.
- **Evidence:** `protocols/deep_screened.jsonl#vaultcraft|SIG-VERIFIER-DEFEATABLE`, `protocols/onchain_probes.json#vaultcraft`
- **Disclosure:** https://vaultcraft.io/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://1854965950-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FDCUWGERi18R9emmxWwO2%2Fuploads%2FgF4N9JVFD9kYVbxfqUOJ%2Fblocksec_popcorn_v1.0-signed.pdf?alt=media&token=452a1fd8-84e6-4131-badc-4cfbe2d4584e

### 17. Tarot  —  `ORACLE-SPOT-THIN-LIQUIDITY`

- **Rank (Ranking C — mechanism match only):** 17
- **Protocol:** Tarot (`tarot`) · Lending · Base, Optimism, Fantom, Binance, Linea, Avalanche …
- **DefiLlama:** https://defillama.com/protocol/tarot
- **PRIORITY 55.77**  =  LIKELIHOOD 55.77 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 18.87/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $583,969 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
- **Broken invariant tested:** Borrowing capacity, mint size, reward size or collateral value must not be derived from a price that a single actor can move within the manipulation window, and the value unlocked must never exceed the cost of moving that price.
    - Conditions: `PRICING_SURFACE_UNDECLARED`
    - Deployed source (`TarotSolidlyPriceOracleV2` @ 0x4B6daE04…(base)): prerequisites matched: spot_without_twap; no guard found
    - deployed source read for TarotSolidlyPriceOracleV2@0x4B6daE04…(base); indicators matched: spot_without_twap
    - condition PRICING_SURFACE_UNDECLARED (PRIORITY): A lending, CDP, derivatives or curation archetype with no oracle declared at all: the pricing path is unmapped.
    - only one oracle (or none) is declared in DefiLlama metadata; this is a prioritisation signal about disclosure, not evidence that no cross-source deviation bound exists in code
- **Preconditions PRESENT / UNKNOWN:** src::spot_without_twap, value_decision_reads_configured_feed, live_positions_exposed / feed_selection_is_configuration
- **Guards searched / found:** twap_present, supply_cap_present, deviation_bound_vs_independent_source / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** All collateral priced by a deep aggregated feed with a deviation cap (kills the pair); Caps are set from measured venue depth and enforced on-chain; The action is sized from realised transfer amounts, so price is never an input
- **Where to start:** On a fork, execute a max-size flash-funded swap against every venue in the pricing path and assert that no value-bearing entrypoint changes its output beyond the configured deviation bound.
- **Evidence:** `protocols/deep_screened.jsonl#tarot|ORACLE-SPOT-THIN-LIQUIDITY`, `protocols/onchain_probes.json#tarot`
- **Disclosure:** https://www.tarot.to · no audit link listed

### 18. EZMoney  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking C — mechanism match only):** 18
- **Protocol:** EZMoney (`ezmoney`) · Liquidity Manager · Base, Hyperliquid L1, Robinhood Chain, Binance, Arbitrum
- **DefiLlama:** https://defillama.com/protocol/ezmoney
- **PRIORITY 55.77**  =  LIKELIHOOD 55.77 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 18.87/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $64,000 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source (`NonfungiblePositionManager` @ 0x03a520b3…(base), `UniswapAdapter` @ 0x0e5d5ADE…(base)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for NonfungiblePositionManager@0x03a520b3…(base), UniswapAdapter@0x0e5d5ADE…(base); indicators matched: unsafe_cross_sign_cast
- **Preconditions PRESENT / UNKNOWN:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** safecast_used / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `TIMELOCK`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#ezmoney|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#ezmoney`
- **Disclosure:** https://ezmoney.finance · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.ezmanager.finance/audits

### 19. Pell Network  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking C — mechanism match only):** 19
- **Protocol:** Pell Network (`pell-network`) · Restaking · Bitlayer, BOB, Binance, CORE, BSquared, Merlin …
- **DefiLlama:** https://defillama.com/protocol/pell-network
- **PRIORITY 55.7**  =  LIKELIHOOD 55.7 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 18.8/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $224,044 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source (`StrategyManagerV2` @ 0x25B73751…(bsc), `StrategyBaseTVLLimits` @ 0x13c5f344…(bsc)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for StrategyManagerV2@0x25B73751…(bsc), StrategyBaseTVLLimits@0x13c5f344…(bsc); indicators matched: unsafe_cross_sign_cast
- **Preconditions PRESENT / UNKNOWN:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** safecast_used / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a Safe requiring several signatures** (`SAFE_M_OF_N`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#pell-network|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#pell-network`
- **Disclosure:** https://pell.network/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/0xPellNetwork/restaking-contracts/blob/main/audits/PeckShield-Audit-Report-PellNetwork-v1.0.pdf

### 20. xWin Finance  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking C — mechanism match only):** 20
- **Protocol:** xWin Finance (`xwin-finance`) · Indexes · Binance, Polygon, Arbitrum
- **DefiLlama:** https://defillama.com/protocol/xwin-finance
- **PRIORITY 55.57**  =  LIKELIHOOD 55.57 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 18.67/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $205,238 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`xWinBuddyChef` @ 0xda728cf7…(bsc), `xWinPriceMaster` @ 0xd712df1d…(bsc)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for xWinBuddyChef@0xda728cf7…(bsc), xWinPriceMaster@0xd712df1d…(bsc); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#xwin-finance|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#xwin-finance`
- **Disclosure:** https://xwin.finance · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://skynet.certik.com/projects/xwinfinance

### 21. Aavegotchi  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking C — mechanism match only):** 21
- **Protocol:** Aavegotchi (`aavegotchi`) · Gaming · Polygon, Ethereum
- **DefiLlama:** https://defillama.com/protocol/aavegotchi
- **PRIORITY 55.18**  =  LIKELIHOOD 55.18 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 18.28/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $207,363 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`MiniMeToken` @ 0x3F382DbD…(ethereum), `AppProxyUpgradeable` @ 0xFFE6280a…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for MiniMeToken@0x3F382DbD…(ethereum), AppProxyUpgradeable@0xFFE6280a…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#aavegotchi|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#aavegotchi`
- **Disclosure:** https://aavegotchi.com · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://www.certik.org/projects/aavegotchi

### 22. Bunni V2  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking C — mechanism match only):** 22
- **Protocol:** Bunni V2 (`bunni-v2`) · Dexs · Ethereum, Base, Unichain, Arbitrum, Binance
- **DefiLlama:** https://defillama.com/protocol/bunni-v2
- **PRIORITY 55.03**  =  LIKELIHOOD 55.03 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 18.13/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $213,436 · **Band:** `IN_BAND`
- **Previously hacked:** 2025-09-02 for $8,400,000 [Rounding Error]
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`BunniHub` @ 0x00000000…(ethereum), `BunniHub` @ 0x000000dc…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for BunniHub@0x00000000…(ethereum), BunniHub@0x000000dc…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `KNOWN_ISSUE_DEPLOYMENT_STATUS_UNKNOWN` — DefiLlama's hacks dataset records 1 prior on-chain incident(s) on this protocol, most recently 2025-09-02 for $8,400,000 [Rounding Error]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#bunni-v2|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#bunni-v2`
- **Disclosure:** https://bunni.xyz/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.bunni.xyz/docs/v2/audits/

### 23. BiFi  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking C — mechanism match only):** 23
- **Protocol:** BiFi (`bifi`) · Lending · Bifrost Network, Ethereum, Binance, Klaytn, Avalanche
- **DefiLlama:** https://defillama.com/protocol/bifi
- **PRIORITY 54.76**  =  LIKELIHOOD 64.42 × ACTIONABILITY 85.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 27.52/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $4,905,718 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`ERC20` @ 0x0c7D5ae0…(ethereum), `tokenProxy` @ 0x12864769…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for ERC20@0x0c7D5ae0…(ethereum), tokenProxy@0x12864769…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#bifi|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#bifi`
- **Disclosure:** https://bifi.finance/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/bifrost-platform/BiFi-X/blob/main/docs/bifrost_bifix_audit.pdf, https://github.com/bifrost-platform/BIFI/blob/master/docs/ENG/(ENG)_BiFi_BIFROST_Extension_Theori.pdf

### 24. Impermax V2  —  `ORACLE-SPOT-THIN-LIQUIDITY`

- **Rank (Ranking C — mechanism match only):** 24
- **Protocol:** Impermax V2 (`impermax-v2`) · Lending · Polygon, Ethereum, Base, Avalanche, Optimism, Arbitrum …
- **DefiLlama:** https://defillama.com/protocol/impermax-v2
- **PRIORITY 54.75**  =  LIKELIHOOD 54.75 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 17.85/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $596,796 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `version_sibling_legacy` — raises likelihood, measured lift ×1.699 (weight +0.53)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Borrowing capacity, mint size, reward size or collateral value must not be derived from a price that a single actor can move within the manipulation window, and the value unlocked must never exceed the cost of moving that price.
    - Conditions: `SINGLE_PRIMARY_ORACLE_NO_CROSSCHECK`
    - Deployed source (`UniswapV2Pair` @ 0x08650bb9…(ethereum)): prerequisites matched: spot_without_twap; no guard found
    - deployed source read for UniswapV2Pair@0x08650bb9…(ethereum); indicators matched: spot_without_twap
    - condition SINGLE_PRIMARY_ORACLE_NO_CROSSCHECK (PRIORITY): Exactly one declared oracle and no declared secondary, so no cross-source deviation bound is declared.
    - only one oracle (or none) is declared in DefiLlama metadata; this is a prioritisation signal about disclosure, not evidence that no cross-source deviation bound exists in code
- **Preconditions PRESENT / UNKNOWN:** src::spot_without_twap, value_decision_reads_configured_feed, live_positions_exposed / feed_selection_is_configuration
- **Guards searched / found:** twap_present, supply_cap_present, deviation_bound_vs_independent_source / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** All collateral priced by a deep aggregated feed with a deviation cap (kills the pair); Caps are set from measured venue depth and enforced on-chain; The action is sized from realised transfer amounts, so price is never an input
- **Where to start:** On a fork, execute a max-size flash-funded swap against every venue in the pricing path and assert that no value-bearing entrypoint changes its output beyond the configured deviation bound.
- **Evidence:** `protocols/deep_screened.jsonl#impermax-v2|ORACLE-SPOT-THIN-LIQUIDITY`, `protocols/onchain_probes.json#impermax-v2`
- **Disclosure:** https://impermax.finance/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/Impermax-Finance/impermax-x-uniswapv2-core/tree/main/audit

### 25. Bunny  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking C — mechanism match only):** 25
- **Protocol:** Bunny (`bunny`) · Yield · Binance, Polygon
- **DefiLlama:** https://defillama.com/protocol/bunny
- **PRIORITY 54.36**  =  LIKELIHOOD 63.95 × ACTIONABILITY 85.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 27.05/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $3,597,277 · **Band:** `IN_BAND`
- **REPEAT VICTIM — 2 recorded hacks.** 
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`VaultFlipToFlipLegacy` @ 0x13817980…(bsc), `VaultVenus` @ 0x5ccc0bcb…(bsc)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for VaultFlipToFlipLegacy@0x13817980…(bsc), VaultVenus@0x5ccc0bcb…(bsc); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#bunny|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#bunny`
- **Disclosure:** https://pancakebunny.finance/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/PancakeBunny-finance/Bunny/blob/main/audits/%5BHAECHI%20AUDIT%5D%20PancakeBunny%20Smart%20Contract%20Audit%20Report%20ver%202.0.pdf

### 26. GrizzlyFi Hives  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking C — mechanism match only):** 26
- **Protocol:** GrizzlyFi Hives (`grizzlyfi-hives`) · Yield · Binance
- **DefiLlama:** https://defillama.com/protocol/grizzlyfi-hives
- **PRIORITY 54.22**  =  LIKELIHOOD 54.22 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 17.32/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $522,590 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`BiswapGrizzly` @ 0x787158bd…(bsc), `Pair` @ 0x075e794f…(bsc)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for BiswapGrizzly@0x787158bd…(bsc), Pair@0x075e794f…(bsc); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a Safe requiring several signatures** (`SAFE_M_OF_N`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#grizzlyfi-hives|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#grizzlyfi-hives`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.grizzly.fi/audits#v1-audits

### 27. Wombex Finance  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking C — mechanism match only):** 27
- **Protocol:** Wombex Finance (`wombex-finance`) · Yield · Binance, Arbitrum
- **DefiLlama:** https://defillama.com/protocol/wombex-finance
- **PRIORITY 53.9**  =  LIKELIHOOD 53.9 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 17.0/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $479,094 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`VeWom` @ 0xa31ed019…(bsc), `BoostedMasterWombat` @ 0x26d67a2d…(bsc)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for VeWom@0xa31ed019…(bsc), BoostedMasterWombat@0x26d67a2d…(bsc); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a timelock with a real delay** (`TIMELOCK`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#wombex-finance|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#wombex-finance`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/wombex-finance/wombex-contracts/tree/main/audits

### 28. Accumulated Finance Liquid Staking  —  `SIG-VERIFIER-DEFEATABLE`

- **Rank (Ranking C — mechanism match only):** 28
- **Protocol:** Accumulated Finance Liquid Staking (`accumulated-finance-liquid-staking`) · Liquid Staking · Sapphire, Bitkub, ZetaChain, Coti, Manta, Velas …
- **DefiLlama:** https://defillama.com/protocol/accumulated-finance-liquid-staking
- **PRIORITY 53.65**  =  LIKELIHOOD 53.65 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 16.75/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $622,677 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
- **Broken invariant tested:** A verification routine must reject malformed, empty or zero-recovered signatures, and must never treat address(0) as a match.
    - Deployed source (`wstVLX` @ 0x7AC168c8…(bsc), `stVLX` @ 0xcba2aeEc…(bsc)): prerequisites matched: ecrecover_without_zero_check; no guard found
    - deployed source read for wstVLX@0x7AC168c8…(bsc), stVLX@0xcba2aeEc…(bsc); indicators matched: ecrecover_without_zero_check
- **Preconditions PRESENT / UNKNOWN:** src::ecrecover_without_zero_check, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** uses_oz_ecdsa / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `EOA_SINGLE_KEY`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** OZ ECDSA library in the deployed bytecode (kills the ecrecover-zero shape); Signer address immutable and non-zero
- **Where to start:** On a fork, submit r=0,s=0,v=27 and an empty signature to every signature-gated entrypoint; all must revert.
- **Evidence:** `protocols/deep_screened.jsonl#accumulated-finance-liquid-staking|SIG-VERIFIER-DEFEATABLE`, `protocols/onchain_probes.json#accumulated-finance-liquid-staking`
- **Disclosure:** https://accumulated.finance/stake · no audit link listed

### 29. Stabull Finance  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking C — mechanism match only):** 29
- **Protocol:** Stabull Finance (`stabull-finance`) · Dexs · Base, Polygon, Ethereum
- **DefiLlama:** https://defillama.com/protocol/stabull-finance
- **PRIORITY 53.35**  =  LIKELIHOOD 53.35 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 16.45/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $58,208 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source (`Curves` @ 0x2e9E34b5…(base)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for Curves@0x2e9E34b5…(base); indicators matched: unsafe_cross_sign_cast
- **Preconditions PRESENT / UNKNOWN:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** safecast_used / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#stabull-finance|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#stabull-finance`
- **Disclosure:** https://stabull.finance · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.stabull.finance/ecosystem/audits

### 30. YieldWolf  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking C — mechanism match only):** 30
- **Protocol:** YieldWolf (`yieldwolf`) · Yield · Avalanche, Binance, Cronos, Fantom, Polygon, Celo …
- **DefiLlama:** https://defillama.com/protocol/yieldwolf
- **PRIORITY 53.12**  =  LIKELIHOOD 53.12 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 16.22/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $62,846 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`ACMasterChef` @ 0xBF65023B…(bsc), `YieldWolf` @ 0xD3aB90CE…(bsc)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for ACMasterChef@0xBF65023B…(bsc), YieldWolf@0xD3aB90CE…(bsc); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#yieldwolf|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#yieldwolf`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://paladinsec.co/projects/yieldwolf

### 31. Cakepie  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking C — mechanism match only):** 31
- **Protocol:** Cakepie (`cakepie`) · Yield · Binance
- **DefiLlama:** https://defillama.com/protocol/cakepie
- **PRIORITY 52.88**  =  LIKELIHOOD 52.88 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 15.98/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $237,912 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`CakeToken` @ 0x0E09FaBB…(bsc), `mCakeSV` @ 0x4e2d40af…(bsc)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for CakeToken@0x0E09FaBB…(bsc), mCakeSV@0x4e2d40af…(bsc); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#cakepie|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#cakepie`
- **Disclosure:** https://www.pancake.magpiexyz.io/stake · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/peckshield/publications/blob/master/audit_reports/PeckShield-Audit-Report-Cakepie-v1.0.pdf, https://github.com/blocksecteam/audit-reports/blob/main/solidity/blocksec_cakepie_v1.0-signed.pdf

### 32. Shift Protocol  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking C — mechanism match only):** 32
- **Protocol:** Shift Protocol (`shift-protocol`) · Onchain Capital Allocator · Arbitrum, Base, Ethereum
- **DefiLlama:** https://defillama.com/protocol/shift-protocol
- **PRIORITY 52.6**  =  LIKELIHOOD 52.6 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 15.7/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $834,205 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`ShiftVault` @ 0x6d7C897c…(arbitrum), `ShiftVault` @ 0x7174f0bD…(arbitrum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for ShiftVault@0x6d7C897c…(arbitrum), ShiftVault@0x7174f0bD…(arbitrum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#shift-protocol|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#shift-protocol`
- **Disclosure:** https://shiftprotocol.xyz · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/SHIFT-NebulaLabs/shift-contracts/blob/main/audits/shift-sbsecurity-audit-2025.pdf

### 33. FinNexus  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking C — mechanism match only):** 33
- **Protocol:** FinNexus (`finnexus`) · Options · Ethereum, Binance, Wanchain
- **DefiLlama:** https://defillama.com/protocol/finnexus
- **PRIORITY 52.58**  =  LIKELIHOOD 52.58 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 15.68/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $232,179 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `zCurve` @ 0x00000000…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), zCurve@0x00000000…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#finnexus|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#finnexus`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/Phoenix-Finance/Pdfs/blob/master/PeckShield-Audit-FinnexusOptionsV1.0.pdf

### 34. Goldsand by InshAllah  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking C — mechanism match only):** 34
- **Protocol:** Goldsand by InshAllah (`goldsand-by-inshallah`) · Liquid Staking · Ethereum
- **DefiLlama:** https://defillama.com/protocol/goldsand-by-inshallah
- **PRIORITY 52.58**  =  LIKELIHOOD 52.58 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 15.68/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $337,796 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source (`WithdrawalVault` @ 0x605aac39…(ethereum), `Goldsand` @ 0xf68b3b27…(ethereum)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for WithdrawalVault@0x605aac39…(ethereum), Goldsand@0xf68b3b27…(ethereum); indicators matched: unsafe_cross_sign_cast
- **Preconditions PRESENT / UNKNOWN:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** safecast_used / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#goldsand-by-inshallah|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#goldsand-by-inshallah`
- **Disclosure:** https://goldsand.fi/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/inshallah-network/goldsand-v1/blob/master/audit/spearbit.pdf

### 35. PoolTogether V4  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking C — mechanism match only):** 35
- **Protocol:** PoolTogether V4 (`pooltogether-v4`) · Yield Lottery · Polygon, Optimism, Ethereum, Avalanche
- **DefiLlama:** https://defillama.com/protocol/pooltogether-v4
- **PRIORITY 52.58**  =  LIKELIHOOD 52.58 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 15.68/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $738,116 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 79.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `version_sibling_legacy` — raises likelihood, measured lift ×1.699 (weight +0.53)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`Pool` @ 0x0cec1a91…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for Pool@0x0cec1a91…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#pooltogether-v4|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#pooltogether-v4`
- **Disclosure:** https://pooltogether.com/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.pooltogether.com/security/audits

### 36. StoneDefi  —  `SIG-VERIFIER-DEFEATABLE`

- **Rank (Ranking C — mechanism match only):** 36
- **Protocol:** StoneDefi (`stonedefi`) · Yield Aggregator · Binance, Polygon, Avalanche, Ethereum
- **DefiLlama:** https://defillama.com/protocol/stonedefi
- **PRIORITY 52.45**  =  LIKELIHOOD 52.45 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 15.55/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $75,186 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A verification routine must reject malformed, empty or zero-recovered signatures, and must never treat address(0) as a match.
    - Deployed source (`PancakePair` @ 0x002e1655…(bsc), `Vyper_contract` @ 0x0F9F39F6…(bsc)): prerequisites matched: ecrecover_without_zero_check; no guard found
    - deployed source read for PancakePair@0x002e1655…(bsc), Vyper_contract@0x0F9F39F6…(bsc); indicators matched: ecrecover_without_zero_check
- **Preconditions PRESENT / UNKNOWN:** src::ecrecover_without_zero_check, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** uses_oz_ecdsa / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** OZ ECDSA library in the deployed bytecode (kills the ecrecover-zero shape); Signer address immutable and non-zero
- **Where to start:** On a fork, submit r=0,s=0,v=27 and an empty signature to every signature-gated entrypoint; all must revert.
- **Evidence:** `protocols/deep_screened.jsonl#stonedefi|SIG-VERIFIER-DEFEATABLE`, `protocols/onchain_probes.json#stonedefi`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://www.certik.com/projects/stonedefi

### 37. Ante Finance  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking C — mechanism match only):** 37
- **Protocol:** Ante Finance (`ante-finance`) · Insurance · Ethereum, Binance, Avalanche, Optimism, Aurora, Polygon …
- **DefiLlama:** https://defillama.com/protocol/ante-finance
- **PRIORITY 52.45**  =  LIKELIHOOD 52.45 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 15.55/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $492,714 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`AntePoolFactory` @ 0xb4FD0Ce1…(bsc)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for AntePoolFactory@0xb4FD0Ce1…(bsc); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#ante-finance|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#ante-finance`
- **Disclosure:** https://ante.finance · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.ante.finance/antev05/about/security#audits

### 38. Rubicon  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking C — mechanism match only):** 38
- **Protocol:** Rubicon (`rubicon`) · Dexs · Optimism, Base, Arbitrum, Ethereum
- **DefiLlama:** https://defillama.com/protocol/rubicon
- **PRIORITY 52.22**  =  LIKELIHOOD 52.22 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 15.32/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $247,341 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source (`OptimismMintableERC20` @ 0x0b3e3284…(base)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for OptimismMintableERC20@0x0b3e3284…(base); indicators matched: unsafe_cross_sign_cast
- **Preconditions PRESENT / UNKNOWN:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** safecast_used / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#rubicon|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#rubicon`
- **Disclosure:** https://app.rubicon.finance/swap · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.rubicon.finance/protocol/audits

### 39. Conic Finance  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking C — mechanism match only):** 39
- **Protocol:** Conic Finance (`conic-finance`) · Yield · Ethereum
- **DefiLlama:** https://defillama.com/protocol/conic-finance
- **PRIORITY 52.15**  =  LIKELIHOOD 52.15 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 15.25/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $63,068 · **Band:** `IN_BAND`
- **REPEAT VICTIM — 2 recorded hacks.** 2023-07-22 $300,000 [Spot Price Manipulation]; 2023-07-21 $3,300,000 [Read-Only Reentrancy]
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`Controller` @ 0x013A3Da6…(ethereum), `Controller` @ 0x2790EC47…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for Controller@0x013A3Da6…(ethereum), Controller@0x2790EC47…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Prior art:** `UNREMEDIATED_KNOWN_ISSUE` — DefiLlama's hacks dataset records 2 prior on-chain incident(s) on this protocol, most recently 2023-07-22 for $300,000 [Spot Price Manipulation]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#conic-finance|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#conic-finance`
- **Disclosure:** https://conic.finance · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://conic.finance/media/PeckShield-Audit-Report-ConicFinance.pdf

### 40. yAxis  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking C — mechanism match only):** 40
- **Protocol:** yAxis (`yaxis`) · Yield Aggregator · Ethereum
- **DefiLlama:** https://defillama.com/protocol/yaxis
- **PRIORITY 52.15**  =  LIKELIHOOD 52.15 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 15.25/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $524,050 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`VaultToken` @ 0x0C44393D…(ethereum), `YaxisToken` @ 0x0adA190c…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for VaultToken@0x0C44393D…(ethereum), YaxisToken@0x0adA190c…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `EOA_SINGLE_KEY`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#yaxis|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#yaxis`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/yaxis-project/yaxis-audit

### 41. PrismaLST  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking C — mechanism match only):** 41
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

### 42. Fungify  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking C — mechanism match only):** 42
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
    - Deployed source (`CEtherDelegate` @ 0x8f005bf2…(ethereum), `Unitroller` @ 0xf9c70750…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for CEtherDelegate@0x8f005bf2…(ethereum), Unitroller@0xf9c70750…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#fungify|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#fungify`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.fungify.it/governance/security

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

### 46. Idle  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking C — mechanism match only):** 46
- **Protocol:** Idle (`idle`) · Yield Aggregator · Ethereum, Polygon, Optimism, Polygon zkEVM, Arbitrum
- **DefiLlama:** https://defillama.com/protocol/idle
- **PRIORITY 51.62**  =  LIKELIHOOD 60.73 × ACTIONABILITY 85.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 23.83/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,567,483 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`IdleTokenV3` @ 0x12B98C62…(ethereum), `IdleCDOEpochVariant` @ 0xdd596250…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for IdleTokenV3@0x12B98C62…(ethereum), IdleCDOEpochVariant@0xdd596250…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#idle|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#idle`
- **Disclosure:** https://idle.finance · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.idle.finance/developers/security/audits

### 47. SOFA.org  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking C — mechanism match only):** 47
- **Protocol:** SOFA.org (`sofa.org`) · Options · Ethereum, Arbitrum, Binance, Polygon
- **DefiLlama:** https://defillama.com/protocol/sofa.org
- **PRIORITY 51.57**  =  LIKELIHOOD 60.67 × ACTIONABILITY 85.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 23.77/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,046,794 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`SmartTrendVault` @ 0x1d2faad4…(ethereum), `StRCH` @ 0x2B9aeA12…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for SmartTrendVault@0x1d2faad4…(ethereum), StRCH@0x2B9aeA12…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **one externally-owned account** (`EOA_SINGLE_KEY`) — a code fix here does not remove that exposure, and it is the cheaper thing to raise first
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#sofa.org|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#sofa.org`
- **Disclosure:** https://www.sofa.org · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/peckshield/publications/blob/master/audit_reports/PeckShield-Audit-Report-Sofa-v1.0.pdf, https://code4rena.com/reports/2024-05-sofa-pro-league

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

### 56. Abracadabra Spell  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking C — mechanism match only):** 56
- **Protocol:** Abracadabra Spell (`abracadabra-spell`) · CDP · Ethereum, Arbitrum, Binance, Avalanche, Blast, Fantom …
- **DefiLlama:** https://defillama.com/protocol/abracadabra-spell
- **PRIORITY 50.73**  =  LIKELIHOOD 59.68 × ACTIONABILITY 85.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 22.78/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $4,667,807 · **Band:** `IN_BAND`
- **REPEAT VICTIM — 3 recorded hacks.** 2025-10-04 $1,700,000 [Improper Access Control]; 2025-03-25 $13,000,000 [Liquidation Logic Flaw]; 2024-01-30 $6,500,000 [Rounding Error]
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`CauldronV4` @ 0x00380CB5…(ethereum), `CauldronV2Flat` @ 0x003d5a75…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for CauldronV4@0x00380CB5…(ethereum), CauldronV2Flat@0x003d5a75…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `UNREMEDIATED_KNOWN_ISSUE` — DefiLlama's hacks dataset records 3 prior on-chain incident(s) on this protocol, most recently 2025-10-04 for $1,700,000 [Improper Access Control]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#abracadabra-spell|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#abracadabra-spell`
- **Disclosure:** https://abracadabra.money/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://abracadabramoney.gitbook.io/learn/our-ecosystem/our-contracts

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
