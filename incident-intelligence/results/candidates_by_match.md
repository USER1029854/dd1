# Candidates — Ranking A — mechanism match

> **Discovery-stage output.** This file asserts no defect in any protocol named below. Each entry is a *high-priority defensive review candidate*: the named evidence matches a family's prerequisites, the named evidence is unknown, and the named guard would falsify it. Everything requires separate authorized verification on a local or pinned fork before any conclusion is drawn.

**Who this list is for.** An independent reviewer who wants to prevent real losses, not a fund allocating audit retainers. The band is $50,000 to $30,000,000: below that there is nothing worth saving, and above it protocols are assumed to carry dedicated professional coverage, so they are dropped unless specific danger evidence says otherwise.

**Why exposure does not drive this ranking.** In this run's own corpus of 128 on-chain incidents, the median loss was $252,000 and 84% cost under $2,000,000. Only 5% exceeded $10,000,000. Size is a poor predictor of being attacked; neglect and segment are far better ones.

Ranking A answers *which protocols most strongly exhibit a family's observable prerequisites*, ignoring segment and neglect entirely.

### 1. Arcade.xyz  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking A — mechanism match):** 1
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

### 2. Fungify  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking A — mechanism match):** 2
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

### 3. Sumer.money  —  `ACC-DONATION-UNACCOUNTED-BALANCE`

- **Rank (Ranking A — mechanism match):** 3
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

### 4. ValueDefi  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking A — mechanism match):** 4
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

### 5. Cook Finance  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking A — mechanism match):** 5
- **Protocol:** Cook Finance (`cook-finance`) · Indexes · Heco, Ethereum, Binance, Avalanche
- **DefiLlama URL:** https://defillama.com/protocol/cook-finance
- **Value at risk (TVL):** $51,767  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
- **HACK_LIKELIHOOD: 61.03 / 100**
    - family evidence 30.0/40 (MATCH 75.0 × evidence-level weight 1.0) · hazard 13.03/25 · neglect 8/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 75.0 / 100 · **EVIDENCE_CONFIDENCE:** 90.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×3.61, category hazard ×1.2. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 8/25):**
    - `single_audit_only` (+2) — a single audit listed, with no indication it covers the current deployment
    - `dead_front_end` (+6) — front end is dead while contracts still hold value
- **Broken invariant this family tests:** After deployment, no caller may (re)establish ownership, admin, or implementation wiring. Initialization state must be provably consumed.
    - Deployed source read (`Oracle` @ 0x35bE7982…(ethereum), `CKToken` @ 0x43633bDb…(ethereum)): prerequisites matched: initialize_without_modifier; no guard found
    - deployed source read for Oracle@0x35bE7982…(ethereum), CKToken@0x43633bDb…(ethereum); indicators matched: initialize_without_modifier
    - 1/1 live proxies read a zero ERC-7201 Initializable slot (inconclusive alone: older OZ versions store the flag elsewhere)
- **Preconditions PRESENT:** src::initialize_without_modifier, upgradeable_architecture, initializer_flag_unset, live_value_or_approvals
- **Preconditions UNKNOWN:** none
- **Guards searched / found:** initializer_modifier_present, upgrade_timelocked / upgrade_timelocked
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Simulated re-initialization reverts (kills the pair); Contract is non-upgradeable and holds no approvals
- **Where to start:** Read the initialization slot on every live proxy/facet and simulate re-initialization from an unprivileged address; it must revert.
- **Evidence:** `protocols/deep_screened.jsonl#cook-finance|UPGRADE-INITIALIZER-REACHABLE-LIVE`, `protocols/onchain_probes.json#cook-finance`, `families/families.json#UPGRADE-INITIALIZER-REACHABLE-LIVE`
- **Disclosure channel:** not listed · audits: https://github.com/CookFinance/cook-token/tree/master/audits

### 6. OreoSwap  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking A — mechanism match):** 6
- **Protocol:** OreoSwap (`oreoswap`) · Dexs · Arbitrum
- **DefiLlama URL:** https://defillama.com/protocol/oreoswap
- **Value at risk (TVL):** $66,960  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
- **HACK_LIKELIHOOD: 57.1 / 100**
    - family evidence 30.0/40 (MATCH 75.0 × evidence-level weight 1.0) · hazard 7.1/25 · neglect 10/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 75.0 / 100 · **EVIDENCE_CONFIDENCE:** 90.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×1.29, category hazard ×1.0. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 10/25):**
    - `no_audit_listed` (+7) — no audit link listed by DefiLlama
    - `misrepresented_tokens` (+3) — DefiLlama cannot reconcile this protocol's reported token holdings
- **Broken invariant this family tests:** After deployment, no caller may (re)establish ownership, admin, or implementation wiring. Initialization state must be provably consumed.
    - Deployed source read (`OreoSwapFactory` @ 0x20fAfD2B…(arbitrum), `OREO` @ 0x319e222D…(arbitrum)): prerequisites matched: initialize_without_modifier; no guard found
    - deployed source read for OreoSwapFactory@0x20fAfD2B…(arbitrum), OREO@0x319e222D…(arbitrum); indicators matched: initialize_without_modifier
    - 1/1 live proxies read a zero ERC-7201 Initializable slot (inconclusive alone: older OZ versions store the flag elsewhere)
    - 1 proxy/proxies expose a non-zero owner()
- **Preconditions PRESENT:** src::initialize_without_modifier, upgradeable_architecture, initializer_flag_unset, live_value_or_approvals
- **Preconditions UNKNOWN:** none
- **Guards searched / found:** initializer_modifier_present, upgrade_timelocked / upgrade_timelocked
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Simulated re-initialization reverts (kills the pair); Contract is non-upgradeable and holds no approvals
- **Where to start:** Read the initialization slot on every live proxy/facet and simulate re-initialization from an unprivileged address; it must revert.
- **Evidence:** `protocols/deep_screened.jsonl#oreoswap|UPGRADE-INITIALIZER-REACHABLE-LIVE`, `protocols/onchain_probes.json#oreoswap`, `families/families.json#UPGRADE-INITIALIZER-REACHABLE-LIVE`
- **Disclosure channel:** https://oreoswap.finance/ · no audit link listed

### 7. Velvet V2  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking A — mechanism match):** 7
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

### 8. Zero Network  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking A — mechanism match):** 8
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

### 9. Caviar V1  —  `SIG-VERIFIER-DEFEATABLE`

- **Rank (Ranking A — mechanism match):** 9
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

### 10. UwU Lend  —  `ORACLE-SPOT-THIN-LIQUIDITY`

- **Rank (Ranking A — mechanism match):** 10
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

### 11. Charm Finance V1  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking A — mechanism match):** 11
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

### 12. deBridge  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — mechanism match):** 12
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

### 13. Ajna V1  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — mechanism match):** 13
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

### 14. Synapse Cross Chain Bridge  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — mechanism match):** 14
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

### 15. Contango V1  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking A — mechanism match):** 15
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

### 16. Lybra V1  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — mechanism match):** 16
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

### 17. Tarot  —  `ORACLE-SPOT-THIN-LIQUIDITY`

- **Rank (Ranking A — mechanism match):** 17
- **Protocol:** Tarot (`tarot`) · Lending · Base, Optimism, Fantom, Binance, Linea, Avalanche …
- **DefiLlama URL:** https://defillama.com/protocol/tarot
- **Value at risk (TVL):** $583,969  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
- **HACK_LIKELIHOOD: 60.61 / 100**
    - family evidence 29.52/40 (MATCH 73.8 × evidence-level weight 1.0) · hazard 14.09/25 · neglect 7/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 73.8 / 100 · **EVIDENCE_CONFIDENCE:** 90.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×3.61, category hazard ×1.49. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 7/25):**
    - `no_audit_listed` (+7) — no audit link listed by DefiLlama
- **Broken invariant this family tests:** Borrowing capacity, mint size, reward size or collateral value must not be derived from a price that a single actor can move within the manipulation window, and the value unlocked must never exceed the cost of moving that price.
    - Conditions observed: `PRICING_SURFACE_UNDECLARED`
    - Deployed source read (`TarotSolidlyPriceOracleV2` @ 0x4B6daE04…(base)): prerequisites matched: spot_without_twap; no guard found
    - deployed source read for TarotSolidlyPriceOracleV2@0x4B6daE04…(base); indicators matched: spot_without_twap
    - condition PRICING_SURFACE_UNDECLARED (PRIORITY): A lending, CDP, derivatives or curation archetype with no oracle declared at all: the pricing path is unmapped.
    - only one oracle (or none) is declared in DefiLlama metadata; this is a prioritisation signal about disclosure, not evidence that no cross-source deviation bound exists in code
    - declared oracles: none declared
- **Preconditions PRESENT:** src::spot_without_twap, value_decision_reads_configured_feed, live_positions_exposed
- **Preconditions UNKNOWN:** feed_selection_is_configuration
- **Guards searched / found:** twap_present, supply_cap_present, deviation_bound_vs_independent_source / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** All collateral priced by a deep aggregated feed with a deviation cap (kills the pair); Caps are set from measured venue depth and enforced on-chain; The action is sized from realised transfer amounts, so price is never an input
- **Where to start:** On a fork, execute a max-size flash-funded swap against every venue in the pricing path and assert that no value-bearing entrypoint changes its output beyond the configured deviation bound.
- **Evidence:** `protocols/deep_screened.jsonl#tarot|ORACLE-SPOT-THIN-LIQUIDITY`, `protocols/onchain_probes.json#tarot`, `families/families.json#ORACLE-SPOT-THIN-LIQUIDITY`
- **Disclosure channel:** https://www.tarot.to · no audit link listed

### 18. LandX Finance  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking A — mechanism match):** 18
- **Protocol:** LandX Finance (`landx-finance`) · RWA · Ethereum
- **DefiLlama URL:** https://defillama.com/protocol/landx-finance
- **Value at risk (TVL):** $1,578,688  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
    - Corroborating danger signals: a deployed-source pair already scores 73.8 at L4 guard review
- **HACK_LIKELIHOOD: 59.14 / 100**
    - family evidence 29.52/40 (MATCH 73.8 × evidence-level weight 1.0) · hazard 6.62/25 · neglect 14/25 · attacker economics 9.0/10
- **MATCH_SCORE:** 73.8 / 100 · **EVIDENCE_CONFIDENCE:** 90.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×2.54, category hazard ×0.46. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 14/25):**
    - `single_audit_only` (+2) — a single audit listed, with no indication it covers the current deployment
    - `dead_front_end` (+6) — front end is dead while contracts still hold value
    - `misrepresented_tokens` (+3) — DefiLlama cannot reconcile this protocol's reported token holdings
    - `no_timelock_in_source` (+3) — no timelock construct found in the source that was read
- **Broken invariant this family tests:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source read (`CToken` @ 0x0d9554CE…(ethereum), `XToken` @ 0x1B2B0FA9…(ethereum)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for CToken@0x0d9554CE…(ethereum), XToken@0x1B2B0FA9…(ethereum); indicators matched: unsafe_cross_sign_cast
- **Preconditions PRESENT:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain
- **Preconditions UNKNOWN:** none
- **Guards searched / found:** safecast_used / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#landx-finance|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#landx-finance`, `families/families.json#ACC-SIGN-OR-BOUND-CHECK-MISSING`
- **Disclosure channel:** not listed · audits: https://certificate.quantstamp.com/full/land-x-finance.pdf

### 19. Trevee Earn  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — mechanism match):** 19
- **Protocol:** Trevee Earn (`trevee-earn`) · Yield Aggregator · Sonic, Ethereum, Plasma
- **DefiLlama URL:** https://defillama.com/protocol/trevee-earn
- **Value at risk (TVL):** $973,621  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
    - Corroborating danger signals: a deployed-source pair already scores 73.8 at L4 guard review
- **HACK_LIKELIHOOD: 58.42 / 100**
    - family evidence 29.52/40 (MATCH 73.8 × evidence-level weight 1.0) · hazard 9.9/25 · neglect 9/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 73.8 / 100 · **EVIDENCE_CONFIDENCE:** 85.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×2.54, category hazard ×0.9. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 9/25):**
    - `no_audit_listed` (+7) — no audit link listed by DefiLlama
    - `rebranded` (+2) — operated under previous names, so old contracts may still be live
- **Broken invariant this family tests:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source read (`ZAMM` @ 0x00000000…(ethereum), `zCurve` @ 0x00000000…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), zCurve@0x00000000…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain
- **Preconditions UNKNOWN:** none
- **Guards searched / found:** merkle_proof_gate / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#trevee-earn|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#trevee-earn`, `families/families.json#AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`
- **Disclosure channel:** https://rings.money/ · no audit link listed

### 20. Impermax V2  —  `ORACLE-SPOT-THIN-LIQUIDITY`

- **Rank (Ranking A — mechanism match):** 20
- **Protocol:** Impermax V2 (`impermax-v2`) · Lending · Polygon, Ethereum, Base, Avalanche, Optimism, Arbitrum …
- **DefiLlama URL:** https://defillama.com/protocol/impermax-v2
- **Value at risk (TVL):** $596,796  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
- **HACK_LIKELIHOOD: 57.89 / 100**
    - family evidence 29.52/40 (MATCH 73.8 × evidence-level weight 1.0) · hazard 12.37/25 · neglect 6/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 73.8 / 100 · **EVIDENCE_CONFIDENCE:** 90.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×2.54, category hazard ×1.49. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 6/25):**
    - `single_audit_only` (+2) — a single audit listed, with no indication it covers the current deployment
    - `version_sibling_legacy` (+4) — a version sibling of a newer deployment still holds value
- **Broken invariant this family tests:** Borrowing capacity, mint size, reward size or collateral value must not be derived from a price that a single actor can move within the manipulation window, and the value unlocked must never exceed the cost of moving that price.
    - Conditions observed: `SINGLE_PRIMARY_ORACLE_NO_CROSSCHECK`
    - Deployed source read (`UniswapV2Pair` @ 0x08650bb9…(ethereum)): prerequisites matched: spot_without_twap; no guard found
    - deployed source read for UniswapV2Pair@0x08650bb9…(ethereum); indicators matched: spot_without_twap
    - condition SINGLE_PRIMARY_ORACLE_NO_CROSSCHECK (PRIORITY): Exactly one declared oracle and no declared secondary, so no cross-source deviation bound is declared.
    - only one oracle (or none) is declared in DefiLlama metadata; this is a prioritisation signal about disclosure, not evidence that no cross-source deviation bound exists in code
    - declared oracles: Chainlink (types: Primary)
- **Preconditions PRESENT:** src::spot_without_twap, value_decision_reads_configured_feed, live_positions_exposed
- **Preconditions UNKNOWN:** feed_selection_is_configuration
- **Guards searched / found:** twap_present, supply_cap_present, deviation_bound_vs_independent_source / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** All collateral priced by a deep aggregated feed with a deviation cap (kills the pair); Caps are set from measured venue depth and enforced on-chain; The action is sized from realised transfer amounts, so price is never an input
- **Where to start:** On a fork, execute a max-size flash-funded swap against every venue in the pricing path and assert that no value-bearing entrypoint changes its output beyond the configured deviation bound.
- **Evidence:** `protocols/deep_screened.jsonl#impermax-v2|ORACLE-SPOT-THIN-LIQUIDITY`, `protocols/onchain_probes.json#impermax-v2`, `families/families.json#ORACLE-SPOT-THIN-LIQUIDITY`
- **Disclosure channel:** https://impermax.finance/ · audits: https://github.com/Impermax-Finance/impermax-x-uniswapv2-core/tree/main/audit

### 21. Bunni V2  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — mechanism match):** 21
- **Protocol:** Bunni V2 (`bunni-v2`) · Dexs · Ethereum, Base, Unichain, Arbitrum, Binance
- **DefiLlama URL:** https://defillama.com/protocol/bunni-v2
- **Value at risk (TVL):** $213,436  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
    - Corroborating danger signals: a deployed-source pair already scores 73.8 at L4 guard review
- **HACK_LIKELIHOOD: 57.66 / 100**
    - family evidence 29.52/40 (MATCH 73.8 × evidence-level weight 1.0) · hazard 12.14/25 · neglect 6/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 73.8 / 100 · **EVIDENCE_CONFIDENCE:** 85.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×3.61, category hazard ×1.0. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 6/25):**
    - `single_audit_only` (+2) — a single audit listed, with no indication it covers the current deployment
    - `deprecated_flag` (+4) — DefiLlama deprecated flag (ambiguous on its own)
- **Broken invariant this family tests:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source read (`BunniHub` @ 0x00000000…(ethereum), `BunniHub` @ 0x000000dc…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for BunniHub@0x00000000…(ethereum), BunniHub@0x000000dc…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain
- **Preconditions UNKNOWN:** none
- **Guards searched / found:** merkle_proof_gate / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#bunni-v2|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#bunni-v2`, `families/families.json#AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`
- **Disclosure channel:** https://bunni.xyz/ · audits: https://docs.bunni.xyz/docs/v2/audits/

### 22. ether.fi Liquid  —  `SIG-VERIFIER-DEFEATABLE`

- **Rank (Ranking A — mechanism match):** 22
- **Protocol:** ether.fi Liquid (`ether.fi-liquid`) · Onchain Capital Allocator · Ethereum
- **DefiLlama URL:** https://defillama.com/protocol/ether.fi-liquid
- **Value at risk (TVL):** $388,960,571  ·  **Band:** `ABOVE_BAND_KEPT_EXPLICIT_DANGER` — above the band but retained: explicit specific danger evidence
    - Retained above the band on explicit danger: a deployed-source pair already scores 73.8 at L4 guard review
- **HACK_LIKELIHOOD: 56.69 / 100**
    - family evidence 29.52/40 (MATCH 73.8 × evidence-level weight 1.0) · hazard 8.67/25 · neglect 18/25 · attacker economics 0.5/10
- **MATCH_SCORE:** 73.8 / 100 · **EVIDENCE_CONFIDENCE:** 90.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×2.54, category hazard ×0.7. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 18/25):**
    - `no_audit_listed` (+7) — no audit link listed by DefiLlama
    - `misrepresented_tokens` (+3) — DefiLlama cannot reconcile this protocol's reported token holdings
    - `owner_is_zero_with_value` (+5) — owner() is the zero address while the contract still holds code and value
    - `no_timelock_in_source` (+3) — no timelock construct found in the source that was read
- **Broken invariant this family tests:** A verification routine must reject malformed, empty or zero-recovered signatures, and must never treat address(0) as a match.
    - Deployed source read (`AccountantWithRateProviders` @ 0x04B81368…(ethereum), `AccountantWithRateProviders` @ 0x075e6055…(ethereum)): prerequisites matched: ecrecover_without_zero_check; no guard found
    - deployed source read for AccountantWithRateProviders@0x04B81368…(ethereum), AccountantWithRateProviders@0x075e6055…(ethereum); indicators matched: ecrecover_without_zero_check
- **Preconditions PRESENT:** src::ecrecover_without_zero_check, live_value_present, deployment_reachable_on_chain
- **Preconditions UNKNOWN:** none
- **Guards searched / found:** uses_oz_ecdsa / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** OZ ECDSA library in the deployed bytecode (kills the ecrecover-zero shape); Signer address immutable and non-zero
- **Where to start:** On a fork, submit r=0,s=0,v=27 and an empty signature to every signature-gated entrypoint; all must revert.
- **Evidence:** `protocols/deep_screened.jsonl#ether.fi-liquid|SIG-VERIFIER-DEFEATABLE`, `protocols/onchain_probes.json#ether.fi-liquid`, `families/families.json#SIG-VERIFIER-DEFEATABLE`
- **Disclosure channel:** https://www.ether.fi · no audit link listed

### 23. Silo V2  —  `ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE`

- **Rank (Ranking A — mechanism match):** 23
- **Protocol:** Silo V2 (`silo-v2`) · Lending · Avalanche, Sonic, Arbitrum, Ethereum
- **DefiLlama URL:** https://defillama.com/protocol/silo-v2
- **Value at risk (TVL):** $5,866,437  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
    - Corroborating danger signals: condition IS_WINDOW_VICTIM_STILL_LIVE
- **HACK_LIKELIHOOD: 57.77 / 100**
    - family evidence 26.4/40 (MATCH 66.0 × evidence-level weight 1.0) · hazard 12.37/25 · neglect 12/25 · attacker economics 7.0/10
- **MATCH_SCORE:** 66.0 / 100 · **EVIDENCE_CONFIDENCE:** 90.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×2.54, category hazard ×1.49. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 12/25):**
    - `single_audit_only` (+2) — a single audit listed, with no indication it covers the current deployment
    - `is_window_victim` (+6) — exploited inside the six-month window and still listed
    - `version_sibling_legacy` (+4) — a version sibling of a newer deployment still holds value
- **Broken invariant this family tests:** A vault share rate is an accounting quantity of another protocol, not a market price. Using it as a feed imports every way that vault's rate can be moved, including donation inflation and same-transaction redemption effects.
    - Deployed source read (`Silo` @ 0x2433D6AC…(arbitrum)): prerequisites matched: rate_used_as_price; no guard found
    - deployed source read for Silo@0x2433D6AC…(arbitrum); indicators matched: rate_used_as_price
    - protocol declares a Fallback/Secondary oracle: fallback selection logic exists by its own declaration
    - declared oracles: RedStone, eOracle, Chainlink (types: Primary, Secondary)
- **Preconditions PRESENT:** src::rate_used_as_price, value_decision_reads_configured_feed, fallback_selection_logic_exists, live_positions_exposed
- **Preconditions UNKNOWN:** feed_selection_is_configuration
- **Guards searched / found:** deviation_bound_vs_independent_source / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Growth-capped rate adapter in the deployed oracle (kills the pair); Wrapper's own rate is monotonic and rate-limited; Collateral priced by an independent market feed instead
- **Where to start:** On a fork, donate to and cycle the underlying vault; assert the lending market's reported collateral price moves no more than the configured cap.
- **Evidence:** `protocols/deep_screened.jsonl#silo-v2|ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE`, `protocols/onchain_probes.json#silo-v2`, `families/families.json#ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE`
- **Disclosure channel:** https://app.silo.finance · audits: https://docs.silo.finance/audits-and-tests

### 24. Percent Finance  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking A — mechanism match):** 24
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

### 25. GoPlus Locker V2  —  `ACC-CREDIT-NOT-RECEIVED`

- **Rank (Ranking A — mechanism match):** 25
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

### 26. DOOAR V2  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — mechanism match):** 26
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

### 27. Strata Season 0  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — mechanism match):** 27
- **Protocol:** Strata Season 0 (`strata-season-0`) · Farm · Ethereum
- **DefiLlama URL:** https://defillama.com/protocol/strata-season-0
- **Value at risk (TVL):** $189,859  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
- **HACK_LIKELIHOOD: 60.76 / 100**
    - family evidence 25.52/40 (MATCH 63.8 × evidence-level weight 1.0) · hazard 23.24/25 · neglect 2/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 63.8 / 100 · **EVIDENCE_CONFIDENCE:** 90.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×2.54, category hazard ×13.74. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 2/25):**
    - `single_audit_only` (+2) — a single audit listed, with no indication it covers the current deployment
- **Broken invariant this family tests:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source read (`pUSDeVault` @ 0x7fe8d7ef…(ethereum)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for pUSDeVault@0x7fe8d7ef…(ethereum); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain
- **Preconditions UNKNOWN:** none
- **Guards searched / found:** none / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#strata-season-0|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#strata-season-0`, `families/families.json#HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`
- **Disclosure channel:** https://strata.markets · audits: https://docs.strata.markets/technical-documentation/audits

### 28. Midas Capital  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking A — mechanism match):** 28
- **Protocol:** Midas Capital (`midas-capital`) · Lending · Binance, Arbitrum, Polygon, Moonbeam
- **DefiLlama URL:** https://defillama.com/protocol/midas-capital
- **Value at risk (TVL):** $103,382  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
- **HACK_LIKELIHOOD: 60.61 / 100**
    - family evidence 25.52/40 (MATCH 63.8 × evidence-level weight 1.0) · hazard 14.09/25 · neglect 11/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 63.8 / 100 · **EVIDENCE_CONFIDENCE:** 85.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×3.61, category hazard ×1.49. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 11/25):**
    - `single_audit_only` (+2) — a single audit listed, with no indication it covers the current deployment
    - `dead_front_end` (+6) — front end is dead while contracts still hold value
    - `no_timelock_in_source` (+3) — no timelock construct found in the source that was read
- **Broken invariant this family tests:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source read (`StakingPool` @ 0x004c0908…(bsc), `StakingPool` @ 0x04493F71…(bsc)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for StakingPool@0x004c0908…(bsc), StakingPool@0x04493F71…(bsc); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain
- **Preconditions UNKNOWN:** none
- **Guards searched / found:** none / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#midas-capital|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#midas-capital`, `families/families.json#AUTH-ZERO-ADDRESS-ACCEPTED`
- **Disclosure channel:** not listed · audits: https://medium.com/midas-capital/audit-with-zellic-29b63f1be25a

### 29. Spectra V1  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking A — mechanism match):** 29
- **Protocol:** Spectra V1 (`spectra-v1`) · Yield Aggregator · Polygon, Ethereum
- **DefiLlama URL:** https://defillama.com/protocol/spectra-v1
- **Value at risk (TVL):** $197,403  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
- **HACK_LIKELIHOOD: 59.42 / 100**
    - family evidence 25.52/40 (MATCH 63.8 × evidence-level weight 1.0) · hazard 9.9/25 · neglect 14/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 63.8 / 100 · **EVIDENCE_CONFIDENCE:** 85.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×2.54, category hazard ×0.9. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 14/25):**
    - `no_audit_listed` (+7) — no audit link listed by DefiLlama
    - `version_sibling_legacy` (+4) — a version sibling of a newer deployment still holds value
    - `no_timelock_in_source` (+3) — no timelock construct found in the source that was read
- **Broken invariant this family tests:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source read (`AdminUpgradeabilityProxy` @ 0x6646A35e…(ethereum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for AdminUpgradeabilityProxy@0x6646A35e…(ethereum); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain
- **Preconditions UNKNOWN:** none
- **Guards searched / found:** none / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#spectra-v1|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#spectra-v1`, `families/families.json#AUTH-ZERO-ADDRESS-ACCEPTED`
- **Disclosure channel:** https://www.spectra.finance/ · no audit link listed

### 30. BoringDAO  —  `ACC-DUPLICATE-ID-ACCUMULATION`

- **Rank (Ranking A — mechanism match):** 30
- **Protocol:** BoringDAO (`boringdao`) · Cross Chain Bridge · Litecoin, Polygon, Doge, Ethereum, Avalanche, OKExChain …
- **DefiLlama URL:** https://defillama.com/protocol/boringdao
- **Value at risk (TVL):** $337,559  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
- **HACK_LIKELIHOOD: 58.91 / 100**
    - family evidence 25.52/40 (MATCH 63.8 × evidence-level weight 1.0) · hazard 18.39/25 · neglect 5/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 63.8 / 100 · **EVIDENCE_CONFIDENCE:** 85.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×3.61, category hazard ×3.59. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 5/25):**
    - `single_audit_only` (+2) — a single audit listed, with no indication it covers the current deployment
    - `no_timelock_in_source` (+3) — no timelock construct found in the source that was read
- **Broken invariant this family tests:** An entitlement attached to an identifier may be counted at most once per period. A caller-supplied ID list must be deduplicated, or each ID's claim state consumed before the next read.
    - Deployed source read (`OToken` @ 0x07C44B5A…(ethereum), `BoringSatelliteChef` @ 0x204c87CD…(ethereum)): prerequisites matched: id_array_loop_without_dedup; no guard found
    - deployed source read for OToken@0x07C44B5A…(ethereum), BoringSatelliteChef@0x204c87CD…(ethereum); indicators matched: id_array_loop_without_dedup
- **Preconditions PRESENT:** src::id_array_loop_without_dedup, live_value_present, deployment_reachable_on_chain
- **Preconditions UNKNOWN:** none
- **Guards searched / found:** none / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Consumed marker written inside the loop (kills the pair); IDs required strictly increasing
- **Where to start:** On a fork, call the batch function with one ID repeated k times; payout must equal the single-ID payout.
- **Evidence:** `protocols/deep_screened.jsonl#boringdao|ACC-DUPLICATE-ID-ACCUMULATION`, `protocols/onchain_probes.json#boringdao`, `families/families.json#ACC-DUPLICATE-ID-ACCUMULATION`
- **Disclosure channel:** https://www.boringdao.com/ · audits: https://github.com/BoringDAO/boringDAO-contract/blob/master/peckshield-audit-report-boringdao-v1.0rc.pdf

### 31. Bond Protocol  —  `SIG-DIGEST-AMBIGUOUS-OR-UNBOUND`

- **Rank (Ranking A — mechanism match):** 31
- **Protocol:** Bond Protocol (`bond-protocol`) · Services · Ethereum, Arbitrum
- **DefiLlama URL:** https://defillama.com/protocol/bond-protocol
- **Value at risk (TVL):** $86,442  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
- **HACK_LIKELIHOOD: 57.19 / 100**
    - family evidence 25.52/40 (MATCH 63.8 × evidence-level weight 1.0) · hazard 8.67/25 · neglect 13/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 63.8 / 100 · **EVIDENCE_CONFIDENCE:** 90.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×2.54, category hazard ×0.7. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 13/25):**
    - `no_audit_listed` (+7) — no audit link listed by DefiLlama
    - `dead_front_end` (+6) — front end is dead while contracts still hold value
- **Broken invariant this family tests:** Every field that changes the economic effect of an authorised action must be inside the signed digest, and the encoding must be injective so no two distinct messages hash equal.
    - Deployed source read (`BondFixedExpiryTeller` @ 0x007FE70d…(ethereum), `BondFixedTermTeller` @ 0x007f7735…(ethereum)): prerequisites matched: encodePacked_multi_dynamic; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): eip712_typehash_present=yes
    - deployed source read for BondFixedExpiryTeller@0x007FE70d…(ethereum), BondFixedTermTeller@0x007f7735…(ethereum); indicators matched: encodePacked_multi_dynamic, eip712_typehash_present
- **Preconditions PRESENT:** src::encodePacked_multi_dynamic, live_value_present, deployment_reachable_on_chain
- **Preconditions UNKNOWN:** none
- **Guards searched / found:** none / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Typehash field set equals the function parameter set (kills the pair); abi.encode used throughout
- **Where to start:** On a fork, take a valid signature and vary each unsigned parameter; every variation must revert.
- **Evidence:** `protocols/deep_screened.jsonl#bond-protocol|SIG-DIGEST-AMBIGUOUS-OR-UNBOUND`, `protocols/onchain_probes.json#bond-protocol`, `families/families.json#SIG-DIGEST-AMBIGUOUS-OR-UNBOUND`
- **Disclosure channel:** not listed · no audit link listed

### 32. Aloe  —  `ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE`

- **Rank (Ranking A — mechanism match):** 32
- **Protocol:** Aloe (`aloe`) · Lending · Arbitrum, Base, Optimism, Linea, Ethereum
- **DefiLlama URL:** https://defillama.com/protocol/aloe
- **Value at risk (TVL):** $71,560  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
- **HACK_LIKELIHOOD: 55.89 / 100**
    - family evidence 25.52/40 (MATCH 63.8 × evidence-level weight 1.0) · hazard 12.37/25 · neglect 8/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 63.8 / 100 · **EVIDENCE_CONFIDENCE:** 90.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×2.54, category hazard ×1.49. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 8/25):**
    - `single_audit_only` (+2) — a single audit listed, with no indication it covers the current deployment
    - `dead_front_end` (+6) — front end is dead while contracts still hold value
- **Broken invariant this family tests:** A vault share rate is an accounting quantity of another protocol, not a market price. Using it as a feed imports every way that vault's rate can be moved, including donation inflation and same-transaction redemption effects.
    - Deployed source read (`Factory` @ 0x00000000…(arbitrum)): prerequisites matched: rate_used_as_price; no guard found
    - deployed source read for Factory@0x00000000…(arbitrum); indicators matched: rate_used_as_price
    - only one oracle (or none) is declared in DefiLlama metadata; this is a prioritisation signal about disclosure, not evidence that no cross-source deviation bound exists in code
    - declared oracles: TWAP (types: Primary)
- **Preconditions PRESENT:** src::rate_used_as_price, value_decision_reads_configured_feed, live_positions_exposed
- **Preconditions UNKNOWN:** feed_selection_is_configuration
- **Guards searched / found:** deviation_bound_vs_independent_source / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Growth-capped rate adapter in the deployed oracle (kills the pair); Wrapper's own rate is monotonic and rate-limited; Collateral priced by an independent market feed instead
- **Where to start:** On a fork, donate to and cycle the underlying vault; assert the lending market's reported collateral price moves no more than the configured cap.
- **Evidence:** `protocols/deep_screened.jsonl#aloe|ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE`, `protocols/onchain_probes.json#aloe`, `families/families.json#ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE`
- **Disclosure channel:** not listed · audits: https://github.com/aloelabs/aloe-ii/tree/master/audits

### 33. Set Protocol  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking A — mechanism match):** 33
- **Protocol:** Set Protocol (`set-protocol`) · Indexes · Ethereum
- **DefiLlama URL:** https://defillama.com/protocol/set-protocol
- **Value at risk (TVL):** $12,301,047  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
    - Corroborating danger signals: condition IS_WINDOW_VICTIM_STILL_LIVE
- **HACK_LIKELIHOOD: 55.83 / 100**
    - family evidence 25.52/40 (MATCH 63.8 × evidence-level weight 1.0) · hazard 11.31/25 · neglect 14/25 · attacker economics 5.0/10
- **MATCH_SCORE:** 63.8 / 100 · **EVIDENCE_CONFIDENCE:** 85.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×2.54, category hazard ×1.2. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 14/25):**
    - `single_audit_only` (+2) — a single audit listed, with no indication it covers the current deployment
    - `dead_front_end` (+6) — front end is dead while contracts still hold value
    - `is_window_victim` (+6) — exploited inside the six-month window and still listed
- **Broken invariant this family tests:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source read (`CErc20` @ 0x39AA39c0…(ethereum), `Vault` @ 0x5B67871C…(ethereum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for CErc20@0x39AA39c0…(ethereum), Vault@0x5B67871C…(ethereum); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain
- **Preconditions UNKNOWN:** none
- **Guards searched / found:** none / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#set-protocol|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#set-protocol`, `families/families.json#AUTH-ZERO-ADDRESS-ACCEPTED`
- **Disclosure channel:** not listed · audits: https://www.tokensets.com/#/security

### 34. SATO  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — mechanism match):** 34
- **Protocol:** SATO (`sato`) · Dexs · Ethereum
- **DefiLlama URL:** https://defillama.com/protocol/sato
- **Value at risk (TVL):** $2,717,624  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
- **HACK_LIKELIHOOD: 54.94 / 100**
    - family evidence 25.52/40 (MATCH 63.8 × evidence-level weight 1.0) · hazard 10.42/25 · neglect 10/25 · attacker economics 9.0/10
- **MATCH_SCORE:** 63.8 / 100 · **EVIDENCE_CONFIDENCE:** 90.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×2.54, category hazard ×1.0. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 10/25):**
    - `no_audit_listed` (+7) — no audit link listed by DefiLlama
    - `no_timelock_in_source` (+3) — no timelock construct found in the source that was read
- **Broken invariant this family tests:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source read (`SatoHook` @ 0x0000f07d…(ethereum)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for SatoHook@0x0000f07d…(ethereum); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain
- **Preconditions UNKNOWN:** none
- **Guards searched / found:** none / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#sato|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#sato`, `families/families.json#HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`
- **Disclosure channel:** not listed · no audit link listed

### 35. Capyfi  —  `ACC-DONATION-UNACCOUNTED-BALANCE`

- **Rank (Ranking A — mechanism match):** 35
- **Protocol:** Capyfi (`capyfi`) · Lending · Ethereum, LaChain Network, World Chain
- **DefiLlama URL:** https://defillama.com/protocol/capyfi
- **Value at risk (TVL):** $6,641,113  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
    - Corroborating danger signals: a deployed-source pair already scores 78.8 at L4 guard review
- **HACK_LIKELIHOOD: 54.89 / 100**
    - family evidence 25.52/40 (MATCH 63.8 × evidence-level weight 1.0) · hazard 12.37/25 · neglect 10/25 · attacker economics 7.0/10
- **MATCH_SCORE:** 63.8 / 100 · **EVIDENCE_CONFIDENCE:** 90.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×2.54, category hazard ×1.49. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 10/25):**
    - `no_audit_listed` (+7) — no audit link listed by DefiLlama
    - `no_timelock_in_source` (+3) — no timelock construct found in the source that was read
- **Broken invariant this family tests:** A share price, exchange rate or totalAssets must be a function of value the protocol accounted for on entry. Reading a raw balance makes any direct transfer into the accounting boundary an unpriced increase in every holder's claim.
    - Deployed source read (`CErc20Immutable` @ 0x004c0908…(ethereum), `TransparentUpgradeableProxy` @ 0x02451015…(ethereum)): prerequisites matched: getCashPrior_balanceOf; no guard found
    - deployed source read for CErc20Immutable@0x004c0908…(ethereum), TransparentUpgradeableProxy@0x02451015…(ethereum); indicators matched: getCashPrior_balanceOf
- **Preconditions PRESENT:** src::getCashPrior_balanceOf, unprivileged_inbound_transfer_possible, live_value_exposed
- **Preconditions UNKNOWN:** src::totalAssets_reads_balanceOf
- **Guards searched / found:** internal_cash_counter / none found in the reviewed path
- **Prior-art status:** `KNOWN_ISSUE_DEPLOYMENT_STATUS_UNKNOWN` — The Compound-fork donation/exchange-rate vector is publicly documented and was raised in Venus's own Code4rena audit before the March 2026 THE-market exploit. Whether THIS deployment carries a fix is not established by read-only evidence.
- **What would falsify this:** totalAssets derived from an internal counter, not balanceOf (kills the pair); Rate is monotonic and rate-limited per block; Inbound transfers to the accounting boundary are rejected or swept to a reserve
- **Where to start:** On a fork, transfer an arbitrary amount of each counted asset directly into every accounting boundary; the share price, exchange rate and derived borrow power must not change.
- **Evidence:** `protocols/deep_screened.jsonl#capyfi|ACC-DONATION-UNACCOUNTED-BALANCE`, `protocols/onchain_probes.json#capyfi`, `families/families.json#ACC-DONATION-UNACCOUNTED-BALANCE`
- **Disclosure channel:** https://capyfi.com/ · no audit link listed

### 36. Segment Finance  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking A — mechanism match):** 36
- **Protocol:** Segment Finance (`segment-finance`) · Lending · BOB, Binance, BSquared, Op_Bnb, CORE, RSK
- **DefiLlama URL:** https://defillama.com/protocol/segment-finance
- **Value at risk (TVL):** $412,774  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
- **HACK_LIKELIHOOD: 54.61 / 100**
    - family evidence 25.52/40 (MATCH 63.8 × evidence-level weight 1.0) · hazard 14.09/25 · neglect 5/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 63.8 / 100 · **EVIDENCE_CONFIDENCE:** 85.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×3.61, category hazard ×1.49. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 5/25):**
    - `single_audit_only` (+2) — a single audit listed, with no indication it covers the current deployment
    - `no_timelock_in_source` (+3) — no timelock construct found in the source that was read
- **Broken invariant this family tests:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source read (`StakingPool` @ 0x004c0908…(bsc), `StakingPool` @ 0x04493F71…(bsc)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for StakingPool@0x004c0908…(bsc), StakingPool@0x04493F71…(bsc); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain
- **Preconditions UNKNOWN:** none
- **Guards searched / found:** none / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#segment-finance|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#segment-finance`, `families/families.json#AUTH-ZERO-ADDRESS-ACCEPTED`
- **Disclosure channel:** https://segment.finance · audits: https://1437394138-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FcYvodOcCalriGDOIk0m4%2Fuploads%2F2aV2FDinQ3TxtFSRRnqN%2FSegment_Finance_-_Public_Report.pdf?alt=media&token=f87acc83-c3b7-4caa-a5d4-cbc7d68dc21d

### 37. Yield Millionaire  —  `ACC-DONATION-UNACCOUNTED-BALANCE`

- **Rank (Ranking A — mechanism match):** 37
- **Protocol:** Yield Millionaire (`yield-millionaire`) · Yield · Base
- **DefiLlama URL:** https://defillama.com/protocol/yield-millionaire
- **Value at risk (TVL):** $71,289  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
- **HACK_LIKELIHOOD: 54.32 / 100**
    - family evidence 25.52/40 (MATCH 63.8 × evidence-level weight 1.0) · hazard 5.8/25 · neglect 13/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 63.8 / 100 · **EVIDENCE_CONFIDENCE:** 90.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×0.96, category hazard ×1.03. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 13/25):**
    - `no_audit_listed` (+7) — no audit link listed by DefiLlama
    - `dead_front_end` (+6) — front end is dead while contracts still hold value
- **Broken invariant this family tests:** A share price, exchange rate or totalAssets must be a function of value the protocol accounted for on entry. Reading a raw balance makes any direct transfer into the accounting boundary an unpriced increase in every holder's claim.
    - Deployed source read (`ATokenInstance` @ 0x273e4b97…(base), `AaveVault` @ 0x9c187591…(base)): prerequisites matched: totalAssets_reads_balanceOf; no guard found
    - deployed source read for ATokenInstance@0x273e4b97…(base), AaveVault@0x9c187591…(base); indicators matched: totalAssets_reads_balanceOf
- **Preconditions PRESENT:** src::totalAssets_reads_balanceOf, unprivileged_inbound_transfer_possible, live_value_exposed
- **Preconditions UNKNOWN:** src::getCashPrior_balanceOf
- **Guards searched / found:** internal_cash_counter / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** totalAssets derived from an internal counter, not balanceOf (kills the pair); Rate is monotonic and rate-limited per block; Inbound transfers to the accounting boundary are rejected or swept to a reserve
- **Where to start:** On a fork, transfer an arbitrary amount of each counted asset directly into every accounting boundary; the share price, exchange rate and derived borrow power must not change.
- **Evidence:** `protocols/deep_screened.jsonl#yield-millionaire|ACC-DONATION-UNACCOUNTED-BALANCE`, `protocols/onchain_probes.json#yield-millionaire`, `families/families.json#ACC-DONATION-UNACCOUNTED-BALANCE`
- **Disclosure channel:** not listed · no audit link listed

### 38. LiveArt  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — mechanism match):** 38
- **Protocol:** LiveArt (`liveart`) · RWA · Binance, Base
- **DefiLlama URL:** https://defillama.com/protocol/liveart
- **Value at risk (TVL):** $94,505  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
- **HACK_LIKELIHOOD: 53.86 / 100**
    - family evidence 25.52/40 (MATCH 63.8 × evidence-level weight 1.0) · hazard 8.34/25 · neglect 10/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 63.8 / 100 · **EVIDENCE_CONFIDENCE:** 90.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×3.61, category hazard ×0.46. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 10/25):**
    - `no_audit_listed` (+7) — no audit link listed by DefiLlama
    - `no_timelock_in_source` (+3) — no timelock construct found in the source that was read
- **Broken invariant this family tests:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source read (`RwaToken` @ 0xfb2c5c72…(bsc), `CustomV3PriceFeed` @ 0x8eB682Cd…(bsc)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for RwaToken@0xfb2c5c72…(bsc), CustomV3PriceFeed@0x8eB682Cd…(bsc); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain
- **Preconditions UNKNOWN:** none
- **Guards searched / found:** none / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#liveart|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#liveart`, `families/families.json#HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`
- **Disclosure channel:** https://liveart.io/ · no audit link listed

### 39. Monolith Market  —  `ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE`

- **Rank (Ranking A — mechanism match):** 39
- **Protocol:** Monolith Market (`monolith-market`) · CDP · Ethereum
- **DefiLlama URL:** https://defillama.com/protocol/monolith-market
- **Value at risk (TVL):** $244,782  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
- **HACK_LIKELIHOOD: 53.62 / 100**
    - family evidence 25.52/40 (MATCH 63.8 × evidence-level weight 1.0) · hazard 11.1/25 · neglect 7/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 63.8 / 100 · **EVIDENCE_CONFIDENCE:** 90.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×2.54, category hazard ×1.15. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 7/25):**
    - `no_audit_listed` (+7) — no audit link listed by DefiLlama
- **Broken invariant this family tests:** A vault share rate is an accounting quantity of another protocol, not a market price. Using it as a feed imports every way that vault's rate can be moved, including donation inflation and same-transaction redemption effects.
    - Deployed source read (`Factory` @ 0x6D961c9D…(ethereum)): prerequisites matched: rate_used_as_price; no guard found
    - deployed source read for Factory@0x6D961c9D…(ethereum); indicators matched: rate_used_as_price
    - only one oracle (or none) is declared in DefiLlama metadata; this is a prioritisation signal about disclosure, not evidence that no cross-source deviation bound exists in code
    - declared oracles: none declared
- **Preconditions PRESENT:** src::rate_used_as_price, value_decision_reads_configured_feed, live_positions_exposed
- **Preconditions UNKNOWN:** feed_selection_is_configuration
- **Guards searched / found:** deviation_bound_vs_independent_source / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Growth-capped rate adapter in the deployed oracle (kills the pair); Wrapper's own rate is monotonic and rate-limited; Collateral priced by an independent market feed instead
- **Where to start:** On a fork, donate to and cycle the underlying vault; assert the lending market's reported collateral price moves no more than the configured cap.
- **Evidence:** `protocols/deep_screened.jsonl#monolith-market|ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE`, `protocols/onchain_probes.json#monolith-market`, `families/families.json#ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE`
- **Disclosure channel:** https://monolith.market · no audit link listed

### 40. LOCKON  —  `ACC-DUPLICATE-ID-ACCUMULATION`

- **Rank (Ranking A — mechanism match):** 40
- **Protocol:** LOCKON (`lockon`) · Indexes · Polygon, Arbitrum
- **DefiLlama URL:** https://defillama.com/protocol/lockon
- **Value at risk (TVL):** $1,098,825  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
    - Corroborating danger signals: condition FORK_OF_WINDOW_VICTIM
- **HACK_LIKELIHOOD: 53.52 / 100**
    - family evidence 25.52/40 (MATCH 63.8 × evidence-level weight 1.0) · hazard 8.0/25 · neglect 11/25 · attacker economics 9.0/10
- **MATCH_SCORE:** 63.8 / 100 · **EVIDENCE_CONFIDENCE:** 85.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×1.29, category hazard ×1.2. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 11/25):**
    - `single_audit_only` (+2) — a single audit listed, with no indication it covers the current deployment
    - `fork_of_window_victim` (+6) — forked from a protocol exploited inside the window
    - `no_timelock_in_source` (+3) — no timelock construct found in the source that was read
- **Broken invariant this family tests:** An entitlement attached to an identifier may be counted at most once per period. A caller-supplied ID list must be deduplicated, or each ID's claim state consumed before the next read.
    - Deployed source read (`Controller` @ 0xA36c2B06…(arbitrum)): prerequisites matched: id_array_loop_without_dedup; no guard found
    - deployed source read for Controller@0xA36c2B06…(arbitrum); indicators matched: id_array_loop_without_dedup
- **Preconditions PRESENT:** src::id_array_loop_without_dedup, live_value_present, deployment_reachable_on_chain
- **Preconditions UNKNOWN:** none
- **Guards searched / found:** none / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Consumed marker written inside the loop (kills the pair); IDs required strictly increasing
- **Where to start:** On a fork, call the batch function with one ID repeated k times; payout must equal the single-ID payout.
- **Evidence:** `protocols/deep_screened.jsonl#lockon|ACC-DUPLICATE-ID-ACCUMULATION`, `protocols/onchain_probes.json#lockon`, `families/families.json#ACC-DUPLICATE-ID-ACCUMULATION`
- **Disclosure channel:** https://lockon.finance · audits: https://gitlab.com/lockon-finance/core-contracts/-/tree/main/audits

### 41. Loop  —  `ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE`

- **Rank (Ranking A — mechanism match):** 41
- **Protocol:** Loop (`loop`) · Leveraged Farming · XDC, Ethereum, Binance, Scroll
- **DefiLlama URL:** https://defillama.com/protocol/loop
- **Value at risk (TVL):** $76,962  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
- **HACK_LIKELIHOOD: 53.05 / 100**
    - family evidence 25.52/40 (MATCH 63.8 × evidence-level weight 1.0) · hazard 15.53/25 · neglect 2/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 63.8 / 100 · **EVIDENCE_CONFIDENCE:** 90.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×3.61, category hazard ×2.0. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 2/25):**
    - `single_audit_only` (+2) — a single audit listed, with no indication it covers the current deployment
- **Broken invariant this family tests:** A vault share rate is an accounting quantity of another protocol, not a market price. Using it as a feed imports every way that vault's rate can be moved, including donation inflation and same-transaction redemption effects.
    - Deployed source read (`ERC165Plugin` @ 0x03C07e6d…(ethereum), `CDPVaultSpectra` @ 0x03d30243…(ethereum)): prerequisites matched: rate_used_as_price; no guard found
    - deployed source read for ERC165Plugin@0x03C07e6d…(ethereum), CDPVaultSpectra@0x03d30243…(ethereum); indicators matched: rate_used_as_price
    - only one oracle (or none) is declared in DefiLlama metadata; this is a prioritisation signal about disclosure, not evidence that no cross-source deviation bound exists in code
    - declared oracles: none declared
- **Preconditions PRESENT:** src::rate_used_as_price, value_decision_reads_configured_feed, live_positions_exposed
- **Preconditions UNKNOWN:** feed_selection_is_configuration
- **Guards searched / found:** deviation_bound_vs_independent_source / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Growth-capped rate adapter in the deployed oracle (kills the pair); Wrapper's own rate is monotonic and rate-limited; Collateral priced by an independent market feed instead
- **Where to start:** On a fork, donate to and cycle the underlying vault; assert the lending market's reported collateral price moves no more than the configured cap.
- **Evidence:** `protocols/deep_screened.jsonl#loop|ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE`, `protocols/onchain_probes.json#loop`, `families/families.json#ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE`
- **Disclosure channel:** https://www.loopfi.xyz/ · audits: https://code4rena.com/reports/2024-05-loop

### 42. Accumulated Finance Liquid Staking  —  `ACC-DONATION-UNACCOUNTED-BALANCE`

- **Rank (Ranking A — mechanism match):** 42
- **Protocol:** Accumulated Finance Liquid Staking (`accumulated-finance-liquid-staking`) · Liquid Staking · Sapphire, Bitkub, ZetaChain, Coti, Manta, Velas …
- **DefiLlama URL:** https://defillama.com/protocol/accumulated-finance-liquid-staking
- **Value at risk (TVL):** $622,677  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
- **HACK_LIKELIHOOD: 52.91 / 100**
    - family evidence 25.52/40 (MATCH 63.8 × evidence-level weight 1.0) · hazard 10.39/25 · neglect 7/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 63.8 / 100 · **EVIDENCE_CONFIDENCE:** 90.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×3.61, category hazard ×0.7. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 7/25):**
    - `no_audit_listed` (+7) — no audit link listed by DefiLlama
- **Broken invariant this family tests:** A share price, exchange rate or totalAssets must be a function of value the protocol accounted for on entry. Reading a raw balance makes any direct transfer into the accounting boundary an unpriced increase in every holder's claim.
    - Deployed source read (`wstVLX` @ 0x7AC168c8…(bsc), `stVLX` @ 0xcba2aeEc…(bsc)): prerequisites matched: totalAssets_reads_balanceOf; no guard found
    - deployed source read for wstVLX@0x7AC168c8…(bsc), stVLX@0xcba2aeEc…(bsc); indicators matched: totalAssets_reads_balanceOf
- **Preconditions PRESENT:** src::totalAssets_reads_balanceOf, unprivileged_inbound_transfer_possible, live_value_exposed
- **Preconditions UNKNOWN:** src::getCashPrior_balanceOf
- **Guards searched / found:** internal_cash_counter / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** totalAssets derived from an internal counter, not balanceOf (kills the pair); Rate is monotonic and rate-limited per block; Inbound transfers to the accounting boundary are rejected or swept to a reserve
- **Where to start:** On a fork, transfer an arbitrary amount of each counted asset directly into every accounting boundary; the share price, exchange rate and derived borrow power must not change.
- **Evidence:** `protocols/deep_screened.jsonl#accumulated-finance-liquid-staking|ACC-DONATION-UNACCOUNTED-BALANCE`, `protocols/onchain_probes.json#accumulated-finance-liquid-staking`, `families/families.json#ACC-DONATION-UNACCOUNTED-BALANCE`
- **Disclosure channel:** https://accumulated.finance/stake · no audit link listed

### 43. Joe V2  —  `ACC-DUPLICATE-ID-ACCUMULATION`

- **Rank (Ranking A — mechanism match):** 43
- **Protocol:** Joe V2 (`joe-v2`) · Dexs · Avalanche, Arbitrum, Binance
- **DefiLlama URL:** https://defillama.com/protocol/joe-v2
- **Value at risk (TVL):** $172,259  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
- **HACK_LIKELIHOOD: 52.66 / 100**
    - family evidence 25.52/40 (MATCH 63.8 × evidence-level weight 1.0) · hazard 12.14/25 · neglect 5/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 63.8 / 100 · **EVIDENCE_CONFIDENCE:** 85.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×3.61, category hazard ×1.0. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 5/25):**
    - `single_audit_only` (+2) — a single audit listed, with no indication it covers the current deployment
    - `no_timelock_in_source` (+3) — no timelock construct found in the source that was read
- **Broken invariant this family tests:** An entitlement attached to an identifier may be counted at most once per period. A caller-supplied ID list must be deduplicated, or each ID's claim state consumed before the next read.
    - Deployed source read (`LBFactory` @ 0x1886d09c…(arbitrum), `JoeTokenOFT` @ 0x371c7ec6…(arbitrum)): prerequisites matched: id_array_loop_without_dedup; no guard found
    - deployed source read for LBFactory@0x1886d09c…(arbitrum), JoeTokenOFT@0x371c7ec6…(arbitrum); indicators matched: id_array_loop_without_dedup
- **Preconditions PRESENT:** src::id_array_loop_without_dedup, live_value_present, deployment_reachable_on_chain
- **Preconditions UNKNOWN:** none
- **Guards searched / found:** none / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Consumed marker written inside the loop (kills the pair); IDs required strictly increasing
- **Where to start:** On a fork, call the batch function with one ID repeated k times; payout must equal the single-ID payout.
- **Evidence:** `protocols/deep_screened.jsonl#joe-v2|ACC-DUPLICATE-ID-ACCUMULATION`, `protocols/onchain_probes.json#joe-v2`, `families/families.json#ACC-DUPLICATE-ID-ACCUMULATION`
- **Disclosure channel:** https://lfj.gg/avalanche/trade · audits: https://github.com/abdk-consulting/audits/blob/main/traderjoe/ABDK_TraderJoe_TraderJoe_v_2_0.pdf

### 44. PICWE  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — mechanism match):** 44
- **Protocol:** PICWE (`picwe`) · Dexs · Binance, Arbitrum, Base
- **DefiLlama URL:** https://defillama.com/protocol/picwe
- **Value at risk (TVL):** $494,361  ·  **Band:** `IN_BAND` — inside the $50,000-$30,000,000 reviewable band
- **HACK_LIKELIHOOD: 52.66 / 100**
    - family evidence 25.52/40 (MATCH 63.8 × evidence-level weight 1.0) · hazard 12.14/25 · neglect 5/25 · attacker economics 10.0/10
- **MATCH_SCORE:** 63.8 / 100 · **EVIDENCE_CONFIDENCE:** 90.4 / 100 · **Evidence level:** `L4_GUARD_REVIEW`
- **Why this segment gets hit:** chain hazard ×3.61, category hazard ×1.0. Hazard is the share of in-window incidents divided by the share of eligible protocols, so ×1 is average and higher means over-represented among real victims.
- **Attention deficit (neglect 5/25):**
    - `single_audit_only` (+2) — a single audit listed, with no indication it covers the current deployment
    - `no_timelock_in_source` (+3) — no timelock construct found in the source that was read
- **Broken invariant this family tests:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source read (`RWAToken` @ 0x3fed4274…(bsc), `WeUSDMintRedeem` @ 0x5D54f109…(bsc)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for RWAToken@0x3fed4274…(bsc), WeUSDMintRedeem@0x5D54f109…(bsc); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain
- **Preconditions UNKNOWN:** none
- **Guards searched / found:** none / none found in the reviewed path
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed for this pair. Novelty is therefore NOT claimed.
- **What would falsify this:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#picwe|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#picwe`, `families/families.json#HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`
- **Disclosure channel:** https://www.picwe.org/en · audits: https://drive.google.com/file/d/12APmNFf_dy2HBnDof_u0mM03_5vKSPWN/view?usp=sharing

### 45. Guru Network Classic  —  `ORACLE-SPOT-THIN-LIQUIDITY`

- **Rank (Ranking A — mechanism match):** 45
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
