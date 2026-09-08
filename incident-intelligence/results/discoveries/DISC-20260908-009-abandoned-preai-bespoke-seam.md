# DISC-20260908-009 — The unmined seam: 116 old, abandoned, hand-rolled protocols that still hold money

## The thinking (this replaces the logic behind DISC-008)

**Copycat logic is weak.** DISC-008 organised everything around "which fresh SlowMist hack does this echo." That reasoning does not hold up: it is *rare* for a Balancer-V1-shaped bug to pay out again days later. Once an incident is public, the obvious siblings get patched, paused, or watched — the copycat window closes almost immediately. Ranking candidates by resemblance to last week's headline predicts very little.

**What actually predicts the next loss is structural neglect.** A protocol loses money when three things are true at once, and none of them has anything to do with last week's news:

1. **It still holds money.** There is something to take.
2. **Nobody is paid to watch it.** No fee revenue, dead site, deprecated — the definition of *unwatched*. No treasury means no auditor on retainer, no monitoring, no one who loses their job if it drains.
3. **The code is hand-rolled and pre-AI-era.** Written before ~2023: before EIP-712 helpers and OZ `SafeCast` were reflexive, before LLM-assisted review existed, by small teams shipping fast in a bull market. That code is *idiosyncratic* — spaghetti — and idiosyncratic code holds **novel** bugs that no scanner has a signature for.

**SOFA is the archetype, and it is worth being precise about why.** It was not hit because "automators were trending." It was hit because an old automator nobody had used in a year still held pooled capital, and its authorisation was something a human invented on the spot — a XOR-accumulated signature over a batch. That is not a known bug class; there is no detector for it. It was findable only because the code was weird, unread, and funded. And it paid **$10,800** — which is the other half of the lesson: these targets survive precisely *because* they are too small for a whitehat or an auditor to bother with, while remaining perfectly worth a scripted attacker's afternoon.

**So forks are deprioritised.** A Compound-V2 or Aave-V2 fork inherits code that has been read thousands of times; its novel-bug probability sits in whatever custom parts were bolted on, not in the inherited core. Most of DISC-008 was forks — that was the weaker half of that batch. **This batch is non-forks only**: protocols whose value-moving logic someone wrote themselves.

## The structural finding that shaped this run

Before selecting anything I measured how much of this seam I have already consumed. Of the whole DefiLlama universe: **1,655 protocols were listed pre-2023**, 1,597 survive a category filter — but **only 397 sit in the $50k–$50M band I had been using, and I had already delivered 323 of them (81%).** At that floor the seam is essentially mined out; only 74 names were left and 70 were forks.

Dropping the floor changed everything, and the reason is the SOFA number. Already-delivered barely moves as the floor falls (326 → 334) while new candidates explode — **I had never looked below $50k at all**:

| TVL floor | in band | already delivered | new | of which bespoke |
|---|---|---|---|---|
| $50k | 400 | 326 | 74 | 4 |
| $25k | 485 | 330 | 155 | 55 |
| **$10k** | **588** | **331** | **257** | **120** |
| $5k | 661 | 333 | 328 | 160 |

**SOFA was a $10,800 loss.** A $50k floor structurally excludes the exact size of target this thesis is about. So the floor here is ~$10k — "at least SOFA-sized" — and that is where the unmined abandoned money actually sits.

## Selection logic

Every row satisfies all five, and each is a checkable attribute, not a vibe: **(1)** listed pre-2023 (pre-AI-era code); **(2)** no fork lineage (hand-rolled value-moving logic); **(3)** unwatched — deprecated / dead site / little-or-no fee revenue; **(4)** still funded, $10k–$50M live TVL; **(5)** never delivered in any prior push (checked against the 2,273-name exclusion set, which includes your 888-name blocklist), and not itself one of the recent victims.

I am not chasing a count. The honest set this logic produces is **116**, tiered by how genuinely hand-rolled the money-moving code is likely to be — Tier A is the actual recommendation.


---

# Tier A — bespoke financial primitives (29)

Custom credit engines, structured-payoff vaults, synthetics, parametric settlement, hand-written bridge verifiers. These wrote their own money-moving math and nobody is paid to re-read it. **Start here.**


## Bespoke credit / lending accounting · 14

**Decisive check:** These 2022 credit protocols wrote their **own risk engine** (no Compound/Aave lineage). Read the health-factor / liquidation / withdraw path: is any fund-moving entrypoint callable without a per-user gate, and is collateral valuation bound to something an outsider can move? Bespoke credit math is where novel accounting bugs live.

| Protocol | Live TVL | Listed | Chain | Bespoke surface | Watch state | Read |
|---|---|---|---|---|---|---|
| GARD | $17k | 2022-04 | Algorand | CDP | deprecated, no revenue | The GARD Protocol offers decentralized money and fixed-yield products for Algorand users. Users can leverage t… |
| Atlendis V1 | $17k | 2022-07 | Polygon | Uncollateralized Lending | deprecated, no revenue | Atlendis is a capital-efficient DeFi lending protocol that enables crypto loans without collateral. |
| Morpho Optimizer CompoundV2 | $31k | 2022-08 | Ethereum | Lending | deprecated, no revenue | Morpho Compound is an on-chain peer-to-peer layer on top of lending pools. Rates are seamlessly improved for b… |
| BNPL Pay | $23k | 2022-08 | Ethereum | Lending | deprecated, no revenue | Collateralised and uncollateralised loans |
| RociFi V1 | $31k | 2022-09 | Polygon | Lending | deprecated, no revenue | RociFi - On-chain Credit Scoring and Capital-Efficient Lending Protocol |
| OpenSky Finance | $21k | 2022-09 | Ethereum | NFT Lending | deprecated, no revenue | The first integrated peer-to-pool and peer-to-peer NFT lending protocol built on top of aave.com |
| Argo | $22k | 2022-10 | Aptos | CDP | deprecated, no revenue | Argo is a lending protocol on Aptos that lets users collateral for minting and borrowing a dollar-pegged stabl… |
| Timeswap V1 | $44k | 2022-04 | Polygon | Lending | no revenue | Timeswap is the first oracleless lending/borrowing protocol. Timeswap enables the creation of money markets fo… |
| Credix | $36k | 2022-05 | Solana | RWA Lending | no revenue | Credix is an institutional capital markets ecosystem designed for debt financing and private credit. |
| Fringe V1 | $15k | 2022-06 | Ethereum | Lending | no revenue | A safe place for you to invest and borrow against your holdings. Fast, easily and on your own terms. |
| MMO Finance | $16k | 2022-07 | Ethereum | NFT Lending | no revenue | MMO Finance is a decentralized pool based NFT lending platform. |
| Yupana | $18k | 2022-09 | Tezos | Lending | no revenue | Yupana.Finance is an open-source, decentralized, and non-custodial lending protocol built to securely borrow a… |
| Llamalend | $22k | 2022-11 | Ethereum | NFT Lending | ~$0k/30d | Deposit NFTs and borrow ETH for small illiquid NFT collections that can't get into the main NFT lending market… |
| NFTfi | $16k | 2022-11 | Ethereum | NFT Lending | no revenue | NFT peer-to-peer lending protocol |

## Bespoke options & structured payoff · 5

**Decisive check:** A DOV / structured vault posts **pooled depositor collateral** as one side of each position. Read who may call mint/settle/exercise: is the entrypoint permissionless, and is the payoff bound to an oracle snapshot taken at open? This is the exact SOFA shape (pooled counterparty + under-gated entrypoint).

| Protocol | Live TVL | Listed | Chain | Bespoke surface | Watch state | Read |
|---|---|---|---|---|---|---|
| Olive | $50k | 2022-04 | Ethereum | Options Vault | deprecated, no revenue | Olive is a multi-chain protocol that combines composability with structured products to amplify yields without… |
| Predy V3.2 | $25k | 2022-04 | Arbitrum | Derivatives | deprecated, ~$1k/30d | Predy V3.2 allows traders to utilize portfolio margin for Squart and ETH perpetual trading while simplifying t… |
| Y2K V1 | $42k | 2022-12 | Arbitrum | Derivatives | deprecated, ~$0k/30d | Y2K Finance is a suite of structured products designed for exotic peg derivatives, that will allow market part… |
| Vovo Finance | $43k | 2022-07 | Arbitrum | Yield | no revenue | Structured products with various risk-returns and payoff structures through packaged financial instruments |
| Pods Yield | $30k | 2022-07 | Ethereum | Yield | no revenue | Change the way you earn. Tap into low-risk protected vaults to make more with less overhead. Starting with ETH… |

## Bespoke vault / share math · 3

**Decisive check:** Bespoke share pricing. Read how mint()/burn() value the position (spot vs TWAP) and who may trigger rebalance — an unguarded share valuation is drainable with a flash-skew.

| Protocol | Live TVL | Listed | Chain | Bespoke surface | Watch state | Read |
|---|---|---|---|---|---|---|
| Universe Finance | $26k | 2021-10 | Ethereum | Liquidity Manager | deprecated, no revenue | Universe Finance is a Uniswap V3 liquidity management platform based on risk grading and quantitative strategi… |
| Hedgehog | $27k | 2022-12 | Ethereum | Liquidity Manager | deprecated, no revenue | An automated strategy that earns ETH, by providing liquidity for the Uniswap V3 and hedging its impermanent lo… |
| Aperture LM | $13k | 2022-03 | Avalanche | Liquidity Manager | no revenue | Cross-chain investment ecosystem with a community-driven marketplace for strategies. All your DeFi needs taken… |

## Bespoke parametric & prediction settlement · 2

**Decisive check:** Bespoke parametric / prediction settlement. Read who can propose and finalize an outcome, and whether payout eligibility is tied to a snapshot taken *before* the proposal.

| Protocol | Live TVL | Listed | Chain | Bespoke surface | Watch state | Read |
|---|---|---|---|---|---|---|
| Polkamarkets | $14k | 2021-12 | Ethereum | Prediction Market | no revenue | Polkamarkets is an Autonomous Prediction Market Protocol built for cross-chain information exchange and tradin… |
| Risk Harbor | $38k | 2022-03 | Arbitrum | Insurance | no revenue | Risk Harbor is a risk management marketplace for decentralized finance (DeFi) that utilizes a completely autom… |

## Bespoke derivatives engine · 2

**Decisive check:** Hand-rolled margin/funding/PnL engine. Read the settlement and withdrawal path: can a dormant or thin market be self-traded into realized PnL that is withdrawable before it is socialized?

| Protocol | Live TVL | Listed | Chain | Bespoke surface | Watch state | Read |
|---|---|---|---|---|---|---|
| UniDex Perp | $30k | 2022-06 | Optimism | Derivatives | deprecated, ~$411k/30d | UniDex is a DeFi aggregation layer making interesting trading products such as leverage trading aggregation, d… |
| JOJO | $25k | 2022-11 | Base | Derivatives | ~$0k/30d | JOJO is a decentralized perpetual contract trading platform that uses an off-chain matching and on-chain settl… |

## Bespoke bridge verification · 2

**Decisive check:** A bespoke bridge wrote its **own verifier**. Read whether every mint/release is bound 1:1 to a verified, replay-protected remote burn, and how many independent signers are actually required.

| Protocol | Live TVL | Listed | Chain | Bespoke surface | Watch state | Read |
|---|---|---|---|---|---|---|
| DotOracle | $41k | 2022-08 | Ethereum | Bridge | deprecated, no revenue | DotOracle is a real-time decentralized Oracle and Cross-chain bridge supported by multi-chains such as Polkado… |
| EverRise | $30k | 2022-01 | Binance | Cross Chain Bridge | no revenue | EverRise is a blockchain technology company that offers bridging and security solutions across blockchains thr… |

## Bespoke synthetic / stablecoin math · 1

**Decisive check:** Hand-rolled mint/burn against a collateral ratio. Read the debt accounting: can the collateral ratio or the oracle be moved cheaply, and is the mint path gated? Bespoke synths carry their own (often unreviewed) solvency math.

| Protocol | Live TVL | Listed | Chain | Bespoke surface | Watch state | Read |
|---|---|---|---|---|---|---|
| Crafting Finance | $12k | 2022-01 | Aurora | Synthetics | no revenue | Crafting is a protocol for forging and trading Rafts, which are smart synthetic assets |

---

# Tier B — bespoke vault / reward math (45)

2021–22 yield and staking protocols with their own vault-share and reward accounting. Honest caveat: many of this cohort are MasterChef-descended even where no fork lineage is recorded, so the inherited-code argument partly applies — hence Tier B, not A. The custom parts (auto-compounding, boost, migration, reward resets) are still hand-written.

**Decisive check:** Bespoke share pricing. Read how mint()/burn() value the position (spot vs TWAP) and who may trigger rebalance — an unguarded share valuation is drainable with a flash-skew. Also: Bespoke reward/claim state machine. Read whether a claimed reward can be reset and re-claimed (a tiny or zero-effective deposit re-arming the payout), and whether the reward pool is shared.

| Protocol | Live TVL | Listed | Chain | Bespoke surface | Watch state |
|---|---|---|---|---|---|
| CougarSwap | $46k | 2021-11 | Cronos | Yield | deprecated, no revenue |
| Pacoca | $29k | 2021-11 | Binance | Yield | deprecated, no revenue |
| Ottopia | $25k | 2021-11 | Polygon | Yield | deprecated, no revenue |
| Golff Protocol | $18k | 2021-11 | Ethereum | Yield | deprecated, no revenue |
| PolyYeld Finance | $17k | 2021-11 | Polygon | Yield | deprecated, no revenue |
| MarshmallowDeFi | $15k | 2021-11 | Binance | Yield | deprecated, no revenue |
| MFinance | $16k | 2021-12 | Ethereum | Yield | deprecated, no revenue |
| Salem Finance | $15k | 2021-12 | Polygon | Yield | deprecated, no revenue |
| Buffaloswap | $12k | 2021-12 | Binance | Yield | deprecated, no revenue |
| PolyShield | $11k | 2021-12 | Polygon | Yield | deprecated, no revenue |
| 0xDAO | $42k | 2022-01 | Fantom | Yield | deprecated, no revenue |
| PearZap | $34k | 2022-01 | Binance | Yield | deprecated, no revenue |
| Mover | $24k | 2022-01 | Ethereum | Yield | deprecated, no revenue |
| BooFinance | $17k | 2022-01 | Avalanche | Yield | deprecated, no revenue |
| Waterfall BSC | $32k | 2022-02 | Binance | Yield | deprecated, no revenue |
| Croblanc | $16k | 2022-02 | Cronos | Yield | deprecated, no revenue |
| GoblinGold | $25k | 2022-03 | Solana | Yield | deprecated, no revenue |
| Vector Finance | $23k | 2022-03 | Avalanche | Yield | deprecated, no revenue |
| Waterfall DeFi | $20k | 2022-04 | Binance | Yield Aggregator | deprecated, no revenue |
| Bolide | $15k | 2022-04 | Binance | Yield Aggregator | deprecated, no revenue |
| Diamond Protocol V1 | $14k | 2022-05 | Arbitrum | Yield | deprecated, no revenue |
| OliveDAO | $11k | 2022-05 | Polygon | Yield | deprecated, no revenue |
| DarkAuto | $20k | 2022-09 | Cronos | Yield Aggregator | deprecated, no revenue |
| Eversol | $15k | 2022-09 | Solana | Liquid Staking | deprecated, no revenue |
| HedgeFarm | $36k | 2022-10 | Avalanche | Yield | deprecated, no revenue |
| Ditto | $32k | 2022-10 | Aptos | Liquid Staking | deprecated, no revenue |
| STRX Finance | $19k | 2022-11 | Tron | Liquid Staking | deprecated, no revenue |
| Bank of Chain | $15k | 2022-11 | Ethereum | Yield Aggregator | deprecated, no revenue |
| Brahma Vaults (Sunset) | $23k | 2021-11 | Ethereum | Yield | no revenue |
| DungeonSwap | $10k | 2021-11 | Binance | Yield | no revenue |
| Thoreum Finance | $42k | 2021-12 | Binance | Yield | no revenue |
| Bent Finance | $27k | 2022-01 | Ethereum | Yield | no revenue |
| Kalmy App | $36k | 2022-02 | Binance | Yield | no revenue |
| GoodDollar | $26k | 2022-02 | Ethereum | Yield | no revenue |
| Solidex | $20k | 2022-02 | Fantom | Yield Aggregator | no revenue |
| Invariant | $31k | 2022-05 | Solana | Dexs | ~$0k/30d |
| Yelay V1 | $12k | 2022-05 | Arbitrum | Yield Aggregator | no revenue |
| DexPad | $27k | 2022-06 | Cronos | Launchpad | no revenue |
| Timeless Finance | $15k | 2022-07 | Ethereum | Yield | no revenue |
| KordFi | $22k | 2022-08 | Tezos | Yield | no revenue |
| Matter Defi | $20k | 2022-08 | Tezos | Yield | no revenue |
| Sense | $30k | 2022-09 | Ethereum | Yield | no revenue |
| Kava Boost | $22k | 2022-11 | Kava | Farm | no revenue |
| SandClock | $24k | 2022-12 | Ethereum | Yield | no revenue |
| Proteo Defi | $20k | 2022-12 | Elrond | Farm | no revenue |

---

# Tier C — stranded, previously-hit, or thin-chain (42)

Listed for completeness with an honest discount: these are either on effectively stranded chains (Terra, EOS, Mixin, Sora, Pokt…), or the protocol has already been exploited once (Platypus, Euler V1, Cykura, Poof Cash…), or the bespoke surface is a plain AMM. **Verify the money is actually reachable before spending time here.**

| Protocol | Live TVL | Listed | Chain | Bespoke surface | Watch state |
|---|---|---|---|---|---|
| Poof Cash | $26k | 2021-10 | Celo | Lending | deprecated, no revenue |
| Synthetify | $26k | 2021-10 | Solana | Synthetics | deprecated, no revenue |
| Platypus Finance | $29k | 2021-11 | Avalanche | Dexs | deprecated, no revenue |
| Aldrin | $26k | 2021-11 | Solana | Dexs | deprecated, no revenue |
| BeGlobal Finance | $18k | 2021-11 | Binance | Dexs | deprecated, no revenue |
| Loop Finance | $10k | 2021-11 | Terra | Dexs | deprecated, no revenue |
| Mobius Finance | $41k | 2021-12 | Polygon | Synthetics | deprecated, no revenue |
| RobiniaSwap | $23k | 2021-12 | Binance | Dexs | deprecated, no revenue |
| Cykura | $15k | 2021-12 | Solana | Dexs | deprecated, no revenue |
| Oin Finance | $36k | 2022-01 | Ethereum | Algo-Stables | deprecated, no revenue |
| ExinSwap | $22k | 2022-01 | Mixin | Dexs | deprecated, no revenue |
| Penguin | $21k | 2022-03 | Solana | Dexs | deprecated, no revenue |
| DolphinSwap | $20k | 2022-03 | EOS | Dexs | deprecated, no revenue |
| HaloFi | $23k | 2022-04 | Polygon | Services | deprecated, no revenue |
| ThunderPOKT | $16k | 2022-04 | Pokt | Liquid Staking | deprecated, no revenue |
| Duet Protocol | $39k | 2022-05 | Arbitrum | Synthetics | deprecated, no revenue |
| Phuture | $36k | 2022-06 | Avalanche | Indexes | deprecated, no revenue |
| Stake.ly | $14k | 2022-09 | Klaytn | Liquid Staking | deprecated, no revenue |
| Powaa Protocol | $13k | 2022-09 | Ethereum | Services | deprecated, no revenue |
| ION DAO | $33k | 2022-10 | Osmosis | Synthetics | deprecated, no revenue |
| AnchorSwap | $44k | 2021-10 | Binance | Dexs | no revenue |
| Polkaswap | $18k | 2021-10 | Sora | Dexs | no revenue |
| Unilend V1 | $10k | 2021-11 | Polygon | Lending | no revenue |
| SpicySwap | $40k | 2021-12 | Tezos | Dexs | no revenue |
| SuperFarm | $31k | 2021-12 | Ethereum | Services | no revenue |
| MonoX | $11k | 2021-12 | Polygon | Dexs | no revenue |
| CyberTime | $45k | 2022-01 | Binance | Services | no revenue |
| Euler V1 | $28k | 2022-01 | Ethereum | Lending | no revenue |
| AtomicHub | $44k | 2022-02 | Wax | Dexs | no revenue |
| WOWswap | $43k | 2022-02 | Binance | Dexs | no revenue |
| Solidly | $13k | 2022-02 | Fantom | Dexs | no revenue |
| Antimatter | $13k | 2022-02 | Avalanche | Options | no revenue |
| Humble Defi | $37k | 2022-04 | Voi Network | Dexs | no revenue |
| Foodcourt | $45k | 2022-05 | Binance | Dexs | no revenue |
| Oswap AMM | $28k | 2022-05 | Obyte | Dexs | no revenue |
| BlockNG | $18k | 2022-05 | smartBCH | Dexs | no revenue |
| Spin Spot | $41k | 2022-06 | Near | Dexs | no revenue |
| sKCS | $26k | 2022-07 | Kucoin | Liquid Staking | no revenue |
| Algem | $23k | 2022-07 | Astar | Liquid Staking | no revenue |
| Kintsugi | $10k | 2022-07 | Kintsugi | Cross Chain Bridge | no revenue |
| Frigg.eco | $183k | 2022-10 | Ethereum | RWA | no revenue |
| Aptoswap | $19k | 2022-10 | Aptos | Dexs | no revenue |

---

## Honesty & dedup

- These are **hypotheses ranked by structural exposure**, not findings. Nothing here is a confirmed vulnerability; the decisive check under each surface is the falsifier.
- All 116 names are new: checked against `results/discoveries/_exclusion_set.json` (2,273 names incl. the 888-name blocklist) and folded in with this push.
- TVL/revenue are live DefiLlama reads taken today; for a deprecated protocol, confirm the balance is real and reachable at head before acting.
- The fork exclusion relies on DefiLlama/enrichment lineage data, which is imperfect — an unlabelled fork can slip into Tier B. That is the main known weakness of this cut, and it is why Tier B carries the MasterChef caveat.
- Backing data: `DISC-20260908-009-candidates.json`.
