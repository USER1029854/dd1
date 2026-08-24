# Candidates — Ranking B — likelihood, ignoring actionability

> **Discovery stage.** This file asserts no defect in any protocol named below. Each entry is a *review candidate*: named evidence matches a family's prerequisites, named evidence is unknown, and a named guard would falsify it. Verify on a local or pinned fork before concluding anything.

**How these are scored** is set out once, at the top of [`candidates_by_priority.md`](candidates_by_priority.md): the out-of-sample validation, why likelihood and actionability are kept apart, and why custody exposure is reported separately.

### The ranking

Full write-ups below for the 30 entries that `candidates_by_priority.md` does not already cover; the other 30 are listed here and written up in full there, under the same `protocol — family` heading.

| # | Protocol | Family | LIKELIHOOD | At risk | Write-up |
|---:|---|---|---:|---:|---|
| 1 | [Keep3r Network](https://defillama.com/protocol/keep3r-network) | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | 69.05 | $3,186,925 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 2 | [Venus Isolated Pools](https://defillama.com/protocol/venus-isolated-pools) | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | 63.38 | $1,122,520 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 3 | [Yam Finance](https://defillama.com/protocol/yam-finance) | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | 62.87 | $237,414 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 4 | [Mummy Finance](https://defillama.com/protocol/mummy-finance) | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | 60.6 | $54,685 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 5 | [Penpie](https://defillama.com/protocol/penpie) | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | 59.4 | $4,503,553 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 6 | [Cozy V1](https://defillama.com/protocol/cozy-v1) | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | 58.1 | $72,293 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 7 | [Sommelier](https://defillama.com/protocol/sommelier) | `SIG-VERIFIER-DEFEATABLE` | 56.3 | $906,670 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 8 | [Fira](https://defillama.com/protocol/fira) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 56.0 | $9,852,774 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 9 | [Mitosis](https://defillama.com/protocol/mitosis) | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | 55.58 | $1,379,158 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 10 | [Flying Tulip ftUSD](https://defillama.com/protocol/flying-tulip-ftusd) | `ACC-DUPLICATE-ID-ACCUMULATION` | 53.67 | $2,273,825 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 11 | [Exactly](https://defillama.com/protocol/exactly) | `SIG-VERIFIER-DEFEATABLE` | 52.75 | $8,067,579 | below |
| 12 | [Clovis](https://defillama.com/protocol/clovis) | `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY` | 52.5 | $234,245 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 13 | [Thesauros](https://defillama.com/protocol/thesauros) | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | 52.28 | $51,215 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 14 | [ZeroLend Lending](https://defillama.com/protocol/zerolend-lending) | `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY` | 52.07 | $3,903,136 | below |
| 15 | [Easedefi.org](https://defillama.com/protocol/easedefi.org) | `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY` | 52.03 | $4,821,120 | below |
| 16 | [Tokenlon AMM](https://defillama.com/protocol/tokenlon-amm) | `SIG-VERIFIER-DEFEATABLE` | 51.85 | $588,461 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 17 | [JPEG'd](https://defillama.com/protocol/jpegd) | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | 51.77 | $564,479 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 18 | [Sushi BentoBox](https://defillama.com/protocol/sushi-bentobox) | `SIG-VERIFIER-DEFEATABLE` | 51.52 | $2,477,441 | below |
| 19 | [Inverse Finance FiRM](https://defillama.com/protocol/inverse-finance-firm) | `SIG-VERIFIER-DEFEATABLE` | 51.35 | $28,336,326 | below |
| 20 | [OnX Finance](https://defillama.com/protocol/onx-finance) | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | 51.32 | $305,022 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 21 | [King Protocol](https://defillama.com/protocol/king-protocol) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 51.32 | $1,323,385 | below |
| 22 | [DODO AMM](https://defillama.com/protocol/dodo-amm) | `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY` | 51.12 | $12,379,916 | below |
| 23 | [AlphaX](https://defillama.com/protocol/alphax) | `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY` | 51.02 | $1,861,771 | below |
| 24 | [Theoriq Gold Vault](https://defillama.com/protocol/theoriq-gold-vault) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 50.85 | $131,019 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 25 | [UltraYield Vaults](https://defillama.com/protocol/ultrayield-vaults) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 50.85 | $13,527,105 | below |
| 26 | [Nerona](https://defillama.com/protocol/nerona) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 50.48 | $2,154,453 | below |
| 27 | [Cryptex V1](https://defillama.com/protocol/cryptex-v1) | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | 50.38 | $428,629 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 28 | [Sudoswap V1](https://defillama.com/protocol/sudoswap-v1) | `ACC-DUPLICATE-ID-ACCUMULATION` | 50.13 | $660,847 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 29 | [PEAKDEFI](https://defillama.com/protocol/peakdefi) | `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY` | 50.12 | $110,630 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 30 | [CANA Holdings California Carbon Credits](https://defillama.com/protocol/cana-holdings-california-carbon-credits) | `SIG-VERIFIER-DEFEATABLE` | 49.83 | $893,977 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 31 | [Umami Finance](https://defillama.com/protocol/umami-finance) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 49.57 | $387,748 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 32 | [Bancor V3](https://defillama.com/protocol/bancor-v3) | `AUTH-ZERO-ADDRESS-ACCEPTED` | 49.55 | $16,647,315 | below |
| 33 | [SushiSwap](https://defillama.com/protocol/sushiswap) | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | 49.55 | $39,285,082 | below |
| 34 | [Tanken Capital](https://defillama.com/protocol/tanken-capital) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 49.22 | $85,381 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 35 | [Conduit Bridge](https://defillama.com/protocol/conduit-bridge) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 49.08 | $1,202,760 | below |
| 36 | [Frax Swap](https://defillama.com/protocol/frax-swap) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 49.05 | $10,396,247 | below |
| 37 | [Byzanlink RWA Markets](https://defillama.com/protocol/byzanlink-rwa-markets) | `AUTH-ZERO-ADDRESS-ACCEPTED` | 48.93 | $1,477,713 | below |
| 38 | [Balancer V1](https://defillama.com/protocol/balancer-v1) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 48.9 | $7,271,376 | below |
| 39 | [Interest Protocol](https://defillama.com/protocol/interest-protocol) | `ORACLE-SPOT-THIN-LIQUIDITY` | 48.85 | $1,448,816 | below |
| 40 | [Swellchain Bridge](https://defillama.com/protocol/swellchain-bridge) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 48.55 | $368,677 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 41 | [Morph Bridge](https://defillama.com/protocol/morph-bridge) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 48.55 | $15,558,534 | below |
| 42 | [MaxShot](https://defillama.com/protocol/maxshot) | `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY` | 48.53 | $165,700 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 43 | [Tangent Finance](https://defillama.com/protocol/tangent-finance) | `ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE` | 48.47 | $4,474,120 | below |
| 44 | [Joe V2.1](https://defillama.com/protocol/joe-v2.1) | `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY` | 48.45 | $3,572,509 | below |
| 45 | [dYdX V3](https://defillama.com/protocol/dydx-v3) | `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY` | 48.37 | $38,722,798 | below |
| 46 | [ApeSwap AMM](https://defillama.com/protocol/apeswap-amm) | `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY` | 48.22 | $9,475,642 | below |
| 47 | [Revault](https://defillama.com/protocol/revault) | `AUTH-ZERO-ADDRESS-ACCEPTED` | 48.15 | $2,076,308 | below |
| 48 | [Silo V1](https://defillama.com/protocol/silo-v1) | `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY` | 47.9 | $1,453,111 | below |
| 49 | [Royco V2](https://defillama.com/protocol/royco-v2) | `ACC-NAV-SHAREPRICE-MANIPULABLE` | 47.87 | $23,040,883 | below |
| 50 | [DeltaPrime](https://defillama.com/protocol/deltaprime) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 47.7 | $3,648,228 | below |
| 51 | [Alongside](https://defillama.com/protocol/alongside) | `ACC-CREDIT-NOT-RECEIVED` | 47.68 | $467,535 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 52 | [Revert Compoundor](https://defillama.com/protocol/revert-compoundor) | `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY` | 47.6 | $146,380 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 53 | [InsureDAO](https://defillama.com/protocol/insuredao) | `SECRET-EMBEDDED-IN-PUBLIC-CODE-AS-AUTH` | 47.6 | $123,685 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 54 | [Reflexer](https://defillama.com/protocol/reflexer) | `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY` | 47.6 | $2,623,624 | below |
| 55 | [Chamber Vaults](https://defillama.com/protocol/chamber-vaults) | `AUTH-ZERO-ADDRESS-ACCEPTED` | 47.6 | $23,648,490 | below |
| 56 | [Kinza Finance](https://defillama.com/protocol/kinza-finance) | `ORACLE-STALE-OR-SILENT-FALLBACK` | 47.58 | $3,277,468 | below |
| 57 | [Extra Finance Leverage Farming](https://defillama.com/protocol/extra-finance-leverage-farming) | `ACC-QUOTE-STALE-ACROSS-OWN-SWAP` | 47.43 | $24,987,646 | below |
| 58 | [EZManager](https://defillama.com/protocol/ezmanager) | `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY` | 47.4 | $430,190 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 59 | [Mayan Bridge](https://defillama.com/protocol/mayan-bridge) | `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY` | 47.4 | $123,829 | [in `candidates_by_priority.md`](candidates_by_priority.md) |
| 60 | [Rezerve Money](https://defillama.com/protocol/rezerve-money) | `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY` | 47.38 | $598,045 | [in `candidates_by_priority.md`](candidates_by_priority.md) |

---

### 11. Exactly  —  `SIG-VERIFIER-DEFEATABLE`

- **Rank (Ranking B — likelihood, ignoring actionability):** 11
- **Protocol:** Exactly (`exactly`) · Lending · Base, Optimism, Ethereum
- **DefiLlama:** https://defillama.com/protocol/exactly
- **PRIORITY 44.84**  =  LIKELIHOOD 52.75 × ACTIONABILITY 85.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 15.85/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $8,067,579 · **Band:** `IN_BAND`
- **Previously hacked:** 2023-08-18 for $7,600,000 [Improper Access Control]
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A verification routine must reject malformed, empty or zero-recovered signatures, and must never treat address(0) as a match.
    - Deployed source (`TransparentUpgradeableProxy` @ 0x310A2694…(ethereum), `Auditor` @ 0xaEb62e6F…(ethereum)): prerequisites matched: ecrecover_without_zero_check; no guard found
    - deployed source read for TransparentUpgradeableProxy@0x310A2694…(ethereum), Auditor@0xaEb62e6F…(ethereum); indicators matched: ecrecover_without_zero_check
- **Preconditions PRESENT / UNKNOWN:** src::ecrecover_without_zero_check, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** uses_oz_ecdsa / none in the reviewed path
- **Prior art:** `KNOWN_ISSUE_DEPLOYMENT_STATUS_UNKNOWN` — DefiLlama's hacks dataset records 1 prior on-chain incident(s) on this protocol, most recently 2023-08-18 for $7,600,000 [Improper Access Control]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** OZ ECDSA library in the deployed bytecode (kills the ecrecover-zero shape); Signer address immutable and non-zero
- **Where to start:** On a fork, submit r=0,s=0,v=27 and an empty signature to every signature-gated entrypoint; all must revert.
- **Evidence:** `protocols/deep_screened.jsonl#exactly|SIG-VERIFIER-DEFEATABLE`, `protocols/onchain_probes.json#exactly`
- **Disclosure:** https://exact.ly · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/exactly/audits

### 14. ZeroLend Lending  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 14
- **Protocol:** ZeroLend Lending (`zerolend-lending`) · Lending · Linea, zkSync Era, Blast, Ethereum, Manta, Base …
- **DefiLlama:** https://defillama.com/protocol/zerolend-lending
- **PRIORITY 44.26**  =  LIKELIHOOD 52.07 × ACTIONABILITY 85.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 25.67/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $3,903,136 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - Conditions: `MULTICHAIN_VERSION_DRIFT`
    - condition MULTICHAIN_VERSION_DRIFT (PRIORITY): Deployed across many chains, where per-chain deployments drift and the least-watched chain sets the risk.
    - 4 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** prior_version_still_callable, still_holds_value_or_authority, not_paused / unmaintained_or_differing_code_path
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#zerolend-lending|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#zerolend-lending`
- **Disclosure:** https://zerolend.xyz/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/zerolend/audits/blob/main/mundus/zerolend_report_depcheck_final.pdf

### 15. Easedefi.org  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 15
- **Protocol:** Easedefi.org (`easedefi.org`) · Insurance · Ethereum
- **DefiLlama:** https://defillama.com/protocol/easedefi.org
- **PRIORITY 44.23**  =  LIKELIHOOD 52.03 × ACTIONABILITY 85.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 25.63/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $4,821,120 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - 5 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** prior_version_still_callable, still_holds_value_or_authority / unmaintained_or_differing_code_path, not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#easedefi.org|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#easedefi.org`
- **Disclosure:** https://easedefi.org · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/EaseDeFi/Audits/blob/main/Dedaub_RCA_Audit.pdf, https://github.com/EaseDeFi/gvToken/tree/main/audits

### 18. Sushi BentoBox  —  `SIG-VERIFIER-DEFEATABLE`

- **Rank (Ranking B — likelihood, ignoring actionability):** 18
- **Protocol:** Sushi BentoBox (`sushi-bentobox`) · Yield · Arbitrum, Ethereum, Polygon, Optimism, Avalanche, xDai …
- **DefiLlama:** https://defillama.com/protocol/sushi-bentobox
- **PRIORITY 43.79**  =  LIKELIHOOD 51.52 × ACTIONABILITY 85.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 14.62/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $2,477,441 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
- **Broken invariant tested:** A verification routine must reject malformed, empty or zero-recovered signatures, and must never treat address(0) as a match.
    - Deployed source (`BentoBoxV1` @ 0x74c764d4…(arbitrum)): prerequisites matched: ecrecover_without_zero_check; no guard found
    - deployed source read for BentoBoxV1@0x74c764d4…(arbitrum); indicators matched: ecrecover_without_zero_check
- **Preconditions PRESENT / UNKNOWN:** src::ecrecover_without_zero_check, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** uses_oz_ecdsa / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** OZ ECDSA library in the deployed bytecode (kills the ecrecover-zero shape); Signer address immutable and non-zero
- **Where to start:** On a fork, submit r=0,s=0,v=27 and an empty signature to every signature-gated entrypoint; all must revert.
- **Evidence:** `protocols/deep_screened.jsonl#sushi-bentobox|SIG-VERIFIER-DEFEATABLE`, `protocols/onchain_probes.json#sushi-bentobox`
- **Disclosure:** https://www.sushi.com · no audit link listed

### 19. Inverse Finance FiRM  —  `SIG-VERIFIER-DEFEATABLE`

- **Rank (Ranking B — likelihood, ignoring actionability):** 19
- **Protocol:** Inverse Finance FiRM (`inverse-finance-firm`) · CDP · Ethereum
- **DefiLlama:** https://defillama.com/protocol/inverse-finance-firm
- **PRIORITY 30.81**  =  LIKELIHOOD 51.35 × ACTIONABILITY 60.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 14.45/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $28,336,326 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A verification routine must reject malformed, empty or zero-recovered signatures, and must never treat address(0) as a match.
    - Deployed source (`DolaBorrowingRights` @ 0xAD038Eb6…(ethereum)): prerequisites matched: ecrecover_without_zero_check; no guard found
    - deployed source read for DolaBorrowingRights@0xAD038Eb6…(ethereum); indicators matched: ecrecover_without_zero_check
- **Preconditions PRESENT / UNKNOWN:** src::ecrecover_without_zero_check, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** uses_oz_ecdsa / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** OZ ECDSA library in the deployed bytecode (kills the ecrecover-zero shape); Signer address immutable and non-zero
- **Where to start:** On a fork, submit r=0,s=0,v=27 and an empty signature to every signature-gated entrypoint; all must revert.
- **Evidence:** `protocols/deep_screened.jsonl#inverse-finance-firm|SIG-VERIFIER-DEFEATABLE`, `protocols/onchain_probes.json#inverse-finance-firm`
- **Disclosure:** https://inverse.finance · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://www.inverse.finance/audits

### 21. King Protocol  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 21
- **Protocol:** King Protocol (`king-protocol`) · Liquid Restaking · Ethereum
- **DefiLlama:** https://defillama.com/protocol/king-protocol
- **PRIORITY 43.62**  =  LIKELIHOOD 51.32 × ACTIONABILITY 85.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 14.42/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,323,385 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`LRTSquaredCore` @ 0x1cb489ef…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for LRTSquaredCore@0x1cb489ef…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#king-protocol|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#king-protocol`
- **Disclosure:** https://kingprotocol.org/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/King-Protocol/king-cross-chain/blob/master/audit/NM_0452_King_Cross_Chain_FINAL.pdf, https://github.com/King-Protocol/king-protocol-sc/tree/master/audits

### 22. DODO AMM  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 22
- **Protocol:** DODO AMM (`dodo-amm`) · Dexs · Binance, Ethereum, Polygon, Avalanche, Arbitrum, Base …
- **DefiLlama:** https://defillama.com/protocol/dodo-amm
- **PRIORITY 30.67**  =  LIKELIHOOD 51.12 × ACTIONABILITY 60.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 24.72/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $12,379,916 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `owner_is_eoa` — raises likelihood, measured lift ×1.729 (weight +0.55)
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
- **Evidence:** `protocols/deep_screened.jsonl#dodo-amm|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#dodo-amm`
- **Disclosure:** https://dodoex.io/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/DODOEX/docs/blob/master/docs/audit.md

### 23. AlphaX  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 23
- **Protocol:** AlphaX (`alphax`) · Derivatives · Binance, Ethereum, Arbitrum, Tron
- **DefiLlama:** https://defillama.com/protocol/alphax
- **PRIORITY 43.37**  =  LIKELIHOOD 51.02 × ACTIONABILITY 85.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 24.62/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,861,771 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - 6 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** prior_version_still_callable, still_holds_value_or_authority / unmaintained_or_differing_code_path, not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#alphax|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#alphax`
- **Disclosure:** https://alphax.com/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/AlphaX-Protocol/AlphaX-Protocol-Contract/blob/master/Audit-Report/AlphaX%20Audit%20final.pdf

### 25. UltraYield Vaults  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 25
- **Protocol:** UltraYield Vaults (`ultrayield-vaults`) · Onchain Capital Allocator · Ethereum
- **DefiLlama:** https://defillama.com/protocol/ultrayield-vaults
- **PRIORITY 30.51**  =  LIKELIHOOD 50.85 × ACTIONABILITY 60.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 13.95/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $13,527,105 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`UUPSProxy` @ 0x472425cc…(ethereum), `UltraVault` @ 0x88300e00…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for UUPSProxy@0x472425cc…(ethereum), UltraVault@0x88300e00…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#ultrayield-vaults|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#ultrayield-vaults`
- **Disclosure:** https://ultrayield.app/ · no audit link listed

### 26. Nerona  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 26
- **Protocol:** Nerona (`nerona`) · Yield Aggregator · Fluent, Ethereum
- **DefiLlama:** https://defillama.com/protocol/nerona
- **PRIORITY 42.91**  =  LIKELIHOOD 50.48 × ACTIONABILITY 85.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 13.58/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $2,154,453 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`ChiToken` @ 0x00000000…(ethereum), `zCurve` @ 0x00000000…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for ChiToken@0x00000000…(ethereum), zCurve@0x00000000…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#nerona|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#nerona`
- **Disclosure:**   · no audit link listed

### 32. Bancor V3  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking B — likelihood, ignoring actionability):** 32
- **Protocol:** Bancor V3 (`bancor-v3`) · Dexs · Ethereum
- **DefiLlama:** https://defillama.com/protocol/bancor-v3
- **PRIORITY 29.73**  =  LIKELIHOOD 49.55 × ACTIONABILITY 60.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 17.65/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $16,647,315 · **Band:** `IN_BAND`
- **REPEAT VICTIM — 2 recorded hacks.** 
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`SmartToken` @ 0x1f573d6f…(ethereum), `MasterVault` @ 0xf3b685d2…(ethereum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for SmartToken@0x1f573d6f…(ethereum), MasterVault@0xf3b685d2…(ethereum); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#bancor-v3|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#bancor-v3`
- **Disclosure:** https://app.bancor.network/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.bancor.network/about-bancor-network/security-and-audits

### 33. SushiSwap  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking B — likelihood, ignoring actionability):** 33
- **Protocol:** SushiSwap (`sushiswap`) · Dexs · Ethereum, Polygon, Arbitrum, Base, Boba, xDai …
- **DefiLlama:** https://defillama.com/protocol/sushiswap
- **PRIORITY 9.91**  =  LIKELIHOOD 49.55 × ACTIONABILITY 20.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 17.65/50
    - actionability: above the band: assume dedicated professional coverage
- **Value at risk:** $39,285,082 · **Band:** `ABOVE_BAND_KEPT_EXPLICIT_DANGER`
- **REPEAT VICTIM — 2 recorded hacks.** 
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`SushiBar` @ 0x8798249c…(ethereum), `SushiToken` @ 0x6b359506…(ethereum)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for SushiBar@0x8798249c…(ethereum), SushiToken@0x6b359506…(ethereum); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#sushiswap|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#sushiswap`
- **Disclosure:** https://sushi.com/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/peckshield/publications/blob/master/audit_reports/PeckShield-Audit-Report-SushiSwap-v1.0.pdf

### 35. Conduit Bridge  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 35
- **Protocol:** Conduit Bridge (`conduit-bridge`) · Bridge · Ethereum
- **DefiLlama:** https://defillama.com/protocol/conduit-bridge
- **PRIORITY 41.72**  =  LIKELIHOOD 49.08 × ACTIONABILITY 85.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 12.18/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,202,760 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`ERC1967Proxy` @ 0x00000000…(ethereum), `TrueGBP` @ 0x00000000…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for ERC1967Proxy@0x00000000…(ethereum), TrueGBP@0x00000000…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#conduit-bridge|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#conduit-bridge`
- **Disclosure:** https://www.conduit.xyz/ · no audit link listed

### 36. Frax Swap  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking B — likelihood, ignoring actionability):** 36
- **Protocol:** Frax Swap (`frax-swap`) · Dexs · Fraxtal, Ethereum, Binance, Avalanche, Polygon, Optimism …
- **DefiLlama:** https://defillama.com/protocol/frax-swap
- **PRIORITY 29.43**  =  LIKELIHOOD 49.05 × ACTIONABILITY 60.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 12.15/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $10,396,247 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
- **Broken invariant tested:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source (`FPIControllerPool` @ 0x2397321b…(ethereum), `FraxswapFactory` @ 0x43ec799e…(ethereum)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for FPIControllerPool@0x2397321b…(ethereum), FraxswapFactory@0x43ec799e…(ethereum); indicators matched: unsafe_cross_sign_cast
- **Preconditions PRESENT / UNKNOWN:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** safecast_used / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#frax-swap|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#frax-swap`
- **Disclosure:** https://frax.com/swap · no audit link listed

### 37. Byzanlink RWA Markets  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking B — likelihood, ignoring actionability):** 37
- **Protocol:** Byzanlink RWA Markets (`byzanlink-rwa-markets`) · RWA · Hedera, Solana, Ethereum
- **DefiLlama:** https://defillama.com/protocol/byzanlink-rwa-markets
- **PRIORITY 41.59**  =  LIKELIHOOD 48.93 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 17.03/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,477,713 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `owner_is_eoa` — raises likelihood, measured lift ×1.729 (weight +0.55)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`VaultV2` @ 0xA5cDEE01…(ethereum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for VaultV2@0xA5cDEE01…(ethereum); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#byzanlink-rwa-markets|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#byzanlink-rwa-markets`
- **Disclosure:** https://markets.byzanlink.com · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://sherlock-files.ams3.digitaloceanspaces.com/reports/2026.01.19%20-%20Final%20-%20Byzanlink%20Collaborative%20Audit%20Report%201768840093.pdf, https://sherlock-files.ams3.digitaloceanspaces.com/reports/2026.01.19%20-%20Final%20-%20Byzanlink%20Collaborative%20Audit%20Report%201768839590.pdf

### 38. Balancer V1  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 38
- **Protocol:** Balancer V1 (`balancer-v1`) · Dexs · Ethereum
- **DefiLlama:** https://defillama.com/protocol/balancer-v1
- **PRIORITY 41.56**  =  LIKELIHOOD 48.9 × ACTIONABILITY 85.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 12.0/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $7,271,376 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `version_sibling_legacy` — raises likelihood, measured lift ×1.699 (weight +0.53)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`SafeguardFactory` @ 0x03c01aca…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for SafeguardFactory@0x03c01aca…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#balancer-v1|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#balancer-v1`
- **Disclosure:** https://balancer.fi/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.balancer.fi/reference/contracts/security.html#audits

### 39. Interest Protocol  —  `ORACLE-SPOT-THIN-LIQUIDITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 39
- **Protocol:** Interest Protocol (`interest-protocol`) · CDP · Ethereum, Optimism
- **DefiLlama:** https://defillama.com/protocol/interest-protocol
- **PRIORITY 41.52**  =  LIKELIHOOD 48.85 × ACTIONABILITY 85.0%
    - likelihood = family evidence 23.1/50 (MATCH 52.5 × evidence weight 0.88) + learned attack surface 25.75/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,448,816 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 52.5 · CONFIDENCE 69.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `unverified_implementation` — raises likelihood, measured lift ×2.007 (weight +0.70)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `owner_is_eoa` — raises likelihood, measured lift ×1.729 (weight +0.55)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Borrowing capacity, mint size, reward size or collateral value must not be derived from a price that a single actor can move within the manipulation window, and the value unlocked must never exceed the cost of moving that price.
    - Conditions: `SINGLE_PRIMARY_ORACLE_NO_CROSSCHECK`
    - Deployed source (`CappedGovToken` @ 0xe565e118…(ethereum)): no prerequisite matched; no guard found
    - RELEVANCE GATE: the contract(s) actually read (CappedGovToken) show no distinguishing indicator for this family, so they are probably not the contracts that implement it. Every source-derived signal is therefore UNKNOWN, including the absence of a guard: not finding a staleness check in a data-provider contract says nothing about the oracle.
    - condition SINGLE_PRIMARY_ORACLE_NO_CROSSCHECK (PRIORITY): Exactly one declared oracle and no declared secondary, so no cross-source deviation bound is declared.
    - only one oracle (or none) is declared in DefiLlama metadata; this is a prioritisation signal about disclosure, not evidence that no cross-source deviation bound exists in code
- **Preconditions PRESENT / UNKNOWN:** value_decision_reads_configured_feed, live_positions_exposed / feed_selection_is_configuration
- **Guards searched / found:** deviation_bound_vs_independent_source / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** All collateral priced by a deep aggregated feed with a deviation cap (kills the pair); Caps are set from measured venue depth and enforced on-chain; The action is sized from realised transfer amounts, so price is never an input
- **Where to start:** On a fork, execute a max-size flash-funded swap against every venue in the pricing path and assert that no value-bearing entrypoint changes its output beyond the configured deviation bound.
- **Evidence:** `protocols/deep_screened.jsonl#interest-protocol|ORACLE-SPOT-THIN-LIQUIDITY`, `protocols/onchain_probes.json#interest-protocol`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://gfx.cafe/ip/contracts/-/blob/master/audit/GFX_IP_Protocol_Audit_Report.pdf

### 41. Morph Bridge  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 41
- **Protocol:** Morph Bridge (`morph-bridge`) · Bridge · Ethereum
- **DefiLlama:** https://defillama.com/protocol/morph-bridge
- **PRIORITY 29.13**  =  LIKELIHOOD 48.55 × ACTIONABILITY 60.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 11.65/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $15,558,534 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`L1CrossDomainMessenger` @ 0x0cc37d52…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for L1CrossDomainMessenger@0x0cc37d52…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#morph-bridge|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#morph-bridge`
- **Disclosure:** https://bridge.morphl2.io/ · no audit link listed

### 43. Tangent Finance  —  `ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE`

- **Rank (Ranking B — likelihood, ignoring actionability):** 43
- **Protocol:** Tangent Finance (`tangent-finance`) · Lending · Ethereum
- **DefiLlama:** https://defillama.com/protocol/tangent-finance
- **PRIORITY 41.2**  =  LIKELIHOOD 48.47 × ACTIONABILITY 85.0%
    - likelihood = family evidence 33.0/50 (MATCH 66.0 × evidence weight 1.0) + learned attack surface 15.47/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $4,474,120 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 66.0 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A vault share rate is an accounting quantity of another protocol, not a market price. Using it as a feed imports every way that vault's rate can be moved, including donation inflation and same-transaction redemption effects.
    - Deployed source (`MarketCreator` @ 0x214C8A10…(ethereum)): prerequisites matched: rate_used_as_price; no guard found
    - deployed source read for MarketCreator@0x214C8A10…(ethereum); indicators matched: rate_used_as_price
    - protocol declares a Fallback/Secondary oracle: fallback selection logic exists by its own declaration
    - declared oracles: Chainlink, RedStone (types: Fallback, Primary)
- **Preconditions PRESENT / UNKNOWN:** src::rate_used_as_price, value_decision_reads_configured_feed, fallback_selection_logic_exists, live_positions_exposed / feed_selection_is_configuration
- **Guards searched / found:** deviation_bound_vs_independent_source / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Growth-capped rate adapter in the deployed oracle (kills the pair); Wrapper's own rate is monotonic and rate-limited; Collateral priced by an independent market feed instead
- **Where to start:** On a fork, donate to and cycle the underlying vault; assert the lending market's reported collateral price moves no more than the configured cap.
- **Evidence:** `protocols/deep_screened.jsonl#tangent-finance|ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE`, `protocols/onchain_probes.json#tangent-finance`
- **Disclosure:** https://app.tangent.finance/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.tangent.finance/docs/faq/audits

### 44. Joe V2.1  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 44
- **Protocol:** Joe V2.1 (`joe-v2.1`) · Dexs · Avalanche, Arbitrum, Binance, Ethereum
- **DefiLlama:** https://defillama.com/protocol/joe-v2.1
- **PRIORITY 41.18**  =  LIKELIHOOD 48.45 × ACTIONABILITY 85.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 22.05/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $3,572,509 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - 1 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** prior_version_still_callable, still_holds_value_or_authority / unmaintained_or_differing_code_path, not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#joe-v2.1|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#joe-v2.1`
- **Disclosure:** https://lfj.gg/arbitrum/trade · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.lfj.gg/audits

### 45. dYdX V3  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 45
- **Protocol:** dYdX V3 (`dydx-v3`) · Derivatives · Ethereum
- **DefiLlama:** https://defillama.com/protocol/dydx-v3
- **PRIORITY 9.67**  =  LIKELIHOOD 48.37 × ACTIONABILITY 20.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 21.97/50
    - actionability: above the band: assume dedicated professional coverage
- **Value at risk:** $38,722,798 · **Band:** `ABOVE_BAND_KEPT_EXPLICIT_DANGER`
- **REPEAT VICTIM — 2 recorded hacks.** 2023-11-18 $9,000,000 [Risk Parameter Abuse]
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `version_sibling_legacy` — raises likelihood, measured lift ×1.699 (weight +0.53)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - Conditions: `VERSION_SIBLING_LEGACY`
    - condition VERSION_SIBLING_LEGACY (PRECOND): Shares a parent protocol with a higher-version sibling while still holding value: the classic sibling-deployment-retains-the-old-version shape.
    - 6 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** prior_version_still_callable, still_holds_value_or_authority / unmaintained_or_differing_code_path, not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `UNREMEDIATED_KNOWN_ISSUE` — DefiLlama's hacks dataset records 1 prior on-chain incident(s) on this protocol, most recently 2023-11-18 for $9,000,000 [Risk Parameter Abuse]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#dydx-v3|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#dydx-v3`
- **Disclosure:** https://dydx.trade · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.dydx.exchange/#independent-audits

### 46. ApeSwap AMM  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 46
- **Protocol:** ApeSwap AMM (`apeswap-amm`) · Dexs · Binance, Polygon, Arbitrum, Telos, Ethereum
- **DefiLlama:** https://defillama.com/protocol/apeswap-amm
- **PRIORITY 40.99**  =  LIKELIHOOD 48.22 × ACTIONABILITY 85.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 21.82/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $9,475,642 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `unverified_implementation` — raises likelihood, measured lift ×2.007 (weight +0.70)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `owner_is_eoa` — raises likelihood, measured lift ×1.729 (weight +0.55)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - 2 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** prior_version_still_callable, still_holds_value_or_authority / unmaintained_or_differing_code_path, not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `EOA_SINGLE_KEY`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#apeswap-amm|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#apeswap-amm`
- **Disclosure:** https://www.ape.bond/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://apeswap.gitbook.io/apeswap-finance/security/audits

### 47. Revault  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking B — likelihood, ignoring actionability):** 47
- **Protocol:** Revault (`revault`) · Yield · Binance
- **DefiLlama:** https://defillama.com/protocol/revault
- **PRIORITY 40.93**  =  LIKELIHOOD 48.15 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 16.25/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $2,076,308 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`RevaChef` @ 0xdc0df7a0…(bsc)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for RevaChef@0xdc0df7a0…(bsc); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a timelock with a real delay** (`TIMELOCK`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#revault|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#revault`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://paladinsec.co/projects/revault-network/, https://www.certik.org/projects/revault

### 48. Silo V1  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 48
- **Protocol:** Silo V1 (`silo-v1`) · Lending · Arbitrum, Ethereum, Optimism, Base, Sonic
- **DefiLlama:** https://defillama.com/protocol/silo-v1
- **PRIORITY 40.71**  =  LIKELIHOOD 47.9 × ACTIONABILITY 85.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 21.5/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,453,111 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `unverified_implementation` — raises likelihood, measured lift ×2.007 (weight +0.70)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `version_sibling_legacy` — raises likelihood, measured lift ×1.699 (weight +0.53)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - Conditions: `VERSION_SIBLING_LEGACY`
    - condition VERSION_SIBLING_LEGACY (PRECOND): Shares a parent protocol with a higher-version sibling while still holding value: the classic sibling-deployment-retains-the-old-version shape.
    - 3 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** prior_version_still_callable, still_holds_value_or_authority / unmaintained_or_differing_code_path, not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `EOA_SINGLE_KEY`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#silo-v1|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#silo-v1`
- **Disclosure:** https://app.silo.finance · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://drive.google.com/file/d/1D2EIOb0XaRov5Ph2AE0DTfIsMISd7UXG/view, https://drive.google.com/file/d/1WXaB3ICLv4rSEX86POK3-NaOIxXwyq9l/view

### 49. Royco V2  —  `ACC-NAV-SHAREPRICE-MANIPULABLE`

- **Rank (Ranking B — likelihood, ignoring actionability):** 49
- **Protocol:** Royco V2 (`royco-v2`) · Yield · Ethereum, Avalanche, Base, Arbitrum
- **DefiLlama:** https://defillama.com/protocol/royco-v2
- **PRIORITY 28.72**  =  LIKELIHOOD 47.87 × ACTIONABILITY 60.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 15.97/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $23,040,883 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
- **Broken invariant tested:** totalAssets() must equal value the vault could actually realise now. Any component valued at book, at a manipulable rate, or after economic impairment lets a redeemer convert other depositors' claims into their own.
    - Deployed source (`ConcreteAsyncVaultImpl` @ 0x1b5cd91e…(ethereum), `RoycoFactory` @ 0x34db2f42…(ethereum)): prerequisites matched: totalAssets_reads_balanceOf; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): totalAssets_defined=yes
    - deployed source read for ConcreteAsyncVaultImpl@0x1b5cd91e…(ethereum), RoycoFactory@0x34db2f42…(ethereum); indicators matched: totalAssets_reads_balanceOf, totalAssets_defined
    - 2 live contract(s) answer totalAssets()
- **Preconditions PRESENT / UNKNOWN:** src::totalAssets_reads_balanceOf, erc4626_style_totalAssets_live, live_pooled_depositor_value / multi_component_totalAssets
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Share price rate-limited per block (kills same-transaction extraction); Single-asset vault with no external valuation; Withdrawals queued with a delay and priced at settlement
- **Where to start:** On a fork, for each component, force its valuation to zero and to 10x; the vault's mint/redeem must revert or be bounded, never transfer more than the depositor's pro-rata realisable share.
- **Evidence:** `protocols/deep_screened.jsonl#royco-v2|ACC-NAV-SHAREPRICE-MANIPULABLE`, `protocols/onchain_probes.json#royco-v2`
- **Disclosure:** https://www.royco.org · no audit link listed

### 50. DeltaPrime  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking B — likelihood, ignoring actionability):** 50
- **Protocol:** DeltaPrime (`deltaprime`) · Leveraged Farming · Avalanche, Arbitrum
- **DefiLlama:** https://defillama.com/protocol/deltaprime
- **PRIORITY 40.55**  =  LIKELIHOOD 47.7 × ACTIONABILITY 85.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 10.8/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $3,648,228 · **Band:** `IN_BAND`
- **REPEAT VICTIM — 3 recorded hacks.** 2024-11-11 $4,800,000 [Missing Input Validation]; 2024-07-23 $1,000,000 [Ownership Takeover]
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
- **Broken invariant tested:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source (`BtcPoolTUP` @ 0x0ed7B42B…(arbitrum), `sPrimeUniswap` @ 0x3Ea9D480…(arbitrum)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for BtcPoolTUP@0x0ed7B42B…(arbitrum), sPrimeUniswap@0x3Ea9D480…(arbitrum); indicators matched: unsafe_cross_sign_cast
- **Preconditions PRESENT / UNKNOWN:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** safecast_used / none in the reviewed path
- **Prior art:** `UNREMEDIATED_KNOWN_ISSUE` — DefiLlama's hacks dataset records 2 prior on-chain incident(s) on this protocol, most recently 2024-11-11 for $4,800,000 [Missing Input Validation]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#deltaprime|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#deltaprime`
- **Disclosure:** https://deltaprime.io · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/DeltaPrimeLabs/deltaprime-primeloans/blob/main/audits/DeltaPrime-Review-Piotr-Szlachciak.pdf, https://github.com/DeltaPrimeLabs/deltaprime-primeloans/blob/main/audits/PeckShield-Audit-Report-DeltaPrime.pdf

### 54. Reflexer  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking B — likelihood, ignoring actionability):** 54
- **Protocol:** Reflexer (`reflexer`) · CDP · Ethereum
- **DefiLlama:** https://defillama.com/protocol/reflexer
- **PRIORITY 40.46**  =  LIKELIHOOD 47.6 × ACTIONABILITY 85.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 21.2/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $2,623,624 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - 3 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** prior_version_still_callable, still_holds_value_or_authority / unmaintained_or_differing_code_path, not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#reflexer|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#reflexer`
- **Disclosure:** https://reflexer.finance/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.reflexer.finance/risk/geb-risks

### 55. Chamber Vaults  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking B — likelihood, ignoring actionability):** 55
- **Protocol:** Chamber Vaults (`chamber-vaults`) · Indexes · Base, Optimism, Polygon, Hyperliquid L1, Arbitrum, Ethereum …
- **DefiLlama:** https://defillama.com/protocol/chamber-vaults
- **PRIORITY 28.56**  =  LIKELIHOOD 47.6 × ACTIONABILITY 60.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 15.7/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $23,648,490 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`GnosisSafeProxy` @ 0x813123a1…(ethereum), `DHedgeTokenProxy` @ 0xca120764…(ethereum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for GnosisSafeProxy@0x813123a1…(ethereum), DHedgeTokenProxy@0xca120764…(ethereum); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#chamber-vaults|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#chamber-vaults`
- **Disclosure:** https://chamberfi.com/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.dhedge.org/security/audits-timeline

### 56. Kinza Finance  —  `ORACLE-STALE-OR-SILENT-FALLBACK`

- **Rank (Ranking B — likelihood, ignoring actionability):** 56
- **Protocol:** Kinza Finance (`kinza-finance`) · Lending · Binance, Op_Bnb, Ethereum, Mantle
- **DefiLlama:** https://defillama.com/protocol/kinza-finance
- **PRIORITY 40.44**  =  LIKELIHOOD 47.58 × ACTIONABILITY 85.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 21.18/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $3,277,468 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 69.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
- **Broken invariant tested:** A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
    - Conditions: `FORK_OF_WINDOW_VICTIM`, `PRICING_SURFACE_UNDECLARED`
    - Deployed source (`KillSwitchToken` @ 0x070CaAea…(bsc)): no prerequisite matched; no guard found
    - RELEVANCE GATE: the contract(s) actually read (KillSwitchToken) show no distinguishing indicator for this family, so they are probably not the contracts that implement it. Every source-derived signal is therefore UNKNOWN, including the absence of a guard: not finding a staleness check in a data-provider contract says nothing about the oracle.
    - condition FORK_OF_WINDOW_VICTIM (LINEAGE): Forked from a protocol that was exploited inside the six-month window: the fork inherits the upstream defect until the patch is proven present in ITS deployed bytecode.
    - condition PRICING_SURFACE_UNDECLARED (PRIORITY): A lending, CDP, derivatives or curation archetype with no oracle declared at all: the pricing path is unmapped.
- **Preconditions PRESENT / UNKNOWN:** value_decision_reads_configured_feed, live_positions_exposed / feed_selection_is_configuration
- **Guards searched / found:** deviation_bound_vs_independent_source / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Where to start:** On a fork, force each configured feed to return zero, a stale timestamp, and a 10x/0.1x value; every value-bearing entrypoint must revert rather than transact.
- **Evidence:** `protocols/deep_screened.jsonl#kinza-finance|ORACLE-STALE-OR-SILENT-FALLBACK`, `protocols/onchain_probes.json#kinza-finance`
- **Disclosure:** https://app.kinza.finance · no audit link listed

### 57. Extra Finance Leverage Farming  —  `ACC-QUOTE-STALE-ACROSS-OWN-SWAP`

- **Rank (Ranking B — likelihood, ignoring actionability):** 57
- **Protocol:** Extra Finance Leverage Farming (`extra-finance-leverage-farming`) · Leveraged Farming · Base, Optimism, Berachain
- **DefiLlama:** https://defillama.com/protocol/extra-finance-leverage-farming
- **PRIORITY 28.46**  =  LIKELIHOOD 47.43 × ACTIONABILITY 60.0%
    - likelihood = family evidence 37.5/50 (MATCH 75.0 × evidence weight 1.0) + learned attack surface 9.93/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $24,987,646 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 75.0 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A value used for minting, crediting or reward must be derived from what the protocol actually received, not from a quote taken before the protocol itself moved the market. Where the protocol's own action changes the price it just read, the value must be recomputed after the fact.
    - Deployed source (`VaultFactory` @ 0x155620a2…(base), `LendingPool` @ 0xBB505c54…(base)): prerequisites matched: quote_then_own_swap, quote_then_addliquidity; guards found: twap_or_feed_for_accounting
    - weak/ambiguous source indicators (ordering only, never scored): referral_reward_with_mint=yes
    - deployed source read for VaultFactory@0x155620a2…(base), LendingPool@0xBB505c54…(base); indicators matched: quote_then_own_swap, quote_then_addliquidity, twap_or_feed_for_accounting, referral_reward_with_mint
- **Preconditions PRESENT / UNKNOWN:** src::quote_then_own_swap, src::quote_then_addliquidity, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** lp_delta_measured, twap_or_feed_for_accounting / twap_or_feed_for_accounting
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** The minted amount is derived from the LP balance delta or from a TWAP (kills the pair); The protocol's swap is bounded so it cannot move reserves materially; Rewards settle in a later block against re-measured backing
- **Where to start:** On a fork, run the bonding path with a flash-funded swap sized to skew the pair, then assert that the minted or credited amount tracks the LP tokens actually received rather than the pre-swap quote.
- **Evidence:** `protocols/deep_screened.jsonl#extra-finance-leverage-farming|ACC-QUOTE-STALE-ACROSS-OWN-SWAP`, `protocols/onchain_probes.json#extra-finance-leverage-farming`
- **Disclosure:** https://app.extrafi.io/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.extrafi.io/extra_finance/audits-and-security
