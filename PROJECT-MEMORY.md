# Project memory & session export — DeFi hack-prevention discovery

*Exported 2026-09-10. This is the "pick up here" document: what the project is, the problems we
worked through and how the thinking changed, what we now stand by, what actually helps, the tools
and conventions, everything produced so far, and where it's still wrong. If you are a fresh session,
read this first — it exists so we never re-litigate settled decisions.*

Companion docs: `UNDERSTANDING.md` (earlier evolution notes) and
`incident-intelligence/results/discoveries/README.md` (the discovery index + no-repeat rules).

---

## 1. What this project is

We are trying to **prevent DeFi protocols from losing money** by finding the *next* likely victim
**before** it happens, so an operator can audit it preemptively.

The loop, in one line: **learn from the last ~6 months of real hacks → understand the on-chain
mechanism → find live, un-hit protocols that share the structural conditions for the next loss.**

Hard scope, settled and non-negotiable:

- **On-chain root causes only.** No off-chain private-key / seed-phrase leaks, no social engineering,
  no infrastructure/DNS compromise, no CEX drains. If the root cause isn't in the contract logic,
  it's out.
- **Discovery, not audit.** Our job is to produce a high-quality, reasoned *queue of candidates*.
  The operator does the actual code audit. We surface the target and the decisive check; we do not
  (usually) confirm the exploit ourselves.
- **Findings are rare, and we never fabricate.** Across hundreds of protocols only one true live
  finding (SOFA) ever came out. An honest negative ("screened, nothing live") is a valid, valuable
  result. We would rather deliver a truthful "no" than a manufactured "maybe."

---

## 2. The problems we went through (and how the thinking changed)

This is the important part — most of our progress was *correcting the selection logic*. Each of
these was a real wrong turn that the operator caught. Do not repeat them.

1. **Mechanical filter-stacking ("conditions").**
   Early runs picked candidates by stacking metadata filters ("4 years unmodified" AND "category X"
   AND "revenue < Y" …) and leaned on a pre-computed scoring/eligibility module.
   **Correction:** drop the conditions. Every pick should be "a little bit personal" — a genuine,
   judgment-based read of *this* protocol — not an AND of filters. Metadata sorting could never have
   found SOFA, because SOFA's bug was in the *authorization math*, visible only by reading code.

2. **Misreading "unwatched" as "unaudited".**
   I filtered on audit status. Wrong.
   **Correction:** *unwatched* has nothing to do with audits. It means **nobody is paid to watch or
   defend the money** — low/no protocol revenue, deprecated, dead website, abandoned. "Just don't
   see 'unaudited' and go at it." Unwatched = no treasury → no auditor on retainer, no monitoring,
   no one who loses their job if it drains.

3. **Repetition across pushes.**
   Runs overwrote the same result files, so each push *replaced* the last and the same protocol
   resurfaced.
   **Correction:** **one immutable file per discovery** (`DISC-<date>-<NNN>-<slug>.md`), and an
   **accumulating exclusion set** (`_exclusion_set.json`) that every new candidate is checked against.
   Never overwrite a prior discovery; add a new file.

4. **Over-centering on SOFA.**
   After the operator shared the SOFA finding, I tried to hunt SOFA *clones*.
   **Correction:** SOFA was **informational context**, not the deliverable. "Do not center everything
   on it." Its lesson is a *shape*, not a template to clone (there were no clones — the code-level
   detector confirmed it was effectively unique on-chain).

5. **A deep single-protocol audit instead of a discovery.**
   I went deep on Notional V1 → its fork Pledge Finance, reading deployed bytecode.
   **Correction:** "I told you a discovery, not an audit." "Personal per each" did **not** mean do a
   full audit of one protocol. That work was good craft but the wrong *altitude* — a discovery is
   many candidates lightly read, not one candidate exhaustively.

6. **Copycat logic — "echoes last week's hack".**
   DISC-008 organized the whole batch around "which fresh incident does this resemble."
   **Correction:** that is a **weak predictor**. It is rare for a Balancer-V1-shaped bug to pay out
   again days later — once an incident is public, the obvious siblings get patched, paused, or
   watched almost immediately. The copycat window closes fast. Resemblance to the headline predicts
   little.

7. **TVL fixation (chasing tiny).**
   DISC-009 let TVL drive selection; I dropped the floor to ~$10k and the list collapsed to a ~$23k
   median, making "tiny" read as the answer.
   **Correction:** **TVL is a neutral attribute, not a ranking axis.** SOFA was an **~$850k-TVL**
   protocol; the exploit only *removed* ~$10k — that number describes the finding, not the target.
   TVL only tells you *whether there's enough to bother auditing*. Don't focus on tiny **or** big;
   "it should be an amount like anything else." (And don't ignore $23k protocols either — just don't
   center on them.)

8. **Chasing a number.**
   I targeted "80+" and produced exactly 84.
   **Correction:** don't chase a count. "When I say 80 it's not that I want exactly 84." Include what
   genuinely fits the logic; the honest number is the number.

9. **"It's not on GitHub / last change 2 weeks ago."**
   Not a work problem — a branch problem. The repo's **default branch** (what the landing page
   renders) was stale. All work sat on the feature branch.
   **Correction:** after pushing the feature branch, **fast-forward the default branch and `main`**
   so the work is visible on the repo page. (Details in §6.)

---

## 3. What we stand by (the durable thesis)

The current, corrected model of **where the next loss will come from** — three things true at once,
none of which is size or resemblance to last week:

1. **It still holds money.** There is something to take. (TVL is the "is it worth it" gate — nothing
   more. SOFA ≈ $850k is the proof that size is not the signal.)
2. **It is unwatched.** No fee revenue / deprecated / dead site / abandoned. Nobody is paid to catch
   the bug, so a bug found today is still live tomorrow. This is the single most important axis.
3. **Its value-moving logic is custom — not a fork.** No Aave / Compound / Uniswap / Liquity /
   MasterChef lineage. Forks inherit code that has been read thousands of times; **novel** bugs live
   in code someone wrote themselves. Bespoke = higher prior of an un-scanned bug.
4. **(Strong bonus) pre-AI-era / unchanged.** Listed before ~2023, before EIP-712 helpers and OZ
   `SafeCast` were reflexive and before LLM-assisted review existed. Idiosyncratic, hand-rolled,
   never machine-scanned — "spaghetti." SOFA's invented XOR-accumulated signature is the archetype.
   The strongest concrete instance of this is the **abandoned "V1"**: a team shipped a V2 and left
   the old bespoke V1 funded and unmaintained (Notional V1 itself is the exemplar).

Additional standing commitments:

- **On-chain root causes only** (see §1).
- **No repetition across pushes** — the accumulating exclusion set is sacred; the operator's
  888-name blocklist is already folded into it.
- **"Personal" = light per-item judgment across many candidates**, not a deep audit of one.
- **Honesty over hedging.** State the decisive check and the falsifier; a clean negative is a result;
  flag known-previously-hacked remnants rather than hiding them; verify claims instead of asserting
  them (e.g., we *measured* "no big protocols in the set," we didn't just say it).
- **Findings are rare; genuinely try, never invent one.**

---

## 4. What actually helps (working with this operator)

- **Take corrections as re-derivations, not patches.** When the operator corrects the logic
  (copycat → structural neglect; TVL → neutral), rebuild the selection from scratch and *show the
  measurement*, don't bolt a tweak onto the old list.
- **Show the reasoning and the numbers.** The most useful single artifact this whole project was the
  diagnostic that showed "81% of the pre-2023 $50k+ band was already delivered" and the floor-sweep
  table — it changed the plan. Measure the population before selecting from it.
- **Don't act on every message.** "You do not have to make changes every time I send a message." A
  question or a clarification is not always a request for a new commit. Answer; act when asked.
- **Be honest about weaknesses in the same breath as the deliverable** (e.g., `listedAt` is listing
  date not last-code-change; fork-lineage metadata is imperfect). The operator trusts flagged
  limitations more than a clean story.
- **Keep TVL descriptive, never prescriptive.**
- **Secrets never touch git** (see §5). This is checked every commit.

---

## 5. Tools, data, and access (what's in the box)

**Data sources**
- `incident-intelligence/protocols/defillama_universe.json` — an **enriched** DefiLlama snapshot
  (8k+ protocols) carrying, beyond name/category/chains/tvl: `_forked_from` (fork lineage — the
  bespoke filter), `_deprecated` / `_dead_url` / `_dead_from` (unwatched signal), `_oracle_types` /
  `_oracles`, `_is_victim` / `_rugged` (exclude already-hit), `listedAt` (age → pre-AI proxy),
  `_governance`, `_authority_flags`. **Note:** it also has pre-computed `_conditions`/`_eligible`
  from the old mechanical era — **ignore those**, per §2.1.
- **Live DefiLlama** (public, no key): `https://api.llama.fi/protocols` (current TVL/category/chains),
  and `https://api.llama.fi/overview/fees?dataType=dailyRevenue` (revenue → the unwatched signal;
  `total30d` per protocol).
- **SlowMist Hacked** (`https://hacked.slowmist.io/?c=&page=N`) — the fresh ~6-month incident feed;
  crawled rows cached at `incident-intelligence/sources/slowmist_run3/rows.json`.

**On-chain / code access**
- **Alchemy** (ETH mainnet, Base) — `eth_getStorageAt`, `eth_call`, code reads. OP not enabled → use
  a public RPC there.
- **Etherscan V2** (multichain via `chainid=`; 1=ETH, 8453=Base, 42161=ARB, 10=OP, 56=BSC):
  `getsourcecode` works on the free tier for **all** chains (this is how we read deployed source);
  **indexer** actions (`getcontractcreation`, logs) are **blocked on the free tier for L2s/BSC**.
- **nodereal** BSC RPC (standard `eth_*`). **Blockscout** for Base logs/reads.
- **GitHub MCP** — `search_code` is **global** and indexes verified-source mirrors
  (`tintinweb/smart-contract-sanctuary-*`) and audit datasets → this is our **code-level detector
  engine** (grep a bug's fingerprint across all deployed verified source). `get_file_contents` is
  **scoped to this repo (dd1)** only; for external source, `WebFetch` on
  `raw.githubusercontent.com/...`.

**Secrets** — all keys live in `incident-intelligence/.env.keys`, which is **gitignored**. Every
commit is preceded by a secret scan (grep for the key fingerprints across everything except
`.git` and `.env.keys`); it must print CLEAN before pushing. Keys have never been committed.

---

## 6. Repo conventions & git reality

**Where things live** (all under `incident-intelligence/`):
- `results/discoveries/DISC-<YYYYMMDD>-<NNN>-<slug>.md` — one immutable file per discovery, plus a
  sibling `...-candidates.json` for machine-readable rows.
- `results/discoveries/_exclusion_set.json` — the accumulating no-repeat set (currently **2,483**
  names; includes the 888-name blocklist). Fold every delivered name+slug in after each push.
- `results/discoveries/README.md` — the discovery index + the no-repeat rules.
- `results/*BATCH*.md`, `CANDIDATES_TO_CHECK.md` — earlier broad lists (see §7).
- `sources/` — on-disk evidence (deployed source, censuses, crawls) per run.
- `tools/` — `check_new.py` (dedup a name against the exclusion set), crawlers, enumeration scripts.

**Git reality (important):**
- Work branch: **`claude/defi-hack-prevention-discovery-0fttk3`**.
- Repo **default branch**: `claude/defi-incident-protocol-audit-hzrbd1` (this is what
  `github.com/USER1029854/dd1` renders). `main` existed but was stale.
- These three are currently fast-forwarded to the same commit. After each push to the work branch,
  **also FF the default branch and `main`** (they've been clean fast-forwards, no history rewrite) so
  the work is visible on the landing page.
- A draft PR (#2) tracks the work branch.
- Commit/PR attribution footer is required and has changed across sessions — use whatever the current
  session's system reminder specifies (it has been Claude Opus 4.8 / Opus 5 with a `Claude-Session:`
  line on commits and a "Generated with Claude Code" line on PRs).

---

## 7. What has been produced so far (the ledger)

**Per-discovery files** (`results/discoveries/`), newest last:

| File | In one line |
|---|---|
| `DISC-20260829-001` | LayerZero OApp unprivileged-arbitrary-call → delegate-hijack screen (SAND class) across 8k+ OApps on ETH+Base. **Clean negative**; detector left standing. |
| `DISC-20260829-002` | The recurring LayerZero-OFT unbacked-mint class (SAND/KelpDAO/StakeDAO) + the on-chain config that stops it. Forward-intel + detector spec. |
| `DISC-20260903-005` | **What SOFA actually was** — replayable / non-binding XOR-aggregate signature auth on a pooled entrypoint. Reusable code-level detector; ran it across GitHub → **no live on-chain sibling** (SOFA was effectively unique). |
| `DISC-20260908-006` | GEB/Maker proxy-actions "singleton-owned SAFE is drainable by anyone." Mechanism proven on live RAI; censused RAI+HAI (clean), Open Dollar immune. Honest negative + standing detector. |
| `DISC-20260908-007` | Notional-V1 `uint128(balance.abs())` truncation defeating `require(freeCollateral>=0)`. Sharp detector across GitHub → the **one** independent fork of the exact bug is **Pledge Finance** (byte-identical source), but no funded deployment found; Notional V2/V3 fixed. |
| `DISC-20260908-008` | Discovery batch, 84 un-hit protocols by "echoes which fresh incident." **Superseded ranking** (copycat logic is weak — see §2.6). |
| `DISC-20260908-009` | "The unmined seam," 116 old/abandoned/bespoke protocols. Correct thesis (structural neglect) but **over-focused on tiny TVL** (~$23k median) — see §2.7. |
| `DISC-20260909-010` | **The current, corrected audit queue.** 108 pre-2023 bespoke-unwatched *primitives*, TVL held neutral, grouped by hand-rolled surface, with a surface-diverse "start here" 14 in the SOFA band. **This is the live deliverable.** |

**Earlier broad batches** (`results/`): `CANDIDATES_TO_CHECK.md` (39), `RANDOM_AUDIT_BATCH.md` (160),
`RANDOM_AUDIT_BATCH_2.md` (180), `UNWATCHED_AUDIT_BATCH.md` (324), `UNWATCHED_AUDIT_BATCH_2.md` (203),
`OLD_AUTOMATOR_BATCH.md` (96), `NEW_DISCOVERY_BATCH.md` (207). All folded into the exclusion set.

**The one confirmed live finding, ever:** SOFA (`sofa.org`), an ~$850k-TVL structured-product
protocol. An old **Automator** unused for ~a year still held pooled depositor capital; its
`mintProducts` entrypoint authorized a whole batch with one signature that was a **XOR accumulation**
of per-item maker hashes — order-independent, collision-craftable, replayable (no nonce/deadline),
and per-item counterparty unchecked. Permissionless entrypoint + pooled counterparty + non-binding
aggregate = drain (~$10.8k realized). It was findable only because the code was *bespoke, unread, and
funded* — the archetype for the whole thesis in §3.

---

## 8. The audit method (the decisive-check discipline)

Every candidate/discovery states:
- its **bespoke surface** — the specific hand-rolled place money moves (option settlement, credit
  solvency, mint/redeem peg, margin/PnL, bridge verification, LP-share pricing, batch authorization);
- a **decisive check** — the concrete on-chain/code question whose answer settles it;
- a **falsifier** — the condition that would make it *safe* (so a "no" is cheap to reach).

Recurring falsifier-worthy shapes we've extracted: unprivileged arbitrary-call reaching config;
non-binding/replayable aggregate signatures on a pooled entrypoint (SOFA); a fund-moving entrypoint
whose owner is an anyone-callable singleton (GEB); a raw narrowing cast of a liability defeating a
solvency check (Notional V1); LP shares priced off `slot0` spot with no TWAP (Arrakis/Float);
thin-float collateral mispriced by a manipulable oracle (Tectonic/Moonwell); mint not bound to a
verified remote burn (Allbridge/Nomad); permissionless asset registration double-counting the same
balance (Reddio); optimistic-oracle settlement with no independent verification / no holder snapshot
(Cozy). These are lenses, not a checklist to stack.

---

## 9. Where it's still wrong (open problems, honest)

- **Age ≠ code-immutability.** `listedAt` is the DefiLlama *listing* date, not the last time the core
  contract changed. The real "pre-AI-era / unchanged" claim needs an on-chain verification (creation
  block + no upgrades since + compiler `<0.8` / no `SafeCast`). **Highest-value next step:** run that
  verification on the DISC-010 "start here" set before auditing, so time isn't spent on something
  quietly maintained.
- **Fork lineage is imperfect.** The bespoke filter trusts DefiLlama/enrichment `_forked_from`; an
  unlabelled fork can slip in and dilute the "novel code" premise.
- **Revenue can be untracked**, so a genuinely watched protocol can look "unwatched" at higher TVL.
  We mitigate by requiring the stronger deprecated/dead signal above ~$5M, but it's not perfect.
- **`address` in DefiLlama is often the token, not the core contract** — so automated per-protocol
  on-chain reads need the real core address first (per-protocol research).
- **Findings are genuinely rare.** The honest base rate is low; the value is in a well-reasoned queue
  + standing code-level detectors that fire when a new deployment matches, not in guaranteeing a hit.

---

## 10. If you're picking this up fresh — do this

1. Read this file, then `results/discoveries/README.md` and `DISC-20260909-010` (the live queue).
2. Recreate `incident-intelligence/.env.keys` from the operator's keys; confirm it's gitignored.
3. Refresh live data (`/protocols`, `/overview/fees?dataType=dailyRevenue`) and re-crawl SlowMist if
   the incident window has moved.
4. Select by **§3**, not by TVL and not by "echoes last week." Rank by unwatched × bespoke × pre-AI.
5. Dedup every candidate against `_exclusion_set.json`; write **one new immutable DISC file**; fold
   the new names back in.
6. Secret-scan → commit (current attribution footer) → push work branch → **FF default branch + `main`**.
7. Don't chase a number, don't fabricate, flag your own weaknesses, and don't commit on every message.
