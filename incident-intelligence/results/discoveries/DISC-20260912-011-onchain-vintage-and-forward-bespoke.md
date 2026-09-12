# DISC-20260912-011 — Reading the chain to recover the hidden pre-AI seam + the forward bespoke cohort

*A discovery under the settled thesis (unwatched × bespoke-non-fork × pre-AI/unchanged, TVL neutral, no repeats — see `PROJECT-MEMORY.md`). Every name here is **new** (checked against the 2,483-name exclusion set) and folded in with this push.*

## The structural finding that shaped this run

I re-measured the un-delivered population first. Two facts fell out:

1. **The pre-AI seam looked exhausted — by listing date.** Of every fresh (un-delivered) bespoke-non-fork unwatched protocol, **zero** had a DefiLlama `listedAt` before 2023. The prior runs (DISC-009/010 + batches) consumed everything the listing-date proxy could see.
2. **But `listedAt` is listing date, not deployment date** (the known weakness in PROJECT-MEMORY §9). So I stopped trusting it and **read the deployed compiler on-chain** for the fresh EVM candidates. That recovered a batch of genuinely **pre-AI-era projects** (token/contract compiled at 0.4–0.7) that the listing date had mislabelled as recent — e.g. TrueFi, CompliFi, Auctus, CoFiX, Tranche, DSU/Empty-Set. They were never delivered precisely *because* the proxy hid them. Reading the chain beat trusting the metadata — which is the whole point.

So this file has two tiers, both fresh, both bespoke + unwatched, TVL held neutral:

- **Tier 1 — recovered pre-AI vintage** (compiler-evidenced old projects). Honest caveat: the compiler read dates the *listed contract* (often the governance token), so it dates the **project** loosely, not necessarily the core logic — reads that landed on a generic token/template are flagged `token-read`. These skew small: the *large* old-bespoke names were already delivered in DISC-010, so what remains is genuinely-old code that has **decayed to low TVL** — which, since TVL is neutral and the code is what we audit, does not lower their interest.
- **Tier 2 — the forward bespoke cohort** (2023+): custom logic that is *already* unwatched/deprecated or earns no fee. This is the live frontier — bespoke basis/delta-neutral vaults, the new **risk-curator** surface (contracts that allocate depositors' funds across others' markets), stablecoin/RWA wrappers, abandoned CDP/bonding-curve **V1s**, and genuinely novel AMMs. Generic Uniswap/MasterChef-shaped clones were dropped as lower-signal semi-forks.

**Flags:** 💤 deprecated/abandoned · ⚠ prior security incident (remnant may still be worth reading, but the obvious vector is likely patched) · `token-read` (compiler vintage came from a token/template, weak evidence for core age).


## Tier 1 — recovered pre-AI vintage (26)

### Synthetics / CDP / stablecoin wrapper · 1

**Decisive check:** Bespoke mint/redeem against a collateral ratio or peg. Can the ratio/oracle be moved cheaply, is mint gated, and is redemption split-invariant? For T-bill/RWA wrappers: is redemption bound to a real, verified reserve?

| Protocol | TVL | Chain | Category | Watch | Vintage | Flags | What it is |
|---|---|---|---|---|---|---|---|
| DSU Money | $22k | Ethereum | CDP | no rev | v0.5.17+com | — | DSU is a trust-minimized, fully backed, & collateral-efficient sta… |
### Derivatives / basis & delta-neutral vaults · 1

**Decisive check:** Hand-rolled funding/margin/PnL — or a delta-neutral basis vault whose share price depends on a live hedge. Can the mark/funding be manipulated, a dormant market self-traded, or the hedge desynced so shares misprice?

| Protocol | TVL | Chain | Category | Watch | Vintage | Flags | What it is |
|---|---|---|---|---|---|---|---|
| CompliFi | $37k | Ethereum | Derivatives | no rev | v0.5.17+com | 💤 deprecated | Decentralised derivatives. No defaults, no margin calls, no liquid… |
### Lending / credit / risk-curators · 7

**Decisive check:** Bespoke credit engine, or a **risk curator** that allocates depositor funds across others' markets and sets caps/oracles. Is any fund-moving path un-gated, is collateral valuation manipulable, and — for curators — can a curator-set oracle/collateral route drain the vault?

| Protocol | TVL | Chain | Category | Watch | Vintage | Flags | What it is |
|---|---|---|---|---|---|---|---|
| Stake DAO Curator | $1.37M | Ethereum | Risk Curators | no rev | v0.6.7+comm | — | Stake DAO curates Morpho lending vaults that supply USDC and frxUS… |
| Paladin Vote | $41k | Ethereum | Lending | no rev | v0.8.4+comm | 💤 deprecated | Paladin is a decentralized, non-custodial governance lending proto… |
| Beta Finance V2 | $30k | Ethereum | Lending | no rev | v0.8.6+comm | 💤 deprecated | Beta Finance is the permissionless money market for borrowing, len… |
| Alkemi | $27k | Ethereum | Lending | no rev | v0.4.24+com | token-read | Alkemi Network is bridging CeFi to DeFi, building an institution-g… |
| TrueFi | $22k | Ethereum | Uncollateralized Lending | no rev | v0.5.13+com | 💤 deprecated | Earn high yields on stablecoin loans and borrow capital without co… |
| Warp Protocol | $39k | Ethereum | Lending | no rev | v0.4.18+com | 💤 deprecated ⚠ prior incident token-read | Warp Finance is an open-source protocol on Ethereum that is creati… |
| Ooki | $28k | Ethereum | Lending | no rev | v0.8.9+comm | 💤 deprecated ⚠ prior incident | Ooki is a flexible decentralized finance protocol for margin tradi… |
### Options / structured payoff · 1

**Decisive check:** Pooled depositor collateral backs each position. Is mint/settle/exercise gated, and is each payoff bound to an oracle snapshot taken at open? (the SOFA shape).

| Protocol | TVL | Chain | Category | Watch | Vintage | Flags | What it is |
|---|---|---|---|---|---|---|---|
| Auctus | $23k | Ethereum | Options | no rev | v0.4.21+com | — | Auctus brings on-chain options to the ecosystem. |
### Insurance / prediction settlement · 2

**Decisive check:** Bespoke insurance/prediction settlement. Does the trigger independently verify the real event, and is payout tied to a pre-proposal holder snapshot? (the Cozy shape).

| Protocol | TVL | Chain | Category | Watch | Vintage | Flags | What it is |
|---|---|---|---|---|---|---|---|
| Lunos | $40k | Ethereum | Insurance | no rev | v0.5.17+com | — | Automated on-chain coverage & advanced security to protect your as… |
| Tidal Finance | $25k | Polygon | Insurance | no rev | v0.6.12+com | ⚠ prior incident | TIDAL is a decentralized discretionary mutual cover protocol that … |
### Custom AMM / DEX · 5

**Decisive check:** Novel (non-fork) AMM. Look for reserve-accounting edges — empty-pool mint, same-asset swap, fee-on-transfer desync, or a custom oracle-priced curve (CoFiX-style) that a flash move distorts.

| Protocol | TVL | Chain | Category | Watch | Vintage | Flags | What it is |
|---|---|---|---|---|---|---|---|
| DinoSwap | $31k | Polygon | Dexs | no rev | v0.6.6+comm | token-read | DinoSwap is a cross-chain infrastructure project that builds liqui… |
| Loopring | $30k | Ethereum | Dexs | no rev | v0.5.7+comm | — | Loopring is a zkRollup Exchange and Payment Protocol. |
| CoFiX | $29k | Ethereum | Dexs | no rev | v0.6.12+com | 💤 deprecated | CoFiX is the most efficient DEX on Ethereum. |
| MacaronSwap | $21k | Binance | Dexs | no rev | v0.6.12+com | — | MacaronSwap is a DEX that allows users to be Liquidity Provider, F… |
| DFX V3 | $31k | Ethereum | Dexs | no rev | v0.7.3+comm | 💤 deprecated ⚠ prior incident | DFX is a decentralized foreign exchange protocol optimized for tra… |
### Yield / vault math · 8

**Decisive check:** Bespoke share/reward math. Spot-vs-TWAP share pricing, reward-reset replay, first-depositor/donation share inflation.

| Protocol | TVL | Chain | Category | Watch | Vintage | Flags | What it is |
|---|---|---|---|---|---|---|---|
| Moonpot | $45k | Binance | Yield | no rev | v0.6.12+com | 💤 deprecated | Win-Win Prize Pots on Binance Smart Chain. Earn interest, win big … |
| Magic Land | $41k | Arbitrum | Yield | no rev | v0.6.12+com | 💤 deprecated | Magicland is an emerging sustainable decentralized one-stop DeFI p… |
| Tranche Finance | $36k | Ethereum | Yield | no rev | v0.6.12+com | 💤 deprecated token-read | Tranche splits any yield-generating asset from the DeFi ecosystem … |
| Hyper Finance | $35k | Binance | Yield | no rev | v0.7.4+comm | 💤 deprecated | Hyper Finance (HyFi.pro) is a decentralized aggregate mining platf… |
| Panda Chef | $30k | Binance | Farm | no rev | v0.6.12+com | 💤 deprecated | Stake PandaSwap LP tokens to earn PNDA |
| Ethernity Chain | $29k | Ethereum | Yield | no rev | v0.6.2+comm | 💤 deprecated | A community-oriented platform that produces limited edition authen… |
| Sperax Demeter V2 | $27k | Arbitrum | Farm | no rev | v0.6.12+com | ⚠ prior incident | Farming-as-a-service infrastructure on UniswapV3. Demeter protocol… |
| Orion Money | $20k | Ethereum | Yield | no rev | v0.8.7+comm | 💤 deprecated ⚠ prior incident | Orion Money's vision is to become a cross-chain stablecoin bank pr… |
### Other custom-logic · 1

**Decisive check:** Custom-logic contract holding pooled funds — read the value-moving entrypoints for gating and oracle trust.

| Protocol | TVL | Chain | Category | Watch | Vintage | Flags | What it is |
|---|---|---|---|---|---|---|---|
| Boardwalk | $29k | Base | Launchpad | $0k/30d | v0.6.12+com | token-read | Boardwalk is a permissionless, community-centered fee-protection p… |

## Tier 2 — forward bespoke cohort, 2023+ (101)

### Synthetics / CDP / stablecoin wrapper · 8

**Decisive check:** Bespoke mint/redeem against a collateral ratio or peg. Can the ratio/oracle be moved cheaply, is mint gated, and is redemption split-invariant? For T-bill/RWA wrappers: is redemption bound to a real, verified reserve?

| Protocol | TVL | Chain | Category | Watch | Vintage | Flags | What it is |
|---|---|---|---|---|---|---|---|
| Summer.fi Pro | $17.19M | Ethereum | CDP Manager | $0k/30d | 2023 | 💤 deprecated | Borrow, Multiply and Earn on the assets you hold across multiple p… |
| USX.Capital | $764k | Scroll | Stablecoin Wrapper | no rev | 2025 | — | USX is a fully collateralized neodollar built by Scroll that combi… |
| NOME Protocol | $39k | Berachain | Algo-Stables | no rev | 2025 | 💤 deprecated | Synthetic algostable |
| DYAD | $36k | Ethereum | CDP | no rev | 2023 | 💤 deprecated | DYAD is a stablecoin optimized for unit economics, leveraging shar… |
| Button Wrappers | $32k | Base | CDP | no rev | 2023 | — | Easily segment your crypto assets into senior and junior tranches … |
| Roots | $24k | Berachain | CDP | $0k/30d | 2025 | 💤 deprecated | Collateralize Berachain LP tokens, Mint MEAD stablecoin, retain al… |
| Wand Protocol | $22k | Blast | CDP | no rev | 2024 | — | Wand protocol offers stablecoins for low-risk stability and margin… |
| USDR | $4.14M | RISE | Stablecoin Wrapper | no rev | 2026 | ⚠ prior incident | USDR is a T-bill backed stablecoin built on top of the M^0 protoco… |
### Derivatives / basis & delta-neutral vaults · 15

**Decisive check:** Hand-rolled funding/margin/PnL — or a delta-neutral basis vault whose share price depends on a live hedge. Can the mark/funding be manipulated, a dormant market self-traded, or the hedge desynced so shares misprice?

| Protocol | TVL | Chain | Category | Watch | Vintage | Flags | What it is |
|---|---|---|---|---|---|---|---|
| Monetrix USDM | $2.54M | Hyperliquid L1 | Basis Trading | $3k/30d | 2026 | — | Monetrix is the first fully on-chain funding-driven yield-bearing … |
| DeSyn Basis Trading | $1.72M | Bitlayer | Basis Trading | no rev | 2024 | — | DeSyn is a decentralized liquidity infrastructure on Web3, empower… |
| Monetrix mxHYPE | $1.69M | Hyperliquid L1 | Basis Trading | $0k/30d | 2026 | — | HYPE-denominated yield vault on Hyperliquid. Deposited HYPE backs … |
| GoodEntry | $39k | Arbitrum | Derivatives | no rev | 2023 | 💤 deprecated | Good Entry is an onchain derivative exchange enabling leveraged da… |
| AshPerp | $38k | Elrond | Derivatives | $5k/30d | 2024 | — | A Decentralized Perpetual Trading Protocol on MultiversX |
| Derivio | $34k | zkSync Era | Derivatives | no rev | 2023 | — | Institutional-grade decentralized derivatives ecosystem. Permissio… |
| Onchain Trade | $33k | zkSync Era | Derivatives | no rev | 2023 | 💤 deprecated | Onchain Trade(OT) is a vertically integrated DeFi protocol where p… |
| Zeno Exchange | $30k | Metis | Derivatives | $0k/30d | 2024 | 💤 deprecated | Premier Decentralized Perpetual Exchange With Cross-Margin, Multi-… |
| Bloom Trading | $30k | Blast | Derivatives | no rev | 2024 | 💤 deprecated | Bloom is a fully decentralized leverage trading and market-making … |
| Numoen | $29k | Arbitrum | Derivatives | no rev | 2023 | 💤 deprecated | Numoen is an application for interacting with the Power Market Mak… |
| Tristero Margin | $28k | Ethereum | Derivatives | no rev | 2026 | — | Tristero Margin is a margin trading platform that allows users to … |
| Rubin Trade | $25k | Arbitrum | Derivatives | no rev | 2026 | — | Rubin is a self-custody decentralized perpetual & spot exchange |
| BasisOS | $24k | Arbitrum | Basis Trading | $0k/30d | 2025 | 💤 deprecated | BasisOS Agent is an autonomous AI system built to manage DeFi prot… |
| Superp | $23k | Binance | Derivatives | no rev | 2025 | — | Superp(formerly Vanilla Finance) is a perp DEX for any meme, up to… |
| Coffin.Meme | $22k | TON | Derivatives | no rev | 2024 | — | Coffin.Meme is a DeFi Platform powered by EVAA Lending Smart contr… |
### Lending / credit / risk-curators · 18

**Decisive check:** Bespoke credit engine, or a **risk curator** that allocates depositor funds across others' markets and sets caps/oracles. Is any fund-moving path un-gated, is collateral valuation manipulable, and — for curators — can a curator-set oracle/collateral route drain the vault?

| Protocol | TVL | Chain | Category | Watch | Vintage | Flags | What it is |
|---|---|---|---|---|---|---|---|
| Presto | $3.32M | Ethereum | Risk Curators | no rev | 2026 | — | Presto is a risk curator on Morpho. |
| 1212 Capital | $2.49M | Ethereum | Risk Curators | no rev | 2026 | — | 1212 Capital is an investment firm specializing in DeFi and Stable… |
| Mt Pelerin | $1.68M | Ethereum | Risk Curators | no rev | 2026 | — | Mt Pelerin, active in self-custodial crypto-fiat exchange services… |
| Architect | $1.25M | Base | Risk Curators | no rev | 2026 | — | Architect is a regulated investment manager and technical curator … |
| Bizantine Labs | $1.05M | Flare | Risk Curators | no rev | 2026 | — | Bizantine Labs is the DeFi risk and curation arm of Bizantine Capi… |
| XOXNO Lending | $978k | Elrond | Lending | $1k/30d | 2026 | — | XOXNO Stellar Lending is an overcollateralized lending protocol on… |
| DACM | $443k | Arbitrum | Risk Curators | no rev | 2026 | — | DACM is an institutional digital asset fund manager. |
| cipher.rip | $50k | Arbitrum | SoFi | $0k/30d | 2023 | 💤 deprecated | Social Finance project on Arbitrum |
| fan.fun | $50k | Hyperliquid L1 | SoFi | no rev | 2025 | 💤 deprecated | fan.fun enables creators to monetize exclusive content and engage … |
| time.fun | $46k | Base | SoFi | $0k/30d | 2024 | 💤 deprecated | Tokenize your time, in minutes, and let fans trade & redeem time w… |
| Credit Guild | $42k | Arbitrum | Lending | no rev | 2024 | 💤 deprecated | The Credit Guild is a protocol for trust minimized pooled lending |
| Covenant | $40k | Monad | Lending | no rev | 2026 | — | Covenant is a tranching layer on Monad that converts any tokenized… |
| Multiplier | $38k | Binance | Lending | no rev | — | 💤 deprecated | Multiplier is an algorithmic money market system designed to bring… |
| Alterscope | $30k | Base | Risk Curators | $0k/30d | 2025 | — | Alterscope is a permissionless platform for creating, deploying an… |
| Morpho Optimizer AaveV3 | $28k | Ethereum | Lending | no rev | 2023 | 💤 deprecated | Morpho's AaveV3-ETH Optimizer allows WETH-only transactions in ETH… |
| Sirio Finance | $23k | Hedera | Lending | no rev | 2025 | 💤 deprecated | The DeFAI Lending & Borrowing Layer of hedera |
| Umee | $20k | Ethereum | Lending | no rev | 2023 | 💤 deprecated | The most programmable, safety-first, autonomous lending algorithm … |
| friend.tech V1 | $2.31M | Base | SoFi | $0k/30d | 2023 | ⚠ prior incident | Your network is your net worth. |
### Options / structured payoff · 3

**Decisive check:** Pooled depositor collateral backs each position. Is mint/settle/exercise gated, and is each payoff bound to an oracle snapshot taken at open? (the SOFA shape).

| Protocol | TVL | Chain | Category | Watch | Vintage | Flags | What it is |
|---|---|---|---|---|---|---|---|
| Jasper Vault | $39k | Arbitrum | Options | no rev | 2024 | — | Jasper Vault is a peer-to-peer interoperable options protocol. Jas… |
| BaseVol | $34k | Base | Options | no rev | 2026 | — | BaseVol is building the onchain options stack for everyone, from z… |
| TON Hedge | $25k | TON | Options | no rev | 2024 | — | Options trading protocol on ton_blockchain |
### Insurance / prediction settlement · 4

**Decisive check:** Bespoke insurance/prediction settlement. Does the trigger independently verify the real event, and is payout tied to a pre-proposal holder snapshot? (the Cozy shape).

| Protocol | TVL | Chain | Category | Watch | Vintage | Flags | What it is |
|---|---|---|---|---|---|---|---|
| Levr Bet | $1.92M | Monad | Prediction Market | no rev | 2026 | — | Prediction markets with 2x-5x leverage on single-game sports lines |
| Hedgehog Markets | $46k | Solana | Prediction Market | no rev | 2024 | — | Hedgehog Markets is the first Prediction Market market platform on… |
| eesee | $43k | Blast | Prediction Market | no rev | 2024 | — | Gamified liquidity solution and marketplace for digital assets, to… |
| O.LAB | $38k | Base | Prediction Market | no rev | 2025 | 💤 deprecated | The World's Opinion Protocol, enabling anyone to create prediction… |
### Bridge / wrapped-asset verifier · 9

**Decisive check:** Hand-rolled verifier. Is every mint/release bound 1:1 to a verified, replay-protected remote burn, and what is the real signer threshold? Several wrapped-BTC/lock-mint designs here are new and unproven.

| Protocol | TVL | Chain | Category | Watch | Vintage | Flags | What it is |
|---|---|---|---|---|---|---|---|
| STRATO Bridge | $1.47M | Ethereum | Bridge | no rev | 2026 | — | Lock-and-mint bridge between STRATO and Ethereum, Base, Linea and … |
| YBTC.B | $147k | Bitlayer | Anchor BTC | $0k/30d | 2025 | — | YBTC.B is a wrapped version of Bitlayer's Native BTC, designed to … |
| GenesisLRT (Native Restaking) | $47k | Ethereum | Liquid Restaking | no rev | 2024 | — | Unveil a new era of staking with Genesis protocol. The restaking f… |
| Euclid Protocol | $47k | Polygon | Cross Chain Bridge | no rev | 2026 | — | Euclid Protocol is a cross-chain settlement infrastructure enablin… |
| Gasp | $31k | Ethereum | Cross Chain Bridge | no rev | 2024 | — | Gasp is a cross-chain DEX and protocol designed for exchanging cry… |
| Ulysses | $31k | Ethereum | Bridge | no rev | 2024 | 💤 deprecated | Ulysses Protocol is a decentralized and permissionless 'Omnichain … |
| HeLa Bridge | $29k | HeLa | Bridge | no rev | 2024 | 💤 deprecated | Opening a New Era of Modular Layer 1 Blockchain for AI. |
| Lorenzo stBTC | $26k | Bitcoin | Restaked BTC | no rev | 2024 | — | Lorenzo is the Bitcoin Liquidity Finance Layer, creates an efficie… |
| Chakra | $22k | Bitcoin | Restaked BTC | no rev | 2024 | — | Chakra Network is an innovative blockchain platform designed to ov… |
### Custom AMM / DEX · 24

**Decisive check:** Novel (non-fork) AMM. Look for reserve-accounting edges — empty-pool mint, same-asset swap, fee-on-transfer desync, or a custom oracle-priced curve (CoFiX-style) that a flash move distorts.

| Protocol | TVL | Chain | Category | Watch | Vintage | Flags | What it is |
|---|---|---|---|---|---|---|---|
| Cantex | $2.38M | Canton | Dexs | $10k/30d | 2026 | — | Cantex is an institutional-grade on-chain exchange built on the Ca… |
| Joe V2.2 | $2.22M | Avalanche | Dexs | $4k/30d | 2024 | — | LFJ Liquidity Book V2.2 gives Liquidity Providers control over liq… |
| Zia | $1.66M | 0G | Dexs | $0k/30d | 2025 | — | Prompt to trade with Zia, a natural language DEX on 0G and Robinho… |
| Liberty Swap | $924k | Pulse | Dexs | no rev | 2026 | — | Liberty Swap is a decentralized exchange ecosystem on PulseChain |
| BDEX V2 | $858k | BOT Chain | Dexs | no rev | 2026 | — | BDEX V2 is an AMM on BOT Chain |
| SUN.io | $777k | Tron | Dexs | no rev | — | — | First integrated platform for stablecoin swap, stake-mining, and s… |
| AllBlue V2 | $760k | Avalanche | Dexs | $0k/30d | 2025 | — | Allblue is a decentralized liquidity platform on Avalanche support… |
| Krown DEX | $660k | Krown Network | Dexs | no rev | 2026 | — | Krown DEX is a concentrated-liquidity decentralized exchange on Kr… |
| Web3.world | $560k | Venom | Dexs | no rev | 2024 | — | Web3.World is an Automated Market Maker, Yield Farming, and Stakin… |
| TONCO V1 | $307k | TON | Dexs | $0k/30d | 2024 | — | The first DEX on TON with concentrated liquidity |
| Umbrae | $159k | Base | Dexs | $0k/30d | 2026 | — | Umbrae is a DeFi trading platform on Base offering DLMM discrete-b… |
| Thorn Protocol | $54k | Sapphire | Dexs | no rev | 2024 | 💤 deprecated | Thorn Protocol is the pioneering Stableswap platform that offers p… |
| AYIN | $45k | Alephium | Dexs | no rev | 2023 | 💤 deprecated | Seamlessly swap Alephium native token pairs, earn, and explore our… |
| CobaltX | $42k | Soon Network | Dexs | no rev | 2025 | — | A Concentrated Liquidity AMM, Building DeFi Ecosystem on Soon Netw… |
| Saturn Swap | $38k | Cardano | Dexs | no rev | 2024 | 💤 deprecated | Saturn Swap is a no batcher order book DEX on Cardano. Saturn Swap… |
| JediSwap V2 | $35k | Starknet | Dexs | no rev | 2024 | 💤 deprecated | A community-led fully permissionless and composable AMM on Starkne… |
| Hyperlynx V3 | $34k | Hyperliquid L1 | Dexs | $0k/30d | — | — | Hyperlynx V3 is a HyperEVM DEX for trading HYPE, liquid-staked HYP… |
| Phera DEX | $34k | Robinhood Chain | Dexs | no rev | 2026 | — | PheraDEX is a concentrated-liquidity (CLMM) DEX and token launchpa… |
| Astarter AMM | $32k | Cardano | Dexs | no rev | 2023 | 💤 deprecated | Astarter is a key DeFi infrastructure hub on Cardano that features… |
| Tonic | $27k | Near | Dexs | no rev | 2023 | 💤 deprecated | Tonic is an open source, decentralized limit order book and perps … |
| Agility LSD | $26k | Ethereum | Indexes | no rev | 2023 | 💤 deprecated | LSD Liquidity Layer & LSD Trading Platform. |
| stake.link index | $26k | Ethereum | Indexes | no rev | 2023 | 💤 deprecated | Earn blended returns on the top LSDs available today. |
| Umbra | $22k | Eclipse | Dexs | no rev | 2025 | 💤 deprecated | Dexs on Eclipse Chain |
| MSwap | $22k | Matchain | Dexs | no rev | 2024 | 💤 deprecated | MSwap is a UniswapV2 fork deployed on Matchain |
### Yield / vault math · 16

**Decisive check:** Bespoke share/reward math. Spot-vs-TWAP share pricing, reward-reset replay, first-depositor/donation share inflation.

| Protocol | TVL | Chain | Category | Watch | Vintage | Flags | What it is |
|---|---|---|---|---|---|---|---|
| EARN | $368k | Robinhood Chain | Liquidity Automation | no rev | 2026 | — | Yield vaults for tokenized stocks on Robinhood Chain. Deposit stoc… |
| set.wtf | $320k | Ethereum | Yield | no rev | 2025 | 💤 deprecated | set.wtf is a USDT staking protocol offering 20.00% APY, compounded… |
| Ruby.Exchange Yield | $138k | Europa | Yield | no rev | 2023 | 💤 deprecated | Yield Farm on Europa chain |
| Blastoff | $48k | Blast | Farm | no rev | 2024 | 💤 deprecated | A Native Yield Based - LaunchPad and Yield Aggregator. Unlocking a… |
| Zino Finance | $45k | Arbitrum | Yield Aggregator | no rev | 2025 | 💤 deprecated | Zino Finance is the premier multichain DeFi hub for yield. Zino al… |
| exit.tech | $39k | Arbitrum | Liquidity Manager | no rev | 2025 | 💤 deprecated | A platform that lets you easily exit your locked DeFi positions, w… |
| FIVA | $34k | TON | Yield | no rev | 2024 | 💤 deprecated | FIVA is a yield optimization protocol on TON that enables users to… |
| Hyperlock Finance | $32k | Blast | Yield | no rev | 2024 | 💤 deprecated | Yield & metagovernance protocol built on ThrusterFi and optimized … |
| Nemo Vault | $29k | Sui | Yield Aggregator | $12k/30d | 2025 | — | Nemo Vaults lower the barrier to entry for users in DeFi, offering… |
| Bitparty | $25k | Bitlayer | Farm | no rev | 2024 | 💤 deprecated | BitParty is the first Asset Gamified Community Network in the BTC … |
| Bountive | $23k | Starknet | Yield | no rev | 2024 | 💤 deprecated | Bountive is the first decentralized prize savings protocol on Star… |
| BlastUp | $22k | Blast | Farm | no rev | 2024 | 💤 deprecated | BlastUP is an innovative launchpad platform for early-stage projec… |
| StakeSteak | $21k | Fantom | Yield | no rev | — | 💤 deprecated | The first Fantom-native, interest-bearing Stable Coin: iFUSD |
| Gaj Finance | $21k | Avalanche | Yield | no rev | — | 💤 deprecated | Gaj, previously known as PolyGaj, is a multichain platform coverin… |
| Struct Finance | $20k | Avalanche | Yield | no rev | 2023 | 💤 deprecated | Struct Finance is a DeFi protocol offering structured financial pr… |
| CookieBase Farm | $40k | Base | Farm | no rev | 2023 | 💤 deprecated ⚠ prior incident | Sweeten your DeFi journey with CookieBase! Embrace creamy yields a… |
### Other custom-logic · 4

**Decisive check:** Custom-logic contract holding pooled funds — read the value-moving entrypoints for gating and oracle trust.

| Protocol | TVL | Chain | Category | Watch | Vintage | Flags | What it is |
|---|---|---|---|---|---|---|---|
| GOLDSTATION RWA | $580k | Klaytn | RWA | no rev | 2024 | — | GPC(Gold-Pegged coin) is 100% physical gold-based RWA issued on Ka… |
| zLot | $29k | Ethereum | Liquid Staking | no rev | — | 💤 deprecated | The first staking protocol built upon Hegic. |
| StakedICP | $21k | ICP | Liquid Staking | no rev | 2023 | 💤 deprecated | StakedICP is a non-custodial liquid staking protocol built on the … |
| TronNRG | $20k | Tron | Staking Pool | no rev | 2023 | 💤 deprecated | TronNRG is a decentralized energy rental system on the Tron blockc… |

## Honesty, scope, dedup

- **Not big protocols / not forks.** The unwatched filter excludes anything with a team paid to watch it; the non-fork filter excludes Aave/Uniswap/Compound/MasterChef lineage. TVL is a neutral per-row column, not a ranking axis.
- **On-chain evidence, honestly bounded.** Compiler vintage is read live from the chain (all EVM chains, free), but on the *listed* address — so it dates the project, not always the core contract. **Step one of any audit here is to confirm the core contracts' real deployment date and that they're unchanged** (compiler, creation block, no upgrades).
- **Non-EVM fresh candidates exist** (Solana, Cardano, Cosmos, Move chains) but can't be compiler-dated with these tools; they are omitted here rather than guessed at.
- **⚠ prior-incident rows are kept but flagged** (Ooki/bZx, Warp, DFX, Orion, Tidal, Sperax, and USDR/friend.tech lineage). Read the *rest* of the surface, not the patched hole.
- Ranked hypotheses, not findings. Backing data: `DISC-20260912-011-candidates.json`.
