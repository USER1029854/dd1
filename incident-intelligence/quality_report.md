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
| Above $30,000,000 | 351 dropped, 43 kept | dropped unless specific danger evidence |

Above-band retention requires named evidence, not category fit: an in-window victim still live, a fork of one, presence in DefiLlama's own dead-adapter registry, a prior-incident hallmark, an unverified implementation behind a live proxy, or an existing L4 pair scoring 70+. Every retained protocol carries its reasons in `danger_reasons`. All 351 dropped protocols are listed with their TVL in `protocols/above_band_dropped.json`, so the exclusion is auditable rather than silent.

## 3. Evidence grading actually applied

| Grade | Rule | Count |
|---|---|---:|
| **A** | Mechanism-level index record plus an independent technical source retrieved, or deployed-code evidence gathered here | 58 |
| **B** | Mechanism-level record naming a specific contract, function or parameter, no contradiction found, no second source retrieved | 52 |
| **C** | Plausible but a material link unverified, or unresolved mixed attribution. Provisional; excluded from all statistics and ranking weight | 22 |
| **D** | Vague, contradictory or unsupported. Excluded from pattern derivation | see excluded.jsonl |

Corroboration across included incidents: `SLOWMIST_MECHANISM_RECORD_ONLY` = 78, `REFERENCE_RETRIEVED` = 17, `INDEPENDENT_TECHNICAL_SOURCE_RETRIEVED` = 15.

## 4. Precision controls

A static sweep at this scale manufactures false candidates unless disciplined. Each control below was added after inspecting output that was actually wrong:

1. **Relevance gate** — a guard reads as *absent* only if the contract read shows a distinguishing indicator for that family. An earlier version reported *no staleness check* for Aave V3 after reading `AaveProtocolDataProvider`, and for Sky after reading `LockstakeEngine`; neither is the pricing contract.

2. **Prevalence demotion** — an indicator firing on more than 25% of the swept population describes a common architecture, not a prerequisite, and drops to ordering-only. This removed Lido, Uniswap V3 and PancakeSwap from the top of the ranking, where a generic *takes an address and bytes and calls it* pattern had placed them. Measured prevalence is published per pair.

3. **Metadata cannot prove code** — DefiLlama's oracle list is a disclosure, not a code fact.

4. **Coverage-weighted preconditions** — measured against the family's full declared signature, so an unevaluated precondition scores zero exactly like an unconfirmed one.

Narrower fixes from the same inspection: Aave's zero-argument `getPool()` is not Uniswap's `getPool(token0, token1, fee)`; CCIP's `releaseOrMint` is bridge plumbing, not a user claim path; and `_msgSender()` alone is in every OpenZeppelin contract, so ERC-2771 detection now requires an actual forwarder.

## 5. New evidence in this pass

- **Owner-is-EOA probe.** For every privileged `owner()` found, a second hop reads whether that address has code. 96 protocols have a privileged owner that is an externally owned account; 81 have one that is a contract (multisig or timelock). That is a direct, cheap read of who can move value, and it is one of the strongest attention-deficit signals in the model.

- **Empirical hazard tables** in `tools/hazard.py`, derived from this run's own corpus rather than assumed.

## 6. Known limitations

1. **Static indicators are regexes, not analysis.** A match means *this shape is present in this file* — a reason to look, never a finding. They cannot follow control flow or resolve inheritance.

2. **7732 of 9067 surviving pairs are still at metadata or adapter evidence**, because their adapters are dynamic or hold no addresses. Only the 45 finals reach L3 or L4.

3. **Most included incidents rest on one mechanism-level source.** Independent corroboration was retrieved for the family anchors only.

4. **Hazard ratios come from 128 incidents.** Segments with few incidents (Supra ×6.4 on one incident, NEAR ×4.1 on two) carry wide error bars and should not be read as precise.

5. **`INC-2026-04-01-DRI` (Drift, ~$285M)** carries an unresolved source contradiction and is excluded from pattern derivation. If its true root cause is on-chain, the corpus is missing its largest point.

6. **The index is a lead source, not a census.** At least one in-window on-chain incident documented elsewhere (STO, 2026-02-23) is absent, so frequency and loss figures are lower bounds.

7. **Exposure is understated for approval-bearing families.** Live allowances and delegations were not enumerated, so TVL is a floor for those pairs, not a ceiling.

8. **Prior art is not established for most finals.** 44 of 45 carry `PRIOR_ART_SEARCH_INCOMPLETE`. Several of these protocols may already have a public disclosure or a deployed fix. Check before spending time.

9. **Small protocols can be small for a reason.** Some candidates are abandoned rather than merely neglected. A dead protocol with $80,000 left is a low-value save even when the finding is real; the value-at-risk column is there so you can make that call before starting.

10. **Scores are not probabilities.** `HACK_LIKELIHOOD` orders a queue. It is not a forecast, and nothing in it should be reported as one.

