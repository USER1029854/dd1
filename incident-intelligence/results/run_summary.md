# Run summary

**Run:** `RUN-2026-08-23-DEFI-INCIDENT-PRIORITIZATION` · **Window:** 2026-02-22 to 2026-08-22 (inclusive, incident date) · **Run date (UTC):** 2026-08-23

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
| $2M-$10M | 14 | 11% |
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
| Included grade A / B | 58 / 52 |
| Provisional (C) / Excluded | 22 / 73 |
| Total included reported loss | $139,297,649 |
| Unique root causes | 107 |
| Mechanism families | 43 (8 single-event) |

## Does the ranking actually predict anything?

The model is fitted on incidents from **2022-2024** and then scored against incidents from **2025-2026** that it never saw. That is the only number in this run worth trusting about predictive power.

| | |
|---|---:|
| Protocols hacked after the fitting window, unseen while fitting | 95 |
| Median future victim lands at | 78.6th percentile |
| Future victims in the model's top quartile | 58% |
| Lift over chance | **x2.32** |

### Which additions earned their place

Each variant is refitted from scratch and revalidated, so a gain is attributed rather than assumed.

| Variant | Signals | Median percentile | Top quartile | Lift |
|---|---:|---:|---:|---:|
| baseline (v3 feature set) | 18 | 77.7th | 55% | x2.19 |
| + exposure age | 20 | 78.6th | 58% | x2.32 |
| + admin posture | 22 | 76.8th | 54% | x2.15 |
| + public-repo flag | 18 | 77.7th | 55% | x2.19 |
| + all v4 additions | 24 | 77.7th | 58% | x2.32 |

**Exposure age was the only addition that paid.** It also points the opposite way from the obvious intuition: a protocol under a year old carries lift **x1.866**, one over three years old **x0.327**. It is not the abandoned deployments that get hit. That single fact explains why several 'neglect' signals measure as protective here — they are markers of age, and age is protective.

**Custody posture was measured, ablated, and then dropped from the score.** Adding it moved out-of-sample lift x2.19 -> x2.15, and over the full window it measures x0.982 — a single-key upgrade authority does *not* predict a code defect. That is the expected answer, because an off-chain key compromise is an excluded root cause under the inclusion gate. It is reported on its own instead; see below.

## Custody exposure, reported separately

Walking ERC-1967 admin slots and `owner()` chains up to three hops, then fingerprinting the terminal authority by the functions it answers.

| Terminal authority | Protocols |
|---|---:|
| `EOA_SINGLE_KEY` | 160 |
| `UNKNOWN_CONTRACT` | 120 |
| `SAFE_M_OF_N` | 69 |
| `TIMELOCK` | 11 |
| `SAFE_1_OF_N` | 4 |
| `GOVERNOR` | 1 |

**23 protocols holding $56,405,869 have an ERC-1967 upgrade authority that terminates in a single key or a single signature.** No code fix removes that exposure, and moving it behind a threshold-2 multisig with a non-zero delay is a configuration change. Full list in `results/upgrade_authority_exposure.md`.


## Band screen

| Metric | Value |
|---|---:|
| Protocols fetched | 8103 |
| Above the $50,000 floor | 2662 |
| Inside the $50k-$30M band | 2268 |
| Above the band, dropped (assumed professionally covered) | 363 |
| Above the band, kept on explicit danger | 31 |
| Below the floor, recorded but not screened | 662 |
| Protocols deep-screened | 1200 |
| Protocol-family pairs screened | 20901 |
| Pairs killed at the gate | 612 |
| Adapters read | 1721 |
| Protocols with live chain evidence | 859 |
| Addresses read on-chain | 2467 |
| Privileged owner() resolving to an EOA | 143 protocols |
| Authority chains walked and fingerprinted | 394 protocols |
| Verified contracts analysed | 1270 |
| Final candidates | 60 |
| Median value at risk across finals | $237,912 |

### Most common measured signals across final candidates

| Signal | Candidates | Measured lift |
|---|---:|---:|
| `on_ethereum` | 49 | x2.121 |
| `chain_hazard_ge2` | 49 | x2.134 |
| `single_audit_only` | 46 | x1.53 |
| `multichain_gt3` | 37 | x1.77 |
| `on_bsc` | 37 | x1.047 |
| `is_proxy` | 29 | x1.858 |
| `owner_is_contract` | 27 | x2.578 |
| `has_oracle_declared` | 25 | x2.127 |
| `authority_addrs_beyond_tvl` | 25 | x1.174 |
| `owner_is_eoa` | 21 | x0.865 |
| `has_governance` | 15 | x2.968 |
| `has_2plus_audits` | 12 | x1.975 |

## Quality

| Metric | Value |
|---|---|
| Unresolved source contradictions | 1 — `INC-2026-04-01-DRI` (Drift, ~$285M): attack-method label says *Social Engineering* while the description describes a vault exploit with no mechanism. Graded D, excluded from pattern derivation. |
| Corpus completeness gap | At least one in-window on-chain incident documented elsewhere (STO token, 2026-02-23) is absent from the index. Counts are lower bounds. |
| Pairs still at metadata or adapter evidence | 17320 of 20289 |
| Prior-art searches incomplete | 50 of 60 finals. `NO_PUBLIC_MATCH_FOUND` is never emitted. |
| Commands reproducible | `commands.sh` replays every retrieval and transformation step |
| Manifest checker | see `results/manifest_check.txt` |

## Safety

- All production-chain access read-only: `eth_call`, `eth_getStorageAt`, `eth_getCode`, explorer `getsourcecode`, HTTP GET.
- Zero transactions constructed, signed, simulated as a broadcast, or submitted.
- Zero credentials recovered or used; none committed.
- No exploitation sequence or production calldata anywhere in this output.
- Sanctions-designated entities are withheld from candidate promotion: an authorized defensive engagement has no lawful disclosure recipient there.
