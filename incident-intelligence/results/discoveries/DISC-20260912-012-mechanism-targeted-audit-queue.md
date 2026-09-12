# DISC-20260912-012 — Mechanism-targeted discovery: two years of hacks, read to the code, aimed at the audit

*A deliberately slow, targeted run. Instead of another metadata batch, I studied every SlowMist incident for two years, tested my own thesis against that evidence, distilled the code shapes that actually drain money, then read deployed source to separate guarded from exposed. The goal is a higher audit hit-rate: hand the auditor the exact function to open and the exact guard to check, backed by evidence that the mechanism is what's really being hit.*

## 1. The evidence — 560 incidents, 2024-09 → 2026-09 (`sources/mechlib/`)

I crawled the full SlowMist Hacked index back two years (560 incidents) and classified each by scope and mechanism.

- **Scope:** 305 on-chain smart-contract root causes (54%) vs 255 off-chain (key/seed leak, phishing, rug, infra). Off-chain is out of our mandate; on-chain is the majority and our whole field.

- **On-chain mechanism distribution (count | total loss):**

| Mechanism | # | Loss | Read |
|---|--:|--:|---|
| logic / accounting | 105 | \$434M | custom state-machine & share/reserve accounting bugs |
| oracle / price-manipulation | 58 | \$220M | spot/thin feeds moved with flash capital |
| access-control | 40 | \$122M | missing gate on a fund-moving fn |
| flashloan-assisted logic | 23 | \$18.6M | (amplifier, usually + one of the above) |
| bridge / mint-burn | 18 | \$47M | mint not bound to a verified burn |
| reentrancy | 8 | \$42.7M | classic, now rarer |
| math / rounding / truncation | 6 | \$144M | rare but catastrophic (Notional shape) |
| share-inflation | 6 | \$10.8M | first-deposit / donation |
| signature / verification | 4 | \$10.2M | **the SOFA class — only 4 in two years** |

- **Loss size:** median **\$392k**; buckets — `<\$100k`: 85, `\$100k–1M`: **100 (the modal band)**, `\$1M–10M`: 74, `>\$10M`: 24. The operator's instinct is evidence-backed: the single most common hack sits in the few-hundred-k band SOFA lived in.

## 2. What this does to my thesis (believing it, and questioning it)

**Confirmed:** custom logic is where the money goes. logic/accounting + oracle + access-control = 203 of 305 incidents and \$776M — overwhelmingly *bespoke* code, not fork-inherited core. "Read custom logic, skip forks" holds.

**Corrected — I was over-indexing on my two showcase mechanisms.** signature/replay (SOFA) is **4 in two years**; narrowing-cast/truncation (Notional) is **6**. Both are rare-but-catastrophic → they deserve *standing detectors* (DISC-005/007 already built), not mass hunts. The mechanisms that actually recur are far more mundane: **spot-price manipulation** and **custom accounting desync**.

**Reframed — "unwatched" is a *preventability* argument, not a probability one.** Active protocols get hit too (Moonwell, CometDEX, Balancer). But their bugs get caught and patched by the people paid to watch them. An unwatched protocol's bug stays live long enough for our warning to matter. So: **target by mechanism (where bugs are), then prefer unwatched (where a found bug is still exploitable and our warning still has value).**

## 3. The mechanism library — the code shapes that drain, from reading the 2026 incidents

Each is a concrete, code-visible shape with a decisive check and a falsifier. This is the targeting lens.

### A — spot price as oracle in a value / mint / collateral path (no TWAP, flash-reachable)  ·  *the modal 2026 hack*
Seen in BeatSwap, Float, Arrakis V1, LOOPSDAO, LULA, 42DAO, Tectonic, Moonwell. A `deposit`/`mint`/`borrow`/`stake` reads `pool.slot0()` / `getReserves()` / a spot quote to price shares or collateral, so a flash-loaned skew mints cheap or borrows over-value.  
**Decisive check:** does the pricing read spot with **no TWAP and no deviation guard**, and is the function reachable by a contract in one tx?  **Falsifier (safe):** a TWAP/deviation guard, **or** an `onlyEOA` (`msg.sender==tx.origin`) gate that blocks the atomic flash-loan, **or** a Chainlink feed with staleness checks.

### B — accounting desync (paired update short-circuited, or same-asset/self path)
Zentra (debt path completes while the aToken burn is reduced), Secured Finance (unfilled orders counted as filled), CometDEX (USDC→USDC same-asset swap corrupts reserves), Reddio (one balance counted by two share prices), Maya (false subsidy).  
**Decisive check:** is every paired state update atomic and mutually consistent, and are same-asset / self-interaction paths blocked?  **Falsifier:** each debit has a matching credit in the same path; same-token/self calls revert.

### C — unprotected fund-mover / privileged-public function
MOKE (`releaseContract().claim()` public, no eligibility), Crypto DAO (public vault fns), LULA (`recycle()`), GebProxyActions (`quitSystem`), 42DAO (pushable median oracle).  
**Decisive check:** is every fund-moving or oracle-setting entrypoint gated to a per-user owner or a trusted role?  **Falsifier:** each such fn has an `onlyOwner`/per-user/authorized-relayer gate.

### D — oracle misassignment / stale-feed fallback
Solido Cash (stale fallback routed SOLID to the CASH feed, over-valuing collateral), Full Sail (attacker added an oracle key).  
**Decisive check:** does the oracle path have a fallback that can over-value collateral, or a permissioned-but-weak key/median an attacker can influence?

### E — signature replay / non-binding aggregate  (rare: SOFA, Atomic Green)  ·  standing detector = DISC-005
### F — mint-against-collateral with incomplete input validation  (Lien Finance multiset; bond/structured mints)

## 4. Reading the code — the decisive check, run (guarded vs exposed)

To prove the check discriminates (and to avoid sending the auditor at already-safe targets), I read two of the sharpest mechanism-A suspects to the metal:

- **Universe Finance** (Ethereum, `GeneralVault`, Solidity 0.7.6, deprecated — `sources/mechA/`): `_calcShare` **does** price the deposit at raw `slot0` spot (`_price()`, no TWAP) — the Arrakis shape. **But `deposit` and `withdraw` are both `onlyEOA` (`msg.sender == tx.origin`)**, which blocks the atomic flash-loan manipulation (a flash loan must call back into a *contract*, so `tx.origin` ≠ `msg.sender`); withdrawal is pro-rata of the real liquidity, not spot-valued; and a 0.3% penalty taxes unbalanced deposits. **Verdict: GUARDED** against the modal flash-loan attack (residual: expensive multi-block manipulation with real capital). An honest clear — don't spend audit hours here.

- **DefiEdge** (multi-chain liquidity manager, deprecated): factory exposes `allowedSwapDeviation` and a dedicated `DefiEdgeTwapStrategy` — deviation/TWAP-guarded. **Verdict: GUARDED.**

**What this tells us:** the modal mechanism (A) is *already guarded in the mature, verified, named ALMs* (Universe `onlyEOA`, DefiEdge deviation, Gamma/Charm TWAP). The live A-risk therefore concentrates in (i) **unverified / obscure small vaults** we can't read remotely, (ii) the **oracle-priced-collateral lending/CDP** surface (the Tectonic/Moonwell shape, mechanism A+D), and (iii) **new bespoke pricers** (basis / delta-neutral vaults) that predate no norm and rolled their own valuation.

## 5. The mechanism-targeted audit queue (TVL neutral; open the named function, check the named guard)

401 bespoke candidates matched to a mechanism, drawn from this project's pools (overlaps DISC-010/011 by design — unaudited). For each surface: **the exact decisive check to run.** Read in this order — it maximizes the chance a given audit-hour lands on a real bug.

### ▶ Read first — A2: oracle-priced-collateral lending / CDP / risk-curators  (134 EVM)
*Biggest surface and the biggest 2026 loss category (\$220M oracle-manip).* **Check:** what prices the collateral? If a DEX spot pool or a low-liquidity token feed with no TWAP/deviation — or a curator-set oracle — a flash-skew over-values it and over-borrows (Tectonic/Moonwell/Solido). Top by TVL (neutral), watched/known flagged:

| Protocol | TVL | Chain | Category | Flags | What it is |
|---|---|---|---|---|---|
| Summer.fi Pro | $17.19M | Ethereum | CDP Manager | 💤 deprecated | Borrow, Multiply and Earn on the assets you hold across mult… |
| Alpaca Finance 2.0 | $12.92M | Binance | Lending | 💤 deprecated | Alpaca Finance offers a simple way for both beginners and pr… |
| Abracadabra Spell | $4.74M | Ethereum | CDP | — | Abracadabra.money is a spell book that allows users to produ… |
| Credit Coop | $4.60M | Ethereum | RWA Lending | — | Credit Coop is transforming credit markets with blockchain-p… |
| Tangent Finance | $4.57M | Ethereum | Lending | — | Tangent is a decentralized lending protocol on Ethereum that… |
| TermFinance Lend | $4.01M | Ethereum | Lending | — | TermFinance is a fixed rate borrow/lend protocol pioneering … |
| Morpho Midnight | $3.90M | Base | Lending | — | Morpho Midnight, Morpho's fixed-rate, fixed-term lending pro… |
| Presto | $3.32M | Ethereum | Risk Curators | — | Presto is a risk curator on Morpho. |
| Compound V1 | $3.28M | Ethereum | Lending | — | Compound is an algorithmic, autonomous interest rate protoco… |
| mStable V2 | $3.12M | Ethereum | CDP | — | mStable V2. |
| Notional V2 | $3.10M | Ethereum | Lending | 💤 deprecated | Fixed rate lending on Ethereum |
| mStable CDP | $3.01M | Ethereum | CDP | — | mStable unites stablecoins, lending and swapping into one st… |
| Venus Flux | $3.01M | Binance | Lending | — | Venus Flux is a lending protocol within the Venus ecosystem … |
| QiDao | $2.71M | Polygon | CDP | — | QiDao is a way for you to keep your crypto and still be able… |
| Reflexer | $2.69M | Ethereum | CDP | — | A decentralized, stable and non pegged currency made for the… |
| Goldfinch | $2.58M | Ethereum | RWA Lending | — | Goldfinch is a decentralized credit protocol, built for the … |
| 1212 Capital | $2.49M | Ethereum | Risk Curators | — | 1212 Capital is an investment firm specializing in DeFi and … |
| Usual ETH0 | $2.32M | Ethereum | Synthetics | — | ETH0 is a synthetic Ethereum-based asset fully collateralize… |
| INIT Capital | $2.09M | Mantle | Lending | — | The Liquidity Hook Money Market: Lend, Borrow, and Access Yi… |
| Ensuro | $2.06M | Ethereum | Insurance | — | Ensuro is a decentralized capital provider for insurance ris… |
| Hyperbeat USD | $1.91M | Hyperliquid L1 | Lending | — | Every dollar deposited into a Hyperbeat Liquid banking accou… |
| DeFIL | $1.76M | Ethereum | Lending | 💤 deprecated | DeFIL is a decentralized Filecoin lending and finance servic… |

### ▶ Read next — A3: basis / delta-neutral vaults  (6)
*Newest bespoke share-pricing; no established guard norm.* **Check:** is the share price a function of a live hedge / funding rate that can be moved or desynced within a tx? Is deposit/withdraw flash-reachable?

| Protocol | TVL | Chain | Category | Flags | What it is |
|---|---|---|---|---|---|
| Monetrix USDM | $2.54M | Hyperliquid L1 | Basis Trading | — | Monetrix is the first fully on-chain funding-driven yield-be… |
| DeSyn Basis Trading | $1.72M | Bitlayer | Basis Trading | — | DeSyn is a decentralized liquidity infrastructure on Web3, e… |
| Monetrix mxHYPE | $1.69M | Hyperliquid L1 | Basis Trading | — | HYPE-denominated yield vault on Hyperliquid. Deposited HYPE … |
| Delpho | $495k | Hyperliquid L1 | CDP | — | Delpho is a CDP protocol on HyperEVM. Users deposit collater… |
| Predy V3.2 | $25k | Arbitrum | Derivatives | 💤 deprecated | Predy V3.2 allows traders to utilize portfolio margin for Sq… |
| BasisOS | $24k | Arbitrum | Basis Trading | 💤 deprecated | BasisOS Agent is an autonomous AI system built to manage DeF… |

### A1: ALM / LP-share vaults  (21 EVM — skip the guarded/known, read the fresh)
**Check:** does `deposit`/`withdraw` price shares off `slot0`/reserves with **no** TWAP/deviation **and no** `onlyEOA`, reachable by a contract? (Universe=GUARDED onlyEOA, DefiEdge=GUARDED deviation, Gamma/Charm=TWAP, Arrakis V1=the incident — all flagged; read the *unflagged* small/fresh ones.)

| Protocol | TVL | Chain | Category | Flags | What it is |
|---|---|---|---|---|---|
| DefiEdge | $878k | Binance | Liquidity Manager | 💤 deprecated | Permissionless Liquidity Management on Uniswap V3. DefiEdge … |
| EZManager | $526k | Base | Liquidity Manager | — | EZManager is a concentrated liquidity management platform th… |
| Krystal Community Vault | $277k | Base | Liquidity Manager | — | Community Vault a strategist publishes their farming approac… |
| Dyson | $269k | Arbitrum | Liquidity Manager | — | Dyson brings exotic investment strategies to some of the mos… |
| YieldFlow Yield Farming | $244k | Arbitrum | Liquidity Manager | — | YieldFlow is a decentralized platform for yieldfarming throu… |
| Skate Fi | $150k | Ethereum | Liquidity Manager | — | Skate Fi (formerly known as Range Protocol): Liquidity Layer… |
| Clip Finance | $86k | Linea | Liquidity Manager | — | Simplifying yield farming and maximizing profitability by le… |
| SteakHut Liquidity | $55k | Avalanche | Liquidity Manager | — | Automate and optimize concentrated liquidity. |
| exit.tech | $41k | Arbitrum | Liquidity Manager | 💤 deprecated | A platform that lets you easily exit your locked DeFi positi… |
| Bunni v1 | $34k | Ethereum | Liquidity Manager | — | Bunni represents Uniswap v3 LP positions with fungible ERC-2… |
| Gamma | $3.20M | Ethereum | Liquidity Manager | watched/known | A protocol for active liquidity management and market-making… |
| Baseline Protocol | $1.94M | Ethereum | Liquidity Manager | watched/known | Baseline is a DEX built for project tokens, combining token-… |
| Arrakis V1 | $1.39M | Ethereum | Liquidity Manager | watched/known | Arrakis is a protocol that specializes in concentrated & act… |
| xToken | $942k | Ethereum | Liquidity Manager | watched/known, 💤 deprecated | Permissionless Investment Bank |
| Charm Finance V1 | $324k | Ethereum | Liquidity Manager | watched/known | An ecosystem of innovative products within DeFi |
| Arrakis V2 | $165k | Ethereum | Liquidity Manager | watched/known | Arrakis V2 is a next-generation market-making infrastructure… |

### B: custom AMM accounting edges  (14 EVM)  &  C: pooled-collateral options/structured  (26 EVM)
**B check:** empty-pool mint, same-asset swap, fee-on-transfer reserve desync (CometDEX/Balancer-V1 shapes). **C check:** is mint/settle/exercise gated, and is each payoff bound to a snapshot taken at open? (the SOFA shape). Full rows in `DISC-20260912-012-candidates.json`.

## 6. Honest limits & self-check

- **I confirmed the check discriminates, and cleared two suspects (Universe, DefiEdge) — I did not confirm a live exposed instance in this pass.** The named, verified ALMs are mostly guarded; the exposed A-instances are disproportionately *unverified* (unreadable remotely) or sit in the A2/A3 surfaces I'm pointing you at. That is a real, if uncomfortable, result: the easy slot0 bug is largely patched in code you can read, so the yield is in code you have to pull on-chain per-target.
- **This queue is mechanism-matched leads, not code-confirmed vulns** (except the two cleared reads). The value is the narrowing: you open one function and check three guards, instead of reading a repo cold.
- **Evidence caveats:** mechanism labels are keyword-classified from incident text (a few land in 'other'); the \$1.78B 'other/unclear' bucket is dominated by a handful of L1/precompile mega-incidents outside our contract scope.
- Backing data: `sources/mechlib/` (2-yr incidents + on-chain classification), `sources/mechA/` (Universe read), `DISC-20260912-012-candidates.json` (the full 401-row queue).

## 7. Module tags on the candidates JSON (audit routing)

`DISC-20260912-012-candidates.json` is keyed `"<module> :: <slug>"` and trimmed to what an
audit needs: `name, cat, tvl, chains, addr, check, desc` (+ `deprecated`/`watched_known`
flags only when true). `addr` is the DefiLlama-listed address (may be `chain:0x…`, may be a
token rather than the core — confirm the core on-chain), or `null` where none is listed.

**Module = `<vm>` (+`,bridge` if a bridge) (+`,generic` if no corresponding primitive module):**
- **vm** from the chain: `evm` (Ethereum/L2s/BSC/Polygon/Avalanche/Tron/… EVM-compatible),
  `solana`, `move` (Aptos/Sui), `cosmos` (Osmosis/Injective/Terra/Thorchain/… appchains),
  else `generic` (Stacks, Cardano, TON, Near, Starknet, Radix, Algorand, Tezos, Stellar, …).
- **`bridge`** appended for cross-chain bridges.
- **`generic`** appended (on a known vm) for categories with no corresponding specific
  primitive module (Algo-Stables, RWA, Reserve Currency, Indexes, Stablecoin Wrapper,
  Services, SoFi, Gaming, …) — matching `evm,generic :: oin-finance`.

Validated against the supplied examples: `move::argo`, `evm::predy-v3.2`,
`solana::synthetify`, `evm,bridge::everrise`, `cosmos::ion-dao`, `evm,generic::oin-finance`
— all reproduced. Distribution: evm 233, generic 112, solana 26, cosmos 11, evm,generic 10,
move 9. Ordering preserved as the audit priority A2→A3→A1→B→C.
