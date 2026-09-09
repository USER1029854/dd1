# DISC-20260909-010 — The corrected audit queue: unwatched, bespoke, pre-AI custom logic (TVL held neutral)

## What changed, and why (this supersedes the *ranking* in DISC-008/009)

DISC-009 quietly let **TVL** drive the list. I dropped the floor to ~$10k and the population collapsed to a median of ~$23k, which made "tiny" read as "the answer." That is wrong, and the counter-example is the one that started this: **SOFA was an ~$850k-TVL protocol.** The exploit only *removed* ~$10k, but that number describes the finding, not the target. TVL tells you *whether there is enough to bother auditing* — nothing more. It is an attribute like any other, not a ranking axis.

So this queue is ranked by the three things that actually predict where a novel bug is still live, none of which is size:

1. **Custom logic — not a fork.** No Aave / Compound / Uniswap / Liquity lineage. Forks inherit code that has been read thousands of times; novel bugs live in code someone wrote themselves. Every row here is a **bespoke financial primitive**.
2. **Unwatched.** No fee revenue, deprecated, or a dead site — nobody is paid to monitor it, so a bug found today is still exploitable tomorrow.
3. **Pre-AI-era / unchanged.** Listed before 2023, before EIP-712 helpers and `SafeCast` were reflexive and before LLM-assisted review existed. Idiosyncratic, hand-rolled, never machine-scanned — SOFA's XOR-signature spaghetti is the archetype.

**TVL is shown as a neutral column across the full range** — from ~$20k up to eight figures. Do not read bigger or smaller as better. If anything the sweet spot is the band SOFA itself lived in (a few hundred k to a few million): big enough to be worth an afternoon, small enough that no one is watching.

The honest population this logic yields is **108** protocols (pre-2023 · bespoke · unwatched · a real value-moving surface), grouped below by the hand-rolled surface where the bug would live. I am not padding or trimming to a number.

**Reading the flags:** 💤 = deprecated or an abandoned "V1" the team left behind when it shipped a V2 (the exact Notional-V1 / SOFA pattern — old money parked in code no one maintains); ⚠ = the protocol was **exploited before** (the remnant may still be worth reading, but know the history and expect the obvious hole to be patched); ↺ = already listed in DISC-009 (kept here because you haven't audited it and the framing is now corrected).

## Start here — bespoke money-moving math in the SOFA band (surface-diverse, not size-sorted)

Fourteen I would open first: hand-rolled credit / derivatives / options / synth math, abandoned or unwatched, still funded, none a known past-hack, none a bridge (those are verifier bugs and sit in their own section). Deliberately spread across surfaces and the few-hundred-k-to-few-M band SOFA lived in — **not** ranked by TVL.

| Protocol | TVL | Listed | Chain | Bespoke surface | Why it's the SOFA shape | Flags |
|---|---|---|---|---|---|---|
| DeFIL | $1.76M | 2022 | Ethereum | Lending | hand-rolled credit/CDP solvency math | 💤 abandoned/V1 |
| Contango V1 | $297k | 2022 | Arbitrum | Derivatives | custom margin/funding/PnL engine | 💤 abandoned/V1 |
| Chest Finance | $654k | 2021 | Solana | Options Vault | pooled-collateral option settlement | 💤 abandoned/V1 |
| Sigmausd | $402k | 2022 | Ergo | Algo-Stables | custom mint/redeem & peg math | — |
| Silo V1 | $1.50M | 2022 | Arbitrum | Lending | hand-rolled credit/CDP solvency math | 💤 abandoned/V1 |
| ApeX Pro | $1.43M | 2022 | Ethereum | Derivatives | custom margin/funding/PnL engine | — |
| PsyOptions | $580k | 2022 | Solana | Options | pooled-collateral option settlement | 💤 abandoned/V1 |
| Ostable | $315k | 2022 | Obyte | Algo-Stables | custom mint/redeem & peg math | — |
| Interest Protocol | $1.45M | 2022 | Ethereum | CDP | hand-rolled credit/CDP solvency math | 💤 abandoned/V1 |
| IPOR Derivatives | $634k | 2022 | Arbitrum | Derivatives | custom margin/funding/PnL engine | — |
| Pods Finance | $389k | 2021 | Polygon | Options | pooled-collateral option settlement | 💤 abandoned/V1 |
| LendFlare | $1.19M | 2022 | Ethereum | Lending | hand-rolled credit/CDP solvency math | 💤 abandoned/V1 |
| Opyn Squeeth | $618k | 2022 | Ethereum | Derivatives | custom margin/funding/PnL engine | — |
| Cega V1 | $308k | 2022 | Solana | Options | pooled-collateral option settlement | 💤 abandoned/V1 |

## Bespoke options / structured products · 9

**Decisive check:** A DOV / structured / exotic-option vault posts **pooled depositor collateral** as one leg of each position. Read who may call mint / settle / exercise / roll: is the entrypoint gated, and is each payoff bound to an oracle snapshot taken at open? Hand-rolled option math (pricing, settlement, collateral release) is exactly the SOFA shape — a pooled counterparty behind an under-reviewed entrypoint.

| Protocol | TVL | Listed | Chain | Category | Watch | Flags | What it is |
|---|---|---|---|---|---|---|---|
| Chest Finance | $654k | 2021 | Solana | Options Vault | no rev | 💤 abandoned/V1 | Earn yield on the largest protocols on Solana: All of the collateral deposited… |
| PsyOptions | $580k | 2022 | Solana | Options | no rev | 💤 abandoned/V1 | Trade on-chain, asset settled, American style options for $BTC & $ETH |
| Pods Finance | $389k | 2021 | Polygon | Options | no rev | 💤 abandoned/V1 | Pods is a decentralized non-custodial options protocol that allows users to cr… |
| Cega V1 | $308k | 2022 | Solana | Options | no rev | 💤 abandoned/V1 | Cega offers safer and transparent yield strategies as defi's first exotic opti… |
| Olive | $50k | 2022 | Ethereum | Options Vault | no rev | 💤 abandoned/V1 ↺ in DISC-009 | Olive is a multi-chain protocol that combines composability with structured pr… |
| Katana | $1.96M | 2022 | Solana | Options Vault | no rev | — | Katana is a yield generation protocol on Solana designed to generate sustainab… |
| Opyn Convexity | $584k | 2022 | Ethereum | Options | no rev | — | Opyn offers European, cash-settled options that auto-exercise upon expiry. |
| Dual Finance | $234k | 2022 | Solana | Options | no rev | — | Incentive Liquidity Infrastructure. Provides token communities with sustainabl… |
| Oddz | $59k | 2021 | Avalanche | Options | no rev | — | Multi-chain derivatives trading platform |

## Bespoke synthetics / algo-stables · 11

**Decisive check:** Custom mint/burn against a collateral ratio or bonding curve. Read the debt & peg accounting: can the ratio or its oracle be moved cheaply, is the mint path gated, and is redemption **split-invariant** (N small redeems == 1 big one)? Bespoke solvency math that no scanner has a signature for.

| Protocol | TVL | Listed | Chain | Category | Watch | Flags | What it is |
|---|---|---|---|---|---|---|---|
| Taiga Acala | $74k | 2022 | Acala | Synthetics | no rev | 💤 abandoned/V1 | A synthetic asset protocol designed to enable maximum efficiency for uniform a… |
| OrderNChaos | $60k | 2022 | Arbitrum | Algo-Stables | no rev | 💤 abandoned/V1 | OrderNChaos(ONC) is a twin system of algorithmic stable coins. ONC produces th… |
| Taiga Karura | $49k | 2022 | Karura | Synthetics | no rev | 💤 abandoned/V1 | A synthetic asset protocol designed to enable maximum efficiency for uniform a… |
| Mobius Finance | $41k | 2021 | Polygon | Synthetics | no rev | 💤 abandoned/V1 ↺ in DISC-009 | Mobius Finance is the first multi-collateral decentralized trading protocol th… |
| Duet Protocol | $39k | 2022 | Arbitrum | Synthetics | no rev | 💤 abandoned/V1 ↺ in DISC-009 | A parallel universe which turns flat assets into sharp assets. |
| Oin Finance | $36k | 2022 | Ethereum | Algo-Stables | no rev | 💤 abandoned/V1 ↺ in DISC-009 | A robust turnkey stablecoin issuance platform built for the multi-chain univer… |
| ION DAO | $34k | 2022 | Osmosis | Synthetics | no rev | 💤 abandoned/V1 ↺ in DISC-009 | ION is the secondary native token on the Osmosis chain. Created by the Osmosis… |
| Synthetify | $26k | 2021 | Solana | Synthetics | no rev | 💤 abandoned/V1 ↺ in DISC-009 | Synthetify is a decentralized synthetic assets protocol build on the Solana bl… |
| Sigmausd | $402k | 2022 | Ergo | Algo-Stables | no rev | — | AgeUSD is a novel crypto-backed algorithmic stablecoin protocol that has been … |
| Ostable | $315k | 2022 | Obyte | Algo-Stables | no rev | — | Ostable is an advanced stable coin platform powered by bonding curves. It is a… |
| ThetaCash | $115k | 2022 | Theta | Synthetics | no rev | — | ThetaCash (TBILL) Rebasing Metaverse Liquidity Token. |

## Bespoke derivatives / perps engine · 19

**Decisive check:** Hand-rolled margin / funding / PnL engine (often a custom vAMM or on-chain book). Read settlement & withdrawal: can a dormant or thin market be self-traded into withdrawable PnL before it is socialized (the Rocket shape); is the mark/funding manipulable; is any close/liquidate path under-gated?

| Protocol | TVL | Listed | Chain | Category | Watch | Flags | What it is |
|---|---|---|---|---|---|---|---|
| Contango V1 | $297k | 2022 | Arbitrum | Derivatives | no rev | 💤 abandoned/V1 | Contango is a unique decentralized market offering expirables, contracts to bu… |
| Mycelium Perpetual Pools | $175k | 2021 | Arbitrum | Derivatives | no rev | 💤 abandoned/V1 | Previously Tracer Perpetual Pools. Build and trade with Mycelium Perpetuals an… |
| SynFutures V1 | $113k | 2022 | Polygon | Derivatives | no rev | 💤 abandoned/V1 | SynFutures is a next-generation derivatives exchange focused on creating an op… |
| 01 | $112k | 2022 | Solana | Derivatives | no rev | 💤 abandoned/V1 | Fully decentralized orderbook based derivatives dex allowing users to trade, b… |
| Unbound | $51k | 2022 | Ethereum | Derivatives | no rev | 💤 abandoned/V1 | Unbound is a decentralized cross-chain liquidity protocol that is building the… |
| Y2K V1 | $43k | 2022 | Arbitrum | Derivatives | $0k/30d | 💤 abandoned/V1 ↺ in DISC-009 | Y2K Finance is a suite of structured products designed for exotic peg derivati… |
| UniDex Perp | $30k | 2022 | Optimism | Derivatives | $411k/30d | 💤 abandoned/V1 ↺ in DISC-009 | UniDex is a DeFi aggregation layer making interesting trading products such as… |
| Predy V3.2 | $25k | 2022 | Arbitrum | Derivatives | $1k/30d | 💤 abandoned/V1 ↺ in DISC-009 | Predy V3.2 allows traders to utilize portfolio margin for Squart and ETH perpe… |
| ApeX Pro | $1.43M | 2022 | Ethereum | Derivatives | no rev | — | ApeX, an innovative derivatives protocol to provide Web3 users with a supreme … |
| IPOR Derivatives | $634k | 2022 | Arbitrum | Derivatives | no rev | — | IPOR (Inter Protocol Over-block Rate) is a DeFi permissionless interest rate i… |
| Opyn Squeeth | $618k | 2022 | Ethereum | Derivatives | no rev | — | Squeeth perpetual exposure to ETH² |
| Pika | $302k | 2021 | Optimism | Derivatives | $0k/30d | — | A Perpetual Swap Exchange |
| HMX | $265k | 2022 | Arbitrum | Derivatives | $0k/30d | — |  HMX (previous perp88) is a next-gen decentralized perpetual exchange with a c… |
| Voltz | $241k | 2022 | Ethereum | Derivatives | no rev | — | Voltz Protocol is a non-custodial Automated Market Maker for Interest Rate Swa… |
| Domination Finance | $238k | 2022 | Base | Derivatives | no rev | — | Trade market share, not price. |
| Demex Perp | $199k | 2022 | Carbon | Derivatives | no rev | — | The first fully decentralized DEX that supports any type of financial market. |
| Ideamarket | $163k | 2021 | Arbitrum | Derivatives | no rev | — | Ideamarket replaces the "arbiter of credibility" function (typically played by… |
| JOJO | $25k | 2022 | Base | Derivatives | $0k/30d | ↺ in DISC-009 | JOJO is a decentralized perpetual contract trading platform that uses an off-c… |
| Drift Trade | $643k | 2021 | Solana | Derivatives | $0k/30d | ⚠ hacked before | Drift brings on-chain, cross-margined perpetual futures to Solana. Making futu… |

## Bespoke lending / CDP (not an Aave/Compound fork) · 43

**Decisive check:** A credit engine someone wrote themselves. Read health-factor / liquidation / withdraw: is any fund-moving entrypoint callable without a per-user gate, is collateral valuation bound to a manipulable source, and does any narrowing cast or rounding corrupt solvency (the Notional-V1 shape)?

| Protocol | TVL | Listed | Chain | Category | Watch | Flags | What it is |
|---|---|---|---|---|---|---|---|
| DeFIL | $1.76M | 2022 | Ethereum | Lending | no rev | 💤 abandoned/V1 | DeFIL is a decentralized Filecoin lending and finance service platform. |
| Silo V1 | $1.50M | 2022 | Arbitrum | Lending | no rev | 💤 abandoned/V1 | Silo Finance creates permissionless and risk-isolated lending markets. |
| Interest Protocol | $1.45M | 2022 | Ethereum | CDP | no rev | 💤 abandoned/V1 | Interest Protocol is a borrow/lend protocol that is highly capital-efficient t… |
| LendFlare | $1.19M | 2022 | Ethereum | Lending | no rev | 💤 abandoned/V1 | Lendflare is a decentralized borrowing platform on Ethereum blockchain that al… |
| Equilibrium Lending | $1.13M | 2022 | Equilibrium | Lending | no rev | 💤 abandoned/V1 | Lending with collateral basket support and min LTV as low as 105% |
| Algofi Lend | $676k | 2021 | Algorand | Lending | no rev | 💤 abandoned/V1 | Decentralized lending protocol and stablecoin built on Algorand |
| BendDAO Lending V1 | $616k | 2022 | Ethereum | NFT Lending | $15k/30d | 💤 abandoned/V1 | BendDAO is a decentralized peer-to-pool based NFT liquidity protocol. |
| Lenfi | $148k | 2022 | Cardano | Lending | no rev | 💤 abandoned/V1 | Open-source and decentralized Lending and Borrowing protocol. |
| BFly Finance | $141k | 2022 | Starcoin | Lending | no rev | 💤 abandoned/V1 | Bfly is a lending platform based on algorithm-based stablecoin of the Starcoin… |
| Morpho Optimizer AaveV2 | $139k | 2022 | Ethereum | Lending | no rev | 💤 abandoned/V1 | Morpho AaveV2 is an on-chain peer-to-peer layer on top of lending pools. Rates… |
| Defrost | $82k | 2021 | Avalanche | CDP | no rev | 💤 abandoned/V1 | Defrost Finance is a decentralized protocol that allows you to leverage yield-… |
| Sturdy V1 | $77k | 2022 | Ethereum | Lending | no rev | 💤 abandoned/V1 | Sturdy is a first of its kind DeFi protocol for interest-free borrowing and hi… |
| Timeswap V1 | $44k | 2022 | Polygon | Lending | no rev | 💤 abandoned/V1 ↺ in DISC-009 | Timeswap is the first oracleless lending/borrowing protocol. Timeswap enables … |
| Morpho Optimizer CompoundV2 | $31k | 2022 | Ethereum | Lending | no rev | 💤 abandoned/V1 ↺ in DISC-009 | Morpho Compound is an on-chain peer-to-peer layer on top of lending pools. Rat… |
| RociFi V1 | $31k | 2022 | Polygon | Lending | no rev | 💤 abandoned/V1 ↺ in DISC-009 | RociFi - On-chain Credit Scoring and Capital-Efficient Lending Protocol |
| Euler V1 | $28k | 2022 | Ethereum | Lending | no rev | 💤 abandoned/V1 ↺ in DISC-009 | Permissionless crypto lending markets are almost here. Euler is a non-custodia… |
| Poof Cash | $26k | 2021 | Celo | Lending | no rev | 💤 abandoned/V1 ↺ in DISC-009 | Decentralized, private DeFi for EVMs. |
| BNPL Pay | $23k | 2022 | Ethereum | Lending | no rev | 💤 abandoned/V1 ↺ in DISC-009 | Collateralised and uncollateralised loans |
| Argo | $22k | 2022 | Aptos | CDP | no rev | 💤 abandoned/V1 ↺ in DISC-009 | Argo is a lending protocol on Aptos that lets users collateral for minting and… |
| OpenSky Finance | $21k | 2022 | Ethereum | NFT Lending | no rev | 💤 abandoned/V1 ↺ in DISC-009 | The first integrated peer-to-pool and peer-to-peer NFT lending protocol built … |
| Indigo | $4.41M | 2022 | Cardano | CDP | $0k/30d | — | Indigo is a decentralized non-custodial synthetic assets protocol built for Ca… |
| FluidTokens | $2.68M | 2022 | Cardano | Lending | $1k/30d | — | Lend and borrow using your NFTs on Cardano's fluid NFT-DeFi bridge. |
| REX Staking | $2.43M | 2021 | Telos | Lending | no rev | — | REX is short for “Resource Exchange” and is a marketplace that allows for the … |
| Hubble | $1.51M | 2022 | Solana | CDP | no rev | — | Hubble's Phase 1 launches a Solana native crypto-backed stablecoin, USDH, that… |
| Arkadiko | $1.14M | 2021 | Stacks | CDP | no rev | — | Arkadiko is a decentralized, non-custodial liquidity protocol where users can … |
| Increment Lending | $378k | 2022 | Flow | Lending | no rev | — | Decentralized Money Market for fungible tokens on Flow. |
| Mars Ecosystem | $274k | 2021 | Binance | CDP | no rev | — | Mars Ecosystem is a new decentralized stablecoin paradigm, it integrates the c… |
| Yield Protocol | $268k | 2021 | Arbitrum | Lending | no rev | — | Yield Protocol brings collateralized fixed-rate,fixed-term borrowing and lendi… |
| Union Protocol | $266k | 2022 | Optimism | Uncollateralized Lending | no rev | — | A decentralized protocol for permissionless credit. |
| Clearpool Lending | $234k | 2022 | Base | Uncollateralized Lending | $0k/30d | — | Clearpool is a decentralized marketplace for unsecured institutional capital. … |
| SmartCredit | $211k | 2022 | Ethereum | Lending | no rev | — | DeFi fixed-term / fixed-interest loans for the borrowers. DeFi personal fixed … |
| AstridDAO | $202k | 2022 | Astar | CDP | no rev | — | AstridDAO is a decentralized money market and multi-collateral stablecoin prot… |
| Green Planet | $158k | 2022 | Binance | Lending | no rev | — | Green Planet is an incentivized, non-custodial lending protocol for earning in… |
| Kokoa Finance | $112k | 2022 | Klaytn | CDP | no rev | — | Kokoa Finance is a crypto-asset-backed stablecoin platform where users can bor… |
| Revest Finance | $110k | 2021 | Ethereum | NFT Lending | no rev | — | The Revest Protocol pioneers a revolutionary new use of NFTs as financial tool… |
| Aave Arc | $57k | 2022 | Ethereum | Lending | no rev | — | Aave Arc is a DeFi liquidity market designed to be compliant with AML regulati… |
| Nereus Finance | $55k | 2022 | Avalanche | Lending | no rev | — | Nereus is a decentralised, non-custodial liquidity market protocol in which us… |
| Hedge | $52k | 2022 | Solana | CDP | no rev | — | Hedge offers 0% interest loans on Solana in form of our CDP stablecoin $USH wi… |
| Credix | $36k | 2022 | Solana | RWA Lending | no rev | ↺ in DISC-009 | Credix is an institutional capital markets ecosystem designed for debt financi… |
| Llamalend | $22k | 2022 | Ethereum | NFT Lending | $0k/30d | ↺ in DISC-009 | Deposit NFTs and borrow ETH for small illiquid NFT collections that can't get … |
| Goldfinch | $2.58M | 2021 | Ethereum | RWA Lending | $4k/30d | 💤 abandoned/V1 ⚠ hacked before | Goldfinch is a decentralized credit protocol, built for the future when all de… |
| JPEG'd | $575k | 2022 | Ethereum | NFT Lending | no rev | 💤 abandoned/V1 ⚠ hacked before | JPEG'd is a decentralized lending protocol on the Ethereum blockchain that ena… |
| Sentiment | $518k | 2022 | Hyperliquid L1 | Lending | no rev | ⚠ hacked before | The Sentiment Protocol is a leveraged lending protocol, specialized for comple… |

## Bespoke parametric & prediction settlement · 6

**Decisive check:** Custom insurance / prediction settlement. Read who may propose and finalize an outcome, whether the trigger independently verifies the real-world event, and whether payout eligibility is tied to a snapshot taken **before** the proposal (the Cozy shape).

| Protocol | TVL | Listed | Chain | Category | Watch | Flags | What it is |
|---|---|---|---|---|---|---|---|
| InsureDAO | $124k | 2022 | Ethereum | Insurance | no rev | 💤 abandoned/V1 | What makes InsureDAO different is our ability to handle everything from creati… |
| Easedefi.org | $4.88M | 2022 | Ethereum | Insurance | no rev | — | Ease is a decentralized coverage protocol that enables users to protect their … |
| Azuro | $1.20M | 2022 | Polygon | Prediction Market | neg | — | Azuro is an infrastructure & liquidity layer for on-chain betting. It utilizes… |
| PRDT | $517k | 2022 | Ethereum | Prediction Market | no rev | — | Know where the Market is going? The First Fully Decentralized Cross-Chain Pred… |
| Bridge Mutual | $56k | 2021 | Ethereum | Insurance | no rev | — | A risk coverage platform for stablecoins, protocols, smart contracts, exchange… |
| Risk Harbor | $38k | 2022 | Arbitrum | Insurance | no rev | ↺ in DISC-009 | Risk Harbor is a risk management marketplace for decentralized finance (DeFi) … |

## Bespoke bridge verifier · 17

**Decisive check:** A hand-rolled cross-chain verifier. Read whether every mint / release is bound 1:1 to a verified, replay-protected remote burn, how many independent signers are truly required, and whether a message can be forged or replayed (the Allbridge / Nomad shape). Several rows here were **already exploited once** — audit the remnant with that history in mind.

| Protocol | TVL | Listed | Chain | Category | Watch | Flags | What it is |
|---|---|---|---|---|---|---|---|
| Proxy | $20.60M | 2022 | Polygon | Bridge | no rev | 💤 abandoned/V1 | Proxy Finance (PRXY) offers a Bitcoin Yield Strategies utilizing DeFi 2.0 incl… |
| Knit Finance | $384k | 2021 | Ethereum | Bridge | no rev | 💤 abandoned/V1 | Developed Single infrastructure which will allow various assets , liquidity to… |
| Hyphen | $100k | 2022 | Polygon | Bridge | no rev | 💤 abandoned/V1 | Hyphen provides simple APIs that lets you easily offer instantaneous value tra… |
| DotOracle | $41k | 2022 | Ethereum | Bridge | no rev | 💤 abandoned/V1 ↺ in DISC-009 | DotOracle is a real-time decentralized Oracle and Cross-chain bridge supported… |
| ioTube | $2.59M | 2022 | IoTeX | Bridge | no rev | — | ioTube is the decentralized bridge for connecting Ethereum, Binance Smart Chai… |
| Butter Network | $1.57M | 2022 | Ethereum | Cross Chain Bridge | no rev | — | Butter is an Omnichain Interoperability Hub integrated with ZK technology that… |
| BabelFish | $1.08M | 2022 | RSK | Bridge | no rev | — | BabelFish is a multi-chain aggregator and distributor of stablecoins |
| ChainPort | $532k | 2021 | Ethereum | Bridge | no rev | — | ChainPort is a next-gen blockchain secure bridge that lets you hop across vari… |
| Counterstake | $415k | 2022 | Obyte | Cross Chain Bridge | no rev | — | Counterstake is a permissionless and fully decentralized cross-chain bridge. |
| Octus Bridge | $395k | 2022 | Avalanche | Bridge | no rev | — | Cross-chain transfers |
| Interlay BTC | $168k | 2022 | Interlay | Bridge | no rev | — | Fully trustless and decentralized Bitcoin bridge |
| anetaBTC | $121k | 2022 | Cardano | Bridge | no rev | — | AnetaBTC is a fully on-chain, decentralized protocol that allows Bitcoin to be… |
| CrossChain Bridge | $79k | 2022 | Ethereum | Cross Chain Bridge | no rev | — | The Cross-Chain Bridge v2.0 has an ambitious goal: It should be possible to mo… |
| EverRise | $31k | 2022 | Binance | Cross Chain Bridge | no rev | ↺ in DISC-009 | EverRise is a blockchain technology company that offers bridging and security … |
| Poly Network | $44.73M | 2022 | Ethereum | Bridge | no rev | 💤 abandoned/V1 ⚠ hacked before | Poly Network is a global cross-chain protocol for implementing blockchain inte… |
| Meter Passport | $791k | 2022 | Ethereum | Bridge | no rev | ⚠ hacked before | Meter Passport is a decentralized multichain bridge for the Meter ecosystem. C… |
| Nomad | $356k | 2022 | Ethereum | Bridge | no rev | ⚠ hacked before | Nomad is an interoperability protocol for generalized message passing. We leve… |

## Bespoke LP-share / liquidity-manager math · 3

**Decisive check:** Custom share pricing over an AMM position. Read how mint() / burn() value the position — spot `slot0` vs a TWAP — and who may trigger rebalance. Unguarded share valuation is drainable with a flash-skew (the Arrakis / Float shape).

| Protocol | TVL | Listed | Chain | Category | Watch | Flags | What it is |
|---|---|---|---|---|---|---|---|
| DefiEdge | $878k | 2022 | Binance | Liquidity Manager | no rev | 💤 abandoned/V1 | Permissionless Liquidity Management on Uniswap V3. DefiEdge provides the smart… |
| Hedgehog | $27k | 2022 | Ethereum | Liquidity Manager | no rev | 💤 abandoned/V1 ↺ in DISC-009 | An automated strategy that earns ETH, by providing liquidity for the Uniswap V… |
| Universe Finance | $26k | 2021 | Ethereum | Liquidity Manager | no rev | 💤 abandoned/V1 ↺ in DISC-009 | Universe Finance is a Uniswap V3 liquidity management platform based on risk g… |

## Scope, honesty, dedup

- **Not big protocols.** Nothing here is Uniswap/Aave-scale or a fork of one; the unwatched filter (no revenue / deprecated) structurally excludes anything with a team paid to watch it. Max TVL in the set is a few tens of millions and those are all deprecated/abandoned (e.g. old bridges), not live giants.
- **TVL is neutral**, shown per row; rank by the bespoke × unwatched × pre-AI signal, not by size.
- **⚠ previously-hacked rows are kept but flagged** (Poly Network, Nomad, Meter Passport, Sentiment, JPEG'd, Drift, Goldfinch). A once-hit protocol that is now abandoned-but-funded is still a legitimate unwatched target, but the obvious vector is likely closed — read the *rest* of its bespoke surface.
- **Overlap with DISC-009 is intentional** (↺): you haven't audited it, and the tiny-TVL framing is now corrected.
- These are **ranked hypotheses**, not findings. The decisive check under each surface is the falsifier — and step one of any audit here is to confirm the core contracts are genuinely **pre-2023 and unchanged** (compiler < 0.8 / no `SafeCast`, no upgrade since) before spending real time.
- Backing data: `DISC-20260909-010-candidates.json`.
