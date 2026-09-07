# New discovery — 207 unwatched, bespoke, mid-size protocols to audit

> **This is the discovery, plain and simple** — a fresh, non-repeating set of live protocols to point
> audit compute at. It's the same search that surfaced earlier real work: **unwatched** (little/no
> protocol revenue, so no one is paid to watch the code), **bespoke** (not a fork of a major protocol),
> **mid-size** (`$50k ≤ TVL ≤ $100M`, real money but not a watched blue-chip), and **not delivered before**.
> Order is random; treat it as coverage, not a ranking.

**What changed from the last batches:** instead of a bare list, each *category* below carries the
concrete, high-yield things to check — distilled from the incident classes this project has seen
(spot-price mint valuation, same-asset swaps, thin-collateral oracles, mint-not-bound-to-burn bridges,
permissionless/replayable/aggregate signature authorization on pooled funds, forgotten strategy/keeper
authority). Read the **deployed** code for these on each row; the list tells you *where*, the guide
tells you *what*.

**General read (every row, before the category specifics):** enumerate the permissionless,
value-moving entrypoints; for any signature check, confirm it **binds the exact action** and carries
**replay protection** (nonce + deadline), and that **each counterparty/recipient is individually
authorized**, not just an aggregate signer; check who holds upgrade/admin authority and how stale it is.

**Filters:** alive, not rugged, not CEX/L1, not a major-protocol fork, low/no tracked revenue, real TVL,
and cleared against the full exclusion set + your blocklist (folded back in after this run). Random
seed `20260903`. TVL/revenue at head (DefiLlama).

## What to check, by category

- **Dexs** — same-asset / same-pool swap allowed? spot (slot0/reserve) used for mint or pricing without a TWAP? fee-on-transfer or rebasing token desyncs the cached reserve? router/callback does an arbitrary call?
- **Lending** — any thin-liquidity collateral priced by a single shallow feed (flash-manipulable)? liquidation & interest-index math at edges? borrow-cap / isolation bypass? permissionless market listing?
- **Bridge** — is each mint/credit bound to a *verified* source burn/lock (not just an attested message)? message replay / nonce; verifier/DVN/peer config mutability; permissionless receive/withdraw.
- **RWA** — mint/redeem authorization & whitelist bypass; off-chain value oracle trust and staleness; pause/admin fund-movement; transfer-agent role acquisition.
- **Canonical Bridge** — deposit/withdraw proof verification; message replay; who can set the remote/root; emergency-exit and pause authority.
- **Yield** — strategy/keeper authorization (permissionless harvest/compound?); first-deposit / donation share inflation; withdrawal accounting & reentrancy; reward-index init.
- **Basis Trading** — hedge/rebalance keeper authorization; funding/settlement math; oracle used for NAV; withdrawal queue accounting.
- **Yield Aggregator** — per-vault strategy authorization; old/retired strategy still approved on the vault; harvest reentrancy; share-price manipulation.
- **Staking Pool** — reward accounting & rate updates; withdrawal queue; slashing/exit authorization; permissionless claim.
- **Risk Curators** — allocation authorization; who can add markets/strategies; approvals & caps; role acquisition.
- **Onchain Capital Allocator** — allocation/rebalance authorization & role acquisition; approvals granted to strategies; permissionless move.
- **CDP** — collateral oracle depth vs manipulation cost; redemption/liquidation pricing; debt-ceiling & rate keepers; mint authorization.
- **Derivatives** — oracle/settlement manipulation; funding; order/quote signature replay & per-counterparty authorization; permissionless settle.
- **Liquid Staking** — exchange-rate read (spot vs smoothed) where used as collateral; reward/rate keeper authorization; withdrawal queue.
- **Prediction Market** — permissionless value-moving entrypoints; signature replay (nonce/deadline) & whether the signature binds the exact action; per-counterparty authorization; upgrade/admin authority.
- **Indexes** — rebalance authorization; component pricing; mint/redeem NAV; fee accounting.
- **Liquidity Manager** — permissionless value-moving entrypoints; signature replay (nonce/deadline) & whether the signature binds the exact action; per-counterparty authorization; upgrade/admin authority.
- **Anchor BTC** — permissionless value-moving entrypoints; signature replay (nonce/deadline) & whether the signature binds the exact action; per-counterparty authorization; upgrade/admin authority.
- **Farm** — reward/harvest authorization; migrator/strategy authority; first-deposit inflation; reentrancy.
- **Algo-Stables** — permissionless value-moving entrypoints; signature replay (nonce/deadline) & whether the signature binds the exact action; per-counterparty authorization; upgrade/admin authority.
- **AI Agents** — permissionless value-moving entrypoints; signature replay (nonce/deadline) & whether the signature binds the exact action; per-counterparty authorization; upgrade/admin authority.
- **Launchpad** — permissionless value-moving entrypoints; signature replay (nonce/deadline) & whether the signature binds the exact action; per-counterparty authorization; upgrade/admin authority.
- **Cross Chain Bridge** — permissionless value-moving entrypoints; signature replay (nonce/deadline) & whether the signature binds the exact action; per-counterparty authorization; upgrade/admin authority.
- **RWA Lending** — permissionless value-moving entrypoints; signature replay (nonce/deadline) & whether the signature binds the exact action; per-counterparty authorization; upgrade/admin authority.
- **Token Locker** — permissionless value-moving entrypoints; signature replay (nonce/deadline) & whether the signature binds the exact action; per-counterparty authorization; upgrade/admin authority.
- **Restaking** — permissionless value-moving entrypoints; signature replay (nonce/deadline) & whether the signature binds the exact action; per-counterparty authorization; upgrade/admin authority.
- **NFT Lending** — permissionless value-moving entrypoints; signature replay (nonce/deadline) & whether the signature binds the exact action; per-counterparty authorization; upgrade/admin authority.
- **DAO Service Provider** — permissionless value-moving entrypoints; signature replay (nonce/deadline) & whether the signature binds the exact action; per-counterparty authorization; upgrade/admin authority.
- **Restaked BTC** — permissionless value-moving entrypoints; signature replay (nonce/deadline) & whether the signature binds the exact action; per-counterparty authorization; upgrade/admin authority.
- **SoFi** — permissionless value-moving entrypoints; signature replay (nonce/deadline) & whether the signature binds the exact action; per-counterparty authorization; upgrade/admin authority.
- **Governance Incentives** — permissionless value-moving entrypoints; signature replay (nonce/deadline) & whether the signature binds the exact action; per-counterparty authorization; upgrade/admin authority.
- **NFT Marketplace** — permissionless value-moving entrypoints; signature replay (nonce/deadline) & whether the signature binds the exact action; per-counterparty authorization; upgrade/admin authority.
- **Gaming** — permissionless value-moving entrypoints; signature replay (nonce/deadline) & whether the signature binds the exact action; per-counterparty authorization; upgrade/admin authority.
- **Payments** — permissionless value-moving entrypoints; signature replay (nonce/deadline) & whether the signature binds the exact action; per-counterparty authorization; upgrade/admin authority.
- **Options** — auto-roll/settlement authorization; per-counterparty (maker) authorization; oracle at expiry; permissionless mint/settle.

## The 207 protocols (random order)

| # | Protocol | Chain(s) | Category | TVL | Revenue |
|--:|---|---|---|--:|---|
| 1 | **MultiBit Protocol** (`multibit-protocol`) | Bitcoin,Ethereum | Bridge | $0.15M | no-rev |
| 2 | **Altura** (`altura`) | Hyperliquid L1 | Liquidity Manager | $32.43M | no-rev |
| 3 | **ColorPool** (`colorpool`) | Chromia | Dexs | $0.31M | no-rev |
| 4 | **Ociswap Precision** (`ociswap-precision`) | Radix | Dexs | $0.05M | no-rev |
| 5 | **tramplin.io** (`tramplin-io`) | Solana | Staking Pool | $1.02M | no-rev |
| 6 | **Sygnum FIUSD Liquidity Fund** (`sygnum-fiusd-liquidity-fund`) | zkSync Era | RWA | $23.94M | no-rev |
| 7 | **ErgoDEX** (`ergodex`) | Ergo | Dexs | $0.38M | no-rev |
| 8 | **Native Lend Curator** (`native-lend-curator`) | Monad | Risk Curators | $0.13M | no-rev |
| 9 | **Vishwa** (`vishwa`) | Bitcoin,Sui | Anchor BTC | $67.47M | no-rev |
| 10 | **Crescent Dex** (`crescent-dex`) | Crescent | Dexs | $0.06M | no-rev |
| 11 | **Kestrel** (`kestrel`) | Solana | Onchain Capital Allocator | $0.15M | no-rev |
| 12 | **VaporDex V1** (`vapordex-v1`) | Avalanche,Telos | Dexs | $0.34M | no-rev |
| 13 | **246Club** (`246club`) | Plasma | Lending | $0.07M | no-rev |
| 14 | **SODAX** (`sodax`) | Arbitrum,Binance | Bridge | $2.02M | no-rev |
| 15 | **Sturdy V1** (`sturdy-v1`) | Ethereum,Fantom | Lending | $0.08M | no-rev |
| 16 | **Rujira Staking** (`rujira-staking`) | Thorchain | Farm | $3.46M | no-rev |
| 17 | **1INTRO** (`1intro`) | Solana | Dexs | $0.09M | no-rev |
| 18 | **Invariant Group** (`invariant-group`) | Plasma,Hemi | Risk Curators | $0.12M | no-rev |
| 19 | **ParyonUSD** (`paryonusd`) | Bitcoincash | CDP | $0.61M | no-rev |
| 20 | **Unichain Bridge** (`unichain-bridge`) | Ethereum | Canonical Bridge | $3.26M | no-rev |
| 21 | **Aquifer** (`aquifer`) | — | Dexs | $2.81M | no-rev |
| 22 | **BounceBit Prime** (`bouncebit-prime`) | Binance,Ethereum | Basis Trading | $11.45M | no-rev |
| 23 | **Flamix** (`flamix`) | Flare | Derivatives | $0.35M | no-rev |
| 24 | **Twyne** (`twyne`) | Ethereum | Lending | $19.48M | no-rev |
| 25 | **Blur Lending** (`blur-lending`) | Ethereum | NFT Lending | $8.83M | no-rev |
| 26 | **Megaton Finance** (`megaton-finance`) | TON | Dexs | $0.79M | no-rev |
| 27 | **USE** (`use`) | Ergo | Algo-Stables | $0.15M | no-rev |
| 28 | **AgentFi** (`agentfi`) | Blast | AI Agents | $0.62M | no-rev |
| 29 | **Kona Stableswap** (`kona-stableswap`) | Abstract | Dexs | $0.10M | no-rev |
| 30 | **DipCoin Spot** (`dipcoin-spot`) | Sui | Dexs | $0.86M | no-rev |
| 31 | **Bitbond Sales** (`bitbond-sales`) | Ethereum,Binance | Launchpad | $0.06M | no-rev |
| 32 | **Bio Protocol** (`bio-protocol`) | Ethereum,Base | Launchpad | $3.71M | no-rev |
| 33 | **Microchain** (`microchain`) | Fuel | Dexs | $0.19M | no-rev |
| 34 | **TownSquare Lending** (`townsquare-lending`) | Monad | Lending | $0.44M | no-rev |
| 35 | **Krystal Auto-Farm Vault** (`krystal-auto-farm-vault`) | Base,Binance | AI Agents | $0.55M | no-rev |
| 36 | **CrossCurve** (`crosscurve`) | Blast,Taiko | Cross Chain Bridge | $0.06M | no-rev |
| 37 | **Circle Gateway** (`circle-gateway`) | Ethereum | Cross Chain Bridge | $62.93M | no-rev |
| 38 | **Hyperdrive HL Lending** (`hyperdrive-hl-lending`) | Hyperliquid L1 | Lending | $0.89M | no-rev |
| 39 | **Estate Protocol** (`estate-protocol`) | Arbitrum | RWA | $13.95M | no-rev |
| 40 | **VyFinance Dex** (`vyfinance-dex`) | Cardano | Dexs | $0.58M | no-rev |
| 41 | **PepeTeam DEX** (`pepeteam-dex`) | Binance,Waves | Dexs | $0.07M | no-rev |
| 42 | **Ignition LST** (`ignition-lst`) | Fogo | Liquid Staking | $1.20M | no-rev |
| 43 | **edgeX Bridge** (`edgex-bridge`) | Arbitrum,Ethereum | Bridge | $71.54M | no-rev |
| 44 | **SocialSwap** (`socialswap`) | Tron | Dexs | $0.25M | no-rev |
| 45 | **SparkDEX stFLR** (`sparkdex-stflr`) | Flare | Liquid Staking | $1.59M | no-rev |
| 46 | **HARVEST FLOW** (`harvest-flow`) | Plume Mainnet,Polygon | RWA Lending | $0.53M | no-rev |
| 47 | **Firelight** (`firelight`) | Flare | Farm | $76.89M | no-rev |
| 48 | **ObeliskBTC** (`obeliskbtc`) | Bitcoin | Bridge | $23.99M | no-rev |
| 49 | **TokenLabs** (`tokenlabs`) | IOTA | Liquid Staking | $0.16M | no-rev |
| 50 | **Clarity** (`clarity`) | Cardano | DAO Service Provider | $0.37M | no-rev |
| 51 | **Smoothy** (`smoothy`) | Ethereum,Binance | Dexs | $0.49M | no-rev |
| 52 | **Asseto CASH+** (`asseto-cash`) | Binance,Ethereum | RWA | $1.50M | no-rev |
| 53 | **Nawa Protocol** (`nawa-protocol`) | ZIGChain,Ethereum | RWA | $3.99M | no-rev |
| 54 | **JEXchangeDefi** (`jexchangedefi`) | Elrond | Dexs | $0.10M | no-rev |
| 55 | **SquadSwap WOW** (`squadswap-wow`) | Binance | Dexs | $0.16M | no-rev |
| 56 | **DeFindex** (`defindex`) | Stellar | Yield Aggregator | $19.91M | no-rev |
| 57 | **Rooster Protocol V1** (`rooster-protocol-v1`) | Plume Mainnet | Dexs | $0.05M | no-rev |
| 58 | **Probable** (`probable`) | Binance | Prediction Market | $0.21M | no-rev |
| 59 | **Arkonix** (`arkonix`) | Ethereum,Arbitrum | Onchain Capital Allocator | $0.15M | no-rev |
| 60 | **DFS V2** (`dfs-v2`) | X Layer | Dexs | $0.09M | no-rev |
| 61 | **Starswap Starcoin** (`starswap-starcoin`) | Starcoin | Dexs | $0.54M | no-rev |
| 62 | **Meso Finance** (`meso-finance`) | Aptos | Lending | $0.20M | no-rev |
| 63 | **Jumbo Exchange** (`jumbo-exchange`) | Near | Dexs | $0.52M | no-rev |
| 64 | **Rysk Premium** (`rysk-premium`) | Hyperliquid L1,Ethereum | Yield | $1.61M | no-rev |
| 65 | **Tori Finance** (`tori-finance`) | Ethereum | Basis Trading | $66.25M | no-rev |
| 66 | **Boar Finance** (`boar-finance`) | Mezo | Yield Aggregator | $0.19M | no-rev |
| 67 | **SolvBTC LSTs** (`solvbtc-lsts`) | Ethereum,Bitcoin | Restaked BTC | $75.85M | no-rev |
| 68 | **Adrastea Restaking Operator** (`adrastea-restaking-operator`) | Solana | Staking Pool | $2.87M | no-rev |
| 69 | **SuiBridge** (`suibridge`) | Ethereum | Canonical Bridge | $31.20M | no-rev |
| 70 | **Dexalot DEX** (`dexalot-dex`) | Dexalot,Arbitrum | Dexs | $2.79M | no-rev |
| 71 | **Stobox** (`stobox`) | Arbitrum,Binance | RWA | $13.95M | no-rev |
| 72 | **WYND DEX** (`wynd-dex`) | Juno | Dexs | $0.07M | no-rev |
| 73 | **Symmetry** (`symmetry`) | Solana | Indexes | $1.13M | no-rev |
| 74 | **Starknet BTC Staking** (`starknet-btc-staking`) | Starknet | Staking Pool | $48.04M | no-rev |
| 75 | **Babylon Finance** (`babylon-finance`) | Ethereum | Indexes | $0.12M | no-rev |
| 76 | **Superposition** (`superposition`) | Aptos | Lending | $0.14M | no-rev |
| 77 | **Ashswap** (`ashswap`) | Elrond | Dexs | $0.81M | no-rev |
| 78 | **Bifrost DEX** (`bifrost-dex`) | Bifrost | Dexs | $3.20M | no-rev |
| 79 | **JustLock** (`justlock`) | Radix | Token Locker | $0.08M | no-rev |
| 80 | **Bitlayer YBTC Family** (`bitlayer-ybtc-family`) | Bitcoin,Ethereum | Anchor BTC | $31.47M | no-rev |
| 81 | **Crema Finance** (`crema-finance`) | Solana | Dexs | $0.13M | no-rev |
| 82 | **AO Bridge** (`ao-bridge`) | Ethereum | Canonical Bridge | $52.61M | no-rev |
| 83 | **Gold DAO** (`gold-dao`) | ICP | RWA | $0.80M | no-rev |
| 84 | **Kipseli** (`kipseli`) | — | Dexs | $1.04M | no-rev |
| 85 | **Rujira AMM Strategies** (`rujira-amm-strategies`) | Thorchain | Yield | $1.66M | no-rev |
| 86 | **AlphaSec Bridge** (`alphasec-bridge`) | Klaytn | Bridge | $0.52M | no-rev |
| 87 | **Extended Spot** (`extended-spot`) | Starknet | Dexs | $2.82M | no-rev |
| 88 | **StarkDeFI** (`starkdefi`) | Starknet | Dexs | $0.07M | no-rev |
| 89 | **Parallel Lending** (`parallel-lending`) | Ethereum | Lending | $0.06M | no-rev |
| 90 | **Frigg.eco** (`frigg-eco`) | Ethereum | RWA | $0.18M | no-rev |
| 91 | **Axis** (`axis`) | Ethereum | Basis Trading | $67.73M | no-rev |
| 92 | **Nostra Money Market** (`nostra-money-market`) | Starknet | Lending | $3.72M | no-rev |
| 93 | **BunnySwap** (`bunnyswap`) | Base | Dexs | $0.18M | no-rev |
| 94 | **Tomo** (`tomo`) | Linea | SoFi | $0.17M | no-rev |
| 95 | **Green Planet** (`green-planet`) | Binance | Lending | $0.15M | no-rev |
| 96 | **Lazy** (`lazy`) | Ethereum | Yield | $1.19M | no-rev |
| 97 | **Meridian Predict** (`meridian-predict`) | Robinhood Chain | Prediction Market | $0.26M | no-rev |
| 98 | **MetalX Dex** (`metalx-dex`) | Proton | Dexs | $5.18M | no-rev |
| 99 | **Moria Protocol** (`moria-protocol`) | Bitcoincash | CDP | $0.84M | no-rev |
| 100 | **Tigris Mezo V2** (`tigris-mezo-v2`) | Mezo | Dexs | $0.36M | no-rev |
| 101 | **mySwap V1** (`myswap-v1`) | Starknet | Dexs | $0.61M | no-rev |
| 102 | **Zodial** (`zodial`) | Solana | Lending | $0.20M | no-rev |
| 103 | **Grvt Bridge** (`grvt-bridge`) | Ethereum | Bridge | $34.38M | no-rev |
| 104 | **Realms** (`realms`) | Solana | Governance Incentives | $19.00M | no-rev |
| 105 | **Loyal Earn** (`loyal-earn`) | Solana | Yield Aggregator | $0.60M | no-rev |
| 106 | **tzBTC** (`tzbtc`) | Bitcoin | Bridge | $9.44M | no-rev |
| 107 | **XAI Bridge** (`xai-bridge`) | Arbitrum | Canonical Bridge | $0.08M | no-rev |
| 108 | **Archer Exchange** (`archer-exchange`) | Solana | Dexs | $0.85M | no-rev |
| 109 | **RSwap** (`rswap`) | Radix | Dexs | $0.19M | no-rev |
| 110 | **Solayer USD** (`solayer-usd`) | Solana | RWA | $0.69M | no-rev |
| 111 | **Punks Terminal** (`punks-terminal`) | Ethereum | NFT Marketplace | $1.67M | no-rev |
| 112 | **Meridian Perps** (`meridian-perps`) | Robinhood Chain | Derivatives | $2.51M | no-rev |
| 113 | **Doma** (`doma`) | Doma | Yield | $0.05M | no-rev |
| 114 | **Koi Finance CL** (`koi-finance-cl`) | zkSync Era | Dexs | $0.08M | no-rev |
| 115 | **Fren Pets** (`fren-pets`) | Base | Gaming | $0.07M | no-rev |
| 116 | **Echo Bridge** (`echo-bridge`) | BSquared,Bitcoin | Bridge | $93.18M | no-rev |
| 117 | **SwitchX** (`switchx`) | — | Dexs | $0.32M | no-rev |
| 118 | **StandX Bridge** (`standx-bridge`) | Binance,Solana | Canonical Bridge | $31.94M | no-rev |
| 119 | **ORIGYN** (`origyn`) | ICP | RWA | $52.00M | no-rev |
| 120 | **Pact** (`pact`) | Algorand | Dexs | $1.32M | no-rev |
| 121 | **Coffer Network** (`coffer-network`) | Bitcoin | Bridge | $1.46M | no-rev |
| 122 | **Ocean One** (`ocean-one`) | Mixin | Dexs | $0.84M | no-rev |
| 123 | **MatrixDock XAUM** (`matrixdock-xaum`) | Binance,Ethereum | RWA | $67.82M | no-rev |
| 124 | **Nightshade Finance** (`nightshade-finance`) | Alephium | Dexs | $0.06M | no-rev |
| 125 | **Superfluid** (`superfluid`) | Ethereum,Optimism | Payments | $6.00M | no-rev |
| 126 | **BULK** (`bulk`) | Solana | Derivatives | $20.43M | no-rev |
| 127 | **Ledgity Yield** (`ledgity-yield`) | Base,Ethereum | Yield | $2.51M | no-rev |
| 128 | **wTAO** (`wtao`) | Bittensor | Bridge | $27.93M | no-rev |
| 129 | **UNCX Network Solana** (`uncx-network-solana`) | Solana | Token Locker | $0.49M | no-rev |
| 130 | **Perena Dex** (`perena-dex`) | Solana | Dexs | $0.63M | no-rev |
| 131 | **JupUSD** (`jupusd`) | Solana | Basis Trading | $48.34M | no-rev |
| 132 | **MuesliSwap** (`muesliswap`) | Cardano,Milkomeda | Dexs | $0.20M | no-rev |
| 133 | **XAX** (`xax`) | Ethereum | Yield | $0.08M | no-rev |
| 134 | **Revert Lend** (`revert-lend`) | Arbitrum,Base | Lending | $7.24M | no-rev |
| 135 | **Unified Labs** (`unified-labs`) | Monad | Risk Curators | $0.10M | no-rev |
| 136 | **DefiTuna Lending** (`defituna-lending`) | Solana | Lending | $1.05M | no-rev |
| 137 | **Lens Chain** (`lens-chain`) | Ethereum | Canonical Bridge | $0.53M | no-rev |
| 138 | **Ink Bridge** (`ink-bridge`) | Ethereum | Canonical Bridge | $43.65M | no-rev |
| 139 | **BisonFi** (`bisonfi`) | — | Dexs | $19.43M | no-rev |
| 140 | **Forthewin Network** (`forthewin-network`) | NEO | Dexs | $0.43M | no-rev |
| 141 | **Compound V1** (`compound-v1`) | Ethereum | Lending | $3.21M | no-rev |
| 142 | **Joule Finance** (`joule-finance`) | Aptos | Lending | $0.20M | no-rev |
| 143 | **Yamfore** (`yamfore`) | Cardano | Lending | $0.05M | no-rev |
| 144 | **ParaSpace Lending V1** (`paraspace-lending-v1`) | Ethereum,zkSync Era | Lending | $0.23M | no-rev |
| 145 | **Sanko Bridge** (`sanko-bridge`) | Arbitrum | Canonical Bridge | $1.34M | no-rev |
| 146 | **Appchain Bridge** (`appchain-bridge`) | Ethereum | Canonical Bridge | $0.05M | no-rev |
| 147 | **SuiDex** (`suidex`) | Sui | Dexs | $0.10M | no-rev |
| 148 | **XRPL DEX** (`xrpl-dex`) | Ripple | Dexs | $37.36M | no-rev |
| 149 | **Isle Finance** (`isle-finance`) | Hedera | RWA Lending | $0.93M | no-rev |
| 150 | **exSat Bridge** (`exsat-bridge`) | Bitcoin | Bridge | $3.04M | no-rev |
| 151 | **Nostra Money Market Alpha** (`nostra-money-market-alpha`) | Starknet | Lending | $0.16M | no-rev |
| 152 | **Exponent Risk Tranching** (`exponent-risk-tranching`) | Solana | Yield | $6.99M | no-rev |
| 153 | **Puzzle Swap** (`puzzle-swap`) | Waves | Dexs | $0.48M | no-rev |
| 154 | **reed** (`reed`) | Cardano | CDP | $0.09M | no-rev |
| 155 | **SYNO Finance** (`syno-finance`) | Arbitrum,Scroll | Lending | $0.20M | no-rev |
| 156 | **WaterX** (`waterx`) | Sui | Derivatives | $0.60M | no-rev |
| 157 | **Arkis** (`arkis`) | Ethereum,Hyperliquid L1 | Lending | $3.51M | no-rev |
| 158 | **Frgmnt** (`frgmnt`) | Base | Yield Aggregator | $0.10M | no-rev |
| 159 | **Carrot Lend** (`carrot-lend`) | Solana | Lending | $0.07M | no-rev |
| 160 | **Mangrove** (`mangrove`) | Blast,Arbitrum | Dexs | $4.28M | no-rev |
| 161 | **PulseChain Bridge** (`pulsechain-bridge`) | Ethereum | Canonical Bridge | $62.87M | no-rev |
| 162 | **Pool Party** (`pool-party`) | Canton | Dexs | $0.24M | no-rev |
| 163 | **CORE Bridge** (`core-bridge`) | Avalanche,Arbitrum | Canonical Bridge | $2.93M | no-rev |
| 164 | **dreamDEX** (`dreamdex`) | Somnia | Dexs | $1.26M | no-rev |
| 165 | **Nereus Finance** (`nereus-finance`) | Avalanche | Lending | $0.05M | no-rev |
| 166 | **Jito Restaking** (`jito-restaking`) | Solana | Restaking | $17.94M | no-rev |
| 167 | **Hypersurface** (`hypersurface`) | Hyperliquid L1,Base | Options | $4.53M | no-rev |
| 168 | **JustMoney** (`justmoney`) | Tron,Binance | Dexs | $0.47M | no-rev |
| 169 | **PowerPool** (`powerpool`) | Ethereum,Binance | Indexes | $0.05M | no-rev |
| 170 | **SundaeSwap V3** (`sundaeswap-v3`) | Cardano | Dexs | $1.32M | no-rev |
| 171 | **SoDEX Bridge** (`sodex-bridge`) | Base,Ethereum | Bridge | $65.31M | no-rev |
| 172 | **DewFinance** (`dewfinance`) | Near | Onchain Capital Allocator | $0.21M | no-rev |
| 173 | **Fathom Lending** (`fathom-lending`) | XDC | Lending | $0.39M | no-rev |
| 174 | **Untangled RWA** (`untangled-rwa`) | Stellar | RWA | $0.15M | no-rev |
| 175 | **SuperEarn** (`superearn`) | Klaytn | Yield | $16.08M | no-rev |
| 176 | **Pascal** (`pascal`) | Solana | Prediction Market | $0.97M | no-rev |
| 177 | **Apyee** (`apyee`) | Ethereum,Base | Yield Aggregator | $0.11M | no-rev |
| 178 | **Mansory** (`mansory`) | Binance,Solana | RWA | $6.70M | no-rev |
| 179 | **Monetrix** (`monetrix`) | Hyperliquid L1 | Basis Trading | $2.46M | no-rev |
| 180 | **Vesta Equity** (`vesta-equity`) | Algorand | RWA | $20.63M | no-rev |
| 181 | **Sonic Gateway** (`sonic-gateway`) | Ethereum | Canonical Bridge | $45.56M | no-rev |
| 182 | **Degen Bridge** (`degen-bridge`) | Base | Canonical Bridge | $1.82M | no-rev |
| 183 | **Rho X LP Vault** (`rho-x-lp-vault`) | Ethereum | Yield | $0.64M | no-rev |
| 184 | **FermiSwap** (`fermiswap`) | — | Dexs | $5.37M | no-rev |
| 185 | **Sky RWA** (`sky-rwa`) | Ethereum | RWA | $73.77M | no-rev |
| 186 | **Suzaku** (`suzaku`) | Avalanche | Restaking | $0.49M | no-rev |
| 187 | **Dyson Finance** (`dyson-finance`) | Linea,Blast | Dexs | $0.10M | no-rev |
| 188 | **Notional V2** (`notional-v2`) | Ethereum | Lending | $3.10M | no-rev |
| 189 | **anetaBTC** (`anetabtc`) | Cardano,Ergo | Bridge | $0.12M | no-rev |
| 190 | **TAC Cross Chain Layer** (`tac-cross-chain-layer`) | TON | Bridge | $3.09M | no-rev |
| 191 | **OraiDEX** (`oraidex`) | Orai | Dexs | $0.12M | no-rev |
| 192 | **KlaySwap V1** (`klayswap-v1`) | Klaytn | Dexs | $4.53M | no-rev |
| 193 | **QuipuSwap V1** (`quipuswap-v1`) | Tezos | Dexs | $0.31M | no-rev |
| 194 | **Trava Finance** (`trava-finance`) | Binance,Fantom | Lending | $0.07M | no-rev |
| 195 | **Increment Lending** (`increment-lending`) | Flow | Lending | $0.38M | no-rev |
| 196 | **STRATO** (`strato`) | Strato | CDP | $16.90M | no-rev |
| 197 | **Teller** (`teller`) | Base,Ethereum | Lending | $1.26M | no-rev |
| 198 | **Igra Attestation** (`igra-attestation`) | Igra | Staking Pool | $0.50M | no-rev |
| 199 | **Oro Finance** (`oro-finance`) | Solana | RWA | $2.63M | no-rev |
| 200 | **Hyward** (`hyward`) | Hyperliquid L1 | Yield | $0.71M | no-rev |
| 201 | **Sigmausd** (`sigmausd`) | Ergo | Algo-Stables | $0.43M | no-rev |
| 202 | **Gimo** (`gimo`) | 0G | Liquid Staking | $3.08M | no-rev |
| 203 | **Dezswap** (`dezswap`) | XPLA | Dexs | $0.10M | no-rev |
| 204 | **Exponent Strategy Vaults** (`exponent-strategy-vaults`) | Solana | Onchain Capital Allocator | $11.06M | no-rev |
| 205 | **Coinmerce Capital** (`coinmerce-capital`) | Hyperliquid L1 | Risk Curators | $1.73M | no-rev |
| 206 | **wCC** (`wcc`) | Canton | Bridge | $0.48M | no-rev |
| 207 | **Lode Markets** (`lode-markets`) | Ethereum | Liquidity Manager | $0.05M | no-rev |

---

**207 protocols**, combined $1,833M. This is the complete remaining qualifying set
in this vein (not a sample). Zero overlap with your blocklist or any prior push; folded into the exclusion set.
