# DISC-20260908-007 — "A raw narrowing cast on a balance can zero out a liability" (Notional V1 class), and the one live fork that copied it

**A personal, code-first pass — one thread pulled to the end.** Of the newest SlowMist hacks I picked the one with the
"old, unmodified code still holds a clean bug" quality that has paid off before — **Notional Finance V1** (Sep 4,
$1.73M) — read the *actual exploited line* in the deployed source, turned it into a sharp code-level detector, and ran
that detector across all of GitHub + the verified-source mirrors to find whoever else is standing on the same landmine.
No metadata filters, no condition-stacking; the authorization/valuation math, read to the metal, then hunted.

## The bug, from deployed source (not a post-mortem paraphrase)

Notional V1 `Escrow` proxy `0x9abd0b8868546105F6F48298eaDC1D9c82f7f683` (impl now `EmptyProxy` — **paused after the
hack**). The exploited math lives in the `ExchangeRate` library, `_convertToETH`, verbatim
(`sources/notional/utils_ExchangeRate.sol`, `pragma solidity ^0.6.0`):

```solidity
function _convertToETH(Rate memory er, uint256 baseDecimals, int256 balance, bool buffer) internal view returns (int256) {
    uint256 rate = _fetchExchangeRate(er, false);
    uint128 absBalance = uint128(balance.abs());          // <-- RAW truncating cast (bug)

    // "We use uint256 to do the calculation and then cast back to int256 to avoid overflows."
    int256 result = int256(
        SafeCast.toUint128(rate.mul(absBalance)           // <-- SafeCast used ON THE RESULT, one line below
            .mul(buffer ? er.buffer : Common.DECIMALS).div(er.rateDecimals).div(baseDecimals))
    );
    return balance > 0 ? result : result.neg();
}
```

`SafeInt256.abs(int256)` returns an **`int256`** (`sources/notional/lib_SafeInt256.sol`). Casting an `int256` to
`uint128` in Solidity 0.6.x **truncates to the low 128 bits with no revert**. So if a currency balance's magnitude is
driven to **exactly `2^128` base units**, `absBalance == uint128(2^128) == 0`, the ETH value of that liability is `0`,
and the solvency gate in `Portfolios` —

```solidity
(int256 fc, , ) = freeCollateral(payer);
require(fc >= 0, $$(ErrorCode(INSUFFICIENT_FREE_COLLATERAL)));
```

— passes for an account that is massively insolvent. The attacker opened two matched positions summing to a `-2^128`
liability, the free-collateral check saw **zero** liability, and they withdrew ~69,257 DAI + 1,658,524 USDC (~$1.73M →
689 ETH → Tornado Cash).

**The tell is exquisite and rare.** The author *imported `SafeCast` and used `SafeCast.toUint128` one line below*, and
even wrote a comment about avoiding overflows — but applied a **raw** `uint128(...)` to the balance. The safe idiom was
in hand and applied inconsistently. That inconsistency is the fingerprint a code screen can own.

## The class — `RAW-NARROWING-CAST-IN-SOLVENCY-VALUATION`

> A collateral/solvency valuation narrows a **balance / liability / debt** to `uintN`/`intN` with a **raw** cast
> (`uint128(x)` / `int128(x)`, *not* `SafeCast.toUintN` and *not* preceded by a `require(min<=x && x<=max)` bound),
> where the magnitude is **attacker-influenceable**, and the narrowed value then feeds a `require(freeCollateral >= 0)`
> / health / liquidation comparison. Truncation makes a huge liability value to ~0 (or a huge asset overflow-wrap),
> defeating the check.

It is **not** an "old contract / unused function" property — Notional V1's `_convertToETH` was on the hot path of every
trade. It is a specific, code-visible arithmetic-authorization mistake, findable only by reading the cast. (Note: an
explicit `uintN(...)` cast **still truncates silently in Solidity 0.8** — 0.8's checked arithmetic covers `+`/`-`/`*`,
not casts — so the class is not confined to pre-0.8 code.)

## The detector (hunt code, not metadata)

**Stage 1 — code search** (run verbatim; these hit deployed code too via the sanctuary / audit-dataset mirrors):

| Indicator | Query | Signal |
|---|---|---|
| the exact tell | `"uint128(balance.abs())"` | abs-of-signed-balance, raw-narrowed — highest signal |
| abs-then-narrow (broad) | `"= uint128(" "abs()" language:Solidity` | any signed magnitude narrowed by a raw cast |
| narrowing near the gate | `"int128(" "freeCollateral" language:Solidity` | a raw narrow in/next to the solvency path |

**Stage 2 — read each hit and answer (a finding is any "no"):** Is the cast **raw** (not `SafeCast`, no preceding
`require(min<=x&&x<=max)`)? Is the narrowed quantity a **balance/liability** (not a bounded price/tick/liquidity)? Can an
attacker drive its magnitude to the type boundary? Does the truncated value feed a **solvency/health** comparison?

**Stage 3 — on-chain, for a live hit:** confirm it's a **funded** deployment (adapter/escrow token balances at head) —
that balance is the value at risk. A source-only or zero-TVL match is a *watch*, not a live finding.

## The hunt, run — honest result

Ran Stage 1 across all of GitHub **and** the verified-source mirrors (`smart-contract-sanctuary-*`, audit datasets):

- **`uint128(balance.abs())`** → 15 hits. All are one of: **Notional V1 itself** (`notional-finance/contracts`; and its
  two *deployed* ETH-mainnet `ERC1155Trade` contracts `0x6f102516…` and `0xc9ec73e9…`, verified 0.6.4), benchmark/audit
  mirrors of it, a personal copy (`maxpen00/notional-contracts`), and **one independent live fork → Pledge Finance**.
- **The only independent fork of the exact bug is `pledgefinance/pledge-contracts`** ("Pledger", a BSC fixed-rate
  lending protocol; pTokens = fCash). Its `contracts/utils/ExchangeRate.sol` is **byte-for-byte identical** to Notional
  V1's (`diff` = empty; `sources/notional/pledge/ExchangeRate.sol`), same `pragma ^0.6.0`, both `uint128(balance.abs())`
  lines (49, 80), same `SafeCast.toUint128` imported-yet-inconsistently-applied. Same `Escrow` / `Portfolios`
  (`freeCollateralView` → `_convertToETH`) / `ERC1155Trade.batchOperation` architecture — so **if a Pledge market were
  live and funded, it would be drainable by the identical two-position `2^128`-liability trade.**
- **False positives cleared by reading them:** **Notional V2/V3** (the *current, funded* Notional) **fixed it** — it
  bounds-checks before the cast (`require(type(int128).min <= finalNotional && finalNotional <= type(int128).max); ...
  int128(finalNotional)`), so the live Notional is **not** at risk from this. **Perpetual Protocol v2** (`.toInt128()`
  SafeCast), **Logium** (`require(amount < uint128(type(int128).max))`), **Pendle Boros** (`signedSize` is already
  `int128`, so `abs() ≤ 2^127` fits `uint128` — author-noted safe), and **Rysk** (narrows *strike prices*, bounded, not
  a liability feeding a gate) are all safe.

### Is Pledge a *live, funded* instance? — the value-at-risk check (this is the actual work)

I tried hard to find a funded Pledge deployment of the vulnerable lending system and could **not**:

- **DefiLlama:** zero entries for Pledge (no tracked lending TVL).
- **BSC verified-source mirror** (`tintinweb/smart-contract-sanctuary-bsc`): the distinctive Notional-V1 tells
  (`G_LIQUIDITY_HAIRCUT`, `depositIntoMarket`, the `batchOperation(address,uint32 maxTime,Deposit[],…)` signature) →
  **0 hits.** The only *deployed-verified* instances of this code anywhere are Notional's own ETH-mainnet contracts.
- **No deployment manifest / subgraph / networks file** committed in either Pledge repo; addresses live only in an
  env-provided file. The repo README says the system is in the **"testing phase."**
- The **live** PLGR is a separate `v0.8.4 PledgeToken` (`0x77e77BA32c14f51Dde98E29AC699e17D3439EDA7`, supply 1,000,000)
  and the docs now describe an **AMM / RWA "V2.0"** — the product **pivoted away** from the Notional fork.

**Stated honestly:** I did **not** find a new live, funded, exploitable instance. This class is, as of today, confined to
the **Notional V1 lineage**: Notional V1 itself (the incident — now **paused**, impl = `EmptyProxy`, contained) plus **one
dormant source-only fork (Pledge)** carrying the identical bug that would be exploitable the instant it deploys a funded
market. The current funded Notional (V2/V3) fixed it. That is the truthful outcome of pulling this thread — proven by
reading the deployed cast and by an exhaustive code + on-chain census, not asserted.

The value of the pass: (a) the bug read to the metal on live code; (b) a **sharp, rare, grep-able detector** for a
catastrophic class; (c) a **specific standing watch** — Pledge (and any Notional-V1 fork) is one funded market away from
being the next $1.7M, so the detector's job is to fire the moment a funded market appears.

## Decisive check / falsifier / residual

- **A live positive** = a hit where the cast is raw (no SafeCast, no bound), the narrowed quantity is a balance/liability,
  its magnitude is attacker-drivable to the type boundary, it feeds a solvency gate, **and** the contract holds real
  backing at head. None found funded; Pledge matches all but the last.
- **Falsifier for any row:** the cast is `SafeCast.toUintN` **or** preceded by `require(min<=x && x<=max)`; or the value
  is provably bounded below the type max (price/tick/liquidity); or the narrowed value never reaches a solvency compare.
- **Residual (honest gaps):** (1) an **unverified** funded Pledge deployment can't be excluded by the mirror alone — the
  escalation is: find Pledge's `Directory` on BSC, `getContract(Escrow)`, and read the Escrow's token balances at head; a
  non-zero balance flips this to a live finding. (2) A **renamed** Notional-V1 fork (different identifiers) would evade
  the exact-string query; the Stage-1 broad query + Stage-2 read is the net for that. (3) The broad class (any raw
  narrowing cast in a solvency path) is larger than the Notional lineage; I read the top perp/option/margin hits (all
  safe) but the semantic screen is a standing job, not a one-shot.
- **Standing action:** keep Stage-1 running against newly deployed / newly verified source; put a **specific watch on
  Pledge Finance** and any Notional-V1 fork for a first funded lending market.

## Dedup

`check_new.py` → **Pledge Finance NEW** (not in `_exclusion_set.json`, not on the 888-blocklist). Notional appears only
as the *incident* (evidence), never as a delivered candidate. Folded into the exclusion set with this push.

## Evidence on disk

- `sources/notional/utils_ExchangeRate.sol`, `lib_SafeInt256.sol`, `Escrow.sol`, `utils_Liquidation.sol` — Notional V1
  deployed source (the exploited library + solvency gate + `abs()`).
- `sources/notional/pledge/ExchangeRate.sol` — Pledge's copy (byte-identical; `diff` empty).
- `sources/notional/screen_result.json` — the detector run: queries, the one fork, the cleared false positives, the
  value-at-risk determination.
