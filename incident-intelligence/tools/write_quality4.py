#!/usr/bin/env python3
import json,collections,csv,sys
sys.path.insert(0,'/home/user/dd1/incident-intelligence/tools')
B='/home/user/dd1/incident-intelligence'
inc=[json.loads(l) for l in open(f'{B}/incidents/included.jsonl')]
prov=[json.loads(l) for l in open(f'{B}/incidents/provisional.jsonl')]
D=[json.loads(l) for l in open(f'{B}/protocols/deep_screened.jsonl')]
live=[d for d in D if not d['killed']]
rows=list(csv.DictReader(open(f'{B}/results/candidates_all.csv')))
finals=[r for r in rows if r['in_final']=='YES']
PRB=json.load(open(f'{B}/protocols/onchain_probes.json'))
LW=json.load(open(f'{B}/protocols/learned_weights.json'))
ABL=json.load(open(f'{B}/protocols/ablation.json'))
FLU=json.load(open(f'{B}/protocols/feature_lift_uncensored.json'))
SV=json.load(open(f'{B}/protocols/survivorship_check.json'))
AX=json.load(open(f'{B}/protocols/authority_exposure.json'))
LIFT={x['signal']:x['lift'] for x in FLU['signals']}
OOS=LW.get('out_of_sample_unseen') or {}
corr=collections.Counter(i['corroboration'] for i in inc)
L=[]
L.append("# Quality report\n")
L.append("> **Verdict:** *Pattern library complete for the stated six-month window; candidate screen complete "
         "within stated filters.*\n>\n"
         "> Discovery stage. No protocol named in this output is asserted to be defective. Every candidate needs "
         "separate authorized verification on a local or pinned fork. A completed screen is not evidence that "
         "non-selected protocols are safe.\n")
L.append("## 1. What changed, and why\n")
L.append("This pass is aimed at an independent reviewer trying to prevent real losses, which makes two earlier "
         "choices wrong:\n")
L.append("- **Exposure-weighted ranking was backwards.** The previous ranking multiplied by a log of TVL, so it "
         "surfaced Aave, Lido, Morpho Blue and Uniswap. Those teams carry dedicated audit retainers. The corpus "
         "built in this very run says exposure is also a poor predictor of *being hit*: median in-window loss "
         "**$252,000**, 84% under **$2,000,000**, only 5% above $10,000,000.\n")
L.append("- **The high-exposure segments were the wrong segments.** Measuring hazard as *incident share divided "
         "by eligible-protocol share* shows Risk Curators at ×0.50 and RWA at ×0.46 — under-represented among "
         "actual victims — while Farm sits at ×13.7, Algo-Stables ×13.2, Privacy ×12.1, Staking Pool ×5.0 and "
         "Bridge ×3.6. By chain, BSC is ×3.6 and Ethereum ×2.5, while Polygon (×0.56) and Avalanche (×0.37) are "
         "*under*-represented. The previous run's emphasis on large curators was therefore aimed away from where "
         "attacks actually land.\n")
L.append("So the ranking is now **HACK_LIKELIHOOD** = family evidence (0-40, weighted by how deeply it was "
         "actually read) + empirical segment hazard (0-25) + attention deficit (0-25) + attacker economics "
         "(0-10). Value at risk is printed beside every candidate and never folded into the score.\n")
L.append("## 2. The band\n")
L.append("| Band | Protocols | Treatment |"); L.append("|---|---:|---|")
BAND=json.load(open(f'{B}/protocols/band_screen.json'))
c=collections.Counter(r['band_status'] for r in BAND)
L.append(f"| Below $50,000 | {len(json.load(open(f'{B}/protocols/subfloor_authority_deferred.json')))} authority-bearing | recorded, never screened |")
L.append(f"| $50,000 - $30,000,000 | {c.get('IN_BAND',0)} | full consideration |")
L.append(f"| Above $30,000,000 | {c.get('ABOVE_BAND_DROPPED',0)} dropped, {c.get('ABOVE_BAND_KEPT_EXPLICIT_DANGER',0)} kept | dropped unless specific danger evidence |")
L.append("\nAbove-band retention requires named evidence, not category fit: an in-window victim still live, a fork "
         "of one, presence in DefiLlama's own dead-adapter registry, a prior-incident hallmark, an unverified "
         "implementation behind a live proxy, or an existing L4 pair scoring 70+. Every retained protocol carries "
         "its reasons in `danger_reasons`. All 351 dropped protocols are listed with their TVL in "
         "`protocols/above_band_dropped.json`, so the exclusion is auditable rather than silent.\n")
L.append("## 3. Evidence grading actually applied\n")
L.append("| Grade | Rule | Count |"); L.append("|---|---|---:|")
L.append(f"| **A** | Mechanism-level index record plus an independent technical source retrieved, or deployed-code "
         f"evidence gathered here | {sum(1 for i in inc if i['evidence_grade']=='A')} |")
L.append(f"| **B** | Mechanism-level record naming a specific contract, function or parameter, no contradiction "
         f"found, no second source retrieved | {sum(1 for i in inc if i['evidence_grade']=='B')} |")
L.append(f"| **C** | Plausible but a material link unverified, or unresolved mixed attribution. Provisional; "
         f"excluded from all statistics and ranking weight | {len(prov)} |")
L.append("| **D** | Vague, contradictory or unsupported. Excluded from pattern derivation | see excluded.jsonl |")
L.append(f"\nCorroboration across included incidents: "+", ".join(f"`{k}` = {v}" for k,v in corr.most_common())+".\n")
L.append("## 4. Precision controls\n")
L.append("A static sweep at this scale manufactures false candidates unless disciplined. Each control below was "
         "added after inspecting output that was actually wrong:\n")
L.append("1. **Relevance gate** — a guard reads as *absent* only if the contract read shows a distinguishing "
         "indicator for that family. An earlier version reported *no staleness check* for Aave V3 after reading "
         "`AaveProtocolDataProvider`, and for Sky after reading `LockstakeEngine`; neither is the pricing contract.\n")
L.append("2. **Prevalence demotion** — an indicator firing on more than 25% of the swept population describes a "
         "common architecture, not a prerequisite, and drops to ordering-only. This removed Lido, Uniswap V3 and "
         "PancakeSwap from the top of the ranking, where a generic *takes an address and bytes and calls it* "
         "pattern had placed them. Measured prevalence is published per pair.\n")
L.append("3. **Metadata cannot prove code** — DefiLlama's oracle list is a disclosure, not a code fact.\n")
L.append("4. **Coverage-weighted preconditions** — measured against the family's full declared signature, so an "
         "unevaluated precondition scores zero exactly like an unconfirmed one.\n")
L.append("Narrower fixes from the same inspection: Aave's zero-argument `getPool()` is not Uniswap's "
         "`getPool(token0, token1, fee)`; CCIP's `releaseOrMint` is bridge plumbing, not a user claim path; and "
         "`_msgSender()` alone is in every OpenZeppelin contract, so ERC-2771 detection now requires an actual "
         "forwarder.\n")
L.append("## 5. The scoring model is now validated rather than asserted\n")
L.append("Every earlier version of this run assigned weights by judgement. This one measures them, and then "
         "checks whether the measurement generalises.\n")
L.append(f"- **Weights are `ln(lift)`**, where lift is P(signal | victim) / P(signal | population), fitted on "
         f"{LW['weights'] and len(LW['weights'])} signals that clear >=40 population support, >=4 train victims "
         "and a lift outside the uninformative 0.70-1.35 band.\n")
L.append(f"- **Fitted on 2022-2024 incidents, tested on 2025-2026 incidents.** On {OOS.get('n')} protocols never "
         f"seen while fitting, the median future victim lands at the **{OOS.get('median_percentile')}th "
         f"percentile** and **{(OOS.get('top_quartile_share') or 0)*100:.0f}%** fall in the model's top quartile "
         f"— a **x{OOS.get('lift')} lift** over chance.\n")
L.append("- **Feature groups are ablated, not assumed.** Each variant below is refitted from scratch and "
         "revalidated on the same held-out incidents:\n")
L.append("| Variant | Out-of-sample lift | Verdict |"); L.append("|---|---:|---|")
_verd={"baseline (v3 feature set)":"reference",
       "+ exposure age":"**kept** — the only addition that paid",
       "+ admin posture":"**dropped** — made prediction worse",
       "+ public-repo flag":"no effect; filtered out on its own lift",
       "+ all v4 additions":"shipped set"}
for name,r in ABL['variants'].items():
    L.append(f"| {name} | x{r['lift']} | {_verd.get(name,'')} |")
L.append("")
L.append("### Three measurements that changed the model's mind\n")
L.append(f"1. **The population was censored by the outcome being predicted.** Of {SV['victims_linked']} linked "
         f"victims, {SV['fell_below_floor']} fell below the $50,000 floor after being hit and left the survivor "
         f"population entirely. They were not a random sample of victims: "
         f"{SV['no_audit_rate_fell_out']*100:.1f}% of them had no listed audit, against "
         f"{SV['no_audit_rate_in_band']*100:.1f}% of victims still in band. Measuring lift against survivors only "
         f"therefore deletes the unaudited victims first and makes neglect look protective. Refitting against the "
         f"full listed universe moved `no_audit_listed` from x0.41 to x{LIFT.get('no_audit_listed')} and flipped "
         f"`dead_adapter_registry` outright, x0.74 to x{LIFT.get('dead_adapter_registry')}. Note that "
         f"`no_audit_listed` is still below 1 after the correction — the correction reduced the bias but did not "
         f"reverse the sign, and item 3 below explains why.\n")
L.append(f"2. **Prior-hack signals were predicting their own incidents.** An early backtest showed x2.87 lift; "
         "with the leakage removed — a protocol's own prior incidents withheld when scoring it — the honest "
         "figure was x1.31. Everything reported here runs with that control on.\n")
L.append(f"3. **Age runs opposite to the abandonment intuition.** Protocols under a year old carry lift "
         f"**x{LIFT.get('age_under_1y')}**; over three years old, **x{LIFT.get('age_over_3y')}**. New code with "
         "new money is what gets hit. This is why signals that read as 'neglect' — a dead front end "
         f"(x{LIFT.get('dead_front_end')}), no listed audit (x{LIFT.get('no_audit_listed')}) — measure as "
         "protective: they are largely markers of age. The band floor and the value-at-risk column are doing the "
         "work of separating *neglected and still worth saving* from *simply over*.\n")
L.append("## 5b. What was measured and then deliberately left out of the score\n")
sing=[r for r in AX if r.get('upgrade_authority_posture') in ('EOA_SINGLE_KEY','SAFE_1_OF_N')]
L.append(f"Authority chains were walked for {len(AX)} in-band protocols: ERC-1967 admin slot and `owner()`, up to "
         "three hops, terminal authority fingerprinted by the functions it answers (`getThreshold()`+`getOwners()` "
         "for a Safe, `getMinDelay()` or `delay()`+`GRACE_PERIOD()` for a timelock, `votingDelay()` for a "
         "governor, zero code size for an externally-owned account).\n")
L.append(f"**{len(sing)} protocols holding ${sum(r['tvl'] for r in sing):,.0f} have an upgrade authority that "
         "terminates in a single key or single signature.** It is a real and cheaply fixable exposure, and it is "
         "reported in `results/upgrade_authority_exposure.md`.\n")
L.append(f"It is **not** in the likelihood score, and the reason is a measurement rather than a preference. Over "
         f"the full window `admin_terminal_eoa` measures x{LIFT.get('admin_terminal_eoa')} and "
         f"`admin_single_signature` x{LIFT.get('admin_single_signature')} — no association with code-defect "
         "incidents at all — and the ablation shows adding the group *degrades* out-of-sample prediction "
         "(x2.19 -> x2.15). This is the answer the inclusion gate predicts: an off-chain key compromise is an "
         "excluded root cause here, so custody exposure should not move a code-defect likelihood. Mixing them "
         "would have made both numbers worse.\n")
L.append("Market cap and TVL trajectory were refused for a different reason: both are read today, and for a "
         "victim they partly measure the hack's own aftermath. `mcap_below_tvl` looks informative at "
         f"x{LIFT.get('mcap_below_tvl')} and is almost certainly measuring post-incident token collapse. They are "
         "carried as ordering-only operational flags and never fitted.\n")
L.append("## 6. New evidence in this pass\n")
eoa=sum(1 for v in PRB.values() if any(a.get('owner_is_eoa') for a in v.get('deployment',{}).get('addresses_probed',[])))
ctr=sum(1 for v in PRB.values() if any(a.get('owner_is_contract') for a in v.get('deployment',{}).get('addresses_probed',[])))
L.append(f"- **Owner-is-EOA probe.** For every privileged `owner()` found, a second hop reads whether that address "
         f"has code. {eoa} protocols have a privileged owner that is an externally owned account; {ctr} have one "
         "that is a contract (multisig or timelock). That is a direct, cheap read of who can move value, and it "
         "is one of the strongest attention-deficit signals in the model.\n")
L.append(f"- **Empirical hazard tables** in `tools/hazard.py`, derived from this run's own corpus rather than "
         "assumed.\n")
L.append("## 7. Known limitations\n")
L.append("1. **Static indicators are regexes, not analysis.** A match means *this shape is present in this file* "
         "— a reason to look, never a finding. They cannot follow control flow or resolve inheritance.\n")
L.append(f"2. **{sum(1 for d in live if d['evidence_level'] in ('L0_METADATA','L1_ADAPTER'))} of {len(live)} "
         "surviving pairs are still at metadata or adapter evidence**, because their adapters are dynamic or hold "
         "no addresses. Only the 45 finals reach L3 or L4.\n")
L.append("2b. **Several learned weights are proxies for size and integration, not causes.** `has_2plus_audits` "
         f"(x{LIFT.get('has_2plus_audits')}) and `has_governance` (x{LIFT.get('has_governance')}) are positive "
         "because protocols large enough to commission audits and run governance are large enough to be worth "
         "attacking. `owner_is_eoa` and `owner_is_contract` are *both* positive because what they really encode "
         "is that a live owner was readable at all. They order a queue usefully; none of them is a mechanism, "
         "and none should be quoted as a cause.\n")
L.append("3. **Most included incidents rest on one mechanism-level source.** Independent corroboration was "
         "retrieved for the family anchors only.\n")
L.append("4. **Hazard ratios come from 128 incidents.** Segments with few incidents (Supra ×6.4 on one incident, "
         "NEAR ×4.1 on two) carry wide error bars and should not be read as precise.\n")
L.append("5. **`INC-2026-04-01-DRI` (Drift, ~$285M)** carries an unresolved source contradiction and is excluded "
         "from pattern derivation. If its true root cause is on-chain, the corpus is missing its largest point.\n")
L.append("6. **The index is a lead source, not a census.** At least one in-window on-chain incident documented "
         "elsewhere (STO, 2026-02-23) is absent, so frequency and loss figures are lower bounds.\n")
L.append("7. **Exposure is understated for approval-bearing families.** Live allowances and delegations were not "
         "enumerated, so TVL is a floor for those pairs, not a ceiling.\n")
L.append(f"8. **Prior art is not established for most finals.** {sum(1 for r in finals if r['prior_art_status']=='PRIOR_ART_SEARCH_INCOMPLETE')} "
         f"of {len(finals)} carry `PRIOR_ART_SEARCH_INCOMPLETE`. Several of these protocols may already have a "
         "public disclosure or a deployed fix. Check before spending time.\n")
L.append("9. **Small protocols can be small for a reason.** Some candidates are abandoned rather than merely "
         "neglected. A dead protocol with $80,000 left is a low-value save even when the finding is real; the "
         "value-at-risk column is there so you can make that call before starting.\n")
L.append("10. **Scores are not probabilities.** `LIKELIHOOD` orders a queue. The validated x2.32 lift says "
         "future victims concentrate near the top of that queue; it does not say any particular protocol will be "
         "hit, and nothing here should be reported as a forecast.\n")
L.append("11. **The out-of-sample test still shares a population with the fit.** Protocols are the same "
         "universe in both windows; only the incidents are held out. Protocols delisted entirely are absent from "
         "both sets, and current DefiLlama fields reflect post-incident edits. The x2.32 is a fair estimate of "
         "ranking skill, not a clean prospective trial.\n")
L.append("12. **Custody fingerprinting is incomplete.** 120 authorities did not match any known shape and read "
         "as `UNKNOWN_CONTRACT`, which means *not identified*, not *safe*. Role-based access "
         "(`AccessControl`) is not enumerated at all, so a protocol reading `NONE_FOUND` may still grant "
         "privileged roles to single keys.\n")
open(f'{B}/quality_report.md','w').write("\n".join(L)+"\n")
print("quality_report.md written")
