# Unwatched audit batch — round 2 — 203 more, low/no-revenue, none on your blocklist

> **Same corrected meaning of "unwatched":** no one is paid to watch or defend the money. The
> deprecated / dead-site / TVL-decay tiers were fully used up by the previous round and your blocklist,
> so this round is built on the **revenue** signal you named directly — a protocol earning little or
> nothing has no budget for monitoring, incident response, or a re-audit after each upgrade, while real
> money still sits in its contracts. Audited-or-not plays no part.

**Two tiers (labelled in the last column):**
- **Tier A — confirmed low revenue** (63): DefiLlama tracks their fees and 30-day protocol revenue is
  under **$25k/mo** against real TVL. Strongest remaining unwatched signal.
- **Tier B — no revenue tracked** (140): real TVL but DefiLlama carries no fee/revenue line at all —
  off the fee radar, which for a funded contract is itself a low-attention signal.

**Structural filters kept:** real money `$50k ≤ TVL ≤ $100M`; **not a direct fork of a major protocol**;
not CEX / not an L1 chain; not rugged; **not on your blocklist** and **not previously delivered** (checked
against the 888-name list you gave plus the 1,511-name exclusion set — union 1,630 — with a hard zero-leak
assertion). Order random (`seed 20260902`).

**Cheap first pass per row:** unwatched + upgradeable is the worst pairing — pull the deployment, check
if it's a proxy and how stale its admin / last upgrade are; forgotten mint authority and live approvals on
low-revenue, low-attention contracts are the recurring way this money leaves.

Composition — categories: Dexs 40, Liquid Staking 25, Yield 19, Lending 19, Derivatives 13, Risk Curators 8, RWA 8, Yield Aggregator 7, CDP 6, Canonical Bridge 6. Chains: Ethereum 38, Solana 18, Base 10, Sui 9, Polygon 8, Binance 8, Hyperliquid L1 7, Arbitrum 6. TVL/revenue at head (DefiLlama, 2026-08-29).

| # | Protocol | Chain(s) | Category | TVL | Unwatched signal | Tier |
|--:|---|---|---|--:|---|:--:|
| 1 | **Bucket CDP** (`bucket-cdp`) | Sui | CDP | $11.92M | no fee/revenue tracked; no-mcap | B |
| 2 | **Avalon Superearn** (`avalon-superearn`) | Ethereum | Yield | $65.86M | no fee/revenue tracked; no-mcap | B |
| 3 | **KongSwap** (`kongswap`) | ICP | Dexs | $2.38M | no fee/revenue tracked; no-mcap | B |
| 4 | **infiniFi** (`infinifi`) | Ethereum | Yield | $47.02M | rev≈$22.3k/mo; no-mcap | A |
| 5 | **Stakehouse** (`stakehouse`) | Ethereum | Liquid Staking | $0.10M | no fee/revenue tracked; no-mcap | B |
| 6 | **Puzzle Lend** (`puzzle-lend`) | Waves | Lending | $0.23M | no fee/revenue tracked; no-mcap | B |
| 7 | **DiversiFi** (`diversifi`) | Solana | Indexes | $0.21M | no fee/revenue tracked; no-mcap | B |
| 8 | **Mezo Earn** (`mezo-earn`) | Mezo | Governance Incentives | $63.38M | no fee/revenue tracked; no-mcap | B |
| 9 | **Polygon zkEVM Bridge** (`polygon-zkevm-bridge`) | Ethereum | Canonical Bridge | $62.43M | no fee/revenue tracked; no-mcap | B |
| 10 | **Sushi Aptos** (`sushi-aptos`) | Aptos | Dexs | $0.32M | no fee/revenue tracked; no-mcap | B |
| 11 | **Monday Trade Perps** (`monday-trade-perps`) | Monad | Derivatives | $0.58M | no fee/revenue tracked; no-mcap; fork:SynFutures V3 | B |
| 12 | **Web3.world** (`web3-world`) | Venom | Dexs | $0.57M | no fee/revenue tracked; no-mcap | B |
| 13 | **Jarvis Network** (`jarvis-network`) | Polygon,Binance | Derivatives | $0.26M | no fee/revenue tracked | B |
| 14 | **SquadSwap Thanos** (`squadswap-thanos`) | Binance,Base | Dexs | $0.47M | rev≈$7.9k/mo; no-mcap | A |
| 15 | **Hyperbeat Earn** (`hyperbeat-earn`) | Hyperliquid L1 | Yield Aggregator | $26.41M | rev≈$13.4k/mo; no-mcap | A |
| 16 | **DeltaTrade** (`deltatrade`) | Near,Solana | Dexs | $0.06M | no fee/revenue tracked; no-mcap | B |
| 17 | **OpenGDP Shared Security** (`opengdp-shared-security`) | Ethereum,Arbitrum | Restaking | $8.12M | no fee/revenue tracked; no-mcap | B |
| 18 | **Algebra DEX** (`algebra-dex`) | Polygon | Dexs | $0.07M | no fee/revenue tracked; no-mcap | B |
| 19 | **duckpools** (`duckpools`) | Ergo | Lending | $0.07M | no fee/revenue tracked; no-mcap | B |
| 20 | **Baryon Network** (`baryon-network`) | Binance,Ancient8 | Dexs | $0.05M | no fee/revenue tracked; no-mcap | B |
| 21 | **Liquidity House** (`liquidity-house`) | Etherlink | Prediction Market | $1.17M | no fee/revenue tracked; no-mcap | B |
| 22 | **Re7 Labs** (`re7-labs`) | World Chain,Avalanche | Risk Curators | $83.18M | rev≈$8.7k/mo; no-mcap | A |
| 23 | **Sovryn Zero** (`sovryn-zero`) | RSK | CDP | $19.84M | no fee/revenue tracked; no-mcap | B |
| 24 | **Strata Markets** (`strata-markets`) | Ethereum | Yield | $74.04M | rev≈$14.3k/mo; no-mcap | A |
| 25 | **Mezo Vaults** (`mezo-vaults`) | Mezo | Yield Aggregator | $7.54M | no fee/revenue tracked; no-mcap | B |
| 26 | **Citrus** (`citrus`) | Solana | NFT Lending | $0.08M | no fee/revenue tracked; no-mcap | B |
| 27 | **Dswap** (`dswap`) | ENI | Dexs | $1.11M | rev≈$4.5k/mo; no-mcap | A |
| 28 | **Mooncake** (`mooncake`) | Solana | Derivatives | $0.09M | no fee/revenue tracked; no-mcap | B |
| 29 | **Avant avETH** (`avant-aveth`) | Ethereum | Onchain Capital Allocator | $30.89M | rev≈$9.8k/mo; no-mcap | A |
| 30 | **Frankencoin** (`frankencoin`) | Ethereum | CDP | $82.40M | rev≈$7.8k/mo | A |
| 31 | **Neptune LSD** (`neptune-lsd`) | Oasys | Liquid Staking | $0.06M | no fee/revenue tracked; no-mcap | B |
| 32 | **SX Bet** (`sx-bet`) | SX Rollup | Prediction Market | $0.64M | rev≈$4.0k/mo; no-mcap | A |
| 33 | **KTON** (`kton`) | TON | Liquid Staking | $2.35M | no fee/revenue tracked; no-mcap | B |
| 34 | **Valiant Trade Spot** (`valiant-trade-spot`) | Fogo | Dexs | $0.27M | no fee/revenue tracked; no-mcap | B |
| 35 | **Scallop Lend** (`scallop-lend`) | Sui | Lending | $10.19M | rev≈$24.3k/mo; no-mcap | A |
| 36 | **JagPool Staked SOL** (`jagpool-staked-sol`) | Solana | Liquid Staking | $80.09M | rev≈$11.5k/mo; no-mcap | A |
| 37 | **Tempo Stablecoin Dex** (`tempo-stablecoin-dex`) | Tempo | Dexs | $11.43M | no fee/revenue tracked; no-mcap | B |
| 38 | **Locus Finance** (`locus-finance`) | Arbitrum,Ethereum | Yield | $0.05M | no fee/revenue tracked; no-mcap | B |
| 39 | **Zama** (`zama`) | Ethereum | Privacy | $59.37M | no fee/revenue tracked | B |
| 40 | **PRED** (`pred`) | Base | Prediction Market | $0.12M | no fee/revenue tracked; no-mcap | B |
| 41 | **Vesu** (`vesu`) | Starknet | Lending | $13.58M | no fee/revenue tracked; no-mcap | B |
| 42 | **INIT Capital** (`init-capital`) | Mantle,Blast | Lending | $2.08M | no fee/revenue tracked; no-mcap | B |
| 43 | **Turbo Loop** (`turbo-loop`) | Binance | Yield | $2.06M | no fee/revenue tracked; no-mcap | B |
| 44 | **Bifrost Liquid Staking** (`bifrost-liquid-staking`) | Bifrost,Ethereum | Liquid Staking | $11.41M | rev≈$7.4k/mo; no-mcap | A |
| 45 | **One Dex** (`one-dex`) | Elrond | Dexs | $0.19M | no fee/revenue tracked | B |
| 46 | **Toucan Protocol** (`toucan-protocol`) | Polygon,Celo | RWA | $0.54M | no fee/revenue tracked; no-mcap | B |
| 47 | **Compound Blue** (`compound-blue`) | Polygon | Lending | $0.55M | no fee/revenue tracked; no-mcap | B |
| 48 | **Kinetiq Earn** (`kinetiq-earn`) | Hyperliquid L1 | Yield Aggregator | $58.92M | rev≈$20.2k/mo; no-mcap | A |
| 49 | **UTONIC** (`utonic`) | TON | Liquid Staking | $4.15M | no fee/revenue tracked; no-mcap | B |
| 50 | **CSWAP DEX** (`cswap-dex`) | Cardano | Dexs | $0.44M | no fee/revenue tracked; no-mcap | B |
| 51 | **BladeSwap AMM** (`bladeswap-amm`) | Blast | Dexs | $0.21M | no fee/revenue tracked; no-mcap; fork:Velocore V2 | B |
| 52 | **Travessia Credit** (`travessia-credit`) | Ethereum,Monad | RWA Lending | $0.63M | no fee/revenue tracked; no-mcap | B |
| 53 | **Lorenzo sUSD1+** (`lorenzo-susd1`) | Binance,Ethereum | Yield | $80.45M | rev≈$8.9k/mo; no-mcap | A |
| 54 | **Sensi** (`sensi`) | Binance | Yield Aggregator | $0.10M | no fee/revenue tracked; no-mcap | B |
| 55 | **Augur** (`augur`) | Ethereum | Prediction Market | $1.93M | no fee/revenue tracked; no-mcap | B |
| 56 | **Adrastea Validator** (`adrastea-validator`) | Solana | Staking Pool | $28.09M | no fee/revenue tracked; no-mcap | B |
| 57 | **SpinUp Liquid Staking** (`spinup-liquid-staking`) | Hyperliquid L1 | Liquid Staking | $0.26M | no fee/revenue tracked; no-mcap | B |
| 58 | **Atomic Green** (`atomic-green`) | Arbitrum | Derivatives | $0.08M | no fee/revenue tracked; no-mcap | B |
| 59 | **AlphaFi Agg** (`alphafi-agg`) | Sui | Yield Aggregator | $16.94M | no fee/revenue tracked; no-mcap | B |
| 60 | **Kea Credit** (`kea-credit`) | Hedera | RWA | $2.98M | no fee/revenue tracked; no-mcap | B |
| 61 | **YieldSeeker** (`yieldseeker`) | Base | Yield Aggregator | $1.16M | no fee/revenue tracked; no-mcap | B |
| 62 | **ZEROBASE CeDeFi** (`zerobase-cedefi`) | Binance,Ethereum | Basis Trading | $62.94M | no fee/revenue tracked | B |
| 63 | **Sanctum Reserve** (`sanctum-reserve`) | Solana | Yield | $65.26M | rev≈$6.8k/mo; no-mcap | A |
| 64 | **Cropper AMM** (`cropper-amm`) | Solana | Dexs | $0.12M | no fee/revenue tracked; no-mcap | B |
| 65 | **Treehouse Protocol** (`treehouse-protocol`) | Ethereum,Avalanche | DOR | $69.70M | rev≈$4.2k/mo | A |
| 66 | **Unitas USDu** (`unitas-usdu`) | Binance,Solana | Basis Trading | $47.70M | no fee/revenue tracked; no-mcap | B |
| 67 | **Treasure Bridge** (`treasure-bridge`) | Ethereum | Canonical Bridge | $0.08M | no fee/revenue tracked; no-mcap | B |
| 68 | **Meshswap** (`meshswap`) | Polygon | Dexs | $0.31M | no fee/revenue tracked; no-mcap | B |
| 69 | **Redstone** (`redstone`) | Ethereum | Canonical Bridge | $0.07M | no fee/revenue tracked; no-mcap | B |
| 70 | **INERTIA** (`inertia`) | Inertia | Lending | $0.17M | no fee/revenue tracked; no-mcap | B |
| 71 | **Scorch** (`scorch`) | — | Dexs | $2.45M | no fee/revenue tracked; no-mcap | B |
| 72 | **ForgeYields** (`forgeyields`) | Starknet,Ethereum | Onchain Capital Allocator | $1.33M | no fee/revenue tracked; no-mcap | B |
| 73 | **NewrlRWA** (`newrlrwa`) | Aptos | RWA | $0.06M | no fee/revenue tracked; no-mcap | B |
| 74 | **Helius Staked SOL** (`helius-staked-sol`) | Solana | Liquid Staking | $96.96M | rev≈$7.9k/mo; no-mcap | A |
| 75 | **Maya Protocol** (`maya-protocol`) | Zcash,Bitcoin | Cross Chain Bridge | $4.70M | rev≈$21.4k/mo | A |
| 76 | **Citadel Vaults** (`citadel-vaults`) | Supra | Yield | $0.13M | no fee/revenue tracked; no-mcap | B |
| 77 | **The LifeDAO** (`the-lifedao`) | Arbitrum | CeDeFi | $0.08M | no fee/revenue tracked; no-mcap | B |
| 78 | **9mm V3** (`9mm-v3`) | Pulse,Base | Dexs | $3.62M | rev≈$15.5k/mo; no-mcap | A |
| 79 | **bemo V1** (`bemo-v1`) | TON | Liquid Staking | $1.86M | no fee/revenue tracked; no-mcap | B |
| 80 | **B.Protocol Curator** (`b-protocol-curator`) | Ethereum,Base | Risk Curators | $0.13M | rev≈$5.6k/mo; no-mcap | A |
| 81 | **SyncSwap** (`syncswap`) | zkSync Era,Linea | Dexs | $8.93M | rev≈$3.6k/mo; no-mcap | A |
| 82 | **Ribbon** (`ribbon`) | Ethereum,Solana | Options Vault | $4.25M | no fee/revenue tracked; no-mcap | B |
| 83 | **STKESOL by SOL Strategies** (`stkesol-by-sol-strategies`) | Solana | Liquid Staking | $64.28M | rev≈$10.8k/mo; no-mcap | A |
| 84 | **Ethos Markets** (`ethos-markets`) | Base | SoFi | $0.22M | no fee/revenue tracked; no-mcap | B |
| 85 | **Swaylend** (`swaylend`) | Fuel | Lending | $0.83M | no fee/revenue tracked; no-mcap | B |
| 86 | **MagicSea LB** (`magicsea-lb`) | IOTA EVM | Dexs | $0.36M | rev≈$3.7k/mo; no-mcap | A |
| 87 | **Basilisk** (`basilisk`) | zkSync Era | Lending | $0.11M | no fee/revenue tracked; no-mcap | B |
| 88 | **Asseto AoABT** (`asseto-aoabt`) | Avalanche,HashKey Chain | RWA | $23.67M | no fee/revenue tracked; no-mcap | B |
| 89 | **Abyss** (`abyss`) | Sui | Yield | $0.29M | no fee/revenue tracked; no-mcap | B |
| 90 | **Lombard Vaults** (`lombard-vaults`) | Ethereum,Base | Onchain Capital Allocator | $70.97M | rev≈$22.3k/mo; no-mcap | A |
| 91 | **Sirius** (`sirius`) | Tezos | Dexs | $1.86M | no fee/revenue tracked; no-mcap | B |
| 92 | **Ethereal DEX** (`ethereal-dex`) | Ethereal | Derivatives | $3.36M | rev≈$7.1k/mo; no-mcap | A |
| 93 | **token.select** (`token-select`) | — | Launchpad | $0.34M | rev≈$23.7k/mo; no-mcap | A |
| 94 | **Echelon Market** (`echelon-market`) | Aptos,Echelon Chain | Lending | $8.05M | rev≈$24.8k/mo | A |
| 95 | **Looped Hype** (`looped-hype`) | Hyperliquid L1 | Yield | $9.58M | rev≈$4.7k/mo | A |
| 96 | **MetalX Swap** (`metalx-swap`) | Proton | Dexs | $9.81M | no fee/revenue tracked; no-mcap | B |
| 97 | **Storm Trade** (`storm-trade`) | TON | Derivatives | $4.75M | rev≈$6.8k/mo | A |
| 98 | **BMX Freestyle** (`bmx-freestyle`) | Base,Mode | Derivatives | $1.30M | no fee/revenue tracked; no-mcap | B |
| 99 | **QX** (`qx`) | Qubic | Dexs | $0.05M | no fee/revenue tracked; no-mcap | B |
| 100 | **Tensor** (`tensor`) | Solana | NFT Marketplace | $0.32M | no fee/revenue tracked | B |
| 101 | **Enzyme Finance** (`enzyme-finance`) | Ethereum,Polygon | Indexes | $90.80M | rev≈$8.2k/mo | A |
| 102 | **Persistence DEX** (`persistence-dex`) | Persistence,Babylon Genesis | Dexs | $0.05M | no fee/revenue tracked; no-mcap | B |
| 103 | **Filet Finance** (`filet-finance`) | Filecoin,Binance | Liquid Staking | $0.98M | no fee/revenue tracked; no-mcap | B |
| 104 | **VenomStake** (`venomstake`) | Venom | Liquid Staking | $6.31M | no fee/revenue tracked; no-mcap | B |
| 105 | **Euphoria Finance** (`euphoria-finance`) | MegaETH | Derivatives | $0.15M | no fee/revenue tracked; no-mcap | B |
| 106 | **Pando Rings** (`pando-rings`) | Mixin | Lending | $6.08M | no fee/revenue tracked; no-mcap | B |
| 107 | **Full Sail** (`full-sail`) | Sui | Dexs | $0.23M | rev≈$19.9k/mo | A |
| 108 | **Meta Pool mpSOL** (`meta-pool-mpsol`) | Solana | Liquid Restaking | $0.12M | no fee/revenue tracked; no-mcap | B |
| 109 | **veDelegate** (`vedelegate`) | VeChain | Governance Incentives | $0.81M | no fee/revenue tracked; no-mcap | B |
| 110 | **ZilSwap** (`zilswap`) | Zilliqa | Dexs | $0.15M | no fee/revenue tracked; no-mcap | B |
| 111 | **Steroids** (`steroids`) | Ethereum | Yield | $0.26M | no fee/revenue tracked; no-mcap | B |
| 112 | **Metis Bridge** (`metis-bridge`) | Ethereum | Canonical Bridge | $25.58M | no fee/revenue tracked; no-mcap | B |
| 113 | **BlazeStake** (`blazestake`) | Solana | Liquid Staking | $95.85M | rev≈$18.4k/mo; no-mcap | A |
| 114 | **Puffer Stake** (`puffer-stake`) | Ethereum | Liquid Restaking | $59.20M | rev≈$5.2k/mo; no-mcap | A |
| 115 | **Stellar DeFi Hub** (`stellar-defi-hub`) | Stellar | Yield | $17.51M | no fee/revenue tracked; no-mcap | B |
| 116 | **Cassa** (`cassa`) | Ethereum | Risk Curators | $9.07M | no fee/revenue tracked; no-mcap | B |
| 117 | **Meld Gold** (`meld-gold`) | Algorand | RWA | $10.16M | no fee/revenue tracked; no-mcap | B |
| 118 | **Tessera V** (`tessera-v`) | — | Dexs | $13.34M | no fee/revenue tracked; no-mcap | B |
| 119 | **up v2** (`up-v2`) | Robinhood Chain | Dexs | $0.64M | rev≈$12.1k/mo; no-mcap | A |
| 120 | **Surf Lending** (`surf-lending`) | Cardano | Lending | $3.32M | no fee/revenue tracked | B |
| 121 | **Swell L2 Farm** (`swell-l2-farm`) | Ethereum | Farm | $78.26M | no fee/revenue tracked; no-mcap | B |
| 122 | **Blast Bridge** (`blast-bridge`) | Ethereum | Canonical Bridge | $60.57M | no fee/revenue tracked; no-mcap | B |
| 123 | **Moor** (`moor`) | Fuel | CDP | $0.38M | no fee/revenue tracked; no-mcap | B |
| 124 | **DipCoin Perps** (`dipcoin-perps`) | Sui | Derivatives | $1.91M | rev≈$16.3k/mo; no-mcap | A |
| 125 | **CookieChain Hyperlane Bridge** (`cookiechain-hyperlane-bridge`) | Solana,CookieChain | Bridge | $0.09M | no fee/revenue tracked | B |
| 126 | **XORA** (`xora`) | Ripple | CeDeFi | $0.33M | no fee/revenue tracked; no-mcap | B |
| 127 | **ICDex** (`icdex`) | ICP | Dexs | $0.56M | no fee/revenue tracked; no-mcap | B |
| 128 | **Republic Note** (`republic-note`) | Avalanche | RWA | $13.42M | no fee/revenue tracked; no-mcap | B |
| 129 | **Orai Quant Terminal** (`orai-quant-terminal`) | Arbitrum | Onchain Capital Allocator | $0.75M | rev≈$15.7k/mo; no-mcap | A |
| 130 | **Hakutora** (`hakutora`) | Ethereum | Risk Curators | $24.21M | rev≈$9.8k/mo; no-mcap | A |
| 131 | **Api3** (`api3`) | Ethereum | Risk Curators | $17.71M | rev≈$5.5k/mo | A |
| 132 | **GIGA V3** (`giga-v3`) | Robinhood Chain | Dexs | $0.63M | rev≈$17.8k/mo; no-mcap | A |
| 133 | **Aborean CL** (`aborean-cl`) | Abstract | Dexs | $3.14M | rev≈$23.0k/mo; no-mcap | A |
| 134 | **Gate SOL** (`gate-sol`) | Solana | Liquid Staking | $69.09M | rev≈$9.5k/mo; no-mcap | A |
| 135 | **world** (`world`) | Solana | Prediction Market | $0.09M | no fee/revenue tracked; no-mcap | B |
| 136 | **Hatom Liquid Staking** (`hatom-liquid-staking`) | Elrond | Liquid Staking | $3.23M | no fee/revenue tracked; no-mcap | B |
| 137 | **Reya Perps** (`reya-perps`) | Reya Network | Derivatives | $9.83M | rev≈$9.2k/mo; no-mcap | A |
| 138 | **Lien** (`lien`) | Ethereum | Options | $0.21M | no fee/revenue tracked; no-mcap | B |
| 139 | **Volo Vault** (`volo-vault`) | Sui | Risk Curators | $8.62M | no fee/revenue tracked; no-mcap | B |
| 140 | **Scale** (`scale`) | Base | Dexs | $0.32M | rev≈$3.8k/mo; no-mcap | A |
| 141 | **Index Coop** (`index-coop`) | Ethereum,Arbitrum | Indexes | $13.84M | rev≈$18.0k/mo | A |
| 142 | **NemoSwap** (`nemoswap`) | RENEC | Dexs | $0.06M | no fee/revenue tracked; no-mcap; fork:Orca DEX | B |
| 143 | **International Stable Currency** (`international-stable-currency`) | Solana | RWA | $2.46M | no fee/revenue tracked; no-mcap | B |
| 144 | **Allstake** (`allstake`) | Near,Solana | Restaking | $0.12M | no fee/revenue tracked; no-mcap | B |
| 145 | **Brasa Finance** (`brasa-finance`) | Fogo | Liquid Staking | $0.70M | no fee/revenue tracked; no-mcap | B |
| 146 | **Vault Bridge** (`vault-bridge`) | Ethereum | Risk Curators | $55.97M | rev≈$3.7k/mo; no-mcap | A |
| 147 | **OKX xBTC** (`okx-xbtc`) | Bitcoin | Bridge | $74.45M | no fee/revenue tracked; no-mcap | B |
| 148 | **Parallel Protocol V2** (`parallel-protocol-v2`) | Ethereum,Polygon | CDP | $0.63M | no fee/revenue tracked; no-mcap | B |
| 149 | **Equilibrium Lending** (`equilibrium-lending`) | Equilibrium | Lending | $1.13M | no fee/revenue tracked; no-mcap | B |
| 150 | **FlowX V2** (`flowx-v2`) | Sui | Dexs | $0.21M | no fee/revenue tracked; no-mcap | B |
| 151 | **Gate Fun** (`gate-fun`) | GateLayer | Launchpad | $0.06M | no fee/revenue tracked; no-mcap | B |
| 152 | **Service Nervous Systems** (`service-nervous-systems`) | ICP | Governance Incentives | $0.39M | no fee/revenue tracked; no-mcap | B |
| 153 | **Swell Liquid Staking** (`swell-liquid-staking`) | Ethereum | Liquid Staking | $31.78M | rev≈$3.4k/mo; no-mcap | A |
| 154 | **Puff Penthouse** (`puff-penthouse`) | Mantle | Farm | $0.07M | no fee/revenue tracked | B |
| 155 | **Prime Protocol** (`prime-protocol`) | Moonbeam,Arbitrum | Lending | $0.35M | no fee/revenue tracked; no-mcap | B |
| 156 | **Definix** (`definix`) | Binance,Klaytn | Dexs | $0.43M | no fee/revenue tracked; no-mcap | B |
| 157 | **Zest V2** (`zest-v2`) | Stacks | Lending | $72.39M | rev≈$4.2k/mo; no-mcap | A |
| 158 | **Kinetiq kmHYPE** (`kinetiq-kmhype`) | Hyperliquid L1 | Liquid Staking | $49.02M | no fee/revenue tracked; no-mcap | B |
| 159 | **Nad.fun V2** (`nad-fun-v2`) | Monad | Launchpad | $0.30M | no fee/revenue tracked; no-mcap | B |
| 160 | **USDCx** (`usdcx`) | Ethereum | Stablecoin Wrapper | $62.59M | no fee/revenue tracked; no-mcap | B |
| 161 | **Stratis mSTRAX** (`stratis-mstrax`) | Stratis | Liquid Staking | $1.65M | no fee/revenue tracked; no-mcap | B |
| 162 | **Meta Pool Near** (`meta-pool-near`) | Near,Aurora | Liquid Staking | $48.13M | no fee/revenue tracked; no-mcap | B |
| 163 | **CallPut** (`callput`) | Base | Options | $0.11M | rev≈$11.0k/mo; no-mcap | A |
| 164 | **FWB** (`fwb`) | Polygon,Binance | Yield | $0.05M | no fee/revenue tracked; no-mcap | B |
| 165 | **gALGO Liquid Governance** (`galgo-liquid-governance`) | Algorand | Liquid Staking | $0.41M | no fee/revenue tracked; no-mcap | B |
| 166 | **Llama Airforce** (`llama-airforce`) | Ethereum | Yield | $1.68M | no fee/revenue tracked; no-mcap | B |
| 167 | **Liquid Driver** (`liquid-driver`) | Fantom,Binance | Yield | $0.18M | no fee/revenue tracked; no-mcap | B |
| 168 | **Ethos Network** (`ethos-network`) | Base | SoFi | $1.34M | no fee/revenue tracked; no-mcap | B |
| 169 | **Hamilton Lane Senior Credit Opportunities Securitize Fund** (`hamilton-lane-senior-credit-opportunities-securitize-fund`) | Polygon,Ethereum | RWA | $4.30M | rev≈$7.1k/mo | A |
| 170 | **Kvants** (`kvants`) | Base,Solana | Onchain Capital Allocator | $0.09M | no fee/revenue tracked; no-mcap | B |
| 171 | **WOOFi Swap** (`woofi-swap`) | Arbitrum,Optimism | Dexs | $2.38M | rev≈$11.1k/mo; no-mcap | A |
| 172 | **Bifrost Liquid Crowdloan** (`bifrost-liquid-crowdloan`) | Bifrost | Liquid Staking | $0.33M | no fee/revenue tracked; no-mcap | B |
| 173 | **AlphaQ** (`alphaq`) | — | Dexs | $1.05M | rev≈$13.8k/mo; no-mcap | A |
| 174 | **WanSwap Dex** (`wanswap-dex`) | Wanchain | Dexs | $1.00M | no fee/revenue tracked | B |
| 175 | **AFX LP** (`afx-lp`) | AFX L1 | Derivatives | $12.23M | no fee/revenue tracked; no-mcap | B |
| 176 | **ENIBridge** (`enibridge`) | Ethereum | Canonical Bridge | $0.07M | no fee/revenue tracked; no-mcap | B |
| 177 | **Rujira Money Market** (`rujira-money-market`) | Thorchain | Lending | $1.08M | no fee/revenue tracked; no-mcap | B |
| 178 | **USX.Capital** (`usx-capital`) | Scroll | Stablecoin Wrapper | $0.76M | no fee/revenue tracked; no-mcap | B |
| 179 | **Tydro** (`tydro`) | Ink | Lending | $87.02M | rev≈$14.4k/mo; no-mcap | A |
| 180 | **Astros Perp** (`astros-perp`) | Sui | Derivatives | $0.29M | rev≈$12.4k/mo; no-mcap | A |
| 181 | **SoSoValue Basis** (`sosovalue-basis`) | Base | Basis Trading | $2.94M | rev≈$8.8k/mo; no-mcap | A |
| 182 | **Hydration DEX** (`hydration-dex`) | HydraDX | Dexs | $27.09M | rev≈$21.0k/mo | A |
| 183 | **Valdora Finance** (`valdora-finance`) | ZIGChain | Liquid Staking | $76.02M | rev≈$3.9k/mo; no-mcap | A |
| 184 | **StockRip** (`stockrip`) | Robinhood Chain | Gamified Mining | $0.17M | rev≈$21.6k/mo; no-mcap | A |
| 185 | **XO Market** (`xo-market`) | XO | Prediction Market | $0.13M | rev≈$3.1k/mo; no-mcap | A |
| 186 | **ElfomoFi** (`elfomofi`) | — | Dexs | $1.07M | rev≈$5.6k/mo; no-mcap | A |
| 187 | **Galaxy Curation** (`galaxy-curation`) | Ethereum,Base | Risk Curators | $69.52M | rev≈$3.2k/mo; no-mcap | A |
| 188 | **SHPRD** (`shprd`) | Arbitrum,Ethereum | Indexes | $0.40M | no fee/revenue tracked; no-mcap | B |
| 189 | **The Vault Unstake Pool** (`the-vault-unstake-pool`) | Solana | Yield | $0.49M | no fee/revenue tracked; no-mcap | B |
| 190 | **ShMonad** (`shmonad`) | Monad | Liquid Staking | $10.35M | rev≈$4.3k/mo; no-mcap | A |
| 191 | **Lavarage** (`lavarage`) | Solana | Derivatives | $0.67M | rev≈$8.3k/mo; no-mcap | A |
| 192 | **ARMSys** (`armsys`) | Base,Robinhood Chain | Yield | $0.05M | no fee/revenue tracked; no-mcap | B |
| 193 | **Bitget bgBTC** (`bitget-bgbtc`) | Bitcoin | Bridge | $87.52M | no fee/revenue tracked; no-mcap | B |
| 194 | **Sphere Finance** (`sphere-finance`) | Polygon | Yield | $6.20M | no fee/revenue tracked; no-mcap | B |
| 195 | **Hyperbeat Credit** (`hyperbeat-credit`) | Hyperliquid L1 | Collateral Management | $1.33M | no fee/revenue tracked; no-mcap | B |
| 196 | **Nimbora Yield** (`nimbora-yield`) | Starknet | Yield | $0.27M | no fee/revenue tracked; no-mcap | B |
| 197 | **Endurance Bridge** (`endurance-bridge`) | Endurance | Bridge | $8.03M | no fee/revenue tracked; no-mcap | B |
| 198 | **Swell BTC LRT** (`swell-btc-lrt`) | Ethereum | Yield Aggregator | $0.46M | no fee/revenue tracked; no-mcap | B |
| 199 | **Timeswap V2** (`timeswap-v2`) | Hyperliquid L1,Arbitrum | Lending | $0.33M | no fee/revenue tracked; no-mcap | B |
| 200 | **Jigsaw** (`jigsaw`) | Ethereum | CDP | $0.43M | no fee/revenue tracked; no-mcap | B |
| 201 | **GETH** (`geth`) | Ethereum | Liquid Staking | $18.83M | rev≈$6.0k/mo; no-mcap | A |
| 202 | **EVAA Protocol** (`evaa-protocol`) | TON | Lending | $9.45M | no fee/revenue tracked | B |
| 203 | **Dungeon DEX** (`dungeon-dex`) | Dungeon | Dexs | $0.08M | no fee/revenue tracked; no-mcap; fork:White Whale Dex | B |

---

**203 unwatched protocols** (Tier A 63 confirmed-low-revenue, Tier B 140 no-revenue-tracked), holding a combined $3,040M. Zero overlap with your blocklist or any prior push.
