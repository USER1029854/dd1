# Random audit batch — round 2 — 180 more protocols, non-overlapping

> **Second draw of the un-patterned coverage list.** Same idea and same filters as
> `RANDOM_AUDIT_BATCH.md`, a fresh random seed, and **guaranteed no overlap** with round 1 or anything
> delivered before. Random on purpose — breadth of coverage, not a thesis per row.

**Filters (only these):** alive (not deprecated/rugged/dead); `$50k ≤ TVL ≤ $50M` at head (excludes the
extremely-watched giants, keeps real money at stake); **not a direct fork of a major protocol**
(Uniswap/Aave/Compound/Balancer/Curve/Liquity/GMX/Yearn/Solidly/Algebra/Olympus/Lido/Synthetix/Maker/…
dropped → bespoke/original code remains); not CEX / not an L1 chain; **not previously delivered** (cleared
the 1,007-name exclusion set, then folded into it).

**Reproducible.** `random.seed(770077)` over the **879-protocol** pool that remained after round 1 was
removed. TVL read at head from DefiLlama `/protocols`, 2026-08-29.

**Notes legend:** `unaudited` = no audit listed (a flag, not proof); `churn:N` = N timestamped hallmarks
(migrations/updates/incidents); `fork:X` = fork of a *minor* template; `orc:…` = declared oracle(s).
**Cheap first pass per row:** is it an upgradeable proxy, and how often has the implementation changed? —
that churn is where storage-collision, re-init, and forgotten-authority bugs concentrate.

Composition — categories: Dexs 41, Liquid Staking 20, Lending 20, Yield 17, Derivatives 11, CDP 9, RWA 8, Launchpad 5, Bridge 5, Canonical Bridge 4. Unaudited-flagged: 93. Churn-flagged: 14. Primary chains: Ethereum 29, Solana 21, Binance 9, Polygon 7, Arbitrum 7, Hyperliquid L1 5, Sui 5, Monad 5.

| # | Protocol | Chain(s) | Category | TVL@head | Notes |
|--:|---|---|---|--:|---|
| 1 | **Valantis STEX** (`valantis-stex`) | Hyperliquid L1 | Dexs | $5.41M |  |
| 2 | **JPOW AI** (`jpow-ai`) | Solana | CDP | $0.20M | unaudited |
| 3 | **Zircuit** (`zircuit`) | Ethereum | Canonical Bridge | $4.95M | unaudited |
| 4 | **Neemo Finance** (`neemo-finance`) | Astar,Ethereum | Liquid Restaking | $0.99M |  |
| 5 | **Hydro LST** (`hydro-lst`) | Injective | Liquid Staking | $9.32M |  |
| 6 | **Aries Markets** (`aries-markets`) | Aptos | Lending | $0.07M | orc:Pyth,Switchboard |
| 7 | **Canopy** (`canopy`) | Movement | Yield Aggregator | $1.13M |  |
| 8 | **Saros DLMM** (`saros-dlmm`) | Solana | Dexs | $0.12M |  |
| 9 | **DAOLama** (`daolama`) | TON | Lending | $0.05M | unaudited |
| 10 | **Prime Staking** (`prime-staking`) | XDC | Liquid Staking | $6.62M | unaudited |
| 11 | **Binaryx Platform** (`binaryx-platform`) | Polygon | RWA | $8.96M |  |
| 12 | **Save SOL** (`save-sol`) | Solana | Liquid Staking | $6.39M | unaudited |
| 13 | **YBTC.B** (`ybtc-b`) | Bitlayer | Anchor BTC | $0.15M | unaudited |
| 14 | **WaterNeuron** (`waterneuron`) | ICP | Liquid Staking | $5.78M |  |
| 15 | **BAMM** (`bamm`) | Fraxtal | Lending | $1.93M | unaudited |
| 16 | **Liqwid** (`liqwid`) | Cardano | Lending | $12.40M |  |
| 17 | **ScrubVault** (`scrubvault`) | Kava,Arbitrum | Basis Trading | $0.14M | unaudited |
| 18 | **Linx App** (`linx-app`) | Alephium | Lending | $0.08M |  |
| 19 | **Pools Finance** (`pools-finance`) | IOTA | Dexs | $1.09M |  |
| 20 | **SquadSwap Dynamo** (`squadswap-dynamo`) | Binance | Dexs | $0.27M |  |
| 21 | **OmniBTC** (`omnibtc`) | Sui,Arbitrum | Lending | $1.75M | unaudited; orc:Pyth |
| 22 | **Token Mill** (`token-mill`) | Avalanche,Solana | Launchpad | $0.07M | unaudited |
| 23 | **FaroSwap** (`faroswap`) | Pharos | Dexs | $0.92M | unaudited |
| 24 | **four.meme** (`four-meme`) | Binance | Launchpad | $4.40M |  |
| 25 | **Mezo Borrow** (`mezo-borrow`) | Mezo | CDP | $3.98M | unaudited |
| 26 | **Hyperstable CDP** (`hyperstable-cdp`) | Hyperliquid L1 | CDP | $0.16M | orc:Pyth |
| 27 | **Varlamore Capital** (`varlamore-capital`) | Sonic,Ethereum | Risk Curators | $0.62M | churn:1 |
| 28 | **DSF.Finance** (`dsf-finance`) | Ethereum | Yield | $0.40M | churn:1 |
| 29 | **Kamigotchi** (`kamigotchi`) | Yominet | Gaming | $0.15M | unaudited |
| 30 | **Button Tranche** (`button-tranche`) | Ethereum | Yield | $0.43M |  |
| 31 | **PancakeSwap StableSwap** (`pancakeswap-stableswap`) | Binance,Arbitrum | Dexs | $3.76M | unaudited |
| 32 | **Orderly Chain** (`orderly-chain`) | Ethereum | Canonical Bridge | $0.32M | unaudited |
| 33 | **T RIZE** (`t-rize`) | Base | RWA | $23.00M | unaudited |
| 34 | **mStable V2** (`mstable-v2`) | Ethereum | CDP | $3.11M | unaudited |
| 35 | **Francium** (`francium`) | Solana | Yield | $6.14M | churn:1; orc:Pyth |
| 36 | **Saros AMM** (`saros-amm`) | Solana | Dexs | $0.06M |  |
| 37 | **BIM Yield** (`bim-yield`) | Base,Polygon | Yield Aggregator | $0.24M |  |
| 38 | **GoPlus Locker V3** (`goplus-locker-v3`) | Binance,Base | Token Locker | $30.31M | unaudited |
| 39 | **Stratis Liquid Staking** (`stratis-liquid-staking`) | Stratis | Liquid Staking | $0.39M |  |
| 40 | **TradeGPT** (`tradegpt`) | 0G | Dexs | $1.93M | unaudited |
| 41 | **Cetus CLMM** (`cetus-clmm`) | Sui,Aptos | Dexs | $23.21M | unaudited |
| 42 | **Rocket Bridge** (`rocket-bridge`) | Arbitrum | Bridge | $0.22M | unaudited |
| 43 | **Ammalgam Vaults** (`ammalgam-vaults`) | Ethereum | Yield | $1.64M |  |
| 44 | **Sharky** (`sharky`) | Solana | NFT Lending | $0.13M | unaudited |
| 45 | **sICX** (`sicx`) | Icon | Liquid Staking | $0.37M | unaudited; orc:Band |
| 46 | **ENKI Protocol** (`enki-protocol`) | Metis | Liquid Staking | $0.24M |  |
| 47 | **Shell Protocol** (`shell-protocol`) | Arbitrum | Dexs | $0.13M | unaudited; churn:1 |
| 48 | **LiquidSwap** (`liquidswap`) | Aptos | Dexs | $1.19M |  |
| 49 | **CatFee Staking Vault** (`catfee-staking-vault`) | Tron | Staking Pool | $17.70M | unaudited |
| 50 | **Bucket Protocol V2** (`bucket-protocol-v2`) | Sui | CDP | $7.54M | unaudited |
| 51 | **Flex** (`flex`) | Ethereum | Lending | $1.06M | unaudited |
| 52 | **T3tris Finance** (`t3tris-finance`) | Arbitrum,Robinhood Chain | Onchain Capital Allocator | $13.28M |  |
| 53 | **sTLOS Liquid Staking** (`stlos-liquid-staking`) | Telos | Liquid Staking | $0.35M |  |
| 54 | **MovePosition** (`moveposition`) | Movement | Lending | $1.31M | orc:Pyth,Switchboard |
| 55 | **Manifest Trade** (`manifest-trade`) | Solana | Dexs | $19.43M | unaudited |
| 56 | **Choice Exchange** (`choice-exchange`) | Injective | Dexs | $0.23M |  |
| 57 | **zkBob** (`zkbob`) | Polygon,Optimism | Privacy | $0.24M | unaudited |
| 58 | **MetalX Lending** (`metalx-lending`) | Proton | Lending | $36.52M | orc:TWAP |
| 59 | **Uniswap V1** (`uniswap-v1`) | Ethereum | Dexs | $3.94M |  |
| 60 | **TownSquare Loop Vaults** (`townsquare-loop-vaults`) | Monad,Base | Leveraged Farming | $0.13M | unaudited |
| 61 | **Opyn Gamma** (`opyn-gamma`) | Ethereum,Polygon | Options | $1.08M | orc:Chainlink |
| 62 | **Picnic** (`picnic`) | Polygon | Indexes | $0.20M |  |
| 63 | **Permapod** (`permapod`) | ZIGChain | Lending | $0.25M | churn:1; fork:Mars Lend; orc:Stork |
| 64 | **Wombat Exchange** (`wombat-exchange`) | Binance,Arbitrum | Dexs | $1.48M | churn:2 |
| 65 | **Axiome Swap** (`axiome-swap`) | Axiome | Dexs | $0.52M | unaudited |
| 66 | **Gate Swap Spot** (`gate-swap-spot`) | GateLayer | Dexs | $2.76M | unaudited |
| 67 | **Eternal Finance** (`eternal-finance`) | Aptos | Yield | $0.26M | unaudited; orc:Internal |
| 68 | **Metric V2** (`metric-v2`) | Ethereum,Base | Dexs | $4.80M | unaudited |
| 69 | **BetterSwap V2** (`betterswap-v2`) | VeChain | Dexs | $0.25M |  |
| 70 | **Sovryn Dex** (`sovryn-dex`) | RSK,BOB | Dexs | $8.58M |  |
| 71 | **Scrub Invest** (`scrub-invest`) | Kava | Yield | $7.02M | unaudited |
| 72 | **AnyHedge** (`anyhedge`) | Bitcoincash | Derivatives | $4.24M | unaudited; churn:3; orc:Oracles.Cash |
| 73 | **Veno Finance** (`veno-finance`) | Cronos,Ethereum | Liquid Staking | $35.35M |  |
| 74 | **HypurrFi Isolated** (`hypurrfi-isolated`) | Hyperliquid L1 | Lending | $0.71M | orc:Pyth |
| 75 | **Optim Finance** (`optim-finance`) | Cardano | Staking Rental | $0.77M |  |
| 76 | **Solomon USDv** (`solomon-usdv`) | Solana | Basis Trading | $1.51M |  |
| 77 | **Temple** (`temple`) | Canton | Dexs | $5.86M | unaudited |
| 78 | **Kava Mint** (`kava-mint`) | Kava | CDP | $11.84M | unaudited; orc:Internal |
| 79 | **Pirex** (`pirex`) | Ethereum,Arbitrum | Yield | $3.76M |  |
| 80 | **Paimon** (`paimon`) | Binance | RWA | $12.35M |  |
| 81 | **TruStake** (`trustake`) | Aptos,Injective | Liquid Staking | $3.86M |  |
| 82 | **Napier** (`napier`) | Ethereum,Base | Yield | $0.11M |  |
| 83 | **40 Acres** (`40-acres`) | Base,Optimism | Lending | $31.31M |  |
| 84 | **Enhanced** (`enhanced`) | Ethereum | Yield | $0.17M | unaudited; fork:Opyn Gamma |
| 85 | **Tangible RWA** (`tangible-rwa`) | Polygon,Arbitrum | RWA | $42.40M | churn:1; orc:Curve |
| 86 | **Aktionariat** (`aktionariat`) | Ethereum,Polygon | RWA | $0.37M | unaudited; orc:Chainlink |
| 87 | **LFJ POE** (`lfj-poe`) | Monad | Dexs | $0.16M | unaudited |
| 88 | **Liquidium** (`liquidium`) | ICP | Lending | $4.36M | unaudited |
| 89 | **HyperWave** (`hyperwave`) | Hyperliquid L1,Arbitrum | Yield | $2.16M |  |
| 90 | **Soneium Bridge** (`soneium-bridge`) | Ethereum | Canonical Bridge | $0.17M | unaudited |
| 91 | **Interlay BTC** (`interlay-btc`) | Interlay | Bridge | $0.17M | unaudited; orc:DIA |
| 92 | **Kai Finance** (`kai-finance`) | Sui | Leveraged Farming | $1.44M | unaudited; orc:Pyth |
| 93 | **Verified Network** (`verified-network`) | Ethereum,Base | RWA | $0.13M | unaudited |
| 94 | **Arbitrove** (`arbitrove`) | Arbitrum | Indexes | $0.61M | orc:Dark Oracle |
| 95 | **alphagrowth** (`alphagrowth`) | Unichain,Base | Risk Curators | $6.92M | unaudited |
| 96 | **Goldilocks** (`goldilocks`) | Berachain | Yield | $0.53M | unaudited |
| 97 | **Doma DEX V3** (`doma-dex-v3`) | Doma | Dexs | $0.91M |  |
| 98 | **Cozy V2** (`cozy-v2`) | Optimism | Insurance | $0.17M | orc:Chainlink,UMA |
| 99 | **FlashTrade** (`flashtrade`) | Solana | Derivatives | $3.47M | unaudited; orc:Pyth |
| 100 | **aPriori** (`apriori`) | Monad | Liquid Staking | $0.68M | unaudited |
| 101 | **9mm V2** (`9mm-v2`) | Pulse,Base | Dexs | $0.08M | unaudited |
| 102 | **Kava Liquid** (`kava-liquid`) | Kava | Liquid Staking | $0.93M | unaudited |
| 103 | **Cube** (`cube`) | Solana | Dexs | $0.10M | unaudited |
| 104 | **DaVinciGraph** (`davincigraph`) | Hedera | Token Locker | $1.85M | unaudited |
| 105 | **Atmos DEX** (`atmos-dex`) | Supra | Dexs | $0.19M | unaudited |
| 106 | **Neutral Trade** (`neutral-trade`) | Solana | Onchain Capital Allocator | $13.27M | unaudited; churn:1; orc:Pyth |
| 107 | **Ambit Finance** (`ambit-finance`) | Binance | Lending | $0.07M | unaudited; orc:RedStone |
| 108 | **Swirl** (`swirl`) | IOTA | Liquid Staking | $2.90M |  |
| 109 | **PiggyBank** (`piggybank`) | Solana | Yield | $1.56M |  |
| 110 | **UXD** (`uxd`) | Solana | Partially Algorithmic Stablecoin | $0.30M |  |
| 111 | **Alt Fun** (`alt-fun`) | Hyperliquid L1 | Launchpad | $0.07M | unaudited |
| 112 | **Ostable** (`ostable`) | Obyte | Algo-Stables | $0.33M | unaudited |
| 113 | **Solayer Restaking** (`solayer-restaking`) | Solana | Restaking | $11.23M | unaudited |
| 114 | **OneSwap** (`oneswap`) | CSC,Ethereum | Dexs | $0.24M |  |
| 115 | **3Jane Options** (`3jane-options`) | Ethereum | Options Vault | $0.13M | fork:Ribbon; orc:Chainlink |
| 116 | **Pika V4** (`pika-v4`) | Optimism | Derivatives | $0.09M | unaudited; orc:Pyth |
| 117 | **Hatom Lending** (`hatom-lending`) | Elrond | Lending | $6.43M |  |
| 118 | **ATOMA** (`atoma`) | Arbitrum | Basis Trading | $0.32M | unaudited |
| 119 | **Katana Perps** (`katana-perps`) | Katana | Derivatives | $2.18M | unaudited |
| 120 | **Anoncoin** (`anoncoin`) | Solana | Launchpad | $0.12M | unaudited |
| 121 | **Magma Staking** (`magma-staking`) | Monad | Liquid Staking | $1.31M | unaudited |
| 122 | **Rhino.fi** (`rhino-fi`) | Polygon,Arbitrum | Bridge | $1.24M |  |
| 123 | **Increment Liquid Staking** (`increment-liquid-staking`) | Flow | Liquid Staking | $0.60M |  |
| 124 | **RISEx** (`risex`) | RISE | Derivatives | $17.32M | unaudited; orc:Stork |
| 125 | **Deriverse** (`deriverse`) | Solana | Dexs | $0.15M |  |
| 126 | **Alpha Arcade** (`alpha-arcade`) | Algorand | Prediction Market | $0.22M | unaudited |
| 127 | **Nami Index** (`nami-index`) | Thorchain | Indexes | $0.06M |  |
| 128 | **Gala Swap** (`gala-swap`) | Gala | Dexs | $3.97M | unaudited |
| 129 | **StarGate** (`stargate`) | VeChain | Farm | $5.74M | unaudited |
| 130 | **hemiBTC** (`hemibtc`) | Bitcoin | Bridge | $0.56M | unaudited |
| 131 | **Supralend** (`supralend`) | Supra | Lending | $0.05M | unaudited |
| 132 | **Bluefin Pro** (`bluefin-pro`) | Sui | Derivatives | $1.92M | orc:Pyth |
| 133 | **Particle LAMM** (`particle-lamm`) | Blast | Derivatives | $0.14M |  |
| 134 | **N1 Exchange Bridge** (`n1-exchange-bridge`) | Solana | Bridge | $1.76M | unaudited |
| 135 | **Hubble** (`hubble`) | Solana | CDP | $1.51M | orc:Pyth |
| 136 | **STONEUSD** (`stoneusd`) | Ethereum,Binance | CeDeFi | $2.02M |  |
| 137 | **Shido Dex V2** (`shido-dex-v2`) | Shido | Dexs | $0.22M |  |
| 138 | **Hydro Lending** (`hydro-lending`) | Injective | Lending | $4.73M | unaudited |
| 139 | **Theo Straddle Vaults** (`theo-straddle-vaults`) | Ethereum,Linea | Basis Trading | $1.12M |  |
| 140 | **NOXA Fun** (`noxa-fun`) | Robinhood Chain,Monad | Launchpad | $5.75M | unaudited |
| 141 | **Bonk Staked SOL** (`bonk-staked-sol`) | Solana | Liquid Staking | $10.53M | unaudited |
| 142 | **Ostium** (`ostium`) | Arbitrum | Derivatives | $16.39M | orc:Stork,Chainlink |
| 143 | **Quarry** (`quarry`) | Solana | Yield | $6.16M | unaudited; churn:1 |
| 144 | **B.Protocol** (`b-protocol`) | Ethereum,Arbitrum | Liquidations | $1.79M | orc:Chainlink |
| 145 | **Layer2 Finance** (`layer2-finance`) | Ethereum | Yield | $0.21M |  |
| 146 | **Sophon Bridge** (`sophon-bridge`) | Ethereum | Canonical Bridge | $12.18M | unaudited |
| 147 | **TONCO** (`tonco`) | TON | Dexs | $0.31M |  |
| 148 | **Bidask** (`bidask`) | TON | Dexs | $0.10M | unaudited |
| 149 | **Apex Omni** (`apex-omni`) | Ethereum,Arbitrum | Derivatives | $30.75M | unaudited; orc:Stork |
| 150 | **Surf Liquid** (`surf-liquid`) | Base,Ethereum | Yield | $0.22M | unaudited; churn:2 |
| 151 | **Colony** (`colony`) | Avalanche | Yield | $0.16M | churn:4 |
| 152 | **bitCow** (`bitcow`) | Bitlayer | Dexs | $0.18M | unaudited |
| 153 | **Joe V2.2** (`joe-v2-2`) | Avalanche,Arbitrum | Dexs | $2.37M |  |
| 154 | **Opus** (`opus`) | Starknet | CDP | $0.34M | orc:Pragma |
| 155 | **Aevo Perps** (`aevo-perps`) | Ethereum,Arbitrum | Derivatives | $15.27M | orc:Pyth |
| 156 | **Gardens** (`gardens`) | xDai,Celo | Governance Incentives | $0.07M | unaudited |
| 157 | **World Markets Spot** (`world-markets-spot`) | MegaETH | Dexs | $3.12M | unaudited |
| 158 | **Usual EUR0** (`usual-eur0`) | Ethereum | RWA | $0.24M | unaudited |
| 159 | **KoffeeSwap** (`koffeeswap`) | Kucoin | Dexs | $0.23M | unaudited |
| 160 | **Sherpa** (`sherpa`) | Ethereum,Base | Onchain Capital Allocator | $0.48M |  |
| 161 | **Tenderize V2** (`tenderize-v2`) | Ethereum,Arbitrum | Liquid Staking | $0.32M |  |
| 162 | **Templar Protocol** (`templar-protocol`) | Stellar,Ethereum | Lending | $27.51M | unaudited; orc:Pyth |
| 163 | **Kogefarm** (`kogefarm`) | Polygon,Fantom | Yield | $0.16M |  |
| 164 | **Boson Protocol** (`boson-protocol`) | Polygon,Ethereum | RWA | $0.23M |  |
| 165 | **Minswap DEX** (`minswap-dex`) | Cardano | Dexs | $14.25M | churn:3 |
| 166 | **Ultraswap** (`ultraswap`) | Algorand | Lending | $0.13M | unaudited |
| 167 | **Textile FX** (`textile-fx`) | Binance,Ethereum | Dexs | $0.53M | unaudited |
| 168 | **GuacSwap** (`guacswap`) | Solana | Dexs | $0.07M | unaudited |
| 169 | **Swapscanner LSD** (`swapscanner-lsd`) | Klaytn | Liquid Staking | $1.97M |  |
| 170 | **Stakingverse** (`stakingverse`) | Ethereum,LUKSO | Liquid Staking | $4.82M | churn:1 |
| 171 | **FlatQube** (`flatqube`) | Everscale | Dexs | $0.11M |  |
| 172 | **Weft V2** (`weft-v2`) | Radix | Lending | $0.32M | unaudited |
| 173 | **Rigoblock** (`rigoblock`) | Arbitrum,Ethereum | Onchain Capital Allocator | $0.05M | unaudited; orc:BackGeoOracle |
| 174 | **BitU Protocol** (`bitu-protocol`) | Binance | CDP | $19.55M | orc:Chainlink |
| 175 | **stCELO** (`stcelo`) | Celo | Liquid Staking | $1.48M |  |
| 176 | **LeverUp** (`leverup`) | Monad | Derivatives | $2.89M | orc:Pyth |
| 177 | **Verus Market** (`verus-market`) | Verus | Dexs | $2.95M | unaudited |
| 178 | **Myriad Markets** (`myriad-markets`) | Abstract,Binance | Prediction Market | $0.28M | unaudited |
| 179 | **Parasail** (`parasail`) | Filecoin,Arbitrum | Restaking | $1.19M |  |
| 180 | **SOFA.org** (`sofa-org`) | Ethereum,Arbitrum | Options | $0.87M | orc:Chainlink |

---

**180 protocols**, seed `770077`, non-overlapping with round 1 (`RANDOM_AUDIT_BATCH.md`) and all prior
pushes. Coverage list, not a ranking. Roughly ~700 eligible names still remain in the pool for future draws.
