# Quality report

> **Verdict:** *Pattern library complete for the stated six-month window; candidate screen complete within stated filters.*
>
> Discovery stage. No protocol named in this output is asserted to be defective. Every candidate needs separate authorized verification on a local or pinned fork. A completed screen is not evidence that non-selected protocols are safe.

## 1. What changed, and why

This pass is aimed at an independent reviewer trying to prevent real losses, which makes two earlier choices wrong:

- **Exposure-weighted ranking was backwards.** The previous ranking multiplied by a log of TVL, so it surfaced Aave, Lido, Morpho Blue and Uniswap. Those teams carry dedicated audit retainers. The corpus built in this very run says exposure is also a poor predictor of *being hit*: median in-window loss **$252,000**, 84% under **$2,000,000**, only 5% above $10,000,000.

- **The high-exposure segments were the wrong segments.** Measuring hazard as *incident share divided by eligible-protocol share* shows Risk Curators at ×0.50 and RWA at ×0.46 — under-represented among actual victims — while Farm sits at ×13.7, Algo-Stables ×13.2, Privacy ×12.1, Staking Pool ×5.0 and Bridge ×3.6. By chain, BSC is ×3.6 and Ethereum ×2.5, while Polygon (×0.56) and Avalanche (×0.37) are *under*-represented. The previous run's emphasis on large curators was therefore aimed away from where attacks actually land.

So the ranking is now **HACK_LIKELIHOOD** = family evidence (0-40, weighted by how deeply it was actually read) + empirical segment hazard (0-25) + attention deficit (0-25) + attacker economics (0-10). Value at risk is printed beside every candidate and never folded into the score.

## 2. The band

| Band | Protocols | Treatment |
|---|---:|---|
| Below $50,000 | 662 authority-bearing | recorded, never screened |
| $50,000 - $30,000,000 | 2268 | full consideration |
| Above $30,000,000 | 363 dropped, 31 kept | dropped unless specific danger evidence |

Above-band retention requires named evidence, not category fit: an in-window victim still live, a fork of one, presence in DefiLlama's own dead-adapter registry, a prior-incident hallmark, an unverified implementation behind a live proxy, or an existing L4 pair scoring 70+. Every retained protocol carries its reasons in `danger_reasons`. All 351 dropped protocols are listed with their TVL in `protocols/above_band_dropped.json`, so the exclusion is auditable rather than silent.

## 3. Evidence grading actually applied

| Grade | Rule | Count |
|---|---|---:|
| **A** | Mechanism-level index record plus an independent technical source retrieved, or deployed-code evidence gathered here | 59 |
| **B** | Mechanism-level record naming a specific contract, function or parameter, no contradiction found, no second source retrieved | 51 |
| **C** | Plausible but a material link unverified, or unresolved mixed attribution. Provisional; excluded from all statistics and ranking weight | 22 |
| **D** | Vague, contradictory or unsupported. Excluded from pattern derivation | see excluded.jsonl |

Corroboration across included incidents: `SLOWMIST_MECHANISM_RECORD_ONLY` = 77, `REFERENCE_RETRIEVED` = 17, `INDEPENDENT_TECHNICAL_SOURCE_RETRIEVED` = 15, `DEPLOYED_SOURCE_VERIFIED` = 1.

## 4. Precision controls

A static sweep at this scale manufactures false candidates unless disciplined. Each control below was added after inspecting output that was actually wrong:

1. **Relevance gate** — a guard reads as *absent* only if the contract read shows a distinguishing indicator for that family. An earlier version reported *no staleness check* for Aave V3 after reading `AaveProtocolDataProvider`, and for Sky after reading `LockstakeEngine`; neither is the pricing contract.

2. **Prevalence demotion** — an indicator firing on more than 25% of the swept population describes a common architecture, not a prerequisite, and drops to ordering-only. This removed Lido, Uniswap V3 and PancakeSwap from the top of the ranking, where a generic *takes an address and bytes and calls it* pattern had placed them. Measured prevalence is published per pair.

3. **Metadata cannot prove code** — DefiLlama's oracle list is a disclosure, not a code fact.

4. **Coverage-weighted preconditions** — measured against the family's full declared signature, so an unevaluated precondition scores zero exactly like an unconfirmed one.

Narrower fixes from the same inspection: Aave's zero-argument `getPool()` is not Uniswap's `getPool(token0, token1, fee)`; CCIP's `releaseOrMint` is bridge plumbing, not a user claim path; and `_msgSender()` alone is in every OpenZeppelin contract, so ERC-2771 detection now requires an actual forwarder.

## 5. The scoring model is now validated rather than asserted

Every earlier version of this run assigned weights by judgement. This one measures them, and then checks whether the measurement generalises.

- **Weights are `ln(lift)`**, where lift is P(signal | victim) / P(signal | population), fitted on 20 signals that clear >=40 population support, >=4 train victims and a lift outside the uninformative 0.70-1.35 band.

- **Fitted on 2022-2024 incidents, tested on 2025-2026 incidents.** On 95 protocols never seen while fitting, the median future victim lands at the **78.6th percentile** and **58%** fall in the model's top quartile — a **x2.32 lift** over chance.

- **Feature groups are ablated, not assumed.** Each variant below is refitted from scratch and revalidated on the same held-out incidents:

| Variant | Out-of-sample lift | Verdict |
|---|---:|---|
| baseline (v3 feature set) | x2.19 | reference |
| + exposure age | x2.32 | **kept** — the only addition that paid |
| + admin posture | x2.15 | **dropped** — made prediction worse |
| + public-repo flag | x2.19 | no effect; filtered out on its own lift |
| + all v4 additions | x2.32 | shipped set |

### Three measurements that changed the model's mind

1. **The population was censored by the outcome being predicted.** Of 161 linked victims, 72 fell below the $50,000 floor after being hit and left the survivor population entirely. They were not a random sample of victims: 62.5% of them had no listed audit, against 20.9% of victims still in band. Measuring lift against survivors only therefore deletes the unaudited victims first and makes neglect look protective. Refitting against the full listed universe moved `no_audit_listed` from x0.41 to x0.582 and flipped `dead_adapter_registry` outright, x0.74 to x1.691. Note that `no_audit_listed` is still below 1 after the correction — the correction reduced the bias but did not reverse the sign, and item 3 below explains why.

2. **Prior-hack signals were predicting their own incidents.** An early backtest showed x2.87 lift; with the leakage removed — a protocol's own prior incidents withheld when scoring it — the honest figure was x1.31. Everything reported here runs with that control on.

3. **Age runs opposite to the abandonment intuition.** Protocols under a year old carry lift **x1.866**; over three years old, **x0.327**. New code with new money is what gets hit. This is why signals that read as 'neglect' — a dead front end (x0.673), no listed audit (x0.582) — measure as protective: they are largely markers of age. The band floor and the value-at-risk column are doing the work of separating *neglected and still worth saving* from *simply over*.

## 5b. What was measured and then deliberately left out of the score

Authority chains were walked for 365 in-band protocols: ERC-1967 admin slot and `owner()`, up to three hops, terminal authority fingerprinted by the functions it answers (`getThreshold()`+`getOwners()` for a Safe, `getMinDelay()` or `delay()`+`GRACE_PERIOD()` for a timelock, `votingDelay()` for a governor, zero code size for an externally-owned account).

**23 protocols holding $56,405,869 have an upgrade authority that terminates in a single key or single signature.** It is a real and cheaply fixable exposure, and it is reported in `results/upgrade_authority_exposure.md`.

It is **not** in the likelihood score, and the reason is a measurement rather than a preference. Over the full window `admin_terminal_eoa` measures x0.982 and `admin_single_signature` x0.959 — no association with code-defect incidents at all — and the ablation shows adding the group *degrades* out-of-sample prediction (x2.19 -> x2.15). This is the answer the inclusion gate predicts: an off-chain key compromise is an excluded root cause here, so custody exposure should not move a code-defect likelihood. Mixing them would have made both numbers worse.

Market cap and TVL trajectory were refused for a different reason: both are read today, and for a victim they partly measure the hack's own aftermath. `mcap_below_tvl` looks informative at x2.258 and is almost certainly measuring post-incident token collapse. They are carried as ordering-only operational flags and never fitted.

## 6. New evidence in this pass

- **Owner-is-EOA probe.** For every privileged `owner()` found, a second hop reads whether that address has code. 143 protocols have a privileged owner that is an externally owned account; 144 have one that is a contract (multisig or timelock). That is a direct, cheap read of who can move value, and it is one of the strongest attention-deficit signals in the model.

- **Empirical hazard tables** in `tools/hazard.py`, derived from this run's own corpus rather than assumed.

## 7. Known limitations

1. **Static indicators are regexes, not analysis.** A match means *this shape is present in this file* — a reason to look, never a finding. They cannot follow control flow or resolve inheritance.

2. **11349 of 14367 surviving pairs are still at metadata or adapter evidence**, because their adapters are dynamic or hold no addresses. Only the 45 finals reach L3 or L4.

2b. **Several learned weights are proxies for size and integration, not causes.** `has_2plus_audits` (x1.975) and `has_governance` (x2.968) are positive because protocols large enough to commission audits and run governance are large enough to be worth attacking. `owner_is_eoa` and `owner_is_contract` are *both* positive because what they really encode is that a live owner was readable at all. They order a queue usefully; none of them is a mechanism, and none should be quoted as a cause.

3. **Most included incidents rest on one mechanism-level source.** Independent corroboration was retrieved for the family anchors only.

4. **Hazard ratios come from 128 incidents.** Segments with few incidents (Supra ×6.4 on one incident, NEAR ×4.1 on two) carry wide error bars and should not be read as precise.

5. **`INC-2026-04-01-DRI` (Drift, ~$285M)** carries an unresolved source contradiction and is excluded from pattern derivation. If its true root cause is on-chain, the corpus is missing its largest point.

6. **The index is a lead source, not a census.** At least one in-window on-chain incident documented elsewhere (STO, 2026-02-23) is absent, so frequency and loss figures are lower bounds.

7. **Exposure is understated for approval-bearing families.** Live allowances and delegations were not enumerated, so TVL is a floor for those pairs, not a ceiling.

8. **Prior art is not established for most finals.** 50 of 60 carry `PRIOR_ART_SEARCH_INCOMPLETE`. Several of these protocols may already have a public disclosure or a deployed fix. Check before spending time.

9. **Small protocols can be small for a reason.** Some candidates are abandoned rather than merely neglected. A dead protocol with $80,000 left is a low-value save even when the finding is real; the value-at-risk column is there so you can make that call before starting.

10. **Scores are not probabilities.** `LIKELIHOOD` orders a queue. The validated x2.32 lift says future victims concentrate near the top of that queue; it does not say any particular protocol will be hit, and nothing here should be reported as a forecast.

11. **The out-of-sample test still shares a population with the fit.** Protocols are the same universe in both windows; only the incidents are held out. Protocols delisted entirely are absent from both sets, and current DefiLlama fields reflect post-incident edits. The x2.32 is a fair estimate of ranking skill, not a clean prospective trial.

12. **Custody fingerprinting is incomplete.** 120 authorities did not match any known shape and read as `UNKNOWN_CONTRACT`, which means *not identified*, not *safe*. Role-based access (`AccessControl`) is not enumerated at all, so a protocol reading `NONE_FOUND` may still grant privileged roles to single keys.

