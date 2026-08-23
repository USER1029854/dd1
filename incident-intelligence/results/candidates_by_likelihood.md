# Candidates — Ranking B — likelihood of being attacked

> **Discovery-stage output.** This file asserts no defect in any protocol named below. Each entry is a *high-priority defensive review candidate*: the named evidence matches a family's prerequisites, the named evidence is unknown, and the named guard would falsify it. Everything requires separate authorized verification on a local or pinned fork before any conclusion is drawn.

**Who this list is for.** An independent reviewer who wants to prevent real losses, not a fund allocating audit retainers. The band is $50,000 to $30,000,000: below that there is nothing worth saving, and above it protocols are assumed to carry dedicated professional coverage, so they are dropped unless specific danger evidence says otherwise.

**Why exposure does not drive this ranking.** In this run's own corpus of 128 on-chain incidents, the median loss was $252,000 and 84% cost under $2,000,000. Only 5% exceeded $10,000,000. Size is a poor predictor of being attacked; neglect and segment are far better ones.

Score = family evidence (0-40, weighted by how deeply the evidence was actually read) + empirical segment hazard (0-25) + attention deficit (0-25) + attacker economics (0-10).

### Family spread in this list

| Family | Candidates |
|---|---:|
| `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY` | 21 |
| `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 6 |
| `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 4 |
| `UPGRADE-INITIALIZER-REACHABLE-LIVE` | 4 |
| `ORACLE-SPOT-THIN-LIQUIDITY` | 2 |
| `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | 2 |
| `ACC-DONATION-UNACCOUNTED-BALANCE` | 1 |
| `AUTH-ZERO-ADDRESS-ACCEPTED` | 1 |
| `SIG-VERIFIER-DEFEATABLE` | 1 |
| `ORACLE-STALE-OR-SILENT-FALLBACK` | 1 |
| `ACC-CREDIT-NOT-RECEIVED` | 1 |
| `ACC-DUPLICATE-ID-ACCUMULATION` | 1 |

`UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY` dominates because a deprecated deployment that still holds value is both the most neglected shape and the one read-only evidence establishes most cleanly. That is an honest reflection of where the cheap wins are, not a modelling artefact.

### Diversified shortlist — top 3 per family

Use this if you would rather work a spread of hypothesis types than a run of one. Same scoring, just capped at three candidates per family.

| # | Protocol | Family | HACK_LIKELIHOOD | Value at risk | Category | Evidence |
|---:|---|---|---:|---:|---|---|
| 1 | [OrderNChaos](https://defillama.com/protocol/ordernchaos) | `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY` | 69.36 | $60,547 | Algo-Stables | `L3_STATE` |
| 2 | [Sumer.money](https://defillama.com/protocol/sumer.money) | `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY` | 67.61 | $1,222,366 | Lending | `L4_GUARD_REVIEW` |
| 3 | [Cub Finance](https://defillama.com/protocol/cub-finance) | `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY` | 67.56 | $212,149 | Farm | `L3_STATE` |
| 4 | [ApeRocket](https://defillama.com/protocol/aperocket) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 67.28 | $967,273 | Yield | `L4_GUARD_REVIEW` |
| 5 | [Percent Finance](https://defillama.com/protocol/percent-finance) | `AUTH-ZERO-ADDRESS-ACCEPTED` | 66.89 | $84,758 | Lending | `L4_GUARD_REVIEW` |
| 6 | [Velvet V2](https://defillama.com/protocol/velvet-v2) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 66.55 | $351,092 | Indexes | `L4_GUARD_REVIEW` |
| 7 | [Zero Network](https://defillama.com/protocol/zero-network) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 66.19 | $563,158 | Canonical Bridge | `L4_GUARD_REVIEW` |
| 8 | [UwU Lend](https://defillama.com/protocol/uwu-lend) | `ORACLE-SPOT-THIN-LIQUIDITY` | 64.89 | $156,312 | Lending | `L4_GUARD_REVIEW` |
| 9 | [Charm Finance V1](https://defillama.com/protocol/charm-finance-v1) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 64.87 | $318,239 | Liquidity Manager | `L4_GUARD_REVIEW` |
| 10 | [Arcade.xyz](https://defillama.com/protocol/arcade.xyz) | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | 64.4 | $210,561 | NFT Lending | `L4_GUARD_REVIEW` |
| 11 | [Fungify](https://defillama.com/protocol/fungify) | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | 64.37 | $131,456 | Lending | `L4_GUARD_REVIEW` |
| 12 | [Guru Network Classic](https://defillama.com/protocol/guru-network-classic) | `ORACLE-SPOT-THIN-LIQUIDITY` | 64.28 | $1,888,996 | Yield | `L4_GUARD_REVIEW` |
| 13 | [Stargate V1](https://defillama.com/protocol/stargate-v1) | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | 63.39 | $10,725,483 | Cross Chain Bridge | `L4_GUARD_REVIEW` |
| 14 | [ValueDefi](https://defillama.com/protocol/valuedefi) | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | 63.14 | $467,702 | Dexs | `L4_GUARD_REVIEW` |
| 15 | [Contango V1](https://defillama.com/protocol/contango-v1) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 62.91 | $290,609 | Derivatives | `L4_GUARD_REVIEW` |
| 16 | [Caviar V1](https://defillama.com/protocol/caviar-v1) | `AUTH-ZERO-ADDRESS-ACCEPTED` | 62.19 | $61,437 | NFT Marketplace | `L4_GUARD_REVIEW` |
| 17 | [GoPlus Locker V2](https://defillama.com/protocol/goplus-locker-v2) | `ACC-CREDIT-NOT-RECEIVED` | 61.91 | $419,406 | Token Locker | `L4_GUARD_REVIEW` |
| 18 | [DOOAR V2](https://defillama.com/protocol/dooar-v2) | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | 61.66 | $5,127,684 | Dexs | `L4_GUARD_REVIEW` |
| 19 | [Morpho Optimizer AaveV2](https://defillama.com/protocol/morpho-optimizer-aavev2) | `ORACLE-STALE-OR-SILENT-FALLBACK` | 61.27 | $138,237 | Lending | `L3_STATE` |
| 20 | [ArbiNYAN](https://defillama.com/protocol/arbinyan) | `ACC-DONATION-UNACCOUNTED-BALANCE` | 61.23 | $75,132 | Farm | `L3_STATE` |
| 21 | [Maverick V1](https://defillama.com/protocol/maverick-v1) | `ACC-DUPLICATE-ID-ACCUMULATION` | 61.14 | $1,064,242 | Dexs | `L4_GUARD_REVIEW` |
| 22 | [Strata Season 0](https://defillama.com/protocol/strata-season-0) | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | 60.76 | $189,859 | Farm | `L4_GUARD_REVIEW` |
| 23 | [Kinza Finance](https://defillama.com/protocol/kinza-finance) | `ORACLE-STALE-OR-SILENT-FALLBACK` | 60.69 | $3,277,468 | Lending | `L3_STATE` |
| 24 | [Midas Capital](https://defillama.com/protocol/midas-capital) | `AUTH-ZERO-ADDRESS-ACCEPTED` | 60.61 | $103,382 | Lending | `L4_GUARD_REVIEW` |
| 25 | [Tarot](https://defillama.com/protocol/tarot) | `ORACLE-SPOT-THIN-LIQUIDITY` | 60.61 | $583,969 | Lending | `L4_GUARD_REVIEW` |
| 26 | [WePiggy](https://defillama.com/protocol/wepiggy) | `ACC-DONATION-UNACCOUNTED-BALANCE` | 60.09 | $802,765 | Lending | `L4_GUARD_REVIEW` |
| 27 | [deBridge](https://defillama.com/protocol/debridge) | `ACC-DUPLICATE-ID-ACCUMULATION` | 59.91 | $1,907,281 | Bridge | `L4_GUARD_REVIEW` |
| 28 | [ShimmerBridge](https://defillama.com/protocol/shimmerbridge) | `ACC-DONATION-UNACCOUNTED-BALANCE` | 59.69 | $180,287 | Bridge | `L3_STATE` |
| 29 | [LandX Finance](https://defillama.com/protocol/landx-finance) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 59.14 | $1,578,688 | RWA | `L4_GUARD_REVIEW` |
| 30 | [Goose Finance](https://defillama.com/protocol/goose-finance) | `ACC-NAV-SHAREPRICE-MANIPULABLE` | 59.02 | $318,137 | Farm | `L1_ADAPTER` |

---

### 1. OrderNChaos  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking B — likelihood of being attacked):** 1
- **Protocol:** OrderNChaos (`ordernchaos`) · Algo-Stables · Arbitrum, Avalanche, Binance, zkSync Era, Kava
- **DefiLlama URL:** https://defillama.com/protocol/ordernchaos
- **Value at risk (TVL):** $60,547  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
- **HACK_LIKELIHOOD: 69.36 / 100**
    - family evidence 21.6/40 (MATCH 60 × evidence-level weight 0.9) · hazard 24.76/25 · neglect 13/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 60 / 100 · **EVIDENCE_CONFIDENCE:** 77.0 / 100 · **Evidence level:** `L3_STATE`
- **Why this segment gets hit:** chain hazard ×3.61, category hazard ×13.2. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 13/25):**
    - `no_audit_listed` (+7) — no audit link listed by DefiLlama
    - `dead_front_end` (+6) — front end is dead while contracts still hold value
- **Broken invariant this family tests:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - Conditions observed: `DEAD_FRONTEND_FUNDED`
    - condition DEAD_FRONTEND_FUNDED (PRECOND): Front end is dead while contracts still hold value: nobody is watching the deployment that still holds funds.
    - 1 address(es) still hold deployed code on-chain
- **Preconditions PRESENT:** unmaintained_or_differing_code_path, prior_version_still_callable, still_holds_value_or_authority
- **Preconditions UNKNOWN:** not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#ordernchaos|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#ordernchaos`, `families/families.json#UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
- **Disclosure channel:** not listed · no audit link listed

### 2. Sumer.money  —  `ACC-DONATION-UNACCOUNTED-BALANCE`

- **Rank (Ranking B — likelihood of being attacked):** 2
- **Protocol:** Sumer.money (`sumer.money`) · Lending · Berachain, CORE, Meter, Arbitrum, Goat, Base …
- **DefiLlama URL:** https://defillama.com/protocol/sumer.money
- **Value at risk (TVL):** $1,222,366  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
- **HACK_LIKELIHOOD: 69.09 / 100**
    - family evidence 31.0/40 (MATCH 77.5 × evidence-level weight 1.0) · hazard 14.09/25 · neglect 15/25 · attacker economics 9.0/10
- **MATCH_SCORE:** 77.5 / 100 · **EVIDENCE_CONFIDENCE:** 90.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×3.61, category hazard ×1.49. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 15/25):**
    - `single_audit_only` (+2) — a single audit listed, with no indication it covers the current deployment
    - `dead_front_end` (+6) — front end is dead while contracts still hold value
    - `warning_banner` (+3) — DefiLlama displays a warning banner
    - `sharp_outflow` (+4) — TVL fell sharply over the last week, the abandonment signature
- **Broken invariant this family tests:** A share price, exchange rate or totalAssets must be a function of value the protocol accounted for on entry. Reading a raw balance makes any direct transfer into the accounting boundary an unpriced increase in every holder's claim.
    - Deployed source read (`CErc20Immutable` @ 0x004c0908…(ethereum), `TransparentUpgradeableProxy` @ 0x02451015…(ethereum)): prerequisites matched: getCashPrior_balanceOf; no guard found
    - deployed source read for CErc20Immutable@0x004c0908…(ethereum), TransparentUpgradeableProxy@0x02451015…(ethereum); indicators matched: getCashPrior_balanceOf
    - market implementation(s) resolved: CErc20
    - 4 live market(s) read on-chain
- **Preconditions PRESENT:** src::getCashPrior_balanceOf, rate_reads_raw_balance, unprivileged_inbound_transfer_possible, inflated_rate_consumed_by_value_decision, third_party_claims_exposed
- **Preconditions UNKNOWN:** src::totalAssets_reads_balanceOf
- **Guards searched / found:** internal_cash_counter / none found in the reviewed path
- **Prior-art status:** `KNOWN_ISSUE_DEPLOYMENT_STATUS_UNKNOWN` — The Compound-fork donation/exchange-rate vector is publicly documented and was raised in Venus's own Code4rena audit before the March 2026 THE-market exploit. Whether THIS deployment carries a fix is not established by read-only evidence.
- **What would falsify this:** totalAssets derived from an internal counter, not balanceOf (kills the pair); Rate is monotonic and rate-limited per block; Inbound transfers to the accounting boundary are rejected or swept to a reserve
- **Where to start:** On a fork, transfer an arbitrary amount of each counted asset directly into every accounting boundary; the share price, exchange rate and derived borrow power must not change.
- **Evidence:** `protocols/deep_screened.jsonl#sumer.money|ACC-DONATION-UNACCOUNTED-BALANCE`, `protocols/onchain_probes.json#sumer.money`, `families/families.json#ACC-DONATION-UNACCOUNTED-BALANCE`
- **Disclosure channel:** not listed · audits: https://docs.sumer.money/security/audits

### 3. Cub Finance  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking B — likelihood of being attacked):** 3
- **Protocol:** Cub Finance (`cub-finance`) · Farm · Binance
- **DefiLlama URL:** https://defillama.com/protocol/cub-finance
- **Value at risk (TVL):** $212,149  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
    - Corroborating danger signals: condition FORK_OF_WINDOW_VICTIM
- **HACK_LIKELIHOOD: 67.56 / 100**
    - family evidence 21.6/40 (MATCH 60 × evidence-level weight 0.9) · hazard 24.96/25 · neglect 11/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 60 / 100 · **EVIDENCE_CONFIDENCE:** 77.0 / 100 · **Evidence level:** `L3_STATE`
- **Why this segment gets hit:** chain hazard ×3.61, category hazard ×13.74. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 11/25):**
    - `single_audit_only` (+2) — a single audit listed, with no indication it covers the current deployment
    - `fork_of_window_victim` (+6) — forked from a protocol exploited inside the window
    - `no_timelock_in_source` (+3) — no timelock construct found in the source that was read
- **Broken invariant this family tests:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - 4 address(es) still hold deployed code on-chain
- **Preconditions PRESENT:** prior_version_still_callable, still_holds_value_or_authority
- **Preconditions UNKNOWN:** unmaintained_or_differing_code_path, not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#cub-finance|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#cub-finance`, `families/families.json#UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
- **Disclosure channel:** https://cubdefi.com · audits: https://www.certik.org/projects/cubfinance

### 4. ArbiNYAN  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking B — likelihood of being attacked):** 4
- **Protocol:** ArbiNYAN (`arbinyan`) · Farm · Arbitrum
- **DefiLlama URL:** https://defillama.com/protocol/arbinyan
- **Value at risk (TVL):** $75,132  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
- **HACK_LIKELIHOOD: 67.53 / 100**
    - family evidence 21.6/40 (MATCH 60 × evidence-level weight 0.9) · hazard 19.93/25 · neglect 16/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 60 / 100 · **EVIDENCE_CONFIDENCE:** 77.0 / 100 · **Evidence level:** `L3_STATE`
- **Why this segment gets hit:** chain hazard ×1.29, category hazard ×13.74. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 16/25):**
    - `no_audit_listed` (+7) — no audit link listed by DefiLlama
    - `dead_front_end` (+6) — front end is dead while contracts still hold value
    - `misrepresented_tokens` (+3) — DefiLlama cannot reconcile this protocol's reported token holdings
- **Broken invariant this family tests:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - Conditions observed: `DEAD_FRONTEND_FUNDED`
    - condition DEAD_FRONTEND_FUNDED (PRECOND): Front end is dead while contracts still hold value: nobody is watching the deployment that still holds funds.
    - 1 address(es) still hold deployed code on-chain
- **Preconditions PRESENT:** unmaintained_or_differing_code_path, prior_version_still_callable, still_holds_value_or_authority
- **Preconditions UNKNOWN:** not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#arbinyan|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#arbinyan`, `families/families.json#UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
- **Disclosure channel:** not listed · no audit link listed

### 5. ApeRocket  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking B — likelihood of being attacked):** 5
- **Protocol:** ApeRocket (`aperocket`) · Yield · Binance
- **DefiLlama URL:** https://defillama.com/protocol/aperocket
- **Value at risk (TVL):** $967,273  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
    - Corroborating danger signals: an implementation behind a live proxy is unverified on the explorer
- **HACK_LIKELIHOOD: 67.28 / 100**
    - family evidence 24.0/40 (MATCH 60 × evidence-level weight 1.0) · hazard 12.28/25 · neglect 21/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 60 / 100 · **EVIDENCE_CONFIDENCE:** 85.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×3.61, category hazard ×1.03. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 21/25):**
    - `single_audit_only` (+2) — a single audit listed, with no indication it covers the current deployment
    - `dead_front_end` (+6) — front end is dead while contracts still hold value
    - `misrepresented_tokens` (+3) — DefiLlama cannot reconcile this protocol's reported token holdings
    - `unverified_implementation` (+7) — an implementation behind a proxy is unverified on the explorer
    - `no_timelock_in_source` (+3) — no timelock construct found in the source that was read
- **Broken invariant this family tests:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source read (`RocketVault` @ 0x80657d8b…(bsc)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for RocketVault@0x80657d8b…(bsc); indicators matched: claim_without_eligibility_map
    - 1 implementation(s) behind a proxy are NOT verified on the explorer: implementation identity unresolved, score capped at 60
- **Preconditions PRESENT:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain
- **Preconditions UNKNOWN:** none
- **Guards searched / found:** merkle_proof_gate / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#aperocket|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#aperocket`, `families/families.json#AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`
- **Disclosure channel:** not listed · audits: https://github.com/peckshield/publications/blob/master/audit_reports/PeckShield-Audit-Report-ApeRocket-v1.0.pdf

### 6. Percent Finance  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking B — likelihood of being attacked):** 6
- **Protocol:** Percent Finance (`percent-finance`) · Lending · Ethereum
- **DefiLlama URL:** https://defillama.com/protocol/percent-finance
- **Value at risk (TVL):** $84,758  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
    - Corroborating danger signals: a deployed-source pair already scores 73.8 at L4 guard review
- **HACK_LIKELIHOOD: 66.89 / 100**
    - family evidence 25.52/40 (MATCH 63.8 × evidence-level weight 1.0) · hazard 12.37/25 · neglect 19/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 63.8 / 100 · **EVIDENCE_CONFIDENCE:** 85.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×2.54, category hazard ×1.49. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 19/25):**
    - `no_audit_listed` (+7) — no audit link listed by DefiLlama
    - `dead_front_end` (+6) — front end is dead while contracts still hold value
    - `misrepresented_tokens` (+3) — DefiLlama cannot reconcile this protocol's reported token holdings
    - `no_timelock_in_source` (+3) — no timelock construct found in the source that was read
- **Broken invariant this family tests:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source read (`PctPool` @ 0x0190bF68…(ethereum), `PctPool` @ 0x23b53026…(ethereum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for PctPool@0x0190bF68…(ethereum), PctPool@0x23b53026…(ethereum); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain
- **Preconditions UNKNOWN:** none
- **Guards searched / found:** none / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#percent-finance|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#percent-finance`, `families/families.json#AUTH-ZERO-ADDRESS-ACCEPTED`
- **Disclosure channel:** not listed · no audit link listed

### 7. Velvet V2  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking B — likelihood of being attacked):** 7
- **Protocol:** Velvet V2 (`velvet-v2`) · Indexes · Binance, Arbitrum
- **DefiLlama URL:** https://defillama.com/protocol/velvet-v2
- **Value at risk (TVL):** $351,092  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
    - Corroborating danger signals: a deployed-source pair already scores 73.8 at L4 guard review
- **HACK_LIKELIHOOD: 66.55 / 100**
    - family evidence 29.52/40 (MATCH 73.8 × evidence-level weight 1.0) · hazard 13.03/25 · neglect 14/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 73.8 / 100 · **EVIDENCE_CONFIDENCE:** 90.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×3.61, category hazard ×1.2. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 14/25):**
    - `no_audit_listed` (+7) — no audit link listed by DefiLlama
    - `version_sibling_legacy` (+4) — a version sibling of a newer deployment still holds value
    - `no_timelock_in_source` (+3) — no timelock construct found in the source that was read
- **Broken invariant this family tests:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source read (`IndexFactory` @ 0x286a97cf…(bsc)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for IndexFactory@0x286a97cf…(bsc); indicators matched: unsafe_cross_sign_cast
- **Preconditions PRESENT:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain
- **Preconditions UNKNOWN:** none
- **Guards searched / found:** safecast_used / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#velvet-v2|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#velvet-v2`, `families/families.json#ACC-SIGN-OR-BOUND-CHECK-MISSING`
- **Disclosure channel:** https://dapp.velvet.capital/Referred/6956901b440d4fc522b2eb7b · no audit link listed

### 8. Cega V1  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking B — likelihood of being attacked):** 8
- **Protocol:** Cega V1 (`cega-v1`) · Options · Solana, Ethereum, Arbitrum
- **DefiLlama URL:** https://defillama.com/protocol/cega-v1
- **Value at risk (TVL):** $308,235  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
    - Corroborating danger signals: a deployed-source pair already scores 73.8 at L4 guard review
- **HACK_LIKELIHOOD: 66.34 / 100**
    - family evidence 21.6/40 (MATCH 60 × evidence-level weight 0.9) · hazard 14.74/25 · neglect 20/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 60 / 100 · **EVIDENCE_CONFIDENCE:** 77.0 / 100 · **Evidence level:** `L3_STATE`
- **Why this segment gets hit:** chain hazard ×2.54, category hazard ×2.42. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 20/25):**
    - `no_audit_listed` (+7) — no audit link listed by DefiLlama
    - `dead_front_end` (+6) — front end is dead while contracts still hold value
    - `version_sibling_legacy` (+4) — a version sibling of a newer deployment still holds value
    - `no_timelock_in_source` (+3) — no timelock construct found in the source that was read
- **Broken invariant this family tests:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - Conditions observed: `VERSION_SIBLING_LEGACY`, `DEAD_FRONTEND_FUNDED`
    - condition DEAD_FRONTEND_FUNDED (PRECOND): Front end is dead while contracts still hold value: nobody is watching the deployment that still holds funds.
    - condition VERSION_SIBLING_LEGACY (PRECOND): Shares a parent protocol with a higher-version sibling while still holding value: the classic sibling-deployment-retains-the-old-version shape.
    - 7 address(es) still hold deployed code on-chain
- **Preconditions PRESENT:** unmaintained_or_differing_code_path, prior_version_still_callable, still_holds_value_or_authority
- **Preconditions UNKNOWN:** not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#cega-v1|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#cega-v1`, `families/families.json#UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
- **Disclosure channel:** not listed · no audit link listed

### 9. Zero Network  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking B — likelihood of being attacked):** 9
- **Protocol:** Zero Network (`zero-network`) · Canonical Bridge · Ethereum
- **DefiLlama URL:** https://defillama.com/protocol/zero-network
- **Value at risk (TVL):** $563,158  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
- **HACK_LIKELIHOOD: 66.19 / 100**
    - family evidence 29.52/40 (MATCH 73.8 × evidence-level weight 1.0) · hazard 16.67/25 · neglect 10/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 73.8 / 100 · **EVIDENCE_CONFIDENCE:** 90.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×2.54, category hazard ×3.59. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 10/25):**
    - `no_audit_listed` (+7) — no audit link listed by DefiLlama
    - `no_timelock_in_source` (+3) — no timelock construct found in the source that was read
- **Broken invariant this family tests:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source read (`L1NativeTokenVault` @ 0x2fc2a2db…(ethereum), `TransparentUpgradeableProxy` @ 0x996d67aa…(ethereum)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for L1NativeTokenVault@0x2fc2a2db…(ethereum), TransparentUpgradeableProxy@0x996d67aa…(ethereum); indicators matched: unsafe_cross_sign_cast
- **Preconditions PRESENT:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain
- **Preconditions UNKNOWN:** none
- **Guards searched / found:** safecast_used / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#zero-network|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#zero-network`, `families/families.json#ACC-SIGN-OR-BOUND-CHECK-MISSING`
- **Disclosure channel:** https://zero.network/ · no audit link listed

### 10. Caviar V1  —  `SIG-VERIFIER-DEFEATABLE`

- **Rank (Ranking B — likelihood of being attacked):** 10
- **Protocol:** Caviar V1 (`caviar-v1`) · NFT Marketplace · Ethereum
- **DefiLlama URL:** https://defillama.com/protocol/caviar-v1
- **Value at risk (TVL):** $61,437  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
    - Corroborating danger signals: a deployed-source pair already scores 73.8 at L4 guard review
- **HACK_LIKELIHOOD: 66.19 / 100**
    - family evidence 29.52/40 (MATCH 73.8 × evidence-level weight 1.0) · hazard 8.67/25 · neglect 18/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 73.8 / 100 · **EVIDENCE_CONFIDENCE:** 90.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×2.54, category hazard ×0.7. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 18/25):**
    - `single_audit_only` (+2) — a single audit listed, with no indication it covers the current deployment
    - `dead_front_end` (+6) — front end is dead while contracts still hold value
    - `version_sibling_legacy` (+4) — a version sibling of a newer deployment still holds value
    - `misrepresented_tokens` (+3) — DefiLlama cannot reconcile this protocol's reported token holdings
    - `no_timelock_in_source` (+3) — no timelock construct found in the source that was read
- **Broken invariant this family tests:** A verification routine must reject malformed, empty or zero-recovered signatures, and must never treat address(0) as a match.
    - Deployed source read (`Caviar` @ 0xa964d6e8…(ethereum)): prerequisites matched: ecrecover_without_zero_check; no guard found
    - deployed source read for Caviar@0xa964d6e8…(ethereum); indicators matched: ecrecover_without_zero_check
- **Preconditions PRESENT:** src::ecrecover_without_zero_check, live_value_present, deployment_reachable_on_chain
- **Preconditions UNKNOWN:** none
- **Guards searched / found:** uses_oz_ecdsa / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** OZ ECDSA library in the deployed bytecode (kills the ecrecover-zero shape); Signer address immutable and non-zero
- **Where to start:** On a fork, submit r=0,s=0,v=27 and an empty signature to every signature-gated entrypoint; all must revert.
- **Evidence:** `protocols/deep_screened.jsonl#caviar-v1|SIG-VERIFIER-DEFEATABLE`, `protocols/onchain_probes.json#caviar-v1`, `families/families.json#SIG-VERIFIER-DEFEATABLE`
- **Disclosure channel:** not listed · audits: https://code4rena.com/reports/2022-12-caviar

### 11. ShimmerBridge  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking B — likelihood of being attacked):** 11
- **Protocol:** ShimmerBridge (`shimmerbridge`) · Bridge · Ethereum, Avalanche, Binance, Optimism, Polygon, Arbitrum …
- **DefiLlama URL:** https://defillama.com/protocol/shimmerbridge
- **Value at risk (TVL):** $180,287  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
- **HACK_LIKELIHOOD: 65.99 / 100**
    - family evidence 21.6/40 (MATCH 60 × evidence-level weight 0.9) · hazard 18.39/25 · neglect 16/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 60 / 100 · **EVIDENCE_CONFIDENCE:** 77.0 / 100 · **Evidence level:** `L3_STATE`
- **Why this segment gets hit:** chain hazard ×3.61, category hazard ×3.59. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 16/25):**
    - `no_audit_listed` (+7) — no audit link listed by DefiLlama
    - `dead_front_end` (+6) — front end is dead while contracts still hold value
    - `misrepresented_tokens` (+3) — DefiLlama cannot reconcile this protocol's reported token holdings
- **Broken invariant this family tests:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - Conditions observed: `DEAD_FRONTEND_FUNDED`, `MULTICHAIN_VERSION_DRIFT`
    - condition DEAD_FRONTEND_FUNDED (PRECOND): Front end is dead while contracts still hold value: nobody is watching the deployment that still holds funds.
    - condition MULTICHAIN_VERSION_DRIFT (PRIORITY): Deployed across many chains, where per-chain deployments drift and the least-watched chain sets the risk.
    - 6 address(es) still hold deployed code on-chain
- **Preconditions PRESENT:** unmaintained_or_differing_code_path, prior_version_still_callable, still_holds_value_or_authority
- **Preconditions UNKNOWN:** not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#shimmerbridge|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#shimmerbridge`, `families/families.json#UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
- **Disclosure channel:** not listed · no audit link listed

### 12. dTRINITY dLEND  —  `ORACLE-STALE-OR-SILENT-FALLBACK`

- **Rank (Ranking B — likelihood of being attacked):** 12
- **Protocol:** dTRINITY dLEND (`dtrinity-dlend`) · Lending · Ethereum, Fraxtal, Sonic
- **DefiLlama URL:** https://defillama.com/protocol/dtrinity-dlend
- **Value at risk (TVL):** $912,100  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
    - Corroborating danger signals: condition FORK_OF_WINDOW_VICTIM; condition IS_WINDOW_VICTIM_STILL_LIVE
- **HACK_LIKELIHOOD: 65.97 / 100**
    - family evidence 21.6/40 (MATCH 60 × evidence-level weight 0.9) · hazard 12.37/25 · neglect 22/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 60 / 100 · **EVIDENCE_CONFIDENCE:** 69.0 / 100 · **Evidence level:** `L3_STATE`
- **Why this segment gets hit:** chain hazard ×2.54, category hazard ×1.49. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 22/25):**
    - `no_audit_listed` (+7) — no audit link listed by DefiLlama
    - `is_window_victim` (+6) — exploited inside the six-month window and still listed
    - `fork_of_window_victim` (+6) — forked from a protocol exploited inside the window
    - `no_timelock_in_source` (+3) — no timelock construct found in the source that was read
- **Broken invariant this family tests:** A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
    - Conditions observed: `FORK_OF_WINDOW_VICTIM`, `SINGLE_PRIMARY_ORACLE_NO_CROSSCHECK`
    - Deployed source read (`LendingPoolAddressesProviderRegistry` @ 0x0029B254…(ethereum), `LendingPoolAddressesProvider` @ 0x01b76559…(ethereum)): no prerequisite matched; no guard found
    - RELEVANCE GATE: the contract(s) actually read (LendingPoolAddressesProviderRegistry, LendingPoolAddressesProvider) show no distinguishing indicator for this family, so they are probably not the contracts that implement it. Every source-derived signal is therefore UNKNOWN, including the absence of a guard: not finding a staleness check in a data-provider contract says nothing about the oracle.
    - condition FORK_OF_WINDOW_VICTIM (LINEAGE): Forked from a protocol that was exploited inside the six-month window: the fork inherits the upstream defect until the patch is proven present in ITS deployed bytecode.
    - condition SINGLE_PRIMARY_ORACLE_NO_CROSSCHECK (PRIORITY): Exactly one declared oracle and no declared secondary, so no cross-source deviation bound is declared.
    - price oracle resolved on-chain: 0x01b76559… -> 0x8a4236f5ef…
- **Preconditions PRESENT:** value_decision_reads_configured_feed, feed_selection_is_configuration, oracle_contract_resolved_on_chain, live_positions_exposed
- **Preconditions UNKNOWN:** none
- **Guards searched / found:** deviation_bound_vs_independent_source / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Where to start:** On a fork, force each configured feed to return zero, a stale timestamp, and a 10x/0.1x value; every value-bearing entrypoint must revert rather than transact.
- **Evidence:** `protocols/deep_screened.jsonl#dtrinity-dlend|ORACLE-STALE-OR-SILENT-FALLBACK`, `protocols/onchain_probes.json#dtrinity-dlend`, `families/families.json#ORACLE-STALE-OR-SILENT-FALLBACK`
- **Disclosure channel:** https://app.dtrinity.org/dlend/lending-borrow/ · no audit link listed

### 13. Lixir Finance  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking B — likelihood of being attacked):** 13
- **Protocol:** Lixir Finance (`lixir-finance`) · Liquidity Manager · Ethereum
- **DefiLlama URL:** https://defillama.com/protocol/lixir-finance
- **Value at risk (TVL):** $94,902  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
    - Corroborating danger signals: condition IS_WINDOW_VICTIM_STILL_LIVE
- **HACK_LIKELIHOOD: 64.95 / 100**
    - family evidence 21.6/40 (MATCH 60 × evidence-level weight 0.9) · hazard 16.35/25 · neglect 17/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 60 / 100 · **EVIDENCE_CONFIDENCE:** 77.0 / 100 · **Evidence level:** `L3_STATE`
- **Why this segment gets hit:** chain hazard ×2.54, category hazard ×3.36. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 17/25):**
    - `single_audit_only` (+2) — a single audit listed, with no indication it covers the current deployment
    - `dead_front_end` (+6) — front end is dead while contracts still hold value
    - `is_window_victim` (+6) — exploited inside the six-month window and still listed
    - `no_timelock_in_source` (+3) — no timelock construct found in the source that was read
- **Broken invariant this family tests:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - Conditions observed: `DEAD_FRONTEND_FUNDED`
    - condition DEAD_FRONTEND_FUNDED (PRECOND): Front end is dead while contracts still hold value: nobody is watching the deployment that still holds funds.
    - 4 address(es) still hold deployed code on-chain
- **Preconditions PRESENT:** unmaintained_or_differing_code_path, prior_version_still_callable, still_holds_value_or_authority
- **Preconditions UNKNOWN:** not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#lixir-finance|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#lixir-finance`, `families/families.json#UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
- **Disclosure channel:** not listed · audits: https://lixir-finance.gitbook.io/lixir-doc/resources/security/audits

### 14. UwU Lend  —  `ORACLE-SPOT-THIN-LIQUIDITY`

- **Rank (Ranking B — likelihood of being attacked):** 14
- **Protocol:** UwU Lend (`uwu-lend`) · Lending · Ethereum
- **DefiLlama URL:** https://defillama.com/protocol/uwu-lend
- **Value at risk (TVL):** $156,312  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
- **HACK_LIKELIHOOD: 64.89 / 100**
    - family evidence 29.52/40 (MATCH 73.8 × evidence-level weight 1.0) · hazard 12.37/25 · neglect 13/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 73.8 / 100 · **EVIDENCE_CONFIDENCE:** 90.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×2.54, category hazard ×1.49. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 13/25):**
    - `no_audit_listed` (+7) — no audit link listed by DefiLlama
    - `dead_front_end` (+6) — front end is dead while contracts still hold value
- **Broken invariant this family tests:** Borrowing capacity, mint size, reward size or collateral value must not be derived from a price that a single actor can move within the manipulation window, and the value unlocked must never exceed the cost of moving that price.
    - Conditions observed: `PRICING_SURFACE_UNDECLARED`
    - Deployed source read (`MultiFeeDistributionV2` @ 0x0a7B2A21…(ethereum), `UniswapV2Pair` @ 0x3E04863D…(ethereum)): prerequisites matched: spot_without_twap; no guard found
    - deployed source read for MultiFeeDistributionV2@0x0a7B2A21…(ethereum), UniswapV2Pair@0x3E04863D…(ethereum); indicators matched: spot_without_twap
    - condition PRICING_SURFACE_UNDECLARED (PRIORITY): A lending, CDP, derivatives or curation archetype with no oracle declared at all: the pricing path is unmapped.
    - only one oracle (or none) is declared in DefiLlama metadata; this is a prioritisation signal about disclosure, not evidence that no cross-source deviation bound exists in code
    - declared oracles: none declared
- **Preconditions PRESENT:** src::spot_without_twap, value_decision_reads_configured_feed, live_positions_exposed
- **Preconditions UNKNOWN:** feed_selection_is_configuration
- **Guards searched / found:** twap_present, supply_cap_present, deviation_bound_vs_independent_source / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** All collateral priced by a deep aggregated feed with a deviation cap (kills the pair); Caps are set from measured venue depth and enforced on-chain; The action is sized from realised transfer amounts, so price is never an input
- **Where to start:** On a fork, execute a max-size flash-funded swap against every venue in the pricing path and assert that no value-bearing entrypoint changes its output beyond the configured deviation bound.
- **Evidence:** `protocols/deep_screened.jsonl#uwu-lend|ORACLE-SPOT-THIN-LIQUIDITY`, `protocols/onchain_probes.json#uwu-lend`, `families/families.json#ORACLE-SPOT-THIN-LIQUIDITY`
- **Disclosure channel:** not listed · no audit link listed

### 15. Charm Finance V1  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking B — likelihood of being attacked):** 15
- **Protocol:** Charm Finance V1 (`charm-finance-v1`) · Liquidity Manager · Ethereum
- **DefiLlama URL:** https://defillama.com/protocol/charm-finance-v1
- **Value at risk (TVL):** $318,239  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
    - Corroborating danger signals: a deployed-source pair already scores 73.8 at L4 guard review
- **HACK_LIKELIHOOD: 64.87 / 100**
    - family evidence 29.52/40 (MATCH 73.8 × evidence-level weight 1.0) · hazard 16.35/25 · neglect 9/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 73.8 / 100 · **EVIDENCE_CONFIDENCE:** 90.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×2.54, category hazard ×3.36. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 9/25):**
    - `single_audit_only` (+2) — a single audit listed, with no indication it covers the current deployment
    - `version_sibling_legacy` (+4) — a version sibling of a newer deployment still holds value
    - `no_timelock_in_source` (+3) — no timelock construct found in the source that was read
- **Broken invariant this family tests:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source read (`AlphaVault` @ 0x9bF7B46C…(ethereum)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for AlphaVault@0x9bF7B46C…(ethereum); indicators matched: unsafe_cross_sign_cast
- **Preconditions PRESENT:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain
- **Preconditions UNKNOWN:** none
- **Guards searched / found:** safecast_used / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#charm-finance-v1|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#charm-finance-v1`, `families/families.json#ACC-SIGN-OR-BOUND-CHECK-MISSING`
- **Disclosure channel:** https://charm.fi/ · audits: https://github.com/solidified-platform/audits/blob/master/Audit%20Report%20-%20Charm%20Finance%20%5B27.10.2020%5D.pdf

### 16. Arcade.xyz  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking B — likelihood of being attacked):** 16
- **Protocol:** Arcade.xyz (`arcade.xyz`) · NFT Lending · Ethereum
- **DefiLlama URL:** https://defillama.com/protocol/arcade.xyz
- **Value at risk (TVL):** $210,561  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
- **HACK_LIKELIHOOD: 64.4 / 100**
    - family evidence 34.0/40 (MATCH 85.0 × evidence-level weight 1.0) · hazard 12.4/25 · neglect 8/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 85.0 / 100 · **EVIDENCE_CONFIDENCE:** 90.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×2.54, category hazard ×1.5. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 8/25):**
    - `single_audit_only` (+2) — a single audit listed, with no indication it covers the current deployment
    - `dead_front_end` (+6) — front end is dead while contracts still hold value
- **Broken invariant this family tests:** After deployment, no caller may (re)establish ownership, admin, or implementation wiring. Initialization state must be provably consumed.
    - Deployed source read (`UniswapV2Pair` @ 0x06af8C35…(ethereum), `VaultFactory` @ 0x26936366…(ethereum)): prerequisites matched: initialize_without_modifier; no guard found
    - deployed source read for UniswapV2Pair@0x06af8C35…(ethereum), VaultFactory@0x26936366…(ethereum); indicators matched: initialize_without_modifier
    - 3/3 live proxies read a zero ERC-7201 Initializable slot (inconclusive alone: older OZ versions store the flag elsewhere)
- **Preconditions PRESENT:** src::initialize_without_modifier, upgradeable_architecture, initializer_flag_unset, live_value_or_approvals
- **Preconditions UNKNOWN:** none
- **Guards searched / found:** initializer_modifier_present, upgrade_timelocked / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Simulated re-initialization reverts (kills the pair); Contract is non-upgradeable and holds no approvals
- **Where to start:** Read the initialization slot on every live proxy/facet and simulate re-initialization from an unprivileged address; it must revert.
- **Evidence:** `protocols/deep_screened.jsonl#arcade.xyz|UPGRADE-INITIALIZER-REACHABLE-LIVE`, `protocols/onchain_probes.json#arcade.xyz`, `families/families.json#UPGRADE-INITIALIZER-REACHABLE-LIVE`
- **Disclosure channel:** not listed · audits: https://docs.arcade.xyz/docs/audit-reports

### 17. Fungify  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking B — likelihood of being attacked):** 17
- **Protocol:** Fungify (`fungify`) · Lending · Ethereum
- **DefiLlama URL:** https://defillama.com/protocol/fungify
- **Value at risk (TVL):** $131,456  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
- **HACK_LIKELIHOOD: 64.37 / 100**
    - family evidence 34.0/40 (MATCH 85.0 × evidence-level weight 1.0) · hazard 12.37/25 · neglect 8/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 85.0 / 100 · **EVIDENCE_CONFIDENCE:** 90.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×2.54, category hazard ×1.49. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 8/25):**
    - `single_audit_only` (+2) — a single audit listed, with no indication it covers the current deployment
    - `dead_front_end` (+6) — front end is dead while contracts still hold value
- **Broken invariant this family tests:** After deployment, no caller may (re)establish ownership, admin, or implementation wiring. Initialization state must be provably consumed.
    - Deployed source read (`CEtherDelegate` @ 0x8f005bf2…(ethereum), `Unitroller` @ 0xf9c70750…(ethereum)): prerequisites matched: initialize_without_modifier; no guard found
    - deployed source read for CEtherDelegate@0x8f005bf2…(ethereum), Unitroller@0xf9c70750…(ethereum); indicators matched: initialize_without_modifier
    - 2/2 live proxies read a zero ERC-7201 Initializable slot (inconclusive alone: older OZ versions store the flag elsewhere)
    - 1 proxy/proxies expose a non-zero owner()
- **Preconditions PRESENT:** src::initialize_without_modifier, upgradeable_architecture, initializer_flag_unset, live_value_or_approvals
- **Preconditions UNKNOWN:** none
- **Guards searched / found:** initializer_modifier_present, upgrade_timelocked / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Simulated re-initialization reverts (kills the pair); Contract is non-upgradeable and holds no approvals
- **Where to start:** Read the initialization slot on every live proxy/facet and simulate re-initialization from an unprivileged address; it must revert.
- **Evidence:** `protocols/deep_screened.jsonl#fungify|UPGRADE-INITIALIZER-REACHABLE-LIVE`, `protocols/onchain_probes.json#fungify`, `families/families.json#UPGRADE-INITIALIZER-REACHABLE-LIVE`
- **Disclosure channel:** not listed · audits: https://docs.fungify.it/governance/security

### 18. Dopple Finance  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking B — likelihood of being attacked):** 18
- **Protocol:** Dopple Finance (`dopple-finance`) · Algo-Stables · Binance, Harmony, Fantom
- **DefiLlama URL:** https://defillama.com/protocol/dopple-finance
- **Value at risk (TVL):** $163,128  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
- **HACK_LIKELIHOOD: 64.36 / 100**
    - family evidence 21.6/40 (MATCH 60 × evidence-level weight 0.9) · hazard 24.76/25 · neglect 8/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 60 / 100 · **EVIDENCE_CONFIDENCE:** 77.0 / 100 · **Evidence level:** `L3_STATE`
- **Why this segment gets hit:** chain hazard ×3.61, category hazard ×13.2. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 8/25):**
    - `single_audit_only` (+2) — a single audit listed, with no indication it covers the current deployment
    - `dead_front_end` (+6) — front end is dead while contracts still hold value
- **Broken invariant this family tests:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - Conditions observed: `DEAD_FRONTEND_FUNDED`
    - condition DEAD_FRONTEND_FUNDED (PRECOND): Front end is dead while contracts still hold value: nobody is watching the deployment that still holds funds.
    - 2 address(es) still hold deployed code on-chain
- **Preconditions PRESENT:** unmaintained_or_differing_code_path, prior_version_still_callable, still_holds_value_or_authority
- **Preconditions UNKNOWN:** not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#dopple-finance|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#dopple-finance`, `families/families.json#UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
- **Disclosure channel:** not listed · audits: https://dopple.gitbook.io/dopple-finance/certik-audit

### 19. Finext Finance  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking B — likelihood of being attacked):** 19
- **Protocol:** Finext Finance (`finext-finance`) · Algo-Stables · Arbitrum
- **DefiLlama URL:** https://defillama.com/protocol/finext-finance
- **Value at risk (TVL):** $61,140  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
- **HACK_LIKELIHOOD: 64.33 / 100**
    - family evidence 21.6/40 (MATCH 60 × evidence-level weight 0.9) · hazard 19.73/25 · neglect 13/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 60 / 100 · **EVIDENCE_CONFIDENCE:** 77.0 / 100 · **Evidence level:** `L3_STATE`
- **Why this segment gets hit:** chain hazard ×1.29, category hazard ×13.2. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 13/25):**
    - `no_audit_listed` (+7) — no audit link listed by DefiLlama
    - `dead_front_end` (+6) — front end is dead while contracts still hold value
- **Broken invariant this family tests:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - Conditions observed: `DEAD_FRONTEND_FUNDED`
    - condition DEAD_FRONTEND_FUNDED (PRECOND): Front end is dead while contracts still hold value: nobody is watching the deployment that still holds funds.
    - 1 address(es) still hold deployed code on-chain
- **Preconditions PRESENT:** unmaintained_or_differing_code_path, prior_version_still_callable, still_holds_value_or_authority
- **Preconditions UNKNOWN:** not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#finext-finance|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#finext-finance`, `families/families.json#UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
- **Disclosure channel:** not listed · no audit link listed

### 20. Guru Network Classic  —  `ORACLE-SPOT-THIN-LIQUIDITY`

- **Rank (Ranking B — likelihood of being attacked):** 20
- **Protocol:** Guru Network Classic (`guru-network-classic`) · Yield · Binance, Sonic, MultiVAC, Fantom, Arbitrum, Kucoin …
- **DefiLlama URL:** https://defillama.com/protocol/guru-network-classic
- **Value at risk (TVL):** $1,888,996  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
- **HACK_LIKELIHOOD: 64.28 / 100**
    - family evidence 25.0/40 (MATCH 62.5 × evidence-level weight 1.0) · hazard 12.28/25 · neglect 18/25 · attacker economics 9.0/10
- **MATCH_SCORE:** 62.5 / 100 · **EVIDENCE_CONFIDENCE:** 90.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×3.61, category hazard ×1.03. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 18/25):**
    - `no_audit_listed` (+7) — no audit link listed by DefiLlama
    - `dead_front_end` (+6) — front end is dead while contracts still hold value
    - `rebranded` (+2) — operated under previous names, so old contracts may still be live
    - `misrepresented_tokens` (+3) — DefiLlama cannot reconcile this protocol's reported token holdings
- **Broken invariant this family tests:** Borrowing capacity, mint size, reward size or collateral value must not be derived from a price that a single actor can move within the manipulation window, and the value unlocked must never exceed the cost of moving that price.
    - Deployed source read (`tvlGuru` @ 0xD600Ec98…(bsc)): prerequisites matched: spot_without_twap; no guard found
    - deployed source read for tvlGuru@0xD600Ec98…(bsc); indicators matched: spot_without_twap
    - only one oracle (or none) is declared in DefiLlama metadata; this is a prioritisation signal about disclosure, not evidence that no cross-source deviation bound exists in code
    - declared oracles: Band (types: Primary)
- **Preconditions PRESENT:** src::spot_without_twap, live_positions_exposed
- **Preconditions UNKNOWN:** value_decision_reads_configured_feed, feed_selection_is_configuration
- **Guards searched / found:** twap_present, supply_cap_present, deviation_bound_vs_independent_source / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** All collateral priced by a deep aggregated feed with a deviation cap (kills the pair); Caps are set from measured venue depth and enforced on-chain; The action is sized from realised transfer amounts, so price is never an input
- **Where to start:** On a fork, execute a max-size flash-funded swap against every venue in the pricing path and assert that no value-bearing entrypoint changes its output beyond the configured deviation bound.
- **Evidence:** `protocols/deep_screened.jsonl#guru-network-classic|ORACLE-SPOT-THIN-LIQUIDITY`, `protocols/onchain_probes.json#guru-network-classic`, `families/families.json#ORACLE-SPOT-THIN-LIQUIDITY`
- **Disclosure channel:** not listed · no audit link listed

### 21. Morpho Optimizer AaveV2  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking B — likelihood of being attacked):** 21
- **Protocol:** Morpho Optimizer AaveV2 (`morpho-optimizer-aavev2`) · Lending · Ethereum
- **DefiLlama URL:** https://defillama.com/protocol/morpho-optimizer-aavev2
- **Value at risk (TVL):** $138,237  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
    - Corroborating danger signals: a deployed-source pair already scores 73.8 at L4 guard review
- **HACK_LIKELIHOOD: 63.97 / 100**
    - family evidence 21.6/40 (MATCH 60 × evidence-level weight 0.9) · hazard 12.37/25 · neglect 20/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 60 / 100 · **EVIDENCE_CONFIDENCE:** 77.0 / 100 · **Evidence level:** `L3_STATE`
- **Why this segment gets hit:** chain hazard ×2.54, category hazard ×1.49. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 20/25):**
    - `single_audit_only` (+2) — a single audit listed, with no indication it covers the current deployment
    - `dead_front_end` (+6) — front end is dead while contracts still hold value
    - `deprecated_flag` (+4) — DefiLlama deprecated flag (ambiguous on its own)
    - `rebranded` (+2) — operated under previous names, so old contracts may still be live
    - `warning_banner` (+3) — DefiLlama displays a warning banner
    - `no_timelock_in_source` (+3) — no timelock construct found in the source that was read
- **Broken invariant this family tests:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - Conditions observed: `REBRANDED_DEPLOYMENT`, `DEAD_FRONTEND_FUNDED`
    - condition DEAD_FRONTEND_FUNDED (PRECOND): Front end is dead while contracts still hold value: nobody is watching the deployment that still holds funds.
    - condition REBRANDED_DEPLOYMENT (PRIORITY): Operated under previous names, so contracts deployed under the old identity may still be live and unwatched.
    - 2 address(es) still hold deployed code on-chain
- **Preconditions PRESENT:** unmaintained_or_differing_code_path, prior_version_still_callable, still_holds_value_or_authority
- **Preconditions UNKNOWN:** not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#morpho-optimizer-aavev2|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#morpho-optimizer-aavev2`, `families/families.json#UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
- **Disclosure channel:** not listed · audits: https://docs.morpho.org/security-reviews

### 22. deBridge  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking B — likelihood of being attacked):** 22
- **Protocol:** deBridge (`debridge`) · Bridge · Ethereum, Binance, Arbitrum, Polygon, Heco, Sei
- **DefiLlama URL:** https://defillama.com/protocol/debridge
- **Value at risk (TVL):** $1,907,281  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
    - Corroborating danger signals: a deployed-source pair already scores 73.8 at L4 guard review
- **HACK_LIKELIHOOD: 63.91 / 100**
    - family evidence 29.52/40 (MATCH 73.8 × evidence-level weight 1.0) · hazard 18.39/25 · neglect 7/25 · attacker economics 9.0/10
- **MATCH_SCORE:** 73.8 / 100 · **EVIDENCE_CONFIDENCE:** 85.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×3.61, category hazard ×3.59. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 7/25):**
    - `single_audit_only` (+2) — a single audit listed, with no indication it covers the current deployment
    - `rebranded` (+2) — operated under previous names, so old contracts may still be live
    - `no_timelock_in_source` (+3) — no timelock construct found in the source that was read
- **Broken invariant this family tests:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source read (`DeBridgeGate` @ 0x797161bc…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for DeBridgeGate@0x797161bc…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain
- **Preconditions UNKNOWN:** none
- **Guards searched / found:** merkle_proof_gate / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#debridge|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#debridge`, `families/families.json#AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`
- **Disclosure channel:** https://app.debridge.com · audits: https://github.com/debridge-finance/debridge-security

### 23. Ajna V1  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking B — likelihood of being attacked):** 23
- **Protocol:** Ajna V1 (`ajna-v1`) · Lending · Ethereum
- **DefiLlama URL:** https://defillama.com/protocol/ajna-v1
- **Value at risk (TVL):** $491,042  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
    - Corroborating danger signals: a deployed-source pair already scores 73.8 at L4 guard review
- **HACK_LIKELIHOOD: 63.89 / 100**
    - family evidence 29.52/40 (MATCH 73.8 × evidence-level weight 1.0) · hazard 12.37/25 · neglect 12/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 73.8 / 100 · **EVIDENCE_CONFIDENCE:** 85.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×2.54, category hazard ×1.49. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 12/25):**
    - `single_audit_only` (+2) — a single audit listed, with no indication it covers the current deployment
    - `version_sibling_legacy` (+4) — a version sibling of a newer deployment still holds value
    - `misrepresented_tokens` (+3) — DefiLlama cannot reconcile this protocol's reported token holdings
    - `no_timelock_in_source` (+3) — no timelock construct found in the source that was read
- **Broken invariant this family tests:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source read (`ERC20PoolFactory` @ 0xe6f4d971…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for ERC20PoolFactory@0xe6f4d971…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain
- **Preconditions UNKNOWN:** none
- **Guards searched / found:** merkle_proof_gate / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#ajna-v1|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#ajna-v1`, `families/families.json#AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`
- **Disclosure channel:** https://www.ajna.finance/ · audits: https://github.com/ajna-finance/audits

### 24. BurgerSwap  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking B — likelihood of being attacked):** 24
- **Protocol:** BurgerSwap (`burgerswap`) · Dexs · Binance
- **DefiLlama URL:** https://defillama.com/protocol/burgerswap
- **Value at risk (TVL):** $178,861  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
    - Corroborating danger signals: an implementation behind a live proxy is unverified on the explorer
- **HACK_LIKELIHOOD: 63.74 / 100**
    - family evidence 21.6/40 (MATCH 60 × evidence-level weight 0.9) · hazard 12.14/25 · neglect 20/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 60 / 100 · **EVIDENCE_CONFIDENCE:** 77.0 / 100 · **Evidence level:** `L3_STATE`
- **Why this segment gets hit:** chain hazard ×3.61, category hazard ×1.0. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 20/25):**
    - `no_audit_listed` (+7) — no audit link listed by DefiLlama
    - `dead_front_end` (+6) — front end is dead while contracts still hold value
    - `unverified_implementation` (+7) — an implementation behind a proxy is unverified on the explorer
- **Broken invariant this family tests:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - Conditions observed: `DEAD_FRONTEND_FUNDED`
    - condition DEAD_FRONTEND_FUNDED (PRECOND): Front end is dead while contracts still hold value: nobody is watching the deployment that still holds funds.
    - 2 address(es) still hold deployed code on-chain
- **Preconditions PRESENT:** unmaintained_or_differing_code_path, prior_version_still_callable, still_holds_value_or_authority
- **Preconditions UNKNOWN:** not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#burgerswap|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#burgerswap`, `families/families.json#UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
- **Disclosure channel:** not listed · no audit link listed

### 25. Blackwing  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking B — likelihood of being attacked):** 25
- **Protocol:** Blackwing (`blackwing`) · Farm · Arbitrum, Binance, Ethereum
- **DefiLlama URL:** https://defillama.com/protocol/blackwing
- **Value at risk (TVL):** $949,551  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
- **HACK_LIKELIHOOD: 63.56 / 100**
    - family evidence 21.6/40 (MATCH 60 × evidence-level weight 0.9) · hazard 24.96/25 · neglect 7/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 60 / 100 · **EVIDENCE_CONFIDENCE:** 77.0 / 100 · **Evidence level:** `L3_STATE`
- **Why this segment gets hit:** chain hazard ×3.61, category hazard ×13.74. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 7/25):**
    - `no_audit_listed` (+7) — no audit link listed by DefiLlama
- **Broken invariant this family tests:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - 2 address(es) still hold deployed code on-chain
- **Preconditions PRESENT:** prior_version_still_callable, still_holds_value_or_authority
- **Preconditions UNKNOWN:** unmaintained_or_differing_code_path, not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#blackwing|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#blackwing`, `families/families.json#UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
- **Disclosure channel:** https://blackwing.fi/ · no audit link listed

### 26. Listapie  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking B — likelihood of being attacked):** 26
- **Protocol:** Listapie (`listapie`) · Farm · Binance
- **DefiLlama URL:** https://defillama.com/protocol/listapie
- **Value at risk (TVL):** $59,378  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
- **HACK_LIKELIHOOD: 63.56 / 100**
    - family evidence 21.6/40 (MATCH 60 × evidence-level weight 0.9) · hazard 24.96/25 · neglect 7/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 60 / 100 · **EVIDENCE_CONFIDENCE:** 77.0 / 100 · **Evidence level:** `L3_STATE`
- **Why this segment gets hit:** chain hazard ×3.61, category hazard ×13.74. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 7/25):**
    - `no_audit_listed` (+7) — no audit link listed by DefiLlama
- **Broken invariant this family tests:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - 8 address(es) still hold deployed code on-chain
- **Preconditions PRESENT:** prior_version_still_callable, still_holds_value_or_authority, not_paused
- **Preconditions UNKNOWN:** unmaintained_or_differing_code_path
- **Guards searched / found:** paused_and_drained, approvals_revoked / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#listapie|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#listapie`, `families/families.json#UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
- **Disclosure channel:** https://www.lista.magpiexyz.io/stake · no audit link listed

### 27. Stargate V1  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking B — likelihood of being attacked):** 27
- **Protocol:** Stargate V1 (`stargate-v1`) · Cross Chain Bridge · Ethereum, Mantle, Arbitrum, Avalanche, Binance, Fantom …
- **DefiLlama URL:** https://defillama.com/protocol/stargate-v1
- **Value at risk (TVL):** $10,725,483  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
    - Corroborating danger signals: an implementation behind a live proxy is unverified on the explorer
- **HACK_LIKELIHOOD: 63.39 / 100**
    - family evidence 24.0/40 (MATCH 60 × evidence-level weight 1.0) · hazard 18.39/25 · neglect 16/25 · attacker economics 5.0/10
- **MATCH_SCORE:** 60 / 100 · **EVIDENCE_CONFIDENCE:** 90.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×3.61, category hazard ×3.59. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 16/25):**
    - `single_audit_only` (+2) — a single audit listed, with no indication it covers the current deployment
    - `version_sibling_legacy` (+4) — a version sibling of a newer deployment still holds value
    - `unverified_implementation` (+7) — an implementation behind a proxy is unverified on the explorer
    - `no_timelock_in_source` (+3) — no timelock construct found in the source that was read
- **Broken invariant this family tests:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source read (`Auction` @ 0x45A01E4e…(ethereum)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for Auction@0x45A01E4e…(ethereum); indicators matched: hook_zero_amount_unguarded
    - 1 implementation(s) behind a proxy are NOT verified on the explorer: implementation identity unresolved, score capped at 60
- **Preconditions PRESENT:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain
- **Preconditions UNKNOWN:** none
- **Guards searched / found:** none / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#stargate-v1|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#stargate-v1`, `families/families.json#HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`
- **Disclosure channel:** https://stargate.finance/ · audits: https://github.com/stargate-protocol/stargate/tree/main/audit

### 28. ValueDefi  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking B — likelihood of being attacked):** 28
- **Protocol:** ValueDefi (`valuedefi`) · Dexs · Binance
- **DefiLlama URL:** https://defillama.com/protocol/valuedefi
- **Value at risk (TVL):** $467,702  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
- **HACK_LIKELIHOOD: 63.14 / 100**
    - family evidence 30.0/40 (MATCH 75.0 × evidence-level weight 1.0) · hazard 12.14/25 · neglect 11/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 75.0 / 100 · **EVIDENCE_CONFIDENCE:** 90.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×3.61, category hazard ×1.0. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 11/25):**
    - `single_audit_only` (+2) — a single audit listed, with no indication it covers the current deployment
    - `dead_front_end` (+6) — front end is dead while contracts still hold value
    - `misrepresented_tokens` (+3) — DefiLlama cannot reconcile this protocol's reported token holdings
- **Broken invariant this family tests:** After deployment, no caller may (re)establish ownership, admin, or implementation wiring. Initialization state must be provably consumed.
    - Deployed source read (`ValueLiquidFactory` @ 0x1b8e12f8…(bsc), `StableSwapFactory` @ 0xae63a206…(bsc)): prerequisites matched: initialize_without_modifier; no guard found
    - deployed source read for ValueLiquidFactory@0x1b8e12f8…(bsc), StableSwapFactory@0xae63a206…(bsc); indicators matched: initialize_without_modifier
    - 1/1 live proxies read a zero ERC-7201 Initializable slot (inconclusive alone: older OZ versions store the flag elsewhere)
- **Preconditions PRESENT:** src::initialize_without_modifier, upgradeable_architecture, initializer_flag_unset, live_value_or_approvals
- **Preconditions UNKNOWN:** none
- **Guards searched / found:** initializer_modifier_present, upgrade_timelocked / upgrade_timelocked
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Simulated re-initialization reverts (kills the pair); Contract is non-upgradeable and holds no approvals
- **Where to start:** Read the initialization slot on every live proxy/facet and simulate re-initialization from an unprivileged address; it must revert.
- **Evidence:** `protocols/deep_screened.jsonl#valuedefi|UPGRADE-INITIALIZER-REACHABLE-LIVE`, `protocols/onchain_probes.json#valuedefi`, `families/families.json#UPGRADE-INITIALIZER-REACHABLE-LIVE`
- **Disclosure channel:** not listed · audits: https://valuedefi.io/audit

### 29. Synapse Cross Chain Bridge  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking B — likelihood of being attacked):** 29
- **Protocol:** Synapse Cross Chain Bridge (`synapse-cross-chain-bridge`) · Cross Chain Bridge · Ethereum, Canto, Avalanche, Blast, Arbitrum, Binance …
- **DefiLlama URL:** https://defillama.com/protocol/synapse-cross-chain-bridge
- **Value at risk (TVL):** $11,793,010  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
    - Corroborating danger signals: a deployed-source pair already scores 73.8 at L4 guard review
- **HACK_LIKELIHOOD: 62.91 / 100**
    - family evidence 29.52/40 (MATCH 73.8 × evidence-level weight 1.0) · hazard 18.39/25 · neglect 10/25 · attacker economics 5.0/10
- **MATCH_SCORE:** 73.8 / 100 · **EVIDENCE_CONFIDENCE:** 85.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×3.61, category hazard ×3.59. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 10/25):**
    - `no_audit_listed` (+7) — no audit link listed by DefiLlama
    - `no_timelock_in_source` (+3) — no timelock construct found in the source that was read
- **Broken invariant this family tests:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source read (`UniswapV2Pair` @ 0x4a86c01d…(ethereum), `MiniChefV2` @ 0xd10ef2a5…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for UniswapV2Pair@0x4a86c01d…(ethereum), MiniChefV2@0xd10ef2a5…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain
- **Preconditions UNKNOWN:** none
- **Guards searched / found:** merkle_proof_gate / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#synapse-cross-chain-bridge|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#synapse-cross-chain-bridge`, `families/families.json#AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`
- **Disclosure channel:** https://synapseprotocol.com · no audit link listed

### 30. Contango V1  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking B — likelihood of being attacked):** 30
- **Protocol:** Contango V1 (`contango-v1`) · Derivatives · Arbitrum, Ethereum
- **DefiLlama URL:** https://defillama.com/protocol/contango-v1
- **Value at risk (TVL):** $290,609  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
    - Corroborating danger signals: a deployed-source pair already scores 73.8 at L4 guard review
- **HACK_LIKELIHOOD: 62.91 / 100**
    - family evidence 29.52/40 (MATCH 73.8 × evidence-level weight 1.0) · hazard 9.39/25 · neglect 14/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 73.8 / 100 · **EVIDENCE_CONFIDENCE:** 90.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×2.54, category hazard ×0.81. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 14/25):**
    - `no_audit_listed` (+7) — no audit link listed by DefiLlama
    - `version_sibling_legacy` (+4) — a version sibling of a newer deployment still holds value
    - `no_timelock_in_source` (+3) — no timelock construct found in the source that was read
- **Broken invariant this family tests:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source read (`ERC1967Proxy` @ 0x30E73481…(arbitrum), `ContangoLadle` @ 0x93343c08…(arbitrum)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for ERC1967Proxy@0x30E73481…(arbitrum), ContangoLadle@0x93343c08…(arbitrum); indicators matched: unsafe_cross_sign_cast
- **Preconditions PRESENT:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain
- **Preconditions UNKNOWN:** none
- **Guards searched / found:** safecast_used / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#contango-v1|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#contango-v1`, `families/families.json#ACC-SIGN-OR-BOUND-CHECK-MISSING`
- **Disclosure channel:** https://contango.xyz/ · no audit link listed

### 31. Olive Network  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking B — likelihood of being attacked):** 31
- **Protocol:** Olive Network (`olive-network`) · Farm · Ethereum, Arbitrum
- **DefiLlama URL:** https://defillama.com/protocol/olive-network
- **Value at risk (TVL):** $98,829  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
- **HACK_LIKELIHOOD: 62.84 / 100**
    - family evidence 21.6/40 (MATCH 60 × evidence-level weight 0.9) · hazard 23.24/25 · neglect 8/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 60 / 100 · **EVIDENCE_CONFIDENCE:** 77.0 / 100 · **Evidence level:** `L3_STATE`
- **Why this segment gets hit:** chain hazard ×2.54, category hazard ×13.74. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 8/25):**
    - `single_audit_only` (+2) — a single audit listed, with no indication it covers the current deployment
    - `dead_front_end` (+6) — front end is dead while contracts still hold value
- **Broken invariant this family tests:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - Conditions observed: `DEAD_FRONTEND_FUNDED`
    - condition DEAD_FRONTEND_FUNDED (PRECOND): Front end is dead while contracts still hold value: nobody is watching the deployment that still holds funds.
    - 1 address(es) still hold deployed code on-chain
- **Preconditions PRESENT:** unmaintained_or_differing_code_path, prior_version_still_callable, still_holds_value_or_authority
- **Preconditions UNKNOWN:** not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#olive-network|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#olive-network`, `families/families.json#UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
- **Disclosure channel:** not listed · audits: https://2227259712-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdiKpPMQRzcvmKZPuBfGZ%2Fuploads%2Fxfzaty6B6Gtxx18McMTQ%2FOlive%20Audit%20Report.pdf?alt=media&token=0a360c6d-cf15-4c7b-b0e5-4762590078d9

### 32. Agave  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking B — likelihood of being attacked):** 32
- **Protocol:** Agave (`agave`) · Lending · xDai
- **DefiLlama URL:** https://defillama.com/protocol/agave
- **Value at risk (TVL):** $88,695  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
    - Corroborating danger signals: a deployed-source pair already scores 73.8 at L4 guard review
- **HACK_LIKELIHOOD: 62.72 / 100**
    - family evidence 21.0/40 (MATCH 52.5 × evidence-level weight 1.0) · hazard 6.72/25 · neglect 25.0/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 52.5 / 100 · **EVIDENCE_CONFIDENCE:** 71.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×0.8, category hazard ×1.49. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 25.0/25):**
    - `no_audit_listed` (+7) — no audit link listed by DefiLlama
    - `dead_front_end` (+6) — front end is dead while contracts still hold value
    - `deprecated_flag` (+4) — DefiLlama deprecated flag (ambiguous on its own)
    - `owner_is_zero_with_value` (+5) — owner() is the zero address while the contract still holds code and value
    - `no_timelock_in_source` (+3) — no timelock construct found in the source that was read
- **Broken invariant this family tests:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source read (`AaveProtocolDataProvider` @ 0x24dCbd37…(xdai), `MiniMeToken` @ 0x3a97704a…(xdai)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for AaveProtocolDataProvider@0x24dCbd37…(xdai), MiniMeToken@0x3a97704a…(xdai); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT:** src::claim_without_eligibility_map, live_value_present
- **Preconditions UNKNOWN:** none
- **Guards searched / found:** merkle_proof_gate / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#agave|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#agave`, `families/families.json#AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`
- **Disclosure channel:** not listed · no audit link listed

### 33. Lybra V1  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking B — likelihood of being attacked):** 33
- **Protocol:** Lybra V1 (`lybra-v1`) · CDP · Ethereum
- **DefiLlama URL:** https://defillama.com/protocol/lybra-v1
- **Value at risk (TVL):** $347,500  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
    - Corroborating danger signals: a deployed-source pair already scores 73.8 at L4 guard review
- **HACK_LIKELIHOOD: 62.62 / 100**
    - family evidence 29.52/40 (MATCH 73.8 × evidence-level weight 1.0) · hazard 11.1/25 · neglect 12/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 73.8 / 100 · **EVIDENCE_CONFIDENCE:** 85.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×2.54, category hazard ×1.15. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 12/25):**
    - `single_audit_only` (+2) — a single audit listed, with no indication it covers the current deployment
    - `dead_front_end` (+6) — front end is dead while contracts still hold value
    - `version_sibling_legacy` (+4) — a version sibling of a newer deployment still holds value
- **Broken invariant this family tests:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source read (`ChiToken` @ 0x00000000…(ethereum), `zCurve` @ 0x00000000…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for ChiToken@0x00000000…(ethereum), zCurve@0x00000000…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain
- **Preconditions UNKNOWN:** none
- **Guards searched / found:** merkle_proof_gate / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#lybra-v1|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#lybra-v1`, `families/families.json#AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`
- **Disclosure channel:** not listed · audits: https://solidity.finance/audits/Lybra/

### 34. Premia V2  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking B — likelihood of being attacked):** 34
- **Protocol:** Premia V2 (`premia-v2`) · Options · Arbitrum, Optimism, Ethereum, Binance, Fantom
- **DefiLlama URL:** https://defillama.com/protocol/premia-v2
- **Value at risk (TVL):** $215,634  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
    - Corroborating danger signals: an implementation behind a live proxy is unverified on the explorer
- **HACK_LIKELIHOOD: 62.06 / 100**
    - family evidence 21.6/40 (MATCH 60 × evidence-level weight 0.9) · hazard 16.46/25 · neglect 14/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 60 / 100 · **EVIDENCE_CONFIDENCE:** 77.0 / 100 · **Evidence level:** `L3_STATE`
- **Why this segment gets hit:** chain hazard ×3.61, category hazard ×2.42. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 14/25):**
    - `version_sibling_legacy` (+4) — a version sibling of a newer deployment still holds value
    - `unverified_implementation` (+7) — an implementation behind a proxy is unverified on the explorer
    - `no_timelock_in_source` (+3) — no timelock construct found in the source that was read
- **Broken invariant this family tests:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - Conditions observed: `VERSION_SIBLING_LEGACY`
    - condition VERSION_SIBLING_LEGACY (PRECOND): Shares a parent protocol with a higher-version sibling while still holding value: the classic sibling-deployment-retains-the-old-version shape.
    - 4 address(es) still hold deployed code on-chain
- **Preconditions PRESENT:** prior_version_still_callable, still_holds_value_or_authority
- **Preconditions UNKNOWN:** unmaintained_or_differing_code_path, not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#premia-v2|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#premia-v2`, `families/families.json#UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
- **Disclosure channel:** https://premia.finance/ · audits: https://solidity.finance/audits/Premia, https://hacken.io/audits/#solidstate

### 35. CrossChain Bridge  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking B — likelihood of being attacked):** 35
- **Protocol:** CrossChain Bridge (`crosschain-bridge`) · Cross Chain Bridge · Ethereum, Polygon, Binance, Avalanche, Fantom
- **DefiLlama URL:** https://defillama.com/protocol/crosschain-bridge
- **Value at risk (TVL):** $88,000  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
- **HACK_LIKELIHOOD: 61.99 / 100**
    - family evidence 21.6/40 (MATCH 60 × evidence-level weight 0.9) · hazard 18.39/25 · neglect 12/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 60 / 100 · **EVIDENCE_CONFIDENCE:** 69.0 / 100 · **Evidence level:** `L3_STATE`
- **Why this segment gets hit:** chain hazard ×3.61, category hazard ×3.59. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 12/25):**
    - `no_audit_listed` (+7) — no audit link listed by DefiLlama
    - `sharp_inflow_unaudited` (+5) — TVL rose sharply over the last week with no audit listed: fresh money on unproven code
- **Broken invariant this family tests:** After deployment, no caller may (re)establish ownership, admin, or implementation wiring. Initialization state must be provably consumed.
    - Deployed source read (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): no prerequisite matched; no guard found
    - RELEVANCE GATE: the contract(s) actually read (ZAMM, ZAMM) show no distinguishing indicator for this family, so they are probably not the contracts that implement it. Every source-derived signal is therefore UNKNOWN, including the absence of a guard: not finding a staleness check in a data-provider contract says nothing about the oracle.
    - 2/2 live proxies read a zero ERC-7201 Initializable slot (inconclusive alone: older OZ versions store the flag elsewhere)
    - 2 proxy/proxies expose a non-zero owner()
- **Preconditions PRESENT:** upgradeable_architecture, initializer_flag_unset, live_value_or_approvals
- **Preconditions UNKNOWN:** none
- **Guards searched / found:** upgrade_timelocked / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Simulated re-initialization reverts (kills the pair); Contract is non-upgradeable and holds no approvals
- **Where to start:** Read the initialization slot on every live proxy/facet and simulate re-initialization from an unprivileged address; it must revert.
- **Evidence:** `protocols/deep_screened.jsonl#crosschain-bridge|UPGRADE-INITIALIZER-REACHABLE-LIVE`, `protocols/onchain_probes.json#crosschain-bridge`, `families/families.json#UPGRADE-INITIALIZER-REACHABLE-LIVE`
- **Disclosure channel:** https://app.crosschainbridge.org/ · no audit link listed

### 36. WavesBridge  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking B — likelihood of being attacked):** 36
- **Protocol:** WavesBridge (`wavesbridge`) · Bridge · UNIT0, Waves, Solana, Ethereum, Binance
- **DefiLlama URL:** https://defillama.com/protocol/wavesbridge
- **Value at risk (TVL):** $769,895  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
- **HACK_LIKELIHOOD: 61.99 / 100**
    - family evidence 21.6/40 (MATCH 60 × evidence-level weight 0.9) · hazard 18.39/25 · neglect 12/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 60 / 100 · **EVIDENCE_CONFIDENCE:** 77.0 / 100 · **Evidence level:** `L3_STATE`
- **Why this segment gets hit:** chain hazard ×3.61, category hazard ×3.59. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 12/25):**
    - `no_audit_listed` (+7) — no audit link listed by DefiLlama
    - `sharp_inflow_unaudited` (+5) — TVL rose sharply over the last week with no audit listed: fresh money on unproven code
- **Broken invariant this family tests:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - 5 address(es) still hold deployed code on-chain
- **Preconditions PRESENT:** prior_version_still_callable, still_holds_value_or_authority
- **Preconditions UNKNOWN:** unmaintained_or_differing_code_path, not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#wavesbridge|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#wavesbridge`, `families/families.json#UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
- **Disclosure channel:** https://wavesbridge.io/ · no audit link listed

### 37. GoPlus Locker V2  —  `ACC-CREDIT-NOT-RECEIVED`

- **Rank (Ranking B — likelihood of being attacked):** 37
- **Protocol:** GoPlus Locker V2 (`goplus-locker-v2`) · Token Locker · Base, Binance, Ethereum, Arbitrum
- **DefiLlama URL:** https://defillama.com/protocol/goplus-locker-v2
- **Value at risk (TVL):** $419,406  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
- **HACK_LIKELIHOOD: 61.91 / 100**
    - family evidence 25.52/40 (MATCH 63.8 × evidence-level weight 1.0) · hazard 10.39/25 · neglect 16/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 63.8 / 100 · **EVIDENCE_CONFIDENCE:** 85.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×3.61, category hazard ×0.7. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 16/25):**
    - `no_audit_listed` (+7) — no audit link listed by DefiLlama
    - `rebranded` (+2) — operated under previous names, so old contracts may still be live
    - `version_sibling_legacy` (+4) — a version sibling of a newer deployment still holds value
    - `no_timelock_in_source` (+3) — no timelock construct found in the source that was read
- **Broken invariant this family tests:** Reward credit must be derived from economic value actually transferred to, or spent through, the protocol. A balance delta observed on a third-party venue is not proof of a purchase.
    - Deployed source read (`TokenLocker` @ 0xF17A08A7…(base)): prerequisites matched: balance_delta_credit; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): public_claim_fn=no
    - deployed source read for TokenLocker@0xF17A08A7…(base); indicators matched: balance_delta_credit
- **Preconditions PRESENT:** src::balance_delta_credit, live_value_present, deployment_reachable_on_chain
- **Preconditions UNKNOWN:** none
- **Guards searched / found:** none / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Credit derived from transferFrom into the protocol (kills the pair); Entitlements written only by a trusted settlement path
- **Where to start:** On a fork, fabricate the observable precondition without transferring value to the protocol; the entitlement must not increase.
- **Evidence:** `protocols/deep_screened.jsonl#goplus-locker-v2|ACC-CREDIT-NOT-RECEIVED`, `protocols/onchain_probes.json#goplus-locker-v2`, `families/families.json#ACC-CREDIT-NOT-RECEIVED`
- **Disclosure channel:** https://gopluslabs.io · no audit link listed

### 38. Terminal Finance Pre-Deposits  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking B — likelihood of being attacked):** 38
- **Protocol:** Terminal Finance Pre-Deposits (`terminal-finance-pre-deposits`) · Farm · Ethereum
- **DefiLlama URL:** https://defillama.com/protocol/terminal-finance-pre-deposits
- **Value at risk (TVL):** $566,593  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
- **HACK_LIKELIHOOD: 61.84 / 100**
    - family evidence 21.6/40 (MATCH 60 × evidence-level weight 0.9) · hazard 23.24/25 · neglect 7/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 60 / 100 · **EVIDENCE_CONFIDENCE:** 77.0 / 100 · **Evidence level:** `L3_STATE`
- **Why this segment gets hit:** chain hazard ×2.54, category hazard ×13.74. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 7/25):**
    - `no_audit_listed` (+7) — no audit link listed by DefiLlama
- **Broken invariant this family tests:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - 3 address(es) still hold deployed code on-chain
- **Preconditions PRESENT:** prior_version_still_callable, still_holds_value_or_authority
- **Preconditions UNKNOWN:** unmaintained_or_differing_code_path, not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#terminal-finance-pre-deposits|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#terminal-finance-pre-deposits`, `families/families.json#UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
- **Disclosure channel:** https://terminal.fi/ · no audit link listed

### 39. DOOAR V2  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking B — likelihood of being attacked):** 39
- **Protocol:** DOOAR V2 (`dooar-v2`) · Dexs · Solana, Binance
- **DefiLlama URL:** https://defillama.com/protocol/dooar-v2
- **Value at risk (TVL):** $5,127,684  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
- **HACK_LIKELIHOOD: 61.66 / 100**
    - family evidence 25.52/40 (MATCH 63.8 × evidence-level weight 1.0) · hazard 12.14/25 · neglect 17/25 · attacker economics 7.0/10
- **MATCH_SCORE:** 63.8 / 100 · **EVIDENCE_CONFIDENCE:** 90.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×3.61, category hazard ×1.0. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 17/25):**
    - `no_audit_listed` (+7) — no audit link listed by DefiLlama
    - `version_sibling_legacy` (+4) — a version sibling of a newer deployment still holds value
    - `misrepresented_tokens` (+3) — DefiLlama cannot reconcile this protocol's reported token holdings
    - `no_timelock_in_source` (+3) — no timelock construct found in the source that was read
- **Broken invariant this family tests:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source read (`DooarSwapV2Factory` @ 0x1e895bFe…(bsc)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for DooarSwapV2Factory@0x1e895bFe…(bsc); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain
- **Preconditions UNKNOWN:** none
- **Guards searched / found:** none / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#dooar-v2|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#dooar-v2`, `families/families.json#HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`
- **Disclosure channel:** https://beta.dooar.com/swap · no audit link listed

### 40. Frax FPI  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking B — likelihood of being attacked):** 40
- **Protocol:** Frax FPI (`frax-fpi`) · Algo-Stables · Ethereum
- **DefiLlama URL:** https://defillama.com/protocol/frax-fpi
- **Value at risk (TVL):** $94,330  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
- **HACK_LIKELIHOOD: 61.64 / 100**
    - family evidence 21.6/40 (MATCH 60 × evidence-level weight 0.9) · hazard 23.04/25 · neglect 7/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 60 / 100 · **EVIDENCE_CONFIDENCE:** 77.0 / 100 · **Evidence level:** `L3_STATE`
- **Why this segment gets hit:** chain hazard ×2.54, category hazard ×13.2. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 7/25):**
    - `no_audit_listed` (+7) — no audit link listed by DefiLlama
- **Broken invariant this family tests:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - 6 address(es) still hold deployed code on-chain
- **Preconditions PRESENT:** prior_version_still_callable, still_holds_value_or_authority
- **Preconditions UNKNOWN:** unmaintained_or_differing_code_path, not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#frax-fpi|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#frax-fpi`, `families/families.json#UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
- **Disclosure channel:** https://frax.com/ · no audit link listed

### 41. Enosys Bridge  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking B — likelihood of being attacked):** 41
- **Protocol:** Enosys Bridge (`enosys-bridge`) · Bridge · Ethereum, XDC
- **DefiLlama URL:** https://defillama.com/protocol/enosys-bridge
- **Value at risk (TVL):** $434,188  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
- **HACK_LIKELIHOOD: 61.27 / 100**
    - family evidence 21.6/40 (MATCH 60 × evidence-level weight 0.9) · hazard 16.67/25 · neglect 13/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 60 / 100 · **EVIDENCE_CONFIDENCE:** 77.0 / 100 · **Evidence level:** `L3_STATE`
- **Why this segment gets hit:** chain hazard ×2.54, category hazard ×3.59. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 13/25):**
    - `no_audit_listed` (+7) — no audit link listed by DefiLlama
    - `dead_front_end` (+6) — front end is dead while contracts still hold value
- **Broken invariant this family tests:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - Conditions observed: `DEAD_FRONTEND_FUNDED`
    - condition DEAD_FRONTEND_FUNDED (PRECOND): Front end is dead while contracts still hold value: nobody is watching the deployment that still holds funds.
    - 6 address(es) still hold deployed code on-chain
- **Preconditions PRESENT:** unmaintained_or_differing_code_path, prior_version_still_callable, still_holds_value_or_authority
- **Preconditions UNKNOWN:** not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#enosys-bridge|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#enosys-bridge`, `families/families.json#UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
- **Disclosure channel:** not listed · no audit link listed

### 42. Privacy Pools  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking B — likelihood of being attacked):** 42
- **Protocol:** Privacy Pools (`privacy-pools`) · Privacy · Ethereum, Arbitrum, Optimism
- **DefiLlama URL:** https://defillama.com/protocol/privacy-pools
- **Value at risk (TVL):** $8,870,480  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
- **HACK_LIKELIHOOD: 61.22 / 100**
    - family evidence 21.6/40 (MATCH 60 × evidence-level weight 0.9) · hazard 22.62/25 · neglect 10/25 · attacker economics 7.0/10
- **MATCH_SCORE:** 60 / 100 · **EVIDENCE_CONFIDENCE:** 77.0 / 100 · **Evidence level:** `L3_STATE`
- **Why this segment gets hit:** chain hazard ×2.54, category hazard ×12.1. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 10/25):**
    - `no_audit_listed` (+7) — no audit link listed by DefiLlama
    - `no_timelock_in_source` (+3) — no timelock construct found in the source that was read
- **Broken invariant this family tests:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - 1 address(es) still hold deployed code on-chain
- **Preconditions PRESENT:** prior_version_still_callable, still_holds_value_or_authority
- **Preconditions UNKNOWN:** unmaintained_or_differing_code_path, not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#privacy-pools|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#privacy-pools`, `families/families.json#UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
- **Disclosure channel:** https://privacypools.com/ · no audit link listed

### 43. Maverick V1  —  `ACC-DUPLICATE-ID-ACCUMULATION`

- **Rank (Ranking B — likelihood of being attacked):** 43
- **Protocol:** Maverick V1 (`maverick-v1`) · Dexs · zkSync Era, Ethereum, Binance, Base
- **DefiLlama URL:** https://defillama.com/protocol/maverick-v1
- **Value at risk (TVL):** $1,064,242  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
    - Corroborating danger signals: an implementation behind a live proxy is unverified on the explorer
- **HACK_LIKELIHOOD: 61.14 / 100**
    - family evidence 24.0/40 (MATCH 60 × evidence-level weight 1.0) · hazard 12.14/25 · neglect 16/25 · attacker economics 9.0/10
- **MATCH_SCORE:** 60 / 100 · **EVIDENCE_CONFIDENCE:** 85.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×3.61, category hazard ×1.0. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 16/25):**
    - `single_audit_only` (+2) — a single audit listed, with no indication it covers the current deployment
    - `version_sibling_legacy` (+4) — a version sibling of a newer deployment still holds value
    - `unverified_implementation` (+7) — an implementation behind a proxy is unverified on the explorer
    - `no_timelock_in_source` (+3) — no timelock construct found in the source that was read
- **Broken invariant this family tests:** An entitlement attached to an identifier may be counted at most once per period. A caller-supplied ID list must be deduplicated, or each ID's claim state consumed before the next read.
    - Deployed source read (`Router` @ 0xB2855783…(ethereum)): prerequisites matched: id_array_loop_without_dedup; no guard found
    - deployed source read for Router@0xB2855783…(ethereum); indicators matched: id_array_loop_without_dedup
    - 1 implementation(s) behind a proxy are NOT verified on the explorer: implementation identity unresolved, score capped at 60
- **Preconditions PRESENT:** src::id_array_loop_without_dedup, live_value_present, deployment_reachable_on_chain
- **Preconditions UNKNOWN:** none
- **Guards searched / found:** none / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Consumed marker written inside the loop (kills the pair); IDs required strictly increasing
- **Where to start:** On a fork, call the batch function with one ID repeated k times; payout must equal the single-ID payout.
- **Evidence:** `protocols/deep_screened.jsonl#maverick-v1|ACC-DUPLICATE-ID-ACCUMULATION`, `protocols/onchain_probes.json#maverick-v1`, `families/families.json#ACC-DUPLICATE-ID-ACCUMULATION`
- **Disclosure channel:** https://www.mav.xyz · audits: https://github.com/maverickprotocol/audits

### 44. Twindex  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking B — likelihood of being attacked):** 44
- **Protocol:** Twindex (`twindex`) · Options · Binance
- **DefiLlama URL:** https://defillama.com/protocol/twindex
- **Value at risk (TVL):** $130,146  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
- **HACK_LIKELIHOOD: 61.06 / 100**
    - family evidence 21.6/40 (MATCH 60 × evidence-level weight 0.9) · hazard 16.46/25 · neglect 13/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 60 / 100 · **EVIDENCE_CONFIDENCE:** 77.0 / 100 · **Evidence level:** `L3_STATE`
- **Why this segment gets hit:** chain hazard ×3.61, category hazard ×2.42. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 13/25):**
    - `no_audit_listed` (+7) — no audit link listed by DefiLlama
    - `dead_front_end` (+6) — front end is dead while contracts still hold value
- **Broken invariant this family tests:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - Conditions observed: `DEAD_FRONTEND_FUNDED`
    - condition DEAD_FRONTEND_FUNDED (PRECOND): Front end is dead while contracts still hold value: nobody is watching the deployment that still holds funds.
    - 2 address(es) still hold deployed code on-chain
- **Preconditions PRESENT:** unmaintained_or_differing_code_path, prior_version_still_callable, still_holds_value_or_authority
- **Preconditions UNKNOWN:** not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#twindex|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#twindex`, `families/families.json#UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
- **Disclosure channel:** not listed · no audit link listed

### 45. FinNexus  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking B — likelihood of being attacked):** 45
- **Protocol:** FinNexus (`finnexus`) · Options · Ethereum, Binance, Wanchain
- **DefiLlama URL:** https://defillama.com/protocol/finnexus
- **Value at risk (TVL):** $232,179  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
    - Corroborating danger signals: condition HALLMARK_PRIOR_INCIDENT
- **HACK_LIKELIHOOD: 61.06 / 100**
    - family evidence 21.6/40 (MATCH 60 × evidence-level weight 0.9) · hazard 16.46/25 · neglect 13/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 60 / 100 · **EVIDENCE_CONFIDENCE:** 77.0 / 100 · **Evidence level:** `L3_STATE`
- **Why this segment gets hit:** chain hazard ×3.61, category hazard ×2.42. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 13/25):**
    - `single_audit_only` (+2) — a single audit listed, with no indication it covers the current deployment
    - `dead_front_end` (+6) — front end is dead while contracts still hold value
    - `prior_incident_hallmark` (+5) — DefiLlama hallmarks record a prior hack, exploit or drain on this protocol
- **Broken invariant this family tests:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - Conditions observed: `DEAD_FRONTEND_FUNDED`
    - condition DEAD_FRONTEND_FUNDED (PRECOND): Front end is dead while contracts still hold value: nobody is watching the deployment that still holds funds.
    - 4 address(es) still hold deployed code on-chain
- **Preconditions PRESENT:** unmaintained_or_differing_code_path, prior_version_still_callable, still_holds_value_or_authority
- **Preconditions UNKNOWN:** not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#finnexus|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#finnexus`, `families/families.json#UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
- **Disclosure channel:** not listed · audits: https://github.com/Phoenix-Finance/Pdfs/blob/master/PeckShield-Audit-FinnexusOptionsV1.0.pdf
