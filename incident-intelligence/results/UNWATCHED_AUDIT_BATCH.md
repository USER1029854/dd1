# Unwatched audit batch — 324 protocols nobody is watching (but that still hold money)

> **Corrected concept of "unwatched."** This is *not* about audits. Unwatched means **no one is actively
> watching or defending the protocol** — the team earns little/no revenue to pay for ongoing security, or
> it's deprecated / abandoned, or its site is dead, or its TVL is quietly bleeding out — yet real money is
> still sitting in the contracts. That is the classic soft target: no mempool watcher, no incident
> response, no one re-auditing after each upgrade. Audited-or-not is irrelevant here and is not used.

**How "unwatched" is measured (any one qualifies):**
- **deprecated** on DefiLlama but still holding TVL (21) — officially wound down, funds still parked;
- **dead website** (136) — the project's own site is gone/broken (DefiLlama flag);
- **~no revenue** (165) — real TVL but tracked 30-day protocol revenue under ~$3k/mo, i.e. no budget to
  fund monitoring or a re-audit;
- **TVL decay** (20) — down >20% in 7 days, users and attention leaving.

**Kept from before (structural, not "characteristic"):** real money at stake (`$50k ≤ TVL ≤ $100M`, so the
watched blue-chips are still excluded); **not a direct fork of a major protocol**; not CEX / not an L1
chain; not rugged; and **not previously delivered** — all cleared the 1,187-name exclusion set and are
folded into it. Order is random (`seed 20260901`); this is the *complete* qualifying set, not a sample.

**Cheap first pass per row:** unwatched + upgradeable is the worst combination — pull the deployment and
check whether it's a proxy and how stale/loose its admin and last upgrade are; forgotten mint authority
and live approvals on abandoned contracts are the recurring way this money leaves.

Composition — categories: Dexs 82, Liquid Staking 38, Yield 31, Lending 27, Derivatives 22, Yield Aggregator 18, CDP 13, RWA 10, Risk Curators 7, SoFi 6. Chains: Ethereum 52, Solana 48, Binance 23, Sui 16, Base 14, Avalanche 12, Polygon 11, Arbitrum 10. TVL/revenue at head (DefiLlama, 2026-08-29).

| # | Protocol | Chain(s) | Category | TVL | Why it's unwatched |
|--:|---|---|---|--:|---|
| 1 | **Affluent** (`affluent`) | TON | Lending | $2.46M | rev≈$0.5k/mo; no-mcap |
| 2 | **Lets Get HAI** (`lets-get-hai`) | Optimism | CDP | $1.03M | rev≈$1.3k/mo |
| 3 | **UltraYield Curator** (`ultrayield-curator`) | Ethereum,Hyperliquid L1 | Risk Curators | $54.51M | rev≈$0.0k/mo; no-mcap |
| 4 | **InitiaDEX** (`initiadex`) | Initia | Dexs | $2.04M | rev≈$0.0k/mo; no-mcap |
| 5 | **Arcade.xyz** (`arcade-xyz`) | Ethereum | NFT Lending | $0.21M | dead-site; no-revenue-tracked; no-mcap |
| 6 | **ClayStack ETH** (`claystack-eth`) | Ethereum | Liquid Restaking | $2.50M | dead-site; no-revenue-tracked; no-mcap |
| 7 | **MineFi** (`minefi`) | Filecoin | Liquid Staking | $0.96M | dead-site; no-revenue-tracked; no-mcap |
| 8 | **Defrost** (`defrost`) | Avalanche | CDP | $0.08M | dead-site; no-revenue-tracked; no-mcap |
| 9 | **FlareBank** (`flarebank`) | Flare | Reserve Currency | $0.20M | dead-site; rev≈$0.2k/mo; fork:Eggs Finance; no-mcap |
| 10 | **deFusion** (`defusion`) | TomoChain | Liquid Staking | $0.12M | no-revenue-tracked; TVL -35%/7d |
| 11 | **Swamp Finance** (`swamp-finance`) | Binance | Yield | $1.27M | dead-site; no-revenue-tracked; no-mcap |
| 12 | **AutoRange** (`autorange`) | Arbitrum,Celo | Dexs | $0.13M | rev≈$0.5k/mo; no-mcap |
| 13 | **Polynomial Trade** (`polynomial-trade`) | Optimism,Polynomial | Derivatives | $4.75M | **deprecated**; no-revenue-tracked; no-mcap |
| 14 | **Torch Dexs** (`torch-dexs`) | TON | Dexs | $0.48M | rev≈$0.0k/mo; no-mcap |
| 15 | **Mellow Restaking** (`mellow-restaking`) | Ethereum,Lisk | Liquid Restaking | $25.24M | rev≈$0.2k/mo; no-mcap |
| 16 | **Tapp Exchange** (`tapp-exchange`) | Aptos | Dexs | $0.19M | dead-site; rev≈$0.1k/mo; no-mcap |
| 17 | **Sherwood** (`sherwood`) | Robinhood Chain | Privacy | $0.07M | rev≈$0.3k/mo; no-mcap |
| 18 | **JediSwap V1** (`jediswap-v1`) | Starknet | Dexs | $0.87M | dead-site; no-revenue-tracked; no-mcap |
| 19 | **LiquidBots** (`liquidbots`) | Hyperliquid L1 | Interface | $0.10M | rev≈$3.0k/mo; TVL -36%/7d; no-mcap |
| 20 | **Crunchy** (`crunchy`) | Tezos | Yield Aggregator | $0.06M | dead-site; no-revenue-tracked; no-mcap |
| 21 | **FluxBeam** (`fluxbeam`) | Solana | Dexs | $3.21M | rev≈$0.4k/mo; no-mcap |
| 22 | **Aborean AMM** (`aborean-amm`) | Abstract | Dexs | $0.94M | rev≈$2.3k/mo; no-mcap |
| 23 | **SteakBank Finance** (`steakbank-finance`) | Binance | Liquid Staking | $0.29M | dead-site; no-revenue-tracked; no-mcap |
| 24 | **Econia** (`econia`) | Aptos | Dexs | $0.18M | dead-site; no-revenue-tracked; no-mcap |
| 25 | **Yuzu Money** (`yuzu-money`) | Plasma,Ethereum | Yield | $82.22M | rev≈$0.0k/mo; no-mcap |
| 26 | **Metastable** (`metastable`) | Sui | CDP | $0.38M | no-revenue-tracked; TVL -63%/7d; no-mcap |
| 27 | **Yuzu Finance** (`yuzu-finance`) | Movement | Dexs | $0.41M | rev≈$0.6k/mo; no-mcap |
| 28 | **Tradoor TON** (`tradoor-ton`) | TON | Derivatives | $0.14M | no-revenue-tracked; TVL -25%/7d |
| 29 | **Lenfi** (`lenfi`) | Cardano | Lending | $0.14M | dead-site; no-revenue-tracked; no-mcap |
| 30 | **Canonic** (`canonic`) | MegaETH | Dexs | $0.06M | rev≈$0.7k/mo; no-mcap |
| 31 | **Poly Network** (`poly-network`) | Ethereum,Binance | Bridge | $44.73M | dead-site; no-revenue-tracked; no-mcap |
| 32 | **swap.coffee** (`swap-coffee`) | TON | DEX Aggregator | $0.12M | rev≈$0.0k/mo; no-mcap |
| 33 | **PolygonFarm Finance** (`polygonfarm-finance`) | Polygon | Yield | $0.05M | dead-site; no-revenue-tracked; no-mcap |
| 34 | **Argo Finance** (`argo-finance`) | Cronos | Liquid Staking | $0.23M | dead-site; no-revenue-tracked; no-mcap |
| 35 | **ThunderCore Staking** (`thundercore-staking`) | ThunderCore | Staking Pool | $0.09M | no-revenue-tracked; TVL -45%/7d |
| 36 | **Summer.fi Pro** (`summer-fi-pro`) | Ethereum,Arbitrum | CDP Manager | $16.80M | **deprecated**; rev≈$0.0k/mo; no-mcap |
| 37 | **Pico Staked SOL** (`pico-staked-sol`) | Solana | Liquid Staking | $2.07M | rev≈$0.2k/mo; no-mcap |
| 38 | **DeepLock** (`deeplock`) | Binance | Launchpad | $2.22M | dead-site; no-revenue-tracked; no-mcap |
| 39 | **Chest Finance** (`chest-finance`) | Solana | Options Vault | $0.80M | dead-site; no-revenue-tracked; no-mcap |
| 40 | **Algofi Swap** (`algofi-swap`) | Algorand | Dexs | $0.06M | dead-site; no-revenue-tracked; no-mcap |
| 41 | **O2 Exchange** (`o2-exchange`) | Fuel | Dexs | $2.37M | rev≈$0.9k/mo; no-mcap |
| 42 | **Hubra Staked SOL** (`hubra-staked-sol`) | Solana | Liquid Staking | $16.81M | rev≈$0.1k/mo; no-mcap |
| 43 | **Drake Exchange** (`drake-exchange`) | Monad | Derivatives | $0.08M | rev≈$0.0k/mo; no-mcap |
| 44 | **Parrot Protocol** (`parrot-protocol`) | Solana | CDP | $0.06M | dead-site; no-revenue-tracked; no-mcap |
| 45 | **Delpho** (`delpho`) | Hyperliquid L1 | CDP | $0.50M | no-revenue-tracked; TVL -31%/7d; no-mcap |
| 46 | **Kuru CLOB** (`kuru-clob`) | Monad | Dexs | $1.49M | rev≈$0.0k/mo; no-mcap |
| 47 | **Polkadex** (`polkadex`) | Polkadex | Dexs | $0.07M | dead-site; no-revenue-tracked; no-mcap |
| 48 | **PandaSwap** (`pandaswap`) | Binance | Dexs | $0.10M | dead-site; no-revenue-tracked; no-mcap |
| 49 | **Aftermath AMM** (`aftermath-amm`) | Sui | Dexs | $2.25M | rev≈$0.0k/mo; no-mcap |
| 50 | **Hats.V2** (`hats-v2`) | Arbitrum,Ethereum | Bug Bounty | $0.16M | **deprecated**; no-revenue-tracked; no-mcap |
| 51 | **Reaper Farm** (`reaper-farm`) | Optimism,Fantom | Yield Aggregator | $1.47M | dead-site; no-revenue-tracked; no-mcap |
| 52 | **Beta Finance V1** (`beta-finance-v1`) | Ethereum,Avalanche | Lending | $0.47M | dead-site; no-revenue-tracked; no-mcap |
| 53 | **Flamingo Lend** (`flamingo-lend`) | NEO | Lending | $0.19M | no-revenue-tracked; TVL -26%/7d; no-mcap |
| 54 | **PulseX StableSwap** (`pulsex-stableswap`) | Pulse | Dexs | $0.96M | rev≈$2.9k/mo; no-mcap |
| 55 | **Bril Finance** (`bril-finance`) | Binance | Yield Aggregator | $0.10M | dead-site; no-revenue-tracked; no-mcap |
| 56 | **LlamaPay** (`llamapay`) | Binance,Ethereum | Payments | $2.08M | no-revenue-tracked; TVL -27%/7d; no-mcap |
| 57 | **Swych Perpetual** (`swych-perpetual`) | Binance | Derivatives | $0.18M | dead-site; no-revenue-tracked; no-mcap |
| 58 | **GumBall Protocol** (`gumball-protocol`) | Arbitrum | NFT Marketplace | $0.37M | dead-site; no-revenue-tracked; no-mcap |
| 59 | **Euclid Finance** (`euclid-finance`) | Ethereum | Liquid Restaking | $0.29M | dead-site; no-revenue-tracked; no-mcap |
| 60 | **RockSolid Network** (`rocksolid-network`) | Ethereum | Yield | $25.49M | rev≈$0.6k/mo; no-mcap |
| 61 | **Ventuals** (`ventuals`) | Hyperliquid L1 | Interface | $0.83M | rev≈$0.0k/mo; no-mcap |
| 62 | **YieldFi** (`yieldfi`) | Ethereum,Base | Yield Aggregator | $11.37M | rev≈$0.0k/mo; no-mcap |
| 63 | **DefiTuna AMM** (`defituna-amm`) | Solana | Dexs | $0.19M | rev≈$1.4k/mo; no-mcap |
| 64 | **SpringSui** (`springsui`) | Sui | Liquid Staking | $53.81M | rev≈$1.9k/mo; no-mcap |
| 65 | **Blue Planet** (`blue-planet`) | Binance | Dexs | $0.15M | rev≈$0.0k/mo; no-mcap |
| 66 | **Algofi Lend** (`algofi-lend`) | Algorand | Lending | $0.65M | dead-site; no-revenue-tracked; no-mcap |
| 67 | **CUBISwap** (`cubiswap`) | Op_Bnb | Dexs | $0.05M | dead-site; no-revenue-tracked; no-mcap |
| 68 | **Gravity by Galxe** (`gravity-by-galxe`) | Ethereum | Canonical Bridge | $23.11M | rev≈$0.1k/mo |
| 69 | **Kinetiq Launch** (`kinetiq-launch`) | Hyperliquid L1 | Liquid Staking | $4.05M | rev≈$0.5k/mo; no-mcap |
| 70 | **Parcl V3** (`parcl-v3`) | Solana | Derivatives | $1.10M | rev≈$0.0k/mo; no-mcap |
| 71 | **Ryze Protocol** (`ryze-protocol`) | Base | Dexs | $0.52M | rev≈$1.2k/mo; no-mcap |
| 72 | **Echo Strategy** (`echo-strategy`) | Aptos | Yield Aggregator | $0.07M | rev≈$0.0k/mo; no-mcap |
| 73 | **Restake Finance** (`restake-finance`) | Ethereum | Liquid Restaking | $0.06M | dead-site; no-revenue-tracked |
| 74 | **Nado Spot** (`nado-spot`) | Ink | Dexs | $51.45M | rev≈$2.6k/mo; no-mcap |
| 75 | **Scopuly** (`scopuly`) | Stellar | Dexs | $1.05M | dead-site; rev≈$0.0k/mo; no-mcap |
| 76 | **Sudo Perps** (`sudo-perps`) | Sui | Derivatives | $3.10M | rev≈$1.9k/mo; no-mcap |
| 77 | **Bitbond Lockers** (`bitbond-lockers`) | Base,Binance | Token Locker | $5.50M | no-revenue-tracked; TVL -35%/7d; no-mcap |
| 78 | **Plasma Saving Vaults** (`plasma-saving-vaults`) | Plasma | Onchain Capital Allocator | $32.67M | rev≈$0.0k/mo; no-mcap |
| 79 | **BTCST** (`btcst`) | Binance | Yield | $0.95M | dead-site; no-revenue-tracked |
| 80 | **Zircuit Staking** (`zircuit-staking`) | Ethereum,Zircuit | Farm | $58.98M | rev≈$0.0k/mo; no-mcap |
| 81 | **Azuro** (`azuro`) | Polygon,Base | Prediction Market | $1.41M | rev≈$-205.9k/mo |
| 82 | **Unit Protocol** (`unit-protocol`) | Ethereum | CDP | $0.26M | dead-site; no-revenue-tracked; no-mcap |
| 83 | **AlphaFi stSUI** (`alphafi-stsui`) | Sui | Liquid Staking | $6.49M | rev≈$1.7k/mo; no-mcap |
| 84 | **Rift Finance** (`rift-finance`) | Aurora,Ethereum | Yield | $0.08M | dead-site; no-revenue-tracked; no-mcap |
| 85 | **Amulet V2** (`amulet-v2`) | Solana,Optimism | Yield Aggregator | $0.07M | dead-site; no-revenue-tracked; no-mcap |
| 86 | **OkieSwap V3** (`okieswap-v3`) | X Layer | Dexs | $0.11M | rev≈$0.6k/mo; no-mcap |
| 87 | **Siren** (`siren`) | Ethereum,Polygon | Options | $0.35M | dead-site; no-revenue-tracked |
| 88 | **Larix** (`larix`) | Solana | Lending | $1.21M | dead-site; no-revenue-tracked; no-mcap |
| 89 | **Magma** (`magma`) | Sui | Dexs | $2.11M | rev≈$1.8k/mo; no-mcap |
| 90 | **3Jane Lending** (`3jane-lending`) | Ethereum | Uncollateralized Lending | $8.35M | rev≈$0.0k/mo; no-mcap |
| 91 | **Omnipair** (`omnipair`) | Solana | Lending | $0.65M | rev≈$0.4k/mo |
| 92 | **Polywhale Finance** (`polywhale-finance`) | Polygon | Yield | $0.08M | dead-site; no-revenue-tracked; no-mcap |
| 93 | **AggreLend** (`aggrelend`) | Solana | Yield Aggregator | $0.37M | dead-site; no-revenue-tracked; no-mcap |
| 94 | **CHATEAU** (`chateau`) | Plasma | RWA | $1.02M | dead-site; no-revenue-tracked; fork:Ethena USDe; no-mcap |
| 95 | **Supernova AMM** (`supernova-amm`) | Ethereum | Dexs | $0.12M | rev≈$0.2k/mo; no-mcap |
| 96 | **Keeta Bridge** (`keeta-bridge`) | Base | Canonical Bridge | $0.72M | no-revenue-tracked; TVL -94%/7d; no-mcap |
| 97 | **Cog** (`cog`) | Scroll | Lending | $0.19M | dead-site; no-revenue-tracked; no-mcap |
| 98 | **HLiquity** (`hliquity`) | Hedera | CDP | $0.20M | dead-site; no-revenue-tracked; no-mcap |
| 99 | **Nabla Finance** (`nabla-finance`) | Arbitrum,Hyperliquid L1 | Dexs | $0.08M | dead-site; rev≈$0.0k/mo |
| 100 | **REX Staking** (`rex-staking`) | Telos | Lending | $2.83M | no-revenue-tracked; TVL -32%/7d; no-mcap |
| 101 | **Jet V1** (`jet-v1`) | Solana | Lending | $0.15M | dead-site; no-revenue-tracked; no-mcap |
| 102 | **Yusan** (`yusan`) | ICP,Ethereum | Lending | $0.06M | rev≈$0.0k/mo; no-mcap |
| 103 | **ClayStack Matic** (`claystack-matic`) | Ethereum | Liquid Staking | $0.05M | dead-site; no-revenue-tracked; no-mcap |
| 104 | **BEND** (`bend`) | Berachain | Lending | $9.79M | rev≈$0.3k/mo; no-mcap |
| 105 | **Proxy** (`proxy`) | Polygon,Ethereum | Bridge | $20.38M | dead-site; no-revenue-tracked; no-mcap |
| 106 | **Dojoswap LSD** (`dojoswap-lsd`) | Injective | Liquid Staking | $0.09M | dead-site; no-revenue-tracked; no-mcap |
| 107 | **PsyOptions** (`psyoptions`) | Solana | Options | $0.58M | dead-site; no-revenue-tracked; no-mcap |
| 108 | **stabble Stableswap** (`stabble-stableswap`) | Solana | Dexs | $0.13M | rev≈$0.1k/mo; no-mcap |
| 109 | **D2 Finance** (`d2-finance`) | Hyperliquid L1,Arbitrum | Onchain Capital Allocator | $33.38M | rev≈$2.1k/mo; no-mcap |
| 110 | **Meta Pool ETH** (`meta-pool-eth`) | Ethereum | Liquid Staking | $25.86M | rev≈$0.7k/mo; no-mcap |
| 111 | **PolyCub** (`polycub`) | Polygon | Yield | $0.08M | dead-site; no-revenue-tracked; no-mcap |
| 112 | **Sierra Protocol** (`sierra-protocol`) | Avalanche | Yield | $45.09M | rev≈$0.0k/mo; no-mcap |
| 113 | **Unbound** (`unbound`) | Ethereum,Polygon | Derivatives | $0.05M | dead-site; no-revenue-tracked; no-mcap |
| 114 | **Kintsu** (`kintsu`) | Monad,Hyperliquid L1 | Liquid Staking | $2.54M | rev≈$0.1k/mo; no-mcap |
| 115 | **Project 0** (`project-0`) | Solana | Lending | $64.26M | rev≈$2.4k/mo; no-mcap |
| 116 | **Sandglass** (`sandglass`) | Solana,Eclipse | Yield | $0.07M | **deprecated**; no-revenue-tracked; no-mcap |
| 117 | **Fables** (`fables`) | — | Dexs | $1.53M | rev≈$0.0k/mo; no-mcap |
| 118 | **stUSDT** (`stusdt`) | Tron,Ethereum | RWA | $62.86M | rev≈$0.3k/mo |
| 119 | **Delea** (`delea`) | TON | CDP | $0.78M | **deprecated**; no-revenue-tracked; no-mcap |
| 120 | **Hord** (`hord`) | Ethereum | Liquid Staking | $0.36M | **deprecated**; dead-site; no-revenue-tracked |
| 121 | **Fragmetric** (`fragmetric`) | Solana | Liquid Restaking | $5.38M | rev≈$1.1k/mo |
| 122 | **MUFEX** (`mufex`) | Binance,Polygon | Derivatives | $0.28M | dead-site; no-revenue-tracked; no-mcap |
| 123 | **NeoBurger** (`neoburger`) | NEO | Liquid Staking | $0.68M | **deprecated**; no-revenue-tracked; no-mcap |
| 124 | **AlphaPing** (`alphaping`) | Ethereum | Risk Curators | $6.72M | rev≈$1.0k/mo; no-mcap |
| 125 | **Thala CDP** (`thala-cdp`) | Aptos | CDP | $0.48M | rev≈$0.1k/mo; no-mcap |
| 126 | **ViteX** (`vitex`) | Vite | Dexs | $4.94M | dead-site; no-revenue-tracked; no-mcap |
| 127 | **Float** (`float`) | Polygon,Avalanche | Derivatives | $0.14M | dead-site; no-revenue-tracked; no-mcap |
| 128 | **IDEX V1** (`idex-v1`) | Ethereum | Dexs | $39.03M | dead-site; no-revenue-tracked; no-mcap |
| 129 | **Frax** (`frax`) | Ethereum | Algo-Stables | $45.82M | rev≈$0.6k/mo; no-mcap |
| 130 | **Pika** (`pika`) | Optimism | Derivatives | $0.30M | rev≈$0.0k/mo; no-mcap |
| 131 | **AstroSwap AMM** (`astroswap-amm`) | Starknet | Dexs | $0.07M | dead-site; no-revenue-tracked; no-mcap |
| 132 | **IFPool** (`ifpool`) | CSC | Liquid Staking | $0.05M | dead-site; no-revenue-tracked; no-mcap |
| 133 | **Hipo** (`hipo`) | TON | Liquid Staking | $10.90M | rev≈$0.0k/mo; no-mcap |
| 134 | **Folks Finance xChain** (`folks-finance-xchain`) | Avalanche,Polygon | Lending | $5.14M | rev≈$1.1k/mo; no-mcap |
| 135 | **01** (`01`) | Solana | Derivatives | $0.11M | dead-site; no-revenue-tracked; no-mcap |
| 136 | **Goblin** (`goblin`) | Aptos | Yield Aggregator | $2.91M | rev≈$0.0k/mo; no-mcap |
| 137 | **Ruby.Exchange Yield** (`ruby-exchange-yield`) | Europa | Yield | $0.14M | dead-site; no-revenue-tracked; no-mcap |
| 138 | **friend.tech V1** (`friend-tech-v1`) | Base | SoFi | $2.28M | rev≈$0.0k/mo; no-mcap |
| 139 | **Concentrator** (`concentrator`) | Ethereum | Yield | $72.99M | rev≈$2.0k/mo |
| 140 | **Canto Dex** (`canto-dex`) | Canto | Dexs | $0.10M | dead-site; no-revenue-tracked; no-mcap |
| 141 | **Laine SOL** (`laine-sol`) | Solana | Liquid Staking | $1.27M | rev≈$0.0k/mo; no-mcap |
| 142 | **SUNSwap V1** (`sunswap-v1`) | Tron | Dexs | $57.68M | rev≈$0.0k/mo; no-mcap |
| 143 | **Gridex** (`gridex`) | Arbitrum,Linea | Dexs | $0.07M | dead-site; no-revenue-tracked; no-mcap |
| 144 | **Javsphere** (`javsphere`) | Base,DeFiChain EVM | Derivatives | $0.05M | rev≈$0.9k/mo |
| 145 | **ComTech Gold** (`comtech-gold`) | XDC | RWA | $3.42M | no-revenue-tracked; TVL -35%/7d; no-mcap |
| 146 | **Jupiter Offerbook** (`jupiter-offerbook`) | Solana | Lending | $1.19M | rev≈$2.5k/mo; no-mcap |
| 147 | **Tomb Swap** (`tomb-swap`) | Fantom | Dexs | $0.05M | dead-site; no-revenue-tracked; no-mcap |
| 148 | **Capybara Dexs** (`capybara-dexs`) | Klaytn | Dexs | $0.11M | rev≈$0.0k/mo; no-mcap |
| 149 | **KiloEx** (`kiloex`) | Binance,Op_Bnb | Derivatives | $1.33M | rev≈$2.3k/mo |
| 150 | **Jet Margin** (`jet-margin`) | Solana | Lending | $0.24M | dead-site; no-revenue-tracked; no-mcap |
| 151 | **Jupiter Lend DEX** (`jupiter-lend-dex`) | Solana | Dexs | $8.13M | rev≈$0.1k/mo; no-mcap |
| 152 | **ctez** (`ctez`) | Tezos | Dexs | $0.05M | dead-site; no-revenue-tracked; no-mcap |
| 153 | **SFT Protocol** (`sft-protocol`) | Filecoin | Liquid Staking | $0.40M | dead-site; no-revenue-tracked; no-mcap |
| 154 | **Djed Stablecoin** (`djed-stablecoin`) | Cardano | Dual-Token Stablecoin | $5.04M | dead-site; no-revenue-tracked; no-mcap |
| 155 | **NodeDAO** (`nodedao`) | Ethereum | Liquid Staking | $35.24M | rev≈$0.0k/mo; no-mcap |
| 156 | **Frost Finance** (`frost-finance`) | Avalanche | Yield | $0.05M | dead-site; no-revenue-tracked; no-mcap |
| 157 | **Beets LST** (`beets-lst`) | Sonic,Fantom | Liquid Staking | $3.53M | **deprecated**; rev≈$1.1k/mo; no-mcap |
| 158 | **Chainge Finance** (`chainge-finance`) | Rollux,Fusion | Dexs | $13.16M | dead-site; no-revenue-tracked; no-mcap |
| 159 | **Seamless Vaults** (`seamless-vaults`) | Base | Onchain Capital Allocator | $1.69M | rev≈$0.0k/mo; no-mcap |
| 160 | **Vessel Finance** (`vessel-finance`) | Scroll | Dexs | $0.19M | dead-site; no-revenue-tracked; no-mcap |
| 161 | **Aurus** (`aurus`) | Ethereum | RWA | $7.89M | dead-site; no-revenue-tracked; no-mcap |
| 162 | **illumineX** (`illuminex`) | Sapphire | Cross Chain Bridge | $0.12M | dead-site; no-revenue-tracked; no-mcap |
| 163 | **FlowX V3** (`flowx-v3`) | Sui | Dexs | $0.10M | rev≈$0.0k/mo; no-mcap |
| 164 | **Ouroboros Capital** (`ouroboros-capital`) | Monad,Ethereum | Risk Curators | $1.05M | rev≈$0.0k/mo; no-mcap |
| 165 | **OpenBook** (`openbook`) | Solana | Dexs | $1.13M | dead-site; no-revenue-tracked; no-mcap |
| 166 | **Dinero (pxETH)** (`dinero-pxeth`) | Ethereum | Liquid Staking | $5.28M | rev≈$0.0k/mo; no-mcap |
| 167 | **Yama Finance** (`yama-finance`) | Arbitrum,Polygon zkEVM | CDP | $0.08M | **deprecated**; dead-site; no-revenue-tracked; no-mcap |
| 168 | **Navigator** (`navigator`) | Sonic | Derivatives | $0.37M | rev≈$0.6k/mo; no-mcap |
| 169 | **Avantis** (`avantis`) | Base | Derivatives | $16.47M | rev≈$0.0k/mo |
| 170 | **Bucket Farm** (`bucket-farm`) | Sui | Farm | $37.98M | **deprecated**; no-revenue-tracked; no-mcap |
| 171 | **Hydro Inflow** (`hydro-inflow`) | Neutron | Yield | $2.37M | rev≈$0.0k/mo; no-mcap |
| 172 | **AquaBank** (`aquabank`) | Avalanche | Yield | $0.52M | rev≈$0.0k/mo; no-mcap |
| 173 | **sDAI** (`sdai`) | xDai | Yield | $51.99M | dead-site; rev≈$0.0k/mo |
| 174 | **Convergence Fi** (`convergence-fi`) | Ethereum | Yield | $0.84M | dead-site; no-revenue-tracked; no-mcap |
| 175 | **Folks Finance Lending** (`folks-finance-lending`) | Algorand | Lending | $21.61M | rev≈$0.3k/mo; no-mcap |
| 176 | **Haiko** (`haiko`) | Starknet | Dexs | $0.06M | dead-site; no-revenue-tracked; no-mcap |
| 177 | **SingularV** (`singularv`) | Ethereum | Risk Curators | $0.44M | rev≈$0.0k/mo; no-mcap |
| 178 | **DoubleZero Staked SOL** (`doublezero-staked-sol`) | Solana | Liquid Staking | $75.52M | TVL -39%/7d; no-mcap |
| 179 | **Arena SocialFi** (`arena-socialfi`) | Avalanche | SoFi | $0.14M | rev≈$0.6k/mo; fork:friend.tech V1; no-mcap |
| 180 | **HyperLend Isolated** (`hyperlend-isolated`) | Hyperliquid L1 | Lending | $0.37M | rev≈$0.3k/mo; no-mcap |
| 181 | **Augury Finance** (`augury-finance`) | Polygon | Yield | $0.27M | dead-site; no-revenue-tracked; no-mcap |
| 182 | **Puffer Vaults** (`puffer-vaults`) | Ethereum | Onchain Capital Allocator | $0.80M | rev≈$0.1k/mo; no-mcap |
| 183 | **CGO Finance** (`cgo-finance`) | Cronos | Yield Aggregator | $1.04M | dead-site; no-revenue-tracked; no-mcap |
| 184 | **StableJack V1** (`stablejack-v1`) | Avalanche | Yield | $1.16M | **deprecated**; no-revenue-tracked; no-mcap |
| 185 | **Zencha Finance** (`zencha-finance`) | Boba | Dexs | $0.08M | dead-site; no-revenue-tracked; no-mcap |
| 186 | **Contango V2** (`contango-v2`) | Ethereum,Arbitrum | Derivatives | $6.16M | rev≈$1.1k/mo; no-mcap |
| 187 | **Kalax** (`kalax`) | Blast,Scroll | Yield Aggregator | $0.15M | dead-site; no-revenue-tracked; no-mcap |
| 188 | **Hyperion** (`hyperion`) | Aptos | Dexs | $2.66M | rev≈$2.2k/mo; no-mcap |
| 189 | **Milkyway Rollup Bridge** (`milkyway-rollup-bridge`) | Initia | Canonical Bridge | $0.05M | dead-site; no-revenue-tracked; no-mcap |
| 190 | **Balanced Exchange** (`balanced-exchange`) | Avalanche,Icon | Dexs | $2.13M | rev≈$0.0k/mo; no-mcap |
| 191 | **Depth** (`depth`) | Binance,Heco | Dexs | $1.18M | dead-site; no-revenue-tracked; no-mcap |
| 192 | **DAO Swap** (`dao-swap`) | Binance | Dexs | $0.05M | dead-site; no-revenue-tracked; no-mcap |
| 193 | **Stabl.fi V1** (`stabl-fi-v1`) | Polygon | Yield | $0.06M | dead-site; no-revenue-tracked; fork:Origin Dollar; no-mcap |
| 194 | **Alpaca Leveraged Yield Farming** (`alpaca-leveraged-yield-farming`) | Binance,Fantom | Leveraged Farming | $33.55M | dead-site; no-revenue-tracked; no-mcap |
| 195 | **Olive Cash** (`olive-cash`) | Binance,Avalanche | Yield | $0.09M | dead-site; no-revenue-tracked |
| 196 | **marginfi Lending** (`marginfi-lending`) | Solana | Lending | $32.02M | **deprecated**; no-revenue-tracked; no-mcap |
| 197 | **Stronghold Staked SOL** (`stronghold-staked-sol`) | Solana | Liquid Staking | $4.37M | rev≈$0.3k/mo; no-mcap |
| 198 | **Tribe.run** (`tribe-run`) | Solana | SoFi | $0.21M | rev≈$0.3k/mo; no-mcap |
| 199 | **Theo Network thBill** (`theo-network-thbill`) | Solana,Ethereum | RWA | $26.42M | rev≈$0.0k/mo; TVL -58%/7d; no-mcap |
| 200 | **Rho Protocol** (`rho-protocol`) | Arbitrum | Dexs | $0.06M | **deprecated**; no-revenue-tracked; no-mcap |
| 201 | **SYMMIO** (`symmio`) | Base,Arbitrum | Derivatives | $2.76M | rev≈$0.2k/mo |
| 202 | **set.wtf** (`set-wtf`) | Ethereum | Yield | $0.32M | dead-site; no-revenue-tracked; no-mcap |
| 203 | **Aegis YUSD** (`aegis-yusd`) | Ethereum,Binance | Basis Trading | $34.85M | rev≈$0.0k/mo; no-mcap |
| 204 | **GIGA V2** (`giga-v2`) | Robinhood Chain | Dexs | $0.07M | rev≈$0.3k/mo; no-mcap |
| 205 | **Resolv USR** (`resolv-usr`) | Ethereum | Basis Trading | $6.36M | rev≈$0.0k/mo |
| 206 | **Juice Finance** (`juice-finance`) | Blast | Leveraged Farming | $0.16M | rev≈$0.0k/mo |
| 207 | **Adamant Finance** (`adamant-finance`) | Polygon,Arbitrum | Yield | $0.17M | dead-site; no-revenue-tracked; no-mcap |
| 208 | **Molten V3** (`molten-v3`) | CORE | Dexs | $0.20M | rev≈$0.0k/mo; no-mcap |
| 209 | **What The Hook** (`what-the-hook`) | Robinhood Chain | Liquidity Automation | $0.21M | rev≈$0.0k/mo |
| 210 | **Remora Markets** (`remora-markets`) | Solana | RWA | $0.22M | **deprecated**; dead-site; no-revenue-tracked; no-mcap |
| 211 | **Clober Liquidity Vault** (`clober-liquidity-vault`) | Base,Monad | Dexs | $0.05M | no-revenue-tracked; TVL -71%/7d; no-mcap |
| 212 | **Amulet Liquidity Staking** (`amulet-liquidity-staking`) | Solana | Liquid Staking | $0.31M | dead-site; no-revenue-tracked; no-mcap |
| 213 | **up v3** (`up-v3`) | Robinhood Chain | Dexs | $7.56M | TVL -31%/7d; no-mcap |
| 214 | **Perpetual Protocol** (`perpetual-protocol`) | Ethereum,Optimism | Derivatives | $0.44M | dead-site; rev≈$0.0k/mo |
| 215 | **SuiDollar Basis** (`suidollar-basis`) | Sui | Basis Trading | $0.25M | **deprecated**; dead-site; no-revenue-tracked; no-mcap |
| 216 | **Whales Market** (`whales-market`) | Ethereum,Solana | OTC Marketplace | $0.73M | rev≈$0.2k/mo |
| 217 | **flaunch** (`flaunch`) | Base | Launchpad | $1.77M | rev≈$0.0k/mo; no-mcap |
| 218 | **lisAster** (`lisaster`) | Binance | Yield Aggregator | $1.19M | rev≈$0.9k/mo; no-mcap |
| 219 | **MoreMarkets.xyz** (`moremarkets-xyz`) | Ethereum,Flare | Yield | $0.48M | dead-site; no-revenue-tracked; no-mcap |
| 220 | **Odyssey Finance** (`odyssey-finance`) | Ethereum,Plasma | Yield Aggregator | $8.47M | rev≈$0.3k/mo; no-mcap |
| 221 | **Serum Swap** (`serum-swap`) | Solana | Dexs | $0.22M | dead-site; no-revenue-tracked; no-mcap |
| 222 | **Echo Lending** (`echo-lending`) | Aptos | Lending | $5.25M | rev≈$0.0k/mo; no-mcap |
| 223 | **Soroswap** (`soroswap`) | Stellar | Dexs | $1.20M | rev≈$0.0k/mo; TVL -100%/7d; no-mcap |
| 224 | **StockFi** (`stockfi`) | Binance | Lending | $0.09M | rev≈$0.0k/mo; no-mcap |
| 225 | **Peer** (`peer`) | Base | Payments | $0.07M | rev≈$0.0k/mo; no-mcap |
| 226 | **DoubleUp** (`doubleup`) | Sui | Luck Games | $0.51M | rev≈$0.4k/mo |
| 227 | **BasketDAO** (`basketdao`) | Ethereum | Indexes | $0.10M | dead-site; no-revenue-tracked; no-mcap |
| 228 | **Keyring** (`keyring`) | Avalanche | Risk Curators | $6.22M | rev≈$0.0k/mo; no-mcap |
| 229 | **Drop** (`drop`) | Neutron | Liquid Staking | $0.53M | dead-site; no-revenue-tracked; no-mcap |
| 230 | **BFly Finance** (`bfly-finance`) | Starcoin | Lending | $0.14M | dead-site; no-revenue-tracked; no-mcap |
| 231 | **SithSwap** (`sithswap`) | Starknet | Dexs | $0.17M | dead-site; no-revenue-tracked; no-mcap |
| 232 | **Shield Swap** (`shield-swap`) | Aleo | Dexs | $0.47M | rev≈$0.4k/mo; no-mcap |
| 233 | **NX Finance** (`nx-finance`) | Solana | Yield Aggregator | $2.17M | dead-site; no-revenue-tracked |
| 234 | **WingRiders** (`wingriders`) | Cardano | Dexs | $2.70M | rev≈$0.0k/mo |
| 235 | **Core Markets** (`core-markets`) | Blast | Derivatives | $0.27M | dead-site; no-revenue-tracked; no-mcap |
| 236 | **Hyphen** (`hyphen`) | Polygon,Arbitrum | Bridge | $0.10M | **deprecated**; no-revenue-tracked |
| 237 | **Rose** (`rose`) | Aurora | Dexs | $0.12M | dead-site; no-revenue-tracked; no-mcap |
| 238 | **FIAT DAO** (`fiat-dao`) | Ethereum | Yield | $0.10M | dead-site; no-revenue-tracked; no-mcap |
| 239 | **Lulo** (`lulo`) | Solana | Yield Aggregator | $53.02M | rev≈$0.0k/mo; no-mcap |
| 240 | **STEAMM** (`steamm`) | Sui | Dexs | $0.37M | rev≈$0.5k/mo; no-mcap |
| 241 | **Swop** (`swop`) | Waves,UNIT0 | Dexs | $0.31M | rev≈$0.5k/mo |
| 242 | **Balmy** (`balmy`) | Ethereum,Optimism | DCA Tools | $0.22M | **deprecated**; no-revenue-tracked; no-mcap |
| 243 | **Surge Credit** (`surge-credit`) | Base,Bitcoin | Lending | $1.17M | rev≈$0.7k/mo; no-mcap |
| 244 | **Pods Finance** (`pods-finance`) | Polygon,Ethereum | Options | $0.39M | dead-site; no-revenue-tracked; no-mcap |
| 245 | **Avantgarde** (`avantgarde`) | Ethereum | Risk Curators | $0.34M | rev≈$0.0k/mo; no-mcap |
| 246 | **Cellana Finance** (`cellana-finance`) | Aptos | Dexs | $0.43M | rev≈$0.0k/mo |
| 247 | **STFIL** (`stfil`) | Filecoin | Liquid Staking | $3.78M | dead-site; no-revenue-tracked; no-mcap |
| 248 | **OroSwap** (`oroswap`) | ZIGChain | Dexs | $3.37M | rev≈$2.2k/mo; no-mcap |
| 249 | **ExinPool** (`exinpool`) | Mixin | Liquid Staking | $9.59M | dead-site; no-revenue-tracked; no-mcap |
| 250 | **YO Protocol** (`yo-protocol`) | Base,Ethereum | Yield Aggregator | $37.14M | rev≈$0.0k/mo; no-mcap |
| 251 | **MooniSwap** (`mooniswap`) | Ethereum | Dexs | $0.52M | dead-site; rev≈$0.0k/mo; no-mcap |
| 252 | **Sparkswap** (`sparkswap`) | Pulse | Farm | $0.18M | dead-site; no-revenue-tracked; no-mcap |
| 253 | **Spice Finance** (`spice-finance`) | Ethereum | Yield Aggregator | $0.13M | dead-site; no-revenue-tracked; no-mcap |
| 254 | **eva Markets** (`eva-markets`) | Ethereum | RWA | $5.08M | rev≈$0.0k/mo; no-mcap |
| 255 | **Kayen Finance LST** (`kayen-finance-lst`) | Chiliz | Liquid Staking | $0.14M | rev≈$0.1k/mo; no-mcap |
| 256 | **Astake** (`astake`) | Astar | Liquid Staking | $0.18M | no-revenue-tracked; TVL -21%/7d; no-mcap |
| 257 | **Amun** (`amun`) | Solana,Ethereum | Indexes | $0.38M | dead-site; no-revenue-tracked; no-mcap |
| 258 | **Overpass** (`overpass`) | Solana | Yield | $0.63M | rev≈$0.0k/mo; no-mcap |
| 259 | **ThalaSwap** (`thalaswap`) | Aptos | Dexs | $0.63M | rev≈$0.1k/mo |
| 260 | **HashMix FIL** (`hashmix-fil`) | Filecoin | Liquid Staking | $0.16M | dead-site; no-revenue-tracked; no-mcap |
| 261 | **Drift Trade** (`drift-trade`) | Solana | Derivatives | $0.64M | rev≈$0.0k/mo; no-mcap |
| 262 | **Kriya Strats** (`kriya-strats`) | Sui | Yield | $0.07M | dead-site; no-revenue-tracked; no-mcap |
| 263 | **Fiamma** (`fiamma`) | Bitcoin | Bridge | $1.15M | dead-site; no-revenue-tracked; no-mcap |
| 264 | **CaviarNine LSU Pool** (`caviarnine-lsu-pool`) | Radix | Dexs | $0.27M | rev≈$0.0k/mo; no-mcap |
| 265 | **Indigo** (`indigo`) | Cardano | CDP | $4.06M | rev≈$0.0k/mo |
| 266 | **AlienFi** (`alienfi`) | Arbitrum | Dexs | $0.08M | rev≈$0.0k/mo; no-mcap |
| 267 | **Haedal Vault** (`haedal-vault`) | Sui | Farm | $0.95M | rev≈$0.5k/mo; no-mcap |
| 268 | **Fathom CDP** (`fathom-cdp`) | XDC | CDP | $0.24M | rev≈$0.4k/mo; no-mcap |
| 269 | **Ferra DLMM** (`ferra-dlmm`) | Sui | Dexs | $0.17M | rev≈$0.1k/mo; no-mcap |
| 270 | **DefiEdge** (`defiedge`) | Binance,Polygon | Liquidity Manager | $0.88M | dead-site; no-revenue-tracked; no-mcap |
| 271 | **Joe V2.1** (`joe-v2-1`) | Avalanche,Arbitrum | Dexs | $3.56M | rev≈$0.6k/mo; no-mcap |
| 272 | **9Summits** (`9summits`) | Ethereum,Base | Risk Curators | $0.08M | rev≈$0.0k/mo; no-mcap |
| 273 | **Dinari** (`dinari`) | Kinto,Plume | RWA | $10.83M | rev≈$0.0k/mo; no-mcap |
| 274 | **Alpaca Finance 2.0** (`alpaca-finance-2-0`) | Binance | Lending | $12.73M | dead-site; no-revenue-tracked; no-mcap |
| 275 | **Origin Sonic** (`origin-sonic`) | Sonic | Liquid Staking | $0.17M | rev≈$0.0k/mo; no-mcap |
| 276 | **Milkyway Restaking** (`milkyway-restaking`) | Milkyway | Restaking | $0.24M | dead-site; no-revenue-tracked; no-mcap |
| 277 | **HawkFi** (`hawkfi`) | Solana | Liquidity Manager | $8.06M | dead-site |
| 278 | **BackedFi** (`backedfi`) | Ethereum,xDai | RWA | $4.35M | rev≈$0.0k/mo; no-mcap |
| 279 | **Kinto Bridge** (`kinto-bridge`) | Ethereum | Canonical Bridge | $0.67M | dead-site; no-revenue-tracked; no-mcap |
| 280 | **Rakeoff** (`rakeoff`) | ICP | Staking Pool | $6.66M | **deprecated**; no-revenue-tracked; no-mcap |
| 281 | **Bonkswap** (`bonkswap`) | Solana | Dexs | $0.63M | rev≈$0.5k/mo; no-mcap |
| 282 | **Wrapped HLP** (`wrapped-hlp`) | Hyperliquid L1 | Yield | $1.52M | rev≈$0.7k/mo |
| 283 | **Cap Finance v1-v3** (`cap-finance-v1-v3`) | Arbitrum | Derivatives | $0.21M | dead-site; no-revenue-tracked; no-mcap |
| 284 | **PieDAO** (`piedao`) | Ethereum | Indexes | $0.95M | dead-site; no-revenue-tracked; no-mcap |
| 285 | **Trueo** (`trueo`) | Base | Prediction Market | $0.88M | rev≈$0.9k/mo |
| 286 | **FortiFi** (`fortifi`) | Avalanche | Yield Aggregator | $0.37M | dead-site; no-revenue-tracked; no-mcap |
| 287 | **Nimbora Yield Aggregator** (`nimbora-yield-aggregator`) | Starknet | Yield | $0.06M | **deprecated**; no-revenue-tracked; no-mcap |
| 288 | **Pala** (`pala`) | Klaytn | Dexs | $0.27M | dead-site; no-revenue-tracked; no-mcap |
| 289 | **KLAYstation** (`klaystation`) | Klaytn | Liquid Staking | $1.34M | no-revenue-tracked; TVL -100%/7d; no-mcap |
| 290 | **Hyperbeat LST** (`hyperbeat-lst`) | Hyperliquid L1 | Liquid Staking | $13.46M | rev≈$0.0k/mo; no-mcap |
| 291 | **Friend3** (`friend3`) | Binance,Op_Bnb | SoFi | $0.08M | rev≈$0.0k/mo; fork:friend.tech V1; no-mcap |
| 292 | **Viva** (`viva`) | Vite | Yield | $0.08M | dead-site; no-revenue-tracked; no-mcap |
| 293 | **Loopscale** (`loopscale`) | Solana | Lending | $92.80M | rev≈$0.0k/mo; no-mcap |
| 294 | **JPG Store** (`jpg-store`) | Cardano | NFT Marketplace | $0.16M | rev≈$0.2k/mo; no-mcap |
| 295 | **Serum** (`serum`) | Solana | Dexs | $16.37M | dead-site; no-revenue-tracked |
| 296 | **BitFi BTC** (`bitfi-btc`) | AILayer | Anchor BTC | $79.56M | rev≈$0.0k/mo; no-mcap |
| 297 | **fan.fun** (`fan-fun`) | Hyperliquid L1 | SoFi | $0.05M | dead-site; no-revenue-tracked; no-mcap |
| 298 | **Kriya AMM** (`kriya-amm`) | Sui | Dexs | $0.18M | dead-site; no-revenue-tracked; no-mcap |
| 299 | **Lifinity V1** (`lifinity-v1`) | Solana | Dexs | $0.07M | **deprecated**; no-revenue-tracked; no-mcap |
| 300 | **Bitget SOL** (`bitget-sol`) | Solana | Liquid Staking | $18.11M | rev≈$0.1k/mo; no-mcap |
| 301 | **River Omni-CDP** (`river-omni-cdp`) | Binance,Base | CeDeFi | $97.57M | rev≈$0.0k/mo; no-mcap |
| 302 | **Omm** (`omm`) | Icon | Lending | $0.15M | dead-site; no-revenue-tracked; no-mcap |
| 303 | **Avant avBTC** (`avant-avbtc`) | Avalanche | Onchain Capital Allocator | $8.41M | rev≈$2.6k/mo; no-mcap |
| 304 | **Zentra Finance** (`zentra-finance`) | Citrea | Lending | $2.00M | rev≈$0.8k/mo; no-mcap |
| 305 | **Beraborrow** (`beraborrow`) | Berachain | CDP | $0.29M | rev≈$0.0k/mo |
| 306 | **Goose Finance** (`goose-finance`) | Binance | Farm | $0.32M | dead-site; no-revenue-tracked |
| 307 | **Bond** (`bond`) | 0G | Dexs | $0.18M | rev≈$0.0k/mo; no-mcap |
| 308 | **PostTechSoFi** (`posttechsofi`) | Arbitrum | SoFi | $0.06M | dead-site; rev≈$0.0k/mo; fork:friend.tech V1; no-mcap |
| 309 | **Atrix** (`atrix`) | Solana | Dexs | $1.06M | dead-site; no-revenue-tracked; no-mcap |
| 310 | **Dojoswap AMM** (`dojoswap-amm`) | Injective | Dexs | $0.40M | dead-site; no-revenue-tracked; no-mcap |
| 311 | **Edgevana** (`edgevana`) | Solana | Liquid Staking | $0.11M | rev≈$0.3k/mo; no-mcap |
| 312 | **marginfi LST** (`marginfi-lst`) | Solana | Liquid Staking | $10.22M | **deprecated**; rev≈$0.1k/mo; no-mcap |
| 313 | **10KSwap** (`10kswap`) | Starknet | Dexs | $0.75M | dead-site; no-revenue-tracked; no-mcap |
| 314 | **Jupiter Prediction** (`jupiter-prediction`) | Solana | Interface | $0.47M | rev≈$0.0k/mo; no-mcap |
| 315 | **SimpleDEX** (`simpledex`) | Proton | Dexs | $0.26M | rev≈$0.2k/mo; no-mcap |
| 316 | **Sunny** (`sunny`) | Solana | Yield | $2.77M | dead-site; no-revenue-tracked; no-mcap |
| 317 | **ZO Perps** (`zo-perps`) | Sui | Derivatives | $0.13M | rev≈$1.0k/mo; fork:Sudo Perps; no-mcap |
| 318 | **Cadabra Finance** (`cadabra-finance`) | Sonic,Binance | Yield Aggregator | $0.06M | dead-site; no-revenue-tracked; no-mcap |
| 319 | **Aequinox** (`aequinox`) | Binance | Dexs | $0.63M | dead-site; no-revenue-tracked; no-mcap |
| 320 | **Armada** (`armada`) | Solana | Liquidity Manager | $0.54M | dead-site; no-revenue-tracked; no-mcap |
| 321 | **Alchemix V2** (`alchemix-v2`) | Ethereum,Optimism | Synthetics | $0.08M | rev≈$0.0k/mo; no-mcap |
| 322 | **SiloStake** (`silostake`) | Sei | Liquid Staking | $0.11M | dead-site; no-revenue-tracked; no-mcap |
| 323 | **VanEck Treasury Fund** (`vaneck-treasury-fund`) | Ethereum,Binance | RWA | $57.82M | TVL -70%/7d; no-mcap |
| 324 | **DefiPlaza** (`defiplaza`) | Radix,Ethereum | Dexs | $0.21M | rev≈$0.3k/mo |

---

**324 unwatched protocols** holding a combined $2,193M, none previously delivered.
Coverage list, not a ranking. The signal is neglect: real money with no one paid to watch it.
