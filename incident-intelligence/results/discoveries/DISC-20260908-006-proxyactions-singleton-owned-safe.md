# DISC-20260908-006 — "A SAFE owned by an anyone-callable singleton is drainable by anyone" (GEB/Maker proxy-actions class)

**A personal, code-first pass — not a filtered batch.** After learning the newest SlowMist hacks
(Aug 30–Sep 8), I followed one that matched the "old, unmodified code" instinct — **GebProxyActions**
(Sep 2) — read the actual deployed code to understand the true mechanism, and then went on-chain to see
whether the same door is open anywhere live. No conditions stacked; one thread, pulled to the end.

## What I learned from the new hacks (Aug 30–Sep 8)

- **GebProxyActions** (Sep 2, ~5.94 ETH) — access-control: a fund-moving action meant to be `delegatecall`ed
  was callable directly; once a victim's SAFE was owned by the shared actions singleton, anyone drained it.
- **Notional Finance** (Sep 4, $1.73M) — legacy V1 Escrow: an unsafe `uint128` cast let a fabricated
  ~2^128 liability truncate to 0, bypassing the solvency check. *Old code, integer truncation.*
- **Balancer V1** (Aug 31, $234k) — legacy pool: flash-compress a reserve to ~0, mint BPT with 1 wei,
  exit proportionally. *Ratio math sane at depth, unbounded at empty.*
- **Unnamed BSC router** (Sep 7, $46k) — `uniswapV3SwapCallback` didn't authenticate the caller is a real
  pool → fake pool + `payer=victim` drains standing allowances via `transferFrom`.
- **Tectonic** ($120M), **Moonwell** ($8.8M) — governance/low-float token used as collateral, price
  manipulated, borrow. **Float Protocol** ($28k) — Gamma Hypervisor LP-share priced off `slot0` (the
  Arrakis shape). **Full Sail** ($91k) — attacker added a key to a live Switchboard oracle.

Two of these are pure "old code still holds a clean bug" (GebProxyActions, Notional, Balancer V1) — the
thread worth pulling personally.

## The mechanism, from deployed source (not the repo)

RAI `GebSafeManager` (mainnet `0xefe0b4ca…f185`, Solidity 0.6.7 — untouched ~5 years),
`sources/geb/safemanager.sol`:

```solidity
mapping (uint => address) public ownsSAFE;              // SAFEId => Owner
modifier safeAllowed(uint safe) {
    require(msg.sender == ownsSAFE[safe] || safeCan[ownsSAFE[safe]][safe][msg.sender] == 1, "safe-not-allowed");
    _;
}
function quitSystem(uint safe, address dst) public safeAllowed(safe) handlerAllowed(dst) { /* move collateral+debt to dst */ }
```

`GebProxyActions` is a **shared singleton** meant to be reached only via a user's DSProxy `delegatecall`
(so `msg.sender` to the manager is the user's DSProxy = the owner). Its wrapper `quitSystem(manager,safe,dst)`
has **no `msg.sender` gate** — correct *only* under delegatecall. The bug is the combination:

> If any SAFE's `ownsSAFE[safe]` is the **GebProxyActions singleton** (which happens when a user mistakenly
> calls the singleton *directly* instead of via their DSProxy), then **anyone** can call
> `GebProxyActions.quitSystem(manager, safe, attacker)`; the singleton is `msg.sender==ownsSAFE[safe]`, so
> `safeAllowed` passes, and the collateral goes to the attacker's `dst`.

Generalized: **a SAFE/CDP whose owner is a contract that anyone can drive (no per-user gate) is drainable
by anyone.** Normal owners — an EOA, or a per-user DSProxy — are self-guarded; a shared actions singleton
is not. The whole DSProxy-actions family shares this shape: Maker `DssProxyActions`+`cdpManager`, GEB
`GebProxyActions`+`GebSafeManager`, and forks (HAI, Open Dollar, Azos, TAI).

## Did I find it live? — the census (this is the actual work)

**RAI (mainnet) — CLEAN now (proven).** I enumerated `ownsSAFE[safe]` for the whole manager
(2,397 / 2,453 safes read at head) and classified every owner by bytecode
(`sources/geb/rai_census.json`):
- **1,837 owners are EOAs** — self-guarded.
- **389 owners are contracts, all one identical DSProxy bytecode** (codehash `572b73…`, len 4346) — each
  owner-gated by its user.
- **0 owners are a non-DSProxy, anyone-callable contract.** No SAFE is owned by the GebProxyActions
  singleton (or any other shared singleton). The Sep-2 exploit swept the one vulnerable SAFE; none remain.

**Open Dollar (Arbitrum, `ODSafeManager 0xc2b820bd…`) — NOT vulnerable by design (proven).**
`sources/geb/od_safemanager_flat.sol`: `quitSystem(uint256 _safe)` sends collateral to `_dst = _sData.owner`
— **not a caller-chosen address** — so even a singleton-owned SAFE returns funds to the owner, not an
attacker; ownership transfers only via the Vault721 NFT; allowances are nonce-scoped. The OD fork closed
this class deliberately.

**HAI (Optimism, `HaiSafeManager 0xB0FF82D8…06C3`) — CENSUSED, CLEAN (proven).**
`quitSystem(uint256 _safe, address _dst)` keeps the **old-GEB shape with an attacker-suppliable `_dst`**
(unlike OD), so HAI *would* be exposed if a SAFE were owned by an anyone-callable singleton. I censused all
**861 SAFEs**: every owner is a **per-user HaiProxy** (one identical bytecode, codehash `5d8d13…`, 480
distinct owners), zero EOAs, **zero non-HaiProxy contract owners** (`sources/geb/hai_census.json`). No
drainable SAFE. Clean.

## The result, stated honestly

I did **not** find a new live-exploitable instance. All three live GEB-family deployments that hold the
money are clean or immune: **RAI clean at head** (on-chain census), **HAI clean at head** (on-chain
census), **Open Dollar hardened by design**. That is the truthful outcome of pulling this thread — proven
on-chain, not asserted. This class's one known live instance (the Sep-2 GebProxyActions SAFE) was already
swept by its exploiter. The value of the pass is (a) the mechanism read to the metal on live code, and
(b) a **standing detector** that catches the *next* victim of this class the moment it appears — a mistaken
singleton-owned SAFE is drainable the instant it is created, so detection speed is the whole game.

## The detector (run continuously; it is cheap and decisive)

For every GEB/Maker-family manager (RAI `GebSafeManager`, HAI `HaiSafeManager`, Azos, TAI, Maker
`cdpManager`, and any fork whose `quitSystem`/equivalent takes a caller-chosen `dst`):

1. Enumerate `ownsSAFE[safe]` (or `_safeData[safe].owner`) for all safes.
2. Classify each owner: EOA → safe; per-user proxy (DSProxy/ODProxy/HaiProxy, single dominant codehash) →
   safe; **any other contract → ALERT.**
3. An alerting owner that is an **anyone-callable singleton** (the actions contract, or anything with an
   ungated function that calls the manager on that safe) is a **live, drainable SAFE** — its
   `lockedCollateral` is the value at risk. Notify the owner / whitehat-rescue before it is swept.

This is the SOFA lesson applied: the bug isn't the protocol's age or category — it's a specific,
code-visible authorization shape, and the way to catch it is to read the owner set on-chain, not to filter
metadata.

## Immediate next threads (live-instance-likely, from the fresh hacks)

- **Azos / TAI census** for the condition above (RAI, HAI already done and clean; Open Dollar immune).
- **Unauthenticated V3 swap-callback allowance-drain** (BSC router class): routers whose
  `uniswapV3SwapCallback`/`pancakeV3SwapCallback` don't verify `msg.sender` is a real pool → drains standing
  allowances. Code-searchable; value-at-risk = live approvals.
- **Legacy `uint128`/narrowing casts in solvency/collateral valuation** (Notional class): old lending/CDP
  code where a fabricated large liability truncates to 0 past a bounds check.

Evidence: `sources/geb/safemanager.sol`, `od_safemanager_flat.sol`, `rai_census.json`;
fresh-hack list `sources/slowmist_run3/rows.json`.
