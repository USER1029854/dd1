# Discoveries — one file per discovery, never overwritten

**Why this directory exists.** Earlier runs kept rewriting the same result files
(`candidates_by_urgency.md`, etc.), so each push *replaced* the prior discovery instead of
adding to it, and the same protocol could resurface across pushes. From run 3 on, **every
discovery is its own immutable file** here, and **every candidate is checked against the full
exclusion set** (all prior pushes) before it is written.

## Rules

1. **One file per discovery.** Filename: `DISC-<YYYYMMDD>-<NNN>-<slug>.md`. Never edit a prior
   discovery's substance to add a new one — add a new file. (Corrections/updates to an existing
   discovery may append a dated `## Update` section to that same file.)
2. **No repetition across any push.** Before writing, run
   `python3 tools/check_new.py "<name>"` against `results/discoveries/_exclusion_set.json`
   (union of `delivered_ledger.json` = 629, every slug in `results/*.md`, and the run-2
   candidates). A candidate already present is not re-delivered.
3. **Every discovery states its evidence tag** (deployment-verified vs reference) and its
   **decisive check** and **falsifier**, per the audit method. A negative result (a screen that
   found nothing live) is a valid discovery and gets its own file — it answers "would the screen
   catch the next one."
4. **Live value is read at head**, never historical TVL.

## Index

| File | Discovery | Type | Status |
|---|---|---|---|
| `DISC-20260829-001-layerzero-oapp-delegate-hijack-screen.md` | LayerZero OApp unprivileged-arbitrary-call → delegate-hijack screen (SAND class) across 8,215 OApps on ETH+Base | EVM screen | **clean negative** — no live un-hit unprivileged instance; SAND contained; detector left standing |
| `DISC-20260829-002-oft-unbacked-mint-recurring-class.md` | The recurring $300M+ LayerZero-OFT unbacked-mint class (SAND / KelpDAO / StakeDAO) and the on-chain config that stops it | forward intelligence + detector spec | in-scope sub-screen (SAND shape) done in DISC-001; delegate/DVN sub-screens specified, not yet run |
| **`../CANDIDATES_TO_CHECK.md`** | **39 non-repeating protocols to check**, grouped by the 6-month incident each echoes (Arrakis / CometDEX / Moonwell / Sandbox-Allbridge-warp / KelpDAO / Term) | **shortlist of leads** | live-TVL-verified, band-filtered, all dedup-cleared vs the exclusion set; per-row decisive check |

> The 39 candidates in `../CANDIDATES_TO_CHECK.md` have been folded into `_exclusion_set.json` (now 847
> names), so the next run will not re-deliver them. Backing data: `DISC-20260829-003-candidates.json`.

_The exclusion set is a snapshot in `_exclusion_set.json`; regenerate it when new pushes land._
| `DISC-20260903-005-aggregate-signature-auth-detector.md` | What SOFA actually was (replayable/non-binding aggregate-signature auth on a pooled entrypoint), the real family, and a reusable **code-level detector**; ran it across GitHub → no live on-chain sibling | mechanism + detector + honest negative | supersedes the age lens; keep the detector running |
| `DISC-20260908-006-proxyactions-singleton-owned-safe.md` | GEB/Maker proxy-actions class (Sep-2 GebProxyActions): a SAFE owned by an anyone-callable singleton is drainable by anyone. Mechanism proven on live RAI; censused RAI + HAI (clean), OD immune | deep audit + on-chain census + detector | clean at head across 3 live deployments; standing detector for the next instance |
| `DISC-20260908-007-narrowing-cast-solvency-truncation-detector.md` | Notional-V1 class (Sep-4, $1.73M): a **raw** `uint128(balance.abs())` cast truncates a `2^128` liability to 0, defeating `require(freeCollateral>=0)`. Read to the metal; sharp detector run across GitHub + verified-source mirrors | mechanism + code detector + on-chain census | the only independent fork of the exact bug is **Pledge Finance** (byte-identical source) — no funded deployment found (0 TVL, "testing phase", product pivoted); Notional V2/V3 fixed. Standing detector + specific watch on Pledge / any Notional-V1 fork |
| `DISC-20260908-008-fresh-mechanism-discovery-batch.md` | **Discovery batch — 84 un-hit protocols** mapped to the 6-month incident whose mechanism each echoes (thin-collateral oracle / illiquid-perp self-trade / permissionless-registration double-count / unauth V3 callback / OO settlement no-snapshot / orderbook / bridge mint / slot0-LP / AMM edge / split-invariance) | broad ranked queue (not an audit) | live-TVL-verified $50k–$50M, unwatched-first, all dedup-cleared vs 2,144-name exclusion set; each row has a decisive check. Folded in → 2,273. Backing: `DISC-20260908-008-candidates.json` |
