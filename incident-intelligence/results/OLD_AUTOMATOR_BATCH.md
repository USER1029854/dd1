# Old, ungated automators — 96 unwatched protocols old enough to have a forgotten one

> **Why this list exists.** A prior pick, `sofa-org`, turned out to have a real vulnerability, and its
> shape is worth learning from: the bug was in **one of its old automators — an automation contract that
> hadn't been used in about a year, but was still live and still not access-gated.** That is the classic
> "forgotten code that still holds authority" door: a keeper / strategy / roll / harvester / liquidator
> that nobody calls any more, nobody watches, and nobody remembered to lock — yet it can still move or
> mint against live funds. **It may well be random** — one data point is not a law — but it points
> somewhere specific, so this run leans there.

## The pattern (record it)

**OLD-UNGATED-AUTOMATOR-STILL-LIVE** — a protocol keeps automation contracts (keepers, vault strategies,
auto-roll/settlement bots, harvesters, rebalancers, liquidators). Over time strategies get replaced and
old ones are *left deployed*. If a retired automator (a) is still granted a role / still an approved
spender / still holds mint or withdraw authority, and (b) its entrypoint was never access-gated (callable
by anyone, or gated only on a keeper set that was never revoked), then an outsider can drive the dead
automator against live funds. Dormancy + surviving authority + no gate = open door.

## Where it's most likely — this list

Protocols that (1) are in **automation-heavy categories** (they *run* keepers/strategies), (2) are **old
enough to have a retired automator generation** (≥1 year; ordered oldest-first, because the oldest have
had the most time to accumulate forgotten contracts), (3) are **unwatched** (no or low tracked revenue —
no one paid to notice a dormant contract), and (4) are **not** blocked/previously-delivered, **not** a fork
of a major protocol, **not** CEX/L1, holding real money `$50k-$100M`. Watched high-revenue names
(Kamino, gTrade, etc.) were dropped by the revenue filter.

## Decisive check per row (this is the whole point)

1. Enumerate the protocol's automation contracts — keepers, `Strategy*`, `Executor`, `Harvester`,
   `Rebalancer`, `Roll`/`Settlement` bots, liquidation callers (from its factory/registry, adapter, or
   explorer "Contract Creator" trail).
2. Find the **dormant** ones — no successful call in ~1 year (last-tx / event history).
3. For each dormant one still **wired to live funds** — still holds a role (`hasRole`), is still an
   approved spender (`allowance>0`) on a live vault/treasury, or still holds mint/withdraw authority —
   read its entrypoint: **is it access-gated?** If an unprivileged address can call it, that is the finding.
4. Falsifier: the old automator's authority was revoked (role removed / approval zeroed / paused), or its
   entrypoint reverts for non-keepers. Then the door is shut.

**Honesty:** the automator *surface* per row below is inferred from category, not confirmed. This is a
"where to look" list; the on-chain enumeration above is where a real finding is made or killed. Random
misses are expected.

Composition — categories: Liquid Staking 27, CDP 12, Yield 10, Derivatives 9, Staking Pool 9, Farm 8, Options 4, Yield Aggregator 3, Liquid Restaking 3, Onchain Capital Allocator 3, Options Vault 2, Leveraged Farming 2. Chains: Ethereum 13, Solana 6, Base 6, Avalanche 5, Klaytn 4, Near 3, Elrond 3, Algorand 3. TVL/revenue at head (DefiLlama, 2026-08-29); age from DefiLlama listing date.

| # | Protocol | Chain(s) | Category | Age | TVL | Likely automator surface | Revenue |
|--:|---|---|---|--:|--:|---|---|
| 1 | **Oddz** (`oddz`) | Avalanche,Binance | Options | 4.8y | $0.06M | auto-roll / settlement automators (the sofa.org shape) | no-rev-tracked |
| 2 | **Katana** (`katana`) | Solana | Options Vault | 4.7y | $1.99M | auto-roll / settlement automators (the sofa.org shape) | no-rev-tracked |
| 3 | **FLRFarm** (`flrfarm`) | Flare,Songbird | Yield | 4.7y | $0.05M | harvest/compound strategy contracts | no-rev-tracked |
| 4 | **Domination Finance** (`domination-finance`) | Base,Polygon | Derivatives | 4.5y | $0.25M | settlement/roll/funding keepers, DOV vaults | no-rev-tracked |
| 5 | **Klayportal** (`klayportal`) | Klaytn | Staking Pool | 4.4y | $0.55M | reward/rate-update keepers | no-rev-tracked |
| 6 | **LiNEAR Protocol** (`linear-protocol`) | Near | Liquid Staking | 4.3y | $49.69M | oracle/rate-update + rebalance keepers | no-rev-tracked |
| 7 | **Mole** (`mole`) | Sui,Aptos | Yield | 4.3y | $8.67M | harvest/compound strategy contracts | no-rev-tracked |
| 8 | **Hedge** (`hedge`) | Solana | CDP | 4.1y | $0.05M | liquidation & rate-update keepers | no-rev-tracked |
| 9 | **Demex Perp** (`demex-perp`) | Carbon | Derivatives | 4.0y | $0.20M | settlement/roll/funding keepers, DOV vaults | no-rev-tracked |
| 10 | **Aurora Plus** (`aurora-plus`) | Aurora | Farm | 4.0y | $1.07M | reward/harvest automators | no-rev-tracked |
| 11 | **Flashstake** (`flashstake`) | Ethereum,Optimism | Yield | 4.0y | $0.05M | harvest/compound strategy contracts | no-rev-tracked |
| 12 | **Easedefi.org** (`easedefi-org`) | Ethereum | Insurance | 3.9y | $4.86M | claim/settlement automators | no-rev-tracked |
| 13 | **Kleva Farm** (`kleva-farm`) | Klaytn | Leveraged Farming | 3.9y | $0.78M | auto-compound + deleverage keepers | no-rev-tracked |
| 14 | **Meteora vaults** (`meteora-vaults`) | Solana | Yield Aggregator | 3.9y | $51.60M | per-vault strategy + harvester keepers | no-rev-tracked |
| 15 | **Yield Yak Staked Avax** (`yield-yak-staked-avax`) | Avalanche | Liquid Staking | 3.9y | $0.39M | oracle/rate-update + rebalance keepers | no-rev-tracked |
| 16 | **Nitron** (`nitron`) | Carbon | CDP | 3.8y | $0.07M | liquidation & rate-update keepers | no-rev-tracked |
| 17 | **NEOPIN Staking** (`neopin-staking`) | Klaytn,Tron | Staking Pool | 3.7y | $36.57M | reward/rate-update keepers | no-rev-tracked |
| 18 | **Opyn Squeeth** (`opyn-squeeth`) | Ethereum | Derivatives | 3.7y | $0.61M | settlement/roll/funding keepers, DOV vaults | no-rev-tracked |
| 19 | **BendDAO APE Staking** (`benddao-ape-staking`) | Ethereum,ApeChain | Yield | 3.5y | $2.36M | harvest/compound strategy contracts | no-rev-tracked |
| 20 | **Phoenix Bonds** (`phoenix-bonds`) | Near | Yield Aggregator | 3.5y | $0.09M | per-vault strategy + harvester keepers | no-rev-tracked |
| 21 | **ABC Pool** (`abc-pool`) | Conflux | Staking Pool | 3.4y | $5.09M | reward/rate-update keepers | no-rev-tracked |
| 22 | **Quicksilver Protocol** (`quicksilver-protocol`) | Quicksilver | Liquid Staking | 3.4y | $0.25M | oracle/rate-update + rebalance keepers | no-rev-tracked |
| 23 | **TokenPocket** (`tokenpocket`) | Ethereum | Staking Pool | 3.4y | $0.25M | reward/rate-update keepers | no-rev-tracked |
| 24 | **CRETH2** (`creth2`) | Ethereum | Liquid Staking | 3.3y | $1.67M | oracle/rate-update + rebalance keepers | no-rev-tracked |
| 25 | **Zomma Protocol** (`zomma-protocol`) | zkSync Era,Arbitrum | Options | 3.3y | $0.08M | auto-roll / settlement automators (the sofa.org shape) | no-rev-tracked |
| 26 | **FilFi** (`filfi`) | Filecoin | Staking Pool | 3.3y | $0.11M | reward/rate-update keepers | no-rev-tracked |
| 27 | **Carmine Options** (`carmine-options`) | Starknet | Options | 3.2y | $0.10M | auto-roll / settlement automators (the sofa.org shape) | no-rev-tracked |
| 28 | **Stella** (`stella`) | Arbitrum | Leveraged Farming | 3.2y | $0.44M | auto-compound + deleverage keepers | no-rev-tracked |
| 29 | **Hypha** (`hypha`) | Avalanche | Liquid Staking | 3.2y | $3.75M | oracle/rate-update + rebalance keepers | no-rev-tracked |
| 30 | **HashKing** (`hashking`) | Filecoin | Liquid Staking | 3.2y | $0.30M | oracle/rate-update + rebalance keepers | no-rev-tracked |
| 31 | **Meter Liquid Staking** (`meter-liquid-staking`) | Meter | Liquid Staking | 3.1y | $0.09M | oracle/rate-update + rebalance keepers | no-rev-tracked |
| 32 | **JewelSwap Liquid Staking** (`jewelswap-liquid-staking`) | Elrond,Sui | Liquid Staking | 3.1y | $0.31M | oracle/rate-update + rebalance keepers | no-rev-tracked |
| 33 | **HERE Wallet staking** (`here-wallet-staking`) | Near | Liquid Staking | 3.1y | $0.60M | oracle/rate-update + rebalance keepers | no-rev-tracked |
| 34 | **Messina Liquid Staking** (`messina-liquid-staking`) | Algorand | Liquid Staking | 3.0y | $1.06M | oracle/rate-update + rebalance keepers | no-rev-tracked |
| 35 | **MEV Protocol** (`mev-protocol`) | Ethereum | Liquid Staking | 2.9y | $0.12M | oracle/rate-update + rebalance keepers | no-rev-tracked |
| 36 | **Blast pre-launch Farm** (`blast-pre-launch-farm`) | Ethereum | Farm | 2.8y | $2.29M | reward/harvest automators | no-rev-tracked |
| 37 | **IntentX** (`intentx`) | Base,Mantle | Derivatives | 2.8y | $5.67M | settlement/roll/funding keepers, DOV vaults | no-rev-tracked |
| 38 | **Deri V4** (`deri-v4`) | Linea,Binance | Options | 2.8y | $7.89M | auto-roll / settlement automators (the sofa.org shape) | no-rev-tracked |
| 39 | **Balanced Dollar** (`balanced-dollar`) | Icon | CDP | 2.7y | $0.37M | liquidation & rate-update keepers | no-rev-tracked |
| 40 | **Magma Finance** (`magma-finance`) | IoTeX | CDP | 2.7y | $0.08M | liquidation & rate-update keepers | no-rev-tracked |
| 41 | **Blueberry** (`blueberry`) | Hyperliquid L1,Ethereum | Yield | 2.6y | $0.26M | harvest/compound strategy contracts | no-rev-tracked |
| 42 | **Omni Liquid Staking** (`omni-liquid-staking`) | Astar,Astar zkEVM | Liquid Staking | 2.6y | $0.31M | oracle/rate-update + rebalance keepers | no-rev-tracked |
| 43 | **Clip Finance** (`clip-finance`) | Linea,Binance | Liquidity Manager | 2.6y | $0.09M | rebalance/compound automators | no-rev-tracked |
| 44 | **SHUI** (`shui`) | Conflux | Liquid Staking | 2.5y | $1.11M | oracle/rate-update + rebalance keepers | no-rev-tracked |
| 45 | **Strater** (`strater`) | Sui | Yield | 2.5y | $0.13M | harvest/compound strategy contracts | no-rev-tracked |
| 46 | **Artemis Finance** (`artemis-finance`) | Goat,Metis | Liquid Staking | 2.5y | $0.82M | oracle/rate-update + rebalance keepers | no-rev-tracked |
| 47 | **Tensorplex** (`tensorplex`) | Bittensor | Liquid Staking | 2.5y | $0.26M | oracle/rate-update + rebalance keepers | no-rev-tracked |
| 48 | **Hatom TAO Liquid Staking** (`hatom-tao-liquid-staking`) | Elrond | Liquid Staking | 2.4y | $0.94M | oracle/rate-update + rebalance keepers | no-rev-tracked |
| 49 | **AILayer farm** (`ailayer-farm`) | Bitcoin,zkLink | Farm | 2.4y | $81.42M | reward/harvest automators | no-rev-tracked |
| 50 | **Particle DUO** (`particle-duo`) | Blast | CDP | 2.4y | $0.06M | liquidation & rate-update keepers | no-rev-tracked |
| 51 | **Breadchain** (`breadchain`) | xDai | CDP | 2.4y | $0.40M | liquidation & rate-update keepers | no-rev-tracked |
| 52 | **BTCFi CDP** (`btcfi-cdp`) | Bitcoin,Bifrost Network | CDP | 2.4y | $7.61M | liquidation & rate-update keepers | no-rev-tracked |
| 53 | **Manta CeDeFi** (`manta-cedefi`) | Manta | Basis Trading | 2.3y | $26.81M | rebalance/hedge automators | no-rev-tracked |
| 54 | **Core Earn** (`core-earn`) | CORE | Liquid Staking | 2.3y | $0.16M | oracle/rate-update + rebalance keepers | no-rev-tracked |
| 55 | **Affine Restaking** (`affine-restaking`) | Ethereum,Linea | Liquid Restaking | 2.2y | $0.06M | oracle/rate-update + rebalance keepers | no-rev-tracked |
| 56 | **Doubler** (`doubler`) | Arbitrum,Manta | Derivatives | 2.2y | $0.16M | settlement/roll/funding keepers, DOV vaults | no-rev-tracked |
| 57 | **Corn Kernels** (`corn-kernels`) | Ethereum | Farm | 1.9y | $0.35M | reward/harvest automators | no-rev-tracked |
| 58 | **Gain** (`gain`) | Ethereum | Onchain Capital Allocator | 1.9y | $32.14M | allocation/rebalance automators | no-rev-tracked |
| 59 | **GOLDSTATION Staking** (`goldstation-staking`) | Klaytn | Staking Pool | 1.9y | $0.46M | reward/rate-update keepers | no-rev-tracked |
| 60 | **Adrastea LRT** (`adrastea-lrt`) | Solana | Liquid Restaking | 1.9y | $0.59M | oracle/rate-update + rebalance keepers | no-rev-tracked |
| 61 | **Hourglass** (`hourglass`) | Ethereum,Mantle | Yield | 1.9y | $0.15M | harvest/compound strategy contracts | no-rev-tracked |
| 62 | **Synatra** (`synatra`) | Solana | Yield Aggregator | 1.9y | $2.02M | per-vault strategy + harvester keepers | no-rev-tracked |
| 63 | **Endur** (`endur`) | Starknet | Liquid Staking | 1.8y | $6.33M | oracle/rate-update + rebalance keepers | no-rev-tracked |
| 64 | **Biquid** (`biquid`) | Bifrost Network | Liquid Staking | 1.8y | $2.98M | oracle/rate-update + rebalance keepers | no-rev-tracked |
| 65 | **Inter Protocol** (`inter-protocol`) | Agoric | CDP | 1.7y | $0.08M | liquidation & rate-update keepers | no-rev-tracked |
| 66 | **InfinityPools** (`infinitypools`) | Base | Derivatives | 1.6y | $0.12M | settlement/roll/funding keepers, DOV vaults | no-rev-tracked |
| 67 | **Reti Pooling** (`reti-pooling`) | Algorand | Staking Pool | 1.6y | $65.12M | reward/rate-update keepers | no-rev-tracked |
| 68 | **Sophon Farm** (`sophon-farm`) | Sophon,Ethereum | Farm | 1.6y | $2.38M | reward/harvest automators | no-rev-tracked |
| 69 | **Angles Stake** (`angles-stake`) | Sonic | Liquid Staking | 1.6y | $0.62M | oracle/rate-update + rebalance keepers | no-rev-tracked |
| 70 | **Ethereal Season Zero** (`ethereal-season-zero`) | Ethereum | Farm | 1.5y | $1.85M | reward/harvest automators | no-rev-tracked |
| 71 | **Hemi Staking** (`hemi-staking`) | Hemi | Farm | 1.5y | $43.31M | reward/harvest automators | no-rev-tracked |
| 72 | **Qearn** (`qearn`) | Qubic | Staking Pool | 1.5y | $14.10M | reward/rate-update keepers | no-rev-tracked |
| 73 | **stCYBER** (`stcyber`) | Cyber | Liquid Staking | 1.5y | $1.04M | oracle/rate-update + rebalance keepers | no-rev-tracked |
| 74 | **Solido Cash** (`solido-cash`) | Supra | CDP | 1.4y | $0.47M | liquidation & rate-update keepers | no-rev-tracked |
| 75 | **bemo V2** (`bemo-v2`) | TON | Liquid Staking | 1.4y | $0.43M | oracle/rate-update + rebalance keepers | no-rev-tracked |
| 76 | **Cyclo** (`cyclo`) | Flare | Derivatives | 1.4y | $0.18M | settlement/roll/funding keepers, DOV vaults | no-rev-tracked |
| 77 | **Telegram USD** (`telegram-usd`) | TON | CDP | 1.3y | $0.36M | liquidation & rate-update keepers | no-rev-tracked |
| 78 | **Solv Strategies** (`solv-strategies`) | Binance,Avalanche | Onchain Capital Allocator | 1.3y | $67.52M | allocation/rebalance automators | no-rev-tracked |
| 79 | **Supra Staking** (`supra-staking`) | Supra | Staking Pool | 1.3y | $4.13M | reward/rate-update keepers | no-rev-tracked |
| 80 | **XOXNO Liquid Staking** (`xoxno-liquid-staking`) | Elrond | Liquid Staking | 1.3y | $0.97M | oracle/rate-update + rebalance keepers | no-rev-tracked |
| 81 | **Stobix** (`stobix`) | Base | Derivatives | 1.2y | $0.05M | settlement/roll/funding keepers, DOV vaults | no-rev-tracked |
| 82 | **AlphBanX** (`alphbanx`) | Alephium | CDP | 1.2y | $0.15M | liquidation & rate-update keepers | no-rev-tracked |
| 83 | **hskhodlium** (`hskhodlium`) | HashKey Chain | Liquid Staking | 1.2y | $0.41M | oracle/rate-update + rebalance keepers | no-rev-tracked |
| 84 | **The Rig** (`the-rig`) | Fuel | Liquid Staking | 1.2y | $0.40M | oracle/rate-update + rebalance keepers | no-rev-tracked |
| 85 | **Myth Finance dualSTAKE** (`myth-finance-dualstake`) | Algorand | Liquid Staking | 1.2y | $0.14M | oracle/rate-update + rebalance keepers | no-rev-tracked |
| 86 | **Escher** (`escher`) | Union,Babylon Genesis | Liquid Staking | 1.2y | $0.35M | oracle/rate-update + rebalance keepers | no-rev-tracked |
| 87 | **Rysk V12** (`rysk-v12`) | Hyperliquid L1,Ethereum | Options Vault | 1.2y | $49.55M | auto-roll / settlement automators (the sofa.org shape) | no-rev-tracked |
| 88 | **Zeus btcSOL** (`zeus-btcsol`) | Solana | Liquid Restaking | 1.1y | $0.59M | oracle/rate-update + rebalance keepers | no-rev-tracked |
| 89 | **Liminal Basis** (`liminal-basis`) | Hyperliquid L1 | Basis Trading | 1.1y | $24.22M | rebalance/hedge automators | no-rev-tracked |
| 90 | **GammaSwap Yield Tokens** (`gammaswap-yield-tokens`) | Base | Yield | 1.1y | $0.09M | harvest/compound strategy contracts | no-rev-tracked |
| 91 | **Atrium** (`atrium`) | Cardano | Farm | 1.1y | $0.40M | reward/harvest automators | no-rev-tracked |
| 92 | **Spectra MetaVaults** (`spectra-metavaults`) | Base,Flare | Onchain Capital Allocator | — | $9.22M | allocation/rebalance automators | no-rev-tracked |
| 93 | **GMX V1 Perps** (`gmx-v1-perps`) | Avalanche,Arbitrum | Derivatives | — | $3.19M | settlement/roll/funding keepers, DOV vaults | no-rev-tracked |
| 94 | **Kolibri** (`kolibri`) | Tezos | CDP | — | $0.60M | liquidation & rate-update keepers | no-rev-tracked |
| 95 | **TEN Finance** (`ten-finance`) | Binance | Yield | — | $0.21M | harvest/compound strategy contracts | no-rev-tracked |
| 96 | **Penguin Finance** (`penguin-finance`) | Avalanche | Yield | — | $0.08M | harvest/compound strategy contracts | no-rev-tracked |

---

**96 protocols**, oldest-first, holding a combined $648M. Not a ranking of likelihood —
a ranking of *how long there's been to forget an automator*. Zero overlap with your blocklist or any prior push.
