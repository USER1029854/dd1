# Excluded protocols and killed protocol-family pairs

Exclusion here means *not carried into candidate ranking*. It is **never** a statement that a protocol is safe.

## 1. Universe-level exclusions (Phase F eligibility)

| Reason | Protocols |
|---|---:|
| `BELOW_TVL_THRESHOLD` | 6537 |
| `EXCLUDED_FLAGGED_RUGGED` | 116 |
| `EXCLUDED_NON_PROTOCOL_CHAIN_ENTRY` | 86 |
| `EXCLUDED_CEX_OR_NON_PROTOCOL` | 80 |

Of the 6537 protocols below the $1,000,000 TVL threshold, 543 were preserved in the sub-threshold high-fit queue because they are deprecated, hold authority over external value, curate third-party vaults, operate routers that hold user approvals, or carry on-chain governance authority. TVL is not equated with total value at risk.

## 2. Pairs killed at the mandatory-precondition gate

| Protocol | Family | Kill reason | Condition proven absent / guard found |
|---|---|---|---|
| `base-bridge` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `etherfi-borrowing-market` | `ACC-DONATION-UNACCOUNTED-BALANCE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | inflated_rate_consumed_by_value_decision, third_party_claims_exposed |
| `granary-finance` | `ACC-DONATION-UNACCOUNTED-BALANCE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | inflated_rate_consumed_by_value_decision, third_party_claims_exposed |
| `guru-network-classic` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `multichain` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `pac-finance` | `ACC-DONATION-UNACCOUNTED-BALANCE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | inflated_rate_consumed_by_value_decision, third_party_claims_exposed |
| `percent-finance` | `ACC-DONATION-UNACCOUNTED-BALANCE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | inflated_rate_consumed_by_value_decision, third_party_claims_exposed |
| `saddle-finance` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `steakhouse-financial` | `ACC-DONATION-UNACCOUNTED-BALANCE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | inflated_rate_consumed_by_value_decision, third_party_claims_exposed |
| `steakhouse-financial` | `AUTH-MISSING-ON-VALUE-MOVING-PATH` | DECISIVE_GUARD_FOUND | multisig_plus_timelock_plus_guardian_veto |
| `tornado-cash` | `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY` | SANCTIONS_DESIGNATED_NO_LAWFUL_ENGAGEMENT | responsible-disclosure recipient |
| `ultrayield-curator` | `ACC-DONATION-UNACCOUNTED-BALANCE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | inflated_rate_consumed_by_value_decision, third_party_claims_exposed |
| `venus-core-pool` | `ACC-DONATION-UNACCOUNTED-BALANCE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | rate_reads_raw_balance |

Every killed pair is written in full to `families/near_miss_library.jsonl` with its initial similarity, the decisive guard or absent precondition, and the uncertainty that remains. Near misses are first-class results: they are what make the next pass more precise.

## 3. Families with no addressable population in this universe

| Family | Incidents | Why no protocol-family pair was generated |
|---|---:|---|
| `TOKEN-DEFERRED-BURN-LP-RESERVE-DESYNC` | 14 | Victims are individually deployed BSC/Base tokens with custom transfer logic that are not listed as DefiLlama protocols; the family has no addressable protocol population in this universe. Handed to the token-level monitoring workstream instead. |
| `TOKEN-TRANSFER-OVERRIDE-BREAKS-CONSERVATION` | 3 | Same population problem as the deferred-burn family. |
| `SECRET-EMBEDDED-IN-PUBLIC-CODE-AS-AUTH` | 3 | Requires bytecode constant analysis per contract; run as a sweep over deep-screened deployments rather than as a ranked pair. |
| `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 3 | Detected by parameter-shape sweep over deep-screened deployments. |
| `AUTH-IDENTITY-SATISFIABLE-BY-ATTACKER-CONTRACT` | 3 | Detected by source-grep sweep over deep-screened deployments. |
| `TOKEN-TRANSFER-INTENT-HEURISTIC-FORGEABLE` | 2 | Same population problem as the deferred-burn family. |
| `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | 2 | Applies to token contracts with accrual hooks; only reachable through per-token screening, not the protocol universe. |
| `TOKEN-PACKED-OWNERSHIP-UNDERFLOW` | 2 | Requires DN404/BT404 lineage; no in-universe protocol above the TVL threshold carries it. |
| `METATX-SENDER-IDENTITY-CONFUSION` | 2 | Requires ERC-2771 detection per contract; run as a sweep. |
| `ACC-DUPLICATE-ID-ACCUMULATION` | 2 | Detected by selector-shape sweep over deep-screened deployments. |
| `SIG-VERIFIER-DEFEATABLE` | 2 | Detected by source-grep sweep over deep-screened deployments. |
| `AUTH-ZERO-ADDRESS-ACCEPTED` | 1 | Screened as a cheap read-only sweep (owner()==address(0) with non-zero balance) rather than as a protocol-family pair. |
| `STORAGE-LAYOUT-COLLISION-PHANTOM-CREDIT` | 1 | Requires a storage-layout dump per contract; run as a sweep over deep-screened deployments. |
| `ACC-CREDIT-NOT-RECEIVED` | 1 | Reward-tracker contracts are rarely separate DefiLlama entries; folded into the reward-index sweep. |
| `ACC-HARDCODED-PEG-REDEMPTION` | 1 | Folded into the stablecoin-issuer oracle screen. |
| `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 1 | Detected by selector sweep over deep-screened deployments. |
