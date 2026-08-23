# Run summary

**Run:** `RUN-2026-08-23-DEFI-INCIDENT-PRIORITIZATION`  ·  **Window:** 2026-02-22 to 2026-08-22 (inclusive, incident date not publication date)  ·  **Run date (UTC):** 2026-08-23

## Incident corpus

| Metric | Value |
|---|---:|
| Date window | 2026-02-22 → 2026-08-22 |
| SlowMist pages fetched (all-category crawl) | 12 |
| Boundary proof on final page | `BOUNDARY_PROVEN` (page 12: 0 in-window, 20/20 older than window start) |
| Per-category crawls (category attribution) | 20 categories, all reaching back past window start |
| Raw incident rows captured | 240 |
| Incidents inside window | 205 |
| Included, grade A | 58 |
| Included, grade B | 52 |
| Provisional (grade C) | 22 |
| Excluded | 73 |
| Duplicate/clone/repeat lineages | 6 |
| Total included reported loss | $139,297,649 |
| Unique root causes (lineage-collapsed) | 107 |
| Mechanism families | 43 |
| Single-event families | 8 |
| Date-unverified incidents | 0 |

### Exclusion counts by reason

| Reason code | Count |
|---|---:|
| `EXC_PRIVATE_KEY` | 13 |
| `EXC_INFRA_SERVER` | 10 |
| `PATTERN_EXC_GRADE_D` | 10 |
| `EXC_CREDENTIAL_COMPROMISE` | 7 |
| `EXC_SUPPLY_CHAIN_FRONTEND` | 7 |
| `EXC_DNS_DOMAIN` | 6 |
| `EXC_CAUSE_UNKNOWN` | 5 |
| `EXC_PHISHING_SOCIAL` | 5 |
| `EXC_WALLET_RNG_FIRMWARE` | 4 |
| `EXC_EXCHANGE_HOTWALLET` | 2 |
| `EXC_OFFCHAIN_CLIENT_PROTO` | 2 |
| `EXC_RUG_OR_ADMIN_MISUSE` | 1 |
| `EXC_OFFCHAIN_SIGNING_INFRA` | 1 |

### Largest families by incident count

| Family | Incidents | Unique root causes | 6-month loss | Most recent |
|---|---:|---:|---:|---|
| `TOKEN-DEFERRED-BURN-LP-RESERVE-DESYNC` | 14 | 14 | $5,425,242 | 2026-07-28 |
| `BRIDGE-MESSAGE-NOT-BOUND-TO-SOURCE` | 7 | 6 | $26,666,000 | 2026-08-09 |
| `ORACLE-SPOT-THIN-LIQUIDITY` | 7 | 7 | $21,658,540 | 2026-08-15 |
| `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY` | 7 | 7 | $6,971,179 | 2026-06-17 |
| `PROOF-VERIFICATION-BYPASSED` | 6 | 6 | $7,372,966 | 2026-07-02 |
| `ORACLE-STALE-OR-SILENT-FALLBACK` | 5 | 5 | $2,688,400 | 2026-07-23 |
| `GOV-CHEAP-CONTROL-NO-TIMELOCK` | 4 | 4 | $22,356,000 | 2026-07-15 |
| `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED` | 4 | 4 | $19,864,350 | 2026-06-10 |
| `CALLDATA-CALLER-CONTROLLED-TARGET` | 4 | 4 | $3,798,750 | 2026-08-06 |
| `LIQUIDATION-ON-MANIPULABLE-VALUATION` | 4 | 4 | $3,360,921 | 2026-07-22 |
| `AUTH-MISSING-ON-VALUE-MOVING-PATH` | 4 | 4 | $814,000 | 2026-07-28 |
| `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET` | 3 | 3 | $18,524,350 | 2026-04-22 |

## DefiLlama screen

| Metric | Value |
|---|---:|
| Protocols fetched from /protocols | 8103 |
| Protocols eligible (main queue, TVL ≥ $1,000,000) | 1284 |
| Sub-threshold high-fit queue preserved | 543 |
| Excluded from the universe | 6276 |
| Protocol-family pairs generated | 19186 |
| Families screened as protocol-family pairs | 27 |
| Families with no addressable population in this universe | 16 |
| Protocols in the stratified deep-screen worklist | 105 |
| Pairs deep-screened | 243 (requirement: ≥ 80) |
| Adapters successfully read | 104 |
| Adapters read via a shared registry | 35 |
| Adapters missing | 1 |
| Dynamic adapters (factory/registry driven) | 49 |
| Adapters depending on an external API | 57 |
| Pairs killed by a mandatory precondition | 11 |
| Pairs killed by a decisive guard | 1 |
| Pairs killed for lack of a lawful disclosure recipient | 1 |
| Surviving pairs | 230 |
| Final candidates | 20 |

### Candidates at each evidence level

| Evidence level | Surviving pairs | Final candidates |
|---|---:|---:|
| `L0_METADATA` | 0 | 0 |
| `L1_ADAPTER` | 177 | 0 |
| `L2_DEPLOYMENT` | 14 | 0 |
| `L3_STATE` | 34 | 18 |
| `L4_GUARD_REVIEW` | 5 | 2 |

## Quality

| Metric | Value |
|---|---|
| Unresolved source contradictions | 1 — `INC-2026-04-01-DRI` (Drift Protocol, ~$285M): the index's attack-method label reads *Social Engineering* while its own description describes a vault exploit with no mechanism given. Graded D and excluded from pattern derivation. |
| Corpus completeness gap | At least one in-window on-chain incident documented elsewhere is absent from the SlowMist index (STO token, 2026-02-23, pair-burn reserve manipulation, per DARKNAVY). The index is a lead source, not a census. |
| Unresolved deployment mappings | 1 adapter(s) unresolved; 190 pairs remain at metadata/adapter evidence |
| Protocols capped by weak evidence | 177 pairs capped at the 45-point adapter ceiling; 0 at the 20-point metadata ceiling |
| Prior-art searches incomplete | 17 of 20 final candidates. `NO_PUBLIC_MATCH_FOUND` is never emitted, so no novelty is claimed anywhere in this run. |
| Commands reproducible | `commands.sh` replays every retrieval and transformation step in execution order |
| Manifest checker result | see `results/manifest_check.txt` |

## Safety attestation

- All production-chain access was read-only: `eth_call`, `eth_getStorageAt`, `eth_getCode`, explorer `getsourcecode`, and HTTP GET.
- Zero transactions constructed, signed, simulated as a broadcast against live user state, or submitted.
- Zero credentials recovered, derived or used. No private key material was touched.
- No exploitation sequence, production calldata, or extraction optimisation was produced anywhere in this output.
- Only contracts with a documented relationship to a selected DefiLlama protocol were read.
- One protocol-family pair was withheld from candidate promotion because the entity is sanctions-designated and an authorized defensive engagement has no lawful disclosure recipient there.
