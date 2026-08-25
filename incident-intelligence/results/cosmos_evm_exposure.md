# Cosmos EVM precompile cluster — triage against this run

> **This is not a list of unpatched networks.** Patch state is not verifiable from outside without active probing of live module parameters and the running binary. No such probe was run here and none is asserted: every row below carries `patch_status: NOT_DETERMINED`. The source report declines to publish an exposure roster on the reasoning that the population is small enough that a public list is a target list, and that reasoning is adopted here.

## What this changed in the run

### 1. Two in-window incidents were missing from the corpus

The window closes 2026-08-22. **MANTRA (20 August)** and the **TAC chain halt (22 August)** were both inside it and absent entirely — the SlowMist index had not carried them at crawl time. Both are now in the corpus at **grade C, PROVISIONAL**, which is what the evidence supports and no more: the subsystem is named (Cosmos EVM module / Cosmos-based EVM side), the mechanism is not, no loss figure is published, the running stack version is undisclosed, and attribution to ASA-2026-002 is explicitly unconfirmed by both the chain teams and the vendor. Grade C keeps them out of the family library while retaining them as provisional evidence.

This is the second and third confirmed instance of a limitation already stated in `quality_report.md`: the index is a lead source, not a census, and incident counts are lower bounds.

### 2. Saga was correctly out of scope, and the figures were never conflated

The report corrects a widely circulated "$7.5M TAC incident" as a conflation of two events. This run's corpus already separated them: `INC-2026-01-21-SAG` records Saga at **$7,000,000** and is marked `in_window: false` (the window opens 2026-02-22), and `INC-2026-05-11-TAC` records the TAC bridge at **$2,854,000**. The only $7.5M figure anywhere in this corpus belongs to an unrelated MEV bot incident. The correction validates the boundary logic rather than amending it.

### 3. A convergence worth more than either finding alone

`GHSA-mjfq-3qr2-6g84` — a caller sets a lower EVM call gas limit, partially executes a precompile, and errors at a chosen point **without reverting the already-written state** — is the same broken invariant as two families this run derived independently from the Maya Protocol incident five days earlier:

| Derived from | Family | Invariant |
|---|---|---|
| INC-2026-08-18-MAY (Cosmos SDK handler) | `RUNTIME-STATE-COMMITTED-BEFORE-FUNDING-TRANSFER` | a write must not survive the failure of the operation that produced it |
| INC-2026-08-18-MAY (Cosmos SDK dispatcher) | `RUNTIME-HANDLER-ERROR-NO-ROLLBACK` | an error must discard the writes, not merely be logged |
| GHSA-mjfq-3qr2-6g84 (Cosmos EVM precompile) | `PRECOMPILE-NESTED-CALL-STATE-NOT-PROPAGATED` | partial execution must leave nothing behind |

Two independent derivations — different chains, different mechanisms, different sources, one week apart — landing on one invariant. That is the strongest evidence this run has that the **EVM-semantics / SDK-state-commitment boundary** is a durable defect class rather than a set of one-off bugs. It also means the family was not invented to fit this report: the invariant was already in the library.

### 4. The methodological point, which is the most useful thing in the report

> *Two distinct root causes, one detection signature.*

The Saga loss, the August TAC event and the unrelated May TAC bridge incident all manifested as **unbacked supply** despite having different root causes. This run's entire screen is **signature-based** — static indicators matched against deployed source. That approach structurally cannot catch a defect nobody has written an indicator for, which is exactly the failure the previous pass found in itself when the four highest-loss families turned out to have no indicators at all.

An **invariant** check is root-cause agnostic and would have flagged all three. Implementing it honestly needs a per-protocol backing model this run's probe does not carry — supply on one side, escrow and module accounts and bridged representations on the other — so it is recorded as the recommended control rather than shipped thin. What the probe layer would need: `totalSupply` alongside the existing `totalAssets`, the declared underlying, and the escrow balance actually held.

## The advisories

| Advisory | Component | Affected | Patched | Mechanism |
|---|---|---|---|---|
| `ASA-2026-002 / GHSA-54gx-3cgr-7mfm / GO-2026-4677` | ICS20 precompile | github.com/cosmos/evm < v0.6.0 | v0.6.0 | state updates during recursive calls not reflected in the outer execution context; the same token balance can be used repeatedly within one transaction |
| `GHSA-mjfq-3qr2-6g84` | any precompile | evmOS / Cosmos EVM using precompiles | per-precompile atomic wrapper reverting partial state | a lower EVM call gas limit lets a caller partially execute a precompile and error at a chosen point without reverting already-written state; also a liveness vector |
| `GHSA-8pfh-j44r-f654` | static and dynamic precompiles | < v0.3.1 / v0.4.2 / v0.5.0 | v0.3.1, v0.4.2, v0.5.0 | withheld at disclosure; the advisory states no workaround exists for chains using precompiles, so upgrading was the only remediation path |

Confirmed exploitation: **Saga EVM, 2026-01-21, ~$7M (OUTSIDE this run's window)**. The other two advisories have no published exploitation.

## Exposure surface in this run's universe

Chain membership in a Cosmos EVM stack is the vendor's own scope criterion. It is **not** a claim about any chain's patch state.

| | |
|---|---:|
| Protocols above the $50,000 floor on a Cosmos EVM chain | 222 |
| Of those, inside the $50k–$30M band | **170** |
| In band, with a prior on-chain incident in the last 12 months | **30** |
| On a chain whose organisation was named in the ASA-2026-002 remediation credits | 7 |

| Chain | In-band protocols |
|---|---:|
| Berachain | 42 |
| Kava | 38 |
| Cronos | 37 |
| Sei | 28 |
| Injective | 18 |
| ZetaChain | 15 |
| Canto | 10 |
| Evmos | 9 |
| Nibiru | 8 |
| Initia | 5 |
| TAC | 3 |
| Saga | 2 |
| Dymension | 2 |
| Shido | 2 |
| Mantra | 1 |

## What can and cannot be assessed from here

Most of the report's risk archetypes need evidence this run cannot reach. Saying so is more useful than guessing at them.

| Archetype | Assessable here | Why |
|---|---|---|
| A — vendored or hard-forked `cosmos/evm` | **No** | needs the chain's repository tree; this session's network policy cannot enumerate arbitrary public repos |
| B — mitigated by disabling, not upgrading | **No** | needs live Cosmos module parameters; no Cosmos RPC path is configured in this run |
| C — attested only by participation | **Yes** | the vendor named the collaborating organisations, and one of them was halted five months later |
| D — migrated off evmOS onto a pre-`v0.6.0` release | **No** | needs upgrade announcements and release notes |
| E — disabled but governance-reachable | **No** | needs parameters plus an on-chain governance path |
| F — precompiles other than ICS20 | **Partially** | the vendor scope covers any Cosmos EVM chain using precompiles, so membership is the criterion |

**Archetype C is the one that matters most and the one that is evidenced.** The report's central finding is that MANTRA was credited as a collaborator on the March remediation and was halted by a Cosmos EVM module incident in August. Participation in a coordinated remediation is not evidence of remediation. Every chain among the vendor's "15" should be treated as unassessed rather than clear — and the true population is a superset of 15, because any identification method based on Go module metadata systematically misses vendored and hard-forked deployments.

## Attribution is unresolved, and this run does not resolve it

| Hypothesis | If true |
|---|---|
| **H1** — incomplete remediation of ASA-2026-002 | `v0.6.0`+ is sufficient; the problem is adoption and configuration drift |
| **H2** — a variant in the same family | `v0.6.0` is **not** sufficient; every chain that believes itself remediated is still exposed |

Both remain live. The provisional grading of the two August incidents in this corpus is the direct expression of that: neither is mapped into the family library as confirmed evidence, and the family they carry is marked `evidence_strength: MEDIUM` with its window-statistic contribution explicitly zero.

## Handling

`protocols/cosmos_evm_triage.json` holds the rows. It is defensive work product on the same footing as the candidate lists in this run: it is a triage input for coordinated disclosure, not a publication. Any finding goes to the chain team and upstream in parallel — upstream can produce a patch, but only the chain team can execute a validator upgrade, and in the January event the gap between fix availability and downstream deployment was the entire exposure window.

## Limits of this triage

- Chain membership is drawn from the report's scope statement plus chains present in this universe. It is not an authoritative roster of Cosmos EVM deployments, and the vendor's own count is a lower bound.
- Protocol TVL is protocol-wide, not per-chain, so a multichain protocol's exposure to any single chain is smaller than its figure suggests. No per-chain split is claimed.
- Prior-incident dates come from DefiLlama's dataset plus this run's own corpus. Absence of a prior incident is absence of a record, not evidence of a clean history.
- Nothing here establishes that any named protocol is affected by any advisory. Deployment on a chain running a stack is not a statement about that chain's version, its enabled precompile set, or the protocol's own code.

