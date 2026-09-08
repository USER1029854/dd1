# DISC-20260908-008 — Fresh-incident discovery batch: 84 un-hit protocols that could lose money next

**This is a discovery, not an audit.** It is a broad, non-repeating net — 84 live protocols, none delivered in any prior push, each mapped to the specific 6-month SlowMist incident whose mechanism it plausibly shares, with a light personal read and the one decisive on-chain check that would confirm or kill it. No single one is deep-audited here; the point is coverage and a ranked queue, not a verdict. A 'feeling that this might lose money' is enough to be listed — the decisive check is how you'd settle it.

## How this batch was built (and what 'personal' means here)

- **Grounded in the fresh hacks.** Every group is one of the on-chain mechanisms from the last ~6 months of SlowMist incidents (`sources/slowmist_run3/rows.json`). Off-chain root causes (key/seed leaks, infra) are excluded.
- **Un-hit & non-repeating.** Every name is checked against the full exclusion set (2,144 names across all prior pushes, incl. the 888-name blocklist) and against the fresh victims themselves. Nothing here has been delivered before.
- **Band + unwatched.** Live TVL in ~$50k–$50M (small-to-mid; giants excluded), sorted **unwatched-first**: deprecated / dead-site / little-or-no fee revenue — the money nobody is paid to defend — rises to the top of each group.
- **Personal, lightly, per item.** The read on each row is its own — its fork lineage, its deprecation state, its chain, the value it would leak — not a filter stack. That's the 'little bit personal' applied across many, not a one-protocol audit.
- **TVL/revenue are live** (DefiLlama, today); treat them as triage signal, and read value at head before acting.

> Honesty line: this is a queue of *hypotheses*, ranked by how exposed they feel. None is a confirmed exploit. The decisive check under each group is the falsifier — run it and the row either becomes a finding or dies.


## Thin-float collateral → oracle manipulation → over-borrow  ·  26 candidates
**Echoes:** Tectonic ($120M, Aug 30) · Moonwell ($8.8M, Aug 27)  
**Mechanism:** A lending market lists a low-liquidity / governance token as collateral and prices it off a manipulable source. Borrow real assets against a price you can push. Deprecated Compound/Aave/Liquity forks are the classic home: nobody's re-checking which collaterals are still thin, and the price feed is often a DEX pool or a stale oracle.  
**Decisive check / falsifier:** Enumerate listed collaterals; for the thinnest one, compare the cost to move its price N× on its deepest DEX pool vs the value that unlocks for borrowing. Safe iff every collateral has a deep, manipulation-resistant feed (or exotic collateral is disabled).

| # | Protocol | Live TVL | Chains | Unwatched signal | Lineage | Personal read |
|---|---|---|---|---|---|---|
| 1 | Alpaca Finance 2.0 | $12.8M | Binance | deprecated, no fee revenue | — | Deprecated lending fork on Binance; deprecated, no fee revenue — check whether any listed collateral is a thin-float token cheaper to move than it is to borrow against. |
| 2 | Ionic Protocol | $2.0M | Mode, Base, Lisk… | deprecated, no fee revenue | Compound V2 | Deprecated Compound V2 fork on Mode; deprecated, no fee revenue — check whether any listed collateral is a thin-float token cheaper to move than it is to borrow against. |
| 3 | Scream | $1.3M | Fantom | deprecated, no fee revenue | Compound V2 | Deprecated Compound V2 fork on Fantom; deprecated, no fee revenue — check whether any listed collateral is a thin-float token cheaper to move than it is to borrow against. |
| 4 | Orbit Protocol | $621k | Blast | deprecated, no fee revenue | Compound V2 | Deprecated Compound V2 fork on Blast; deprecated, no fee revenue — check whether any listed collateral is a thin-float token cheaper to move than it is to borrow against. |
| 5 | ReactorFusion | $282k | zkSync Era, Telos | deprecated, no fee revenue | Compound V2 | Deprecated Compound V2 fork on zkSync Era; deprecated, no fee revenue — check whether any listed collateral is a thin-float token cheaper to move than it is to borrow against. |
| 6 | ABEL Finance | $240k | Aptos | deprecated, no fee revenue | Compound V2 | Deprecated Compound V2 fork on Aptos; deprecated, no fee revenue — check whether any listed collateral is a thin-float token cheaper to move than it is to borrow against. |
| 7 | Vaultedge | $187k | Base, Plasma | deprecated, no fee revenue | Liquity V1 | Deprecated Liquity V1 fork on Base; deprecated, no fee revenue — check whether any listed collateral is a thin-float token cheaper to move than it is to borrow against. |
| 8 | Tender Finance | $178k | Arbitrum | deprecated, no fee revenue | Compound V2 | Deprecated Compound V2 fork on Arbitrum; deprecated, no fee revenue — check whether any listed collateral is a thin-float token cheaper to move than it is to borrow against. |
| 9 | Fountain Protocol | $102k | Oasis | deprecated, no fee revenue | Compound V2 | Deprecated Compound V2 fork on Oasis; deprecated, no fee revenue — check whether any listed collateral is a thin-float token cheaper to move than it is to borrow against. |
| 10 | PolyQuity | $94k | Polygon | deprecated, no fee revenue | Liquity V1 | Deprecated Liquity V1 fork on Polygon; deprecated, no fee revenue — check whether any listed collateral is a thin-float token cheaper to move than it is to borrow against. |
| 11 | Sendit | $75k | Solana | deprecated, no fee revenue | Save | Deprecated Save fork on Solana; deprecated, no fee revenue — check whether any listed collateral is a thin-float token cheaper to move than it is to borrow against. |
| 12 | SiO2 Finance | $55k | Astar | deprecated, no fee revenue | Aave V2 | Deprecated Aave V2 fork on Astar; deprecated, no fee revenue — check whether any listed collateral is a thin-float token cheaper to move than it is to borrow against. |
| 13 | Pac Finance | $7.0M | Blast | deprecated | Aave V3 | Deprecated Aave V3 fork on Blast; deprecated — check whether any listed collateral is a thin-float token cheaper to move than it is to borrow against. |
| 14 | Longbow | $1.7M | Robinhood Chain | no fee revenue | — | lending fork on Robinhood Chain; no fee revenue — check whether any listed collateral is a thin-float token cheaper to move than it is to borrow against. |
| 15 | JustLend V2 | $1.5M | Tron | no fee revenue | Morpho Blue | Morpho Blue fork on Tron; no fee revenue — check whether any listed collateral is a thin-float token cheaper to move than it is to borrow against. |
| 16 | Moola Market | $995k | Celo | no fee revenue | Aave V2 | Aave V2 fork on Celo; no fee revenue — check whether any listed collateral is a thin-float token cheaper to move than it is to borrow against. |
| 17 | Incprinter | $795k | Pulse | no fee revenue | Liquity V1 | Liquity V1 fork on Pulse; no fee revenue — check whether any listed collateral is a thin-float token cheaper to move than it is to borrow against. |
| 18 | Phiat Protocol | $768k | Pulse | no fee revenue | Aave V2 | Aave V2 fork on Pulse; no fee revenue — check whether any listed collateral is a thin-float token cheaper to move than it is to borrow against. |
| 19 | Bastion | $725k | Aurora | no fee revenue | Compound V2 | Compound V2 fork on Aurora; no fee revenue — check whether any listed collateral is a thin-float token cheaper to move than it is to borrow against. |
| 20 | Aurigami | $517k | Aurora | no fee revenue | Compound V2 | Compound V2 fork on Aurora; no fee revenue — check whether any listed collateral is a thin-float token cheaper to move than it is to borrow against. |
| 21 | VETRO | $508k | Ethereum | no fee revenue | — | lending fork on Ethereum; no fee revenue — check whether any listed collateral is a thin-float token cheaper to move than it is to borrow against. |
| 22 | Kona Lend | $500k | Abstract | no fee revenue | Aave V3 | Aave V3 fork on Abstract; no fee revenue — check whether any listed collateral is a thin-float token cheaper to move than it is to borrow against. |
| 23 | USDFC | $437k | Filecoin | no fee revenue | Liquity V1 | Liquity V1 fork on Filecoin; no fee revenue — check whether any listed collateral is a thin-float token cheaper to move than it is to borrow against. |
| 24 | Ripe Protocol | $289k | Robinhood Chain, Base | no fee revenue | — | lending fork on Robinhood Chain; no fee revenue — check whether any listed collateral is a thin-float token cheaper to move than it is to borrow against. |
| 25 | Amply Finance | $262k | Cronos zkEVM | no fee revenue | Aave V3 | Aave V3 fork on Cronos zkEVM; no fee revenue — check whether any listed collateral is a thin-float token cheaper to move than it is to borrow against. |
| 26 | WanLend | $186k | Wanchain | no fee revenue | Compound V2 | Compound V2 fork on Wanchain; no fee revenue — check whether any listed collateral is a thin-float token cheaper to move than it is to borrow against. |

## Dormant / illiquid perp market → self-trade → socialized PnL  ·  16 candidates
**Echoes:** Rocket ($287k, Sep 5)  
**Mechanism:** A perp/derivatives venue keeps a market that is dormant or thinly-quoted. An attacker posts orders at absurd prices and trades against themselves: one account books fake profit, the burner is bankrupted, and the loss is socialized to the pool — then the profit is withdrawn. GMX-V1 forks and small perps that never turned off unused markets are the shape.  
**Decisive check / falsifier:** List every market and its open interest / liquidity; is there a dormant or thin one where self-trading moves the mark and realized PnL is withdrawable before socialization? Safe iff mark is oracle-based, per-market caps exist, and PnL can't be withdrawn faster than it's socialized.

| # | Protocol | Live TVL | Chains | Unwatched signal | Lineage | Personal read |
|---|---|---|---|---|---|---|
| 27 | Taiga Karura | $131k | Karura | deprecated, no fee revenue | — | Deprecated perp venue; look for a dormant/thin market where self-trade moves the mark and PnL is withdrawable. |
| 28 | Mycelium Perpetual Swaps | $113k | Arbitrum | deprecated, no fee revenue | GMX V1 Perps | Deprecated GMX-V1 fork; look for a dormant/thin market where self-trade moves the mark and PnL is withdrawable. |
| 29 | Alpaca Perpetual Futures Exchange | $53k | Binance | deprecated, no fee revenue | GMX V1 Perps | Deprecated GMX-V1 fork; look for a dormant/thin market where self-trade moves the mark and PnL is withdrawable. |
| 30 | SakePerp | $50k | Ethereum, Binance | deprecated, no fee revenue | — | Deprecated perp venue; look for a dormant/thin market where self-trade moves the mark and PnL is withdrawable. |
| 31 | Flipster | $28.3M | Ethereum, Binance, Tron… | no fee revenue | — | perp venue; look for a dormant/thin market where self-trade moves the mark and PnL is withdrawable. |
| 32 | Arcus pTokens | $1.3M | Robinhood Chain | no fee revenue | — | perp venue; look for a dormant/thin market where self-trade moves the mark and PnL is withdrawable. |
| 33 | Strat Perps | $1.2M | Strat | no fee revenue | — | perp venue; look for a dormant/thin market where self-trade moves the mark and PnL is withdrawable. |
| 34 | Scientix | $367k | Binance | no fee revenue | Alchemix V2 | Alchemix V2; look for a dormant/thin market where self-trade moves the mark and PnL is withdrawable. |
| 35 | Gambit Financial | $228k | Binance | no fee revenue | GMX V1 Perps | GMX-V1 fork; look for a dormant/thin market where self-trade moves the mark and PnL is withdrawable. |
| 36 | Jetbit | $96k | Binance | no fee revenue | — | perp venue; look for a dormant/thin market where self-trade moves the mark and PnL is withdrawable. |
| 37 | 10KDex | $91k | Scroll | no fee revenue | GMX V1 Perps | GMX-V1 fork; look for a dormant/thin market where self-trade moves the mark and PnL is withdrawable. |
| 38 | PHAME Protocol | $561k | Pulse | ~no revenue | GMX V1 Perps | GMX-V1 fork; look for a dormant/thin market where self-trade moves the mark and PnL is withdrawable. |
| 39 | FusionX V3 | $94k | Mantle | ~no revenue | Uniswap V3 | Uniswap V3; look for a dormant/thin market where self-trade moves the mark and PnL is withdrawable. |
| 40 | HertzFlow | $7.2M | Binance | low-watched | — | perp venue; look for a dormant/thin market where self-trade moves the mark and PnL is withdrawable. |
| 41 | Bounce.Tech | $925k | Hyperliquid L1 | low-watched | — | perp venue; look for a dormant/thin market where self-trade moves the mark and PnL is withdrawable. |
| 42 | Alchemix V3 | $37.8M | Ethereum, Optimism, Arbitrum | low-watched | — | perp venue; look for a dormant/thin market where self-trade moves the mark and PnL is withdrawable. |

## Permissionless asset/vault registration → same balance counted twice  ·  12 candidates
**Echoes:** Reddio RedSonic ($22.8k, Sep 5)  
**Mechanism:** An LST/restaking aggregator lets a new sub-vault or asset be registered (sometimes permissionlessly), and the same underlying balance ends up counted toward two different share prices. Flash-inflate one share price, redeem the excess, then redeem the other claim on the same underlying.  
**Decisive check / falsifier:** Can a new market/asset be registered without governance, and is any underlying token balance reachable by two share-accounting paths? Safe iff registration is permissioned and each underlying is isolated to exactly one share unit.

| # | Protocol | Live TVL | Chains | Unwatched signal | Lineage | Personal read |
|---|---|---|---|---|---|---|
| 43 | Gryphon | $59k | Injective | deprecated, no fee revenue | — | LST/restaking on Injective; check whether a sub-vault/asset can be added and the same underlying counted by two share prices (the Reddio shape). |
| 44 | Astarter Launch ISPO | $52k | Cardano | deprecated, no fee revenue | — | LST/restaking on Cardano; check whether a sub-vault/asset can be added and the same underlying counted by two share prices (the Reddio shape). |
| 45 | WEMIX.FI Staking | $19.4M | WEMIX | no fee revenue | — | LST/restaking on WEMIX; check whether a sub-vault/asset can be added and the same underlying counted by two share prices (the Reddio shape). |
| 46 | InceptionLRT (Isolated Restaking) | $6.9M | Ethereum | no fee revenue | — | LST/restaking on Ethereum; check whether a sub-vault/asset can be added and the same underlying counted by two share prices (the Reddio shape). |
| 47 | K2 | $5.4M | Ethereum | no fee revenue | — | LST/restaking on Ethereum; check whether a sub-vault/asset can be added and the same underlying counted by two share prices (the Reddio shape). |
| 48 | Phase Stake | $1.9M | Solana | no fee revenue | — | LST/restaking on Solana; check whether a sub-vault/asset can be added and the same underlying counted by two share prices (the Reddio shape). |
| 49 | tramplin.io | $979k | Solana | no fee revenue | — | LST/restaking on Solana; check whether a sub-vault/asset can be added and the same underlying counted by two share prices (the Reddio shape). |
| 50 | Cyber | $559k | Ethereum | no fee revenue | — | LST/restaking on Ethereum; check whether a sub-vault/asset can be added and the same underlying counted by two share prices (the Reddio shape). |
| 51 | Geode | $426k | Avalanche | no fee revenue | Saddle Finance | Saddle Finance on Avalanche; check whether a sub-vault/asset can be added and the same underlying counted by two share prices (the Reddio shape). |
| 52 | Orchai LST | $340k | Orai | no fee revenue | Lido | Lido on Orai; check whether a sub-vault/asset can be added and the same underlying counted by two share prices (the Reddio shape). |
| 53 | Lido Impact Staking | $230k | Ethereum | no fee revenue | Lido | Lido on Ethereum; check whether a sub-vault/asset can be added and the same underlying counted by two share prices (the Reddio shape). |
| 54 | Hubra Yield | $50k | Solana | no fee revenue | — | LST/restaking on Solana; check whether a sub-vault/asset can be added and the same underlying counted by two share prices (the Reddio shape). |

## Unauthenticated V3 swap-callback → allowance drain  ·  9 candidates
**Echoes:** Unnamed BSC DEX router ($46k, Sep 7)  
**Mechanism:** A router/CLMM exposes uniswapV3SwapCallback / pancakeV3SwapCallback that transfers `payer`'s tokens via transferFrom but never verifies msg.sender is a real pool. A fake pool with payer=victim drains standing allowances. Fresh V3 forks and thin routers are where the check is most often copied wrong or omitted.  
**Decisive check / falsifier:** Read the swap callback: does it verify msg.sender == factory.getPool(token0,token1,fee) (or an equivalent pool check) before transferFrom? Value at risk = the sum of live allowances users hold to the router. Safe iff the pool is authenticated.

| # | Protocol | Live TVL | Chains | Unwatched signal | Lineage | Personal read |
|---|---|---|---|---|---|---|
| 55 | Tetu Swap | $51k | Polygon | deprecated, no fee revenue | Uniswap V2 | Uniswap V2; read the swap callback for a real-pool check — if missing, live allowances to the router are the loss. |
| 56 | Laminar | $110k | Hyperliquid L1 | no fee revenue | Uniswap V3 | Uniswap V3; read the swap callback for a real-pool check — if missing, live allowances to the router are the loss. |
| 57 | Sonex | $70k | Soneium | no fee revenue | Uniswap V3 | Uniswap V3; read the swap callback for a real-pool check — if missing, live allowances to the router are the loss. |
| 58 | Junoswap.trade CLMM | $72k | Bitkub, JBC | ~no revenue | Uniswap V3 | Uniswap V3; read the swap callback for a real-pool check — if missing, live allowances to the router are the loss. |
| 59 | HyperBloom | $79k | Hyperliquid L1 | ~no revenue | Beefy | Beefy; read the swap callback for a real-pool check — if missing, live allowances to the router are the loss. |
| 60 | swap.coffee | $114k | TON | ~no revenue | — | V3-style DEX/router; read the swap callback for a real-pool check — if missing, live allowances to the router are the loss. |
| 61 | KrokoSwap V3 | $171k | Kasplex | ~no revenue | Uniswap V3 | Uniswap V3; read the swap callback for a real-pool check — if missing, live allowances to the router are the loss. |
| 62 | Hypertrade V3 | $196k | Hyperliquid L1 | ~no revenue | Uniswap V3 | Uniswap V3; read the swap callback for a real-pool check — if missing, live allowances to the router are the loss. |
| 63 | GroypFi | $84k | TON | low-watched | — | V3-style DEX/router; read the swap callback for a real-pool check — if missing, live allowances to the router are the loss. |

## Payout/settlement with no independent verification or holder snapshot  ·  6 candidates
**Echoes:** Cozy Finance ($160k, Sep 7)  
**Mechanism:** A payout market (insurance / prediction / parametric) settles on an optimistic-oracle YES/NO or a self-reported trigger, without independently verifying the real event and without tying payout eligibility to a pre-proposal holder snapshot. Buy the payout token cheap, propose/settle YES, claim.  
**Decisive check / falsifier:** Does the trigger independently confirm the real-world event (not just an undisputed OO answer), and is payout tied to a snapshot taken before the proposal? Safe iff both hold.

| # | Protocol | Live TVL | Chains | Unwatched signal | Lineage | Personal read |
|---|---|---|---|---|---|---|
| 64 | Satsuma | $780k | Citrea | no fee revenue | Algebra Integral | Dexs; check the trigger independently verifies the event and payout uses a pre-proposal holder snapshot. |
| 65 | PredictEX | $242k | Base | no fee revenue | — | Prediction Market; check the trigger independently verifies the event and payout uses a pre-proposal holder snapshot. |
| 66 | OPINION | $3.5M | Binance | low-watched | — | Prediction Market; check the trigger independently verifies the event and payout uses a pre-proposal holder snapshot. |
| 67 | Sport.fun | $2.7M | Base | low-watched | — | Prediction Market; check the trigger independently verifies the event and payout uses a pre-proposal holder snapshot. |
| 68 | PredictStreet | $4.4M | ADI | low-watched | — | Prediction Market; check the trigger independently verifies the event and payout uses a pre-proposal holder snapshot. |
| 69 | Predict Fun | $11.3M | Binance, Blast | low-watched | — | Prediction Market; check the trigger independently verifies the event and payout uses a pre-proposal holder snapshot. |

## Order-book accounting treats unfilled orders as filled  ·  5 candidates
**Echoes:** Secured Finance ($180k, Sep 5)  
**Mechanism:** A fixed-rate / order-book venue mis-accounts partially- or un-filled orders as filled, creating invalid balances that a flash-loan + self-trade can realize. Small books and V2/V3 forks bolted onto an order layer are the risk.  
**Decisive check / falsifier:** Trace order lifecycle: can an unfilled/partially-filled order ever increment a spendable balance? Can a self-trade in one block create a net-positive balance? Safe iff only actual fills move balances.

| # | Protocol | Live TVL | Chains | Unwatched signal | Lineage | Personal read |
|---|---|---|---|---|---|---|
| 70 | ChickenSwap | $122k | Ethereum | deprecated, no fee revenue | Uniswap V2 | Uniswap V2; trace whether an unfilled/partial order can ever move a spendable balance. |
| 71 | Alien Base V3 | $1.2M | Base | no fee revenue | Uniswap V3 | Uniswap V3; trace whether an unfilled/partial order can ever move a spendable balance. |
| 72 | Alien Base V2 | $363k | Base | no fee revenue | Uniswap V2 | Uniswap V2; trace whether an unfilled/partial order can ever move a spendable balance. |
| 73 | Fluxion Network | $7.3M | Mantle | ~no revenue | Uniswap V3 | Uniswap V3; trace whether an unfilled/partial order can ever move a spendable balance. |
| 74 | Deepstate | $126k | Robinhood Chain | low-watched | — | Dexs; trace whether an unfilled/partial order can ever move a spendable balance. |

## Mint/withdraw not bound to a verified remote burn  ·  4 candidates
**Echoes:** Allbridge ($190k, Aug 19) · warp.green ($93k, Aug 23) · SAND OFT ($675k, Aug 21)  
**Mechanism:** A bridge credits a deposit or mints a wrapped asset on the strength of a message that isn't cryptographically bound to a real, replay-protected burn on the source chain (forged CCTP message, weak puzzle, self-attested relayer, or a seizable OFT config).  
**Decisive check / falsifier:** Is every mint/release bound 1:1 to a verified source burn with replay protection and an independent verifier set (≥2 DVNs for OFTs; real attestation for CCTP)? Safe iff binding + replay-protection + independent verification all hold.

| # | Protocol | Live TVL | Chains | Unwatched signal | Lineage | Personal read |
|---|---|---|---|---|---|---|
| 75 | Alephium Bridge | $238k | Ethereum, Binance, Alephium | deprecated, no fee revenue | Portal | Portal; check every mint/release is bound to a verified, replay-protected remote burn. |
| 76 | Rhino.fi | $1.4M | Polygon, Arbitrum, Ethereum | no fee revenue | — | Bridge; check every mint/release is bound to a verified, replay-protected remote burn. |
| 77 | XO Bridge | $311k | Base | no fee revenue | — | Bridge; check every mint/release is bound to a verified, replay-protected remote burn. |
| 78 | RWA Perp Bridge | $66k | X Layer | no fee revenue | — | Bridge; check every mint/release is bound to a verified, replay-protected remote burn. |

## LP-share priced off spot slot0 (no TWAP) → flash-skew mint/burn  ·  1 candidates
**Echoes:** Arrakis V1 ($7k, Aug 23) · Float Protocol ($28k, Aug 31)  
**Mechanism:** A liquidity-manager / ALM vault values its Uniswap-V3 position (and hence its LP shares) from pool.slot0() spot, with TWAP only guarding rebalance. Flash-skew the pool, mint or burn shares at the distorted valuation, restore.  
**Decisive check / falsifier:** Do mint()/burn() value the position off slot0()/a spot quote with no TWAP or deviation guard? Safe iff share valuation uses a TWAP/oracle with a deviation bound.

| # | Protocol | Live TVL | Chains | Unwatched signal | Lineage | Personal read |
|---|---|---|---|---|---|---|
| 79 | vfat.io | $26.1M | Base, Ethereum, Arbitrum… | low-watched | — | ALM vault; check mint()/burn() don't value shares off slot0 spot without a TWAP guard. |

## AMM reserve-accounting breaks at an edge (empty pool / same-asset / fee-on-transfer)  ·  2 candidates
**Echoes:** Balancer V1 ($234k, Aug 31) · CometDEX ($717k, Aug 25)  
**Mechanism:** Constant-product / weighted-pool math that is sane at depth becomes exploitable at an edge: reserves compressed to ~0 (mint BPT with 1 wei then exit), a same-asset swap that corrupts reserves, or a fee-on-transfer token that desyncs balances. Old V2/Balancer forks carry it.  
**Decisive check / falsifier:** Can a reserve be driven near-0 and shares minted against it, or can a same-token / fee-on-transfer path desync reserves? Safe iff there's a min-liquidity floor, a same-token guard, and balance re-reads after transfer.

| # | Protocol | Live TVL | Chains | Unwatched signal | Lineage | Personal read |
|---|---|---|---|---|---|---|
| 80 | Polycat | $221k | Polygon | deprecated, no fee revenue | Uniswap V2 | Uniswap V2 fork; check for an empty-pool / same-asset / fee-on-transfer accounting edge. |
| 81 | Polycat Dex | $99k | Polygon | deprecated, no fee revenue | Uniswap V2 | Uniswap V2 fork; check for an empty-pool / same-asset / fee-on-transfer accounting edge. |

## Redemption/mint math not invariant under splitting (rounding extraction)  ·  3 candidates
**Echoes:** USM ($136k, Aug 10)  
**Mechanism:** A mint/redeem path uses a mean of current & post-trade prices plus per-op state contraction and integer rounding, so splitting one large op into many small ones extracts more than a single call. Algo-stables and bonding-curve tokens are the family.  
**Decisive check / falsifier:** Is redeem/mint split-invariant (N small ops == 1 big op, net of fees)? Safe iff the pricing integral is exact or a floor/ceiling makes splitting strictly unprofitable.

| # | Protocol | Live TVL | Chains | Unwatched signal | Lineage | Personal read |
|---|---|---|---|---|---|---|
| 82 | Iron Finance | $316k | Polygon, Avalanche, Fantom | deprecated, no fee revenue | Frax | Frax; check redeem/mint is invariant under splitting into many small calls. |
| 83 | WESO DeFi | $395k | Terra | no fee revenue | — | Dexs; check redeem/mint is invariant under splitting into many small calls. |
| 84 | Frontier | $64k | Robinhood Chain | ~no revenue | — | Launchpad; check redeem/mint is invariant under splitting into many small calls. |

## Dedup & provenance

- All 84 names cleared `tools/check_new.py` against `results/discoveries/_exclusion_set.json` (2,144 names) and are folded into it with this push, so the next run won't re-surface them.
- Fresh victims themselves (Tectonic, Moonwell, Notional, Arrakis, Balancer, CometDEX, Reddio, Cozy, Secured Finance, Rocket, SAND, Allbridge, warp.green, …) are hard-excluded — this is the *next* set, not the hit set.
- Backing data: `DISC-20260908-008-candidates.json` (live TVL/chains/fork/deprecation per row).
- Not a verdict on any row; it is a ranked place to point the adversarial audit method next.
