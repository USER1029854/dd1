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

_The exclusion set is a snapshot in `_exclusion_set.json`; regenerate it when new pushes land._
