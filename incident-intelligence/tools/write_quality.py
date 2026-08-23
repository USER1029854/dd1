#!/usr/bin/env python3
import json,collections,os
B='/home/user/dd1/incident-intelligence'
inc=[json.loads(l) for l in open(f'{B}/incidents/included.jsonl')]
D=[json.loads(l) for l in open(f'{B}/protocols/deep_screened.jsonl')]
F=json.load(open(f'{B}/families/families.json'))
corr=collections.Counter(i['corroboration'] for i in inc)
L=[]
L.append("# Quality report\n")
L.append("> **Verdict:** *Pattern library complete for the stated six-month window; candidate screen complete "
         "within stated filters.*\n>\n"
         "> This is a discovery and prioritisation pass. No protocol named anywhere in this output is asserted to be "
         "exploitable or vulnerable. Every candidate requires separate authorized verification in a local or pinned-fork "
         "environment. A completed screen is not evidence that non-selected protocols are safe.\n")
L.append("## 1. Evidence grading rule actually applied\n")
L.append("The source index is explicitly a lead source, not sufficient alone for a high-confidence root cause. "
         "The grading rule applied in this run, stated so it can be audited:\n")
L.append("| Grade | Rule as applied | Count |")
L.append("|---|---|---:|")
L.append(f"| **A** | Mechanism-level index record **plus** at least one independent technical source retrieved "
         f"(official postmortem, security-firm analysis) **or** deployed-code/live-state evidence gathered in this run | "
         f"{sum(1 for i in inc if i['evidence_grade']=='A')} |")
L.append(f"| **B** | Mechanism-level index record naming a specific contract, function, parameter or state variable — "
         f"a strong technical source in itself — with no contradicting source found, but no second independent source retrieved | "
         f"{sum(1 for i in inc if i['evidence_grade']=='B')} |")
L.append("| **C** | On-chain root cause plausible but a material link unverified, or a mixed on/off-chain attribution "
         "that could not be resolved. Written to `provisional.jsonl`; excluded from all statistics and ranking weight. | 22 |")
L.append("| **D** | Mechanism vague, contradictory or unsupported. Excluded from pattern derivation and recorded in "
         "`excluded.jsonl` under `PATTERN_EXC_GRADE_D`, with the gate result preserved. | see excluded.jsonl |")
L.append(f"\nCorroboration status across the {len(inc)} included incidents: "
         + ", ".join(f"`{k}` = {v}" for k,v in corr.most_common()) + ".\n")
L.append("**This is the single most important limitation of the run.** "
         f"{corr.get('SLOWMIST_MECHANISM_RECORD_ONLY',0)} of {len(inc)} included incidents rest on one mechanism-level "
         "source. Independent corroboration was performed for the incidents that anchor the highest-weight families "
         "(Lazy Summer, Venus, Ekubo, Secret Network, Blend/YieldBlox, Curve LlamaLend, Rhea, Singularity, Verus, and "
         "the BSC pair-burn template), and those upgrades are recorded per incident in the `corroboration` field. "
         "A grade-B record is a well-specified mechanism, not a verified one.\n")
L.append("## 2. Mechanical quality gates (§18)\n")
L.append("The gate results are produced by `tools/check_manifest.py` and written to `results/manifest_check.txt`. "
         "That script is the authority; the narrative below explains the judgement calls behind three of the gates.\n")
L.append("### Clone handling (§18.1)\n")
L.append("Three lineages collapse to a single root cause: the two Verus bridge exploits (same unpatched "
         "`checkCCEValues` value-equality gap, May and July), Flooring/Asterix (one shared DN404/BT404 codebase, one day "
         "apart), and the Computility pair (TGAI/YSDAO, one operator template). The 14-deployment BSC deferred-burn "
         "cluster is treated as **template propagation**, not forking: those are independent deployments that "
         "reimplement the same pattern, so they count as independent root causes, but the family's recurrence "
         "multiplier is capped so they cannot masquerade as fourteen independent discoveries.\n")
L.append("### Generic-label prohibition (§18.2)\n")
L.append("No family is named for an attack technique. Flash loans appear only as `optional_amplifiers`. The source "
         "database's `Attack method` string is preserved on every incident record under the field name "
         "`slowmist_attack_method_label_NOT_USED_FOR_CLUSTERING` so a reviewer can confirm it never drove clustering. "
         "Where the source labelled an incident *Flash Loan Attack*, the derived family is about what the flash loan "
         "reached — for example FoxMarket sits in `ORACLE-SPOT-THIN-LIQUIDITY` because the defect was a spot quote "
         "captured before a state-changing swap, not the borrowing of capital.\n")
L.append("### Novelty (§14, §18.4)\n")
L.append("`NO_PUBLIC_MATCH_FOUND` is **never emitted anywhere in this run**. A per-deployment sweep of published "
         "audits, audit competitions, upstream advisories and postmortems was performed only for the pairs recorded in "
         "`protocols/prior_art.json`; every other pair carries `PRIOR_ART_SEARCH_INCOMPLETE`, which is an addition to "
         "the required enum because that enum has no value meaning *not yet searched*, and using any of its existing "
         "values would overstate what was checked.\n")
L.append("## 3. What the screen found, and what that cost\n")
L.append("Two results are worth stating plainly because they show the gate doing its job in both directions:\n")
L.append("- **Venus Core Pool was killed by its own fix.** Venus was the largest donation-attack victim in the window "
         "(March 2026, THE market). Following its beacon proxy to the deployed `VToken` implementation shows an internal "
         "cash counter, so the exchange rate is no longer a function of the raw token balance. The mandatory "
         "precondition is proven absent and the pair is dead, despite $1.25B of live TVL and a perfect archetype match. "
         "A screen that ranked on similarity alone would have put it near the top.\n")
L.append("- **Steakhouse Financial was downgraded by documented guards.** It was the highest-exposure curator in the "
         "worklist (~$2.98B). Published risk documentation shows owner multisig, 7-day action timelocks and an Aragon "
         "guardian veto. That closes the malicious-component-addition path, so the pair became a near miss rather than "
         "a candidate. The residual question recorded in the near-miss library is narrower and more useful: a multi-day "
         "timelock does not address the Lazy Summer shape, where the loss came from a component that was already "
         "approved and still counted in `totalAssets()` during an incomplete offboarding.\n")
L.append("## 4. Known limitations\n")
L.append("1. **Corpus completeness.** The index is a lead source, not a census. At least one in-window on-chain "
         "incident documented elsewhere (STO token, 2026-02-23, pair-burn reserve manipulation) does not appear in it. "
         "Frequency and loss statistics are therefore lower bounds.\n")
L.append("2. **One unresolved source contradiction.** `INC-2026-04-01-DRI` (Drift Protocol, ~$285M — by loss the "
         "largest event in the window) carries an attack-method label of *Social Engineering* against a description of "
         "a vault exploit with no mechanism. It is graded D and excluded from pattern derivation. If its true root "
         "cause is on-chain, the corpus is missing its single largest data point.\n")
L.append("3. **Reference retrieval.** 104 of 130 reference URLs for gate-passing incidents are client-rendered social "
         "posts whose bodies are not machine-retrievable. They are recorded as `LEAD_ONLY_CLIENT_RENDERED` and were "
         "never counted as corroboration.\n")
L.append("4. **Loss figures are as-reported.** No independent net-loss reconstruction was performed. Several "
         "incidents involve partial returns, whitehat recovery or frozen funds; `net_loss_basis` preserves the raw "
         "string, and recoveries are visible in the narrative but are not netted out of the totals.\n")
L.append("5. **Sixteen families have no addressable population here.** The highest-frequency family in the corpus "
         "(`TOKEN-DEFERRED-BURN-LP-RESERVE-DESYNC`, 15 incidents) targets individually deployed tokens that are not "
         "DefiLlama protocol entries. Those families are listed in "
         "`protocols/families_not_screenable_in_universe.json` and belong to a token-level monitoring workstream. "
         "A reader who assumed the candidate list covers the whole family library would be wrong.\n")
L.append("6. **Deep screening is not an audit.** 243 pairs were gated, but only 5 reached `L4_GUARD_REVIEW` — the "
         "level at which a decisive guard was actually read out of deployed implementation code. The rest rest on "
         "adapter architecture and live-state reads.\n")
L.append("7. **Exposure is understated for approval-bearing families.** Live ERC-20/721 allowances and credit "
         "delegations to router, executor and module contracts were not enumerated on-chain. For "
         "`CALLDATA-CALLER-CONTROLLED-TARGET`, `CALLBACK-UNAUTHENTICATED-CALLER-USES-APPROVALS` and "
         "`APPROVALS-TO-UPGRADEABLE-SPENDER`, TVL is the wrong exposure basis and the recorded figure is a floor. "
         "This is flagged per-candidate in `authority_notes`.\n")
L.append("8. **DefiLlama's `deprecated` flag is ambiguous.** It is also used when an adapter is superseded or its TVL "
         "is counted elsewhere. Base's canonical bridge carries it at $2.79B. The flag alone is therefore scored as "
         "UNKNOWN and a caution note is attached to every affected candidate.\n")
L.append("9. **Governance economics were not measured.** For `GOV-CHEAP-CONTROL-NO-TIMELOCK`, the cost of acquiring "
         "decisive voting power was not compared against controlled value and timelock parameters were not read "
         "on-chain. Both preconditions stay UNKNOWN and score zero, so those pairs are open questions, not claims.\n")
L.append("10. **Scores are not probabilities.** `MATCH_SCORE` measures how much of a family's observable prerequisite "
         "signature was confirmed. `PREVENTION_SCORE` is a prioritisation heuristic. Neither is an exploit likelihood, "
         "and neither should be reported as one.\n")
open(f'{B}/quality_report.md','w').write("\n".join(L)+"\n")
print("quality_report.md written")
