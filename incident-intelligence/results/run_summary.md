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

## Band screen

| Metric | Value |
|---|---:|
| Protocols fetched | 8103 |
| Above the $50,000 floor | 2662 |
| Inside the $50k-$30M band | 2268 |
| Above the band, dropped (assumed professionally covered) | 351 |
| Above the band, kept on explicit danger | 43 |
| Below the floor, recorded but not screened | 662 |
| Protocols deep-screened | 700 |
| Protocol-family pairs screened | 9425 |
| Pairs killed at the gate | 358 |
| Adapters read | 1151 |
| Protocols with live chain evidence | 550 |
| Addresses read on-chain | 1610 |
| Privileged owner() resolving to an EOA | 96 protocols |
| Verified contracts analysed | 749 |
| Final candidates | 45 |
| Median value at risk across finals | $290,609 |

### Most common attention-deficit signals across final candidates

| Signal | Candidates |
|---|---:|
| `no_audit_listed` | 26 |
| `dead_front_end` | 24 |
| `no_timelock_in_source` | 22 |
| `single_audit_only` | 18 |
| `version_sibling_legacy` | 12 |
| `misrepresented_tokens` | 9 |
| `unverified_implementation` | 5 |
| `rebranded` | 4 |
| `warning_banner` | 2 |
| `fork_of_window_victim` | 2 |
| `is_window_victim` | 2 |
| `deprecated_flag` | 2 |

## Quality

| Metric | Value |
|---|---|
| Unresolved source contradictions | 1 — `INC-2026-04-01-DRI` (Drift, ~$285M): attack-method label says *Social Engineering* while the description describes a vault exploit with no mechanism. Graded D, excluded from pattern derivation. |
| Corpus completeness gap | At least one in-window on-chain incident documented elsewhere (STO token, 2026-02-23) is absent from the index. Counts are lower bounds. |
| Pairs still at metadata or adapter evidence | 7732 of 9067 |
| Prior-art searches incomplete | 44 of 45 finals. `NO_PUBLIC_MATCH_FOUND` is never emitted. |
| Commands reproducible | `commands.sh` replays every retrieval and transformation step |
| Manifest checker | see `results/manifest_check.txt` |

## Safety

- All production-chain access read-only: `eth_call`, `eth_getStorageAt`, `eth_getCode`, explorer `getsourcecode`, HTTP GET.
- Zero transactions constructed, signed, simulated as a broadcast, or submitted.
- Zero credentials recovered or used; none committed.
- No exploitation sequence or production calldata anywhere in this output.
- Sanctions-designated entities are withheld from candidate promotion: an authorized defensive engagement has no lawful disclosure recipient there.
