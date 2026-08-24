# Custody exposure — who can replace the code

> **This is not a vulnerability report.** Nothing here says any protocol is exploitable, and nothing here is an attack instruction. Every value below is public chain state, read with `eth_call` and `eth_getCode`. A single-key authority is a *design posture*, not a defect: plenty of small teams run one deliberately. It is listed because it is the cheapest thing in DeFi to fix and the most expensive to get wrong.

**Why this is scored separately from everything else in this run.** An off-chain key compromise is an excluded root cause under the inclusion gate (§6), so it may not inflate a code-defect likelihood score. It is also the amplifier that decides what a code defect *costs*. Keeping the two apart is the only way to avoid one quietly contaminating the other.

## Method

For every address probed, the ERC-1967 admin slot and `owner()` were read, then the authority chain was walked up to three hops — a proxy's admin is usually an OpenZeppelin `ProxyAdmin` whose own `owner()` is the real authority, which is in turn often a Safe or a timelock. The **terminal** authority is fingerprinted by the functions it answers: `getThreshold()` + `getOwners()` for a Safe, `getMinDelay()` or `delay()`+`GRACE_PERIOD()` for a timelock, `votingDelay()` for a governor, zero code size for an externally-owned account. A protocol is reported at its **weakest** terminal authority, because that is the one a defender has to plan around.

## Distribution across 483 in-band protocols with a readable authority

| Terminal authority | Protocols | Meaning |
|---|---:|---|
| `UNKNOWN_CONTRACT` | 191 | a contract this run could not fingerprint |
| `EOA_SINGLE_KEY` | 187 | one externally-owned account — a single private key |
| `SAFE_M_OF_N` | 81 | a Safe requiring several signatures |
| `TIMELOCK` | 18 | a timelock with a real delay |
| `SAFE_1_OF_N` | 4 | a Safe with threshold 1 — any one of its signers acts alone |
| `GOVERNOR` | 2 | an on-chain governor |

## Single-signature authority over an upgradeable deployment

The sharpest subset, and the only one that can actually replace code: the chain walked here starts at an **ERC-1967 admin slot**, not at a plain `owner()`, and it terminates in one key or one signature. Total at stake below: **$32,344,207** across **13** protocols.

| # | Protocol | Category | Value at risk | Terminal authority | Hops | Chain |
|---:|---|---|---:|---|---:|---|
| 1 | [Cronos zkEVM Bridge](https://defillama.com/protocol/cronos-zkevm-bridge) | Canonical Bridge | $20,070,907 | `EOA_SINGLE_KEY` | 1 | ethereum |
| 2 | [Harmonix Finance](https://defillama.com/protocol/harmonix-finance) | Yield | $6,493,620 | `EOA_SINGLE_KEY` | 1 | arbitrum |
| 3 | [Planet Farm](https://defillama.com/protocol/planet-farm) | Yield | $1,657,781 | `EOA_SINGLE_KEY` | 0 | bsc |
| 4 | [LendFlare](https://defillama.com/protocol/lendflare) | Lending | $1,171,712 | `EOA_SINGLE_KEY` | 2 | ethereum |
| 5 | [SOFA.org](https://defillama.com/protocol/sofa.org) | Options | $1,046,794 | `EOA_SINGLE_KEY` | 0 | ethereum |
| 6 | [Altitude.Fi](https://defillama.com/protocol/altitude.fi) | Lending | $520,834 | `EOA_SINGLE_KEY` | 0 | ethereum |
| 7 | [SingularityDAO](https://defillama.com/protocol/singularitydao) | Yield | $436,691 | `EOA_SINGLE_KEY` | 0 | bsc |
| 8 | [Orion Pools](https://defillama.com/protocol/orion-pools) | Dexs | $274,685 | `EOA_SINGLE_KEY` | 0 | bsc |
| 9 | [Iron Bank](https://defillama.com/protocol/iron-bank) | Lending | $216,657 | `EOA_SINGLE_KEY` | 1 | ethereum |
| 10 | [SmartCredit](https://defillama.com/protocol/smartcredit) | Lending | $204,900 | `EOA_SINGLE_KEY` | 1 | ethereum |
| 11 | [De1](https://defillama.com/protocol/de1) | DEX Aggregator | $130,275 | `EOA_SINGLE_KEY` | 0 | bsc |
| 12 | [Velo Finance](https://defillama.com/protocol/velo-finance) | Dexs | $67,584 | `EOA_SINGLE_KEY` | 2 | bsc |
| 13 | [Cook Finance](https://defillama.com/protocol/cook-finance) | Indexes | $51,767 | `EOA_SINGLE_KEY` | 0 | ethereum |

## Single-signature *privileged role*, no upgrade path proven

A weaker and much noisier claim than the table above, kept separate for that reason: somewhere in the protocol a single key answers `owner()` — on a pool, an oracle setter, a fee recipient, a treasury — but no ERC-1967 admin chain terminating in that key was proven, so this is a privileged role, **not** an upgrade path. The money column is the protocol's whole TVL, and **most of it is usually not behind this key**. Read it as a pointer to a contract worth opening, nothing more. 175 protocols.

| # | Protocol | Protocol TVL (not all behind this key) | Weakest terminal authority | Proxy present |
|---:|---|---:|---|---|
| 1 | [Piku Finance](https://defillama.com/protocol/piku-finance) | $29,352,222 | `EOA_SINGLE_KEY` | yes |
| 2 | [Clearpool TPOOL](https://defillama.com/protocol/clearpool-tpool) | $20,534,218 | `EOA_SINGLE_KEY` | no |
| 3 | [Belt Finance](https://defillama.com/protocol/belt-finance) | $13,098,699 | `EOA_SINGLE_KEY` | no |
| 4 | [FlokiFi Locker](https://defillama.com/protocol/flokifi-locker) | $11,753,115 | `EOA_SINGLE_KEY` | no |
| 5 | [Equilibria](https://defillama.com/protocol/equilibria) | $11,256,299 | `EOA_SINGLE_KEY` | yes |
| 6 | [Stargate V1](https://defillama.com/protocol/stargate-v1) | $10,725,483 | `EOA_SINGLE_KEY` | no |
| 7 | [FstSwap](https://defillama.com/protocol/fstswap) | $10,110,093 | `EOA_SINGLE_KEY` | no |
| 8 | [MUX Perps](https://defillama.com/protocol/mux-perps) | $9,913,739 | `EOA_SINGLE_KEY` | no |
| 9 | [Bancor V2.1](https://defillama.com/protocol/bancor-v2.1) | $9,827,540 | `EOA_SINGLE_KEY` | no |
| 10 | [Antarctic](https://defillama.com/protocol/antarctic) | $9,494,061 | `EOA_SINGLE_KEY` | yes |
| 11 | [ApeSwap AMM](https://defillama.com/protocol/apeswap-amm) | $9,475,642 | `EOA_SINGLE_KEY` | no |
| 12 | [Symbiosis](https://defillama.com/protocol/symbiosis) | $8,735,933 | `EOA_SINGLE_KEY` | no |
| 13 | [Autofarm](https://defillama.com/protocol/autofarm) | $7,773,487 | `EOA_SINGLE_KEY` | no |
| 14 | [TurboFlow Perps](https://defillama.com/protocol/turboflow-perps) | $5,878,191 | `EOA_SINGLE_KEY` | no |
| 15 | [Biswap V2](https://defillama.com/protocol/biswap-v2) | $5,826,090 | `EOA_SINGLE_KEY` | no |
| 16 | [BSCSwap](https://defillama.com/protocol/bscswap) | $5,311,830 | `EOA_SINGLE_KEY` | no |
| 17 | [Wing Finance](https://defillama.com/protocol/wing-finance) | $5,173,532 | `EOA_SINGLE_KEY` | no |
| 18 | [BiFi](https://defillama.com/protocol/bifi) | $4,905,718 | `EOA_SINGLE_KEY` | no |
| 19 | [BabyDogeSwap](https://defillama.com/protocol/babydogeswap) | $3,978,667 | `EOA_SINGLE_KEY` | no |
| 20 | [BakerySwap](https://defillama.com/protocol/bakeryswap) | $3,913,482 | `EOA_SINGLE_KEY` | no |
| 21 | [ZeroLend Lending](https://defillama.com/protocol/zerolend-lending) | $3,903,136 | `EOA_SINGLE_KEY` | yes |
| 22 | [Bunny](https://defillama.com/protocol/bunny) | $3,597,277 | `EOA_SINGLE_KEY` | yes |
| 23 | [Dnax](https://defillama.com/protocol/dnax) | $3,302,927 | `EOA_SINGLE_KEY` | no |
| 24 | [Kinza Finance](https://defillama.com/protocol/kinza-finance) | $3,277,468 | `EOA_SINGLE_KEY` | yes |
| 25 | [Venus Flux](https://defillama.com/protocol/venus-flux) | $3,267,620 | `EOA_SINGLE_KEY` | no |
| 26 | [SynFutures V3](https://defillama.com/protocol/synfutures-v3) | $3,109,274 | `EOA_SINGLE_KEY` | no |
| 27 | [RateX DEX](https://defillama.com/protocol/ratex-dex) | $2,899,456 | `EOA_SINGLE_KEY` | yes |
| 28 | [QiDao](https://defillama.com/protocol/qidao) | $2,708,451 | `EOA_SINGLE_KEY` | no |
| 29 | [EmpireDEX](https://defillama.com/protocol/empiredex) | $2,676,867 | `EOA_SINGLE_KEY` | no |
| 30 | [Rank Trading](https://defillama.com/protocol/rank-trading) | $2,604,526 | `EOA_SINGLE_KEY` | no |
| 31 | [Gnosis Protocol v1](https://defillama.com/protocol/gnosis-protocol-v1) | $2,429,436 | `EOA_SINGLE_KEY` | yes |
| 32 | [ioTube](https://defillama.com/protocol/iotube) | $2,395,598 | `EOA_SINGLE_KEY` | no |
| 33 | [Singular Farm](https://defillama.com/protocol/singular-farm) | $2,079,500 | `EOA_SINGLE_KEY` | no |
| 34 | [Peapods Finance](https://defillama.com/protocol/peapods-finance) | $2,030,459 | `EOA_SINGLE_KEY` | yes |
| 35 | [Angle](https://defillama.com/protocol/angle) | $2,008,559 | `EOA_SINGLE_KEY` | yes |
| 36 | [Gro](https://defillama.com/protocol/gro) | $1,783,882 | `EOA_SINGLE_KEY` | no |
| 37 | [DeFIL](https://defillama.com/protocol/defil) | $1,759,083 | `EOA_SINGLE_KEY` | no |
| 38 | [iZiSwap](https://defillama.com/protocol/iziswap) | $1,662,324 | `EOA_SINGLE_KEY` | no |
| 39 | [KaoyaSwap](https://defillama.com/protocol/kaoyaswap) | $1,527,588 | `EOA_SINGLE_KEY` | no |
| 40 | [BabySwap](https://defillama.com/protocol/babyswap) | $1,515,281 | `EOA_SINGLE_KEY` | no |
| 41 | [Arrakis V1](https://defillama.com/protocol/arrakis-v1) | $1,494,413 | `EOA_SINGLE_KEY` | no |
| 42 | [Silo V1](https://defillama.com/protocol/silo-v1) | $1,453,111 | `EOA_SINGLE_KEY` | no |
| 43 | [Interest Protocol](https://defillama.com/protocol/interest-protocol) | $1,448,816 | `EOA_SINGLE_KEY` | yes |
| 44 | [THENA V1](https://defillama.com/protocol/thena-v1) | $1,433,455 | `EOA_SINGLE_KEY` | no |
| 45 | [MDEX](https://defillama.com/protocol/mdex) | $1,408,197 | `EOA_SINGLE_KEY` | no |
| 46 | [Unchain X](https://defillama.com/protocol/unchain-x) | $1,244,238 | `EOA_SINGLE_KEY` | no |
| 47 | [Overtime](https://defillama.com/protocol/overtime) | $1,159,711 | `EOA_SINGLE_KEY` | no |
| 48 | [9inch V2](https://defillama.com/protocol/9inch-v2) | $1,049,596 | `EOA_SINGLE_KEY` | no |
| 49 | [Allbridge Classic](https://defillama.com/protocol/allbridge-classic) | $1,044,112 | `EOA_SINGLE_KEY` | no |
| 50 | [dForce Lending](https://defillama.com/protocol/dforce-lending) | $1,027,387 | `EOA_SINGLE_KEY` | yes |
| 51 | [THENA INTEGRAL](https://defillama.com/protocol/thena-integral) | $1,004,471 | `EOA_SINGLE_KEY` | no |
| 52 | [Etherfuse](https://defillama.com/protocol/etherfuse) | $977,586 | `EOA_SINGLE_KEY` | yes |
| 53 | [GMD Protocol](https://defillama.com/protocol/gmd-protocol) | $971,646 | `EOA_SINGLE_KEY` | no |
| 54 | [ApeRocket](https://defillama.com/protocol/aperocket) | $967,273 | `EOA_SINGLE_KEY` | yes |
| 55 | [Solo Top](https://defillama.com/protocol/solo-top) | $928,246 | `EOA_SINGLE_KEY` | yes |
| 56 | [MORE Vaults](https://defillama.com/protocol/more-vaults) | $822,973 | `EOA_SINGLE_KEY` | yes |
| 57 | [Cover Protocol](https://defillama.com/protocol/cover-protocol) | $808,743 | `EOA_SINGLE_KEY` | no |
| 58 | [Topaz CL](https://defillama.com/protocol/topaz-cl) | $782,349 | `EOA_SINGLE_KEY` | no |
| 59 | [VenomBridge](https://defillama.com/protocol/venombridge) | $743,145 | `EOA_SINGLE_KEY` | yes |
| 60 | [THENA FUSION](https://defillama.com/protocol/thena-fusion) | $740,733 | `EOA_SINGLE_KEY` | no |

## What to do with this

For any protocol above, the defensive ask is small, specific and free: move the terminal authority behind a multi-signature account with a threshold above one, and put a non-zero delay in front of upgrades so that a replacement can be seen before it lands. That is a configuration change, not a rewrite, and it is the kind of report a small team will usually act on.

## Limits of this measurement

- **Worked example of the second table's limitation.** Curve DEX resolves to `EOA_SINGLE_KEY` under weakest-link semantics, because one pool among many answers `owner()` with an externally-owned account. Curve's actual protocol authority is DAO-governed and nothing here contradicts that. The protocol-wide TVL figure is therefore not the amount behind that key, which is why the second table is restricted to in-band protocols and its money column is labelled as protocol TVL. The first table does not have this problem: it only counts chains that begin at an ERC-1967 admin slot.
- Only addresses this run already probed were walked. A privileged role held by an address never surfaced in a TVL adapter is invisible here.
- `UNKNOWN_CONTRACT` means the fingerprint did not match, not that the authority is safe. Some are custom governance; some are Safes behind a non-standard proxy.
- A Safe's threshold is read now; signer sets change.
- Role-based access (`AccessControl`) is not enumerated — a protocol reading as `NONE_FOUND` may still have privileged roles granted to single keys.
- Posture is read today, so a team that hardened after an incident reads as hardened. That biases every measurement here toward understating exposure, never overstating it.
