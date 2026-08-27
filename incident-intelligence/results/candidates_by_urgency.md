# Urgency-first candidates — ranked by the clock, not by likelihood

> **Discovery stage.** Nothing here says any protocol is exploitable. Each entry is a *high-urgency audit candidate*: named evidence matches a family's prerequisites, named evidence is unknown, and a named guard would falsify it. A high `URGENCY` is a triage order, never an exploit probability.

## The axis changed

The previous list ranked by how **likely** a protocol was to be hacked. That treats a novel bug nobody has found the same as one whose exploit is already written and circulating. This ranks by **how little stands between an attacker and the money now** — remediation status is no longer a footnote at the bottom of a block, it is 40 of the 100 points.

**The honest ceiling in this run is 28 of those 40, not 40.** The full band requires confirming that the specific fixed line is *absent from the deployed artifact* — an L4 read of runtime bytecode at the live address. This run has not performed that per-protocol check, so every Tier-1/2 row carries `KNOWN_ISSUE_STATUS_UNKNOWN` and names the decisive check that would settle it. That check is the first thing to run, and it is fast.

## What the tiers found

| Tier | What it means | Fresh protocols |
|---|---|---:|
| **1 — UNREMEDIATED-KNOWN** | a public technique exists for this protocol's own code, and it still holds funds | **67** |
| **2 — SHARED-DEPENDENCY** | an advisory or template live across a population with no patch-compliance mechanism | **117** |
| 3 — DEPENDENCY-IMPAIRMENT | the target holds or is backed by a system that is itself exposed | 4 |
| 4 — FORK-OF-RECENT-VICTIM | forked from a protocol exploited in-window | 18 |
| 5 — NOVEL-HIGH-FIT | strong match, no public disclosure — the clock has not started | 1497 |

This list leads with **70 Tier 1–2 candidates**. Spend the first hours entirely there.

## Handoff lines for CORE.md

```
TARGET=https://defillama.com/protocol/atomic-green || TIER=1 || FAMILY=UPGRADE-INITIALIZER-REACHABLE-LIVE || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2026-08-08 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=84486 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/lien || TIER=1 || FAMILY=UPGRADE-INITIALIZER-REACHABLE-LIVE || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2026-07-23 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=204912 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/sentiment || TIER=1 || FAMILY=SIG-VERIFIER-DEFEATABLE || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2023-04-04 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=517964 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/gamma || TIER=1 || FAMILY=HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2024-01-04 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=3105706 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/float-protocol || TIER=1 || FAMILY=HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2022-01-15 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=216418 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/arrakis-v1 || TIER=1 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2026-08-23 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=1494413 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/goldfinch || TIER=1 || FAMILY=AUTH-ZERO-ADDRESS-ACCEPTED || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2025-12-02 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=1645216 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/overnight-finance || TIER=1 || FAMILY=UPGRADE-INITIALIZER-REACHABLE-LIVE || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2022-12-02 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=10021853 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/revert-lend || TIER=1 || FAMILY=ACC-DONATION-UNACCOUNTED-BALANCE || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2026-01-29 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=7651407 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/renegade || TIER=1 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2026-05-10 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=114525 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/clober-liquidity-vault || TIER=1 || FAMILY=UPGRADE-INITIALIZER-REACHABLE-LIVE || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2024-12-10 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=160960 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/rigoblock || TIER=1 || FAMILY=ACC-DONATION-UNACCOUNTED-BALANCE || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2022-02-18 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=54699 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/tenderize-v2 || TIER=1 || FAMILY=ACC-DONATION-UNACCOUNTED-BALANCE || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2025-04-07 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=368517 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/crosscurve || TIER=1 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2026-02-01 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=56152 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=BRIDGE|EVM
TARGET=https://defillama.com/protocol/kiloex || TIER=1 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2025-04-14 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=1576426 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/leetswap || TIER=1 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2023-08-01 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=168493 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/woofi-swap || TIER=1 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2024-03-05 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=2388568 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/dao-swap || TIER=1 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2022-09-05 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=51629 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/kaoyaswap || TIER=1 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2022-08-24 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=1527587 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/defiplaza || TIER=1 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2024-07-05 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=161333 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/solido-cash || TIER=1 || FAMILY=ORACLE-STALE-OR-SILENT-FALLBACK || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2026-07-23 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=505159 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/allbridge-core || TIER=1 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2026-07-19 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=338501 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=BRIDGE|EVM
TARGET=https://defillama.com/protocol/ambient || TIER=1 || FAMILY=CALLBACK-UNAUTHENTICATED-CALLER-USES-APPROVALS || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2026-06-07 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=2258778 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/maya-protocol || TIER=1 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2026-08-18 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=4592973 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=BRIDGE|EVM
TARGET=https://defillama.com/protocol/goose-finance || TIER=1 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2026-03-14 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=318136 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/drift-trade || TIER=1 || FAMILY=ORACLE-STALE-OR-SILENT-FALLBACK || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2026-04-01 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=642619 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=SOLANA
TARGET=https://defillama.com/protocol/bonzo-lend || TIER=1 || FAMILY=ORACLE-STALE-OR-SILENT-FALLBACK || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2026-07-11 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=4237832 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/risex || TIER=1 || FAMILY=ORACLE-STALE-OR-SILENT-FALLBACK || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2026-08-03 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=16163761 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/raydium-amm || TIER=1 || FAMILY=AUTH-MISSING-ON-VALUE-MOVING-PATH || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2026-06-10 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=1056329581 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=SOLANA
TARGET=https://defillama.com/protocol/defituna-lending || TIER=1 || FAMILY=ORACLE-STALE-OR-SILENT-FALLBACK || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2026-07-16 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=1002161 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=SOLANA
TARGET=https://defillama.com/protocol/thorchain-dex || TIER=1 || FAMILY=ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2026-05-15 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=61903895 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/scallop-lend || TIER=1 || FAMILY=ORACLE-STALE-OR-SILENT-FALLBACK || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2026-04-26 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=10913969 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=MOVE_SUI
TARGET=https://defillama.com/protocol/flashtrade || TIER=1 || FAMILY=ORACLE-STALE-OR-SILENT-FALLBACK || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2026-07-21 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=4296299 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=SOLANA
TARGET=https://defillama.com/protocol/blend-pools-v2 || TIER=1 || FAMILY=ORACLE-SPOT-THIN-LIQUIDITY || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2026-02-22 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=169206654 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=SOROBAN
TARGET=https://defillama.com/protocol/hyperdrive-hl-lending || TIER=1 || FAMILY=ORACLE-STALE-OR-SILENT-FALLBACK || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2025-09-27 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=903755 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/ribbon || TIER=1 || FAMILY=AUTH-MISSING-ON-VALUE-MOVING-PATH || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2025-12-12 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=4174198 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM|SOLANA
TARGET=https://defillama.com/protocol/cozy-v2 || TIER=1 || FAMILY=AUTH-MISSING-ON-VALUE-MOVING-PATH || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2025-08-30 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=172357 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/sturdy-v1 || TIER=1 || FAMILY=ORACLE-STALE-OR-SILENT-FALLBACK || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2023-06-12 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=76697 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/gmx-v1-perps || TIER=1 || FAMILY=ORACLE-STALE-OR-SILENT-FALLBACK || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2025-07-09 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=3173782 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/paraspace-lending-v1 || TIER=1 || FAMILY=ORACLE-STALE-OR-SILENT-FALLBACK || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2023-03-17 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=235355 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/save || TIER=1 || FAMILY=ORACLE-STALE-OR-SILENT-FALLBACK || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2022-11-02 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=82040454 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM|SOLANA
TARGET=https://defillama.com/protocol/tropykus-rsk || TIER=1 || FAMILY=ORACLE-STALE-OR-SILENT-FALLBACK || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2023-06-14 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=116449 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/sonne-finance || TIER=1 || FAMILY=ORACLE-STALE-OR-SILENT-FALLBACK || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2024-05-15 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=55616 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/tectonic || TIER=1 || FAMILY=ORACLE-STALE-OR-SILENT-FALLBACK || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2024-11-18 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=121668693 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/starlay-finance || TIER=1 || FAMILY=ORACLE-STALE-OR-SILENT-FALLBACK || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2024-02-08 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=139207 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/moola-market || TIER=1 || FAMILY=ORACLE-STALE-OR-SILENT-FALLBACK || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2022-10-18 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=990994 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/tender-finance || TIER=1 || FAMILY=ORACLE-STALE-OR-SILENT-FALLBACK || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2023-03-07 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=241673 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/omm || TIER=1 || FAMILY=ORACLE-STALE-OR-SILENT-FALLBACK || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2023-01-21 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=150414 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/pando-rings || TIER=1 || FAMILY=ORACLE-STALE-OR-SILENT-FALLBACK || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2022-11-06 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=6075748 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/juice-finance || TIER=1 || FAMILY=ORACLE-STALE-OR-SILENT-FALLBACK || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2024-03-09 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=159272 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/amun || TIER=1 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2022-12-26 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=379345 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM|SOLANA
TARGET=https://defillama.com/protocol/kinto-bridge || TIER=1 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2025-07-10 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=672216 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=BRIDGE|EVM
TARGET=https://defillama.com/protocol/poly-network || TIER=1 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2023-07-02 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=44728247 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=BRIDGE|EVM
TARGET=https://defillama.com/protocol/basketdao || TIER=1 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2024-01-17 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=112721 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/reaper-farm || TIER=1 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2022-08-01 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=1374988 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/alex || TIER=1 || FAMILY=AUTH-MISSING-ON-VALUE-MOVING-PATH || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2025-06-06 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=700135 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/1inch-swap || TIER=1 || FAMILY=ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2025-03-07 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=3145949 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/terraport || TIER=1 || FAMILY=AUTH-MISSING-ON-VALUE-MOVING-PATH || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2023-04-10 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=113857 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/tinyman || TIER=1 || FAMILY=ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2022-01-01 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=5654837 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/four.meme || TIER=1 || FAMILY=ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2025-03-18 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=4487963 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/chainge-finance || TIER=1 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2024-04-15 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=13028029 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/superfluid || TIER=1 || FAMILY=AUTH-MISSING-ON-VALUE-MOVING-PATH || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2022-02-08 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=6272981 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/cetus-clmm || TIER=1 || FAMILY=AUTH-MISSING-ON-VALUE-MOVING-PATH || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2025-05-22 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=24733471 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=MOVE_SUI
TARGET=https://defillama.com/protocol/thalaswap || TIER=1 || FAMILY=ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2024-11-15 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=684285 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=MOVE_SUI
TARGET=https://defillama.com/protocol/equalizer-exchange || TIER=1 || FAMILY=ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2022-06-07 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=135186 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/crema-finance || TIER=1 || FAMILY=ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2022-07-02 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=127828 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=SOLANA
TARGET=https://defillama.com/protocol/arena-socialfi || TIER=1 || FAMILY=AUTH-MISSING-ON-VALUE-MOVING-PATH || DECISIVE_CHECK=Confirm in the DEPLOYED artifact whether the fix described in the 2023-10-07 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now. || VALUE_AT_RISK=145685 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/connext || TIER=2 || FAMILY=HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled static precompile set -- do not infer either from release notes. A vend || VALUE_AT_RISK=29891549 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=BRIDGE|EVM
TARGET=https://defillama.com/protocol/dxsale || TIER=2 || FAMILY=AUTH-ZERO-ADDRESS-ACCEPTED || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled static precompile set -- do not infer either from release notes. A vend || VALUE_AT_RISK=15934950 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/scrubvault || TIER=2 || FAMILY=ACC-DONATION-UNACCOUNTED-BALANCE || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled static precompile set -- do not infer either from release notes. A vend || VALUE_AT_RISK=138958 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=COSMOS_APPCHAIN|EVM
```

## Candidates

### 1. Atomic Green — Tier 1 — URGENCY 72.0

- **Protocol:** `atomic-green` · Derivatives · Arbitrum
- **DefiLlama:** https://defillama.com/protocol/atomic-green
- **Value at risk (beside the score, not in it):** $84,487 · band `IN_BAND`
- **Matched family:** `UPGRADE-INITIALIZER-REACHABLE-LIVE`
    - broken invariant: After deployment, no caller may (re)establish ownership, admin, or implementation wiring. Initialization state must be provably consumed.
- **URGENCY 72.0 / EVIDENCE_CONFIDENCE 69.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 15.0/20 · reachable live value 20.0/25 · precondition match 9.0/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2026-08-08 for $29,984 [Signature Replay], and still holds $84,487
    - reachability: 3 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 19d ago; 2 siblings
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2026-08-08 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2026-08-08 $29,984 [Signature Replay]
- **What would falsify it:** Simulated re-initialization reverts (kills the pair); Contract is non-upgradeable and holds no approvals
- **Disclosure channel, if public:** https://atomic.green
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 2. Lien — Tier 1 — URGENCY 69.0

- **Protocol:** `lien` · Options · Ethereum
- **DefiLlama:** https://defillama.com/protocol/lien
- **Value at risk (beside the score, not in it):** $204,912 · band `IN_BAND`
- **Matched family:** `UPGRADE-INITIALIZER-REACHABLE-LIVE`
    - broken invariant: After deployment, no caller may (re)establish ownership, admin, or implementation wiring. Initialization state must be provably consumed.
- **URGENCY 69.0 / EVIDENCE_CONFIDENCE 69.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 12.0/20 · reachable live value 20.0/25 · precondition match 9.0/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2026-07-23 for $542,000 [Missing Input Validation], and still holds $204,912
    - reachability: 3 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 35d ago; 2 siblings
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2026-07-23 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2026-07-23 $542,000 [Missing Input Validation]
- **What would falsify it:** Simulated re-initialization reverts (kills the pair); Contract is non-upgradeable and holds no approvals
- **Disclosure channel, if public:** https://lien.finance/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 3. Sentiment — Tier 1 — URGENCY 68.07

- **Protocol:** `sentiment` · Lending · Hyperliquid L1, Arbitrum
- **DefiLlama:** https://defillama.com/protocol/sentiment
- **Value at risk (beside the score, not in it):** $517,964 · band `IN_BAND`
- **Matched family:** `SIG-VERIFIER-DEFEATABLE`
    - broken invariant: A verification routine must reject malformed, empty or zero-recovered signatures, and must never treat address(0) as a match.
- **URGENCY 68.07 / EVIDENCE_CONFIDENCE 90.4** — evidence level `L4_GUARD_REVIEW`
    - remediation gap 28/40 · technique recency+propagation 4.0/20 · reachable live value 25.0/25 · precondition match 11.07/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2023-04-04 for $1,000,000 [Reentrancy], and still holds $517,964
    - reachability: 3 precondition(s) present at L4_GUARD_REVIEW, no guard found in the reviewed path
    - recency: technique public 1241d ago; 2 siblings
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2023-04-04 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2023-04-04 $1,000,000 [Reentrancy]
- **What would falsify it:** OZ ECDSA library in the deployed bytecode (kills the ecrecover-zero shape); Signer address immutable and non-zero
- **Disclosure channel, if public:** https://app.sentiment.xyz
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 4. Gamma — Tier 1 — URGENCY 66.57

- **Protocol:** `gamma` · Liquidity Manager · Ethereum, Binance, Polygon, Arbitrum, xDai
- **DefiLlama:** https://defillama.com/protocol/gamma
- **Value at risk (beside the score, not in it):** $3,105,706 · band `IN_BAND`
- **Matched family:** `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`
    - broken invariant: A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
- **URGENCY 66.57 / EVIDENCE_CONFIDENCE 90.4** — evidence level `L4_GUARD_REVIEW`
    - remediation gap 28/40 · technique recency+propagation 4.0/20 · reachable live value 25.0/25 · precondition match 9.57/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2024-01-04 for $4,500,000 [Spot Price Manipulation], and still holds $3,105,706
    - reachability: 3 precondition(s) present at L4_GUARD_REVIEW, no guard found in the reviewed path
    - recency: technique public 966d ago; 2 siblings
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2024-01-04 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2024-01-04 $4,500,000 [Spot Price Manipulation]
- **What would falsify it:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Disclosure channel, if public:** https://www.gamma.xyz
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 5. Float Protocol — Tier 1 — URGENCY 66.57

- **Protocol:** `float-protocol` · Yield · Ethereum
- **DefiLlama:** https://defillama.com/protocol/float-protocol
- **Value at risk (beside the score, not in it):** $216,419 · band `IN_BAND`
- **Matched family:** `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`
    - broken invariant: A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
- **URGENCY 66.57 / EVIDENCE_CONFIDENCE 90.4** — evidence level `L4_GUARD_REVIEW`
    - remediation gap 28/40 · technique recency+propagation 4.0/20 · reachable live value 25.0/25 · precondition match 9.57/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2022-01-15 for $1,160,000 [Spot Price Manipulation], and still holds $216,419
    - reachability: 3 precondition(s) present at L4_GUARD_REVIEW, no guard found in the reviewed path
    - recency: technique public 1685d ago; 2 siblings
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2022-01-15 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2022-01-15 $1,160,000 [Spot Price Manipulation]
- **What would falsify it:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 6. Arrakis V1 — Tier 1 — URGENCY 66.0

- **Protocol:** `arrakis-v1` · Liquidity Manager · Ethereum, Optimism, Polygon
- **DefiLlama:** https://defillama.com/protocol/arrakis-v1
- **Value at risk (beside the score, not in it):** $1,494,413 · band `IN_BAND`
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 66.0 / EVIDENCE_CONFIDENCE 77.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 12.0/25 · precondition match 9.0/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2026-08-23 for $7,100 [Spot Price Manipulation], and still holds $1,494,413
    - reachability: 2 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 4d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2026-08-23 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2026-08-23 $7,100 [Spot Price Manipulation]
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://arrakis.finance/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 7. Goldfinch — Tier 1 — URGENCY 65.57

- **Protocol:** `goldfinch` · RWA Lending · Ethereum
- **DefiLlama:** https://defillama.com/protocol/goldfinch
- **Value at risk (beside the score, not in it):** $1,645,216 · band `IN_BAND`
- **Matched family:** `AUTH-ZERO-ADDRESS-ACCEPTED`
    - broken invariant: Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
- **URGENCY 65.57 / EVIDENCE_CONFIDENCE 85.4** — evidence level `L4_GUARD_REVIEW`
    - remediation gap 28/40 · technique recency+propagation 3.0/20 · reachable live value 25.0/25 · precondition match 9.57/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2025-12-02 for $330,000 [Token Approval Abuse], and still holds $1,645,216
    - reachability: 3 precondition(s) present at L4_GUARD_REVIEW, no guard found in the reviewed path
    - recency: technique public 268d ago; no population established
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2025-12-02 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2025-12-02 $330,000 [Token Approval Abuse]
- **What would falsify it:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Disclosure channel, if public:** https://goldfinch.finance
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 8. Overnight Finance — Tier 1 — URGENCY 61.0

- **Protocol:** `overnight-finance` · CDP · Blast, Base, Arbitrum, Linea, Optimism
- **DefiLlama:** https://defillama.com/protocol/overnight-finance
- **Value at risk (beside the score, not in it):** $10,021,853 · band `IN_BAND`
- **Matched family:** `UPGRADE-INITIALIZER-REACHABLE-LIVE`
    - broken invariant: After deployment, no caller may (re)establish ownership, admin, or implementation wiring. Initialization state must be provably consumed.
- **URGENCY 61.0 / EVIDENCE_CONFIDENCE 69.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 4.0/20 · reachable live value 20.0/25 · precondition match 9.0/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2022-12-02 for $0 [Unknown], and still holds $10,021,853
    - reachability: 3 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 1364d ago; 2 siblings
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2022-12-02 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2022-12-02 $0 [Unknown]
- **What would falsify it:** Simulated re-initialization reverts (kills the pair); Contract is non-upgradeable and holds no approvals
- **Disclosure channel, if public:** https://overnight.fi
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 9. Revert Lend — Tier 1 — URGENCY 60.38

- **Protocol:** `revert-lend` · Lending · Arbitrum, Base, Ethereum
- **DefiLlama:** https://defillama.com/protocol/revert-lend
- **Value at risk (beside the score, not in it):** $7,651,408 · band `IN_BAND`
- **Matched family:** `ACC-DONATION-UNACCOUNTED-BALANCE`
    - broken invariant: A share price, exchange rate or totalAssets must be a function of value the protocol accounted for on entry. Reading a raw balance makes any direct transfer into the accounting boundary an unpriced increase in every holder's claim.
- **URGENCY 60.38 / EVIDENCE_CONFIDENCE 69.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 20.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2026-01-29 for $50,000 [Staking Logic Flaw], and still holds $7,651,408
    - reachability: 2 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 210d ago; 3 siblings
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2026-01-29 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2026-01-29 $50,000 [Staking Logic Flaw]
- **What would falsify it:** totalAssets derived from an internal counter, not balanceOf (kills the pair); Rate is monotonic and rate-limited per block; Inbound transfers to the accounting boundary are rejected or swept to a reserve
- **Disclosure channel, if public:** https://revert.finance/#/ref/w6vno3
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 10. Renegade — Tier 1 — URGENCY 60.0

- **Protocol:** `renegade` · Dexs · Base, Arbitrum
- **DefiLlama:** https://defillama.com/protocol/renegade
- **Value at risk (beside the score, not in it):** $114,526 · band `IN_BAND`
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 60.0 / EVIDENCE_CONFIDENCE 77.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 11.0/20 · reachable live value 12.0/25 · precondition match 9.0/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2026-05-10 for $209,000 [Uninitialized Proxy], and still holds $114,526
    - reachability: 3 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 109d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2026-05-10 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2026-05-10 $209,000 [Uninitialized Proxy]
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 11. Clober Liquidity Vault — Tier 1 — URGENCY 59.88

- **Protocol:** `clober-liquidity-vault` · Dexs · Base, Monad
- **DefiLlama:** https://defillama.com/protocol/clober-liquidity-vault
- **Value at risk (beside the score, not in it):** $160,960 · band `IN_BAND`
- **Matched family:** `UPGRADE-INITIALIZER-REACHABLE-LIVE`
    - broken invariant: After deployment, no caller may (re)establish ownership, admin, or implementation wiring. Initialization state must be provably consumed.
- **URGENCY 59.88 / EVIDENCE_CONFIDENCE 69.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 4.0/20 · reachable live value 20.0/25 · precondition match 7.88/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2024-12-10 for $500,000 [Reentrancy], and still holds $160,960
    - reachability: 2 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 625d ago; 2 siblings
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2024-12-10 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2024-12-10 $500,000 [Reentrancy]
- **What would falsify it:** Simulated re-initialization reverts (kills the pair); Contract is non-upgradeable and holds no approvals
- **Disclosure channel, if public:** https://app.clober.io/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 12. Rigoblock — Tier 1 — URGENCY 58.38

- **Protocol:** `rigoblock` · Onchain Capital Allocator · Arbitrum, Ethereum, Optimism, Base, Unichain
- **DefiLlama:** https://defillama.com/protocol/rigoblock
- **Value at risk (beside the score, not in it):** $54,699 · band `IN_BAND`
- **Matched family:** `ACC-DONATION-UNACCOUNTED-BALANCE`
    - broken invariant: A share price, exchange rate or totalAssets must be a function of value the protocol accounted for on entry. Reading a raw balance makes any direct transfer into the accounting boundary an unpriced increase in every holder's claim.
- **URGENCY 58.38 / EVIDENCE_CONFIDENCE 69.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 4.0/20 · reachable live value 20.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2022-02-18 for $464,000 [Improper Access Control], and still holds $54,699
    - reachability: 2 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 1651d ago; 3 siblings
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2022-02-18 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2022-02-18 $464,000 [Improper Access Control]
- **What would falsify it:** totalAssets derived from an internal counter, not balanceOf (kills the pair); Rate is monotonic and rate-limited per block; Inbound transfers to the accounting boundary are rejected or swept to a reserve
- **Disclosure channel, if public:** https://rigoblock.com
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 13. Tenderize V2 — Tier 1 — URGENCY 58.38

- **Protocol:** `tenderize-v2` · Liquid Staking · Ethereum, Arbitrum
- **DefiLlama:** https://defillama.com/protocol/tenderize-v2
- **Value at risk (beside the score, not in it):** $368,518 · band `IN_BAND`
- **Matched family:** `ACC-DONATION-UNACCOUNTED-BALANCE`
    - broken invariant: A share price, exchange rate or totalAssets must be a function of value the protocol accounted for on entry. Reading a raw balance makes any direct transfer into the accounting boundary an unpriced increase in every holder's claim.
- **URGENCY 58.38 / EVIDENCE_CONFIDENCE 69.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 4.0/20 · reachable live value 20.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2025-04-07 for $10,850 [Unknown], and still holds $368,518
    - reachability: 2 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 507d ago; 3 siblings
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2025-04-07 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2025-04-07 $10,850 [Unknown]
- **What would falsify it:** totalAssets derived from an internal counter, not balanceOf (kills the pair); Rate is monotonic and rate-limited per block; Inbound transfers to the accounting boundary are rejected or swept to a reserve
- **Disclosure channel, if public:** https://tenderize.me
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 14. CrossCurve — Tier 1 — URGENCY 57.0

- **Protocol:** `crosscurve` · Cross Chain Bridge · Blast, Taiko, xDai, Binance, Base
- **DefiLlama:** https://defillama.com/protocol/crosscurve
- **Value at risk (beside the score, not in it):** $56,153 · band `IN_BAND`
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 57.0 / EVIDENCE_CONFIDENCE 77.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 8.0/20 · reachable live value 12.0/25 · precondition match 9.0/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2026-02-01 for $3,000,000 [Cross-Chain Message Spoofing], and still holds $56,153
    - reachability: 2 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 207d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2026-02-01 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2026-02-01 $3,000,000 [Cross-Chain Message Spoofing]
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://crosscurve.fi
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 15. KiloEx — Tier 1 — URGENCY 55.0

- **Protocol:** `kiloex` · Derivatives · Binance, Op_Bnb, Base, Manta, BSquared
- **DefiLlama:** https://defillama.com/protocol/kiloex
- **Value at risk (beside the score, not in it):** $1,576,427 · band `IN_BAND`
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 55.0 / EVIDENCE_CONFIDENCE 77.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 12.0/25 · precondition match 9.0/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2025-04-14 for $7,500,000 [Spot Price Manipulation], and still holds $1,576,427
    - reachability: 2 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 500d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2025-04-14 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2025-04-14 $7,500,000 [Spot Price Manipulation]
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://app.kiloex.io/#/trade
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 16. LeetSwap — Tier 1 — URGENCY 55.0

- **Protocol:** `leetswap` · Dexs · Base, Op_Bnb, Manta, Linea, Shibarium
- **DefiLlama:** https://defillama.com/protocol/leetswap
- **Value at risk (beside the score, not in it):** $168,494 · band `IN_BAND`
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 55.0 / EVIDENCE_CONFIDENCE 77.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 12.0/25 · precondition match 9.0/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2023-08-01 for $620,000 [Improper Access Control], and still holds $168,494
    - reachability: 3 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 1122d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2023-08-01 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2023-08-01 $620,000 [Improper Access Control]
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 17. WOOFi Swap — Tier 1 — URGENCY 55.0

- **Protocol:** `woofi-swap` · Dexs · Arbitrum, Optimism, Avalanche, Polygon, Base
- **DefiLlama:** https://defillama.com/protocol/woofi-swap
- **Value at risk (beside the score, not in it):** $2,388,568 · band `IN_BAND`
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 55.0 / EVIDENCE_CONFIDENCE 77.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 12.0/25 · precondition match 9.0/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2024-03-05 for $8,750,000 [Spot Price Manipulation], and still holds $2,388,568
    - reachability: 2 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 905d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2024-03-05 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2024-03-05 $8,750,000 [Spot Price Manipulation]
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://woofi.com
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 18. DAO Swap — Tier 1 — URGENCY 55.0

- **Protocol:** `dao-swap` · Dexs · Binance
- **DefiLlama:** https://defillama.com/protocol/dao-swap
- **Value at risk (beside the score, not in it):** $51,630 · band `IN_BAND`
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 55.0 / EVIDENCE_CONFIDENCE 77.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 12.0/25 · precondition match 9.0/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2022-09-05 for $580,000 [Improper Access Control], and still holds $51,630
    - reachability: 3 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 1452d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2022-09-05 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2022-09-05 $580,000 [Improper Access Control]
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 19. KaoyaSwap — Tier 1 — URGENCY 55.0

- **Protocol:** `kaoyaswap` · Dexs · Binance
- **DefiLlama:** https://defillama.com/protocol/kaoyaswap
- **Value at risk (beside the score, not in it):** $1,527,588 · band `IN_BAND`
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 55.0 / EVIDENCE_CONFIDENCE 77.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 12.0/25 · precondition match 9.0/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2022-08-24 for $118,000 [Swap Logic Flaw], and still holds $1,527,588
    - reachability: 3 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 1464d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2022-08-24 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2022-08-24 $118,000 [Swap Logic Flaw]
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 20. DefiPlaza — Tier 1 — URGENCY 55.0

- **Protocol:** `defiplaza` · Dexs · Radix, Ethereum
- **DefiLlama:** https://defillama.com/protocol/defiplaza
- **Value at risk (beside the score, not in it):** $161,334 · band `IN_BAND`
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 55.0 / EVIDENCE_CONFIDENCE 71.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 12.0/25 · precondition match 9.0/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2024-07-05 for $200,000 [Swap Logic Flaw], and still holds $161,334
    - reachability: 2 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 783d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2024-07-05 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2024-07-05 $200,000 [Swap Logic Flaw]
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://defiplaza.net/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 21. Solido Cash — Tier 1 — URGENCY 45

- **Protocol:** `solido-cash` · CDP · Supra
- **DefiLlama:** https://defillama.com/protocol/solido-cash
- **Value at risk (beside the score, not in it):** $505,160 · band `IN_BAND`
- **Matched family:** `ORACLE-STALE-OR-SILENT-FALLBACK`
    - broken invariant: A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 14.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2026-07-23 for $900,000 [Oracle Misconfiguration], and still holds $505,160
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 35d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2026-07-23 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2026-07-23 $900,000 [Oracle Misconfiguration]
- **What would falsify it:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Disclosure channel, if public:** https://solido.money/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 22. Allbridge Core — Tier 1 — URGENCY 45

- **Protocol:** `allbridge-core` · Bridge · Celo, Base, Polygon, Arbitrum, Ethereum
- **DefiLlama:** https://defillama.com/protocol/allbridge-core
- **Value at risk (beside the score, not in it):** $338,501 · band `IN_BAND`
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 14.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - this protocol has 2 recorded public incident(s), most recently 2026-07-19 for $1,650,000 [Withdrawal Logic Flaw], and still holds $338,501
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 39d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2026-07-19 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2026-07-19 $1,650,000 [Withdrawal Logic Flaw]; 2023-04-02 $573,000 [Swap Logic Flaw]
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://core.allbridge.io
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 23. Ambient — Tier 1 — URGENCY 45

- **Protocol:** `ambient` · Dexs · Scroll, Blast, Ethereum, Plume Mainnet, Canto
- **DefiLlama:** https://defillama.com/protocol/ambient
- **Value at risk (beside the score, not in it):** $2,258,778 · band `IN_BAND`
- **Matched family:** `CALLBACK-UNAUTHENTICATED-CALLER-USES-APPROVALS`
    - broken invariant: When a contract pulls funds during a callback, the payer must be proven to be the initiator of the current flow, and the callback's caller must be proven to be the expected counterparty contract. Neither may be taken from caller-supplied payload.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 12.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2026-06-07 for $110,600 [Deposit Logic Flaw], and still holds $2,258,778
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 81d ago; 3 siblings
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2026-06-07 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2026-06-07 $110,600 [Deposit Logic Flaw]
- **What would falsify it:** Callback asserts both caller identity and payer == initiator (kills the pair); Contract never holds third-party approvals; Payment always uses msg.sender as source
- **Disclosure channel, if public:** https://ambient.finance/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 24. Maya Protocol — Tier 1 — URGENCY 45

- **Protocol:** `maya-protocol` · Cross Chain Bridge · Zcash, Bitcoin, Ethereum, Thorchain, Arbitrum
- **DefiLlama:** https://defillama.com/protocol/maya-protocol
- **Value at risk (beside the score, not in it):** $4,592,974 · band `IN_BAND`
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2026-08-18 for $1,700,000 [Withdrawal Logic Flaw], and still holds $4,592,974
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 9d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2026-08-18 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2026-08-18 $1,700,000 [Withdrawal Logic Flaw]
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://www.mayaprotocol.com
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 25. Goose Finance — Tier 1 — URGENCY 45

- **Protocol:** `goose-finance` · Farm · Binance
- **DefiLlama:** https://defillama.com/protocol/goose-finance
- **Value at risk (beside the score, not in it):** $318,137 · band `IN_BAND`
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 11.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2026-03-14 for $8,435 [Incorrect Share Accounting], and still holds $318,137
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 166d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2026-03-14 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2026-03-14 $8,435 [Incorrect Share Accounting]
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 26. Drift Trade — Tier 1 — URGENCY 45

- **Protocol:** `drift-trade` · Derivatives · Solana
- **DefiLlama:** https://defillama.com/protocol/drift-trade
- **Value at risk (beside the score, not in it):** $642,620 · band `IN_BAND`
- **Matched family:** `ORACLE-STALE-OR-SILENT-FALLBACK`
    - broken invariant: A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 11.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - this protocol has 2 recorded public incident(s), most recently 2026-04-01 for $295,000,000 [Proxy Upgrade Hijack], and still holds $642,620
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 148d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2026-04-01 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2026-04-01 $295,000,000 [Proxy Upgrade Hijack]; 2022-05-11 $14,500,000 [Risk Parameter Abuse]
- **What would falsify it:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Disclosure channel, if public:** https://app.drift.trade
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 27. Bonzo Lend — Tier 1 — URGENCY 45

- **Protocol:** `bonzo-lend` · Lending · Hedera
- **DefiLlama:** https://defillama.com/protocol/bonzo-lend
- **Value at risk (beside the score, not in it):** $4,237,832 · band `IN_BAND`
- **Matched family:** `ORACLE-STALE-OR-SILENT-FALLBACK`
    - broken invariant: A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 14.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2026-07-11 for $9,050,000 [Spot Price Manipulation], and still holds $4,237,832
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 47d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2026-07-11 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2026-07-11 $9,050,000 [Spot Price Manipulation]
- **What would falsify it:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Disclosure channel, if public:** https://bonzo.finance/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 28. RISEx — Tier 1 — URGENCY 45

- **Protocol:** `risex` · Derivatives · RISE
- **DefiLlama:** https://defillama.com/protocol/risex
- **Value at risk (beside the score, not in it):** $16,163,762 · band `IN_BAND`
- **Matched family:** `ORACLE-STALE-OR-SILENT-FALLBACK`
    - broken invariant: A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2026-08-03 for $673,012 [Improper Access Control], and still holds $16,163,762
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 24d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2026-08-03 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2026-08-03 $673,012 [Improper Access Control]
- **What would falsify it:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Disclosure channel, if public:** https://www.rise.trade/en
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 29. Raydium AMM — Tier 1 — URGENCY 45

- **Protocol:** `raydium-amm` · Dexs · Solana
- **DefiLlama:** https://defillama.com/protocol/raydium-amm
- **Value at risk (beside the score, not in it):** $1,056,329,582 · band `ABOVE_BAND_KEPT_EXPLICIT_DANGER`
- **Matched family:** `AUTH-MISSING-ON-VALUE-MOVING-PATH`
    - broken invariant: Every function that moves value or rebinds a privileged address must require a role the caller cannot obtain.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 14.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2026-06-10 for $1,340,000 [Infinite Mint], and still holds $1,056,329,582
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 78d ago; 4-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2026-06-10 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2026-06-10 $1,340,000 [Infinite Mint]
- **What would falsify it:** Every value-moving selector reverts for an unprivileged caller in simulation (kills the pair); Contract holds no value and controls no role
- **Disclosure channel, if public:** https://raydium.io
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 30. DefiTuna Lending — Tier 1 — URGENCY 45

- **Protocol:** `defituna-lending` · Lending · Solana
- **DefiLlama:** https://defillama.com/protocol/defituna-lending
- **Value at risk (beside the score, not in it):** $1,002,162 · band `IN_BAND`
- **Matched family:** `ORACLE-STALE-OR-SILENT-FALLBACK`
    - broken invariant: A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 14.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2026-07-16 for $580,000 [Swap Logic Flaw], and still holds $1,002,162
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 42d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2026-07-16 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2026-07-16 $580,000 [Swap Logic Flaw]
- **What would falsify it:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Disclosure channel, if public:** https://defituna.com
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 31. THORChain DEX — Tier 1 — URGENCY 45

- **Protocol:** `thorchain-dex` · Dexs · Thorchain, Bitcoin, Ethereum, Binance, Bitcoincash
- **DefiLlama:** https://defillama.com/protocol/thorchain-dex
- **Value at risk (beside the score, not in it):** $61,903,896 · band `ABOVE_BAND_KEPT_EXPLICIT_DANGER`
- **Matched family:** `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`
    - broken invariant: Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 11.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2026-05-15 for $10,700,000 [Bridge Logic Flaw], and still holds $61,903,896
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 104d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2026-05-15 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2026-05-15 $10,700,000 [Bridge Logic Flaw]
- **What would falsify it:** Every identifier derived or verified against the factory/registry (kills the pair); Routing restricted to an immutable venue allowlist
- **Disclosure channel, if public:** https://thorchain.org/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 32. Scallop Lend — Tier 1 — URGENCY 45

- **Protocol:** `scallop-lend` · Lending · Sui
- **DefiLlama:** https://defillama.com/protocol/scallop-lend
- **Value at risk (beside the score, not in it):** $10,913,969 · band `IN_BAND`
- **Matched family:** `ORACLE-STALE-OR-SILENT-FALLBACK`
    - broken invariant: A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 11.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2026-04-26 for $142,000 [Reward Logic Flaw], and still holds $10,913,969
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 123d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2026-04-26 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2026-04-26 $142,000 [Reward Logic Flaw]
- **What would falsify it:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Disclosure channel, if public:** https://app.scallop.io
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 33. FlashTrade — Tier 1 — URGENCY 45

- **Protocol:** `flashtrade` · Derivatives · Solana
- **DefiLlama:** https://defillama.com/protocol/flashtrade
- **Value at risk (beside the score, not in it):** $4,296,300 · band `IN_BAND`
- **Matched family:** `ORACLE-STALE-OR-SILENT-FALLBACK`
    - broken invariant: A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 14.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2026-07-21 for $98,000 [Missing Input Validation], and still holds $4,296,300
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 37d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2026-07-21 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2026-07-21 $98,000 [Missing Input Validation]
- **What would falsify it:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Disclosure channel, if public:** https://www.flash.trade
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 34. Blend Pools V2 — Tier 1 — URGENCY 42.75

- **Protocol:** `blend-pools-v2` · Lending · Stellar
- **DefiLlama:** https://defillama.com/protocol/blend-pools-v2
- **Value at risk (beside the score, not in it):** $169,206,655 · band `ABOVE_BAND_KEPT_EXPLICIT_DANGER`
- **Matched family:** `ORACLE-SPOT-THIN-LIQUIDITY`
    - broken invariant: Borrowing capacity, mint size, reward size or collateral value must not be derived from a price that a single actor can move within the manipulation window, and the value unlocked must never exceed the cost of moving that price.
- **URGENCY 42.75 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 8.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2026-02-22 for $10,970,000 [Spot Price Manipulation], and still holds $169,206,655
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 186d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2026-02-22 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2026-02-22 $10,970,000 [Spot Price Manipulation]
- **What would falsify it:** All collateral priced by a deep aggregated feed with a deviation cap (kills the pair); Caps are set from measured venue depth and enforced on-chain; The action is sized from realised transfer amounts, so price is never an input
- **Disclosure channel, if public:** https://www.blend.capital
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 35. Hyperdrive HL Lending — Tier 1 — URGENCY 42.75

- **Protocol:** `hyperdrive-hl-lending` · Lending · Hyperliquid L1
- **DefiLlama:** https://defillama.com/protocol/hyperdrive-hl-lending
- **Value at risk (beside the score, not in it):** $903,755 · band `IN_BAND`
- **Matched family:** `ORACLE-STALE-OR-SILENT-FALLBACK`
    - broken invariant: A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
- **URGENCY 42.75 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 8.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2025-09-27 for $782,000 [Arbitrary External Call], and still holds $903,755
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 334d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2025-09-27 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2025-09-27 $782,000 [Arbitrary External Call]
- **What would falsify it:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Disclosure channel, if public:** https://hyperdrive.fi/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 36. Ribbon — Tier 1 — URGENCY 42.38

- **Protocol:** `ribbon` · Options Vault · Ethereum, Solana, Avalanche, Binance
- **DefiLlama:** https://defillama.com/protocol/ribbon
- **Value at risk (beside the score, not in it):** $4,174,199 · band `IN_BAND`
- **Matched family:** `AUTH-MISSING-ON-VALUE-MOVING-PATH`
    - broken invariant: Every function that moves value or rebinds a privileged address must require a role the caller cannot obtain.
- **URGENCY 42.38 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 8.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2025-12-12 for $2,700,000 [Improper Access Control], and still holds $4,174,199
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 258d ago; 4-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2025-12-12 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2025-12-12 $2,700,000 [Improper Access Control]
- **What would falsify it:** Every value-moving selector reverts for an unprivileged caller in simulation (kills the pair); Contract holds no value and controls no role
- **Disclosure channel, if public:** https://www.ribbon.finance/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 37. Cozy V2 — Tier 1 — URGENCY 42.38

- **Protocol:** `cozy-v2` · Insurance · Optimism
- **DefiLlama:** https://defillama.com/protocol/cozy-v2
- **Value at risk (beside the score, not in it):** $172,358 · band `IN_BAND`
- **Matched family:** `AUTH-MISSING-ON-VALUE-MOVING-PATH`
    - broken invariant: Every function that moves value or rebinds a privileged address must require a role the caller cannot obtain.
- **URGENCY 42.38 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 8.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2025-08-30 for $427,000 [Missing Input Validation], and still holds $172,358
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 362d ago; 4-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2025-08-30 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2025-08-30 $427,000 [Missing Input Validation]
- **What would falsify it:** Every value-moving selector reverts for an unprivileged caller in simulation (kills the pair); Contract holds no value and controls no role
- **Disclosure channel, if public:** https://www.cozy.finance
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 38. Sturdy V1 — Tier 1 — URGENCY 40.75

- **Protocol:** `sturdy-v1` · Lending · Ethereum, Fantom
- **DefiLlama:** https://defillama.com/protocol/sturdy-v1
- **Value at risk (beside the score, not in it):** $76,697 · band `IN_BAND`
- **Matched family:** `ORACLE-STALE-OR-SILENT-FALLBACK`
    - broken invariant: A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
- **URGENCY 40.75 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2023-06-12 for $775,000 [Read-Only Reentrancy], and still holds $76,697
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 1172d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2023-06-12 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2023-06-12 $775,000 [Read-Only Reentrancy]
- **What would falsify it:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Disclosure channel, if public:** https://app.sturdy.finance
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 39. GMX V1 Perps — Tier 1 — URGENCY 40.75

- **Protocol:** `gmx-v1-perps` · Derivatives · Avalanche, Arbitrum
- **DefiLlama:** https://defillama.com/protocol/gmx-v1-perps
- **Value at risk (beside the score, not in it):** $3,173,783 · band `IN_BAND`
- **Matched family:** `ORACLE-STALE-OR-SILENT-FALLBACK`
    - broken invariant: A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
- **URGENCY 40.75 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - this protocol has 2 recorded public incident(s), most recently 2025-07-09 for $42,000,000 [Reentrancy], and still holds $3,173,783
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 414d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2025-07-09 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2025-07-09 $42,000,000 [Reentrancy]; 2022-09-18 $565,000 [Stale Price Arbitrage]
- **What would falsify it:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Disclosure channel, if public:** https://gmx.io/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 40. ParaSpace Lending V1 — Tier 1 — URGENCY 40.75

- **Protocol:** `paraspace-lending-v1` · Lending · Ethereum, zkSync Era, Arbitrum, Polygon, Moonbeam
- **DefiLlama:** https://defillama.com/protocol/paraspace-lending-v1
- **Value at risk (beside the score, not in it):** $235,356 · band `IN_BAND`
- **Matched family:** `ORACLE-STALE-OR-SILENT-FALLBACK`
    - broken invariant: A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
- **URGENCY 40.75 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2023-03-17 for $5,000,000 [Spot Price Manipulation], and still holds $235,356
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 1259d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2023-03-17 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2023-03-17 $5,000,000 [Spot Price Manipulation]
- **What would falsify it:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Disclosure channel, if public:** https://parallel.fi/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 41. Save — Tier 1 — URGENCY 40.75

- **Protocol:** `save` · Lending · Solana, Eclipse
- **DefiLlama:** https://defillama.com/protocol/save
- **Value at risk (beside the score, not in it):** $82,040,455 · band `ABOVE_BAND_KEPT_EXPLICIT_DANGER`
- **Matched family:** `ORACLE-STALE-OR-SILENT-FALLBACK`
    - broken invariant: A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
- **URGENCY 40.75 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - this protocol has 2 recorded public incident(s), most recently 2022-11-02 for $1,260,000 [Spot Price Manipulation], and still holds $82,040,455
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 1394d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2022-11-02 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2022-11-02 $1,260,000 [Spot Price Manipulation]; 2022-11-01 $1,026,000 [Risk Parameter Abuse]
- **What would falsify it:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Disclosure channel, if public:** https://www.save.finance/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 42. Tropykus RSK — Tier 1 — URGENCY 40.75

- **Protocol:** `tropykus-rsk` · Lending · RSK
- **DefiLlama:** https://defillama.com/protocol/tropykus-rsk
- **Value at risk (beside the score, not in it):** $116,450 · band `IN_BAND`
- **Matched family:** `ORACLE-STALE-OR-SILENT-FALLBACK`
    - broken invariant: A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
- **URGENCY 40.75 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2023-06-14 for $150,000 [Rounding Error], and still holds $116,450
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 1170d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2023-06-14 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2023-06-14 $150,000 [Rounding Error]
- **What would falsify it:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Disclosure channel, if public:** https://app.tropykus.com
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 43. Sonne Finance — Tier 1 — URGENCY 40.75

- **Protocol:** `sonne-finance` · Lending · Base, Optimism
- **DefiLlama:** https://defillama.com/protocol/sonne-finance
- **Value at risk (beside the score, not in it):** $55,617 · band `IN_BAND`
- **Matched family:** `ORACLE-STALE-OR-SILENT-FALLBACK`
    - broken invariant: A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
- **URGENCY 40.75 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2024-05-15 for $20,000,000 [Donation Attack], and still holds $55,617
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 834d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2024-05-15 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2024-05-15 $20,000,000 [Donation Attack]
- **What would falsify it:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Disclosure channel, if public:** https://sonne.finance
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 44. Tectonic — Tier 1 — URGENCY 40.75

- **Protocol:** `tectonic` · Lending · Cronos
- **DefiLlama:** https://defillama.com/protocol/tectonic
- **Value at risk (beside the score, not in it):** $121,668,693 · band `ABOVE_BAND_KEPT_EXPLICIT_DANGER`
- **Matched family:** `ORACLE-STALE-OR-SILENT-FALLBACK`
    - broken invariant: A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
- **URGENCY 40.75 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - this protocol has 2 recorded public incident(s), most recently 2024-11-18 for $0 [Unknown], and still holds $121,668,693
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 647d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2024-11-18 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2024-11-18 $0 [Unknown]; 2024-02-22 $250,000 [Unknown]
- **What would falsify it:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Disclosure channel, if public:** https://tectonic.finance/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 45. Starlay Finance — Tier 1 — URGENCY 40.75

- **Protocol:** `starlay-finance` · Lending · Astar
- **DefiLlama:** https://defillama.com/protocol/starlay-finance
- **Value at risk (beside the score, not in it):** $139,207 · band `IN_BAND`
- **Matched family:** `ORACLE-STALE-OR-SILENT-FALLBACK`
    - broken invariant: A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
- **URGENCY 40.75 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2024-02-08 for $2,100,000 [Redeem Logic Flaw], and still holds $139,207
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 931d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2024-02-08 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2024-02-08 $2,100,000 [Redeem Logic Flaw]
- **What would falsify it:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Disclosure channel, if public:** https://starlay.finance
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 46. Moola Market — Tier 1 — URGENCY 40.75

- **Protocol:** `moola-market` · Lending · Celo
- **DefiLlama:** https://defillama.com/protocol/moola-market
- **Value at risk (beside the score, not in it):** $990,995 · band `IN_BAND`
- **Matched family:** `ORACLE-STALE-OR-SILENT-FALLBACK`
    - broken invariant: A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
- **URGENCY 40.75 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2022-10-18 for $8,400,000 [Spot Price Manipulation], and still holds $990,995
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 1409d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2022-10-18 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2022-10-18 $8,400,000 [Spot Price Manipulation]
- **What would falsify it:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Disclosure channel, if public:** https://moola.market
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 47. Tender Finance — Tier 1 — URGENCY 40.75

- **Protocol:** `tender-finance` · Lending · Arbitrum
- **DefiLlama:** https://defillama.com/protocol/tender-finance
- **Value at risk (beside the score, not in it):** $241,673 · band `IN_BAND`
- **Matched family:** `ORACLE-STALE-OR-SILENT-FALLBACK`
    - broken invariant: A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
- **URGENCY 40.75 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2023-03-07 for $1,590,000 [Stale Oracle Price], and still holds $241,673
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 1269d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2023-03-07 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2023-03-07 $1,590,000 [Stale Oracle Price]
- **What would falsify it:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 48. Omm — Tier 1 — URGENCY 40.75

- **Protocol:** `omm` · Lending · Icon
- **DefiLlama:** https://defillama.com/protocol/omm
- **Value at risk (beside the score, not in it):** $150,414 · band `IN_BAND`
- **Matched family:** `ORACLE-STALE-OR-SILENT-FALLBACK`
    - broken invariant: A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
- **URGENCY 40.75 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2023-01-21 for $1,891,000 [Redeem Logic Flaw], and still holds $150,414
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 1314d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2023-01-21 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2023-01-21 $1,891,000 [Redeem Logic Flaw]
- **What would falsify it:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 49. Pando Rings — Tier 1 — URGENCY 40.75

- **Protocol:** `pando-rings` · Lending · Mixin
- **DefiLlama:** https://defillama.com/protocol/pando-rings
- **Value at risk (beside the score, not in it):** $6,075,749 · band `IN_BAND`
- **Matched family:** `ORACLE-STALE-OR-SILENT-FALLBACK`
    - broken invariant: A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
- **URGENCY 40.75 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2022-11-06 for $22,000,000 [Spot Price Manipulation], and still holds $6,075,749
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 1390d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2022-11-06 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2022-11-06 $22,000,000 [Spot Price Manipulation]
- **What would falsify it:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Disclosure channel, if public:** https://pando.im
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 50. Juice Finance — Tier 1 — URGENCY 40.75

- **Protocol:** `juice-finance` · Leveraged Farming · Blast
- **DefiLlama:** https://defillama.com/protocol/juice-finance
- **Value at risk (beside the score, not in it):** $159,273 · band `IN_BAND`
- **Matched family:** `ORACLE-STALE-OR-SILENT-FALLBACK`
    - broken invariant: A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
- **URGENCY 40.75 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2024-03-09 for $54,000 [Reward Logic Flaw], and still holds $159,273
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 901d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2024-03-09 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2024-03-09 $54,000 [Reward Logic Flaw]
- **What would falsify it:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Disclosure channel, if public:** https://juice.finance
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 51. Amun — Tier 1 — URGENCY 40.38

- **Protocol:** `amun` · Indexes · Solana, Ethereum, Polygon
- **DefiLlama:** https://defillama.com/protocol/amun
- **Value at risk (beside the score, not in it):** $379,345 · band `IN_BAND`
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 40.38 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2022-12-26 for $300,000 [Improper Access Control], and still holds $379,345
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 1340d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2022-12-26 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2022-12-26 $300,000 [Improper Access Control]
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 52. Kinto Bridge — Tier 1 — URGENCY 40.38

- **Protocol:** `kinto-bridge` · Canonical Bridge · Ethereum
- **DefiLlama:** https://defillama.com/protocol/kinto-bridge
- **Value at risk (beside the score, not in it):** $672,217 · band `IN_BAND`
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 40.38 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2025-07-10 for $1,550,000 [Uninitialized Proxy], and still holds $672,217
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 413d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2025-07-10 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2025-07-10 $1,550,000 [Uninitialized Proxy]
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 53. Poly Network — Tier 1 — URGENCY 40.38

- **Protocol:** `poly-network` · Bridge · Ethereum, Binance, NEO, Heco, Neo3
- **DefiLlama:** https://defillama.com/protocol/poly-network
- **Value at risk (beside the score, not in it):** $44,728,248 · band `ABOVE_BAND_KEPT_EXPLICIT_DANGER`
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 40.38 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2023-07-02 for $5,000,000 [Forged Proof], and still holds $44,728,248
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 1152d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2023-07-02 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2023-07-02 $5,000,000 [Forged Proof]
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 54. BasketDAO — Tier 1 — URGENCY 40.38

- **Protocol:** `basketdao` · Indexes · Ethereum
- **DefiLlama:** https://defillama.com/protocol/basketdao
- **Value at risk (beside the score, not in it):** $112,721 · band `IN_BAND`
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 40.38 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - this protocol has 2 recorded public incident(s), most recently 2024-01-17 for $1,200,000 [Arbitrary External Call], and still holds $112,721
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 953d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2024-01-17 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2024-01-17 $1,200,000 [Arbitrary External Call]; 2022-03-30 $1,200,000 [Arbitrary External Call]
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 55. Reaper Farm — Tier 1 — URGENCY 40.38

- **Protocol:** `reaper-farm` · Yield Aggregator · Optimism, Fantom, Binance, Arbitrum
- **DefiLlama:** https://defillama.com/protocol/reaper-farm
- **Value at risk (beside the score, not in it):** $1,374,988 · band `IN_BAND`
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 40.38 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2022-08-01 for $1,700,000 [Improper Access Control], and still holds $1,374,988
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 1487d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2022-08-01 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2022-08-01 $1,700,000 [Improper Access Control]
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 56. ALEX — Tier 1 — URGENCY 40.38

- **Protocol:** `alex` · Dexs · Stacks
- **DefiLlama:** https://defillama.com/protocol/alex
- **Value at risk (beside the score, not in it):** $700,136 · band `IN_BAND`
- **Matched family:** `AUTH-MISSING-ON-VALUE-MOVING-PATH`
    - broken invariant: Every function that moves value or rebinds a privileged address must require a role the caller cannot obtain.
- **URGENCY 40.38 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2025-06-06 for $8,373,000 [Caller Impersonation], and still holds $700,136
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 447d ago; 4-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2025-06-06 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2025-06-06 $8,373,000 [Caller Impersonation]
- **What would falsify it:** Every value-moving selector reverts for an unprivileged caller in simulation (kills the pair); Contract holds no value and controls no role
- **Disclosure channel, if public:** https://alexlab.co/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 57. 1inch Swap — Tier 1 — URGENCY 40.38

- **Protocol:** `1inch-swap` · DEX Aggregator · Ethereum, Binance
- **DefiLlama:** https://defillama.com/protocol/1inch-swap
- **Value at risk (beside the score, not in it):** $3,145,949 · band `IN_BAND`
- **Matched family:** `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`
    - broken invariant: Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.
- **URGENCY 40.38 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2025-03-07 for $5,000,000 [Arbitrary External Call], and still holds $3,145,949
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 538d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2025-03-07 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2025-03-07 $5,000,000 [Arbitrary External Call]
- **What would falsify it:** Every identifier derived or verified against the factory/registry (kills the pair); Routing restricted to an immutable venue allowlist
- **Disclosure channel, if public:** https://1inch.com
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 58. Terraport — Tier 1 — URGENCY 40.38

- **Protocol:** `terraport` · Dexs · Terra
- **DefiLlama:** https://defillama.com/protocol/terraport
- **Value at risk (beside the score, not in it):** $113,858 · band `IN_BAND`
- **Matched family:** `AUTH-MISSING-ON-VALUE-MOVING-PATH`
    - broken invariant: Every function that moves value or rebinds a privileged address must require a role the caller cannot obtain.
- **URGENCY 40.38 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2023-04-10 for $4,000,000 [Improper Access Control], and still holds $113,858
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 1235d ago; 4-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2023-04-10 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2023-04-10 $4,000,000 [Improper Access Control]
- **What would falsify it:** Every value-moving selector reverts for an unprivileged caller in simulation (kills the pair); Contract holds no value and controls no role
- **Disclosure channel, if public:** https://terraport.finance/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 59. Tinyman — Tier 1 — URGENCY 40.38

- **Protocol:** `tinyman` · Dexs · Algorand
- **DefiLlama:** https://defillama.com/protocol/tinyman
- **Value at risk (beside the score, not in it):** $5,654,838 · band `IN_BAND`
- **Matched family:** `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`
    - broken invariant: Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.
- **URGENCY 40.38 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2022-01-01 for $3,000,000 [Incorrect Share Accounting], and still holds $5,654,838
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 1699d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2022-01-01 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2022-01-01 $3,000,000 [Incorrect Share Accounting]
- **What would falsify it:** Every identifier derived or verified against the factory/registry (kills the pair); Routing restricted to an immutable venue allowlist
- **Disclosure channel, if public:** https://tinyman.org
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 60. four.meme — Tier 1 — URGENCY 40.38

- **Protocol:** `four.meme` · Launchpad · Binance
- **DefiLlama:** https://defillama.com/protocol/four.meme
- **Value at risk (beside the score, not in it):** $4,487,964 · band `IN_BAND`
- **Matched family:** `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`
    - broken invariant: Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.
- **URGENCY 40.38 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - this protocol has 2 recorded public incident(s), most recently 2025-03-18 for $80,000 [Improper Access Control], and still holds $4,487,964
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 527d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2025-03-18 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2025-03-18 $80,000 [Improper Access Control]; 2025-02-11 $183,000 [Swap Logic Flaw]
- **What would falsify it:** Every identifier derived or verified against the factory/registry (kills the pair); Routing restricted to an immutable venue allowlist
- **Disclosure channel, if public:** https://four.meme
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 61. Chainge Finance — Tier 1 — URGENCY 40.38

- **Protocol:** `chainge-finance` · Dexs · Rollux, Fusion
- **DefiLlama:** https://defillama.com/protocol/chainge-finance
- **Value at risk (beside the score, not in it):** $13,028,029 · band `IN_BAND`
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 40.38 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2024-04-15 for $0 [Arbitrary External Call], and still holds $13,028,029
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 864d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2024-04-15 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2024-04-15 $0 [Arbitrary External Call]
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 62. Superfluid — Tier 1 — URGENCY 40.38

- **Protocol:** `superfluid` · Payments · Ethereum, Optimism, Base, Polygon, Celo
- **DefiLlama:** https://defillama.com/protocol/superfluid
- **Value at risk (beside the score, not in it):** $6,272,981 · band `IN_BAND`
- **Matched family:** `AUTH-MISSING-ON-VALUE-MOVING-PATH`
    - broken invariant: Every function that moves value or rebinds a privileged address must require a role the caller cannot obtain.
- **URGENCY 40.38 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2022-02-08 for $8,700,000 [Missing Input Validation], and still holds $6,272,981
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 1661d ago; 4-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2022-02-08 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2022-02-08 $8,700,000 [Missing Input Validation]
- **What would falsify it:** Every value-moving selector reverts for an unprivileged caller in simulation (kills the pair); Contract holds no value and controls no role
- **Disclosure channel, if public:** https://superfluid.org/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 63. Cetus CLMM — Tier 1 — URGENCY 40.38

- **Protocol:** `cetus-clmm` · Dexs · Sui, Aptos
- **DefiLlama:** https://defillama.com/protocol/cetus-clmm
- **Value at risk (beside the score, not in it):** $24,733,471 · band `IN_BAND`
- **Matched family:** `AUTH-MISSING-ON-VALUE-MOVING-PATH`
    - broken invariant: Every function that moves value or rebinds a privileged address must require a role the caller cannot obtain.
- **URGENCY 40.38 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2025-05-22 for $223,000,000 [Arithmetic Error], and still holds $24,733,471
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 462d ago; 4-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2025-05-22 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2025-05-22 $223,000,000 [Arithmetic Error]
- **What would falsify it:** Every value-moving selector reverts for an unprivileged caller in simulation (kills the pair); Contract holds no value and controls no role
- **Disclosure channel, if public:** https://www.cetus.zone
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 64. ThalaSwap — Tier 1 — URGENCY 40.38

- **Protocol:** `thalaswap` · Dexs · Aptos
- **DefiLlama:** https://defillama.com/protocol/thalaswap
- **Value at risk (beside the score, not in it):** $684,285 · band `IN_BAND`
- **Matched family:** `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`
    - broken invariant: Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.
- **URGENCY 40.38 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2024-11-15 for $25,500,000 [Missing Input Validation], and still holds $684,285
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 650d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2024-11-15 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2024-11-15 $25,500,000 [Missing Input Validation]
- **What would falsify it:** Every identifier derived or verified against the factory/registry (kills the pair); Routing restricted to an immutable venue allowlist
- **Disclosure channel, if public:** https://www.thala.fi/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 65. Equalizer Exchange — Tier 1 — URGENCY 40.38

- **Protocol:** `equalizer-exchange` · Dexs · Sonic, Fantom
- **DefiLlama:** https://defillama.com/protocol/equalizer-exchange
- **Value at risk (beside the score, not in it):** $135,187 · band `IN_BAND`
- **Matched family:** `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`
    - broken invariant: Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.
- **URGENCY 40.38 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2022-06-07 for $50,000 [Withdrawal Logic Flaw], and still holds $135,187
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 1542d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2022-06-07 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2022-06-07 $50,000 [Withdrawal Logic Flaw]
- **What would falsify it:** Every identifier derived or verified against the factory/registry (kills the pair); Routing restricted to an immutable venue allowlist
- **Disclosure channel, if public:** https://equalizer.exchange
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 66. Crema Finance — Tier 1 — URGENCY 40.38

- **Protocol:** `crema-finance` · Dexs · Solana
- **DefiLlama:** https://defillama.com/protocol/crema-finance
- **Value at risk (beside the score, not in it):** $127,828 · band `IN_BAND`
- **Matched family:** `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`
    - broken invariant: Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.
- **URGENCY 40.38 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2022-07-02 for $8,800,000 [Improper Access Control], and still holds $127,828
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 1517d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2022-07-02 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2022-07-02 $8,800,000 [Improper Access Control]
- **What would falsify it:** Every identifier derived or verified against the factory/registry (kills the pair); Routing restricted to an immutable venue allowlist
- **Disclosure channel, if public:** https://www.crema.finance
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 67. Arena SocialFi — Tier 1 — URGENCY 40.38

- **Protocol:** `arena-socialfi` · SoFi · Avalanche
- **DefiLlama:** https://defillama.com/protocol/arena-socialfi
- **Value at risk (beside the score, not in it):** $145,686 · band `IN_BAND`
- **Matched family:** `AUTH-MISSING-ON-VALUE-MOVING-PATH`
    - broken invariant: Every function that moves value or rebinds a privileged address must require a role the caller cannot obtain.
- **URGENCY 40.38 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - this protocol has 1 recorded public incident(s), most recently 2023-10-07 for $2,974,530 [Reentrancy], and still holds $145,686
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 1055d ago; 4-member population
- **THE decisive check (single fastest confirm/kill):** Confirm in the DEPLOYED artifact whether the fix described in the 2023-10-07 postmortem is present at the live address. Present -> drop. Absent -> Tier 1, act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
    - recorded incidents: 2023-10-07 $2,974,530 [Reentrancy]
- **What would falsify it:** Every value-moving selector reverts for an unprivileged caller in simulation (kills the pair); Contract holds no value and controls no role
- **Disclosure channel, if public:** https://arena.social/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 68. Connext — Tier 2 — URGENCY 79.57

- **Protocol:** `connext` · Bridge · Ethereum, Linea, Arbitrum, Metis, Base
- **DefiLlama:** https://defillama.com/protocol/connext
- **Value at risk (beside the score, not in it):** $29,891,550 · band `IN_BAND`
- **Matched family:** `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`
    - broken invariant: A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
- **URGENCY 79.57 / EVIDENCE_CONFIDENCE 90.4** — evidence level `L4_GUARD_REVIEW`
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 25.0/25 · precondition match 9.57/15
- **Why the clock is hot:**
    - deployed on Cronos, Evmos, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: 3 precondition(s) present at L4_GUARD_REVIEW, no guard found in the reviewed path
    - recency: technique public 65d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled static precompile set -- do not infer either from release notes. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Disclosure channel, if public:** https://connext.network/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 69. DxSale — Tier 2 — URGENCY 76.57

- **Protocol:** `dxsale` · Launchpad · Binance, Ethereum, Base, Arbitrum, Polygon
- **DefiLlama:** https://defillama.com/protocol/dxsale
- **Value at risk (beside the score, not in it):** $15,934,950 · band `IN_BAND`
- **Matched family:** `AUTH-ZERO-ADDRESS-ACCEPTED`
    - broken invariant: Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
- **URGENCY 76.57 / EVIDENCE_CONFIDENCE 79.4** — evidence level `L4_GUARD_REVIEW`
    - remediation gap 28/40 · technique recency+propagation 14.0/20 · reachable live value 25.0/25 · precondition match 9.57/15
- **Why the clock is hot:**
    - deployed on Cronos, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: 3 precondition(s) present at L4_GUARD_REVIEW, no guard found in the reviewed path
    - recency: technique public 91d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled static precompile set -- do not infer either from release notes. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Disclosure channel, if public:** https://dx.app
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 70. ScrubVault — Tier 2 — URGENCY 71.38

- **Protocol:** `scrubvault` · Basis Trading · Kava, Arbitrum
- **DefiLlama:** https://defillama.com/protocol/scrubvault
- **Value at risk (beside the score, not in it):** $138,958 · band `IN_BAND`
- **Matched family:** `ACC-DONATION-UNACCOUNTED-BALANCE`
    - broken invariant: A share price, exchange rate or totalAssets must be a function of value the protocol accounted for on entry. Reading a raw balance makes any direct transfer into the accounting boundary an unpriced increase in every holder's claim.
- **URGENCY 71.38 / EVIDENCE_CONFIDENCE 69.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 20.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - deployed on Kava, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: 2 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 52d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled static precompile set -- do not infer either from release notes. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** totalAssets derived from an internal counter, not balanceOf (kills the pair); Rate is monotonic and rate-limited per block; Inbound transfers to the accounting boundary are rejected or swept to a reserve
- **Disclosure channel, if public:** https://invest.scrub.money/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

---

## Withheld by the no-repetition ledger — but now classified Tier 1–2

These **104** protocols were handed over in earlier runs and are excluded from the list above. They are named here rather than silently dropped because the ranking axis changed underneath them: they were delivered as likelihood candidates and now classify as hot clocks. Withholding a Tier-1 item because it was once served cold would be the wrong call, so this is your decision, not mine.

| Protocol | Tier | URGENCY | Family | At risk | First delivered |
|---|---:|---:|---|---:|---|
| [TermFinance Vaults](https://defillama.com/protocol/termfinance-vaults) | 1 | 79.07 | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | $12,450,703 | `2ce88d1` |
| [Ekubo](https://defillama.com/protocol/ekubo) | 1 | 75.07 | `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED` | $25,947,903 | `693e2ed` |
| [Set Protocol](https://defillama.com/protocol/set-protocol) | 1 | 74.57 | `AUTH-ZERO-ADDRESS-ACCEPTED` | $12,301,047 | `3bc30a7` |
| [Taiko Bridge](https://defillama.com/protocol/taiko-bridge) | 1 | 74.57 | `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET` | $11,647,101 | `693e2ed` |
| [SmartCredit](https://defillama.com/protocol/smartcredit) | 1 | 73.0 | `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED` | $204,900 | `1ad898f` |
| [Juicebox V3](https://defillama.com/protocol/juicebox-v3) | 1 | 71.57 | `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET` | $163,511 | `1ad898f` |
| [Gondi V3](https://defillama.com/protocol/gondi-v3) | 1 | 71.57 | `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET` | $3,121,447 | `693e2ed` |
| [Venus Core Pool](https://defillama.com/protocol/venus-core-pool) | 1 | 71.57 | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | $1,252,650,314 | `ccb5273` |
| [Abracadabra Spell](https://defillama.com/protocol/abracadabra-spell) | 1 | 70.07 | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | $4,667,807 | `2ce88d1` |
| [Rari Capital](https://defillama.com/protocol/rari-capital) | 1 | 70.07 | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | $1,374,781 | `2ce88d1` |
| [Balancer V2](https://defillama.com/protocol/balancer-v2) | 1 | 70.07 | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | $32,632,264 | `ccb5273` |
| [Penpie](https://defillama.com/protocol/penpie) | 1 | 69.75 | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | $4,503,553 | `6e7df7a` |
| [Aave V3](https://defillama.com/protocol/aave-v3) | 1 | 69.7 | `BRIDGE-MESSAGE-NOT-BOUND-TO-SOURCE` | $16,959,761,663 | `ccb5273` |
| [Bunni V2](https://defillama.com/protocol/bunni-v2) | 1 | 68.57 | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | $213,436 | `3bc30a7` |
| [OTSea](https://defillama.com/protocol/otsea) | 1 | 68.57 | `PROOF-VERIFICATION-BYPASSED` | $576,062 | `1ad898f` |
| [Impermax V3](https://defillama.com/protocol/impermax-v3) | 1 | 68.57 | `AUTH-ZERO-ADDRESS-ACCEPTED` | $98,183 | `693e2ed` |
| [Makina](https://defillama.com/protocol/makina) | 1 | 68.57 | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | $42,438,316 | `1ad898f` |
| [Xave Finance](https://defillama.com/protocol/xave-finance) | 1 | 68.57 | `PROOF-VERIFICATION-BYPASSED` | $149,205 | `693e2ed` |
| [Radiant V2](https://defillama.com/protocol/radiant-v2) | 1 | 68.07 | `SIG-VERIFIER-DEFEATABLE` | $693,778 | `2ce88d1` |
| [Sperax USD](https://defillama.com/protocol/sperax-usd) | 1 | 68.07 | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | $520,189 | `2ce88d1` |
| [KyberSwap Elastic](https://defillama.com/protocol/kyberswap-elastic) | 1 | 68.07 | `SIG-VERIFIER-DEFEATABLE` | $127,719 | `7e319ee` |
| [Conic Finance](https://defillama.com/protocol/conic-finance) | 1 | 68.07 | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | $63,068 | `2ce88d1` |
| [The Idols](https://defillama.com/protocol/the-idols) | 1 | 68.07 | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | $6,571,389 | `2ce88d1` |
| [PrismaLST](https://defillama.com/protocol/prismalst) | 1 | 68.07 | `SIG-VERIFIER-DEFEATABLE` | $331,656 | `2ce88d1` |
| [Exactly](https://defillama.com/protocol/exactly) | 1 | 68.07 | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | $8,067,579 | `6e7df7a` |
| [Yield Protocol](https://defillama.com/protocol/yield-protocol) | 1 | 68.07 | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | $203,354 | `1ad898f` |
| [SIR](https://defillama.com/protocol/sir) | 1 | 68.07 | `SIG-VERIFIER-DEFEATABLE` | $106,823 | `2ce88d1` |
| [Arcadia V2](https://defillama.com/protocol/arcadia-v2) | 1 | 68.07 | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | $5,470,140 | `6e7df7a` |
| [Multichain](https://defillama.com/protocol/multichain) | 1 | 68.07 | `SIG-VERIFIER-DEFEATABLE` | $37,621,575 | `ccb5273` |
| [Moonwell Lending](https://defillama.com/protocol/moonwell-lending) | 1 | 68.0 | `ACC-DONATION-UNACCOUNTED-BALANCE` | $52,209,288 | `1ad898f` |
| [Hundred Finance](https://defillama.com/protocol/hundred-finance) | 1 | 66.57 | `AUTH-ZERO-ADDRESS-ACCEPTED` | $73,585 | `2ce88d1` |
| [Zunami Protocol](https://defillama.com/protocol/zunami-protocol) | 1 | 66.57 | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | $548,289 | `2ce88d1` |
| [Midas Capital](https://defillama.com/protocol/midas-capital) | 1 | 66.57 | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | $103,382 | `3bc30a7` |
| [Swerve](https://defillama.com/protocol/swerve) | 1 | 66.57 | `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET` | $305,359 | `693e2ed` |
| [Bond Protocol](https://defillama.com/protocol/bond-protocol) | 1 | 66.57 | `SIG-DIGEST-AMBIGUOUS-OR-UNBOUND` | $86,442 | `3bc30a7` |
| [UwU Lend](https://defillama.com/protocol/uwu-lend) | 1 | 66.57 | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | $156,312 | `3bc30a7` |
| [Ronin Bridge](https://defillama.com/protocol/ronin-bridge) | 1 | 66.57 | `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET` | $5,172,000 | `6e7df7a` |
| [Inverse Finance Frontier](https://defillama.com/protocol/inverse-finance-frontier) | 1 | 66.57 | `AUTH-ZERO-ADDRESS-ACCEPTED` | $4,540,643 | `693e2ed` |
| [Clipper](https://defillama.com/protocol/clipper) | 1 | 66.57 | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | $781,257 | `1ad898f` |
| [dYdX V3](https://defillama.com/protocol/dydx-v3) | 1 | 66.57 | `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET` | $38,722,798 | `6e7df7a` |

---

## Limits of this ranking

- **No fix-in-artifact check was run.** That is the single highest-value next action and it is what separates 28 points from 40. Until it runs, no row here is `UNREMEDIATED_KNOWN`.
- **Tier 3 is barely populated (4 protocols).** The only dependency this run can evidence is the *declared oracle*, and only where the provider's user population is small enough for one incident to mean something. Backing, collateral, LP and vault-share holdings are **not** resolved — the Blend case (contracts sound, backstop composed of another protocol's LP) is exactly what this run cannot yet see.

- **Tier 1 rests on DefiLlama's incident dataset plus this run's corpus.** A protocol with no recorded incident may simply have no record.

- **Value at risk sits beside the score and never inside it.** A real finding on $60k of dust is a low-value save; check the column before spending time.

- Read-only throughout. No transaction, no calldata, no credential use.

