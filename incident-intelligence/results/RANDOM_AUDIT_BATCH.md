# Random audit batch — 160 protocols, deliberately un-patterned

> **What this is.** A large, **semi-random** sample of live protocols to point audit compute at.
> Unlike the other files in `results/`, this one does **not** rank by a mechanism or a "characteristic" —
> the SlowMist window shows a large share of losses are effectively random, they hit *watched* protocols
> too, and heavy upgrade churn is itself a risk. So the selection here is random on purpose; the value is
> breadth of coverage, not a thesis per row.

**Filters applied (only these):**
- **Alive** — not deprecated / rugged / dead-listed.
- **Something to lose, but not a whale** — `$50k ≤ TVL ≤ $50M` at head, so the *extremely-watched* giants
  (which already retain auditors) are excluded, but real money is still on the line.
- **Not a direct fork of a major protocol** — anything whose `forkedFrom` is Uniswap / Aave / Compound /
  Balancer / Curve / Liquity / GMX / Yearn / Solidly / Algebra / Olympus / Lido / Synthetix / Maker / etc.
  is dropped. What remains is **bespoke / original code** (or forks of only minor templates, tagged below).
- **No repetition** — every row cleared `results/discoveries/_exclusion_set.json` (847 names across all prior
  pushes). None has been handed over before, and all are folded back into the set after this run.
- **Not CEX** — centralized venues aren't contract-auditable, so that category is excluded.

**Reproducible.** Sampled with `random.seed(20260829)` from the 1,039-protocol eligible pool
(`tools/`… → `/tmp/randombatch.py`). TVL read at head from DefiLlama `/protocols`, 2026-08-29.

**Notes column legend:** `unaudited` = no audit listed on DefiLlama (not proof of none, but a flag);
`churn:N` = N timestamped hallmarks (migrations/updates/incidents — a churn signal); `fork:X` = fork of a
*minor* template X (not a major); `orc:…` = declared oracle(s).

**Suggested first pass per row** (cheap, and it targets the churn risk the corpus keeps showing): pull the
deployment, check whether it's an **upgradeable proxy and how often the implementation has changed** — the
most-upgraded contracts are where storage-collision, re-init, and forgotten-authority bugs concentrate.

**One honest observation (you invited it).** The *eligible* non-major-fork pool — and therefore this
sample — skews to original DEX / perps / yield / LST engines on **newer chains** (Ethereum 39, Solana 11, Sui 7, Base 6, Arbitrum 6, Avalanche 4, Hyperliquid L1 4, Aptos 4). That is not a
per-row thesis; it just reflects where bespoke code and rapid iteration currently live. Treat it as a hint,
not a filter.

Composition of this sample — categories: Dexs 34, Liquid Staking 17, Lending 14, Yield 13, RWA 9, CDP 9, Derivatives 7, Bridge 6, Canonical Bridge 6, Onchain Capital Allocator 5. Unaudited-flagged: 85. Churn-flagged: 13.

| # | Protocol | Chain(s) | Category | TVL@head | Notes |
|--:|---|---|---|--:|---|
| 1 | **Arrakis V2** (`arrakis-v2`) | Ethereum,Polygon | Liquidity Manager | $0.16M | unaudited |
| 2 | **PacaSwap Bridge** (`pacaswap-bridge`) | Constellation | Bridge | $0.28M | unaudited |
| 3 | **MEV Capital** (`mev-capital`) | Ethereum,Hyperliquid L1 | Risk Curators | $11.86M | unaudited; orc:RedStone,Chronicle |
| 4 | **GoldFinger** (`goldfinger`) | Binance | RWA | $23.80M |  |
| 5 | **Youves** (`youves`) | Tezos | Synthetics | $16.33M | orc:Acurast |
| 6 | **xExchange** (`xexchange`) | Elrond | Dexs | $3.79M | unaudited |
| 7 | **Swell Liquid Restaking** (`swell-liquid-restaking`) | Ethereum | Liquid Restaking | $29.83M |  |
| 8 | **xALGO Liquid Staking** (`xalgo-liquid-staking`) | Algorand | Liquid Staking | $24.49M | orc:Internal |
| 9 | **Feather** (`feather`) | Sei,Celo | Risk Curators | $13.52M | unaudited |
| 10 | **Fomo3D** (`fomo3d`) | Ethereum | Farm | $2.93M | unaudited |
| 11 | **Swaap Maker V1** (`swaap-maker-v1`) | Polygon | Dexs | $0.11M |  |
| 12 | **Lista RWA** (`lista-rwa`) | Binance,Ethereum | RWA | $4.07M | unaudited |
| 13 | **Pyron** (`pyron`) | Fogo | Lending | $0.73M |  |
| 14 | **Streamflow** (`streamflow`) | Solana,Aptos | Payments | $7.88M |  |
| 15 | **3F** (`3f`) | Ethereum | RWA Lending | $29.20M | unaudited |
| 16 | **Overnight Finance** (`overnight-finance`) | Blast,Base | CDP | $10.02M |  |
| 17 | **SettleTON** (`settleton`) | TON | Yield | $0.08M | unaudited |
| 18 | **Big Data Protocol** (`big-data-protocol`) | Ethereum | Yield | $0.07M | unaudited |
| 19 | **TanX.fi** (`tanx-fi`) | Ethereum,Arbitrum | Dexs | $0.29M | unaudited |
| 20 | **GLIF** (`glif`) | Filecoin,Base | Liquid Staking | $19.78M | unaudited |
| 21 | **SeaFi** (`seafi`) | Avalanche | Yield | $0.21M |  |
| 22 | **Meridian AMM** (`meridian-amm`) | Movement | Dexs | $0.28M | unaudited |
| 23 | **Aera V2** (`aera-v2`) | Ethereum,Base | Onchain Capital Allocator | $42.74M | orc:Chainlink |
| 24 | **Oxygen** (`oxygen`) | Solana | Lending | $0.06M | unaudited |
| 25 | **Circuit** (`circuit`) | Chia | CDP | $0.20M |  |
| 26 | **mStable CDP** (`mstable-cdp`) | Ethereum,Polygon | CDP | $3.01M |  |
| 27 | **Mento V3** (`mento-v3`) | Monad,Celo | Dexs | $4.30M | orc:Chainlink |
| 28 | **RealtyX** (`realtyx`) | Base,Plume Mainnet | RWA | $1.03M |  |
| 29 | **Evedex** (`evedex`) | Arbitrum,Eventum | Derivatives | $3.36M | unaudited |
| 30 | **Awaken Swap** (`awaken-swap`) | aelf | Dexs | $4.62M | unaudited |
| 31 | **LUSD ChickenBonds** (`lusd-chickenbonds`) | Ethereum | Yield Aggregator | $1.48M |  |
| 32 | **GrowiHF** (`growihf`) | Hyperliquid L1,Hibachi | Yield | $10.22M | unaudited |
| 33 | **CaviarNine Shape Liquidity** (`caviarnine-shape-liquidity`) | Radix | Dexs | $0.07M | unaudited |
| 34 | **PepeTeam sWAVES** (`pepeteam-swaves`) | Waves | Liquid Staking | $0.23M | unaudited |
| 35 | **Increment Swap** (`increment-swap`) | Flow | Dexs | $1.35M |  |
| 36 | **Lantern Staked SOL** (`lantern-staked-sol`) | Solana | Liquid Staking | $2.18M | unaudited |
| 37 | **Kokoa Finance** (`kokoa-finance`) | Klaytn | CDP | $0.11M | orc:TWAP |
| 38 | **Shido Dex V3** (`shido-dex-v3`) | Shido | Dexs | $0.51M |  |
| 39 | **Neptune Finance** (`neptune-finance`) | Injective | Lending | $2.42M | unaudited; orc:Pyth |
| 40 | **Karura Liquid Staking** (`karura-liquid-staking`) | Karura | Liquid Staking | $0.47M | unaudited |
| 41 | **Adrena Protocol** (`adrena-protocol`) | Solana | Derivatives | $0.51M | orc:Chaos,Pyth |
| 42 | **RAGE Protocol** (`rage-protocol`) | Base | Onchain Capital Allocator | $0.39M |  |
| 43 | **Cauldron** (`cauldron`) | Bitcoincash | Dexs | $0.77M | unaudited; churn:2 |
| 44 | **Sonic ICP** (`sonic-icp`) | ICP | Dexs | $3.03M | unaudited |
| 45 | **DorkFi** (`dorkfi`) | Algorand,Voi Network | Lending | $0.21M |  |
| 46 | **Inertia Bridge** (`inertia-bridge`) | Initia | Canonical Bridge | $0.20M | unaudited |
| 47 | **Virtue** (`virtue`) | IOTA | CDP | $0.41M | orc:Pyth |
| 48 | **Pondo Protocol** (`pondo-protocol`) | Aleo | Liquid Staking | $0.44M | unaudited |
| 49 | **Uranium.io** (`uranium-io`) | Etherlink | RWA | $7.58M | unaudited |
| 50 | **Rip.xyz** (`rip-xyz`) | Hyperliquid L1 | NFT Automated Strategies | $0.10M | unaudited |
| 51 | **Defa By InvoiceMate** (`defa-by-invoicemate`) | Stellar,ZIGChain | RWA | $7.19M | unaudited |
| 52 | **Team Finance** (`team-finance`) | Ethereum,Binance | Token Locker | $45.71M |  |
| 53 | **Carbon Defi** (`carbon-defi`) | Ethereum,Sei | Dexs | $1.51M |  |
| 54 | **Manta Pacific** (`manta-pacific`) | Ethereum | Canonical Bridge | $25.82M | unaudited |
| 55 | **Koi Finance AMM** (`koi-finance-amm`) | zkSync Era | Dexs | $1.27M | unaudited |
| 56 | **NFT20** (`nft20`) | Ethereum,Polygon | NFT Marketplace | $0.07M | unaudited |
| 57 | **Amnis Finance** (`amnis-finance`) | Aptos | Liquid Staking | $3.43M |  |
| 58 | **MoneyOnChain** (`moneyonchain`) | RSK | Dual-Token Stablecoin | $21.68M |  |
| 59 | **Rocket Vault** (`rocket-vault`) | Arbitrum | Onchain Capital Allocator | $0.17M | unaudited |
| 60 | **1sec** (`1sec`) | ICP,Ethereum | Bridge | $2.00M | unaudited |
| 61 | **HypeZion Finance** (`hypezion-finance`) | Hyperliquid L1 | CDP | $0.07M | unaudited |
| 62 | **RIF ON CHAIN** (`rif-on-chain`) | RSK | Dual-Token Stablecoin | $21.70M |  |
| 63 | **Starke Staked SOL** (`starke-staked-sol`) | Solana | Liquid Staking | $1.15M | unaudited |
| 64 | **Chain Fusion** (`chain-fusion`) | Bitcoin,Ethereum | Decentralized BTC | $24.90M |  |
| 65 | **Lisk Bridge** (`lisk-bridge`) | Ethereum | Canonical Bridge | $34.08M | unaudited |
| 66 | **Sceptre Liquid** (`sceptre-liquid`) | Flare | Liquid Staking | $14.83M |  |
| 67 | **SomniaLend** (`somnialend`) | Somnia | Lending | $0.65M | unaudited |
| 68 | **Bedrock uniIOTX** (`bedrock-uniiotx`) | IoTeX | Liquid Staking | $1.21M |  |
| 69 | **Phoenix Spot** (`phoenix-spot`) | Solana | Dexs | $1.06M | unaudited |
| 70 | **Consensus Liquidity DEX** (`consensus-liquidity-dex`) | Klaytn | Dexs | $0.64M | unaudited |
| 71 | **Flamingo Finance** (`flamingo-finance`) | NEO | Dexs | $0.59M | churn:7 |
| 72 | **Sudoswap V2** (`sudoswap-v2`) | Ethereum,Base | NFT Marketplace | $0.68M |  |
| 73 | **Eclipse Bridge** (`eclipse-bridge`) | Ethereum | Canonical Bridge | $7.22M | unaudited |
| 74 | **Noon** (`noon`) | Ethereum,zkSync Era | Yield | $38.35M | churn:1 |
| 75 | **ThalaSwap V2** (`thalaswap-v2`) | Aptos | Dexs | $0.59M | unaudited |
| 76 | **Decibel** (`decibel`) | Aptos | Derivatives | $29.75M | unaudited |
| 77 | **Dual Finance** (`dual-finance`) | Solana | Options | $0.23M | unaudited; orc:Pyth |
| 78 | **BabelFish** (`babelfish`) | RSK | Bridge | $1.06M | unaudited |
| 79 | **Kyan Blue Perps** (`kyan-blue-perps`) | Arbitrum | Derivatives | $0.08M | unaudited |
| 80 | **vfat.io** (`vfat-io`) | Base,Ethereum | Yield Aggregator | $27.87M |  |
| 81 | **Chainflip AMM** (`chainflip-amm`) | Chainflip,Ethereum | Dexs | $9.53M |  |
| 82 | **xSui** (`xsui`) | Sui | Liquid Staking | $0.18M | unaudited; fork:SpringSui |
| 83 | **BendDAO Lending V1** (`benddao-lending-v1`) | Ethereum | NFT Lending | $0.65M | orc:NFTOracle,ReserveOracle |
| 84 | **StratEx** (`stratex`) | Base,Flare | Yield Aggregator | $0.21M | unaudited; orc:Chainlink |
| 85 | **Ensuro** (`ensuro`) | Ethereum,Polygon | Insurance | $2.04M | churn:2 |
| 86 | **1inch Swap** (`1inch-swap`) | Ethereum,Binance | DEX Aggregator | $3.17M |  |
| 87 | **Origami Finance** (`origami-finance`) | Ethereum,Berachain | Leveraged Farming | $49.39M |  |
| 88 | **Bounce.Tech** (`bounce-tech`) | Hyperliquid L1 | Derivatives | $1.04M |  |
| 89 | **Dano Finance** (`dano-finance`) | Cardano | Dexs | $3.40M |  |
| 90 | **Zeus Network** (`zeus-network`) | Bitcoin | Decentralized BTC | $3.80M | unaudited |
| 91 | **Hashport** (`hashport`) | Ethereum,Hedera | Bridge | $1.15M |  |
| 92 | **Salvor** (`salvor`) | Avalanche | NFT Marketplace | $0.31M |  |
| 93 | **UntitledBank** (`untitledbank`) | Soneium | Lending | $0.14M | orc:Pyth |
| 94 | **Vendor V2** (`vendor-v2`) | Base,Arbitrum | Lending | $0.69M | orc:Chainlink |
| 95 | **Unilend Protocol** (`unilend-protocol`) | UNIT0 | Lending | $0.06M | unaudited; orc:DIA |
| 96 | **Y10K Capital** (`y10k-capital`) | Ethereum,Sei | Risk Curators | $31.61M | unaudited |
| 97 | **Lunarbase** (`lunarbase`) | Base,Binance | Dexs | $0.16M | unaudited |
| 98 | **ThetaCash** (`thetacash`) | Theta | Synthetics | $0.11M | unaudited |
| 99 | **Propbase** (`propbase`) | Aptos | RWA | $1.35M |  |
| 100 | **SMARDEX USDN** (`smardex-usdn`) | Ethereum | Basis Trading | $1.52M | unaudited |
| 101 | **Turbos** (`turbos`) | Sui | Dexs | $3.39M | unaudited |
| 102 | **SOLID** (`solid`) | Terra2 | CDP | $0.09M |  |
| 103 | **Alto** (`alto`) | Ethereum | CDP | $0.28M | orc:Chainlink |
| 104 | **Suigar** (`suigar`) | Sui | Luck Games | $0.12M |  |
| 105 | **Acre** (`acre`) | Ethereum | Yield | $0.56M | unaudited |
| 106 | **Hakka Finance** (`hakka-finance`) | Ethereum,Binance | Derivatives | $5.41M | unaudited; orc:Chainlink |
| 107 | **Dexalot Portfolio** (`dexalot-portfolio`) | Avalanche,Arbitrum | Bridge | $5.51M |  |
| 108 | **VNX** (`vnx`) | Solana,Base | RWA | $5.14M |  |
| 109 | **Nucleon** (`nucleon`) | Conflux | Liquid Staking | $0.61M |  |
| 110 | **StakePoint** (`stakepoint`) | Solana | Farm | $4.64M | unaudited |
| 111 | **HbarSuite** (`hbarsuite`) | Hedera | Dexs | $3.52M |  |
| 112 | **SundaeSwap V2** (`sundaeswap-v2`) | Cardano | Dexs | $0.50M |  |
| 113 | **AstridDAO** (`astriddao`) | Astar | CDP | $0.16M | orc:DIA |
| 114 | **Spectra V2** (`spectra-v2`) | Flare,Hemi | Yield | $30.78M | unaudited; churn:1 |
| 115 | **Chainflip Lending** (`chainflip-lending`) | Chainflip | Lending | $4.77M | orc:Chainlink |
| 116 | **Beradrome** (`beradrome`) | Berachain | Yield | $0.46M |  |
| 117 | **Splash Protocol** (`splash-protocol`) | Cardano | Dexs | $3.19M | unaudited |
| 118 | **Plasma One** (`plasma-one`) | Plasma | Crypto Card Issuer | $10.52M | unaudited |
| 119 | **Tinlake** (`tinlake`) | Ethereum | RWA Lending | $0.06M |  |
| 120 | **SUN.io** (`sun-io`) | Tron | Dexs | $0.78M |  |
| 121 | **Momentum** (`momentum`) | Sui | Dexs | $4.01M |  |
| 122 | **Tardly** (`tardly`) | Algorand | Yield Lottery | $0.06M | unaudited |
| 123 | **Crypto.com Liquid Staking** (`crypto-com-liquid-staking`) | Cronos,Solana | Liquid Staking | $30.23M | unaudited |
| 124 | **Helix Spot** (`helix-spot`) | Injective | Dexs | $0.67M | unaudited |
| 125 | **Butter Network** (`butter-network`) | Tron,Ethereum | Cross Chain Bridge | $1.50M | unaudited |
| 126 | **Ethena tsUSDe** (`ethena-tsusde`) | TON | Yield | $3.22M | unaudited |
| 127 | **Harbor** (`harbor`) | Ethereum,MegaETH | Yield | $0.12M | churn:2; fork:fx Protocol; orc:Harbor,Chainlink |
| 128 | **Ring Few** (`ring-few`) | Ethereum,Hyperliquid L1 | Bridge | $44.39M |  |
| 129 | **Bumpin Trade** (`bumpin-trade`) | Solana | Derivatives | $4.37M | unaudited |
| 130 | **Polynomial Liquidity** (`polynomial-liquidity`) | Polynomial | Dexs | $0.49M | unaudited; churn:1 |
| 131 | **HiYield** (`hiyield`) | Avalanche,Canto | RWA | $2.74M | unaudited |
| 132 | **Pumex** (`pumex`) | Injective | DEX Aggregator | $1.82M | unaudited |
| 133 | **InceptionLRT (Isolated Restaking)** (`inceptionlrt-isolated-restaking`) | Ethereum | Liquid Restaking | $6.80M | unaudited; churn:2 |
| 134 | **StableHodl** (`stablehodl`) | Polygon,Ethereum | Yield | $6.36M | unaudited |
| 135 | **Kizzy** (`kizzy`) | Monad | Prediction Market | $0.07M | unaudited |
| 136 | **Agua** (`agua`) | Ethereum,Monad | Onchain Capital Allocator | $8.11M |  |
| 137 | **Hibachi Bridge** (`hibachi-bridge`) | Arbitrum | Canonical Bridge | $5.23M | unaudited |
| 138 | **Rezerve Lending** (`rezerve-lending`) | Ethereum | Lending | $1.42M | unaudited; orc:DIA |
| 139 | **Excellar** (`excellar`) | Stellar | Basis Trading | $0.18M | unaudited |
| 140 | **DipCoin Vault** (`dipcoin-vault`) | Sui | Yield | $1.59M | churn:1 |
| 141 | **Verio** (`verio`) | Story | Liquid Staking | $2.85M | unaudited |
| 142 | **FluidTokens** (`fluidtokens`) | Cardano | Lending | $2.69M | unaudited; churn:2 |
| 143 | **Ambient** (`ambient`) | Scroll,Blast | Dexs | $2.26M | unaudited |
| 144 | **DefiChain DEX** (`defichain-dex`) | DefiChain | Dexs | $1.03M |  |
| 145 | **Accumulated Finance Lending** (`accumulated-finance-lending`) | Bitkub,Coti | Lending | $0.16M |  |
| 146 | **0x0.ai** (`0x0-ai`) | Ethereum | Privacy | $0.26M |  |
| 147 | **Hegic** (`hegic`) | Arbitrum,Ethereum | Options | $10.25M |  |
| 148 | **Scroll Bridge** (`scroll-bridge`) | Ethereum | Canonical Bridge | $39.13M | unaudited |
| 149 | **Bancor V2.1** (`bancor-v2-1`) | Ethereum | Dexs | $9.78M | churn:2 |
| 150 | **FILLiquid** (`filliquid`) | Binance,Filecoin | Liquid Staking | $0.17M | unaudited |
| 151 | **Port Finance** (`port-finance`) | Solana | Lending | $0.22M | orc:Pyth |
| 152 | **Toros** (`toros`) | Arbitrum,Optimism | Yield | $7.63M | churn:10; orc:Chainlink |
| 153 | **Bracket Vaults** (`bracket-vaults`) | Ethereum | Onchain Capital Allocator | $0.50M |  |
| 154 | **Curve LlamaLend V2** (`curve-llamalend-v2`) | Optimism | Lending | $1.97M | unaudited; churn:1 |
| 155 | **SpringSui Ecosystem** (`springsui-ecosystem`) | Sui | Liquid Staking | $0.52M |  |
| 156 | **Aftermath afSUI** (`aftermath-afsui`) | Sui | Liquid Staking | $2.35M | unaudited |
| 157 | **CACHE.Gold** (`cache-gold`) | Ethereum | RWA | $0.57M |  |
| 158 | **Elix.fi** (`elix-fi`) | Somnia | Dexs | $0.06M | unaudited |
| 159 | **ICPSwap** (`icpswap`) | ICP | Dexs | $3.64M | unaudited |
| 160 | **Reactor DEX** (`reactor-dex`) | Fuel | Dexs | $0.99M |  |

---

**160 protocols**, random seed `20260829`, filters as above. This is a coverage list, not a ranking:
audit in any order. False leads are expected — the point is that a large random sweep of un-forked, mid-size,
less-watched code is where the corpus says the next surprise most often is.
