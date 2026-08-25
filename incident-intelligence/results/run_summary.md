# Run summary

**Run:** `RUN-2026-08-23-DEFI-INCIDENT-PRIORITIZATION` · **Window:** 2026-02-22 to 2026-08-22 (inclusive, incident date) · **Run date (UTC):** 2026-08-23

## Every candidate here is one you have not been given before

A candidate list is a queue of work, not a leaderboard. Earlier runs of this screen handed over **466 protocols** across **8 deliveries**, and re-ranking the same set would hand over nothing new. Those protocols are withheld from this run's candidates. They are not resolved and not ruled out; they were already given. The ledger is `protocols/delivered_ledger.json`, reconstructed from git history rather than from anything carried between runs, and every withheld protocol still appears in `candidates_all.csv` with `previously_delivered=YES` and the run that delivered it.

## What this run optimises for

An independent reviewer preventing real losses, not a fund allocating audit retainers. Two consequences drive everything downstream:

1. **A $50,000 to $30,000,000 band.** Below it there is nothing worth saving. Above it, protocols are assumed to carry dedicated professional coverage and are dropped unless specific danger evidence says otherwise.

2. **Exposure does not drive the ranking.** In this run's own corpus the median on-chain loss was **$252,000** and **84% of incidents cost under $2,000,000**; only 5% exceeded $10,000,000. Size is a poor predictor of being attacked, so the primary ranking is likelihood, and value at risk is reported beside it rather than baked into it.

## Empirical victim profile (derived from this corpus, not assumed)

| Loss band | Incidents | Share |
|---|---:|---:|
| under $100k | 35 | 27% |
| $100k-$500k | 42 | 33% |
| $500k-$2M | 31 | 24% |
| $2M-$10M | 15 | 12% |
| over $10M | 6 | 5% |

Median **$254,000**, p75 **$1,140,000**, p90 **$3,700,000**.

### Hazard ratios: incident share divided by eligible-protocol share

A ratio above 1 means the segment is over-represented among actual victims.

| Category | Hazard | | Chain | Hazard |
|---|---:|---|---|---:|
| `Farm` | ×13.74 | | `Supra` | ×6.42 |
| `Algo-Stables` | ×13.2 | | `Near` | ×4.08 |
| `Privacy` | ×12.1 | | `NEAR` | ×4.08 |
| `Staking Pool` | ×5.04 | | `Binance` | ×3.61 |
| `Bridge` | ×3.59 | | `BSC` | ×3.61 |
| `Cross Chain Bridge` | ×3.59 | | `Ethereum` | ×2.54 |
| `Canonical Bridge` | ×3.59 | | `Sui` | ×1.93 |
| `Liquidity Manager` | ×3.36 | | `Arbitrum` | ×1.29 |
| `Options` | ×2.42 | | `Solana` | ×1.11 |
| `Leveraged Farming` | ×2.0 | | `Base` | ×0.96 |

Risk Curators (×0.50) and RWA (×0.46) are *under*-represented among victims. An earlier pass of this run ranked them highly on exposure; the corpus says that was the wrong emphasis for this objective.

## Incident corpus

| Metric | Value |
|---|---:|
| SlowMist pages fetched | 12 (boundary `BOUNDARY_PROVEN`) |
| Raw rows / inside window | 240 / 205 |
| Included grade A / B | 60 / 51 |
| Provisional (C) / Excluded | 22 / 72 |
| Total included reported loss | $142,151,649 |
| Unique root causes | 108 |
| Mechanism families | 48 (12 single-event) |

## Does the ranking actually predict anything?

The model is fitted on incidents from **2022-2024** and then scored against incidents from **2025-2026** that it never saw. That is the only number in this run worth trusting about predictive power.

| | |
|---|---:|
| Protocols hacked after the fitting window, unseen while fitting | 95 |
| Median future victim lands at | 78.7th percentile |
| Future victims in the model's top quartile | 59% |
| Lift over chance | **x2.36** |

### Which additions earned their place

Each variant is refitted from scratch and revalidated, so a gain is attributed rather than assumed.

| Variant | Signals | Median percentile | Top quartile | Lift |
|---|---:|---:|---:|---:|
| baseline (v3 feature set) | 18 | 77.4th | 55% | x2.19 |
| + exposure age | 20 | 78.7th | 59% | x2.36 |
| + admin posture | 22 | 78.1th | 55% | x2.19 |
| + public-repo flag | 18 | 77.4th | 55% | x2.19 |
| + all v4 additions | 24 | 80.5th | 59% | x2.36 |

**Exposure age was the only addition that paid.** It also points the opposite way from the obvious intuition: a protocol under a year old carries lift **x1.866**, one over three years old **x0.327**. It is not the abandoned deployments that get hit. That single fact explains why several 'neglect' signals measure as protective here — they are markers of age, and age is protective.

**Custody posture was measured, ablated, and then dropped from the score.** Adding it moved out-of-sample lift x2.19 -> x2.15, and over the full window it measures x0.846 — a single-key upgrade authority does *not* predict a code defect. That is the expected answer, because an off-chain key compromise is an excluded root cause under the inclusion gate. It is reported on its own instead; see below.

## Custody exposure, reported separately

Walking ERC-1967 admin slots and `owner()` chains up to three hops, then fingerprinting the terminal authority by the functions it answers.

| Terminal authority | Protocols |
|---|---:|
| `UNKNOWN_CONTRACT` | 191 |
| `EOA_SINGLE_KEY` | 187 |
| `SAFE_M_OF_N` | 81 |
| `TIMELOCK` | 18 |
| `SAFE_1_OF_N` | 4 |
| `GOVERNOR` | 2 |

**13 protocols holding $32,344,207 have an ERC-1967 upgrade authority that terminates in a single key or a single signature.** No code fix removes that exposure, and moving it behind a threshold-2 multisig with a non-zero delay is a configuration change. Full list in `results/upgrade_authority_exposure.md`.


## Band screen

| Metric | Value |
|---|---:|
| Protocols fetched | 8103 |
| Above the $50,000 floor | 2662 |
| Inside the $50k-$30M band | 2268 |
| Above the band, dropped (assumed professionally covered) | 363 |
| Above the band, kept on explicit danger | 31 |
| Below the floor, recorded but not screened | 662 |
| Protocols deep-screened | 2299 |
| Protocol-family pairs screened | 27863 |
| Pairs killed at the gate | 675 |
| Adapters read | 2459 |
| Protocols with live chain evidence | 834 |
| Addresses read on-chain | 2580 |
| Privileged owner() resolving to an EOA | 167 protocols |
| Authority chains walked and fingerprinted | 512 protocols |
| Verified contracts analysed | 1474 |
| Final candidates | 163 |
| Median value at risk across finals | $822,973 |

### Most common measured signals across final candidates

| Signal | Candidates | Measured lift |
|---|---:|---:|
| `on_ethereum` | 128 | x2.121 |
| `chain_hazard_ge2` | 128 | x2.134 |
| `no_audit_listed` | 93 | x0.582 |
| `single_chain` | 89 | x0.71 |
| `age_1_3y` | 69 | x0.902 |
| `single_audit_only` | 65 | x1.53 |
| `is_proxy` | 59 | x1.65 |
| `owner_is_contract` | 33 | x2.414 |
| `age_under_1y` | 32 | x1.866 |
| `multichain_gt3` | 31 | x1.77 |
| `on_bsc` | 31 | x1.047 |
| `pricing_surface_undeclared` | 28 | x1.91 |

## Quality

| Metric | Value |
|---|---|
| Unresolved source contradictions | 1 — `INC-2026-04-01-DRI` (Drift, ~$285M): attack-method label says *Social Engineering* while the description describes a vault exploit with no mechanism. Graded D, excluded from pattern derivation. |
| Corpus completeness gap | At least one in-window on-chain incident documented elsewhere (STO token, 2026-02-23) is absent from the index. Counts are lower bounds. |
| Pairs still at metadata or adapter evidence | 23722 of 27188 |
| Prior-art searches incomplete | 155 of 163 finals. `NO_PUBLIC_MATCH_FOUND` is never emitted. |
| Commands reproducible | `commands.sh` replays every retrieval and transformation step |
| Manifest checker | see `results/manifest_check.txt` |

## Safety

- All production-chain access read-only: `eth_call`, `eth_getStorageAt`, `eth_getCode`, explorer `getsourcecode`, HTTP GET.
- Zero transactions constructed, signed, simulated as a broadcast, or submitted.
- Zero credentials recovered or used; none committed.
- No exploitation sequence or production calldata anywhere in this output.
- Sanctions-designated entities are withheld from candidate promotion: an authorized defensive engagement has no lawful disclosure recipient there.
