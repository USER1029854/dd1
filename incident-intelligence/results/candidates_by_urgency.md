# Urgency-first candidates — ranked by the clock, not by likelihood

> **Discovery stage.** Nothing here says any protocol is exploitable. Each entry is a *high-urgency audit candidate*: named evidence matches a family's prerequisites, named evidence is unknown, and a named guard would falsify it. A high `URGENCY` is a triage order, never an exploit probability.

## The incident is the evidence. The un-hit relative is the target.

The previous version of this list put the **victim** in Tier 1. That was backwards. A drained victim's value is already gone — a hot clock over an empty vault is not a candidate. What the incident actually gives you is proof that the technique is public and the code was unpatched; the money is in the *other* deployments of that code.

Measured, not assumed: **155 of 283 recorded victims hold less than the $50,000 floor today.** The old Tier-1 list was largely empty vaults, and the ones that were not empty were giants — aave-v3 at $17.4bn, venus-core-pool at $1.27bn — which is exactly the exposure weighting that was rejected.

### Three rules, in this order

1. **Gate on live value, read at head (2026-08-27T09:59:26Z).** Never historical TVL, never the amount a past incident moved. Empty → out, *before* anything is scored. A drained victim is excluded however fresh its incident is.
2. **Score reachability, never magnitude.** A small wide-open vault outranks a large hard-to-reach one. No dollar term appears anywhere in the 100 points — putting size back into the score would re-create the $3bn-tops-the-list failure.
3. **Tiebreak on magnitude.** Among equals on the same code, prefer the fuller sibling.

Ordering is **tier first, then urgency** — a hotter tier outranks a higher score, so a Tier-1 row at 40.75 sits above a Tier-2 row at 84.07 by design.

### The one exception: the restore window

A protocol restarted, refunded or whitehat-restored **without the fix in the deployed artifact** is holding real money again on the same open door, and the first hours after it resumes are the highest-sensitivity moment in this whole model. Six qualify, identified from their TVL series rather than a snapshot: they fell hard around their incident and have since recovered materially.

**The honest ceiling in this run is 28 of those 40, not 40.** The full band requires confirming that the specific fixed line is *absent from the deployed artifact* — an L4 read of runtime bytecode at the live address. This run has not performed that per-protocol check, so every Tier-1/2 row carries `KNOWN_ISSUE_STATUS_UNKNOWN` and names the decisive check that would settle it. That check is the first thing to run, and it is fast.

## What the tiers found

| Tier | What it means | Fresh protocols |
|---|---|---:|
| **1 — UNREMEDIATED-KNOWN** | restore-window victim, or an un-hit deployment on the *same code* as a hit sibling | **2** |
| **2 — SHARED-DEPENDENCY** | an advisory or template live across a population with no patch-compliance mechanism | **14** |
| 3 — DEPENDENCY-IMPAIRMENT | the target holds or is backed by a system that is itself exposed | 0 |
| **4 — FORK-OF-RECENT-VICTIM** | version sibling of a victim — *this is where the un-hit relatives are* | **27** |
| 5 — NOVEL-HIGH-FIT | strong match, no public disclosure — the clock has not started | 1407 |

This list delivers **every fresh candidate in the hot tiers (1–4): 43 protocols**, not a round number. Tier 5 — novel high-fit, where the clock has not started — is excluded by construction; it is the old likelihood-first list and it belongs below everything here.

**Tier 2 is collapsed to chain rows.** The Cosmos EVM precompile advisory is a defect in the *chain's* stack, not in each protocol deployed on it. Listing it per-protocol produced 110 rows for 14 real findings — eightfold inflation, and it pointed the work at 37 DEX teams when the decisive check runs once per chain and the disclosure goes to the chain team. The protocols are named as exposure inside each chain row.

**Where Tier 4 is:** it is the biggest hot tier in this run at **27 fresh protocols**, and under this framing it is the point. A Tier-4 row is an un-hit version sibling of a protocol that was exploited — the sibling supplies the technique, this deployment still holds the money. The previous list buried them because it filled every slot with Tier 1–2; they are ranked in line here.

## Handoff lines for CORE.md

```
TARGET=https://defillama.com/protocol/save || TIER=1 || FAMILY=ORACLE-STALE-OR-SILENT-FALLBACK || DECISIVE_CHECK=Confirm the fix from the 2022-11-02 postmortem is present in the DEPLOYED artifact at the live address, not merely in the repo or a release note. Absent -> act now. || VALUE_AT_RISK=85337343 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM|SOLANA
TARGET=https://defillama.com/protocol/tinyman || TIER=1 || FAMILY=ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED || DECISIVE_CHECK=Confirm the fix from the 2022-01-01 postmortem is present in the DEPLOYED artifact at the live address, not merely in the repo or a release note. Absent -> act now. || VALUE_AT_RISK=5523729 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/chain/Berachain || TIER=2 || FAMILY=AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY || DECISIVE_CHECK=Pin Berachain's running github.com/cosmos/evm version AND query live module params for the enabled static precompile set. Do not infer either from release notes; a vendor || VALUE_AT_RISK=247257928 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/chain/Canto || TIER=2 || FAMILY=AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY || DECISIVE_CHECK=Pin Canto's running github.com/cosmos/evm version AND query live module params for the enabled static precompile set. Do not infer either from release notes; a vendored x || VALUE_AT_RISK=27743956 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=BRIDGE|EVM
TARGET=https://defillama.com/chain/Cronos || TIER=2 || FAMILY=AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY || DECISIVE_CHECK=Pin Cronos's running github.com/cosmos/evm version AND query live module params for the enabled static precompile set. Do not infer either from release notes; a vendored  || VALUE_AT_RISK=119844848 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=BRIDGE|EVM
TARGET=https://defillama.com/chain/Sei || TIER=2 || FAMILY=BRIDGE-MESSAGE-NOT-BOUND-TO-SOURCE || DECISIVE_CHECK=Pin Sei's running github.com/cosmos/evm version AND query live module params for the enabled static precompile set. Do not infer either from release notes; a vendored x/e || VALUE_AT_RISK=167445095 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=BRIDGE|EVM|SOLANA
TARGET=https://defillama.com/chain/Kava || TIER=2 || FAMILY=BRIDGE-MESSAGE-NOT-BOUND-TO-SOURCE || DECISIVE_CHECK=Pin Kava's running github.com/cosmos/evm version AND query live module params for the enabled static precompile set. Do not infer either from release notes; a vendored x/ || VALUE_AT_RISK=104390516 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=BRIDGE|EVM
TARGET=https://defillama.com/chain/ZetaChain || TIER=2 || FAMILY=ACC-SIGN-OR-BOUND-CHECK-MISSING || DECISIVE_CHECK=Pin ZetaChain's running github.com/cosmos/evm version AND query live module params for the enabled static precompile set. Do not infer either from release notes; a vendor || VALUE_AT_RISK=36688622 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/chain/TAC || TIER=2 || FAMILY=ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED || DECISIVE_CHECK=Pin TAC's running github.com/cosmos/evm version AND query live module params for the enabled static precompile set. Do not infer either from release notes; a vendored x/e || VALUE_AT_RISK=13092188 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM|MOVE_SUI
TARGET=https://defillama.com/chain/Nibiru || TIER=2 || FAMILY=AUTH-ZERO-ADDRESS-ACCEPTED || DECISIVE_CHECK=Pin Nibiru's running github.com/cosmos/evm version AND query live module params for the enabled static precompile set. Do not infer either from release notes; a vendored  || VALUE_AT_RISK=34225642 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=COSMOS_APPCHAIN|EVM
TARGET=https://defillama.com/chain/Evmos || TIER=2 || FAMILY=ACC-DONATION-UNACCOUNTED-BALANCE || DECISIVE_CHECK=Pin Evmos's running github.com/cosmos/evm version AND query live module params for the enabled static precompile set. Do not infer either from release notes; a vendored x || VALUE_AT_RISK=52346635 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/chain/Saga || TIER=2 || FAMILY=ACC-DONATION-UNACCOUNTED-BALANCE || DECISIVE_CHECK=Pin Saga's running github.com/cosmos/evm version AND query live module params for the enabled static precompile set. Do not infer either from release notes; a vendored x/ || VALUE_AT_RISK=32022154 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/chain/Injective || TIER=2 || FAMILY=AUTH-MISSING-ON-VALUE-MOVING-PATH || DECISIVE_CHECK=Pin Injective's running github.com/cosmos/evm version AND query live module params for the enabled static precompile set. Do not infer either from release notes; a vendor || VALUE_AT_RISK=45873068 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=COSMOS_APPCHAIN
TARGET=https://defillama.com/chain/Dymension || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin Dymension's running github.com/cosmos/evm version AND query live module params for the enabled static precompile set. Do not infer either from release notes; a vendor || VALUE_AT_RISK=5745325 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=COSMOS_APPCHAIN|EVM
TARGET=https://defillama.com/chain/Initia || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin Initia's running github.com/cosmos/evm version AND query live module params for the enabled static precompile set. Do not infer either from release notes; a vendored  || VALUE_AT_RISK=4842851 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/chain/Shido || TIER=2 || FAMILY=QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET || DECISIVE_CHECK=Pin Shido's running github.com/cosmos/evm version AND query live module params for the enabled static precompile set. Do not infer either from release notes; a vendored x || VALUE_AT_RISK=729653 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/hope-collateral || TIER=4 || FAMILY=QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=1604842 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/allbridge-classic || TIER=4 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=1057520 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=BRIDGE|EVM|SOLANA
TARGET=https://defillama.com/protocol/balancer-cow-amm || TIER=4 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=59803 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/paraluni-dex || TIER=4 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=323497 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/hope-swap || TIER=4 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=114226 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/wemix.fi-staking || TIER=4 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=19923463 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/summer.fi-pro || TIER=4 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=17019560 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/termfinance-lend || TIER=4 || FAMILY=ORACLE-STALE-OR-SILENT-FALLBACK || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=5167045 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/wemix-concentrated-range-deposit || TIER=4 || FAMILY=QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=2169898 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/wemix-full-range-deposit || TIER=4 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=824781 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/bonzo-vaults || TIER=4 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=425571 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/wemix-liquid-staking || TIER=4 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=254157 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/cozy-earn || TIER=4 || FAMILY=AUTH-MISSING-ON-VALUE-MOVING-PATH || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=1043001 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/typus-dov || TIER=4 || FAMILY=AUTH-MISSING-ON-VALUE-MOVING-PATH || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=996301 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=MOVE_SUI
TARGET=https://defillama.com/protocol/velar-amm || TIER=4 || FAMILY=ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=401394 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/typus-safu || TIER=4 || FAMILY=ACC-ZERO-SUPPLY-INFLATION || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=191193 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=MOVE_SUI
TARGET=https://defillama.com/protocol/apertureswap || TIER=4 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=51432 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/pando-leaf || TIER=4 || FAMILY=ORACLE-STALE-OR-SILENT-FALLBACK || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=11396230 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/woofi-earn || TIER=4 || FAMILY=ACC-ZERO-SUPPLY-INFLATION || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=2694195 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/nirvana-v2 || TIER=4 || FAMILY=AUTH-MISSING-ON-VALUE-MOVING-PATH || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=2586219 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=SOLANA
TARGET=https://defillama.com/protocol/4swap || TIER=4 || FAMILY=ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=494167 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/basin-exchange || TIER=4 || FAMILY=ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=438854 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/cetus-dlmm || TIER=4 || FAMILY=ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=433422 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=MOVE_SUI
TARGET=https://defillama.com/protocol/swapx-algebra || TIER=4 || FAMILY=ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=404169 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/voltage-v4 || TIER=4 || FAMILY=ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=186232 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/velocore-v1 || TIER=4 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=126571 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/voltage-liquid-staking || TIER=4 || FAMILY=PROOF-VERIFICATION-BYPASSED || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=86834 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
```

## Candidates

### 1. Save — Tier 1 — URGENCY 40.75

- **Protocol:** `save` · Lending · Solana, Eclipse
- **DefiLlama:** https://defillama.com/protocol/save
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $85,337,344
    - **RESTORE WINDOW** — fell 91% around 2022-11-02 ($269,197,907 -> $25,259,893) and has since recovered to $85,337,344
- **Matched family:** `ORACLE-STALE-OR-SILENT-FALLBACK`
    - broken invariant: A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
- **URGENCY 40.75 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - RESTORE WINDOW: fell 91% around 2022-11-02 ($269,197,907 -> $25,259,893) and has since recovered to $85,337,344. It is holding real money again; if the fix is not in the deployed artifact it is the same open door.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 1394d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Confirm the fix from the 2022-11-02 postmortem is present in the DEPLOYED artifact at the live address, not merely in the repo or a release note. Absent -> act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Disclosure channel, if public:** https://www.save.finance/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 2. Tinyman — Tier 1 — URGENCY 40.38

- **Protocol:** `tinyman` · Dexs · Algorand
- **DefiLlama:** https://defillama.com/protocol/tinyman
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $5,523,730
    - **RESTORE WINDOW** — fell 100% around 2022-01-01 ($38,434,474 -> $22,593) and has since recovered to $5,523,730
- **Matched family:** `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`
    - broken invariant: Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.
- **URGENCY 40.38 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - RESTORE WINDOW: fell 100% around 2022-01-01 ($38,434,474 -> $22,593) and has since recovered to $5,523,730. It is holding real money again; if the fix is not in the deployed artifact it is the same open door.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 1699d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Confirm the fix from the 2022-01-01 postmortem is present in the DEPLOYED artifact at the live address, not merely in the repo or a release note. Absent -> act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Every identifier derived or verified against the factory/registry (kills the pair); Routing restricted to an immutable venue allowlist
- **Disclosure channel, if public:** https://tinyman.org
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 3. Berachain (chain-level) — Tier 2 — URGENCY 84.07

- **Chain-level candidate:** `Berachain` — the defect is in the chain's own stack. **37 protocols** above the floor are exposed; one chain fix closes all of them.
    - most exposed: `extra-finance-leverage-farming`, `reservoir-protocol`, `kodiak-islands`, `orderly-bridge`, `steer-protocol`, `zoo-finance`, `infrared-finance`, `kodiak-v3`
- **DefiLlama:** https://defillama.com/chain/Berachain
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $247,257,928
- **Matched family:** `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`
    - broken invariant: A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
- **URGENCY 84.07 / EVIDENCE_CONFIDENCE 85.4** — evidence level `L4_GUARD_REVIEW`
    - remediation gap 28/40 · technique recency+propagation 20.0/20 · reachable live value 25.0/25 · precondition match 11.07/15
- **Why the clock is hot:**
    - Berachain runs a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED. The defect is in the chain's own stack, not in any one protocol deployed on it.
    - 37 protocols above the floor sit on this chain, holding $247,257,928 between them. They are the exposure, not 37 separate candidates -- one chain fix closes all of them.
    - reachability: 3 precondition(s) present at L4_GUARD_REVIEW, no guard found in the reviewed path
    - recency: technique public 25d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin Berachain's running github.com/cosmos/evm version AND query live module params for the enabled static precompile set. Do not infer either from release notes; a vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 4. Canto (chain-level) — Tier 2 — URGENCY 84.07

- **Chain-level candidate:** `Canto` — the defect is in the chain's own stack. **8 protocols** above the floor are exposed; one chain fix closes all of them.
    - most exposed: `synapse-cross-chain-bridge`, `acryptos`, `hiyield`, `canto-lending`, `tarot`, `impermax-v2`, `fortunafi`, `canto-dex`
- **DefiLlama:** https://defillama.com/chain/Canto
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $27,743,956
- **Matched family:** `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`
    - broken invariant: A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
- **URGENCY 84.07 / EVIDENCE_CONFIDENCE 85.4** — evidence level `L4_GUARD_REVIEW`
    - remediation gap 28/40 · technique recency+propagation 20.0/20 · reachable live value 25.0/25 · precondition match 11.07/15
- **Why the clock is hot:**
    - Canto runs a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED. The defect is in the chain's own stack, not in any one protocol deployed on it.
    - 8 protocols above the floor sit on this chain, holding $27,743,956 between them. They are the exposure, not 8 separate candidates -- one chain fix closes all of them.
    - reachability: 3 precondition(s) present at L4_GUARD_REVIEW, no guard found in the reviewed path
    - recency: technique public 25d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin Canto's running github.com/cosmos/evm version AND query live module params for the enabled static precompile set. Do not infer either from release notes; a vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 5. Cronos (chain-level) — Tier 2 — URGENCY 84.07

- **Chain-level candidate:** `Cronos` — the defect is in the chain's own stack. **33 protocols** above the floor are exposed; one chain fix closes all of them.
    - most exposed: `moonlander`, `dxsale`, `fulcrom-perps`, `flokifi-locker`, `synapse-cross-chain-bridge`, `acryptos`, `symbiosis`, `autofarm`
- **DefiLlama:** https://defillama.com/chain/Cronos
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $119,844,849
- **Matched family:** `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`
    - broken invariant: A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
- **URGENCY 84.07 / EVIDENCE_CONFIDENCE 85.4** — evidence level `L4_GUARD_REVIEW`
    - remediation gap 28/40 · technique recency+propagation 20.0/20 · reachable live value 25.0/25 · precondition match 11.07/15
- **Why the clock is hot:**
    - Cronos runs a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED. The defect is in the chain's own stack, not in any one protocol deployed on it.
    - 33 protocols above the floor sit on this chain, holding $119,844,849 between them. They are the exposure, not 33 separate candidates -- one chain fix closes all of them.
    - reachability: 3 precondition(s) present at L4_GUARD_REVIEW, no guard found in the reviewed path
    - recency: technique public 25d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin Cronos's running github.com/cosmos/evm version AND query live module params for the enabled static precompile set. Do not infer either from release notes; a vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 6. Sei (chain-level) — Tier 2 — URGENCY 83.12

- **Chain-level candidate:** `Sei` — the defect is in the chain's own stack. **26 protocols** above the floor are exposed; one chain fix closes all of them.
    - most exposed: `pumpbtc`, `orderly-bridge`, `steer-protocol`, `zoo-finance`, `feather`, `saphyre-v3`, `astroport`, `symbiosis`
- **DefiLlama:** https://defillama.com/chain/Sei
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $167,445,096
- **Matched family:** `BRIDGE-MESSAGE-NOT-BOUND-TO-SOURCE`
    - broken invariant: A release, mint or payout on the destination domain must be authorised only by a proof that binds, simultaneously: the source chain identity, the source channel/route, the exact asset, the exact amount, the recipient, and a nonce that is consumed exactly once. Verifying that a message is well-formed or correctly signed is not the same as verifying that it corresponds to a real deposit of equal value.
- **URGENCY 83.12 / EVIDENCE_CONFIDENCE 90.4** — evidence level `L4_GUARD_REVIEW`
    - remediation gap 28/40 · technique recency+propagation 20.0/20 · reachable live value 25.0/25 · precondition match 10.12/15
- **Why the clock is hot:**
    - Sei runs a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED. The defect is in the chain's own stack, not in any one protocol deployed on it.
    - 26 protocols above the floor sit on this chain, holding $167,445,096 between them. They are the exposure, not 26 separate candidates -- one chain fix closes all of them.
    - reachability: 5 precondition(s) present at L4_GUARD_REVIEW, no guard found in the reviewed path
    - recency: technique public 18d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin Sei's running github.com/cosmos/evm version AND query live module params for the enabled static precompile set. Do not infer either from release notes; a vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Destination mint requires a Merkle/zk proof against a source state root that itself commits to the amount; Reserve reconciliation is enforced on-chain (mint reverts if supply would exceed escrow); Bridge is one-way with no destination-side release
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 7. Kava (chain-level) — Tier 2 — URGENCY 82.0

- **Chain-level candidate:** `Kava` — the defect is in the chain's own stack. **33 protocols** above the floor are exposed; one chain fix closes all of them.
    - most exposed: `steer-protocol`, `kava-mint`, `stargate-v1`, `acryptos`, `symbiosis`, `ichi`, `scrub-invest`, `kava-lend`
- **DefiLlama:** https://defillama.com/chain/Kava
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $104,390,516
- **Matched family:** `BRIDGE-MESSAGE-NOT-BOUND-TO-SOURCE`
    - broken invariant: A release, mint or payout on the destination domain must be authorised only by a proof that binds, simultaneously: the source chain identity, the source channel/route, the exact asset, the exact amount, the recipient, and a nonce that is consumed exactly once. Verifying that a message is well-formed or correctly signed is not the same as verifying that it corresponds to a real deposit of equal value.
- **URGENCY 82.0 / EVIDENCE_CONFIDENCE 90.4** — evidence level `L4_GUARD_REVIEW`
    - remediation gap 28/40 · technique recency+propagation 20.0/20 · reachable live value 25.0/25 · precondition match 9.0/15
- **Why the clock is hot:**
    - Kava runs a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED. The defect is in the chain's own stack, not in any one protocol deployed on it.
    - 33 protocols above the floor sit on this chain, holding $104,390,516 between them. They are the exposure, not 33 separate candidates -- one chain fix closes all of them.
    - reachability: 4 precondition(s) present at L4_GUARD_REVIEW, no guard found in the reviewed path
    - recency: technique public 18d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin Kava's running github.com/cosmos/evm version AND query live module params for the enabled static precompile set. Do not infer either from release notes; a vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Destination mint requires a Merkle/zk proof against a source state root that itself commits to the amount; Reserve reconciliation is enforced on-chain (mint reverts if supply would exceed escrow); Bridge is one-way with no destination-side release
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 8. ZetaChain (chain-level) — Tier 2 — URGENCY 81.07

- **Chain-level candidate:** `ZetaChain` — the defect is in the chain's own stack. **14 protocols** above the floor are exposed; one chain fix closes all of them.
    - most exposed: `steer-protocol`, `symbiosis`, `dyorswap-amm`, `iziswap`, `accumulated-finance-liquid-staking`, `meson`, `nervebridge`, `abstradex`
- **DefiLlama:** https://defillama.com/chain/ZetaChain
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $36,688,623
- **Matched family:** `ACC-SIGN-OR-BOUND-CHECK-MISSING`
    - broken invariant: A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
- **URGENCY 81.07 / EVIDENCE_CONFIDENCE 90.4** — evidence level `L4_GUARD_REVIEW`
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 25.0/25 · precondition match 11.07/15
- **Why the clock is hot:**
    - ZetaChain runs a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED. The defect is in the chain's own stack, not in any one protocol deployed on it.
    - 14 protocols above the floor sit on this chain, holding $36,688,623 between them. They are the exposure, not 14 separate candidates -- one chain fix closes all of them.
    - reachability: 3 precondition(s) present at L4_GUARD_REVIEW, no guard found in the reviewed path
    - recency: technique public 44d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin ZetaChain's running github.com/cosmos/evm version AND query live module params for the enabled static precompile set. Do not infer either from release notes; a vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 9. TAC (chain-level) — Tier 2 — URGENCY 81.07

- **Chain-level candidate:** `TAC` — the defect is in the chain's own stack. **3 protocols** above the floor are exposed; one chain fix closes all of them.
    - most exposed: `yieldfi`, `carbon-defi`, `satlayer`
- **DefiLlama:** https://defillama.com/chain/TAC
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $13,092,188
- **Matched family:** `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`
    - broken invariant: Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.
- **URGENCY 81.07 / EVIDENCE_CONFIDENCE 90.4** — evidence level `L4_GUARD_REVIEW`
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 25.0/25 · precondition match 11.07/15
- **Why the clock is hot:**
    - TAC runs a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED. The defect is in the chain's own stack, not in any one protocol deployed on it.
    - 3 protocols above the floor sit on this chain, holding $13,092,188 between them. They are the exposure, not 3 separate candidates -- one chain fix closes all of them.
    - reachability: 3 precondition(s) present at L4_GUARD_REVIEW, no guard found in the reviewed path
    - recency: technique public 78d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin TAC's running github.com/cosmos/evm version AND query live module params for the enabled static precompile set. Do not infer either from release notes; a vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Every identifier derived or verified against the factory/registry (kills the pair); Routing restricted to an immutable venue allowlist
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 10. Nibiru (chain-level) — Tier 2 — URGENCY 76.57

- **Chain-level candidate:** `Nibiru` — the defect is in the chain's own stack. **8 protocols** above the floor are exposed; one chain fix closes all of them.
    - most exposed: `steer-protocol`, `ichi`, `layerbank`, `eris-protocol`, `prdt`, `sai`, `astrovault`, `mim-swap`
- **DefiLlama:** https://defillama.com/chain/Nibiru
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $34,225,642
    - relative of **abracadabra-spell** via version sibling — that sibling is *never materially hit* and holds $4,827,737 now
- **Matched family:** `AUTH-ZERO-ADDRESS-ACCEPTED`
    - broken invariant: Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
- **URGENCY 76.57 / EVIDENCE_CONFIDENCE 85.4** — evidence level `L4_GUARD_REVIEW`
    - remediation gap 28/40 · technique recency+propagation 14.0/20 · reachable live value 25.0/25 · precondition match 9.57/15
- **Why the clock is hot:**
    - Nibiru runs a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED. The defect is in the chain's own stack, not in any one protocol deployed on it.
    - 8 protocols above the floor sit on this chain, holding $34,225,642 between them. They are the exposure, not 8 separate candidates -- one chain fix closes all of them.
    - reachability: 3 precondition(s) present at L4_GUARD_REVIEW, no guard found in the reviewed path
    - recency: technique public 91d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin Nibiru's running github.com/cosmos/evm version AND query live module params for the enabled static precompile set. Do not infer either from release notes; a vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 11. Evmos (chain-level) — Tier 2 — URGENCY 71.38

- **Chain-level candidate:** `Evmos` — the defect is in the chain's own stack. **6 protocols** above the floor are exposed; one chain fix closes all of them.
    - most exposed: `steer-protocol`, `flokifi-locker`, `ichi`, `autofarm`, `stride`, `photonswap-finance`
- **DefiLlama:** https://defillama.com/chain/Evmos
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $52,346,636
- **Matched family:** `ACC-DONATION-UNACCOUNTED-BALANCE`
    - broken invariant: A share price, exchange rate or totalAssets must be a function of value the protocol accounted for on entry. Reading a raw balance makes any direct transfer into the accounting boundary an unpriced increase in every holder's claim.
- **URGENCY 71.38 / EVIDENCE_CONFIDENCE 63.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 20.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - Evmos runs a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED. The defect is in the chain's own stack, not in any one protocol deployed on it.
    - 6 protocols above the floor sit on this chain, holding $52,346,636 between them. They are the exposure, not 6 separate candidates -- one chain fix closes all of them.
    - reachability: 2 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 52d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin Evmos's running github.com/cosmos/evm version AND query live module params for the enabled static precompile set. Do not infer either from release notes; a vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** totalAssets derived from an internal counter, not balanceOf (kills the pair); Rate is monotonic and rate-limited per block; Inbound transfers to the accounting boundary are rejected or swept to a reserve
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 12. Saga (chain-level) — Tier 2 — URGENCY 71.38

- **Chain-level candidate:** `Saga` — the defect is in the chain's own stack. **2 protocols** above the floor are exposed; one chain fix closes all of them.
    - most exposed: `steer-protocol`, `yieldfi`
- **DefiLlama:** https://defillama.com/chain/Saga
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $32,022,154
- **Matched family:** `ACC-DONATION-UNACCOUNTED-BALANCE`
    - broken invariant: A share price, exchange rate or totalAssets must be a function of value the protocol accounted for on entry. Reading a raw balance makes any direct transfer into the accounting boundary an unpriced increase in every holder's claim.
- **URGENCY 71.38 / EVIDENCE_CONFIDENCE 69.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 20.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - Saga runs a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED. The defect is in the chain's own stack, not in any one protocol deployed on it.
    - 2 protocols above the floor sit on this chain, holding $32,022,154 between them. They are the exposure, not 2 separate candidates -- one chain fix closes all of them.
    - reachability: 2 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 52d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin Saga's running github.com/cosmos/evm version AND query live module params for the enabled static precompile set. Do not infer either from release notes; a vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** totalAssets derived from an internal counter, not balanceOf (kills the pair); Rate is monotonic and rate-limited per block; Inbound transfers to the accounting boundary are rejected or swept to a reserve
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 13. Injective (chain-level) — Tier 2 — URGENCY 45

- **Chain-level candidate:** `Injective` — the defect is in the chain's own stack. **17 protocols** above the floor are exposed; one chain fix closes all of them.
    - most exposed: `hydro-lst`, `astroport`, `stride`, `hydro-lending`, `trustake`, `neptune-finance`, `balanced-exchange`, `eris-protocol`
- **DefiLlama:** https://defillama.com/chain/Injective
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $45,873,068
- **Matched family:** `AUTH-MISSING-ON-VALUE-MOVING-PATH`
    - broken invariant: Every function that moves value or rebinds a privileged address must require a role the caller cannot obtain.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 20.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - Injective runs a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED. The defect is in the chain's own stack, not in any one protocol deployed on it.
    - 17 protocols above the floor sit on this chain, holding $45,873,068 between them. They are the exposure, not 17 separate candidates -- one chain fix closes all of them.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 30d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin Injective's running github.com/cosmos/evm version AND query live module params for the enabled static precompile set. Do not infer either from release notes; a vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Every value-moving selector reverts for an unprivileged caller in simulation (kills the pair); Contract holds no value and controls no role
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 14. Dymension (chain-level) — Tier 2 — URGENCY 45

- **Chain-level candidate:** `Dymension` — the defect is in the chain's own stack. **1 protocols** above the floor are exposed; one chain fix closes all of them.
    - most exposed: `stride`
- **DefiLlama:** https://defillama.com/chain/Dymension
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $5,745,325
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - Dymension runs a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED. The defect is in the chain's own stack, not in any one protocol deployed on it.
    - 1 protocols above the floor sit on this chain, holding $5,745,325 between them. They are the exposure, not 1 separate candidates -- one chain fix closes all of them.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin Dymension's running github.com/cosmos/evm version AND query live module params for the enabled static precompile set. Do not infer either from release notes; a vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 15. Initia (chain-level) — Tier 2 — URGENCY 45

- **Chain-level candidate:** `Initia` — the defect is in the chain's own stack. **5 protocols** above the floor are exposed; one chain fix closes all of them.
    - most exposed: `cabal`, `initiadex`, `inertia-bridge`, `echelon-initia-bridge`, `milkyway-rollup-bridge`
- **DefiLlama:** https://defillama.com/chain/Initia
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $4,842,851
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - Initia runs a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED. The defect is in the chain's own stack, not in any one protocol deployed on it.
    - 5 protocols above the floor sit on this chain, holding $4,842,851 between them. They are the exposure, not 5 separate candidates -- one chain fix closes all of them.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin Initia's running github.com/cosmos/evm version AND query live module params for the enabled static precompile set. Do not infer either from release notes; a vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 16. Shido (chain-level) — Tier 2 — URGENCY 45

- **Chain-level candidate:** `Shido` — the defect is in the chain's own stack. **2 protocols** above the floor are exposed; one chain fix closes all of them.
    - most exposed: `shido-dex-v3`, `shido-dex-v2`
- **DefiLlama:** https://defillama.com/chain/Shido
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $729,653
- **Matched family:** `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`
    - broken invariant: A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 14.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - Shido runs a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED. The defect is in the chain's own stack, not in any one protocol deployed on it.
    - 2 protocols above the floor sit on this chain, holding $729,653 between them. They are the exposure, not 2 separate candidates -- one chain fix closes all of them.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 127d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin Shido's running github.com/cosmos/evm version AND query live module params for the enabled static precompile set. Do not infer either from release notes; a vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 17. HOPE Collateral — Tier 4 — URGENCY 66.57

- **Protocol:** `hope-collateral` · Basis Trading · Bitcoin, Ethereum
- **DefiLlama:** https://defillama.com/protocol/hope-collateral
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $1,604,842
    - relative of **hope-lend** via version sibling — that sibling is *drained or dead* and holds $158 now
- **Matched family:** `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`
    - broken invariant: A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
- **URGENCY 66.57 / EVIDENCE_CONFIDENCE 90.4** — evidence level `L4_GUARD_REVIEW`
    - remediation gap 28/40 · technique recency+propagation 4.0/20 · reachable live value 25.0/25 · precondition match 9.57/15
- **Why the clock is hot:**
    - version sibling of hope-lend, exploited on 2023-10-18; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $1,604,842.
    - reachability: 3 precondition(s) present at L4_GUARD_REVIEW, no guard found in the reviewed path
    - recency: technique public 1044d ago; 3 siblings
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 18. Allbridge Classic — Tier 4 — URGENCY 63.0

- **Protocol:** `allbridge-classic` · Bridge · Ethereum, Solana, Terra, Binance, Near
- **DefiLlama:** https://defillama.com/protocol/allbridge-classic
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $1,057,520
    - relative of **allbridge-core** via version sibling — that sibling is *drained or dead* and holds $322,827 now
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 63.0 / EVIDENCE_CONFIDENCE 77.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 14.0/20 · reachable live value 12.0/25 · precondition match 9.0/15
- **Why the clock is hot:**
    - version sibling of allbridge-core, exploited on 2026-07-19; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $1,057,520.
    - reachability: 2 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 39d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://app.allbridge.io
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 19. Balancer CoW AMM — Tier 4 — URGENCY 57.0

- **Protocol:** `balancer-cow-amm` · Dexs · xDai, Ethereum, Arbitrum, Base
- **DefiLlama:** https://defillama.com/protocol/balancer-cow-amm
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $59,804
    - relative of **balancer-v2** via version sibling — that sibling is *drained or dead* and holds $28,168,365 now
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 57.0 / EVIDENCE_CONFIDENCE 77.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 8.0/20 · reachable live value 12.0/25 · precondition match 9.0/15
- **Why the clock is hot:**
    - version sibling of balancer-v2, exploited on 2025-11-03; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $59,804.
    - reachability: 2 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 297d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://balancer.fi
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 20. Paraluni Dex — Tier 4 — URGENCY 55.0

- **Protocol:** `paraluni-dex` · Dexs · Binance
- **DefiLlama:** https://defillama.com/protocol/paraluni-dex
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $323,498
    - relative of **paraluni-masterchef** via version sibling — that sibling is *drained or dead* and holds $2,641 now
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 55.0 / EVIDENCE_CONFIDENCE 77.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 12.0/25 · precondition match 9.0/15
- **Why the clock is hot:**
    - version sibling of paraluni-masterchef, exploited on 2022-03-13; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $323,498.
    - reachability: 2 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 1628d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://paraluni.org
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 21. HOPE Swap — Tier 4 — URGENCY 55.0

- **Protocol:** `hope-swap` · Dexs · Ethereum
- **DefiLlama:** https://defillama.com/protocol/hope-swap
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $114,227
    - relative of **hope-lend** via version sibling — that sibling is *drained or dead* and holds $158 now
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 55.0 / EVIDENCE_CONFIDENCE 77.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 12.0/25 · precondition match 9.0/15
- **Why the clock is hot:**
    - version sibling of hope-lend, exploited on 2023-10-18; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $114,227.
    - reachability: 3 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 1044d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 22. WEMIX.FI Staking — Tier 4 — URGENCY 45

- **Protocol:** `wemix.fi-staking` · Staking Pool · WEMIX
- **DefiLlama:** https://defillama.com/protocol/wemix.fi-staking
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $19,923,463
    - relative of **wemix.fi-lend** via version sibling — that sibling is *drained or dead* and holds $1,971 now
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 14.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - version sibling of wemix.fi-lend, exploited on 2026-07-26; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $19,923,463.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 32d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://wemix.fi
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 23. Summer.fi Pro — Tier 4 — URGENCY 45

- **Protocol:** `summer.fi-pro` · CDP Manager · Ethereum, Arbitrum, Optimism, Base
- **DefiLlama:** https://defillama.com/protocol/summer.fi-pro
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $17,019,561
    - relative of **lazy-summer-protocol** via version sibling — that sibling is *drained or dead* and holds $1,134 now
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 14.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - version sibling of lazy-summer-protocol, exploited on 2026-07-05; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $17,019,561.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 53d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://summer.fi/earn?referralCode=2001317
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 24. TermFinance Lend — Tier 4 — URGENCY 45

- **Protocol:** `termfinance-lend` · Lending · Ethereum, Arbitrum, Plasma, Base, Avalanche
- **DefiLlama:** https://defillama.com/protocol/termfinance-lend
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $5,167,046
    - relative of **termfinance-vaults** via version sibling — that sibling is *drained or dead* and holds $1,608,407 now
- **Matched family:** `ORACLE-STALE-OR-SILENT-FALLBACK`
    - broken invariant: A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - version sibling of termfinance-vaults, exploited on 2026-08-23; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $5,167,046.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 4d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Disclosure channel, if public:** https://term.finance
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 25. WEMIX Concentrated Range Deposit — Tier 4 — URGENCY 45

- **Protocol:** `wemix-concentrated-range-deposit` · Dexs · WEMIX
- **DefiLlama:** https://defillama.com/protocol/wemix-concentrated-range-deposit
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $2,169,898
    - relative of **wemix.fi-lend** via version sibling — that sibling is *drained or dead* and holds $1,971 now
- **Matched family:** `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`
    - broken invariant: A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 12.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - version sibling of wemix.fi-lend, exploited on 2026-07-26; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $2,169,898.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 32d ago; 3 siblings
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Disclosure channel, if public:** https://wemix.fi
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 26. WEMIX Full Range Deposit — Tier 4 — URGENCY 45

- **Protocol:** `wemix-full-range-deposit` · Dexs · WEMIX
- **DefiLlama:** https://defillama.com/protocol/wemix-full-range-deposit
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $824,781
    - relative of **wemix.fi-lend** via version sibling — that sibling is *drained or dead* and holds $1,971 now
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 14.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - version sibling of wemix.fi-lend, exploited on 2026-07-26; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $824,781.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 32d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://wemix.fi
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 27. Bonzo Vaults — Tier 4 — URGENCY 45

- **Protocol:** `bonzo-vaults` · Liquidity Manager · Hedera
- **DefiLlama:** https://defillama.com/protocol/bonzo-vaults
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $425,571
    - relative of **bonzo-lend** via version sibling — that sibling is *drained or dead* and holds $4,199,410 now
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 14.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - version sibling of bonzo-lend, exploited on 2026-07-11; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $425,571.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 47d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://bonzo.finance/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 28. WEMIX Liquid Staking — Tier 4 — URGENCY 45

- **Protocol:** `wemix-liquid-staking` · Liquid Staking · WEMIX
- **DefiLlama:** https://defillama.com/protocol/wemix-liquid-staking
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $254,158
    - relative of **wemix.fi-lend** via version sibling — that sibling is *drained or dead* and holds $1,971 now
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 14.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - version sibling of wemix.fi-lend, exploited on 2026-07-26; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $254,158.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 32d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://wemix.fi/en/liquid-staking
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 29. Cozy Earn — Tier 4 — URGENCY 42.38

- **Protocol:** `cozy-earn` · Insurance · Ethereum
- **DefiLlama:** https://defillama.com/protocol/cozy-earn
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $1,043,001
    - relative of **cozy-v2** via version sibling — that sibling is *drained or dead* and holds $172,358 now
- **Matched family:** `AUTH-MISSING-ON-VALUE-MOVING-PATH`
    - broken invariant: Every function that moves value or rebinds a privileged address must require a role the caller cannot obtain.
- **URGENCY 42.38 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 8.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - version sibling of cozy-v2, exploited on 2025-08-30; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $1,043,001.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 362d ago; 4-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Every value-moving selector reverts for an unprivileged caller in simulation (kills the pair); Contract holds no value and controls no role
- **Disclosure channel, if public:** https://www.cozy.finance
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 30. Typus DOV — Tier 4 — URGENCY 42.38

- **Protocol:** `typus-dov` · Options Vault · Sui
- **DefiLlama:** https://defillama.com/protocol/typus-dov
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $996,302
    - relative of **typus-perp** via version sibling — that sibling is *drained or dead* and holds $16,004 now
- **Matched family:** `AUTH-MISSING-ON-VALUE-MOVING-PATH`
    - broken invariant: Every function that moves value or rebinds a privileged address must require a role the caller cannot obtain.
- **URGENCY 42.38 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 8.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - version sibling of typus-perp, exploited on 2025-10-15; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $996,302.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 316d ago; 4-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Every value-moving selector reverts for an unprivileged caller in simulation (kills the pair); Contract holds no value and controls no role
- **Disclosure channel, if public:** https://typus.finance
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 31. Velar AMM — Tier 4 — URGENCY 42.38

- **Protocol:** `velar-amm` · Dexs · Stacks
- **DefiLlama:** https://defillama.com/protocol/velar-amm
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $401,394
    - relative of **velar-perps** via version sibling — that sibling is *drained or dead* and holds $13,986 now
- **Matched family:** `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`
    - broken invariant: Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.
- **URGENCY 42.38 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 8.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - version sibling of velar-perps, exploited on 2026-02-19; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $401,394.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 189d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Every identifier derived or verified against the factory/registry (kills the pair); Routing restricted to an immutable venue allowlist
- **Disclosure channel, if public:** https://velar.com/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 32. Typus Safu — Tier 4 — URGENCY 42.38

- **Protocol:** `typus-safu` · Yield · Sui
- **DefiLlama:** https://defillama.com/protocol/typus-safu
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $191,194
    - relative of **typus-perp** via version sibling — that sibling is *drained or dead* and holds $16,004 now
- **Matched family:** `ACC-ZERO-SUPPLY-INFLATION`
    - broken invariant: The first depositor must not be able to set an arbitrary asset-per-share ratio, and no operation may drive supply low enough to restore that branch.
- **URGENCY 42.38 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 8.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - version sibling of typus-perp, exploited on 2025-10-15; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $191,194.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 316d ago; 4-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Dead shares minted at creation (kills the pair); Vault creation is permissioned and every vault is seeded; Virtual offset present in the deployed bytecode
- **Disclosure channel, if public:** https://typus.finance/safu
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 33. ApertureSwap — Tier 4 — URGENCY 42.38

- **Protocol:** `apertureswap` · Dexs · Manta
- **DefiLlama:** https://defillama.com/protocol/apertureswap
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $51,433
    - relative of **aperture-lm** via version sibling — that sibling is *drained or dead* and holds $12,779 now
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 42.38 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 8.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - version sibling of aperture-lm, exploited on 2026-01-25; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $51,433.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 214d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 34. Pando Leaf — Tier 4 — URGENCY 40.75

- **Protocol:** `pando-leaf` · CDP · Mixin
- **DefiLlama:** https://defillama.com/protocol/pando-leaf
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $11,396,231
    - relative of **pando-rings** via version sibling — that sibling is *drained or dead* and holds $6,076,001 now
- **Matched family:** `ORACLE-STALE-OR-SILENT-FALLBACK`
    - broken invariant: A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
- **URGENCY 40.75 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - version sibling of pando-rings, exploited on 2022-11-06; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $11,396,231.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 1390d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Disclosure channel, if public:** https://pando.im
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 35. WOOFi Earn — Tier 4 — URGENCY 40.38

- **Protocol:** `woofi-earn` · Yield · Arbitrum, Optimism, Base, Avalanche, Polygon
- **DefiLlama:** https://defillama.com/protocol/woofi-earn
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $2,694,195
    - relative of **woofi-swap** via version sibling — that sibling is *drained or dead* and holds $2,418,019 now
- **Matched family:** `ACC-ZERO-SUPPLY-INFLATION`
    - broken invariant: The first depositor must not be able to set an arbitrary asset-per-share ratio, and no operation may drive supply low enough to restore that branch.
- **URGENCY 40.38 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - version sibling of woofi-swap, exploited on 2024-03-05; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $2,694,195.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 905d ago; 4-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Dead shares minted at creation (kills the pair); Vault creation is permissioned and every vault is seeded; Virtual offset present in the deployed bytecode
- **Disclosure channel, if public:** https://fi.woo.org/earn
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 36. Nirvana V2 — Tier 4 — URGENCY 40.38

- **Protocol:** `nirvana-v2` · Reserve Currency · Solana
- **DefiLlama:** https://defillama.com/protocol/nirvana-v2
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $2,586,219
    - relative of **nirvana-v1** via version sibling — that sibling is *drained or dead* and holds $3 now
- **Matched family:** `AUTH-MISSING-ON-VALUE-MOVING-PATH`
    - broken invariant: Every function that moves value or rebinds a privileged address must require a role the caller cannot obtain.
- **URGENCY 40.38 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - version sibling of nirvana-v1, exploited on 2022-07-28; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $2,586,219.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 1491d ago; 4-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Every value-moving selector reverts for an unprivileged caller in simulation (kills the pair); Contract holds no value and controls no role
- **Disclosure channel, if public:** https://www.nirvana.finance/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 37. 4Swap — Tier 4 — URGENCY 40.38

- **Protocol:** `4swap` · Dexs · Mixin
- **DefiLlama:** https://defillama.com/protocol/4swap
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $494,167
    - relative of **pando-rings** via version sibling — that sibling is *drained or dead* and holds $6,076,001 now
- **Matched family:** `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`
    - broken invariant: Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.
- **URGENCY 40.38 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - version sibling of pando-rings, exploited on 2022-11-06; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $494,167.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 1390d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Every identifier derived or verified against the factory/registry (kills the pair); Routing restricted to an immutable venue allowlist
- **Disclosure channel, if public:** https://pando.im
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 38. Basin Exchange — Tier 4 — URGENCY 40.38

- **Protocol:** `basin-exchange` · Dexs · Arbitrum, Ethereum
- **DefiLlama:** https://defillama.com/protocol/basin-exchange
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $438,854
    - relative of **beanstalk** via version sibling — that sibling is *drained or dead* and holds $0 now
- **Matched family:** `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`
    - broken invariant: Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.
- **URGENCY 40.38 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - version sibling of beanstalk, exploited on 2022-04-17; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $438,854.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 1593d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Every identifier derived or verified against the factory/registry (kills the pair); Routing restricted to an immutable venue allowlist
- **Disclosure channel, if public:** https://basin.exchange
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 39. Cetus DLMM — Tier 4 — URGENCY 40.38

- **Protocol:** `cetus-dlmm` · Dexs · Sui
- **DefiLlama:** https://defillama.com/protocol/cetus-dlmm
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $433,423
    - relative of **cetus-clmm** via version sibling — that sibling is *drained or dead* and holds $25,461,685 now
- **Matched family:** `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`
    - broken invariant: Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.
- **URGENCY 40.38 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - version sibling of cetus-clmm, exploited on 2025-05-22; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $433,423.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 462d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Every identifier derived or verified against the factory/registry (kills the pair); Routing restricted to an immutable venue allowlist
- **Disclosure channel, if public:** https://www.cetus.zone
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 40. SwapX Algebra — Tier 4 — URGENCY 40.38

- **Protocol:** `swapx-algebra` · Dexs · Sonic
- **DefiLlama:** https://defillama.com/protocol/swapx-algebra
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $404,170
    - relative of **swapx-v2** via version sibling — that sibling is *drained or dead* and holds $43,833 now
- **Matched family:** `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`
    - broken invariant: Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.
- **URGENCY 40.38 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - version sibling of swapx-v2, exploited on 2023-02-27; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $404,170.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 1277d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Every identifier derived or verified against the factory/registry (kills the pair); Routing restricted to an immutable venue allowlist
- **Disclosure channel, if public:** https://swapx.fi/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 41. Voltage V4 — Tier 4 — URGENCY 40.38

- **Protocol:** `voltage-v4` · Dexs · Fuse
- **DefiLlama:** https://defillama.com/protocol/voltage-v4
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $186,233
    - relative of **voltage-v3** via version sibling — that sibling is *drained or dead* and holds $550 now
- **Matched family:** `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`
    - broken invariant: Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.
- **URGENCY 40.38 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - version sibling of voltage-v3, exploited on 2025-03-18; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $186,233.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 527d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Every identifier derived or verified against the factory/registry (kills the pair); Routing restricted to an immutable venue allowlist
- **Disclosure channel, if public:** https://app.voltage.finance/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 42. Velocore V1 — Tier 4 — URGENCY 40.38

- **Protocol:** `velocore-v1` · Dexs · zkSync Era
- **DefiLlama:** https://defillama.com/protocol/velocore-v1
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $126,572
    - relative of **velocore-v2** via version sibling — that sibling is *drained or dead* and holds $1,175 now
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 40.38 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - version sibling of velocore-v2, exploited on 2024-06-02; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $126,572.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 816d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 43. Voltage Liquid Staking — Tier 4 — URGENCY 40.38

- **Protocol:** `voltage-liquid-staking` · Liquid Staking · Fuse
- **DefiLlama:** https://defillama.com/protocol/voltage-liquid-staking
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $86,834
    - relative of **voltage-v3** via version sibling — that sibling is *drained or dead* and holds $550 now
- **Matched family:** `PROOF-VERIFICATION-BYPASSED`
    - broken invariant: A withdrawal or mint gated by a proof must verify that proof against the correct verifying key, over all the public inputs that bind the action, and must reject when any component is absent.
- **URGENCY 40.38 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - version sibling of voltage-v3, exploited on 2025-03-18; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $86,834.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 527d ago; 6-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Verifying key immutable and attested (kills the misconfiguration shape); No alternative release path exists (enumerate selectors)
- **Disclosure channel, if public:** https://app.voltage.finance/#/stake
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

---

## Demoted: well-resourced families

**69 protocols** were removed from the hot tiers because the family they belong to holds more than $100M across its deployments. A team at that scale retains security staff and patches a public issue fast, so it is usually not the save — the edge is the small, neglected, or forgotten deployment on the same unpatched version.

This is measured, not a name list: across hot-tier candidates the median family holds **$5.8M** and the 90th percentile **$168M**, while the Aave family holds **$18.1bn**. They are named here rather than silently dropped.

| Protocol | Own live value | Family holds | Family |
|---|---:|---:|---|
| `aave-v1` | $7,722,971 | $18,131,278,645 | aave |
| `aave-arc` | $57,264 | $18,131,278,645 | aave |
| `aave-aptos` | $308,734 | $18,131,278,645 | aave |
| `morpho-optimizer-aavev2` | $139,080 | $9,465,990,395 | morpho |
| `morpho-midnight` | $3,252,819 | $9,465,990,395 | morpho |
| `hamilton-lane-senior-credit-opportunities-securitize-fund` | $4,296,646 | $4,971,214,813 | securitize |
| `ethena-tsusde` | $3,195,207 | $4,528,282,469 | ethena |
| `justlend-v2` | $1,508,942 | $3,689,401,963 | justlend |
| `uniswap-v1` | $3,986,812 | $3,470,812,968 | uniswap |
| `jupiter-offerbook` | $1,238,334 | $2,447,601,942 | jupiter |
| `jupiter-prediction` | $471,341 | $2,447,601,942 | jupiter |
| `jupiter-lend-dex` | $7,636,832 | $2,447,601,942 | jupiter |
| `pancakeswap-stableswap` | $3,811,177 | $2,297,217,430 | pancakeswap |
| `lista-rwa` | $4,063,619 | $1,830,436,597 | lista-dao |
| `lisaster` | $1,196,281 | $1,830,436,597 | lista-dao |
| `tinlake` | $61,319 | $1,640,261,226 | centrifuge |
| `curve-llamalend-v2` | $2,057,612 | $1,558,788,044 | curve-finance |
| `compound-v1` | $3,252,870 | $1,529,183,884 | compound-finance |
| `kinetiq-launch` | $3,977,467 | $1,278,913,431 | kinetiq |
| `venus-isolated-pools` | $1,075,798 | $1,274,890,282 | venus |
| `venus-flux` | $3,421,097 | $1,274,890,282 | venus |
| `kernel` | $1,361,877 | $1,151,287,222 | kerneldao |
| `jito-restaking` | $17,577,871 | $1,036,770,476 | jito |
| `solv-vesting` | $142,311 | $866,896,958 | solv-protocol |
| `solv-rwa` | $9,001,900 | $866,896,958 | solv-protocol |

---

## Withheld by the no-repetition ledger — but now classified Tier 1–2

These **4** protocols were handed over in earlier runs and are excluded from the list above. They are named here rather than silently dropped because the ranking axis changed underneath them: they were delivered as likelihood candidates and now classify as hot clocks. Withholding a Tier-1 item because it was once served cold would be the wrong call, so this is your decision, not mine.

| Protocol | Tier | URGENCY | Family | Live value | First delivered |
|---|---:|---:|---|---:|---|
| [SIR](https://defillama.com/protocol/sir) | 1 | 68.07 | `SIG-VERIFIER-DEFEATABLE` | $109,365 | `2ce88d1` |
| [Nomad](https://defillama.com/protocol/nomad) | 1 | 66.57 | `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET` | $359,084 | `1ad898f` |
| [UwU Lend](https://defillama.com/protocol/uwu-lend) | 1 | 66.57 | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | $94,541 | `3bc30a7` |
| [Agave](https://defillama.com/protocol/agave) | 1 | 40.75 | `ORACLE-STALE-OR-SILENT-FALLBACK` | $89,754 | `7d49c12` |

---

## Limits of this ranking

- **No fix-in-artifact check was run.** That is the single highest-value next action and it is what separates 28 points from 40. Until it runs, no row here is `UNREMEDIATED_KNOWN`.
- **Tier 3 is barely populated (0 protocols).** The only dependency this run can evidence is the *declared oracle*, and only where the provider's user population is small enough for one incident to mean something. Backing, collateral, LP and vault-share holdings are **not** resolved — the Blend case (contracts sound, backstop composed of another protocol's LP) is exactly what this run cannot yet see.

- **Fork lineage is weak, and that caps Tier 1.** DefiLlama populates `forkedFrom` on **6 protocols out of 8,135**, so it carries nothing. The only code-lineage evidence available is `parentProtocol` (version siblings), which is why Tier 1 holds 6 and Tier 4 holds 83 — the relatives are real but the link is a sibling relationship, not proven shared code.
- **A grouping this pass rejected.** Grouping protocols by shared adapter module first produced a 7-member "fork cluster" around a victim, headed by a $19.3M protocol. The shared module was `dummy.js` — DefiLlama's placeholder for *no adapter*, carried by 1,124 protocols including Fantom, 0x, Jupiter and OpenSea Seaport. Not shared code at all. Placeholder modules and groups above 12 members are now rejected.
- **The capability that would fix this: runtime bytecode similarity.** Hashing deployed code across the probed population would find literal clones of a victim — the "byte-similar" half of Tier 4 that lineage metadata cannot reach. Not run in this pass.
- **Tier 1 rests on DefiLlama's incident dataset plus this run's corpus.** A protocol with no recorded incident may simply have no record.

- **Value at risk sits beside the score and never inside it.** A real finding on $60k of dust is a low-value save; check the column before spending time.

- Read-only throughout. No transaction, no calldata, no credential use.

