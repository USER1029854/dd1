# How this project got here — a narrative for whoever picks it up next

**Read this before touching anything.** It is not a summary of the repository; it is the
story of how the repository's *thinking* changed, which is the part that does not survive
in code. The artifacts tell you what the system does now. This tells you what it used to
do, why that was wrong, and which of the current answers are still probably wrong.

Written 2026-08-27, at commit `d15ad33`, after fifteen commits and roughly a dozen
substantive corrections. Almost every one of those corrections came from the operator
pushing back, not from the system noticing its own error. Keep that in mind when reading
anything below that sounds confident.

---

## 0. How to use this file

**Do not treat this as sufficient context.** It deliberately does not reproduce the
incident corpus, the family definitions, the candidate list, or the scoring internals.
Where something matters, it gives you a *pointer and enough orientation to fetch it
properly*. If a decision below matters to what you are about to do, go read the artifact —
this file will be out of date before the artifacts are.

Orientation pointers, roughly in the order you would want them:

| What you want | Where it is | How to read it |
|---|---|---|
| The current candidate list | `incident-intelligence/results/candidates_by_urgency.md` | The only current list. Everything else in `results/` is stale — see §9. |
| Why any candidate is on it | same file, per-candidate block | Each carries its tier, its decisive check, and what would falsify it |
| The incident corpus | `incident-intelligence/incidents/*.jsonl` | `all_raw` → `included` / `provisional` / `excluded`, each with a reason code |
| The mechanism families | `incident-intelligence/families/families.json` | 49 of them; clustered by broken invariant, never by attack label |
| Whether a claim is evidenced | `incident-intelligence/results/manifest_check.txt` | 90 mechanical gates; run `tools/check_manifest.py` |
| How to re-run anything | `incident-intelligence/commands.sh` | Every stage, in order, each appearing once |
| What was already delivered | `incident-intelligence/protocols/delivered_ledger.json` | 629 protocols; rebuilt from git history, not memory |
| The full conversation | `export.md` (gitignored) | Verbatim; contains the operator's API keys, which is why it is not committed |

Credentials live in environment variables only. Nothing in the repository contains a key;
a repo-wide scan enforces this. All chain access throughout has been read-only.

---

## 1. Where we started, and what I thought the problem was

The operator opened with a long specification: enumerate public on-chain security
incidents in a rolling six-month window (2026-02-22 to 2026-08-22, incident date not
publication date), exclude purely off-chain root causes, derive reusable vulnerability
families, then rank the DefiLlama protocol universe for deeper defensive review.

**My initial reading was that this was a ranking problem.** Given a corpus of what got
hacked and a universe of live protocols, score each protocol for how likely it was to be
hacked, sort, hand over the top N. That framing survived, unchallenged by me, for the
first eight commits. Every improvement I made inside it — more protocols, better
indicators, measured weights — made the ranking *better at a task that was the wrong
task*. That is the single most important thing in this document.

The early build was sound as engineering: crawl SlowMist to a **proven date boundary**
(continue until a full page contains no in-window row and every row predates the window
start), gate every incident on root cause, cluster into families by broken invariant
rather than by attack label, fetch the DefiLlama universe and its TVL adapters, probe
deployments read-only, sweep verified source for family indicators. Most of that
machinery is still in use and still correct. The problem was never the machinery.

---

## 2. The corrections, in order

Each of these is written as: what I believed → what the operator said → what the data
actually showed → what changed. The data column matters, because in several cases the
operator's instinct was right but *for a different reason than they gave*, and in at
least one case the measurement contradicted us both.

### 2.1 "I am a small independent entity" — the operator's constraint is part of the problem

I was ranking the whole universe by likelihood, which put large protocols on top because
large protocols genuinely do get attacked more. The operator pointed out that a protocol
holding hundreds of millions is not their save — it already retains auditors.

This produced the **band**: a hard $50k floor (below it there is nothing worth saving) and
a soft $30M ceiling (above it, assume professional coverage). It also produced the first
real separation of concerns: **LIKELIHOOD** (a property of the protocol) and
**ACTIONABILITY** (a property of the operator) became two numbers multiplied together
rather than one blended score.

That separation was right and has survived. The band has survived. What did *not* survive
is my assumption that a good ranking is what the operator needed at all — see §2.8.

### 2.2 Stop asserting weights; measure them

I had been hand-assigning weights to signals. I replaced that with measured lift —
`P(signal | victim) ÷ P(signal | population)` — then fitted weights as `ln(lift)` on
2022–24 incidents and tested against 2025–26 incidents the model never saw.

Three findings from that pass, all of which changed the answer:

- **Survivorship censoring.** Measured against surviving protocols only, "no audit listed"
  looked *protective*. It is not: 62.5% of victims that fell below the floor after being
  hit had no audit, against 20.9% of victims still in band. The population was being
  censored by the very outcome being predicted. (`protocols/survivorship_check.json`)
- **Leakage.** An early backtest showed ×2.87 lift. With a protocol's own prior incidents
  withheld when scoring it, the honest figure was ×1.31. Everything since runs with that
  control on.
- **Ablation over assertion.** I added custody/admin posture expecting it to help. Refitting
  with it *lowered* out-of-sample lift from ×2.19 to ×2.15, so it was dropped from the score
  and reported separately. Exposure age was the only addition that paid (×2.19 → ×2.36).
  (`protocols/ablation.json`)

Current validated figure: **×2.36 lift on 95 protocols hacked after the fitting window**.
Treat that as a statement about *ranking skill*, not about any individual protocol, and
note the caveat in §8.

### 2.3 "You still have repetitions — wepiggy, arcade.xyz"

I measured it: **54 of the 60 protocols in that run had already been handed over.** Each
run was re-ranking the same universe and delivering the same names. Fixed by building a
delivery ledger reconstructed from git history rather than from anything remembered
between sessions (`tools/build_ledger.py`). Withheld-but-surviving protocols are disclosed
rather than silently dropped.

A subtlety I got wrong first time: the ledger excluded `HEAD`, on the theory that HEAD was
"the run being produced now." But HEAD is always a *committed, already-delivered* run — so
five protocols got served twice. Fixed; the gate now covers it.

### 2.4 "You're getting a lot of Solana when it's a small amount of them"

I had sized the non-EVM cohort by **how many protocols each chain hosts**. That is a
popularity measure, not a risk measure. Measured properly as incident-share ÷
protocol-share:

- Solana **×0.63** (22 incidents across 293 protocols) — under-represented, and I had given
  it the largest share at 169 slots
- Cosmos family **×2.25**; EOS **×7.02** (15 incidents / 18 protocols) — never considered
- Sui ×0.59, TON ×0.34

The operator's own corpus agreed independently and I had not looked. Chains below a
support floor are now marked `UNMEASURED` and never given a default value — 382 of them.

### 2.5 The four families that caused the most loss had no indicators

While chasing a bridge lead I found that `BRIDGE-MESSAGE-NOT-BOUND-TO-SOURCE` — the
**highest-loss family in the window** — had zero source indicators, so every one of its
457 pairs was stuck at the shallowest evidence level and none could ever reach guard
review. Same for three others. **The candidate lists had been shaped by which families I
happened to have written regexes for, not by where value was actually lost.** Writing
indicators for those four took deep-evidence pairs from 793 to 992.

This is the clearest example of a general failure mode: *the screen reports on what it can
see, and silently reports nothing about what it cannot.*

### 2.6 Beyond EVM, and a lead that died correctly

Prompted to look past EVM, the run verified the Maya Protocol incident against the
project's live public source — five of six claimed defects confirmed at exact file and
line — and derived four families describing defects the **EVM cannot produce** (a handler
that writes state, fails, and keeps the write; the EVM unwinds, a Cosmos SDK handler does
not).

Then the obvious follow-on lead — THORChain, the $61.9M upstream of the fork that was
exploited — was checked and **killed on evidence**: it carries the `CacheContext()` guard
Maya lacks and none of the five defects. That negative result is recorded rather than
dropped, because a killed lead is a result.

A convergence worth noting: an advisory the operator supplied weeks later
(`GHSA-mjfq-3qr2-6g84`) describes the same broken invariant as two families derived
independently from Maya. Two derivations, different chains, one week apart, same
invariant. That is the strongest evidence in this project that the EVM-semantics /
SDK-state-commitment boundary is a durable defect class.

### 2.7 A threat-intelligence report the operator supplied, used as a filter

It surfaced **two in-window incidents missing from the corpus entirely** (MANTRA and the
TAC chain halt, both inside the window, neither indexed at crawl time). Both were added at
grade C / provisional — the subsystem is named, the mechanism is not, attribution is
explicitly unresolved by the vendor. This is the second and third confirmed instance of a
limitation already documented: **the index is a lead source, not a census.**

It also corrected a circulating figure — and the corpus already had it right, which was
worth knowing.

### 2.8 The axis was wrong: rank by the clock, not by likelihood

This is the largest single change. Likelihood-first treats a novel bug nobody has found
the same as one whose exploit is already written and circulating. The operator replaced
the axis with **time-to-exploitation**: urgency is highest where the technique is already
public **and** the fix is not in the deployed artifact **and** live value is reachable.

Remediation status stopped being a footnote at the bottom of a candidate block and became
40 of 100 points. Tiers 1–5 replaced a flat ranking.

### 2.9 The victim is evidence; the un-hit relative is the target

I implemented the tiers and put **the drained victim in Tier 1**. Backwards. The operator
corrected it, and the measurement was blunt: **155 of 283 recorded victims hold less than
the $50k floor today.** `blend-pools-v2` went $169.2M → $0. My previous #1 candidate had
shrunk 87%. The victims that were *not* empty were aave-v3 at $17.4bn and venus at
$1.27bn — the exposure weighting the operator had rejected two corrections earlier,
sneaking back in through the tier assignment rather than the score.

Three rules now, in this order: **gate** on live value read at head (never historical TVL,
never the amount a past incident moved); **score** reachability only, never magnitude;
**tiebreak** on magnitude — among equals on the same code, prefer the fuller sibling.

The one exception is the **restore window**: a protocol restarted, refunded or
whitehat-restored while the fix is not in the deployed artifact is holding real money
again on the same open door. Six qualify, identified from each victim's TVL *series*
rather than a snapshot — a snapshot cannot distinguish "restored" from "never hit."

### 2.10 "175 is too broad, and Aave V2 is in it"

It was, at $110.9M. Three faults:

1. The above-band exemption let *any* relative link bypass the ceiling, so aave-v2
   re-entered on a sibling that was never materially hit. Now requires the restore window
   or a sibling **proven drained**.
2. **No well-resourced-team filter existed**, although the specification asks for one. Now
   measured rather than name-listed: a protocol whose `parentProtocol` family holds over
   $100M is demoted. Median hot-tier candidate family holds $5.8M; the Aave family holds
   $18.1bn.
3. A sibling never materially hit is weak evidence and no longer carries a tier alone.

The larger inflation was elsewhere and neither of us saw it at first: **all 110 Tier-2 rows
were the same finding.** The Cosmos EVM precompile advisory is a defect in the *chain's*
stack — a DEX on Sei is not running the precompile, Sei is. One row per protocol turned 14
chain findings into 110 candidates and pointed the work at 37 DEX teams when the decisive
check runs once per chain. Collapsed to one candidate per chain: **175 → 43.**

---

## 3. Where the understanding started, and where it ended

| | At the start | Now |
|---|---|---|
| The question | which protocol is most likely to be hacked | which protocol has the shortest path between a public technique and live money |
| The victim | a high-scoring candidate | evidence only; usually an empty vault |
| The target | the protocol the corpus points at | the un-hit relative on the same code |
| Size | folded into the score | a gate and a tiebreak, never a point |
| Weights | assigned by judgement | fitted, ablated, and dropped when they fail out of sample |
| Chain priority | protocol counts | measured incident-share ÷ protocol-share |
| A "population" finding | N candidates | one candidate, N exposures |
| Remediation status | a footnote | the primary ranking driver |
| Unknown evidence | a default | zero, always |

---

## 4. What makes this kind of discovery better

- **Measure the thing rather than assert it.** Every improvement that stuck came from a
  measurement. Every regression came from a plausible assumption.
- **Gate before you score.** A filter applied after ranking lets excluded things influence
  the order. Empty vault → out, before anything is computed.
- **Keep magnitude out of the score.** It re-enters through side doors — through a tier
  assignment, through an exemption clause — and has to be actively kept out. It got back
  in twice here after being removed.
- **Cap prevalence on every signal.** An indicator firing on a third of the population
  describes the population, not the defect. Two separate false clusters came from skipping
  this.
- **Ask what the screen cannot see.** The four highest-loss families were invisible for
  weeks because nobody had written their indicators, and nothing in the system said so.
- **Collapse population findings to the population.** One chain defect is one candidate.
- **Say "unassessable."** Four of six risk archetypes in the Cosmos work need evidence this
  environment cannot reach. Marking them beats guessing, and it tells the next person what
  capability to build.
- **Reconstruct state from artifacts, not memory.** The delivery ledger comes from git.

## 5. What makes it worse

- **Any signal that is secretly a size proxy.** Several fitted weights are; they order a
  queue usefully and mean nothing causally.
- **Trusting a metadata field without checking its population.** `dummy.js` is DefiLlama's
  placeholder for *no adapter*, carried by 1,124 protocols; grouping on it produced a
  7-member "fork cluster" headed by a $19.3M protocol. `forkedFrom` is populated on 6
  protocols out of 8,135, which is why fork lineage here is weak.
- **A snapshot where a series is needed.** Drained and restored look identical in current
  TVL.
- **Self-consistency.** This system never once corrected its own framing. Every axis-level
  error was caught by the operator.

---

## 6. What the system actually does now, mechanically

Roughly, and `commands.sh` is authoritative:

1. Crawl the incident index to a proven date boundary; normalise; gate each incident on
   root cause; grade the evidence; cluster into families by broken invariant.
2. Fetch the DefiLlama universe and its TVL adapters; apply the band; compute observable
   conditions.
3. Probe deployments read-only (`eth_call`, `eth_getStorageAt`, `eth_getCode`, explorer
   source); sweep verified source for each family's documented indicators, with a relevance
   gate, a prevalence cap, and view-helper exclusion.
4. Measure chain hazard; fit and ablate weights; validate out of sample.
5. Classify every recorded victim from its TVL series (drained / restored / never hit);
   build the un-hit relatives graph; **gate on live value read at head**; assign tiers;
   score reachability; collapse chain-level findings; exclude the delivery ledger.
6. Write the list, then run 90 mechanical gates over every load-bearing claim.

---

## 7. Things deliberately **not** in this file — fetch them properly

- **The candidate list itself.** It changes every run and is sensitive work product. Read
  `results/candidates_by_urgency.md`; do not carry names in a summary.
- **Family definitions.** 49 of them, each with preconditions, guards, false-positive
  killers. `families/families.json`. Do not paraphrase a family — the precision is the point.
- **The Maya source verification.** Exact files and lines in
  `incidents/source_verification.json`, including the THORChain negative result.
- **The Cosmos EVM triage.** `results/cosmos_evm_exposure.md`. Note its handling rule:
  it is deliberately *not* a roster of unpatched networks.
- **Scoring internals.** `tools/urgency.py` and `tools/tiers2.py`; the component caps and
  the reasons for each are in their docstrings.

---

## 8. Where I am probably still wrong

The operator has been right about essentially every framing error so far, and has said
plainly that they keep finding wrong things. This list is my best attempt at the ones I
can see; it is certainly incomplete.

1. **The entire urgency premise is unverified.** The scoring band that matters most —
   "the fix is absent from the deployed artifact" — requires reading runtime bytecode at
   the live address. **That check has never been run, for any candidate.** Every row caps
   at 28 of 40 and says so, but that means the central claim of the model is untested.
   This is the highest-value next action by a wide margin.
2. **Zero findings have been confirmed.** Nothing in this project has established that any
   protocol is actually vulnerable. It is a triage queue, and a triage queue that has
   never been validated against an outcome.
3. **Tier 4 rests on `parentProtocol`**, which is a *team* relationship, not a *code*
   relationship. I present it as "same code" more confidently than the evidence supports.
   Runtime bytecode hashing would settle it and has not been done.
4. **The $100M family threshold is a judgement call I made**, defended with a distribution
   but not derived from anything. A different threshold gives a different list.
5. **Tier 3 is nearly empty because there is no holdings model.** The Blend case — sound
   contracts, backstop composed of another protocol's LP — is exactly what this run cannot
   see. This is the second-highest-value missing capability.
6. **Supply-conservation detection was deferred twice.** It is the one instrument that is
   root-cause agnostic, and it is still not built.
7. **Several fitted weights are size and complexity proxies.** `has_2plus_audits` is
   positive because audited protocols are big enough to be worth attacking.
8. **The corpus is a lead source, not a census** — proven twice, by incidents the operator
   supplied that the index never carried. Counts are lower bounds.
9. **The out-of-sample test shares a protocol population with the fit.** Only incidents are
   held out. ×2.36 estimates ranking skill, not a clean prospective trial.
10. **I have repeatedly reintroduced the same class of error** — letting size back into the
    ranking — after removing it. Assume it is back somewhere I have not looked.

---

## 9. Known defects in the repository right now

**The `results/` directory contains two contradictory candidate lists.** Only
`candidates_by_urgency.md` reflects the current model. `candidates_by_priority.md` still
presents itself as "Ranking A — priority (likelihood × actionability)" from the superseded
likelihood-first model, and `run_summary.md` contains **zero** mentions of urgency or
tiers — it describes a model that no longer exists. `candidates_all.csv` and
`audit_variables.txt` are likewise the old handoff.

Anyone opening `run_summary.md` first would get an entirely wrong picture of what this
system does. This is not a subtlety; it is a defect, it is unflagged inside those files,
and it was found while writing this document rather than by any gate. The gates check that
claims are evidenced — they do not check that outputs agree with each other.

---

## 10. If you are picking this up

Run `tools/check_manifest.py` first and read `results/manifest_check.txt`. Then read
`results/candidates_by_urgency.md` and nothing else in `results/` until §9 is resolved.

Then do the thing nobody has done: **take one Tier-1 or Tier-4 candidate, pin its chain
and block, read the runtime bytecode at the live address, and determine whether the fix
from its sibling's postmortem is present.** That single check is what separates 28 points
from 40, it is the premise the whole ranking rests on, and it has never been performed.
