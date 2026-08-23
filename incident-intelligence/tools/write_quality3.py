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
L.append("## 5. New evidence in this pass\n")
eoa=sum(1 for v in PRB.values() if any(a.get('owner_is_eoa') for a in v.get('deployment',{}).get('addresses_probed',[])))
ctr=sum(1 for v in PRB.values() if any(a.get('owner_is_contract') for a in v.get('deployment',{}).get('addresses_probed',[])))
L.append(f"- **Owner-is-EOA probe.** For every privileged `owner()` found, a second hop reads whether that address "
         f"has code. {eoa} protocols have a privileged owner that is an externally owned account; {ctr} have one "
         "that is a contract (multisig or timelock). That is a direct, cheap read of who can move value, and it "
         "is one of the strongest attention-deficit signals in the model.\n")
L.append(f"- **Empirical hazard tables** in `tools/hazard.py`, derived from this run's own corpus rather than "
         "assumed.\n")
L.append("## 6. Known limitations\n")
L.append("1. **Static indicators are regexes, not analysis.** A match means *this shape is present in this file* "
         "— a reason to look, never a finding. They cannot follow control flow or resolve inheritance.\n")
L.append(f"2. **{sum(1 for d in live if d['evidence_level'] in ('L0_METADATA','L1_ADAPTER'))} of {len(live)} "
         "surviving pairs are still at metadata or adapter evidence**, because their adapters are dynamic or hold "
         "no addresses. Only the 45 finals reach L3 or L4.\n")
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
L.append("10. **Scores are not probabilities.** `HACK_LIKELIHOOD` orders a queue. It is not a forecast, and "
         "nothing in it should be reported as one.\n")
open(f'{B}/quality_report.md','w').write("\n".join(L)+"\n")
print("quality_report.md written")
