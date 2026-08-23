# Quality report

> **Verdict:** *Pattern library complete for the stated six-month window; candidate screen complete within stated filters.*
>
> This is a discovery and prioritisation pass. No protocol named anywhere in this output is asserted to be exploitable or vulnerable. Every candidate requires separate authorized verification in a local or pinned-fork environment. A completed screen is not evidence that non-selected protocols are safe.

## 1. Evidence grading rule actually applied

The source index is explicitly a lead source, not sufficient alone for a high-confidence root cause. The grading rule applied in this run, stated so it can be audited:

| Grade | Rule as applied | Count |
|---|---|---:|
| **A** | Mechanism-level index record **plus** at least one independent technical source retrieved (official postmortem, security-firm analysis) **or** deployed-code/live-state evidence gathered in this run | 58 |
| **B** | Mechanism-level index record naming a specific contract, function, parameter or state variable — a strong technical source in itself — with no contradicting source found, but no second independent source retrieved | 52 |
| **C** | On-chain root cause plausible but a material link unverified, or a mixed on/off-chain attribution that could not be resolved. Written to `provisional.jsonl`; excluded from all statistics and ranking weight. | 22 |
| **D** | Mechanism vague, contradictory or unsupported. Excluded from pattern derivation and recorded in `excluded.jsonl` under `PATTERN_EXC_GRADE_D`, with the gate result preserved. | see excluded.jsonl |

Corroboration status across the 110 included incidents: `SLOWMIST_MECHANISM_RECORD_ONLY` = 78, `REFERENCE_RETRIEVED` = 17, `INDEPENDENT_TECHNICAL_SOURCE_RETRIEVED` = 15.

**This is the single most important limitation of the run.** 78 of 110 included incidents rest on one mechanism-level source. Independent corroboration was performed for the incidents that anchor the highest-weight families (Lazy Summer, Venus, Ekubo, Secret Network, Blend/YieldBlox, Curve LlamaLend, Rhea, Singularity, Verus, and the BSC pair-burn template), and those upgrades are recorded per incident in the `corroboration` field. A grade-B record is a well-specified mechanism, not a verified one.

## 2. Mechanical quality gates (§18)

The gate results are produced by `tools/check_manifest.py` and written to `results/manifest_check.txt`. That script is the authority; the narrative below explains the judgement calls behind three of the gates.

### Clone handling (§18.1)

Three lineages collapse to a single root cause: the two Verus bridge exploits (same unpatched `checkCCEValues` value-equality gap, May and July), Flooring/Asterix (one shared DN404/BT404 codebase, one day apart), and the Computility pair (TGAI/YSDAO, one operator template). The 14-deployment BSC deferred-burn cluster is treated as **template propagation**, not forking: those are independent deployments that reimplement the same pattern, so they count as independent root causes, but the family's recurrence multiplier is capped so they cannot masquerade as fourteen independent discoveries.

### Generic-label prohibition (§18.2)

No family is named for an attack technique. Flash loans appear only as `optional_amplifiers`. The source database's `Attack method` string is preserved on every incident record under the field name `slowmist_attack_method_label_NOT_USED_FOR_CLUSTERING` so a reviewer can confirm it never drove clustering. Where the source labelled an incident *Flash Loan Attack*, the derived family is about what the flash loan reached — for example FoxMarket sits in `ORACLE-SPOT-THIN-LIQUIDITY` because the defect was a spot quote captured before a state-changing swap, not the borrowing of capital.

### Novelty (§14, §18.4)

`NO_PUBLIC_MATCH_FOUND` is **never emitted anywhere in this run**. A per-deployment sweep of published audits, audit competitions, upstream advisories and postmortems was performed only for the pairs recorded in `protocols/prior_art.json`; every other pair carries `PRIOR_ART_SEARCH_INCOMPLETE`, which is an addition to the required enum because that enum has no value meaning *not yet searched*, and using any of its existing values would overstate what was checked.

## 3. What the screen found, and what that cost

Two results are worth stating plainly because they show the gate doing its job in both directions:

- **Venus Core Pool was killed by its own fix.** Venus was the largest donation-attack victim in the window (March 2026, THE market). Following its beacon proxy to the deployed `VToken` implementation shows an internal cash counter, so the exchange rate is no longer a function of the raw token balance. The mandatory precondition is proven absent and the pair is dead, despite $1.25B of live TVL and a perfect archetype match. A screen that ranked on similarity alone would have put it near the top.

- **Steakhouse Financial was downgraded by documented guards.** It was the highest-exposure curator in the worklist (~$2.98B). Published risk documentation shows owner multisig, 7-day action timelocks and an Aragon guardian veto. That closes the malicious-component-addition path, so the pair became a near miss rather than a candidate. The residual question recorded in the near-miss library is narrower and more useful: a multi-day timelock does not address the Lazy Summer shape, where the loss came from a component that was already approved and still counted in `totalAssets()` during an incomplete offboarding.

## 4. The expansion pass

A second pass widened the screen on operator instruction: a **hard $50,000 TVL floor** (replacing the $1M threshold plus a sub-threshold queue), plus two new evidence layers.

**Condition layer** (`tools/conditions.py`, 24 observable conditions). Rather than screening only by DefiLlama category, a condition can now *create* a protocol-family pair on its own, because the condition is itself the applicability evidence. The highest-yield ones: forked from a protocol exploited inside the window; listed in DefiLlama's own `deadAdapters.json` while still reporting value; a version sibling of a newer deployment; a declared Fallback or Secondary oracle; an RWA pricing surface; vaults co-curated with another curator; and architecture tags (hook-based AMM, CLMM, StableSwap, ve(3,3), order book) that map to specific families.

**Deployed-source sweep** (`tools/source_sweep.py`). Verified source is fetched for the contracts actually found on-chain, following delegator and beacon proxies to their implementations, and each family's documented `static_indicators` are evaluated against it. Source is cached under `sources/deployments/`, so re-analysis after an indicator change costs nothing. This is what converted 11 families from *no addressable population* into screenable pairs, and it is why 40 of 40 final candidates reach `L4_GUARD_REVIEW` rather than stopping at adapter evidence.

### Precision controls, and why they were necessary

A static-indicator sweep at this scale manufactures false candidates unless it is disciplined. Four controls were added after inspecting what the first version actually produced:

1. **Relevance gate.** A guard can only read as *absent* if the contract that was read shows at least one distinguishing indicator for that family. The first version reported *no staleness check* for Aave V3 after reading `AaveProtocolDataProvider`, and for Sky after reading `LockstakeEngine` — neither is the pricing contract. Not finding an oracle guard in a contract that is not the oracle says nothing, so every source-derived signal for such a pair is now UNKNOWN.

2. **Prevalence demotion.** Any indicator firing on more than 25% of the swept population is describing a common architecture, not a distinguishing prerequisite, and is demoted to ordering-only. This removed Lido, Uniswap V3, PancakeSwap and usdt0 from the top of the loss-prevention ranking, where they had been placed by a generic *takes an address and bytes and calls it* pattern that half of all routers match. The measured prevalence is published on every affected pair.

3. **Metadata cannot prove code.** DefiLlama's oracle list is a disclosure, not a code fact. It no longer establishes a precondition or proves a deviation bound absent; it is recorded as a note.

4. **Approval-dependent families keep an UNKNOWN exposure precondition,** because live allowances and credit delegations were not enumerated. Those families cannot reach a full score from code shape alone.

Two narrower regex fixes came from the same inspection: Aave's zero-argument `getPool()` is not Uniswap's `getPool(token0, token1, fee)`, and CCIP's `releaseOrMint` is bridge plumbing rather than a user claim path. Both had produced top-ranked entries that were purely naming collisions.

## 5. Known limitations

1. **Corpus completeness.** The index is a lead source, not a census. At least one in-window on-chain incident documented elsewhere (STO token, 2026-02-23, pair-burn reserve manipulation) does not appear in it. Frequency and loss statistics are therefore lower bounds.

2. **One unresolved source contradiction.** `INC-2026-04-01-DRI` (Drift Protocol, ~$285M — by loss the largest event in the window) carries an attack-method label of *Social Engineering* against a description of a vault exploit with no mechanism. It is graded D and excluded from pattern derivation. If its true root cause is on-chain, the corpus is missing its single largest data point.

3. **Reference retrieval.** 104 of 130 reference URLs for gate-passing incidents are client-rendered social posts whose bodies are not machine-retrievable. They are recorded as `LEAD_ONLY_CLIENT_RENDERED` and were never counted as corroboration.

4. **Loss figures are as-reported.** No independent net-loss reconstruction was performed. Several incidents involve partial returns, whitehat recovery or frozen funds; `net_loss_basis` preserves the raw string, and recoveries are visible in the narrative but are not netted out of the totals.

5. **Sixteen families have no addressable population here.** The highest-frequency family in the corpus (`TOKEN-DEFERRED-BURN-LP-RESERVE-DESYNC`, 15 incidents) targets individually deployed tokens that are not DefiLlama protocol entries. Those families are listed in `protocols/families_not_screenable_in_universe.json` and belong to a token-level monitoring workstream. A reader who assumed the candidate list covers the whole family library would be wrong.

6. **Deep screening is not an audit.** 243 pairs were gated, but only 5 reached `L4_GUARD_REVIEW` — the level at which a decisive guard was actually read out of deployed implementation code. The rest rest on adapter architecture and live-state reads.

7. **Exposure is understated for approval-bearing families.** Live ERC-20/721 allowances and credit delegations to router, executor and module contracts were not enumerated on-chain. For `CALLDATA-CALLER-CONTROLLED-TARGET`, `CALLBACK-UNAUTHENTICATED-CALLER-USES-APPROVALS` and `APPROVALS-TO-UPGRADEABLE-SPENDER`, TVL is the wrong exposure basis and the recorded figure is a floor. This is flagged per-candidate in `authority_notes`.

8. **DefiLlama's `deprecated` flag is ambiguous.** It is also used when an adapter is superseded or its TVL is counted elsewhere. Base's canonical bridge carries it at $2.79B. The flag alone is therefore scored as UNKNOWN and a caution note is attached to every affected candidate.

9. **Governance economics were not measured.** For `GOV-CHEAP-CONTROL-NO-TIMELOCK`, the cost of acquiring decisive voting power was not compared against controlled value and timelock parameters were not read on-chain. Both preconditions stay UNKNOWN and score zero, so those pairs are open questions, not claims.

11. **Static indicators are heuristics, not analysis.** The deployed-source sweep is regular expressions over verified source. It cannot follow control flow, resolve inheritance, or tell a guard in a library from a guard on the path that matters. A matched indicator means *this shape is present in this file*, which is a reason to look, never a finding. Three Centrifuge-family entries flagged for the same `ecrecover` shape are very likely one shared codebase rather than three independent results, and are recorded that way in `prior_art.json`.

12. **Only the contracts an adapter or registry names were read.** Where an adapter is dynamic or has no hardcoded addresses, no contract was reached at all, and those pairs stay at adapter evidence. 251 worklist protocols yielded no on-chain address to probe.

13. **The $50,000 floor is the operator's, not the methodology's.** 662 authority-bearing protocols below it were identified and recorded in `protocols/subfloor_authority_deferred.json` but never screened. Several carry conditions that would otherwise have ranked them, including in-window victims still holding value. TVL remains a poor proxy for value at risk.

10. **Scores are not probabilities.** `MATCH_SCORE` measures how much of a family's observable prerequisite signature was confirmed. `PREVENTION_SCORE` is a prioritisation heuristic. Neither is an exploit likelihood, and neither should be reported as one.

