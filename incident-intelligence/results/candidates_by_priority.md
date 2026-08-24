# Candidates — Ranking A — priority (likelihood × actionability)

> **Discovery stage.** This file asserts no defect in any protocol named below. Each entry is a *review candidate*: named evidence matches a family's prerequisites, named evidence is unknown, and a named guard would falsify it. Verify on a local or pinned fork before concluding anything.

**Scoring is now validated, not asserted.** Attack-surface weights were fitted on 2022-24 hacks and tested against 2025-26 hacks: 95 protocols unseen during fitting, median victim landing at the **78.6th percentile**, **58%** of future victims in the model's top quartile — a **×2.32 lift** over chance.

**Likelihood and actionability are kept apart.** Bigger protocols are *more* likely to be attacked (`tvl_over_5m` carries lift ×1.75) and *less* actionable for an independent reviewer. Folding those together is what produced earlier rankings full of protocols you cannot help. PRIORITY multiplies them explicitly so you can see both halves.

**Exposure age beat every other addition, and it contradicts the obvious intuition.** Protocols under a year old carry lift ×1.87; protocols over three years old carry ×0.33. It is not the abandoned deployments that get hit — it is the new ones. Ablation attributes the whole out-of-sample gain to this one group (×2.19 → ×2.32).

**Custody posture was measured and then deliberately dropped from the score.** A single-key upgrade authority does not predict a code defect (measured ×0.98 over the full window; adding it moved out-of-sample lift ×2.19 → ×2.15, i.e. slightly worse). That is the expected answer, since key compromise is an excluded root cause here — so it is reported on its own in `results/upgrade_authority_exposure.md`, where 23 protocols holding $56.4M have an ERC-1967 upgrade authority terminating in a single key. Often the cheapest thing on this whole list to fix.

**A finding that overturned the earlier model:** measured against survivors only, neglect looked protective. It is not — 62.5% of victims that fell below $50k had no audit, versus 20.9% of those still listed. The population was censored by the very outcome being predicted. Weights are now fitted against the full listed universe.

### At a glance

| | |
|---|---:|
| Candidates | 60 |
| Previously hacked | 10 |
| Repeat victims (2+ recorded hacks) | 7 |
| Median value at risk | $237,912 |
| Total value at risk | $28,301,109 |
| At L4 guard review | 56 |

### Repeat victims in this list

Whatever allowed a second incident has not necessarily been removed. These are the highest-conviction entries in the set.

| Protocol | Hacks | Family | Priority | At risk |
|---|---:|---|---:|---:|
| [Hundred Finance](https://defillama.com/protocol/hundred-finance) | 2 | `AUTH-ZERO-ADDRESS-ACCEPTED` | 61.18 | $73,585 |
| [Radiant V2](https://defillama.com/protocol/radiant-v2) | 2 | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 59.7 | $693,778 |
| [Bunny](https://defillama.com/protocol/bunny) | 2 | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 54.36 | $3,597,277 |
| [CREAM Lending](https://defillama.com/protocol/cream-lending) | 2 | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | 53.93 | $149,030 |
| [dForce Lending](https://defillama.com/protocol/dforce-lending) | 2 | `AUTH-ZERO-ADDRESS-ACCEPTED` | 52.5 | $1,027,387 |
| [Conic Finance](https://defillama.com/protocol/conic-finance) | 2 | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 52.15 | $63,068 |
| [Zunami Protocol](https://defillama.com/protocol/zunami-protocol) | 2 | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | 51.93 | $548,289 |

### Diversified shortlist — top 3 per family

| # | Protocol | Family | Priority | Likelihood | At risk | Evidence |
|---:|---|---|---:|---:|---:|---|
| 1 | [Hundred Finance](https://defillama.com/protocol/hundred-finance) | `AUTH-ZERO-ADDRESS-ACCEPTED` | 61.18 | 61.18 | $73,585 | `L4_GUARD_REVIEW` |
| 2 | [Sperax USD](https://defillama.com/protocol/sperax-usd) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 61.08 | 61.08 | $520,189 | `L4_GUARD_REVIEW` |
| 3 | [Cook Finance](https://defillama.com/protocol/cook-finance) | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | 60.13 | 60.13 | $51,767 | `L4_GUARD_REVIEW` |
| 4 | [Radiant V2](https://defillama.com/protocol/radiant-v2) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 59.7 | 59.7 | $693,778 | `L4_GUARD_REVIEW` |
| 5 | [Revest Finance](https://defillama.com/protocol/revest-finance) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 59.45 | 59.45 | $107,916 | `L4_GUARD_REVIEW` |
| 6 | [Iron Bank](https://defillama.com/protocol/iron-bank) | `AUTH-ZERO-ADDRESS-ACCEPTED` | 59.18 | 59.18 | $216,657 | `L4_GUARD_REVIEW` |
| 7 | [BoringDAO](https://defillama.com/protocol/boringdao) | `ACC-DUPLICATE-ID-ACCUMULATION` | 59.17 | 59.17 | $337,559 | `L4_GUARD_REVIEW` |
| 8 | [Cytonic Airdrop Campaign](https://defillama.com/protocol/cytonic-airdrop-campaign) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 59.0 | 59.0 | $169,482 | `L4_GUARD_REVIEW` |
| 9 | [Gravita Protocol](https://defillama.com/protocol/gravita-protocol) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 58.67 | 58.67 | $395,368 | `L4_GUARD_REVIEW` |
| 10 | [Bridge Mutual](https://defillama.com/protocol/bridge-mutual) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 58.05 | 58.05 | $56,267 | `L4_GUARD_REVIEW` |
| 11 | [VaultCraft](https://defillama.com/protocol/vaultcraft) | `SIG-VERIFIER-DEFEATABLE` | 57.73 | 57.73 | $557,157 | `L4_GUARD_REVIEW` |
| 12 | [WePiggy](https://defillama.com/protocol/wepiggy) | `AUTH-ZERO-ADDRESS-ACCEPTED` | 57.47 | 57.47 | $802,765 | `L4_GUARD_REVIEW` |
| 13 | [Arcade.xyz](https://defillama.com/protocol/arcade.xyz) | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | 57.25 | 57.25 | $210,561 | `L4_GUARD_REVIEW` |
| 14 | [OpenLeverage](https://defillama.com/protocol/openleverage) | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | 57.17 | 57.17 | $99,823 | `L4_GUARD_REVIEW` |
| 15 | [Tarot](https://defillama.com/protocol/tarot) | `ORACLE-SPOT-THIN-LIQUIDITY` | 55.77 | 55.77 | $583,969 | `L4_GUARD_REVIEW` |
| 16 | [InsurAce](https://defillama.com/protocol/insurace) | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | 55.0 | 55.0 | $142,772 | `L4_GUARD_REVIEW` |
| 17 | [Impermax V2](https://defillama.com/protocol/impermax-v2) | `ORACLE-SPOT-THIN-LIQUIDITY` | 54.75 | 54.75 | $596,796 | `L4_GUARD_REVIEW` |
| 18 | [iZUMi LiquidBox](https://defillama.com/protocol/izumi-liquidbox) | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | 54.72 | 54.72 | $121,512 | `L4_GUARD_REVIEW` |
| 19 | [SatLayer](https://defillama.com/protocol/satlayer) | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | 54.0 | 54.0 | $184,744 | `L4_GUARD_REVIEW` |
| 20 | [Accumulated Finance Liquid Staking](https://defillama.com/protocol/accumulated-finance-liquid-staking) | `SIG-VERIFIER-DEFEATABLE` | 53.65 | 53.65 | $622,677 | `L4_GUARD_REVIEW` |
| 21 | [Horizon Protocol](https://defillama.com/protocol/horizon-protocol) | `ACC-CREDIT-NOT-RECEIVED` | 52.57 | 52.57 | $233,312 | `L4_GUARD_REVIEW` |
| 22 | [SynFutures V1](https://defillama.com/protocol/synfutures-v1) | `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY` | 52.53 | 52.53 | $112,430 | `L3_STATE` |
| 23 | [StoneDefi](https://defillama.com/protocol/stonedefi) | `SIG-VERIFIER-DEFEATABLE` | 52.45 | 52.45 | $75,186 | `L4_GUARD_REVIEW` |
| 24 | [Likwid](https://defillama.com/protocol/likwid) | `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY` | 51.9 | 51.9 | $62,648 | `L3_STATE` |
| 25 | [SmartCredit](https://defillama.com/protocol/smartcredit) | `ORACLE-SPOT-THIN-LIQUIDITY` | 51.3 | 51.3 | $204,900 | `L4_GUARD_REVIEW` |
| 26 | [Fuji V1](https://defillama.com/protocol/fuji-v1) | `ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE` | 51.22 | 51.22 | $197,607 | `L3_STATE` |
| 27 | [Krystal Community Vault](https://defillama.com/protocol/krystal-community-vault) | `ACC-DUPLICATE-ID-ACCUMULATION` | 51.18 | 51.18 | $229,978 | `L4_GUARD_REVIEW` |
| 28 | [Loop](https://defillama.com/protocol/loop) | `ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE` | 50.12 | 50.12 | $76,962 | `L4_GUARD_REVIEW` |
| 29 | [Bunny](https://defillama.com/protocol/bunny) | `ACC-HARDCODED-PEG-REDEMPTION` | 50.11 | 58.95 | $3,597,277 | `L4_GUARD_REVIEW` |
| 30 | [VenomBridge](https://defillama.com/protocol/venombridge) | `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY` | 49.97 | 49.97 | $743,145 | `L3_STATE` |

---

### 1. Hundred Finance  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 1
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

### 2. Sperax USD  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking A — priority (likelihood × actionability)):** 2
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

### 3. Cook Finance  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 3
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

### 4. Radiant V2  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 4
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

### 5. Revest Finance  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 5
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

### 6. Iron Bank  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 6
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

### 7. BoringDAO  —  `ACC-DUPLICATE-ID-ACCUMULATION`

- **Rank (Ranking A — priority (likelihood × actionability)):** 7
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

### 8. Cytonic Airdrop Campaign  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 8
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

### 9. Gravita Protocol  —  `ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 9
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

### 10. Bridge Mutual  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 10
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

### 11. Tetu Earn  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 11
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

### 12. VaultCraft  —  `SIG-VERIFIER-DEFEATABLE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 12
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

### 13. WePiggy  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 13
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

### 14. Likwid  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 14
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

### 15. Arcade.xyz  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 15
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

### 16. OpenLeverage  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 16
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

### 17. Kine Finance  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 17
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

### 18. Tarot  —  `ORACLE-SPOT-THIN-LIQUIDITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 18
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

### 19. EZMoney  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking A — priority (likelihood × actionability)):** 19
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

### 20. Pell Network  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking A — priority (likelihood × actionability)):** 20
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

### 21. xWin Finance  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 21
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

### 22. PepeTeam Bridge  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 22
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

### 23. SingularityDAO  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 23
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

### 24. Aavegotchi  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 24
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

### 25. Kokonut Swap  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 25
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

### 26. Bunni V2  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 26
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

### 27. InsurAce  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 27
- **Protocol:** InsurAce (`insurace`) · Insurance · Binance, Ethereum, Polygon, Avalanche
- **DefiLlama:** https://defillama.com/protocol/insurace
- **PRIORITY 55.0**  =  LIKELIHOOD 55.0 × ACTIONABILITY 100.0%
    - likelihood = family evidence 30.0/50 (MATCH 60 × evidence weight 1.0) + learned attack surface 25.0/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $142,772 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 60 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `unverified_implementation` — raises likelihood, measured lift ×2.062 (weight +0.72)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`InsurAceToken` @ 0x544c42fb…(bsc)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for InsurAceToken@0x544c42fb…(bsc); indicators matched: hook_zero_amount_unguarded
    - 1 implementation(s) behind a proxy are NOT verified on the explorer: implementation identity unresolved, score capped at 60
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#insurace|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#insurace`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.insurace.io/landing-page/documentation/security-1

### 28. 88mph  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 28
- **Protocol:** 88mph (`88mph`) · Lending · Ethereum, Fantom, Avalanche, Polygon
- **DefiLlama:** https://defillama.com/protocol/88mph
- **PRIORITY 54.97**  =  LIKELIHOOD 54.97 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 23.07/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $359,152 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`OptimizedTransparentUpgradeableProxy` @ 0x062214fb…(ethereum), `OptimizedTransparentUpgradeableProxy` @ 0x0f834c36…(ethereum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for OptimizedTransparentUpgradeableProxy@0x062214fb…(ethereum), OptimizedTransparentUpgradeableProxy@0x0f834c36…(ethereum); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#88mph|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#88mph`
- **Disclosure:** https://88mph.app/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.88mph.app/developer-docs/security

### 29. BiFi  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 29
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

### 30. Impermax V2  —  `ORACLE-SPOT-THIN-LIQUIDITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 30
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

### 31. iZUMi LiquidBox  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 31
- **Protocol:** iZUMi LiquidBox (`izumi-liquidbox`) · Yield · Binance, Arbitrum, Ethereum, Polygon, Aurora, Cronos
- **DefiLlama:** https://defillama.com/protocol/izumi-liquidbox
- **PRIORITY 54.72**  =  LIKELIHOOD 54.72 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 22.82/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $121,512 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`izumiToken` @ 0x9ad37205…(ethereum), `veiZi` @ 0xb56a454d…(ethereum)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for izumiToken@0x9ad37205…(ethereum), veiZi@0xb56a454d…(ethereum); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `EOA_SINGLE_KEY`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#izumi-liquidbox|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#izumi-liquidbox`
- **Disclosure:** https://izumi.finance · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docsend.com/view/ura947u6ck3urpqb, https://docsend.com/view/2bif3vfinpv657mh

### 32. Fuji V1  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 32
- **Protocol:** Fuji V1 (`fuji-v1`) · Lending · Ethereum, Arbitrum, Polygon, Fantom, Optimism
- **DefiLlama:** https://defillama.com/protocol/fuji-v1
- **PRIORITY 54.52**  =  LIKELIHOOD 54.52 × ACTIONABILITY 100.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 28.12/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $197,607 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `version_sibling_legacy` — raises likelihood, measured lift ×1.699 (weight +0.53)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - Conditions: `VERSION_SIBLING_LEGACY`, `DEAD_FRONTEND_FUNDED`
    - condition VERSION_SIBLING_LEGACY (PRECOND): Shares a parent protocol with a higher-version sibling while still holding value: the classic sibling-deployment-retains-the-old-version shape.
    - condition DEAD_FRONTEND_FUNDED (PRECOND): Front end is dead while contracts still hold value: nobody is watching the deployment that still holds funds.
    - 3 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** unmaintained_or_differing_code_path, prior_version_still_callable, still_holds_value_or_authority / not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#fuji-v1|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#fuji-v1`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/Fujicracy/fuji-protocol/blob/main/audits/Fuji_Securing_2021-07.pdf, https://github.com/Fujicracy/fuji-protocol/blob/main/audits/Fuji_TrailOfBits_2021-11.pdf

### 33. Bunny  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 33
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

### 34. GrizzlyFi Hives  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 34
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

### 35. SatLayer  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 35
- **Protocol:** SatLayer (`satlayer`) · Anchor BTC · Ethereum, Binance, Sui, Babylon Genesis, Berachain, Bitlayer …
- **DefiLlama:** https://defillama.com/protocol/satlayer
- **PRIORITY 54.0**  =  LIKELIHOOD 54.0 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 22.1/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $184,744 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`uniBTC` @ 0xe0e6a124…(ethereum), `SatLayerPoolV2` @ 0x32fD8E43…(ethereum)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for uniBTC@0xe0e6a124…(ethereum), SatLayerPoolV2@0x32fD8E43…(ethereum); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#satlayer|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#satlayer`
- **Disclosure:** https://satlayer.xyz/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/satlayer/deposit-contract-public/blob/main/audits/Satlayer_audit_report_2024-08-15.pdf, https://github.com/satlayer/deposit-contract-public/blob/main/audits/SatLayer%20Pool%20-%20Zellic%20Audit%20Report.pdf

### 36. CREAM Lending  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 36
- **Protocol:** CREAM Lending (`cream-lending`) · Lending · Binance, Polygon, Arbitrum, Ethereum, Base
- **DefiLlama:** https://defillama.com/protocol/cream-lending
- **PRIORITY 53.93**  =  LIKELIHOOD 53.93 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 22.03/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $149,030 · **Band:** `IN_BAND`
- **REPEAT VICTIM — 2 recorded hacks.** 
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`StakingPool` @ 0x004c0908…(bsc), `StakingPool` @ 0x04493F71…(bsc)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for StakingPool@0x004c0908…(bsc), StakingPool@0x04493F71…(bsc); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `EOA_SINGLE_KEY`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#cream-lending|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#cream-lending`
- **Disclosure:** https://cream.finance/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.cream.finance/audit-report

### 37. Wombex Finance  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 37
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

### 38. RadioShack  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 38
- **Protocol:** RadioShack (`radioshack`) · Dexs · Binance, Avalanche, Polygon, Ethereum, Cronos, Dogechain …
- **DefiLlama:** https://defillama.com/protocol/radioshack
- **PRIORITY 53.88**  =  LIKELIHOOD 53.88 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 21.98/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $453,693 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`UniswapV2Factory` @ 0x1D72b58d…(bsc), `RadioToken` @ 0x30807D3b…(bsc)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for UniswapV2Factory@0x1D72b58d…(bsc), RadioToken@0x30807D3b…(bsc); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_1_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#radioshack|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#radioshack`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://www.certik.com/projects/radioshack

### 39. Accumulated Finance Liquid Staking  —  `SIG-VERIFIER-DEFEATABLE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 39
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

### 40. Stabull Finance  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking A — priority (likelihood × actionability)):** 40
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

### 41. YieldWolf  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 41
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

### 42. Infinite Trading Protocol  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 42
- **Protocol:** Infinite Trading Protocol (`infinite-trading-protocol`) · AI Agents · Optimism, Base, Ethereum, Polygon, Arbitrum
- **DefiLlama:** https://defillama.com/protocol/infinite-trading-protocol
- **PRIORITY 52.93**  =  LIKELIHOOD 52.93 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 21.03/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $228,023 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`PoolFactory` @ 0x7256070a…(base)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for PoolFactory@0x7256070a…(base); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#infinite-trading-protocol|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#infinite-trading-protocol`
- **Disclosure:** https://www.infinitetrading.io/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/0xGuard-com/audit-reports/blob/master/Infinite%20Trading%20Protocol/Infinite%20Trading%20Protocol.pdf

### 43. Cakepie  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 43
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

### 44. Shift Protocol  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 44
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

### 45. FinNexus  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 45
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

### 46. Goldsand by InshAllah  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking A — priority (likelihood × actionability)):** 46
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

### 47. PoolTogether V4  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 47
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

### 48. Horizon Protocol  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 48
- **Protocol:** Horizon Protocol (`horizon-protocol`) · Derivatives · Binance
- **DefiLlama:** https://defillama.com/protocol/horizon-protocol
- **PRIORITY 52.57**  =  LIKELIHOOD 52.57 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 20.67/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $233,312 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`BEP20PHB` @ 0x0409633A…(bsc), `StakingRewards` @ 0x5646aA2F…(bsc)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for BEP20PHB@0x0409633A…(bsc), StakingRewards@0x5646aA2F…(bsc); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `EOA_SINGLE_KEY`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#horizon-protocol|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#horizon-protocol`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://static.horizonprotocol.com/Horizon-Protocol-Smart-Contract-Audit-Report.pdf

### 49. SynFutures V1  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 49
- **Protocol:** SynFutures V1 (`synfutures-v1`) · Derivatives · Polygon, Binance, Ethereum, Arbitrum
- **DefiLlama:** https://defillama.com/protocol/synfutures-v1
- **PRIORITY 52.53**  =  LIKELIHOOD 52.53 × ACTIONABILITY 100.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 26.13/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $112,430 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `unverified_implementation` — raises likelihood, measured lift ×2.062 (weight +0.72)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `version_sibling_legacy` — raises likelihood, measured lift ×1.699 (weight +0.53)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - Conditions: `VERSION_SIBLING_LEGACY`
    - condition VERSION_SIBLING_LEGACY (PRECOND): Shares a parent protocol with a higher-version sibling while still holding value: the classic sibling-deployment-retains-the-old-version shape.
    - 1 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** prior_version_still_callable, still_holds_value_or_authority / unmaintained_or_differing_code_path, not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `EOA_SINGLE_KEY`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#synfutures-v1|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#synfutures-v1`
- **Disclosure:** https://www.synfutures.com/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://www.synfutures.com/peckshield-audit-report-synfutures-v1.1.pdf

### 50. dForce Lending  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 50
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

### 51. StoneDefi  —  `SIG-VERIFIER-DEFEATABLE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 51
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

### 52. Ante Finance  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 52
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

### 53. Rubicon  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking A — priority (likelihood × actionability)):** 53
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

### 54. Conic Finance  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 54
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

### 55. yAxis  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 55
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

### 56. IMPOSSIBLE  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 56
- **Protocol:** IMPOSSIBLE (`impossible`) · Launchpad · Binance, Aurora, OKExChain, Avalanche, Boba, Kava …
- **DefiLlama:** https://defillama.com/protocol/impossible
- **PRIORITY 52.07**  =  LIKELIHOOD 52.07 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 20.17/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $133,417 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`ImpossibleDecentralizedIncubatorAccessToken` @ 0x0b15ddf1…(bsc), `IFAllocationMaster` @ 0x1aBd0067…(bsc)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for ImpossibleDecentralizedIncubatorAccessToken@0x0b15ddf1…(bsc), IFAllocationMaster@0x1aBd0067…(bsc); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `EOA_SINGLE_KEY`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#impossible|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#impossible`
- **Disclosure:** https://impossible.finance · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/ImpossibleFinance/audits

### 57. PrismaLST  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 57
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

### 58. Zunami Protocol  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 58
- **Protocol:** Zunami Protocol (`zunami-protocol`) · Yield Aggregator · Ethereum
- **DefiLlama:** https://defillama.com/protocol/zunami-protocol
- **PRIORITY 51.93**  =  LIKELIHOOD 51.93 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 20.03/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $548,289 · **Band:** `IN_BAND`
- **REPEAT VICTIM — 2 recorded hacks.** 2023-08-13 $2,100,000 [Spot Price Manipulation]
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`ZunamiPoolApsZunUSD` @ 0x28e487bb…(ethereum), `ERC1967Proxy` @ 0x45af4F12…(ethereum)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for ZunamiPoolApsZunUSD@0x28e487bb…(ethereum), ERC1967Proxy@0x45af4F12…(ethereum); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `UNREMEDIATED_KNOWN_ISSUE` — DefiLlama's hacks dataset records 1 prior on-chain incident(s) on this protocol, most recently 2023-08-13 for $2,100,000 [Spot Price Manipulation]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#zunami-protocol|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#zunami-protocol`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/ZunamiLab/ZunamiProtocol/tree/main/audit

### 59. Fungify  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 59
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

### 60. Single Finance  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 60
- **Protocol:** Single Finance (`single-finance`) · Leveraged Farming · Cronos, Arbitrum, Fantom
- **DefiLlama:** https://defillama.com/protocol/single-finance
- **PRIORITY 51.88**  =  LIKELIHOOD 51.88 × ACTIONABILITY 100.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 25.48/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $69,849 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `unverified_implementation` — raises likelihood, measured lift ×2.062 (weight +0.72)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - 2 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** prior_version_still_callable, still_holds_value_or_authority / unmaintained_or_differing_code_path, not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#single-finance|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#single-finance`
- **Disclosure:** https://singlefinance.io · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://www.certik.com/projects/singlefinance
