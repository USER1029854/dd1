# Candidates — Ranking B — likelihood, ignoring actionability

> **Discovery stage.** This file asserts no defect in any protocol named below. Each entry is a *review candidate*: named evidence matches a family's prerequisites, named evidence is unknown, and a named guard would falsify it. Verify on a local or pinned fork before concluding anything.

**Scoring is now validated, not asserted.** Attack-surface weights were fitted on 2022-24 hacks and tested against 2025-26 hacks: 95 protocols unseen during fitting, median victim landing at the **78.6th percentile**, **58%** of future victims in the model's top quartile — a **×2.32 lift** over chance.

**Likelihood and actionability are kept apart.** Bigger protocols are *more* likely to be attacked (`tvl_over_5m` carries lift ×1.75) and *less* actionable for an independent reviewer. Folding those together is what produced earlier rankings full of protocols you cannot help. PRIORITY multiplies them explicitly so you can see both halves.

**Exposure age beat every other addition, and it contradicts the obvious intuition.** Protocols under a year old carry lift ×1.87; protocols over three years old carry ×0.33. It is not the abandoned deployments that get hit — it is the new ones. Ablation attributes the whole out-of-sample gain to this one group (×2.19 → ×2.32).

**Custody posture was measured and then deliberately dropped from the score.** A single-key upgrade authority does not predict a code defect (measured ×0.98 over the full window; adding it moved out-of-sample lift ×2.19 → ×2.15, i.e. slightly worse). That is the expected answer, since key compromise is an excluded root cause here — so it is reported on its own in `results/upgrade_authority_exposure.md`, where 23 protocols holding $56.4M have an ERC-1967 upgrade authority terminating in a single key. Often the cheapest thing on this whole list to fix.

**A finding that overturned the earlier model:** measured against survivors only, neglect looked protective. It is not — 62.5% of victims that fell below $50k had no audit, versus 20.9% of those still listed. The population was censored by the very outcome being predicted. Weights are now fitted against the full listed universe.

### 1. Kine Finance  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking B — likelihood, ignoring actionability):** 1
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

### 2. BiFi  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 2
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

### 3. Bunny  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 3
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

### 4. Gearbox  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking B — likelihood, ignoring actionability):** 4
- **Protocol:** Gearbox (`gearbox`) · Lending · Ethereum, Etherlink, Monad, Plasma, Hemi, Arbitrum …
- **DefiLlama:** https://defillama.com/protocol/gearbox
- **PRIORITY 37.12**  =  LIKELIHOOD 61.87 × ACTIONABILITY 60.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 24.97/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $21,850,472 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source (`MarketConfiguratorLegacy` @ 0x354fe9f4…(ethereum)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for MarketConfiguratorLegacy@0x354fe9f4…(ethereum); indicators matched: unsafe_cross_sign_cast
- **Preconditions PRESENT / UNKNOWN:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** safecast_used / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#gearbox|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#gearbox`
- **Disclosure:** https://gearbox.finance/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.gearbox.finance/risk-and-security/audits-bug-bounty

### 5. dForce Lending  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking B — likelihood, ignoring actionability):** 5
- **Protocol:** dForce Lending (`dforce-lending`) · Lending · Ethereum, Binance, Optimism, Arbitrum, Polygon, Conflux …
- **DefiLlama:** https://defillama.com/protocol/dforce-lending
- **PRIORITY 52.5**  =  LIKELIHOOD 61.77 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 29.87/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,027,387 · **Band:** `IN_BAND`
- **REPEAT VICTIM — 2 recorded hacks.** 2023-02-10 $3,650,000 [Read-Only Reentrancy]
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`DTokenProxy` @ 0x02285Aca…(ethereum), `DTokenProxy` @ 0x109917F7…(ethereum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for DTokenProxy@0x02285Aca…(ethereum), DTokenProxy@0x109917F7…(ethereum); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `UNREMEDIATED_KNOWN_ISSUE` — DefiLlama's hacks dataset records 1 prior on-chain incident(s) on this protocol, most recently 2023-02-10 for $3,650,000 [Read-Only Reentrancy]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#dforce-lending|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#dforce-lending`
- **Disclosure:** https://dforce.network/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/dforce-network/documents/tree/master/audit_report/Lending

### 6. Hundred Finance  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking B — likelihood, ignoring actionability):** 6
- **Protocol:** Hundred Finance (`hundred-finance`) · Lending · Arbitrum, Fantom, Polygon, xDai, Harmony, Optimism …
- **DefiLlama:** https://defillama.com/protocol/hundred-finance
- **PRIORITY 61.18**  =  LIKELIHOOD 61.18 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 29.28/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $73,585 · **Band:** `IN_BAND`
- **REPEAT VICTIM — 2 recorded hacks.** 2023-04-15 $7,400,000 [Donation Attack]; 2022-03-15 $6,200,000 [Reentrancy]
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`iTokenV2BLP` @ 0xaf23e036…(arbitrum), `AErc20Delegator` @ 0x03ef96f5…(arbitrum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for iTokenV2BLP@0xaf23e036…(arbitrum), AErc20Delegator@0x03ef96f5…(arbitrum); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `UNREMEDIATED_KNOWN_ISSUE` — DefiLlama's hacks dataset records 2 prior on-chain incident(s) on this protocol, most recently 2023-04-15 for $7,400,000 [Donation Attack]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#hundred-finance|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#hundred-finance`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/chainsulting/Smart-Contract-Security-Audits/blob/master/Percent%20Finance/02_Smart%20Contract%20Audit%20Percent%20Finance.pdf

### 7. Sperax USD  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking B — likelihood, ignoring actionability):** 7
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

### 8. Idle  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 8
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

### 9. SOFA.org  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 9
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

### 10. Badger DAO  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 10
- **Protocol:** Badger DAO (`badger-dao`) · Yield Aggregator · Ethereum, Arbitrum, Polygon, Binance, Fantom
- **DefiLlama:** https://defillama.com/protocol/badger-dao
- **PRIORITY 36.14**  =  LIKELIHOOD 60.23 × ACTIONABILITY 60.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 23.33/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $12,627,627 · **Band:** `IN_BAND`
- **REPEAT VICTIM — 2 recorded hacks.** 
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 79.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`MiniMeToken` @ 0x3472A5A7…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for MiniMeToken@0x3472A5A7…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#badger-dao|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#badger-dao`
- **Disclosure:** https://badger.com/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://badger.finance/wp-content/uploads/2021/01/HAECHI-AUDIT-BadgerDAO-Smart-Contract-Audit-Report-1.pdf, https://code4rena.com/contests/2022-06-badger-vested-aura-contest/

### 11. Cook Finance  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking B — likelihood, ignoring actionability):** 11
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

### 12. Curve DEX  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking B — likelihood, ignoring actionability):** 12
- **Protocol:** Curve DEX (`curve-dex`) · Dexs · Ethereum, Fraxtal, Base, Arbitrum, Etherlink, Monad …
- **DefiLlama:** https://defillama.com/protocol/curve-dex
- **PRIORITY 2.99**  =  LIKELIHOOD 59.77 × ACTIONABILITY 5.0%
    - likelihood = family evidence 30.0/50 (MATCH 60 × evidence weight 1.0) + learned attack surface 29.77/50
    - actionability: far above the band: continuous professional coverage assumed
- **Value at risk:** $1,327,174,451 · **Band:** `ABOVE_BAND_KEPT_EXPLICIT_DANGER`
- **REPEAT VICTIM — 2 recorded hacks.** 2023-07-30 $61,700,000 [Vyper Compiler Bug]
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 60 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `unverified_implementation` — raises likelihood, measured lift ×2.062 (weight +0.72)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`frxETH` @ 0x5e842234…(ethereum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for frxETH@0x5e842234…(ethereum); indicators matched: owner_compare_without_nonzero
    - 1 implementation(s) behind a proxy are NOT verified on the explorer: implementation identity unresolved, score capped at 60
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `EOA_SINGLE_KEY`; no ERC-1967 admin chain was proven
- **Prior art:** `UNREMEDIATED_KNOWN_ISSUE` — DefiLlama's hacks dataset records 1 prior on-chain incident(s) on this protocol, most recently 2023-07-30 for $61,700,000 [Vyper Compiler Bug]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#curve-dex|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#curve-dex`
- **Disclosure:** https://curve.finance · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.curve.finance/references/audits/

### 13. Radiant V2  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 13
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

### 14. Abracadabra Spell  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 14
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

### 15. Revest Finance  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 15
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

### 16. Iron Bank  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking B — likelihood, ignoring actionability):** 16
- **Protocol:** Iron Bank (`iron-bank`) · Lending · Ethereum, Optimism, Avalanche, Fantom
- **DefiLlama:** https://defillama.com/protocol/iron-bank
- **PRIORITY 59.18**  =  LIKELIHOOD 59.18 × ACTIONABILITY 100.0%
    - likelihood = family evidence 30.0/50 (MATCH 60 × evidence weight 1.0) + learned attack surface 29.18/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $216,657 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 60 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `unverified_implementation` — raises likelihood, measured lift ×2.062 (weight +0.72)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
- **Broken invariant tested:** After deployment, no caller may (re)establish ownership, admin, or implementation wiring. Initialization state must be provably consumed.
    - Deployed source (`CErc20Immutable` @ 0x004c0908…(ethereum)): prerequisites matched: initialize_without_modifier; no guard found
    - deployed source read for CErc20Immutable@0x004c0908…(ethereum); indicators matched: initialize_without_modifier
    - 1 implementation(s) behind a proxy are NOT verified on the explorer: implementation identity unresolved, score capped at 60
    - 1/1 live proxies read a zero ERC-7201 Initializable slot (inconclusive alone: older OZ versions store the flag elsewhere)
- **Preconditions PRESENT / UNKNOWN:** src::initialize_without_modifier, upgradeable_architecture, initializer_flag_unset, live_value_or_approvals / none
- **Guards searched / found:** initializer_modifier_present, upgrade_timelocked / upgrade_timelocked
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **one externally-owned account** (`EOA_SINGLE_KEY`) — a code fix here does not remove that exposure, and it is the cheaper thing to raise first
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Simulated re-initialization reverts (kills the pair); Contract is non-upgradeable and holds no approvals
- **Where to start:** Read the initialization slot on every live proxy/facet and simulate re-initialization from an unprivileged address; it must revert.
- **Evidence:** `protocols/deep_screened.jsonl#iron-bank|UPGRADE-INITIALIZER-REACHABLE-LIVE`, `protocols/onchain_probes.json#iron-bank`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/trailofbits/publications/blob/master/reviews/CREAMSummary.pdf

### 17. BoringDAO  —  `ACC-DUPLICATE-ID-ACCUMULATION`

- **Rank (Ranking B — likelihood, ignoring actionability):** 17
- **Protocol:** BoringDAO (`boringdao`) · Cross Chain Bridge · Litecoin, Polygon, Doge, Ethereum, Avalanche, OKExChain …
- **DefiLlama:** https://defillama.com/protocol/boringdao
- **PRIORITY 59.17**  =  LIKELIHOOD 59.17 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 27.27/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $337,559 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
- **Broken invariant tested:** An entitlement attached to an identifier may be counted at most once per period. A caller-supplied ID list must be deduplicated, or each ID's claim state consumed before the next read.
    - Deployed source (`OToken` @ 0x07C44B5A…(ethereum), `BoringSatelliteChef` @ 0x204c87CD…(ethereum)): prerequisites matched: id_array_loop_without_dedup; no guard found
    - deployed source read for OToken@0x07C44B5A…(ethereum), BoringSatelliteChef@0x204c87CD…(ethereum); indicators matched: id_array_loop_without_dedup
- **Preconditions PRESENT / UNKNOWN:** src::id_array_loop_without_dedup, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `EOA_SINGLE_KEY`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Consumed marker written inside the loop (kills the pair); IDs required strictly increasing
- **Where to start:** On a fork, call the batch function with one ID repeated k times; payout must equal the single-ID payout.
- **Evidence:** `protocols/deep_screened.jsonl#boringdao|ACC-DUPLICATE-ID-ACCUMULATION`, `protocols/onchain_probes.json#boringdao`
- **Disclosure:** https://www.boringdao.com/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/BoringDAO/boringDAO-contract/blob/master/peckshield-audit-report-boringdao-v1.0rc.pdf

### 18. Cytonic Airdrop Campaign  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 18
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

### 19. cSigma Finance  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking B — likelihood, ignoring actionability):** 19
- **Protocol:** cSigma Finance (`csigma-finance`) · RWA Lending · Arbitrum, Ethereum, Hedera, Base
- **DefiLlama:** https://defillama.com/protocol/csigma-finance
- **PRIORITY 35.29**  =  LIKELIHOOD 58.82 × ACTIONABILITY 60.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 21.92/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $21,601,384 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
- **Broken invariant tested:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source (`Diamond` @ 0x45dCf4F9…(arbitrum), `CsigmaV2Factory` @ 0x63da09d5…(arbitrum)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for Diamond@0x45dCf4F9…(arbitrum), CsigmaV2Factory@0x63da09d5…(arbitrum); indicators matched: unsafe_cross_sign_cast
- **Preconditions PRESENT / UNKNOWN:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** safecast_used / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#csigma-finance|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#csigma-finance`
- **Disclosure:** https://csigma.finance · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/csigma-labs/audit-reports/blob/main/cSigma%20Edge%20Audit%20Report%20-%20QuillAudits.pdf, https://github.com/csigma-labs/audit-reports/blob/main/cSigma%20Institutional%20Audit%20Report%20-%20Immunebytes.pdf

### 20. Gravita Protocol  —  `ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE`

- **Rank (Ranking B — likelihood, ignoring actionability):** 20
- **Protocol:** Gravita Protocol (`gravita-protocol`) · CDP · Ethereum, Optimism, Arbitrum, Polygon zkEVM, Mantle, zkSync Era …
- **DefiLlama:** https://defillama.com/protocol/gravita-protocol
- **PRIORITY 58.67**  =  LIKELIHOOD 58.67 × ACTIONABILITY 100.0%
    - likelihood = family evidence 30.0/50 (MATCH 60 × evidence weight 1.0) + learned attack surface 28.67/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $395,368 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 60 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `unverified_implementation` — raises likelihood, measured lift ×2.062 (weight +0.72)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
- **Broken invariant tested:** A vault share rate is an accounting quantity of another protocol, not a market price. Using it as a feed imports every way that vault's rate can be moved, including donation inflation and same-transaction redemption effects.
    - Deployed source (`RPLVault` @ 0xc730c6a1…(ethereum)): prerequisites matched: rate_used_as_price; no guard found
    - deployed source read for RPLVault@0xc730c6a1…(ethereum); indicators matched: rate_used_as_price
    - 1 implementation(s) behind a proxy are NOT verified on the explorer: implementation identity unresolved, score capped at 60
    - declared oracles: Chainlink, Api3 (types: Primary)
- **Preconditions PRESENT / UNKNOWN:** src::rate_used_as_price, value_decision_reads_configured_feed, live_positions_exposed / feed_selection_is_configuration
- **Guards searched / found:** deviation_bound_vs_independent_source / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `EOA_SINGLE_KEY`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Growth-capped rate adapter in the deployed oracle (kills the pair); Wrapper's own rate is monotonic and rate-limited; Collateral priced by an independent market feed instead
- **Where to start:** On a fork, donate to and cycle the underlying vault; assert the lending market's reported collateral price moves no more than the configured cap.
- **Evidence:** `protocols/deep_screened.jsonl#gravita-protocol|ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE`, `protocols/onchain_probes.json#gravita-protocol`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.gravitaprotocol.com/gravita-docs/about-gravita-protocol/audits

### 21. QiDao  —  `ORACLE-STALE-OR-SILENT-FALLBACK`

- **Rank (Ranking B — likelihood, ignoring actionability):** 21
- **Protocol:** QiDao (`qidao`) · CDP · Polygon, Base, Ethereum, Avalanche, Optimism, Fantom …
- **DefiLlama:** https://defillama.com/protocol/qidao
- **PRIORITY 49.6**  =  LIKELIHOOD 58.35 × ACTIONABILITY 85.0%
    - likelihood = family evidence 33.5/50 (MATCH 67.0 × evidence weight 1.0) + learned attack surface 24.85/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $2,708,451 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 67.0 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
    - Conditions: `PRICING_SURFACE_UNDECLARED`
    - Deployed source (`ContractOne` @ 0x11826d20…(arbitrum), `crosschainQiStablecoinSlim` @ 0x12FcB286…(arbitrum)): prerequisites matched: latestRoundData_without_staleness; no guard found
    - deployed source read for ContractOne@0x11826d20…(arbitrum), crosschainQiStablecoinSlim@0x12FcB286…(arbitrum); indicators matched: latestRoundData_without_staleness
    - condition PRICING_SURFACE_UNDECLARED (PRIORITY): A lending, CDP, derivatives or curation archetype with no oracle declared at all: the pricing path is unmapped.
    - only one oracle (or none) is declared in DefiLlama metadata; this is a prioritisation signal about disclosure, not evidence that no cross-source deviation bound exists in code
- **Preconditions PRESENT / UNKNOWN:** src::latestRoundData_without_staleness, value_decision_reads_configured_feed, live_positions_exposed / src::getPool_without_zero_check, feed_selection_is_configuration
- **Guards searched / found:** staleness_check, deviation_bound_vs_independent_source / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `EOA_SINGLE_KEY`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Where to start:** On a fork, force each configured feed to return zero, a stale timestamp, and a 10x/0.1x value; every value-bearing entrypoint must revert rather than transact.
- **Evidence:** `protocols/deep_screened.jsonl#qidao|ORACLE-STALE-OR-SILENT-FALLBACK`, `protocols/onchain_probes.json#qidao`
- **Disclosure:** https://app.mai.finance · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.mai.finance/risks/security#has-the-project-been-audited

### 22. Piku Finance  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking B — likelihood, ignoring actionability):** 22
- **Protocol:** Piku Finance (`piku-finance`) · Basis Trading · Ethereum
- **DefiLlama:** https://defillama.com/protocol/piku-finance
- **PRIORITY 34.99**  =  LIKELIHOOD 58.32 × ACTIONABILITY 60.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 21.42/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $29,352,222 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source (`ERC20IssuanceUpgradeable_Blacklist_v1` @ 0x9e40b6be…(ethereum), `StockMarketTRBasisTradeCustomAggregatorFeed` @ 0xe6e024d7…(ethereum)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for ERC20IssuanceUpgradeable_Blacklist_v1@0x9e40b6be…(ethereum), StockMarketTRBasisTradeCustomAggregatorFeed@0xe6e024d7…(ethereum); indicators matched: unsafe_cross_sign_cast
- **Preconditions PRESENT / UNKNOWN:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** safecast_used / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#piku-finance|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#piku-finance`
- **Disclosure:** https://piku.co/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.piku.co/piku/piku/security-and-risks/audits

### 23. NFTX  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 23
- **Protocol:** NFTX (`nftx`) · NFT Marketplace · Ethereum, Arbitrum
- **DefiLlama:** https://defillama.com/protocol/nftx
- **PRIORITY 49.55**  =  LIKELIHOOD 58.3 × ACTIONABILITY 85.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 21.4/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,967,102 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`NFTXVaultFactoryUpgradeable` @ 0xfa750439…(ethereum), `MiniMeToken` @ 0x87d73e91…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for NFTXVaultFactoryUpgradeable@0xfa750439…(ethereum), MiniMeToken@0x87d73e91…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#nftx|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#nftx`
- **Disclosure:** https://nftx.io · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/NFTX-project/audit-level-k/blob/master/NFTX-final.pdf

### 24. MorpheusAI  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 24
- **Protocol:** MorpheusAI (`morpheusai`) · AI Agents · Ethereum, Arbitrum, Base
- **DefiLlama:** https://defillama.com/protocol/morpheusai
- **PRIORITY 34.84**  =  LIKELIHOOD 58.07 × ACTIONABILITY 60.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 21.17/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $20,854,791 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`WStETHMock` @ 0x42BB446e…(ethereum), `DepositPool` @ 0xdb10daef…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for WStETHMock@0x42BB446e…(ethereum), DepositPool@0xdb10daef…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#morpheusai|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#morpheusai`
- **Disclosure:** https://mor.org · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/MorpheusAIs/Docs/tree/main/Security%20Audit%20Reports

### 25. Bridge Mutual  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 25
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

### 26. Tetu Earn  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 26
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

### 27. Accountable  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 27
- **Protocol:** Accountable (`accountable`) · Uncollateralized Lending · Robinhood Chain, Monad, Arbitrum, Ethereum, Citrea
- **DefiLlama:** https://defillama.com/protocol/accountable
- **PRIORITY 49.27**  =  LIKELIHOOD 57.97 × ACTIONABILITY 85.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 21.07/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $2,313,689 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`FixedTermFactory` @ 0x2A7F22f8…(arbitrum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for FixedTermFactory@0x2A7F22f8…(arbitrum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#accountable|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#accountable`
- **Disclosure:** https://accountable.capital/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.accountable.capital/accountable-documentation/readme/audits

### 28. VaultCraft  —  `SIG-VERIFIER-DEFEATABLE`

- **Rank (Ranking B — likelihood, ignoring actionability):** 28
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

### 29. Rari Capital  —  `SIG-VERIFIER-DEFEATABLE`

- **Rank (Ranking B — likelihood, ignoring actionability):** 29
- **Protocol:** Rari Capital (`rari-capital`) · Yield Aggregator · Ethereum, Arbitrum
- **DefiLlama:** https://defillama.com/protocol/rari-capital
- **PRIORITY 48.99**  =  LIKELIHOOD 57.63 × ACTIONABILITY 85.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 20.73/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,374,781 · **Band:** `IN_BAND`
- **REPEAT VICTIM — 3 recorded hacks.** 2025-12-18 $2,000,000 [Uninitialized Proxy]; 2022-05-01 $80,000,000 [Reentrancy]
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A verification routine must reject malformed, empty or zero-recovered signatures, and must never treat address(0) as a match.
    - Deployed source (`UniswapV2Pair` @ 0x18a797c7…(ethereum), `RariFundProxy` @ 0x35DDEFa2…(ethereum)): prerequisites matched: ecrecover_without_zero_check; no guard found
    - deployed source read for UniswapV2Pair@0x18a797c7…(ethereum), RariFundProxy@0x35DDEFa2…(ethereum); indicators matched: ecrecover_without_zero_check
- **Preconditions PRESENT / UNKNOWN:** src::ecrecover_without_zero_check, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** uses_oz_ecdsa / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `UNREMEDIATED_KNOWN_ISSUE` — DefiLlama's hacks dataset records 2 prior on-chain incident(s) on this protocol, most recently 2025-12-18 for $2,000,000 [Uninitialized Proxy]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** OZ ECDSA library in the deployed bytecode (kills the ecrecover-zero shape); Signer address immutable and non-zero
- **Where to start:** On a fork, submit r=0,s=0,v=27 and an empty signature to every signature-gated entrypoint; all must revert.
- **Evidence:** `protocols/deep_screened.jsonl#rari-capital|SIG-VERIFIER-DEFEATABLE`, `protocols/onchain_probes.json#rari-capital`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://www.notion.so/Rari-Capital-Audit-Quantstamp-December-2020-24a1d1df94894d6881ee190686f47bc7

### 30. XGLD  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking B — likelihood, ignoring actionability):** 30
- **Protocol:** XGLD (`xgld`) · Stablecoin Wrapper · Binance, Base, Ethereum
- **DefiLlama:** https://defillama.com/protocol/xgld
- **PRIORITY 34.53**  =  LIKELIHOOD 57.55 × ACTIONABILITY 60.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 20.65/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $11,365,300 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source (`XGLDToken` @ 0xe60106a5…(bsc), `USDu` @ 0xeA953eA6…(bsc)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for XGLDToken@0xe60106a5…(bsc), USDu@0xeA953eA6…(bsc); indicators matched: unsafe_cross_sign_cast
- **Preconditions PRESENT / UNKNOWN:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** safecast_used / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#xgld|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#xgld`
- **Disclosure:** https://evm.unitas.so/xgld · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/UnipayFI/Audit

### 31. WePiggy  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking B — likelihood, ignoring actionability):** 31
- **Protocol:** WePiggy (`wepiggy`) · Lending · Ethereum, Arbitrum, Optimism, Binance, Polygon, Aurora …
- **DefiLlama:** https://defillama.com/protocol/wepiggy
- **PRIORITY 57.47**  =  LIKELIHOOD 57.47 × ACTIONABILITY 100.0%
    - likelihood = family evidence 30.0/50 (MATCH 60 × evidence weight 1.0) + learned attack surface 27.47/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $802,765 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 60 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `unverified_implementation` — raises likelihood, measured lift ×2.062 (weight +0.72)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
- **Broken invariant tested:** After deployment, no caller may (re)establish ownership, admin, or implementation wiring. Initialization state must be provably consumed.
    - Deployed source (`CErc20Immutable` @ 0x004c0908…(ethereum)): prerequisites matched: initialize_without_modifier; no guard found
    - deployed source read for CErc20Immutable@0x004c0908…(ethereum); indicators matched: initialize_without_modifier
    - 1 implementation(s) behind a proxy are NOT verified on the explorer: implementation identity unresolved, score capped at 60
    - 1/1 live proxies read a zero ERC-7201 Initializable slot (inconclusive alone: older OZ versions store the flag elsewhere)
- **Preconditions PRESENT / UNKNOWN:** src::initialize_without_modifier, upgradeable_architecture, initializer_flag_unset, live_value_or_approvals / none
- **Guards searched / found:** initializer_modifier_present, upgrade_timelocked / upgrade_timelocked
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Simulated re-initialization reverts (kills the pair); Contract is non-upgradeable and holds no approvals
- **Where to start:** Read the initialization slot on every live proxy/facet and simulate re-initialization from an unprivileged address; it must revert.
- **Evidence:** `protocols/deep_screened.jsonl#wepiggy|UPGRADE-INITIALIZER-REACHABLE-LIVE`, `protocols/onchain_probes.json#wepiggy`
- **Disclosure:** https://www.wepiggy.com/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/WePiggy/wepiggy-contracts/tree/master/docs/audits

### 32. Gro  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 32
- **Protocol:** Gro (`gro`) · Yield · Ethereum, Avalanche
- **DefiLlama:** https://defillama.com/protocol/gro
- **PRIORITY 48.85**  =  LIKELIHOOD 57.47 × ACTIONABILITY 85.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 20.57/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,783,882 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`LPTokenStaker` @ 0x001C249c…(ethereum), `UniswapV2Pair` @ 0x21C5918C…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for LPTokenStaker@0x001C249c…(ethereum), UniswapV2Pair@0x21C5918C…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `EOA_SINGLE_KEY`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#gro|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#gro`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.gro.xyz/gro-docs/security/audits

### 33. Likwid  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking B — likelihood, ignoring actionability):** 33
- **Protocol:** Likwid (`likwid`) · Derivatives · Base, Binance, Ethereum
- **DefiLlama:** https://defillama.com/protocol/likwid
- **PRIORITY 57.4**  =  LIKELIHOOD 57.4 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 25.5/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $62,648 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`LikwidVault` @ 0x065d449e…(bsc), `LikwidHelper` @ 0x16a9633f…(bsc)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for LikwidVault@0x065d449e…(bsc), LikwidHelper@0x16a9633f…(bsc); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `EOA_SINGLE_KEY`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#likwid|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#likwid`
- **Disclosure:** https://likwid.fi · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/likwid-fi/likwid-margin/blob/main/audits/2025_11_13_Zenith_Likwid_V2_2_Audit_Report.pdf, https://github.com/likwid-fi/likwid-margin/blob/main/audits/2026_02_05_Sherlock_Likwid_V2_2_Audit_Report.pdf

### 34. Arcade.xyz  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking B — likelihood, ignoring actionability):** 34
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

### 35. OpenLeverage  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking B — likelihood, ignoring actionability):** 35
- **Protocol:** OpenLeverage (`openleverage`) · Dexs · Binance, Ethereum, Kucoin, Arbitrum
- **DefiLlama:** https://defillama.com/protocol/openleverage
- **PRIORITY 57.17**  =  LIKELIHOOD 57.17 × ACTIONABILITY 100.0%
    - likelihood = family evidence 30.0/50 (MATCH 60 × evidence weight 1.0) + learned attack surface 27.17/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $99,823 · **Band:** `IN_BAND`
- **Previously hacked:** 2024-04-01 for $0 [Unknown]
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 60 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `unverified_implementation` — raises likelihood, measured lift ×2.062 (weight +0.72)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
- **Broken invariant tested:** After deployment, no caller may (re)establish ownership, admin, or implementation wiring. Initialization state must be provably consumed.
    - Deployed source (`OpenLevV1` @ 0xd39a7f74…(bsc)): prerequisites matched: initialize_without_modifier; no guard found
    - deployed source read for OpenLevV1@0xd39a7f74…(bsc); indicators matched: initialize_without_modifier
    - 1 implementation(s) behind a proxy are NOT verified on the explorer: implementation identity unresolved, score capped at 60
    - 2/2 live proxies read a zero ERC-7201 Initializable slot (inconclusive alone: older OZ versions store the flag elsewhere)
- **Preconditions PRESENT / UNKNOWN:** src::initialize_without_modifier, upgradeable_architecture, initializer_flag_unset, live_value_or_approvals / none
- **Guards searched / found:** initializer_modifier_present, upgrade_timelocked / none in the reviewed path
- **Prior art:** `KNOWN_ISSUE_DEPLOYMENT_STATUS_UNKNOWN` — DefiLlama's hacks dataset records 1 prior on-chain incident(s) on this protocol, most recently 2024-04-01 for $0 [Unknown]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** Simulated re-initialization reverts (kills the pair); Contract is non-upgradeable and holds no approvals
- **Where to start:** Read the initialization slot on every live proxy/facet and simulate re-initialization from an unprivileged address; it must revert.
- **Evidence:** `protocols/deep_screened.jsonl#openleverage|UPGRADE-INITIALIZER-REACHABLE-LIVE`, `protocols/onchain_probes.json#openleverage`
- **Disclosure:** https://openleverage.finance · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/OpenLeverageDev/openleverage-contracts/blob/main/audits/REP-OpenLeverage-Protocol-2021-06-24.pdf, https://github.com/peckshield/publications/blob/master/audit_reports/PeckShield-Audit-Report-OpenLeverage-1.0.1.pdf

### 36. The Idols  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking B — likelihood, ignoring actionability):** 36
- **Protocol:** The Idols (`the-idols`) · Reserve Currency · Ethereum
- **DefiLlama:** https://defillama.com/protocol/the-idols
- **PRIORITY 48.38**  =  LIKELIHOOD 56.92 × ACTIONABILITY 85.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 20.02/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $6,571,389 · **Band:** `IN_BAND`
- **Previously hacked:** 2025-01-14 for $324,000 [Reward Logic Flaw]
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source (`IdolMarketplace` @ 0x0dd5a35f…(ethereum), `IdolMain` @ 0x439cac14…(ethereum)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for IdolMarketplace@0x0dd5a35f…(ethereum), IdolMain@0x439cac14…(ethereum); indicators matched: unsafe_cross_sign_cast
- **Preconditions PRESENT / UNKNOWN:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** safecast_used / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `KNOWN_ISSUE_DEPLOYMENT_STATUS_UNKNOWN` — DefiLlama's hacks dataset records 1 prior on-chain incident(s) on this protocol, most recently 2025-01-14 for $324,000 [Reward Logic Flaw]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#the-idols|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#the-idols`
- **Disclosure:** https://www.theidols.io · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.theidols.io/resources/audit

### 37. Angle  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 37
- **Protocol:** Angle (`angle`) · CDP · Ethereum, Arbitrum, Polygon, Optimism, Avalanche, Binance …
- **DefiLlama:** https://defillama.com/protocol/angle
- **PRIORITY 48.31**  =  LIKELIHOOD 56.83 × ACTIONABILITY 85.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 30.43/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $2,008,559 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - Conditions: `MULTICHAIN_VERSION_DRIFT`
    - condition MULTICHAIN_VERSION_DRIFT (PRIORITY): Deployed across many chains, where per-chain deployments drift and the least-watched chain sets the risk.
    - 8 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** prior_version_still_callable, still_holds_value_or_authority, not_paused / unmaintained_or_differing_code_path
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a Safe requiring several signatures** (`SAFE_M_OF_N`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#angle|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#angle`
- **Disclosure:** https://app.angle.money · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/AngleProtocol/angle-core/tree/main/audits

### 38. Maverick V1  —  `ACC-DUPLICATE-ID-ACCUMULATION`

- **Rank (Ranking B — likelihood, ignoring actionability):** 38
- **Protocol:** Maverick V1 (`maverick-v1`) · Dexs · zkSync Era, Ethereum, Binance, Base
- **DefiLlama:** https://defillama.com/protocol/maverick-v1
- **PRIORITY 48.2**  =  LIKELIHOOD 56.7 × ACTIONABILITY 85.0%
    - likelihood = family evidence 30.0/50 (MATCH 60 × evidence weight 1.0) + learned attack surface 26.7/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,064,242 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 60 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `unverified_implementation` — raises likelihood, measured lift ×2.062 (weight +0.72)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `version_sibling_legacy` — raises likelihood, measured lift ×1.699 (weight +0.53)
- **Broken invariant tested:** An entitlement attached to an identifier may be counted at most once per period. A caller-supplied ID list must be deduplicated, or each ID's claim state consumed before the next read.
    - Deployed source (`Router` @ 0xB2855783…(ethereum)): prerequisites matched: id_array_loop_without_dedup; no guard found
    - deployed source read for Router@0xB2855783…(ethereum); indicators matched: id_array_loop_without_dedup
    - 1 implementation(s) behind a proxy are NOT verified on the explorer: implementation identity unresolved, score capped at 60
- **Preconditions PRESENT / UNKNOWN:** src::id_array_loop_without_dedup, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Consumed marker written inside the loop (kills the pair); IDs required strictly increasing
- **Where to start:** On a fork, call the batch function with one ID repeated k times; payout must equal the single-ID payout.
- **Evidence:** `protocols/deep_screened.jsonl#maverick-v1|ACC-DUPLICATE-ID-ACCUMULATION`, `protocols/onchain_probes.json#maverick-v1`
- **Disclosure:** https://www.mav.xyz · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/maverickprotocol/audits

### 39. PoolTogether V3  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 39
- **Protocol:** PoolTogether V3 (`pooltogether-v3`) · Yield Lottery · Ethereum, Polygon, Celo, Binance
- **DefiLlama:** https://defillama.com/protocol/pooltogether-v3
- **PRIORITY 48.15**  =  LIKELIHOOD 56.65 × ACTIONABILITY 85.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 19.75/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $4,554,288 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
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
- **Evidence:** `protocols/deep_screened.jsonl#pooltogether-v3|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#pooltogether-v3`
- **Disclosure:** https://pooltogether.com/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.pooltogether.com/security/audits

### 40. DeFIL  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 40
- **Protocol:** DeFIL (`defil`) · Lending · Ethereum, Binance
- **DefiLlama:** https://defillama.com/protocol/defil
- **PRIORITY 48.07**  =  LIKELIHOOD 56.55 × ACTIONABILITY 85.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 19.65/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,759,083 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`Staking` @ 0x01aabbad…(ethereum), `DFL` @ 0x09ce2b74…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for Staking@0x01aabbad…(ethereum), DFL@0x09ce2b74…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `EOA_SINGLE_KEY`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#defil|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#defil`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://www.slowmist.com/security-audit-certificate.html?id=e84a975074cb9aef9299f9dec92311fd1458d0bbb4163adfadac8e16e0da3c61

### 41. Planet Farm  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 41
- **Protocol:** Planet Farm (`planet-farm`) · Yield · Binance
- **DefiLlama:** https://defillama.com/protocol/planet-farm
- **PRIORITY 48.02**  =  LIKELIHOOD 56.5 × ACTIONABILITY 85.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 19.6/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,657,781 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`PlanetFinance` @ 0x0ac58Fd2…(bsc), `PlanetFarm` @ 0x0116b420…(bsc)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for PlanetFinance@0x0ac58Fd2…(bsc), PlanetFarm@0x0116b420…(bsc); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **one externally-owned account** (`EOA_SINGLE_KEY`) — a code fix here does not remove that exposure, and it is the cheaper thing to raise first
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#planet-farm|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#planet-farm`
- **Disclosure:** https://app.planet.finance/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/HalbornSecurity/PublicReports/blob/master/Solidity%20Smart%20Contract%20Audits/Planet_Finance_Smart_Contract_Security_Audit_Halborn_v1_1.pdf

### 42. Across  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 42
- **Protocol:** Across (`across`) · Cross Chain Bridge · Ethereum
- **DefiLlama:** https://defillama.com/protocol/across
- **PRIORITY 33.77**  =  LIKELIHOOD 56.28 × ACTIONABILITY 60.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 19.38/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $20,247,263 · **Band:** `IN_BAND`
- **Previously hacked:** 2026-07-17 for $4,500,000 [Spoofed Event Log]
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`MiniMeToken` @ 0x3472A5A7…(ethereum), `BOBA` @ 0x42bBFa2e…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for MiniMeToken@0x3472A5A7…(ethereum), BOBA@0x42bBFa2e…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Prior art:** `KNOWN_ISSUE_DEPLOYMENT_STATUS_UNKNOWN` — DefiLlama's hacks dataset records 1 prior on-chain incident(s) on this protocol, most recently 2026-07-17 for $4,500,000 [Spoofed Event Log]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#across|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#across`
- **Disclosure:** https://across.to · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://blog.openzeppelin.com/uma-audit-l2-bridges/

### 43. KyberSwap Classic  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking B — likelihood, ignoring actionability):** 43
- **Protocol:** KyberSwap Classic (`kyberswap-classic`) · Dexs · Ethereum, Polygon, Avalanche, Binance, Optimism, zkSync Era …
- **DefiLlama:** https://defillama.com/protocol/kyberswap-classic
- **PRIORITY 47.43**  =  LIKELIHOOD 55.8 × ACTIONABILITY 85.0%
    - likelihood = family evidence 30.0/50 (MATCH 60 × evidence weight 1.0) + learned attack surface 25.8/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,041,666 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 60 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `unverified_implementation` — raises likelihood, measured lift ×2.062 (weight +0.72)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** After deployment, no caller may (re)establish ownership, admin, or implementation wiring. Initialization state must be provably consumed.
    - Deployed source (`KSFactory` @ 0x1c758aF0…(ethereum)): prerequisites matched: initialize_without_modifier; no guard found
    - deployed source read for KSFactory@0x1c758aF0…(ethereum); indicators matched: initialize_without_modifier
    - 1 implementation(s) behind a proxy are NOT verified on the explorer: implementation identity unresolved, score capped at 60
    - 1/1 live proxies read a zero ERC-7201 Initializable slot (inconclusive alone: older OZ versions store the flag elsewhere)
- **Preconditions PRESENT / UNKNOWN:** src::initialize_without_modifier, upgradeable_architecture, initializer_flag_unset, live_value_or_approvals / none
- **Guards searched / found:** initializer_modifier_present, upgrade_timelocked / upgrade_timelocked
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Simulated re-initialization reverts (kills the pair); Contract is non-upgradeable and holds no approvals
- **Where to start:** Read the initialization slot on every live proxy/facet and simulate re-initialization from an unprivileged address; it must revert.
- **Evidence:** `protocols/deep_screened.jsonl#kyberswap-classic|UPGRADE-INITIALIZER-REACHABLE-LIVE`, `protocols/onchain_probes.json#kyberswap-classic`
- **Disclosure:** https://kyberswap.com/#/swap · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://chainsecurity.com/security-audit/kyber-network-dynamic-market-maker-dmm/

### 44. Tarot  —  `ORACLE-SPOT-THIN-LIQUIDITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 44
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

### 45. EZMoney  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking B — likelihood, ignoring actionability):** 45
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

### 46. Tranchess Yield  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 46
- **Protocol:** Tranchess Yield (`tranchess-yield`) · Yield · Binance, Scroll, Ethereum
- **DefiLlama:** https://defillama.com/protocol/tranchess-yield
- **PRIORITY 47.37**  =  LIKELIHOOD 55.73 × ACTIONABILITY 85.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 18.83/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $4,871,755 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`BishopStableSwapV2` @ 0x01209A23…(bsc), `MaturityFund` @ 0x01907f04…(bsc)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for BishopStableSwapV2@0x01209A23…(bsc), MaturityFund@0x01907f04…(bsc); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `TIMELOCK`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#tranchess-yield|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#tranchess-yield`
- **Disclosure:** https://tranchess.com · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/peckshield/publications/blob/master/audit_reports/PeckShield-Audit-Report-Tranchess-v1.0.pdf, https://www.certik.org/projects/tranchess

### 47. Flying Tulip Lend  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 47
- **Protocol:** Flying Tulip Lend (`flying-tulip-lend`) · Lending · Ethereum, Sonic
- **DefiLlama:** https://defillama.com/protocol/flying-tulip-lend
- **PRIORITY 33.43**  =  LIKELIHOOD 55.72 × ACTIONABILITY 60.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 18.82/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $11,948,017 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`Frax1967Proxy` @ 0x00000000…(ethereum), `ftYieldWrapper` @ 0x51afd3ed…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for Frax1967Proxy@0x00000000…(ethereum), ftYieldWrapper@0x51afd3ed…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a Safe requiring several signatures** (`SAFE_M_OF_N`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#flying-tulip-lend|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#flying-tulip-lend`
- **Disclosure:** https://flyingtulip.com/lend/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.flyingtulip.com/risks/

### 48. Pell Network  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking B — likelihood, ignoring actionability):** 48
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

### 49. Bancor V2.1  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 49
- **Protocol:** Bancor V2.1 (`bancor-v2.1`) · Dexs · Ethereum
- **DefiLlama:** https://defillama.com/protocol/bancor-v2.1
- **PRIORITY 47.32**  =  LIKELIHOOD 55.67 × ACTIONABILITY 85.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 18.77/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $9,827,540 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `version_sibling_legacy` — raises likelihood, measured lift ×1.699 (weight +0.53)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`ContractRegistry` @ 0x52Ae12AB…(ethereum), `BancorConverterRegistry` @ 0xf6E2D7F6…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for ContractRegistry@0x52Ae12AB…(ethereum), BancorConverterRegistry@0xf6E2D7F6…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `EOA_SINGLE_KEY`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#bancor-v2.1|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#bancor-v2.1`
- **Disclosure:** https://app.bancor.network/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://bancor-network.gitbook.io/v2.1/ethereum-contracts/security

### 50. Yala  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking B — likelihood, ignoring actionability):** 50
- **Protocol:** Yala (`yala`) · CDP · Bitcoin, Ethereum
- **DefiLlama:** https://defillama.com/protocol/yala
- **PRIORITY 47.24**  =  LIKELIHOOD 55.58 × ACTIONABILITY 85.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 18.68/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $2,237,940 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source (`BridgeToken` @ 0x27A70B9F…(ethereum), `DebtToken` @ 0xE868084c…(ethereum)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for BridgeToken@0x27A70B9F…(ethereum), DebtToken@0xE868084c…(ethereum); indicators matched: unsafe_cross_sign_cast
- **Preconditions PRESENT / UNKNOWN:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** safecast_used / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#yala|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#yala`
- **Disclosure:** https://www.yala.org · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.yala.org/security-audits

### 51. iZiSwap  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking B — likelihood, ignoring actionability):** 51
- **Protocol:** iZiSwap (`iziswap`) · Dexs · zkSync Era, Scroll, ZetaChain, Manta, Binance, Linea …
- **DefiLlama:** https://defillama.com/protocol/iziswap
- **PRIORITY 47.24**  =  LIKELIHOOD 55.58 × ACTIONABILITY 85.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 18.68/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,662,324 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
- **Broken invariant tested:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source (`FlashModule` @ 0x110dE362…(bsc), `iZiSwapFactory` @ 0x1502d025…(bsc)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for FlashModule@0x110dE362…(bsc), iZiSwapFactory@0x1502d025…(bsc); indicators matched: unsafe_cross_sign_cast
- **Preconditions PRESENT / UNKNOWN:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** safecast_used / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `EOA_SINGLE_KEY`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#iziswap|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#iziswap`
- **Disclosure:** https://izumi.finance/trade/swap · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docsend.com/view/ura947u6ck3urpqb, https://docsend.com/view/2bif3vfinpv657mh

### 52. xWin Finance  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 52
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

### 53. deBridge  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 53
- **Protocol:** deBridge (`debridge`) · Bridge · Ethereum, Binance, Arbitrum, Polygon, Heco, Sei
- **DefiLlama:** https://defillama.com/protocol/debridge
- **PRIORITY 47.23**  =  LIKELIHOOD 55.57 × ACTIONABILITY 85.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 18.67/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,907,281 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`DeBridgeGate` @ 0x797161bc…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for DeBridgeGate@0x797161bc…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#debridge|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#debridge`
- **Disclosure:** https://app.debridge.com · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/debridge-finance/debridge-security

### 54. Wompie  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 54
- **Protocol:** Wompie (`wompie`) · Yield · Binance, Arbitrum
- **DefiLlama:** https://defillama.com/protocol/wompie
- **PRIORITY 47.23**  =  LIKELIHOOD 55.57 × ACTIONABILITY 85.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 18.67/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,023,525 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`mWOM` @ 0xfc3a0ca6…(bsc), `mWomSV` @ 0xaa037b4b…(bsc)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for mWOM@0xfc3a0ca6…(bsc), mWomSV@0xaa037b4b…(bsc); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#wompie|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#wompie`
- **Disclosure:** https://www.magpiexyz.io · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/peckshield/publications/blob/master/audit_reports/PeckShield-Audit-Report-Magpie-v1.1.pdf

### 55. PepeTeam Bridge  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking B — likelihood, ignoring actionability):** 55
- **Protocol:** PepeTeam Bridge (`pepeteam-bridge`) · Bridge · Ethereum, Waves, Polygon, Binance, Tron
- **DefiLlama:** https://defillama.com/protocol/pepeteam-bridge
- **PRIORITY 55.33**  =  LIKELIHOOD 55.33 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 23.43/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $745,485 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`EIP173Proxy` @ 0x0de7b091…(ethereum), `EIP173Proxy` @ 0x88226032…(ethereum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for EIP173Proxy@0x0de7b091…(ethereum), EIP173Proxy@0x88226032…(ethereum); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#pepeteam-bridge|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#pepeteam-bridge`
- **Disclosure:** https://bridge.pepe.team · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/deemru/pepebridge-audit

### 56. Sentora  —  `ACC-DUPLICATE-ID-ACCUMULATION`

- **Rank (Ranking B — likelihood, ignoring actionability):** 56
- **Protocol:** Sentora (`sentora`) · Risk Curators · Ethereum, Ink, Solana, Tempo
- **DefiLlama:** https://defillama.com/protocol/sentora
- **PRIORITY 2.77**  =  LIKELIHOOD 55.33 × ACTIONABILITY 5.0%
    - likelihood = family evidence 30.0/50 (MATCH 60 × evidence weight 1.0) + learned attack surface 25.33/50
    - actionability: far above the band: continuous professional coverage assumed
- **Value at risk:** $2,417,461,031 · **Band:** `ABOVE_BAND_KEPT_EXPLICIT_DANGER`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 60 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `unverified_implementation` — raises likelihood, measured lift ×2.062 (weight +0.72)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
- **Broken invariant tested:** An entitlement attached to an identifier may be counted at most once per period. A caller-supplied ID list must be deduplicated, or each ID's claim state consumed before the next read.
    - Deployed source (`BoringVault` @ 0x13cc1b39…(ethereum)): prerequisites matched: id_array_loop_without_dedup; no guard found
    - deployed source read for BoringVault@0x13cc1b39…(ethereum); indicators matched: id_array_loop_without_dedup
    - 1 implementation(s) behind a proxy are NOT verified on the explorer: implementation identity unresolved, score capped at 60
- **Preconditions PRESENT / UNKNOWN:** src::id_array_loop_without_dedup, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Consumed marker written inside the loop (kills the pair); IDs required strictly increasing
- **Where to start:** On a fork, call the batch function with one ID repeated k times; payout must equal the single-ID payout.
- **Evidence:** `protocols/deep_screened.jsonl#sentora|ACC-DUPLICATE-ID-ACCUMULATION`, `protocols/onchain_probes.json#sentora`
- **Disclosure:** https://sentora.com/ · no audit link listed

### 57. TermFinance Vaults  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking B — likelihood, ignoring actionability):** 57
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

### 58. SingularityDAO  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 58
- **Protocol:** SingularityDAO (`singularitydao`) · Yield · Ethereum, Binance
- **DefiLlama:** https://defillama.com/protocol/singularitydao
- **PRIORITY 55.3**  =  LIKELIHOOD 55.3 × ACTIONABILITY 100.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 28.9/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $436,691 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - 6 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** prior_version_still_callable, still_holds_value_or_authority / unmaintained_or_differing_code_path, not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **one externally-owned account** (`EOA_SINGLE_KEY`) — a code fix here does not remove that exposure, and it is the cheaper thing to raise first
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#singularitydao|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#singularitydao`
- **Disclosure:** https://singularitydao.ai · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.singularitydao.ai/security/smart-contract-audits, https://www.certik.com/projects/singularitydao

### 59. Aavegotchi  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 59
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

### 60. Kokonut Swap  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking B — likelihood, ignoring actionability):** 60
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
