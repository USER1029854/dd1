# Candidates to check — 39 non-repeating protocols, grounded in the last 6 months of incidents

> **What this is.** A shortlist of live protocols that *rhyme with a real incident from the trailing
> six-month window* and still hold money. Each is a **lead to check, not a confirmed finding**. The point
> is coverage: run this before a pattern's next occurrence and you have the maximum chance of catching it
> in time. A high place on the list is a triage order, never an exploit probability.

**Scope (as instructed):** on-chain root causes only — no off-chain key compromise, social engineering, or
infrastructure. Band **$50k ≤ TVL ≲ $30M** (below, nothing to save; above, assume the team already retains
auditors). Preference for **un-hit relatives on a shared or fresh public mechanism**, not the biggest names.

**No repetition — the thing you asked for.** Every row was checked against
`results/discoveries/_exclusion_set.json`, the union of the 629-name delivered ledger, every slug ever
written into `results/*.md`, and the run-2/run-3 candidates (**805 names**). Nothing here has been handed
over in any prior push. This file is additive: it does not overwrite anything.

**How to use.** Take a row, run its *decisive check* against the **deployed** artifact (verified/decompiled
source, or a fork at head) — then kill it with a cited guard or promote it. TVL is read at head
(DefiLlama current, 2026-08-29); a `~` marks a value carried from the 2026-08-27 universe snapshot where the
live endpoint didn't return a clean figure.

**Honesty.** These are reasoned leads from protocol metadata + the incident corpus. The EVM ones are
cheap to confirm; the non-EVM ones (Sui/Solana/Stellar/TON/Move/CosmWasm/Near) were **not** fork-verified
in this environment — the *reason* column is a feeling grounded in a fresh mechanism, exactly as asked, and
the *decisive check* is where the real audit begins. Some rows will be false leads; that is expected and fine.


## A. LP-share mint/burn priced off spot — echoes **Arrakis V1 / G-UNI** (2026-08-23)

*The vault issues an LP-share token and values it from the AMM's *instantaneous* price (Uniswap-V3 `slot0`, a DLMM active bin, a CLMM active tick). If the TWAP/deviation guard sits only on `rebalance()`, a flash-loan skews the price, mints shares cheap, restores, and burns rich. (Verified live on Arrakis V1's own fleet.)*

| # | Protocol | Chain(s) | TVL@head | Why it might lose money (the lead) | Decisive check |
|--:|---|---|--:|---|---|
| 1 | **Kodiak Islands** (`kodiak-islands`) | Berachain | $24.2M | ALM issuing LP-share tokens on Berachain; if mint()/burn() value the position off the pool spot tick (slot0) with the TWAP/deviation guard only on rebalance, a flash-skew mints cheap and burns rich. | Read the deployed vault mint/burn: is the valuation sqrtPrice/tick from spot, and is there a TWAP/deviation check on the mint path (not just rebalance)? |
| 2 | **ACryptoS** (`acryptos`) | Binance,Arbitrum,Avalanche | $10.5M | DefiLlama confirms it as an Automated Concentrated Liquidity Manager (ACLM) for V3 DEXs — the exact Arrakis surface. Confirm whether share mint/withdraw values the V3 position off spot tick or off the declared Chainlink oracle. | Trace ACLM deposit/withdraw share math to its price source; is there a TWAP/deviation guard on the mint path (not only rebalance)? |
| 3 | **DefiTuna Liquidity** (`defituna-liquidity`) | Solana | $0.6M | Solana CLMM liquidity manager; concentrated-liquidity share pricing off active tick is the Arrakis shape on a different VM. | Confirm deposit/withdraw doesn't value the position at the instantaneous active tick. |
| 4 | **Mito Finance** (`mito-finance`) | Injective | $0.4M | Injective ALM vaults; non-EVM ALM where mint/burn valuation guards are often thinner than EVM incumbents. | Confirm vault share issuance is not priced off an instantaneous AMM ratio. |
| 5 | **Metropolis DLMM Vaults** (`metropolis-dlmm-vaults`) | Sonic | $0.3M | DLMM (concentrated-liquidity) vaults on Sonic; DLMM bins make spot valuation especially skewable at a range edge. | Check that vault share mint values bins off a time-averaged, not active-bin, price. |

## B. Same-asset-swap / weighted-pool distinctness — echoes **CometDEX** (2026-08-25)

*Comet drained the Blend backstop because its swap never required `token_in != token_out`; a `USDC→USDC` loop corrupted reserves. New-VM AMM ports (Soroban, Sui/Move, Solana, TON, CosmWasm, Near) repeatedly drop distinctness/rounding invariants the EVM original enforced implicitly.*

| # | Protocol | Chain(s) | TVL@head | Why it might lose money (the lead) | Decisive check |
|--:|---|---|--:|---|---|
| 6 | **Rhea Dex** (`rhea-dex`) | Near | $27.9M | Largest Near DEX ($28M); Near VM asset accounting is a fresh, less-audited surface. | Same-asset-swap distinctness + rounding direction on Near. |
| 7 | **ston-fi** (`ston-fi`) | — | $26.4M | Largest TON DEX ($26M); TON jetton transfer/asynchrony model makes reserve reconciliation error-prone. | Verify jetton-in equals credited amount and same-jetton swaps are rejected. |
| 8 | **Meteora DAMM V2** (`meteora-damm-v2`) | Solana | $24.0M | Solana dynamic AMM v2; large TVL, new-VM pool accounting. | Confirm swap/deposit distinctness and reserve reconciliation. |
| 9 | **Bluefin Spot** (`bluefin-spot`) | Sui | $20.0M | Sui orderbook DEX; same self-match / settlement-invariant surface as any Move CLOB port. | Verify self-trade handling and settlement conservation on Move. |
| 10 | **Stellar DEX** (`stellar-dex`) | Stellar | $14.0M | DEX on Stellar/Soroban — the exact VM where Comet's missing token_in!=token_out drained the Blend backstop; new-VM AMMs frequently omit the distinctness guard. | Confirm the swap entry rejects token_in==token_out before touching reserves. |
| 11 | **Saphyre V3** (`saphyre-v3`) | Sei | $13.3M | Uniswap-V3 fork on Sei — a fork inherits parent bugs and rarely parent fixes; diff against upstream both ways. | Diff against Uniswap V3 upstream; enumerate added/removed guards on swap/mint. |
| 12 | **DeepBook V3** (`deepbook-v3`) | Sui | $12.3M | Sui on-chain CLOB and liquidity layer; the CometDEX analog here is a self-match / settlement-rounding gap (crossing your own orders, or same-asset settlement) in a Move port. | Check that self-trades and same-asset settlements can't net value out, and audit settlement rounding direction. |
| 13 | **Sushi Stellar** (`sushi-stellar`) | Stellar | $10.0M | Sushi deployment on Stellar/Soroban; a port to a new VM can drop invariants the EVM version enforced implicitly. | Verify the Soroban port forbids same-asset swaps and preserves reserve invariants. |
| 14 | **Astroport** (`astroport`) | Neutron,Terra2,Injective | $9.6M | CosmWasm AMM across Neutron/Terra2/Injective; multi-VM CosmWasm pools where asset-denom identity handling differs from EVM. | Check pair swap forbids same-denom and validates denom identity (no poisoned CW20/native mapping). |
| 15 | **Stellar AMM** (`stellar-amm`) | Stellar | $8.1M | Second Soroban AMM; same-VM relative of the Comet exploit. | Same-asset-swap distinctness check present? |
| 16 | **DeDust** (`dedust`) | TON | $5.4M | TON DEX; TON VM asset identity handling differs from EVM. | Confirm asset identity/distinctness and jetton accounting on swaps. |
| 17 | **Saber** (`saber`) | Solana | $5.2M | Solana stable-swap; stable-swap invariants on same-decimals assets are exactly where same-asset accounting bugs hide. | Same-asset-swap guard + curve invariant on equal reserves. |

## C. Thin-liquidity collateral on a manipulable oracle — echoes **Moonwell** (2026-08-27)

*Moonwell lost $8.8M when a low-liquidity token (MAMO) was posted as collateral and its price inflated to borrow real assets. Aave/Compound/Liquity forks on young chains routinely list low-float collateral priced by a single non-deep feed — the remedy is a risk parameter, not a code patch.*

| # | Protocol | Chain(s) | TVL@head | Why it might lose money (the lead) | Decisive check |
|--:|---|---|--:|---|---|
| 18 | **Neverland** (`neverland`) | Monad | $19.0M | Aave-V3 fork on Monad with RedStone/Chainlink; a young high-throughput chain with shallow spot books. | Thinnest listed collateral vs oracle manipulability. |
| 19 | **Bonzo Lend** (`bonzo-lend`) | Hedera | $16.9M | Aave-V2 fork on Hedera; V2 lineage lacks some V3 risk guards. | Confirm price-source and per-asset caps on listed collateral. |
| 20 | **Seamless V2** (`seamless-v2`) | Ethereum,Base | $15.5M | Aave-V3 fork on Base/Ethereum; even mature-chain forks list long-tail collateral on RedStone feeds. | Enumerate collaterals; any thin asset on a manipulable feed with a high LTV? |
| 21 | **Vena Finance** (`vena-finance`) | Fluent | $12.0M | Aave-V3 fork on Fluent, Pyth oracle; new-chain lending markets often list low-float collateral. | Which collaterals are thin, and can spot be moved cheaply vs the borrow they unlock? |
| 22 | **YeiLend** (`yeilend`) | Sei | $10.2M | Aave-V3 fork on Sei with Api3/Pyth/RedStone; multiple feeds don't help if the collateral's spot is thin. | Identify the thinnest collateral and price the borrow it unlocks against manipulation cost. |
| 23 | **HypurrFi Pooled** (`hypurrfi-pooled`) | Hyperliquid L1 | $8.6M | Aave-V3 fork on Hyperliquid L1; Pyth/RedStone feeds on a young chain with thin spot markets. | Per-collateral liquidity vs oracle; flash-manipulability of the cheapest listed asset. |
| 24 | **Enosys Loans** (`enosys-loans`) | Flare | $8.0M | Liquity-V2 fork on Flare (CDP); Liquity forks price collateral off feeds that on a small chain can be thin. | Collateral oracle source + redemption/liquidation pricing robustness. |
| 25 | **MORE Markets** (`more-markets`) | Flow | $7.4M | Aave-V3 fork on Flow, Pyth; Flow spot liquidity is shallow. | Thin-collateral enumeration + oracle manipulability. |
| 26 | **Solera** (`solera`) | Plume Mainnet,Hemi | $4.7M | Aave-V3 fork on Plume/Hemi with Stork/eOracle; brand-new chains + non-Chainlink feeds + RWA collateral. | Per-collateral spot depth vs oracle; is any RWA/low-float asset cheaply movable? |
| 27 | **LayerBank** (`layerbank`) | RSK,Manta,BOB | $3.7M | Compound-V2 fork across RSK/Manta/BOB; Compound-V2 forks are the classic thin-collateral-listing victims. | Per-market collateral factor + oracle; cheapest manipulable listed asset. |
| 28 | **Extra Finance Xlend** (`extra-finance-xlend`) | Base,Optimism | $2.5M | Aave-V3-style lending on Base/Optimism; leveraged-farming lenders list LP and long-tail collateral. | Which collaterals are LP/thin, and how is each priced? |

## D. Mint not bound to a verified source burn — echoes **Sandbox / Allbridge / warp.green** (Aug 2026)

*Three fresh bridge losses all minted or credited on a *message/attestation* the code trusted without proving a real burn/lock happened at the source. Mint/burn bridges that verify the envelope but not the source event are the shape.*

| # | Protocol | Chain(s) | TVL@head | Why it might lose money (the lead) | Decisive check |
|--:|---|---|--:|---|---|
| 29 | **TxFlow Bridge** (`txflow-bridge`) | Arbitrum | $16.4M | Cross-chain liquidity/settlement layer holding ~$16M; the fresh bridge losses all credited on a message the code trusted without a proven source lock/burn. | Confirm every credited/settled amount is bound to a verified source-chain lock or burn, not just an attested message. |
| 30 | **pNetwork** (`pnetwork`) | Binance,Ethereum,Ultra | $13.1M | Multi-chain mint/burn bridge; prior pNetwork incidents + the fresh mint-on-unverified-burn pattern make its message->mint binding worth re-checking. | Is each mint bound to a verified burn on the source (not just an attested message body)? |
| 31 | **Universal Bridge** (`universal-bridge`) | Ethereum | $6.9M | Issues 80+ 1:1 wrapped assets (uXRP, uSUI, uSOL) on Ethereum; wrapped-asset mints must be bound to a proven reserve/lock, not an attestation alone (note: some backing is custodial = partly off-chain). | Confirm the on-chain mint authorization requires a verified lock/proof; enumerate who can mint each uAsset. |
| 32 | **Wan Bridge** (`wan-bridge`) | Ethereum,Binance,Ripple | $6.8M | Wanchain cross-chain mint/burn; validator-signature bridges are where forged-source mints recur. | Confirm the mint verifies the source burn/lock, and signer-set integrity. |

## E. LST/LRT share-rate read as spot, and cross-chain mint trust — echoes **KelpDAO rsETH** (2026-04) + the share-rate family

*An LST/LRT share token used as collateral or bridged cross-chain inherits two surfaces: a share-rate read at spot (manipulable in one trade), and a cross-chain mint whose trust (DVN set / delegate / peer) can be seized. KelpDAO's rsETH lost $292M on the second.*

| # | Protocol | Chain(s) | TVL@head | Why it might lose money (the lead) | Decisive check |
|--:|---|---|--:|---|---|
| 33 | **Bedrock uniETH** (`bedrock-unieth`) | Ethereum | $25.1M | uniETH LRT; LRTs bridged cross-chain (OFT) or used as collateral inherit both KelpDAO's forged-mint and share-rate-as-spot surfaces. | Cross-chain mint verification + any spot share-rate reads. |
| 34 | **StakeStone STONE** (`stakestone-stone`) | Ethereum | $21.0M | STONE is an omnichain LST explicitly designed to move cross-chain; the cross-chain trust config is the KelpDAO/StakeDAO surface. | DVN count + delegate immutability on STONE's cross-chain path; share-rate read robustness. |
| 35 | **Hylo LSTs** (`hylo-lsts`) | Solana | $20.8M | Solana LST set; share-rate-as-price and cross-program composability risk. | Rate-read robustness where hylo LSTs back other positions. |
| 36 | **RHEA LST** (`rhea-lst`) | Near | $18.7M | Near LST ($18M); its staked-NEAR rate, if read spot by any Near money-market, is manipulable. | Where rhea LST backs borrow, is its exchange rate read spot or smoothed? |
| 37 | **Infrared Finance** (`infrared-finance`) | Berachain | $18.3M | Berachain liquid staking ($20M); iBGT/validator-staking share tokens widely used as collateral in the young Berachain DeFi stack. | Confirm the LST rate used by downstream markets is not the instantaneous vault ratio. |
| 38 | **Volo LST** (`volo-lst`) | Sui | $16.9M | Sui LST; its share token is read as collateral elsewhere — if any market prices it off an instantaneous exchange rate it is manipulable. | Where is volo's LST used as collateral, and is its rate read spot or smoothed? |

## F. Deposit-shares confer votes that can disable the timelock — echoes **Term Finance** (2026-08-23)

*Term lost $8.5M when an attacker acquired majority vault voting power, passed a proposal to disable the timelock, and drained. Any vault where deposit/stake weight can pass a fund-moving proposal with a removable timelock has this shape.*

| # | Protocol | Chain(s) | TVL@head | Why it might lose money (the lead) | Decisive check |
|--:|---|---|--:|---|---|
| 39 | **Pickle** (`pickle`) | Ethereum,Polygon,Optimism | $4.8M | Governance-driven yield vaults; where deposit/stake confers votes and a majority can pass a fund-moving proposal, cheap-quorum capture drains vaults. | Can deposit-derived voting weight pass a proposal that moves vault funds, and is the timelock removable by that same vote? |

---

**39 candidates**, grouped by the incident each echoes. Method: the DefiLlama universe (8,103 protocols)
filtered to the band + alive + not-previously-delivered (1,339 eligible), bucketed by the mechanism
families derived from the trailing-6-month SlowMist corpus, then curated for genuine mechanism fit and
live value. Tooling and corpus: `tools/`, `incidents/`, exclusion set `results/discoveries/_exclusion_set.json`.
Chain access read-only.
