# Candidates — Ranking B — expected loss prevention

> **Discovery-stage output.** This file asserts no defect in any protocol named below. Each entry is a *high-priority defensive audit candidate*: evidence A, B and C match a family's prerequisites, evidence D remains unknown, and guard E would falsify the hypothesis. Every entry requires separate authorized verification in a local or pinned-fork environment before any conclusion is drawn. Selection here is a statement about where to look next, not about what will be found.

Ranking B answers: *where could a focused audit plausibly prevent the most loss?* It multiplies technical fit by evidence confidence, live exposure, family recency and a capped recurrence multiplier. It is a prioritisation heuristic, not a probability.

### 1. Flux Finance  —  `ORACLE-SPOT-THIN-LIQUIDITY`

- **Rank (Ranking B — expected loss prevention):** 1
- **Protocol:** Flux Finance (`flux-finance`)
- **DefiLlama URL:** https://defillama.com/protocol/flux-finance
- **Current TVL:** $44,535,722
- **Chains:** Ethereum
- **Category:** Lending
- **Matched family IDs:** `ORACLE-SPOT-THIN-LIQUIDITY` (other pairs generated for this protocol: ACC-DONATION-UNACCOUNTED-BALANCE, LIQUIDATION-ON-MANIPULABLE-VALUATION, ORACLE-STALE-OR-SILENT-FALLBACK)
- **Ranking:**
    - MATCH_SCORE: **77.3** / 100
    - EVIDENCE_CONFIDENCE: **89.0** / 100 (mapping 100, deployment parity 90, live state 85, corroboration 90, guard review 80)
    - PREVENTION_SCORE: **62.932** = MATCH 77.3 × CONF 89.0/100 × EXPOSURE 0.7709 × RECENCY 0.9884 × RECURRENCE 1.2
- **Evidence level:** `L4_GUARD_REVIEW`
- **Why the family applies:** Borrowing capacity, mint size, reward size or collateral value must not be derived from a price that a single actor can move within the manipulation window, and the value unlocked must never exceed the cost of moving that price.
    - Screening evidence: archetype applicable: category=Lending; description/methodology signals: borrow, collateral, yield; no audit link listed (prioritisation signal only, never evidence of a defect); sub-threshold high-fit: onchain_governance_authority; no oracle declared in DefiLlama metadata (unknown pricing path)
    - Deep-screen observations: declared oracles: none declared in DefiLlama metadata
- **Mandatory preconditions PRESENT:** value_decision_reads_configured_feed, live_positions_exposed, single_or_undeclared_oracle
- **Mandatory preconditions UNKNOWN:** feed_selection_is_configuration, failure_path_returns_usable_number
- **Decisive guards searched:** staleness_check_reverts, deviation_bound_vs_independent_source, caps_sized_to_venue_depth
- **Decisive guards found:** none found in the reviewed path
- **Live value / authority / approval relevance:** exposure basis $51,216,080; on-chain governance authority
- **Implementation and deployment status:** adapter `registries/compound.js` (READ_VIA_REGISTRY); 5 lending market(s) read on-chain; 2 adapter address(es) probed; 4 proxy implementation(s) resolved and reviewed; not flagged deprecated; no audit link listed
- **Prior-art status:** `KNOWN_ISSUE_DEPLOYMENT_STATUS_UNKNOWN` — Flux is a Compound V2 fork run by the Ondo team, audited through Code4rena, with a public Immunefi bug-bounty programme and Ondo DAO governance. Its collateral set includes tokenized treasuries (OUSG, backed by BlackRock BUIDL since the 2024 migration), which is precisely the pricing surface that failed in Solido Cash and Ploutos Money inside this window. The class of issue is publicly known; the deployed oracle's venue depth, deviation bounds and borrow caps were not resolved by read-only screening. (search scope: protocol documentation, Code4rena audit reference, Immunefi programme; per-market oracle adapter NOT decompiled)
- **What would falsify the hypothesis:** All collateral priced by a deep aggregated feed with a deviation cap (kills the pair); Caps are set from measured venue depth and enforced on-chain; The action is sized from realised transfer amounts, so price is never an input
- **Recommended audit focus:** On a fork, execute a max-size flash-funded swap against every venue in the pricing path and assert that no value-bearing entrypoint changes its output beyond the configured deviation bound.
    - Questions: Is every mandatory precondition present in the live deployment? · Is any decisive guard present in the deployed bytecode, not just the repository? · What live value, authority or approval is reachable through this path?
- **Evidence paths:** `protocols/deep_screened.jsonl#flux-finance|ORACLE-SPOT-THIN-LIQUIDITY`, `protocols/adapters_index.json#flux-finance`, `protocols/onchain_probes.json#flux-finance`, `families/families.json#ORACLE-SPOT-THIN-LIQUIDITY`, `sources/defillama/adapters/flux-finance__registries__compound.js`
- **Responsible disclosure channel, if public:** not listed in DefiLlama metadata

### 2. Sumer.money  —  `ACC-DONATION-UNACCOUNTED-BALANCE`

- **Rank (Ranking B — expected loss prevention):** 2
- **Protocol:** Sumer.money (`sumer.money`)
- **DefiLlama URL:** https://defillama.com/protocol/sumer.money
- **Current TVL:** $1,222,366
- **Chains:** Berachain, CORE, Meter, Arbitrum, Goat, Base, Ethereum, Binance …
- **Category:** Lending
- **Matched family IDs:** `ACC-DONATION-UNACCOUNTED-BALANCE`
- **Ranking:**
    - MATCH_SCORE: **100.0** / 100
    - EVIDENCE_CONFIDENCE: **89.0** / 100 (mapping 100, deployment parity 90, live state 85, corroboration 90, guard review 80)
    - PREVENTION_SCORE: **52.452** = MATCH 100.0 × CONF 89.0/100 × EXPOSURE 0.6087 × RECENCY 0.9221 × RECURRENCE 1.05
- **Evidence level:** `L4_GUARD_REVIEW`
- **Why the family applies:** A share price, exchange rate or totalAssets must be a function of value the protocol accounted for on entry. Reading a raw balance makes any direct transfer into the accounting boundary an unpriced increase in every holder's claim.
    - Screening evidence: archetype applicable: category=Lending; fork lineage matches a family upstream: Compound V2; dead front end with residual TVL; DefiLlama warning banner; sub-threshold high-fit: dead_front_end_with_residual_tvl, defillama_warning_banner
    - Deep-screen observations: deployed market implementation(s) resolved and read: CErc20 (followed from the delegator/beacon proxy); cash read from balanceOf(address(this))=yes; internal cash counter=absent; exchange-rate change cap=absent; 4 live market(s) read across 1 chain(s); sample: 0xe19fd48c… cash=3251229605 borrows=34908001; 0xb2ff02ee… cash=2390008889789943500516 borrows=None; 0x10a2e256… cash=10090862821276803587 borrows=None; fork lineage: Compound V2
- **Mandatory preconditions PRESENT:** rate_reads_raw_balance, unprivileged_inbound_transfer_possible, inflated_rate_consumed_by_value_decision, third_party_claims_exposed
- **Mandatory preconditions UNKNOWN:** none
- **Decisive guards searched:** internal_cash_counter, exchange_rate_change_cap, supply_cap_binds_rate
- **Decisive guards found:** none found in the reviewed path
- **Live value / authority / approval relevance:** exposure basis $1,222,366
- **Implementation and deployment status:** adapter `registries/compound.js` (READ_VIA_REGISTRY); 6 lending market(s) read on-chain; 4 proxy implementation(s) resolved and reviewed; not flagged deprecated; 1 audit link(s) listed
- **Prior-art status:** `KNOWN_ISSUE_DEPLOYMENT_STATUS_UNKNOWN` — The Compound-fork donation/exchange-rate vector is publicly documented and was raised in Venus's own Code4rena audit before the March 2026 THE-market exploit. Whether THIS deployment carries a fix is not established by the read-only evidence collected here. (search scope: family-level public prior art only; per-deployment audit-competition and advisory search NOT performed)
- **What would falsify the hypothesis:** totalAssets derived from an internal counter, not balanceOf (kills the pair); Rate is monotonic and rate-limited per block; Inbound transfers to the accounting boundary are rejected or swept to a reserve
- **Recommended audit focus:** On a fork, transfer an arbitrary amount of each counted asset directly into every accounting boundary; the share price, exchange rate and derived borrow power must not change.
    - Questions: Is every mandatory precondition present in the live deployment? · Is any decisive guard present in the deployed bytecode, not just the repository? · What live value, authority or approval is reachable through this path?
- **Evidence paths:** `protocols/deep_screened.jsonl#sumer.money|ACC-DONATION-UNACCOUNTED-BALANCE`, `protocols/adapters_index.json#sumer.money`, `protocols/onchain_probes.json#sumer.money`, `families/families.json#ACC-DONATION-UNACCOUNTED-BALANCE`, `sources/defillama/adapters/sumer.money__registries__compound.js`
- **Responsible disclosure channel, if public:** not listed in DefiLlama metadata · audits: https://docs.sumer.money/security/audits

### 3. Base Bridge  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking B — expected loss prevention):** 3
- **Protocol:** Base Bridge (`base-bridge`)
- **DefiLlama URL:** https://defillama.com/protocol/base-bridge
- **Current TVL:** $2,790,942,273
- **Chains:** Ethereum
- **Category:** Canonical Bridge
- **Matched family IDs:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
- **Ranking:**
    - MATCH_SCORE: **62.5** / 100
    - EVIDENCE_CONFIDENCE: **75.0** / 100 (mapping 100, deployment parity 55, live state 50, corroboration 90, guard review 80)
    - PREVENTION_SCORE: **47.321** = MATCH 62.5 × CONF 75.0/100 × EXPOSURE 0.9446 × RECENCY 0.8906 × RECURRENCE 1.2
- **Evidence level:** `L3_STATE`
- **Why the family applies:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - Screening evidence: archetype-agnostic family (applies to any archetype); DefiLlama deprecated flag (weight 16 for this family); no audit link listed (prioritisation signal only, never evidence of a defect); sub-threshold high-fit: deprecated_deployment_may_retain_live_exposure, bridge_authority_over_external_value; exposure tilt from TVL $2,790,942,273
    - Deep-screen observations: CAUTION: DefiLlama's `deprecated` flag is set but uncorroborated. That flag is also used when an adapter is superseded or its TVL is counted elsewhere, so on its own it does NOT establish an abandoned deployment. Treated as UNKNOWN (no positive score).; DefiLlama deprecated flag set with non-zero residual TVL
- **Mandatory preconditions PRESENT:** prior_version_still_callable, still_holds_value_or_authority
- **Mandatory preconditions UNKNOWN:** unmaintained_or_differing_code_path, not_paused
- **Decisive guards searched:** paused_and_drained, approvals_revoked
- **Decisive guards found:** none found in the reviewed path
- **Live value / authority / approval relevance:** exposure basis $2,790,942,273
- **Implementation and deployment status:** adapter `registries/sumTokens.js` (READ_VIA_REGISTRY); 4 adapter address(es) probed; deprecated flag set; no audit link listed
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, audit competitions, upstream advisories, postmortems and relevant forks was performed for this pair. Novelty is therefore NOT claimed and NO_PUBLIC_MATCH_FOUND is deliberately not used. (search scope: none performed for this pair)
- **What would falsify the hypothesis:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Recommended audit focus:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
    - Questions: Is every mandatory precondition present in the live deployment? · Is any decisive guard present in the deployed bytecode, not just the repository? · What live value, authority or approval is reachable through this path?
- **Evidence paths:** `protocols/deep_screened.jsonl#base-bridge|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/adapters_index.json#base-bridge`, `protocols/onchain_probes.json#base-bridge`, `families/families.json#UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `sources/defillama/adapters/base-bridge__registries__sumTokens.js`
- **Responsible disclosure channel, if public:** not listed in DefiLlama metadata

### 4. Sentora  —  `ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE`

- **Rank (Ranking B — expected loss prevention):** 4
- **Protocol:** Sentora (`sentora`)
- **DefiLlama URL:** https://defillama.com/protocol/sentora
- **Current TVL:** $2,417,461,031
- **Chains:** Ethereum, Ink, Solana, Tempo
- **Category:** Risk Curators
- **Matched family IDs:** `ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE` (other pairs generated for this protocol: ACC-NAV-SHAREPRICE-MANIPULABLE, ACC-ZERO-SUPPLY-INFLATION)
- **Ranking:**
    - MATCH_SCORE: **56.7** / 100
    - EVIDENCE_CONFIDENCE: **75.0** / 100 (mapping 100, deployment parity 55, live state 50, corroboration 90, guard review 80)
    - PREVENTION_SCORE: **36.44** = MATCH 56.7 × CONF 75.0/100 × EXPOSURE 0.9383 × RECENCY 0.9138 × RECURRENCE 1.0
- **Evidence level:** `L3_STATE`
- **Why the family applies:** A vault share rate is an accounting quantity of another protocol, not a market price. Using it as a feed imports every way that vault's rate can be moved, including donation inflation and same-transaction redemption effects.
    - Screening evidence: archetype applicable: category=Risk Curators; no audit link listed (prioritisation signal only, never evidence of a defect); sub-threshold high-fit: curator_authority_over_third_party_vaults; multi-chain surface (4 chains); single declared oracle: Chainlink
    - Deep-screen observations: declared oracles: Chainlink
- **Mandatory preconditions PRESENT:** value_decision_reads_configured_feed, feed_selection_is_configuration, single_or_undeclared_oracle
- **Mandatory preconditions UNKNOWN:** failure_path_returns_usable_number, live_positions_exposed
- **Decisive guards searched:** staleness_check_reverts, deviation_bound_vs_independent_source, caps_sized_to_venue_depth
- **Decisive guards found:** none found in the reviewed path
- **Live value / authority / approval relevance:** exposure basis $2,417,461,031
- **Implementation and deployment status:** adapter `sentora/index.js` (READ); 4 adapter address(es) probed; not flagged deprecated; no audit link listed
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, audit competitions, upstream advisories, postmortems and relevant forks was performed for this pair. Novelty is therefore NOT claimed and NO_PUBLIC_MATCH_FOUND is deliberately not used. (search scope: none performed for this pair)
- **What would falsify the hypothesis:** Growth-capped rate adapter in the deployed oracle (kills the pair); Wrapper's own rate is monotonic and rate-limited; Collateral priced by an independent market feed instead
- **Recommended audit focus:** On a fork, donate to and cycle the underlying vault; assert the lending market's reported collateral price moves no more than the configured cap.
    - Questions: Is every mandatory precondition present in the live deployment? · Is any decisive guard present in the deployed bytecode, not just the repository? · What live value, authority or approval is reachable through this path?
- **Evidence paths:** `protocols/deep_screened.jsonl#sentora|ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE`, `protocols/adapters_index.json#sentora`, `protocols/onchain_probes.json#sentora`, `families/families.json#ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE`, `sources/defillama/adapters/sentora__sentora__index.js`
- **Responsible disclosure channel, if public:** not listed in DefiLlama metadata

### 5. Saddle Finance  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking B — expected loss prevention):** 5
- **Protocol:** Saddle Finance (`saddle-finance`)
- **DefiLlama URL:** https://defillama.com/protocol/saddle-finance
- **Current TVL:** $945,997
- **Chains:** Ethereum, Arbitrum, Optimism, Aurora, Fantom, Evmos, Kava
- **Category:** Dexs
- **Matched family IDs:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY` (other pairs generated for this protocol: ACC-MULTI-PATH-CREDIT-DRIFT, AMM-POOL-RATIO-SKEW-EXTRACTION, ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED, CALLBACK-UNAUTHENTICATED-CALLER-USES-APPROVALS, GOV-CHEAP-CONTROL-NO-TIMELOCK)
- **Ranking:**
    - MATCH_SCORE: **75.0** / 100
    - EVIDENCE_CONFIDENCE: **75.0** / 100 (mapping 100, deployment parity 55, live state 50, corroboration 90, guard review 80)
    - PREVENTION_SCORE: **36.292** = MATCH 75.0 × CONF 75.0/100 × EXPOSURE 0.6037 × RECENCY 0.8906 × RECURRENCE 1.2
- **Evidence level:** `L3_STATE`
- **Why the family applies:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - Screening evidence: archetype-agnostic family (applies to any archetype); DefiLlama deprecated flag (weight 16 for this family); dead front end with residual TVL; misrepresentedTokens flag; sub-threshold high-fit: deprecated_deployment_may_retain_live_exposure, dead_front_end_with_residual_tvl, onchain_governance_authority
    - Deep-screen observations: DefiLlama deprecated flag set with non-zero residual TVL; front end dead; contracts still hold value
- **Mandatory preconditions PRESENT:** prior_version_still_callable, unmaintained_or_differing_code_path, still_holds_value_or_authority
- **Mandatory preconditions UNKNOWN:** not_paused
- **Decisive guards searched:** paused_and_drained, approvals_revoked
- **Decisive guards found:** none found in the reviewed path
- **Live value / authority / approval relevance:** exposure basis $1,087,896; on-chain governance authority
- **Implementation and deployment status:** adapter `saddle/index.js` (READ); 2 adapter address(es) probed; deprecated flag set; 3 audit link(s) listed
- **Prior-art status:** `KNOWN_FIX_DEPLOYED` — The Saddle DAO voted in SIP-54 to wind the protocol down, pausing all pools and dissolving the community multisig, and the contracts repository was archived read-only on 2026-02-10. Pausing is the decisive guard for this family. The hypothesis is therefore downgraded rather than promoted; residual DefiLlama TVL means value is still parked in paused contracts, so the remaining question is withdrawal-path liveness, not exploitability. (search scope: protocol docs, governance record (SIP-54) and repository state)
- **What would falsify the hypothesis:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Recommended audit focus:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
    - Questions: Is every mandatory precondition present in the live deployment? · Is any decisive guard present in the deployed bytecode, not just the repository? · What live value, authority or approval is reachable through this path?
- **Evidence paths:** `protocols/deep_screened.jsonl#saddle-finance|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/adapters_index.json#saddle-finance`, `protocols/onchain_probes.json#saddle-finance`, `families/families.json#UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `sources/defillama/adapters/saddle-finance__saddle__index.js`
- **Responsible disclosure channel, if public:** not listed in DefiLlama metadata · audits: https://github.com/saddle-finance/saddle-audits/blob/master/10-29-2020_Certik.pdf, https://blog.openzeppelin.com/saddle-contracts-audit

### 6. Extended Perps  —  `LIQUIDATION-ON-MANIPULABLE-VALUATION`

- **Rank (Ranking B — expected loss prevention):** 6
- **Protocol:** Extended Perps (`extended-perps`)
- **DefiLlama URL:** https://defillama.com/protocol/extended-perps
- **Current TVL:** $121,536,393
- **Chains:** Starknet, Ethereum
- **Category:** Derivatives
- **Matched family IDs:** `LIQUIDATION-ON-MANIPULABLE-VALUATION`
- **Ranking:**
    - MATCH_SCORE: **56.7** / 100
    - EVIDENCE_CONFIDENCE: **75.0** / 100 (mapping 100, deployment parity 55, live state 50, corroboration 90, guard review 80)
    - PREVENTION_SCORE: **35.855** = MATCH 56.7 × CONF 75.0/100 × EXPOSURE 0.8085 × RECENCY 0.9486 × RECURRENCE 1.1
- **Evidence level:** `L3_STATE`
- **Why the family applies:** A position may be liquidated only on a valuation that the liquidator cannot move, and the discount captured must not exceed the cost of moving the price.
    - Screening evidence: archetype applicable: category=Derivatives; description/methodology signals: margin, perp, collateral; no audit link listed (prioritisation signal only, never evidence of a defect); single declared oracle: Stork; exposure tilt from TVL $121,536,393
    - Deep-screen observations: declared oracles: Stork
- **Mandatory preconditions PRESENT:** value_decision_reads_configured_feed, feed_selection_is_configuration, single_or_undeclared_oracle
- **Mandatory preconditions UNKNOWN:** failure_path_returns_usable_number, live_positions_exposed
- **Decisive guards searched:** staleness_check_reverts, deviation_bound_vs_independent_source, caps_sized_to_venue_depth
- **Decisive guards found:** none found in the reviewed path
- **Live value / authority / approval relevance:** exposure basis $121,536,393
- **Implementation and deployment status:** adapter `registries/sumTokens.js` (READ_VIA_REGISTRY); 4 adapter address(es) probed; not flagged deprecated; no audit link listed
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, audit competitions, upstream advisories, postmortems and relevant forks was performed for this pair. Novelty is therefore NOT claimed and NO_PUBLIC_MATCH_FOUND is deliberately not used. (search scope: none performed for this pair)
- **What would falsify the hypothesis:** Deviation-capped, independently sourced price plus a grace period (kills the pair); Liquidations rate-limited per block; Collateral only in deep assets with caps sized to depth
- **Recommended audit focus:** On a fork, execute the largest flash-funded move available on each pricing venue and assert that no position becomes liquidatable beyond the configured deviation bound.
    - Questions: Is every mandatory precondition present in the live deployment? · Is any decisive guard present in the deployed bytecode, not just the repository? · What live value, authority or approval is reachable through this path?
- **Evidence paths:** `protocols/deep_screened.jsonl#extended-perps|LIQUIDATION-ON-MANIPULABLE-VALUATION`, `protocols/adapters_index.json#extended-perps`, `protocols/onchain_probes.json#extended-perps`, `families/families.json#LIQUIDATION-ON-MANIPULABLE-VALUATION`, `sources/defillama/adapters/extended-perps__registries__sumTokens.js`
- **Responsible disclosure channel, if public:** not listed in DefiLlama metadata

### 7. Cooler Loans  —  `ORACLE-SPOT-THIN-LIQUIDITY`

- **Rank (Ranking B — expected loss prevention):** 7
- **Protocol:** Cooler Loans (`cooler-loans`)
- **DefiLlama URL:** https://defillama.com/protocol/cooler-loans
- **Current TVL:** $217,378,305
- **Chains:** Ethereum
- **Category:** Lending
- **Matched family IDs:** `ORACLE-SPOT-THIN-LIQUIDITY`
- **Ranking:**
    - MATCH_SCORE: **48.3** / 100
    - EVIDENCE_CONFIDENCE: **75.0** / 100 (mapping 100, deployment parity 55, live state 50, corroboration 90, guard review 80)
    - PREVENTION_SCORE: **35.845** = MATCH 48.3 × CONF 75.0/100 × EXPOSURE 0.8337 × RECENCY 0.9884 × RECURRENCE 1.2
- **Evidence level:** `L3_STATE`
- **Why the family applies:** Borrowing capacity, mint size, reward size or collateral value must not be derived from a price that a single actor can move within the manipulation window, and the value unlocked must never exceed the cost of moving that price.
    - Screening evidence: archetype applicable: category=Lending; description/methodology signals: borrow, collateral, apr; no audit link listed (prioritisation signal only, never evidence of a defect); no oracle declared in DefiLlama metadata (unknown pricing path); exposure tilt from TVL $217,378,305
    - Deep-screen observations: declared oracles: none declared in DefiLlama metadata
- **Mandatory preconditions PRESENT:** value_decision_reads_configured_feed, single_or_undeclared_oracle
- **Mandatory preconditions UNKNOWN:** feed_selection_is_configuration, failure_path_returns_usable_number, live_positions_exposed
- **Decisive guards searched:** staleness_check_reverts, deviation_bound_vs_independent_source, caps_sized_to_venue_depth
- **Decisive guards found:** none found in the reviewed path
- **Live value / authority / approval relevance:** exposure basis $217,378,305
- **Implementation and deployment status:** adapter `cooler-loans/index.js` (READ); 4 adapter address(es) probed; not flagged deprecated; no audit link listed
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, audit competitions, upstream advisories, postmortems and relevant forks was performed for this pair. Novelty is therefore NOT claimed and NO_PUBLIC_MATCH_FOUND is deliberately not used. (search scope: none performed for this pair)
- **What would falsify the hypothesis:** All collateral priced by a deep aggregated feed with a deviation cap (kills the pair); Caps are set from measured venue depth and enforced on-chain; The action is sized from realised transfer amounts, so price is never an input
- **Recommended audit focus:** On a fork, execute a max-size flash-funded swap against every venue in the pricing path and assert that no value-bearing entrypoint changes its output beyond the configured deviation bound.
    - Questions: Is every mandatory precondition present in the live deployment? · Is any decisive guard present in the deployed bytecode, not just the repository? · What live value, authority or approval is reachable through this path?
- **Evidence paths:** `protocols/deep_screened.jsonl#cooler-loans|ORACLE-SPOT-THIN-LIQUIDITY`, `protocols/adapters_index.json#cooler-loans`, `protocols/onchain_probes.json#cooler-loans`, `families/families.json#ORACLE-SPOT-THIN-LIQUIDITY`, `sources/defillama/adapters/cooler-loans__cooler-loans__index.js`
- **Responsible disclosure channel, if public:** not listed in DefiLlama metadata

### 8. Granary Finance  —  `ORACLE-SPOT-THIN-LIQUIDITY`

- **Rank (Ranking B — expected loss prevention):** 8
- **Protocol:** Granary Finance (`granary-finance`)
- **DefiLlama URL:** https://defillama.com/protocol/granary-finance
- **Current TVL:** $169,396
- **Chains:** Optimism, Metis, Arbitrum, Binance, Avalanche, Fantom, Ethereum, Base
- **Category:** Lending
- **Matched family IDs:** `ORACLE-SPOT-THIN-LIQUIDITY`
- **Ranking:**
    - MATCH_SCORE: **65.7** / 100
    - EVIDENCE_CONFIDENCE: **86.0** / 100 (mapping 100, deployment parity 75, live state 85, corroboration 90, guard review 80)
    - PREVENTION_SCORE: **35.433** = MATCH 65.7 × CONF 86.0/100 × EXPOSURE 0.529 × RECENCY 0.9884 × RECURRENCE 1.2
- **Evidence level:** `L3_STATE`
- **Why the family applies:** Borrowing capacity, mint size, reward size or collateral value must not be derived from a price that a single actor can move within the manipulation window, and the value unlocked must never exceed the cost of moving that price.
    - Screening evidence: archetype applicable: category=Lending; description/methodology signals: borrow, collateral, yield; dead front end with residual TVL; no audit link listed (prioritisation signal only, never evidence of a defect); sub-threshold high-fit: dead_front_end_with_residual_tvl, onchain_governance_authority
    - Deep-screen observations: addresses-provider probe: 0x773E0277… priceOracle=None pool=None reserves=None owner=None; 0xC043BA54… priceOracle=None pool=None reserves=0 owner=0xe027880ceb; 0x872B9e8a… priceOracle=None pool=None reserves=0 owner=0xe027880ceb; addresses-provider owner is a live address: oracle re-registration is a configuration action, so feed-to-asset binding depends on that role, not on code; declared oracles: Chainlink
- **Mandatory preconditions PRESENT:** value_decision_reads_configured_feed, feed_selection_is_configuration, single_or_undeclared_oracle
- **Mandatory preconditions UNKNOWN:** failure_path_returns_usable_number, live_positions_exposed
- **Decisive guards searched:** staleness_check_reverts, deviation_bound_vs_independent_source, caps_sized_to_venue_depth
- **Decisive guards found:** none found in the reviewed path
- **Live value / authority / approval relevance:** exposure basis $194,806; on-chain governance authority
- **Implementation and deployment status:** adapter `registries/aave.js` (READ_VIA_REGISTRY); 5 addresses-provider(s) read; not flagged deprecated; no audit link listed
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, audit competitions, upstream advisories, postmortems and relevant forks was performed for this pair. Novelty is therefore NOT claimed and NO_PUBLIC_MATCH_FOUND is deliberately not used. (search scope: none performed for this pair)
- **What would falsify the hypothesis:** All collateral priced by a deep aggregated feed with a deviation cap (kills the pair); Caps are set from measured venue depth and enforced on-chain; The action is sized from realised transfer amounts, so price is never an input
- **Recommended audit focus:** On a fork, execute a max-size flash-funded swap against every venue in the pricing path and assert that no value-bearing entrypoint changes its output beyond the configured deviation bound.
    - Questions: Is every mandatory precondition present in the live deployment? · Is any decisive guard present in the deployed bytecode, not just the repository? · What live value, authority or approval is reachable through this path?
- **Evidence paths:** `protocols/deep_screened.jsonl#granary-finance|ORACLE-SPOT-THIN-LIQUIDITY`, `protocols/adapters_index.json#granary-finance`, `protocols/onchain_probes.json#granary-finance`, `families/families.json#ORACLE-SPOT-THIN-LIQUIDITY`, `sources/defillama/adapters/granary-finance__registries__aave.js`
- **Responsible disclosure channel, if public:** not listed in DefiLlama metadata

### 9. Curve LlamaLend  —  `ORACLE-SPOT-THIN-LIQUIDITY`

- **Rank (Ranking B — expected loss prevention):** 9
- **Protocol:** Curve LlamaLend (`curve-llamalend`)
- **DefiLlama URL:** https://defillama.com/protocol/curve-llamalend
- **Current TVL:** $78,074,979
- **Chains:** Ethereum, Arbitrum, Fraxtal, Optimism
- **Category:** Lending
- **Matched family IDs:** `ORACLE-SPOT-THIN-LIQUIDITY` (other pairs generated for this protocol: ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED, LIQUIDATION-ON-MANIPULABLE-VALUATION, ORACLE-STALE-OR-SILENT-FALLBACK)
- **Ranking:**
    - MATCH_SCORE: **48.3** / 100
    - EVIDENCE_CONFIDENCE: **75.0** / 100 (mapping 100, deployment parity 55, live state 50, corroboration 90, guard review 80)
    - PREVENTION_SCORE: **33.936** = MATCH 48.3 × CONF 75.0/100 × EXPOSURE 0.7893 × RECENCY 0.9884 × RECURRENCE 1.2
- **Evidence level:** `L3_STATE`
- **Why the family applies:** Borrowing capacity, mint size, reward size or collateral value must not be derived from a price that a single actor can move within the manipulation window, and the value unlocked must never exceed the cost of moving that price.
    - Screening evidence: archetype applicable: category=Lending; description/methodology signals: borrow, collateral; no audit link listed (prioritisation signal only, never evidence of a defect); multi-chain surface (4 chains); no oracle declared in DefiLlama metadata (unknown pricing path)
    - Deep-screen observations: declared oracles: none declared in DefiLlama metadata
- **Mandatory preconditions PRESENT:** value_decision_reads_configured_feed, single_or_undeclared_oracle
- **Mandatory preconditions UNKNOWN:** feed_selection_is_configuration, failure_path_returns_usable_number, live_positions_exposed
- **Decisive guards searched:** staleness_check_reverts, deviation_bound_vs_independent_source, caps_sized_to_venue_depth
- **Decisive guards found:** none found in the reviewed path
- **Live value / authority / approval relevance:** exposure basis $78,074,979
- **Implementation and deployment status:** adapter `llamalend-curve/index.js` (READ); 1 adapter address(es) probed; not flagged deprecated; no audit link listed
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, audit competitions, upstream advisories, postmortems and relevant forks was performed for this pair. Novelty is therefore NOT claimed and NO_PUBLIC_MATCH_FOUND is deliberately not used. (search scope: none performed for this pair)
- **What would falsify the hypothesis:** All collateral priced by a deep aggregated feed with a deviation cap (kills the pair); Caps are set from measured venue depth and enforced on-chain; The action is sized from realised transfer amounts, so price is never an input
- **Recommended audit focus:** On a fork, execute a max-size flash-funded swap against every venue in the pricing path and assert that no value-bearing entrypoint changes its output beyond the configured deviation bound.
    - Questions: Is every mandatory precondition present in the live deployment? · Is any decisive guard present in the deployed bytecode, not just the repository? · What live value, authority or approval is reachable through this path?
- **Evidence paths:** `protocols/deep_screened.jsonl#curve-llamalend|ORACLE-SPOT-THIN-LIQUIDITY`, `protocols/adapters_index.json#curve-llamalend`, `protocols/onchain_probes.json#curve-llamalend`, `families/families.json#ORACLE-SPOT-THIN-LIQUIDITY`, `sources/defillama/adapters/curve-llamalend__llamalend-curve__index.js`
- **Responsible disclosure channel, if public:** not listed in DefiLlama metadata

### 10. RockawayX  —  `ORACLE-STALE-OR-SILENT-FALLBACK`

- **Rank (Ranking B — expected loss prevention):** 10
- **Protocol:** RockawayX (`rockawayx`)
- **DefiLlama URL:** https://defillama.com/protocol/rockawayx
- **Current TVL:** $193,301,703
- **Chains:** Ethereum, Solana, Sei, Pharos, Binance, Etherlink, Base, Plume Mainnet
- **Category:** Risk Curators
- **Matched family IDs:** `ORACLE-STALE-OR-SILENT-FALLBACK` (other pairs generated for this protocol: ACC-NAV-SHAREPRICE-MANIPULABLE, ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE)
- **Ranking:**
    - MATCH_SCORE: **48.3** / 100
    - EVIDENCE_CONFIDENCE: **75.0** / 100 (mapping 100, deployment parity 55, live state 50, corroboration 90, guard review 80)
    - PREVENTION_SCORE: **32.826** = MATCH 48.3 × CONF 75.0/100 × EXPOSURE 0.8286 × RECENCY 0.9503 × RECURRENCE 1.15
- **Evidence level:** `L3_STATE`
- **Why the family applies:** A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
    - Screening evidence: archetype applicable: category=Risk Curators; no audit link listed (prioritisation signal only, never evidence of a defect); sub-threshold high-fit: curator_authority_over_third_party_vaults; multi-chain surface (8 chains); no oracle declared in DefiLlama metadata (unknown pricing path)
    - Deep-screen observations: declared oracles: none declared in DefiLlama metadata
- **Mandatory preconditions PRESENT:** value_decision_reads_configured_feed, single_or_undeclared_oracle
- **Mandatory preconditions UNKNOWN:** feed_selection_is_configuration, failure_path_returns_usable_number, live_positions_exposed
- **Decisive guards searched:** staleness_check_reverts, deviation_bound_vs_independent_source, caps_sized_to_venue_depth
- **Decisive guards found:** none found in the reviewed path
- **Live value / authority / approval relevance:** exposure basis $193,301,703
- **Implementation and deployment status:** adapter `rockawayx/index.js` (READ); 4 adapter address(es) probed; not flagged deprecated; no audit link listed
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, audit competitions, upstream advisories, postmortems and relevant forks was performed for this pair. Novelty is therefore NOT claimed and NO_PUBLIC_MATCH_FOUND is deliberately not used. (search scope: none performed for this pair)
- **What would falsify the hypothesis:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Recommended audit focus:** On a fork, force each configured feed to return zero, a stale timestamp, and a 10x/0.1x value; every value-bearing entrypoint must revert rather than transact.
    - Questions: Is every mandatory precondition present in the live deployment? · Is any decisive guard present in the deployed bytecode, not just the repository? · What live value, authority or approval is reachable through this path?
- **Evidence paths:** `protocols/deep_screened.jsonl#rockawayx|ORACLE-STALE-OR-SILENT-FALLBACK`, `protocols/adapters_index.json#rockawayx`, `protocols/onchain_probes.json#rockawayx`, `families/families.json#ORACLE-STALE-OR-SILENT-FALLBACK`, `sources/defillama/adapters/rockawayx__rockawayx__index.js`
- **Responsible disclosure channel, if public:** not listed in DefiLlama metadata

### 11. Grove Finance  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking B — expected loss prevention):** 11
- **Protocol:** Grove Finance (`grove-finance`)
- **DefiLlama URL:** https://defillama.com/protocol/grove-finance
- **Current TVL:** $2,387,522,579
- **Chains:** Ethereum, Base, Avalanche, Plume Mainnet
- **Category:** Onchain Capital Allocator
- **Matched family IDs:** `UPGRADE-INITIALIZER-REACHABLE-LIVE` (other pairs generated for this protocol: ORACLE-STALE-OR-SILENT-FALLBACK)
- **Ranking:**
    - MATCH_SCORE: **66.7** / 100
    - EVIDENCE_CONFIDENCE: **62.0** / 100 (mapping 100, deployment parity 55, live state 50, corroboration 90, guard review 15)
    - PREVENTION_SCORE: **32.208** = MATCH 66.7 × CONF 62.0/100 × EXPOSURE 0.9378 × RECENCY 0.8309 × RECURRENCE 1.0
- **Evidence level:** `L3_STATE`
- **Why the family applies:** After deployment, no caller may (re)establish ownership, admin, or implementation wiring. Initialization state must be provably consumed.
    - Screening evidence: archetype-agnostic family (applies to any archetype); description/methodology signals: proxy; no audit link listed (prioritisation signal only, never evidence of a defect); sub-threshold high-fit: curator_authority_over_third_party_vaults; multi-chain surface (4 chains)
    - Deep-screen observations: 1/4 probed adapter addresses are ERC-1967 proxies; implementations: 0x77684815f4
- **Mandatory preconditions PRESENT:** prior_version_still_callable, upgradeable_architecture, live_value_or_approvals
- **Mandatory preconditions UNKNOWN:** initializer_flag_unset
- **Decisive guards searched:** initializer_consumed, upgrade_timelocked
- **Decisive guards found:** none found in the reviewed path
- **Live value / authority / approval relevance:** exposure basis $2,387,522,579
- **Implementation and deployment status:** adapter `grove/index.js` (READ); 4 adapter address(es) probed; not flagged deprecated; no audit link listed
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, audit competitions, upstream advisories, postmortems and relevant forks was performed for this pair. Novelty is therefore NOT claimed and NO_PUBLIC_MATCH_FOUND is deliberately not used. (search scope: none performed for this pair)
- **What would falsify the hypothesis:** Simulated re-initialization reverts (kills the pair); Contract is non-upgradeable and holds no approvals
- **Recommended audit focus:** Read the initialization slot on every live proxy/facet and simulate re-initialization from an unprivileged address; it must revert.
    - Questions: Is every mandatory precondition present in the live deployment? · Is any decisive guard present in the deployed bytecode, not just the repository? · What live value, authority or approval is reachable through this path?
- **Evidence paths:** `protocols/deep_screened.jsonl#grove-finance|UPGRADE-INITIALIZER-REACHABLE-LIVE`, `protocols/adapters_index.json#grove-finance`, `protocols/onchain_probes.json#grove-finance`, `families/families.json#UPGRADE-INITIALIZER-REACHABLE-LIVE`, `sources/defillama/adapters/grove-finance__grove__index.js`
- **Responsible disclosure channel, if public:** not listed in DefiLlama metadata

### 12. Stability  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking B — expected loss prevention):** 12
- **Protocol:** Stability (`stability`)
- **DefiLlama URL:** https://defillama.com/protocol/stability
- **Current TVL:** $1,906,982
- **Chains:** Sonic, Base, Polygon, re.al
- **Category:** Liquidity Manager
- **Matched family IDs:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
- **Ranking:**
    - MATCH_SCORE: **62.5** / 100
    - EVIDENCE_CONFIDENCE: **75.0** / 100 (mapping 100, deployment parity 55, live state 50, corroboration 90, guard review 80)
    - PREVENTION_SCORE: **31.46** = MATCH 62.5 × CONF 75.0/100 × EXPOSURE 0.628 × RECENCY 0.8906 × RECURRENCE 1.2
- **Evidence level:** `L3_STATE`
- **Why the family applies:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - Screening evidence: archetype-agnostic family (applies to any archetype); DefiLlama deprecated flag (weight 16 for this family); no audit link listed (prioritisation signal only, never evidence of a defect); sub-threshold high-fit: deprecated_deployment_may_retain_live_exposure; multi-chain surface (4 chains)
    - Deep-screen observations: CAUTION: DefiLlama's `deprecated` flag is set but uncorroborated. That flag is also used when an adapter is superseded or its TVL is counted elsewhere, so on its own it does NOT establish an abandoned deployment. Treated as UNKNOWN (no positive score).; DefiLlama deprecated flag set with non-zero residual TVL
- **Mandatory preconditions PRESENT:** prior_version_still_callable, still_holds_value_or_authority
- **Mandatory preconditions UNKNOWN:** unmaintained_or_differing_code_path, not_paused
- **Decisive guards searched:** paused_and_drained, approvals_revoked
- **Decisive guards found:** none found in the reviewed path
- **Live value / authority / approval relevance:** exposure basis $1,906,982
- **Implementation and deployment status:** adapter `stability/index.js` (READ); 2 adapter address(es) probed; deprecated flag set; no audit link listed
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, audit competitions, upstream advisories, postmortems and relevant forks was performed for this pair. Novelty is therefore NOT claimed and NO_PUBLIC_MATCH_FOUND is deliberately not used. (search scope: none performed for this pair)
- **What would falsify the hypothesis:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Recommended audit focus:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
    - Questions: Is every mandatory precondition present in the live deployment? · Is any decisive guard present in the deployed bytecode, not just the repository? · What live value, authority or approval is reachable through this path?
- **Evidence paths:** `protocols/deep_screened.jsonl#stability|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/adapters_index.json#stability`, `protocols/onchain_probes.json#stability`, `families/families.json#UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `sources/defillama/adapters/stability__stability__index.js`
- **Responsible disclosure channel, if public:** not listed in DefiLlama metadata

### 13. Morpho Optimizer AaveV2  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking B — expected loss prevention):** 13
- **Protocol:** Morpho Optimizer AaveV2 (`morpho-optimizer-aavev2`)
- **DefiLlama URL:** https://defillama.com/protocol/morpho-optimizer-aavev2
- **Current TVL:** $138,237
- **Chains:** Ethereum
- **Category:** Lending
- **Matched family IDs:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY` (other pairs generated for this protocol: ACC-MULTI-PATH-CREDIT-DRIFT)
- **Ranking:**
    - MATCH_SCORE: **75.0** / 100
    - EVIDENCE_CONFIDENCE: **75.0** / 100 (mapping 100, deployment parity 55, live state 50, corroboration 90, guard review 80)
    - PREVENTION_SCORE: **30.905** = MATCH 75.0 × CONF 75.0/100 × EXPOSURE 0.5141 × RECENCY 0.8906 × RECURRENCE 1.2
- **Evidence level:** `L3_STATE`
- **Why the family applies:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - Screening evidence: archetype-agnostic family (applies to any archetype); description/methodology signals: v2; DefiLlama deprecated flag (weight 16 for this family); dead front end with residual TVL; DefiLlama warning banner
    - Deep-screen observations: DefiLlama deprecated flag set with non-zero residual TVL; front end dead; contracts still hold value
- **Mandatory preconditions PRESENT:** prior_version_still_callable, unmaintained_or_differing_code_path, still_holds_value_or_authority
- **Mandatory preconditions UNKNOWN:** not_paused
- **Decisive guards searched:** paused_and_drained, approvals_revoked
- **Decisive guards found:** none found in the reviewed path
- **Live value / authority / approval relevance:** exposure basis $138,237
- **Implementation and deployment status:** adapter `morpho-aave/index.js` (READ); 1 adapter address(es) probed; deprecated flag set; 1 audit link(s) listed
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, audit competitions, upstream advisories, postmortems and relevant forks was performed for this pair. Novelty is therefore NOT claimed and NO_PUBLIC_MATCH_FOUND is deliberately not used. (search scope: none performed for this pair)
- **What would falsify the hypothesis:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Recommended audit focus:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
    - Questions: Is every mandatory precondition present in the live deployment? · Is any decisive guard present in the deployed bytecode, not just the repository? · What live value, authority or approval is reachable through this path?
- **Evidence paths:** `protocols/deep_screened.jsonl#morpho-optimizer-aavev2|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/adapters_index.json#morpho-optimizer-aavev2`, `protocols/onchain_probes.json#morpho-optimizer-aavev2`, `families/families.json#UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `sources/defillama/adapters/morpho-optimizer-aavev2__morpho-aave__index.js`
- **Responsible disclosure channel, if public:** not listed in DefiLlama metadata · audits: https://docs.morpho.org/security-reviews

### 14. Stake DAO  —  `ORACLE-SPOT-THIN-LIQUIDITY`

- **Rank (Ranking B — expected loss prevention):** 14
- **Protocol:** Stake DAO (`stake-dao`)
- **DefiLlama URL:** https://defillama.com/protocol/stake-dao
- **Current TVL:** $138,809,701
- **Chains:** Ethereum, Base, Fraxtal, Arbitrum, Polygon, Optimism, Avalanche, Sonic …
- **Category:** Yield
- **Matched family IDs:** `ORACLE-SPOT-THIN-LIQUIDITY` (other pairs generated for this protocol: ACC-MULTI-PATH-CREDIT-DRIFT, ACC-REWARD-INDEX-INIT-AND-ORDERING, CALLBACK-STATE-LOCK-INCOMPLETE, CALLBACK-UNAUTHENTICATED-CALLER-USES-APPROVALS, GOV-CHEAP-CONTROL-NO-TIMELOCK, INCENTIVE-PER-ADDRESS-NO-SYBIL-COST, SETTLEMENT-EPOCH-BOUNDARY-CREDIT, SIG-REPLAY-CROSS-POSITION)
- **Ranking:**
    - MATCH_SCORE: **40.0** / 100
    - EVIDENCE_CONFIDENCE: **75.0** / 100 (mapping 100, deployment parity 55, live state 50, corroboration 90, guard review 80)
    - PREVENTION_SCORE: **29.188** = MATCH 40.0 × CONF 75.0/100 × EXPOSURE 0.8203 × RECENCY 0.9884 × RECURRENCE 1.2
- **Evidence level:** `L3_STATE`
- **Why the family applies:** Borrowing capacity, mint size, reward size or collateral value must not be derived from a price that a single actor can move within the manipulation window, and the value unlocked must never exceed the cost of moving that price.
    - Screening evidence: archetype applicable: category=Yield; description/methodology signals: stake, yield; misrepresentedTokens flag; sub-threshold high-fit: onchain_governance_authority; multi-chain surface (10 chains)
    - Deep-screen observations: declared oracles: none declared in DefiLlama metadata
- **Mandatory preconditions PRESENT:** single_or_undeclared_oracle
- **Mandatory preconditions UNKNOWN:** value_decision_reads_configured_feed, feed_selection_is_configuration, failure_path_returns_usable_number, live_positions_exposed
- **Decisive guards searched:** staleness_check_reverts, deviation_bound_vs_independent_source, caps_sized_to_venue_depth
- **Decisive guards found:** none found in the reviewed path
- **Live value / authority / approval relevance:** exposure basis $159,631,156; on-chain governance authority
- **Implementation and deployment status:** adapter `stakedao/index.js` (READ); 6 adapter address(es) probed; not flagged deprecated; 1 audit link(s) listed
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, audit competitions, upstream advisories, postmortems and relevant forks was performed for this pair. Novelty is therefore NOT claimed and NO_PUBLIC_MATCH_FOUND is deliberately not used. (search scope: none performed for this pair)
- **What would falsify the hypothesis:** All collateral priced by a deep aggregated feed with a deviation cap (kills the pair); Caps are set from measured venue depth and enforced on-chain; The action is sized from realised transfer amounts, so price is never an input
- **Recommended audit focus:** On a fork, execute a max-size flash-funded swap against every venue in the pricing path and assert that no value-bearing entrypoint changes its output beyond the configured deviation bound.
    - Questions: Is every mandatory precondition present in the live deployment? · Is any decisive guard present in the deployed bytecode, not just the repository? · What live value, authority or approval is reachable through this path?
- **Evidence paths:** `protocols/deep_screened.jsonl#stake-dao|ORACLE-SPOT-THIN-LIQUIDITY`, `protocols/adapters_index.json#stake-dao`, `protocols/onchain_probes.json#stake-dao`, `families/families.json#ORACLE-SPOT-THIN-LIQUIDITY`, `sources/defillama/adapters/stake-dao__stakedao__index.js`
- **Responsible disclosure channel, if public:** not listed in DefiLlama metadata · audits: https://docs.stakedao.org/audits

### 15. Yield Basis  —  `ORACLE-SPOT-THIN-LIQUIDITY`

- **Rank (Ranking B — expected loss prevention):** 15
- **Protocol:** Yield Basis (`yield-basis`)
- **DefiLlama URL:** https://defillama.com/protocol/yield-basis
- **Current TVL:** $156,332,797
- **Chains:** Ethereum
- **Category:** Leveraged Farming
- **Matched family IDs:** `ORACLE-SPOT-THIN-LIQUIDITY`
- **Ranking:**
    - MATCH_SCORE: **40.0** / 100
    - EVIDENCE_CONFIDENCE: **75.0** / 100 (mapping 100, deployment parity 55, live state 50, corroboration 90, guard review 80)
    - PREVENTION_SCORE: **29.156** = MATCH 40.0 × CONF 75.0/100 × EXPOSURE 0.8194 × RECENCY 0.9884 × RECURRENCE 1.2
- **Evidence level:** `L3_STATE`
- **Why the family applies:** Borrowing capacity, mint size, reward size or collateral value must not be derived from a price that a single actor can move within the manipulation window, and the value unlocked must never exceed the cost of moving that price.
    - Screening evidence: archetype applicable: category=Leveraged Farming; description/methodology signals: borrow, reward, yield; no audit link listed (prioritisation signal only, never evidence of a defect); no oracle declared in DefiLlama metadata (unknown pricing path); exposure tilt from TVL $156,332,797
    - Deep-screen observations: declared oracles: none declared in DefiLlama metadata
- **Mandatory preconditions PRESENT:** single_or_undeclared_oracle
- **Mandatory preconditions UNKNOWN:** value_decision_reads_configured_feed, feed_selection_is_configuration, failure_path_returns_usable_number, live_positions_exposed
- **Decisive guards searched:** staleness_check_reverts, deviation_bound_vs_independent_source, caps_sized_to_venue_depth
- **Decisive guards found:** none found in the reviewed path
- **Live value / authority / approval relevance:** exposure basis $156,332,797
- **Implementation and deployment status:** adapter `yield-basis/index.js` (READ); 1 adapter address(es) probed; not flagged deprecated; no audit link listed
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, audit competitions, upstream advisories, postmortems and relevant forks was performed for this pair. Novelty is therefore NOT claimed and NO_PUBLIC_MATCH_FOUND is deliberately not used. (search scope: none performed for this pair)
- **What would falsify the hypothesis:** All collateral priced by a deep aggregated feed with a deviation cap (kills the pair); Caps are set from measured venue depth and enforced on-chain; The action is sized from realised transfer amounts, so price is never an input
- **Recommended audit focus:** On a fork, execute a max-size flash-funded swap against every venue in the pricing path and assert that no value-bearing entrypoint changes its output beyond the configured deviation bound.
    - Questions: Is every mandatory precondition present in the live deployment? · Is any decisive guard present in the deployed bytecode, not just the repository? · What live value, authority or approval is reachable through this path?
- **Evidence paths:** `protocols/deep_screened.jsonl#yield-basis|ORACLE-SPOT-THIN-LIQUIDITY`, `protocols/adapters_index.json#yield-basis`, `protocols/onchain_probes.json#yield-basis`, `families/families.json#ORACLE-SPOT-THIN-LIQUIDITY`, `sources/defillama/adapters/yield-basis__yield-basis__index.js`
- **Responsible disclosure channel, if public:** not listed in DefiLlama metadata

### 16. Lido  —  `GOV-CHEAP-CONTROL-NO-TIMELOCK`

- **Rank (Ranking B — expected loss prevention):** 16
- **Protocol:** Lido (`lido`)
- **DefiLlama URL:** https://defillama.com/protocol/lido
- **Current TVL:** $23,256,609,669
- **Chains:** Ethereum, Solana, Terra, Moonriver, Moonbeam
- **Category:** Liquid Staking
- **Matched family IDs:** `GOV-CHEAP-CONTROL-NO-TIMELOCK` (other pairs generated for this protocol: ACC-REWARD-INDEX-INIT-AND-ORDERING)
- **Ranking:**
    - MATCH_SCORE: **42.5** / 100
    - EVIDENCE_CONFIDENCE: **62.0** / 100 (mapping 100, deployment parity 55, live state 50, corroboration 90, guard review 15)
    - PREVENTION_SCORE: **28.319** = MATCH 42.5 × CONF 62.0/100 × EXPOSURE 1.0427 × RECENCY 0.937 × RECURRENCE 1.1
- **Evidence level:** `L3_STATE`
- **Why the family applies:** The cost of acquiring decisive voting power must exceed the value governance controls, and execution must be separated from passage by a delay long enough for holders to exit or a guardian to veto.
    - Screening evidence: archetype-agnostic family (applies to any archetype); sub-threshold high-fit: onchain_governance_authority; multi-chain surface (5 chains); on-chain governance registered: snapshot:lido-snapshot.eth; exposure tilt from TVL $23,256,609,669
    - Deep-screen observations: Cost to acquire decisive voting power was NOT measured against controlled value, and timelock parameters were NOT read on-chain. Both remain UNKNOWN and therefore score zero: this pair is listed as an open question about governance economics, not as an assertion that control is cheap.
- **Mandatory preconditions PRESENT:** governance_can_move_value_mint_or_upgrade, live_value_or_approvals_reachable_by_governance
- **Mandatory preconditions UNKNOWN:** decisive_voting_power_cheaper_than_controlled_value, no_timelock_or_timelock_shorter_than_response_window
- **Decisive guards searched:** timelock_plus_guardian_veto, quorum_scaled_to_controlled_value
- **Decisive guards found:** none found in the reviewed path
- **Live value / authority / approval relevance:** exposure basis $26,745,101,120; on-chain governance authority
- **Implementation and deployment status:** adapter `lido/index.js` (READ); 1 adapter address(es) probed; not flagged deprecated; 1 audit link(s) listed
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, audit competitions, upstream advisories, postmortems and relevant forks was performed for this pair. Novelty is therefore NOT claimed and NO_PUBLIC_MATCH_FOUND is deliberately not used. (search scope: none performed for this pair)
- **What would falsify the hypothesis:** Timelock plus an active guardian with veto (kills execution speed); Cost to acquire quorum exceeds controlled value by a wide margin; Governance cannot upgrade or mint
- **Recommended audit focus:** Compute, from live market depth, the capital required to reach quorum, and compare it with treasury plus TVL plus the value reachable through approvals; the ratio is the finding.
    - Questions: Is every mandatory precondition present in the live deployment? · Is any decisive guard present in the deployed bytecode, not just the repository? · What live value, authority or approval is reachable through this path?
- **Evidence paths:** `protocols/deep_screened.jsonl#lido|GOV-CHEAP-CONTROL-NO-TIMELOCK`, `protocols/adapters_index.json#lido`, `protocols/onchain_probes.json#lido`, `families/families.json#GOV-CHEAP-CONTROL-NO-TIMELOCK`, `sources/defillama/adapters/lido__lido__index.js`
- **Responsible disclosure channel, if public:** not listed in DefiLlama metadata · audits: https://github.com/lidofinance/audits

### 17. ether.fi Liquid  —  `ORACLE-STALE-OR-SILENT-FALLBACK`

- **Rank (Ranking B — expected loss prevention):** 17
- **Protocol:** ether.fi Liquid (`ether.fi-liquid`)
- **DefiLlama URL:** https://defillama.com/protocol/ether.fi-liquid
- **Current TVL:** $388,960,571
- **Chains:** Ethereum
- **Category:** Onchain Capital Allocator
- **Matched family IDs:** `ORACLE-STALE-OR-SILENT-FALLBACK`
- **Ranking:**
    - MATCH_SCORE: **40.0** / 100
    - EVIDENCE_CONFIDENCE: **75.0** / 100 (mapping 100, deployment parity 55, live state 50, corroboration 90, guard review 80)
    - PREVENTION_SCORE: **28.163** = MATCH 40.0 × CONF 75.0/100 × EXPOSURE 0.859 × RECENCY 0.9503 × RECURRENCE 1.15
- **Evidence level:** `L3_STATE`
- **Why the family applies:** A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
    - Screening evidence: archetype applicable: category=Onchain Capital Allocator; no audit link listed (prioritisation signal only, never evidence of a defect); misrepresentedTokens flag; sub-threshold high-fit: curator_authority_over_third_party_vaults; no oracle declared in DefiLlama metadata (unknown pricing path)
    - Deep-screen observations: declared oracles: none declared in DefiLlama metadata
- **Mandatory preconditions PRESENT:** single_or_undeclared_oracle
- **Mandatory preconditions UNKNOWN:** value_decision_reads_configured_feed, feed_selection_is_configuration, failure_path_returns_usable_number, live_positions_exposed
- **Decisive guards searched:** staleness_check_reverts, deviation_bound_vs_independent_source, caps_sized_to_venue_depth
- **Decisive guards found:** none found in the reviewed path
- **Live value / authority / approval relevance:** exposure basis $388,960,571
- **Implementation and deployment status:** adapter `etherfi-liquid/index.js` (READ); 6 adapter address(es) probed; not flagged deprecated; no audit link listed
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, audit competitions, upstream advisories, postmortems and relevant forks was performed for this pair. Novelty is therefore NOT claimed and NO_PUBLIC_MATCH_FOUND is deliberately not used. (search scope: none performed for this pair)
- **What would falsify the hypothesis:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Recommended audit focus:** On a fork, force each configured feed to return zero, a stale timestamp, and a 10x/0.1x value; every value-bearing entrypoint must revert rather than transact.
    - Questions: Is every mandatory precondition present in the live deployment? · Is any decisive guard present in the deployed bytecode, not just the repository? · What live value, authority or approval is reachable through this path?
- **Evidence paths:** `protocols/deep_screened.jsonl#ether.fi-liquid|ORACLE-STALE-OR-SILENT-FALLBACK`, `protocols/adapters_index.json#ether.fi-liquid`, `protocols/onchain_probes.json#ether.fi-liquid`, `families/families.json#ORACLE-STALE-OR-SILENT-FALLBACK`, `sources/defillama/adapters/ether.fi-liquid__etherfi-liquid__index.js`
- **Responsible disclosure channel, if public:** not listed in DefiLlama metadata

### 18. Tulipa Capital  —  `ACC-NAV-SHAREPRICE-MANIPULABLE`

- **Rank (Ranking B — expected loss prevention):** 18
- **Protocol:** Tulipa Capital (`tulipa-capital`)
- **DefiLlama URL:** https://defillama.com/protocol/tulipa-capital
- **Current TVL:** $44,238,986
- **Chains:** Ethereum, Avalanche, Berachain, BOB, Monad, Binance, TAC, Base
- **Category:** Risk Curators
- **Matched family IDs:** `ACC-NAV-SHAREPRICE-MANIPULABLE`
- **Ranking:**
    - MATCH_SCORE: **54.5** / 100
    - EVIDENCE_CONFIDENCE: **69.0** / 100 (mapping 100, deployment parity 55, live state 85, corroboration 90, guard review 15)
    - PREVENTION_SCORE: **27.839** = MATCH 54.5 × CONF 69.0/100 × EXPOSURE 0.7646 × RECENCY 0.9221 × RECURRENCE 1.05
- **Evidence level:** `L3_STATE`
- **Why the family applies:** totalAssets() must equal value the vault could actually realise now. Any component valued at book, at a manipulable rate, or after economic impairment lets a redeemer convert other depositors' claims into their own.
    - Screening evidence: archetype applicable: category=Risk Curators; description/methodology signals: vault, strateg, curat; no audit link listed (prioritisation signal only, never evidence of a defect); sub-threshold high-fit: curator_authority_over_third_party_vaults; multi-chain surface (8 chains)
    - Deep-screen observations: curator controls 3 declared vaults via registries/curators.js; owner keys 0x59e608E4842162480591032f3c8b0aE55C98d104; live vault reads: 0x686c83Aa… totalAssets=53974792511106717850370; 0x6Bf340dB… totalAssets=None; 0x7895a046… totalAssets=0
- **Mandatory preconditions PRESENT:** multi_component_totalAssets, live_pooled_depositor_value
- **Mandatory preconditions UNKNOWN:** component_valuation_externally_influenceable, deposit_and_redeem_reachable
- **Decisive guards searched:** per_block_share_price_cap, component_valuation_deviation_bound
- **Decisive guards found:** none found in the reviewed path
- **Live value / authority / approval relevance:** exposure basis $44,238,986; curator authority over third-party vaults
- **Implementation and deployment status:** adapter `registries/curators.js` (READ_VIA_REGISTRY); 3 curated vault(s) read; 1 adapter address(es) probed; not flagged deprecated; no audit link listed
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, audit competitions, upstream advisories, postmortems and relevant forks was performed for this pair. Novelty is therefore NOT claimed and NO_PUBLIC_MATCH_FOUND is deliberately not used. (search scope: none performed for this pair)
- **What would falsify the hypothesis:** Share price rate-limited per block (kills same-transaction extraction); Single-asset vault with no external valuation; Withdrawals queued with a delay and priced at settlement
- **Recommended audit focus:** On a fork, for each component, force its valuation to zero and to 10x; the vault's mint/redeem must revert or be bounded, never transfer more than the depositor's pro-rata realisable share.
    - Questions: Is every mandatory precondition present in the live deployment? · Is any decisive guard present in the deployed bytecode, not just the repository? · What live value, authority or approval is reachable through this path?
- **Evidence paths:** `protocols/deep_screened.jsonl#tulipa-capital|ACC-NAV-SHAREPRICE-MANIPULABLE`, `protocols/adapters_index.json#tulipa-capital`, `protocols/onchain_probes.json#tulipa-capital`, `families/families.json#ACC-NAV-SHAREPRICE-MANIPULABLE`, `sources/defillama/adapters/tulipa-capital__registries__curators.js`
- **Responsible disclosure channel, if public:** not listed in DefiLlama metadata

### 19. Lighter Bridge  —  `PROOF-VERIFICATION-BYPASSED`

- **Rank (Ranking B — expected loss prevention):** 19
- **Protocol:** Lighter Bridge (`lighter-bridge`)
- **DefiLlama URL:** https://defillama.com/protocol/lighter-bridge
- **Current TVL:** $530,440,530
- **Chains:** Ethereum, Arbitrum
- **Category:** Bridge
- **Matched family IDs:** `PROOF-VERIFICATION-BYPASSED`
- **Ranking:**
    - MATCH_SCORE: **45** / 100
    - EVIDENCE_CONFIDENCE: **62.0** / 100 (mapping 100, deployment parity 55, live state 50, corroboration 90, guard review 15)
    - PREVENTION_SCORE: **26.743** = MATCH 45 × CONF 62.0/100 × EXPOSURE 0.8725 × RECENCY 0.9155 × RECURRENCE 1.2
- **Evidence level:** `L1_ADAPTER`
- **Why the family applies:** A withdrawal or mint gated by a proof must verify that proof against the correct verifying key, over all the public inputs that bind the action, and must reject when any component is absent.
    - Screening evidence: archetype applicable: category=Bridge; description/methodology signals: zk, rollup; no audit link listed (prioritisation signal only, never evidence of a defect); sub-threshold high-fit: bridge_authority_over_external_value; exposure tilt from TVL $530,440,530
    - Deep-screen observations: GENERIC-FAMILY SCREEN: no family-specific precondition was verified for this pair. Evidence is adapter-level architecture only, so the score is capped at the L1 adapter ceiling and this pair is preliminary by construction.; adapter `registries/sumTokens.js` read: 6880 hardcoded addresses, dynamic=True, external API=True
- **Mandatory preconditions PRESENT:** _generic_family_adapter_only, family_architecture_signals_in_adapter, live_value_present
- **Mandatory preconditions UNKNOWN:** none
- **Decisive guards searched:** decisive_guard_reviewed
- **Decisive guards found:** none found in the reviewed path
- **Live value / authority / approval relevance:** exposure basis $530,440,530
- **Implementation and deployment status:** adapter `registries/sumTokens.js` (READ_VIA_REGISTRY); 4 adapter address(es) probed; not flagged deprecated; no audit link listed
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, audit competitions, upstream advisories, postmortems and relevant forks was performed for this pair. Novelty is therefore NOT claimed and NO_PUBLIC_MATCH_FOUND is deliberately not used. (search scope: none performed for this pair)
- **What would falsify the hypothesis:** Verifying key immutable and attested (kills the misconfiguration shape); No alternative release path exists (enumerate selectors)
- **Recommended audit focus:** On a fork, submit an empty proof, a proof for different public inputs, and a proof under a foreign key; every release path must revert.
    - Questions: Is every mandatory precondition present in the live deployment? · Is any decisive guard present in the deployed bytecode, not just the repository? · What live value, authority or approval is reachable through this path?
- **Evidence paths:** `protocols/deep_screened.jsonl#lighter-bridge|PROOF-VERIFICATION-BYPASSED`, `protocols/adapters_index.json#lighter-bridge`, `protocols/onchain_probes.json#lighter-bridge`, `families/families.json#PROOF-VERIFICATION-BYPASSED`, `sources/defillama/adapters/lighter-bridge__registries__sumTokens.js`
- **Responsible disclosure channel, if public:** not listed in DefiLlama metadata

### 20. Uniswap V2  —  `ACC-MULTI-PATH-CREDIT-DRIFT`

- **Rank (Ranking B — expected loss prevention):** 20
- **Protocol:** Uniswap V2 (`uniswap-v2`)
- **DefiLlama URL:** https://defillama.com/protocol/uniswap-v2
- **Current TVL:** $912,700,838
- **Chains:** Ethereum, Base, Polygon, Robinhood Chain, Arbitrum, Binance, X Layer, Monad …
- **Category:** Dexs
- **Matched family IDs:** `ACC-MULTI-PATH-CREDIT-DRIFT` (other pairs generated for this protocol: QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET)
- **Ranking:**
    - MATCH_SCORE: **45** / 100
    - EVIDENCE_CONFIDENCE: **62.0** / 100 (mapping 100, deployment parity 55, live state 50, corroboration 90, guard review 15)
    - PREVENTION_SCORE: **26.075** = MATCH 45 × CONF 62.0/100 × EXPOSURE 0.896 × RECENCY 0.9934 × RECURRENCE 1.05
- **Evidence level:** `L1_ADAPTER`
- **Why the family applies:** Every path that can credit or debit a given balance must apply identical accounting. Where a protocol offers module sidecars, legacy plus current paths, or several entrypoints to one pool, cycling between them must be value-neutral.
    - Screening evidence: archetype applicable: category=Dexs; description/methodology signals: v2; misrepresentedTokens flag; multi-chain surface (14 chains); exposure tilt from TVL $912,700,838
    - Deep-screen observations: GENERIC-FAMILY SCREEN: no family-specific precondition was verified for this pair. Evidence is adapter-level architecture only, so the score is capped at the L1 adapter ceiling and this pair is preliminary by construction.; adapter `uniswap-v2/index.js` read: 13 hardcoded addresses, dynamic=True, external API=True
- **Mandatory preconditions PRESENT:** _generic_family_adapter_only, family_architecture_signals_in_adapter, live_value_present
- **Mandatory preconditions UNKNOWN:** none
- **Decisive guards searched:** decisive_guard_reviewed
- **Decisive guards found:** none found in the reviewed path
- **Live value / authority / approval relevance:** exposure basis $912,700,838
- **Implementation and deployment status:** adapter `uniswap-v2/index.js` (READ); 1 adapter address(es) probed; not flagged deprecated; 3 audit link(s) listed
- **Prior-art status:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, audit competitions, upstream advisories, postmortems and relevant forks was performed for this pair. Novelty is therefore NOT claimed and NO_PUBLIC_MATCH_FOUND is deliberately not used. (search scope: none performed for this pair)
- **What would falsify the hypothesis:** All mint/burn routes through a single internal function with a closing invariant assert (kills the pair); Only one live entrypoint per balance
- **Recommended audit focus:** On a fork, enumerate all entrypoints touching a given balance and fuzz orderings; assert the global share/asset invariant holds after every sequence.
    - Questions: Is every mandatory precondition present in the live deployment? · Is any decisive guard present in the deployed bytecode, not just the repository? · What live value, authority or approval is reachable through this path?
- **Evidence paths:** `protocols/deep_screened.jsonl#uniswap-v2|ACC-MULTI-PATH-CREDIT-DRIFT`, `protocols/adapters_index.json#uniswap-v2`, `protocols/onchain_probes.json#uniswap-v2`, `families/families.json#ACC-MULTI-PATH-CREDIT-DRIFT`, `sources/defillama/adapters/uniswap-v2__uniswap-v2__index.js`
- **Responsible disclosure channel, if public:** not listed in DefiLlama metadata · audits: https://github.com/Uniswap/uniswap-v3-core/tree/main/audits, https://github.com/Uniswap/uniswap-v3-periphery/tree/main/audits
