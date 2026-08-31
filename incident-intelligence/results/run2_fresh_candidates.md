# Run 2 — fresh-window re-crawl and new candidates

> **Discovery stage, same disclaimer as `candidates_by_urgency.md`.** Nothing here says any
> protocol is exploitable. Each entry is a high-urgency *audit candidate*: a fresh public
> incident proves a technique, and named evidence says an un-hit relative still holds money on
> the same or a shared mechanism. A candidate is a triage order, never an exploit probability.

**Run:** 2026-08-29. **Pinned:** ETH `#25858924`, Base `#50596624`, 2026-08-29T05:49:54Z.
**Chain access:** read-only throughout.

This run re-crawls the SlowMist Hacked index with the window re-anchored on today
(2026-02-28 → 2026-08-29, one week further forward than run 1) and diffs against the run-1
corpus. It is deliberately **narrow**: it adds only what the fresh incidents newly teach, and
it does **not** re-derive the 43 candidates already in `candidates_by_urgency.md`.

---

## 1. What the re-crawl found

- Boundary **re-proven** at page 12 (a full page with zero in-window rows, every row older than
  the window start). Crawl log: `sources/slowmist_run2/crawl_log_all.json`.
- **11 in-window incidents are new** since the run-1 corpus (`sources/slowmist_run2/fresh_rows.json`).
  All 11 are in-scope on-chain root causes (no off-chain key compromise). Classified in
  `incidents/run2_fresh.jsonl`.

### The prior run already caught the three biggest fresh hits — this is the validation the operator asked for

If this screen had been run before each hack, would it have flagged the target? For the three
largest fresh in-scope losses, the prior run **already had them**:

| Fresh incident | Loss | Already in prior run? |
|---|---:|---|
| **Term Finance** — governance takeover, disable timelock, drain | $8.5M | **Yes** — `termfinance-vaults` (ledger) + `termfinance-lend` (current urgency list). Family `GOV-CHEAP-CONTROL-NO-TIMELOCK`. |
| **Moonwell** — thin-liquidity MAMO collateral price manipulation | $8.79M | **Yes** — `moonwell-lending` / `moonwell-vaults` (ledger). |
| **TAC** — Cosmos EVM precompile drain | $7.5M | **Yes** — Cosmos-EVM precompile cluster is Tier-2 in the current urgency list; TAC is the cluster being exploited live. |

That is the point of the exercise landing: the mechanism families the prior run built were the
right ones, and the un-hit-relative framing put the names on the list before the clock started.

---

## 2. New candidates and leads (not in the existing 43)

Ranked by how much I could establish here, not by loss size. Two are EVM and verified on-chain;
three are non-EVM or shared-template classes I characterized from public source + the incident
but could not fork-verify in this environment (said plainly per finding).

### A. Arrakis V1 / G-UNI vault fleet — VERIFIED on-chain, but honestly small money

**Tier 1 (un-hit relative on the same code as a hit sibling). NEW — not in ledger or urgency list.**

- **Incident (evidence):** 2026-08-23, the Arrakis V1 / G-UNI **ENS-WETH** vault
  (`0x7c687f775a3b73bbab0e15832f24caab5d53bdde`) was drained via Uniswap V3 spot-price
  manipulation for ~2.94 WETH.
- **Root cause, read at source:** `ArrakisVaultV1.mint()`/`burn()` value the position through
  `getUnderlyingBalances()` → `pool.slot0()` (instantaneous tick), with **no TWAP or deviation
  guard**. The TWAP path (`_checkSlippage` → `pool.observe()`) is reachable **only from
  `rebalance()`** — the guard sits on a sibling path the attacker never touches. Evidence:
  `sources/arrakis/impl_flat.sol` lines 1763–1900 (mint/burn) and 2452–2481 (`_checkSlippage`).
- **Fleet, enumerated from the factory** (`0xea1aff9dbffd1580f6b81a3ad3589e66652db7d9`):
  **105 vaults**, 4 implementations, **all the same `ArrakisVaultV1`/`GUniPool` family**
  (identical `slot0()`×6–7, `observe()`×3 profile). 52 hold supply today.
  Evidence: `sources/arrakis/vaults.json`, `sources/arrakis/vault_tvl.json`.
- **The honest measurement kills the size story.** The whole V1 fleet holds **~$1.2M on
  mainnet**, and the largest vaults are **stablecoin pairs** (DAI/USDC $476k, DAI/USDC $307k,
  USDC/USDT) where skewing a deep near-1:1 pool yields almost no mispricing profit. The largest
  **volatile** un-hit sibling is **ETH2x-FLI/WETH ~$198k** (impl `0xaf4ed…`, same family), then
  USDC/FLOAT ~$66k, agEUR/USDC ~$30k, icETH/WETH ~$23k. DefiLlama's ~$30M "Arrakis" mainnet TVL
  is almost entirely **V2/Modular**, which values differently and is *not* this code.
- **Why it still belongs on the list:** the technique went public 6 days ago, V1 was never
  patched (the fix was to move to V2), and the shared code is live. It is a real Tier-1 fleet —
  just a small one. Prefer the volatile-pair siblings; the stablecoin vaults are near-unexploitable.
- **Decisive check:** for a volatile-pair V1 vault, confirm `mint()/burn()` still route valuation
  through `slot0()` at the live impl (they do at head) and price the flash-loan cost to move the
  specific Uniswap V3 pool's tick across the vault range vs. the extractable mix. **Residual not
  done here:** the V1 factories on Polygon/Optimism/Arbitrum/Base were **not** enumerated — same
  code, unknown extra TVL; that is the next cheap step.

### B. LayerZero OApp + arbitrary-call → delegate hijack → unbacked mint — NEW class, mechanism VERIFIED

**New family `LZ-OAPP-ARBITRARY-CALL-DELEGATE-HIJACK`. The forward lead of this run.**

- **Incident (evidence):** 2026-08-21, The Sandbox **SAND** OFT on Base/BNB. Attacker minted
  ~329T unbacked SAND and unlocked ~14.75M real SAND (~$675k) from the Ethereum adapter.
- **Root cause, read at source** (`sources/sandbox/sand_base_flat.sol`,
  `ERC20BasicApproveExtension.sol`): `approveAndCall(target, amount, data)` and `paidCall(...)`
  do **`target.call{value}(data)` from the token contract's own context**, guarded *only* by
  `doFirstParamEqualsAddress(data, msg.sender)`. That guard blocks a spoofed `transferFrom`, but
  **not** `endpoint.setDelegate(attacker)` — the attacker's own address legitimately *is* the
  first param. `OFTSand` is a LayerZero **OApp**, and `EndpointV2.setDelegate` keys the delegate
  by `msg.sender`. So `approveAndCall(endpoint, 0, setDelegate(attacker))` makes the **SAND OApp
  set the attacker as its own delegate** → attacker installs a malicious DVN / receive library →
  delivers a forged inbound OFT message → unbacked mint → bridge back → unlock the real backing.
- **Generalization (the fleet):** *any* LayerZero OApp/OFT that also exposes an **unprivileged
  arbitrary-target call** — `approveAndCall` / `paidCall` / `transferAndCall` (ERC-677) /
  `multicall` with an arbitrary target / a generic `execute` — is delegate-hijackable the same
  way, **regardless of who the current delegate is**, because the call originates from the OApp
  itself. Value at risk per token = the backing locked in its OFT adapter(s).
- **State of SAND:** contained — at head all `peers[eid]` are zero (bridge severed) and the
  delegate is a multisig. The OG SAND on Ethereum (`0x3845…`) and Polygon (`0xbbba…`) **have**
  `approveAndCall`/`paidCall` but are **not** OApps (`endpoint()` reverts), so they are not
  hijackable. The SAND deployment itself is spent; **the class is the live lead.**
- **Decisive screen (never run — highest-value next action):** intersect the **LayerZero OApp/OFT
  population** (has `endpoint()` + `peers()`) with contracts exposing an **arbitrary-target call
  method** reachable by an unprivileged caller. Any match holding/backing real value is a
  candidate at the severity of its adapter's locked balance. This is a mechanical, enumerable
  screen; it just requires the OApp set (LayerZero's deployment registry) crossed with a
  bytecode/source check for the call method.

### C. Rain card-stack signature-verification misrouting (Solana) — fleet is custodial money

**New family `SOLANA-SIG-VERIFY-INSTRUCTION-INDEX-MISROUTED`. Named, not fork-verified here.**

- **Incident:** 2026-08-28, **Avici** (Solana card platform), ~$500k from 1,685 users'
  card-collateral balances. Root cause (per multiple analyses): the second Ed25519 signature
  verification was **routed to the first instruction**, so the attacker's own signature was
  accepted a second time; `AddCollateralAdmin` then made the attacker admin of user collateral
  accounts, enabling `WithdrawCollateralAsset`. Explicitly **not** an upgrade-key compromise
  (upgrade authority unused since 2025-03).
- **Fleet:** SlowMist framed it as an **outdated shared Rain card contract "used by a few other
  programs."** Rain's card-issuing stack is deployed across many partners (per Rain: Avici, KAST,
  Offramp, Rhythmic, ether.fi cards) on **Solana / Tron / Stellar / Monad**. These hold custodial
  stablecoin card collateral — real user money, and a **shared-dependency fleet** exactly like the
  four highest-loss families the prior run had to backfill.
- **Decisive check:** for each Rain-partner card program, determine whether it runs the **patched**
  authorization/collateral program or the **outdated** version with the instruction-index
  misrouting in its signature check; confirm the Ed25519 verify is bound to the *correct*
  instruction index and cannot be satisfied by a self-signature. **Limitation:** Solana program
  verification (decompile + instruction-introspection reasoning) was not performed in this
  environment; this is a named lead with a concrete check, not a confirmed finding.

### D. Comet AMM same-asset-swap distinctness (Soroban / Stellar) — public-template fleet

**New family `AMM-SAME-ASSET-SWAP-NOT-DISTINCT` (the Lens-E distinctness mirror).**

- **Incident:** 2026-08-25, **CometDEX** (Comet AMM) BLND-USDC pool — Blend's backstop — drained
  ~$717k via a **USDC→USDC same-asset swap** looped ~36× on flash-loaned funds, corrupting
  weighted-pool reserve math. Stellar DeFi TVL fell ~60% ($270M→~$98M); Blend paused its backstop.
- **Root cause, from public source** (`CometDEX/comet-contracts-v1`): the top-level
  `swap_exact_amount_in` / `swap_exact_amount_out` do only `require_auth()` and TTL bumps — **no
  `token_in != token_out` check** at that layer (delegated to `execute_swap`, matching the reported
  cause).
- **Fleet:** Comet v1 is a **public Balancer-fork template** reused across Stellar DeFi (Blend
  backstop, "Smol" auto-Comet liquidity, other Comet pools). Un-hit relatives = other live Comet
  pools. Generalizes to **any weighted-pool AMM on a newer VM** (Soroban/Sui/Aptos/Solana) that
  fails to force `assetIn != assetOut` — the same cross-substrate blindness the audit method warns
  about.
- **Decisive check:** in each Comet deployment (and each non-EVM weighted-pool fork), confirm the
  swap entry rejects `token_in == token_out` before touching reserves. **Limitation:** Soroban
  fork-verification not performed here; the missing top-level check is confirmed from source.

### E. CCTP forged-message credit across integrators (EVM) — Lens B forgery

- **Incident:** 2026-08-19, **Allbridge** CCTP router, ~$190k. The attacker pre-registered a
  forged CCTP-style message weeks earlier (Circle `MessageTransmitterV2.sendMessage` on Polygon,
  claiming 1M USDC with **no burn**), got a valid attestation, then `receiveCctpMessage` on the
  Base Router **credited the message body as a real deposit** — it verified the attestation
  envelope but not that the source was a real `depositForBurn`.
- **Fleet:** CCTP integrators that credit off a **received message body** (generic
  `sendMessage`/`receiveMessage`) instead of binding the credit to a verified `DepositForBurn`/mint
  event. `allbridge-classic` is already in the urgency list; the **CCTP-router credit pattern is
  broader** and worth a dedicated screen.
- **Decisive check:** for each integrator calling CCTP `receiveMessage`, confirm the credited
  amount/asset is bound to a burn on the source domain, and that a plain `sendMessage` with an
  attacker-authored body cannot be replayed into a credit. Maps to existing family
  `BRIDGE-MESSAGE-NOT-BOUND-TO-SOURCE`.

### F. Legacy delegatecall-adapter proxy takeover (EVM) — forgotten code holding backing

- **Incident:** 2026-08-25, **Enjin** legacy ERC-1155 Crypto Items — storage-layout mismatch in
  delegate-call adapters + **unprotected `initialize`** let the attacker take over the Managed
  Delegate Proxy via `DELEGATECALL`, register a malicious adapter, move NFTs from ~52 wallets, and
  melt them to redeem backing ENJ.
- **Fleet / lead:** old delegatecall-adapter proxy systems that **still hold backing** and expose
  an unprotected initializer or permissionless adapter registration. Maps to existing families
  `UPGRADE-INITIALIZER-REACHABLE-LIVE` + `STORAGE-LAYOUT-COLLISION-PHANTOM-CREDIT`; the fresh proof
  is a reason to re-run those indicators against **legacy** deployments still holding value.

---

## 3. Handoff lines (CORE.md format)

```
TARGET=arrakis-v1-guni-fleet || TIER=1 || FAMILY=ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE || DECISIVE_CHECK=For a volatile-pair Arrakis V1/G-UNI vault, confirm mint()/burn() value via getUnderlyingBalances()->pool.slot0() with no TWAP/deviation (guard only on rebalance()), then price the flash-loan cost to move the specific UniV3 pool tick across the vault range vs the extractable token mix. Enumerate the Polygon/Optimism/Arbitrum/Base V1 factories too. || VALUE_AT_RISK=1200000 || PINNED=ETH#25858924 || MODULES=EVM || EVIDENCE=sources/arrakis/impl_flat.sol,sources/arrakis/vault_tvl.json
TARGET=layerzero-oapp-arbitrary-call || TIER=2 || FAMILY=LZ-OAPP-ARBITRARY-CALL-DELEGATE-HIJACK || DECISIVE_CHECK=Intersect the LayerZero OApp/OFT population (endpoint()+peers()) with contracts exposing an unprivileged arbitrary-target call (approveAndCall/paidCall/transferAndCall/multicall/execute); any match => attacker calls it with endpoint.setDelegate(attacker) to seize OApp config -> malicious DVN -> unbacked mint -> unlock adapter backing. Severity = adapter locked balance. || VALUE_AT_RISK=UNMEASURED_POPULATION || PINNED=BASE#50596624 || MODULES=EVM|BRIDGE || EVIDENCE=sources/sandbox/sand_base_flat.sol
TARGET=rain-card-stack || TIER=1 || FAMILY=SOLANA-SIG-VERIFY-INSTRUCTION-INDEX-MISROUTED || DECISIVE_CHECK=For each Rain-partner card program (Avici, KAST, Offramp, Rhythmic, ether.fi cards; Solana/Tron/Stellar/Monad) determine whether it runs the patched authorization/collateral program or the outdated version whose Ed25519 verify is routed to the wrong instruction index and satisfiable by a self-signature; confirm AddCollateralAdmin cannot be reached without a genuine second signer. || VALUE_AT_RISK=CUSTODIAL_CARD_COLLATERAL || PINNED=<solana slot at handoff> || MODULES=SOLANA
TARGET=comet-amm-forks || TIER=1 || FAMILY=AMM-SAME-ASSET-SWAP-NOT-DISTINCT || DECISIVE_CHECK=In each Comet v1 deployment and each non-EVM weighted-pool AMM fork, confirm the swap entry rejects token_in==token_out before mutating reserves. Un-hit relatives = live Comet pools other than the drained Blend backstop. || VALUE_AT_RISK=STELLAR_DEFI_POOLS || PINNED=<stellar ledger at handoff> || MODULES=SOROBAN
TARGET=cctp-router-integrators || TIER=2 || FAMILY=BRIDGE-MESSAGE-NOT-BOUND-TO-SOURCE || DECISIVE_CHECK=For each integrator calling CCTP receiveMessage, confirm the credited amount/asset is bound to a verified DepositForBurn on the source domain and a plain attacker-authored sendMessage body cannot be replayed into a credit. || VALUE_AT_RISK=UNMEASURED_POPULATION || PINNED=BASE#50596624 || MODULES=EVM|BRIDGE
```

---

## 4. Where this run is probably still wrong

1. **The LayerZero-OApp screen (B) is the whole value and has not been run.** I verified the
   mechanism on one contract; I did not enumerate the OApp population or find a single live un-hit
   instance. Everything about that lead's *magnitude* is unproven until that screen runs.
2. **Arrakis is real but small, and I only measured mainnet.** The L2 V1 factories are the same
   code and unmeasured; the true fleet TVL could be a few × higher or not.
3. **Three leads (C, D, and the Solana/Soroban parts) were not fork-verified** — this environment's
   depth is EVM. They are named leads with concrete checks and public-source corroboration, not
   confirmed findings. Marking them beats guessing.
4. **The corpus is still a lead source, not a census.** The re-crawl found 11 rows the run-1 index
   never carried; the count is a lower bound, and off-chain-root-cause losses (private key, supply
   chain, social engineering — the majority of the ~$1.1B window total) are correctly excluded and
   out of scope.
5. **No finding here is confirmed exploitable.** This is a triage queue, consistent with the rest
   of the project.
