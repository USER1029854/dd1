# Candidates — Ranking A — priority (likelihood × actionability)

> **Discovery stage.** This file asserts no defect in any protocol named below. Each entry is a *review candidate*: named evidence matches a family's prerequisites, named evidence is unknown, and a named guard would falsify it. Verify on a local or pinned fork before concluding anything.

**Scoring is now validated, not asserted.** Attack-surface weights were fitted on 2022-24 hacks and tested against 2025-26 hacks: 95 protocols unseen during fitting, median victim landing at the **78.7th percentile**, **59%** of future victims in the model's top quartile — a **×2.36 lift** over chance.

**Likelihood and actionability are kept apart.** Bigger protocols are *more* likely to be attacked (`tvl_over_5m` carries lift ×1.75) and *less* actionable for an independent reviewer. Folding those together is what produced earlier rankings full of protocols you cannot help. PRIORITY multiplies them explicitly so you can see both halves.

**Exposure age beat every other addition, and it contradicts the obvious intuition.** Protocols under a year old carry lift ×1.87; protocols over three years old carry ×0.33. It is not the abandoned deployments that get hit — it is the new ones. Ablation attributes the whole out-of-sample gain to this one group (×2.19 → ×2.32).

**Custody posture was measured and then deliberately dropped from the score.** A single-key upgrade authority does not predict a code defect (measured ×0.98 over the full window; adding it moved out-of-sample lift ×2.19 → ×2.15, i.e. slightly worse). That is the expected answer, since key compromise is an excluded root cause here — so it is reported on its own in `results/upgrade_authority_exposure.md`, where 23 protocols holding $56.4M have an ERC-1967 upgrade authority terminating in a single key. Often the cheapest thing on this whole list to fix.

**A finding that overturned the earlier model:** measured against survivors only, neglect looked protective. It is not — 62.5% of victims that fell below $50k had no audit, versus 20.9% of those still listed. The population was censored by the very outcome being predicted. Weights are now fitted against the full listed universe.

### At a glance

| | |
|---|---:|
| Candidates | 53 |
| Previously hacked | 4 |
| Repeat victims (2+ recorded hacks) | 1 |
| Median value at risk | $795,077 |
| Total value at risk | $203,968,128 |
| At L4 guard review | 53 |
| Distinct mechanism families | 10 |
| Previously delivered (withheld from this list) | 596 |

### The size of this list is set by evidence, not by a round number

Every fresh protocol reaching **`L4_GUARD_REVIEW`** is here — 53 of them — rather than the ranking being truncated at some count. A count is an arbitrary cut through a ranking; an evidence level is a statement about how deeply each entry was actually read. At this level the protocol's deployed source was fetched, proxies were followed to their implementations, the family's documented preconditions were evaluated against that source, and its decisive guards were searched for and not found in the reviewed path.

### Every protocol here is one you have not been given before

A candidate list is a queue of work, not a leaderboard. **596 protocols that survive screening were withheld from this run because earlier runs already handed them over** across 9 previous deliveries. They are not resolved and not ruled out — they were already given to you, so repeating them would hand you no new work.

| Previous delivery | Protocols handed over |
|---|---:|
| `7d49c12` — Add six-month DeFi incident intelligence and DefiLlama audit pri | 24 |
| `ccb5273` — Expand the screen to a $50k floor with a condition layer and dep | 49 |
| `3bc30a7` — Re-target the screen at what actually gets hacked, in a reviewab | 72 |
| `2ce88d1` — Validate the ranking model and measure custody exposure separate | 111 |
| `5a3468f` — Remove leftovers from earlier iterations of this run | 111 |
| `7e319ee` — Extend beyond EVM: verify Maya at source, kill the THORChain lea | 108 |
| `1ad898f` — Never hand over the same protocol twice | 130 |
| `6e7df7a` — New run: 60 fresh candidates, and chain priority measured instea | 117 |
| `693e2ed` — Screen the families that actually cause the loss, and size the l | 163 |

The full ledger is `protocols/delivered_ledger.json`, reconstructed from git history rather than from anything remembered between runs. Every withheld protocol still appears in `candidates_all.csv` with `previously_delivered=YES` and the run that delivered it, so nothing is hidden — it is only kept out of the queue.

<details><summary>The 596 withheld protocols</summary>

`3f-mutual`, `88mph`, `8lends`, `9inch-v2`, `aarna-protocol`, `aave-v1`, `aave-v3`, `aavegotchi`, `abracadabra-spell`, `abstradex`, `accountable`, `accumulated-finance-liquid-staking`, `across`, `adi-bridge`, `aegis-markets`, `aerodrome-ignition`, `agave`, `airpuff`, `ajna-v1`, `ajna-v2`, `alchemist`, `alcum`, `almanak`, `aloe`, `alongside`, `alphax`, `alphix`, `altitude.fi`, `alvara`, `ammalgam-dlex`, `amphor`, `ample`, `angle`, `angstrom`, `ankr`, `antarctic`, `ante-finance`, `antfarm-finance`, `anthias-labs`, `anvil`, `anzen-v2`, `apechain-bridge`, `aperocket`, `apeswap-amm`, `apeswap-lending`, `apex-pro`, `apostro`, `apy-finance`, `arbinyan`, `arbitrum-nova-bridge`, `arca-labs-arcoin`, `arcade.xyz`, `arcadia-v2`, `arch`, `asseto-cash+`, `astaria-v2`, `asymmetry-usdaf`, `aura`, `autopilot`, `axelar-cross-chain`, `b-lucky`, `b.protocol`, `b.protocol-curator`, `babydoge-bridge`, `badger-dao`, `bakerfi`, `balancer-v1`, `balancer-v2`, `balancer-v3`, `bancor-v2.1`, `bancor-v3`, `basalt-vault`, `base-dollar`, `basedbid`, `baseline-protocol`, `basis-cash`, `bearnfi`, `bella-protocol`, `belt-finance`, `bifi`, `bima-cdp`, `biswap-v3`, `bitstable-finance`, `blackwing`, `block-analitica`, `blur-bids`, `bob-bridge`, `bob-fusion`, `boba-bridge`, `bond-protocol`, `bondlink-finance`, `boringdao`, `bridge-mutual`, `bridgers`, `btcd`, `bundles`, `bunicorn`, `bunni-v2`, `bunny`, `burgerswap`, `byzanlink-rwa-markets`, `cache.gold`, `cakepie`, `cana-holdings-california-carbon-credits`, `capyfi`, `cat-in-a-box`, `caviar-v1`, `cbridge`, `cega-v1`, `cega-v2`, `chainport`, `chamber-vaults`, `charm-finance-v1`, `charm-finance-v2`, `citrea-bridge`, `clearpool-lending`, `clipper`, `clovis`, `conduit-bridge`, `conic-finance`, `contango-v1`, `convex-finance`, `cook-finance`, `cove-boosties`, `cover-protocol`, `cozy-v1`, `cream-lending`, `creamswap`, `credit-coop`, `cronos-zkevm-bridge`, `crosschain-bridge`, `cryptex-v1`, `csigma-finance`, `cub-finance`, `curve-dex`, `curve-llamalend`, `cvault-finance`, `cvi-finance`, `cyclone`, `cytonic-airdrop-campaign`, `dango-bridge`, `ddex`, `de1`, `debridge`, `decentralized-euro`, `defi-franc`, `defibox`, `defil`, `degenprime`, `deltaprime`, `delv-yield`, `demeter`, `deri-protocol`, `derivadex`, `derive-v1`, `dexfi-aggregator`, `dforce-lending`, `dfx-v2`, `dodo-amm`, `domani-protocol`, `dooar-v2`, `dopple-finance`, `dsf.finance`, `dtrinity-dlend`, `dtrinity-dusd`, `dydx-v3`, `dyson`, `ea-finance`, `easedefi.org`, `ekubo`, `electra`, `elfi-protocol`, `elk`, `elysium-bridge`, `enosys-bridge`, `equilibria`, `eth-strategy`, `ether.fi-liquid`, `etherflip`, `etherfuse`, `everything`, `exactly`, `extra-finance-leverage-farming`, `extra-finance-vaults`, `ezmanager`, `ezmoney`, `factor-leverage-vault`, `felix-usdhl`, `finext-finance`, `finnexus`, `fira`, `flat-money-v2`, `flexa`, `flux-finance`, `flying-tulip-ftusd`, `flying-tulip-lend`, `fortunafi`, `fractional-art`, `frax-fpi`, `frax-swap`, `fraxlend`, `fuel-bridge`, `fuji-v1`, `fungify`, `fyde-protocol`, `gaib`, `gammaswap-open-interest`, `gauntlet`, `gearbox`, `geyser`, `gmd-protocol`, `gnosis-protocol-v1`, `goldsand-by-inshallah`, `gondi-v3`, `goose`, `goplus-locker-v2`, `governor-dao`, `granary-finance`, `gravita-protocol`, `gravity-bridge`, `gremlix`, `grizzlyfi-hives`, `gro`, `gudchain`, `guru-network-classic`, `gyroscope-protocol`, `halodao`, `harvest-finance`, `hashflow`, `hats.v2`, `hidden-hand`, `hlp0`, `hop-protocol`, `horizon-protocol`, `hundred-finance`, `hunny-finance`, `hydt-protocol`, `hyperdrive`, `hyperjump`, `ichi`, `ideamarket`, `idle`, `immutablex`, `impermax-v2`, `impermax-v3`, `impossible`, `indexed-finance`, `infinite-trading-protocol`, `injective-bridge`, `insurace`, `insuredao`, `interest-protocol`, `international-meme-fund-v2`, `inverse-finance-firm`, `inverse-finance-frontier`, `ipor-derivatives`, `iron-bank`, `itrust-finance`, `iziswap`, `izumi-liquidbox`, `jaypeggers`, `jetfuel-finance`, `joe-dex`, `joe-v2`, `joe-v2.1`, `jones-dao`, `jpegd`, `juicebox-v1`, `juicebox-v3`, `kasu`, `katana-pre-launch`, `keep-network`, `keep3r-network`, `kine-finance`, `king-protocol`, `kinza-finance`, `kokonut-swap`, `kromatika`, `krystal-community-vault`, `kyberswap-classic`, `kyberswap-elastic`, `landshare`, `landx-finance`, `latch`, `legion`, `lendflare`, `level`, `likwid`, `limitless-exchange`, `liquid-finance`, `lista-cdp`, `listapie`, `liveart`, `lixir-finance`, `lockon`, `loop`, `lucidly-finance`, `lybra-v1`, `lybra-v2`, `lynx`, `magic-eden`, `makina`, `mars-ecosystem`, `mars-poolin`, `matrixdock-stbt`, `maverick-v1`, `maverick-v2`, `maxapy`, `maxshot`, `mayan-bridge`, `mcdex`, `megaeth-bridge`, `mellow-yield`, `mento-v2`, `mero`, `mesher`, `meter-passport`, `metronome-v1`, `mezo-bridge`, `midas-capital`, `mim-swap`, `mint-club-v2`, `mitosis`, `mochifi`, `moneyfi`, `monolith-market`, `moonwell-lending`, `moonwell-vaults`, `more-vaults`, `moremarkets.xyz`, `morph-bridge`, `morpheusai`, `morpho-midnight`, `morpho-optimizer-aavev2`, `mortgagefi`, `mountain-protocol`, `muffin`, `multichain`, `mummy-finance`, `muscadine`, `mycelium-perpetual-pools`, `myx-finance`, `native-credit-pool`, `nerona`, `nested`, `nftx`, `niob-finance`, `nocturne`, `nomad`, `nomiswap`, `nsure`, `nucleus`, `nuva`, `octus-bridge`, `olive-network`, `onx-finance`, `openeden-prism`, `openleverage`, `opium`, `opyn-convexity`, `orbit-bridge`, `orderly-bridge`, `ordernchaos`, `oreoswap`, `origin-arm`, `origin-dollar`, `orion-liquidity-nodes`, `orion-pools`, `otsea`, `outcome-finance`, `overtime`, `padswap`, `panoptic-v2`, `paradex-bridge`, `parallel-protocol-v3`, `pay-protocol`, `peakdefi`, `peapods-finance`, `pell-network`, `penpie`, `pepeteam-bridge`, `pepu-bridge`, `percent-finance`, `peridot`, `picwe`, `piku-finance`, `planet-farm`, `plutusdao`, `pooltogether-v3`, `pooltogether-v4`, `pooltogether-v5`, `powh3d`, `prdt`, `premia-v2`, `premia-v3`, `preon-finance`, `printr`, `prismalst`, `privacy-cash`, `privacy-pools`, `pstake-lsd`, `puffer-unifi`, `pyreswap`, `qidao`, `quickswap-v4`, `radiant-v2`, `radioshack`, `radpie`, `rainbow-bridge`, `raindex`, `rank-trading`, `rari-capital`, `ratex-dex`, `reflexer`, `reservoir-protocol`, `resonate-finance`, `revault`, `revert-compoundor`, `revest-finance`, `reya-bridge`, `rezerve-money`, `rho-x`, `ribbon-earn`, `rise-bridge`, `rollx`, `ronin-bridge`, `rosen-bridge`, `royco-v1`, `royco-v2`, `rubicon`, `rumpel-labs`, `rysk-v1`, `sablier-legacy`, `saddle-finance`, `saffron-vaults`, `satlayer`, `sato`, `savvy`, `sector-finance`, `sectorone-dlmm`, `secured-finance-lending`, `segment-finance`, `sentora`, `sera`, `set-protocol`, `shape-bridge`, `shardingdao`, `sherlock`, `shift-protocol`, `shimmerbridge`, `sigma-money`, `silo-v1`, `silo-v2`, `silo-v3`, `single-finance`, `singular-farm`, `singularitydao`, `singularx`, `sir`, `skate-fi`, `smardex-amm`, `smartcredit`, `snowbl-capital`, `snowswap`, `snuggle`, `sofa.org`, `solo-top`, `solv-rwa`, `sommelier`, `sorare-bridge`, `sovryn-bridge`, `sparklend`, `spectra-metavaults-outside-v2`, `spectra-v1`, `sperax-usd`, `spot-cash`, `stability`, `stabull-finance`, `stafi`, `stake-dao`, `stakestone-berachain-vault`, `stargate-v1`, `steakhut-liquidity`, `steer-protocol`, `stonedefi`, `strata-season-0`, `sturdy-v2`, `subfrost`, `sudoswap-v1`, `sumer.money`, `sunx-bridge`, `superfund`, `superreturn`, `sushi-bentobox`, `sushiswap`, `swaap-maker-v2`, `swapr-v2`, `swell-earn`, `swellchain-bridge`, `swerve`, `swinghook`, `switcheo-finance`, `sx-rollup-bridge`, `synapse-cross-chain-bridge`, `synfutures-v1`, `syntetika`, `synthetix-v4`, `taiko-bridge`, `tangent-finance`, `tanken-capital`, `tanx.fi`, `tarot`, `tau-labs`, `termfinance-vaults`, `terminal-finance-pre-deposits`, `tetu-earn`, `the-idols`, `the-tokenized-bitcoin`, `thedeep`, `theoriq-alphavault-eth`, `theoriq-gold-vault`, `thesauros`, `threshold-thusd`, `thruster-v2`, `tidaldex`, `tokenlon-amm`, `tokenstore`, `tprotocol-v1`, `tranchess-yield`, `treedefi`, `trevee-earn`, `twindex`, `tymio`, `ufarm-digital`, `ultrayield-vaults`, `umami-finance`, `unagii`, `uncx-network-v4`, `unifarm`, `union-protocol`, `unipower`, `unitus`, `universe-xyz`, `unsheth`, `unslashed`, `untangled-vault`, `usdfi-lending`, `usual-eth0`, `uwu-lend`, `valuedefi`, `varen`, `vault-street-primeusd`, `vaultcraft`, `velvet-v2`, `velvet-v3`, `venombridge`, `venus-core-pool`, `venus-isolated-pools`, `vest-markets`, `volmex`, `voltz`, `wasabi-perps`, `wasabix`, `wavesbridge`, `wepiggy`, `wing-finance`, `wombex-finance`, `wompie`, `wrap-protocol`, `wrapped`, `xave-finance`, `xgld`, `xsigma`, `xtoken`, `xwin-finance`, `yala`, `yam-finance`, `yamato-protocol`, `yaxis`, `yay!`, `yearn-finance`, `yellow`, `yfii`, `yield-millionaire`, `yield-protocol`, `yieldflow-yield-farming`, `yieldnest`, `yieldwolf`, `zebradao`, `zero-network`, `zerolend-lending`, `zircuit-finance`, `zkcandy-bridge`, `zoo-finance`, `ztln-p`, `zunami-protocol`

</details>

### Repeat victims in this list

Whatever allowed a second incident has not necessarily been removed. These are the highest-conviction entries in the set.

| Protocol | Hacks | Family | Priority | At risk |
|---|---:|---|---:|---:|
| [Gamma](https://defillama.com/protocol/gamma) | 3 | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | 41.4 | $3,105,706 |

### Diversified shortlist — top 3 per family

| # | Protocol | Family | Priority | Likelihood | At risk | Evidence |
|---:|---|---|---:|---:|---:|---|
| 1 | [xDollar](https://defillama.com/protocol/xdollar) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 52.65 | 52.65 | $217,062 | `L4_GUARD_REVIEW` |
| 2 | [Sentiment](https://defillama.com/protocol/sentiment) | `SIG-VERIFIER-DEFEATABLE` | 50.73 | 50.73 | $517,964 | `L4_GUARD_REVIEW` |
| 3 | [Float Protocol](https://defillama.com/protocol/float-protocol) | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | 50.57 | 50.57 | $216,419 | `L4_GUARD_REVIEW` |
| 4 | [CIAN Automation](https://defillama.com/protocol/cian-automation) | `SIG-VERIFIER-DEFEATABLE` | 49.32 | 49.32 | $712,935 | `L4_GUARD_REVIEW` |
| 5 | [Turtle Club](https://defillama.com/protocol/turtle-club) | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | 48.4 | 48.4 | $795,077 | `L4_GUARD_REVIEW` |
| 6 | [Bracket LST](https://defillama.com/protocol/bracket-lst) | `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED` | 47.92 | 47.92 | $251,914 | `L4_GUARD_REVIEW` |
| 7 | [Ape Finance](https://defillama.com/protocol/ape-finance) | `SIG-VERIFIER-DEFEATABLE` | 47.57 | 47.57 | $55,553 | `L4_GUARD_REVIEW` |
| 8 | [Deq](https://defillama.com/protocol/deq) | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | 47.33 | 47.33 | $59,100 | `L4_GUARD_REVIEW` |
| 9 | [Minterest](https://defillama.com/protocol/minterest) | `AUTH-ZERO-ADDRESS-ACCEPTED` | 47.05 | 47.05 | $100,579 | `L4_GUARD_REVIEW` |
| 10 | [Solid Yield](https://defillama.com/protocol/solid-yield) | `ACC-DUPLICATE-ID-ACCUMULATION` | 46.67 | 46.67 | $215,384 | `L4_GUARD_REVIEW` |
| 11 | [Strike Finance Perpetuals](https://defillama.com/protocol/strike-finance-perpetuals) | `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET` | 46.26 | 54.42 | $2,633,301 | `L4_GUARD_REVIEW` |
| 12 | [HMX](https://defillama.com/protocol/hmx) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 46.08 | 46.08 | $263,928 | `L4_GUARD_REVIEW` |
| 13 | [Tizi](https://defillama.com/protocol/tizi) | `PROOF-VERIFICATION-BYPASSED` | 45.03 | 45.03 | $223,724 | `L4_GUARD_REVIEW` |
| 14 | [Hyperbeat USD](https://defillama.com/protocol/hyperbeat-usd) | `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET` | 44.56 | 52.42 | $1,766,161 | `L4_GUARD_REVIEW` |
| 15 | [KUMA Protocol](https://defillama.com/protocol/kuma-protocol) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 43.95 | 51.7 | $3,168,105 | `L4_GUARD_REVIEW` |
| 16 | [Birch Hill](https://defillama.com/protocol/birch-hill) | `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED` | 43.62 | 43.62 | $101,136 | `L4_GUARD_REVIEW` |
| 17 | [BitSwap](https://defillama.com/protocol/bitswap) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 42.93 | 42.93 | $62,979 | `L4_GUARD_REVIEW` |
| 18 | [Syntropia](https://defillama.com/protocol/syntropia) | `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED` | 41.72 | 49.08 | $5,465,297 | `L4_GUARD_REVIEW` |
| 19 | [Gamma](https://defillama.com/protocol/gamma) | `AUTH-ZERO-ADDRESS-ACCEPTED` | 41.4 | 48.7 | $3,105,706 | `L4_GUARD_REVIEW` |
| 20 | [Supernova CL](https://defillama.com/protocol/supernova-cl) | `ACC-DUPLICATE-ID-ACCUMULATION` | 41.05 | 41.05 | $770,613 | `L4_GUARD_REVIEW` |
| 21 | [MUX Perps](https://defillama.com/protocol/mux-perps) | `AUTH-ZERO-ADDRESS-ACCEPTED` | 39.61 | 46.6 | $9,913,739 | `L4_GUARD_REVIEW` |
| 22 | [Hemi](https://defillama.com/protocol/hemi) | `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET` | 39.13 | 39.13 | $882,892 | `L4_GUARD_REVIEW` |
| 23 | [iAero Protocol](https://defillama.com/protocol/iaero-protocol) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 38.79 | 45.63 | $2,241,398 | `L4_GUARD_REVIEW` |
| 24 | [Seer](https://defillama.com/protocol/seer) | `ACC-DUPLICATE-ID-ACCUMULATION` | 37.5 | 37.5 | $709,999 | `L4_GUARD_REVIEW` |
| 25 | [set.wtf](https://defillama.com/protocol/set.wtf) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 34.54 | 46.05 | $320,265 | `L4_GUARD_REVIEW` |
| 26 | [ZyFAI](https://defillama.com/protocol/zyfai) | `ACC-HARDCODED-PEG-REDEMPTION` | 30.67 | 51.12 | $10,278,463 | `L4_GUARD_REVIEW` |
| 27 | [Sprinter](https://defillama.com/protocol/sprinter) | `ACC-DONATION-UNACCOUNTED-BALANCE` | 30.33 | 35.68 | $1,139,725 | `L4_GUARD_REVIEW` |
| 28 | [OpenEden USDO](https://defillama.com/protocol/openeden-usdo) | `ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE` | 25.8 | 43.0 | $24,618,886 | `L4_GUARD_REVIEW` |
| 29 | [Yield Yak Aggregator](https://defillama.com/protocol/yield-yak-aggregator) | `BRIDGE-MESSAGE-NOT-BOUND-TO-SOURCE` | 24.14 | 40.23 | $15,139,245 | `L4_GUARD_REVIEW` |
| 30 | [g8keep](https://defillama.com/protocol/g8keep) | `ACC-CREDIT-NOT-RECEIVED` | 23.92 | 31.9 | $151,873 | `L4_GUARD_REVIEW` |

---

### 1. xDollar  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 1
- **Protocol:** xDollar (`xdollar`) · CDP · IoTeX, Ethereum, Arbitrum, Polygon, Avalanche
- **DefiLlama:** https://defillama.com/protocol/xdollar
- **PRIORITY 52.65**  =  LIKELIHOOD 52.65 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 15.75/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $217,062 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`StableCollTroveManager` @ 0x1e49892c…(ethereum), `CollateralRegistry` @ 0x1ec92874…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for StableCollTroveManager@0x1e49892c…(ethereum), CollateralRegistry@0x1ec92874…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#xdollar|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#xdollar`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/xDollar-Finance/xDollar-contracts/blob/main/xDollar%20-%20Smart%20Contract%20Audit%20v210624.pdf

### 2. Sentiment  —  `SIG-VERIFIER-DEFEATABLE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 2
- **Protocol:** Sentiment (`sentiment`) · Lending · Hyperliquid L1, Arbitrum
- **DefiLlama:** https://defillama.com/protocol/sentiment
- **PRIORITY 50.73**  =  LIKELIHOOD 50.73 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 13.83/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $517,964 · **Band:** `IN_BAND`
- **Previously hacked:** 2023-04-04 for $1,000,000 [Reentrancy]
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
- **Broken invariant tested:** A verification routine must reject malformed, empty or zero-recovered signatures, and must never treat address(0) as a match.
    - Deployed source (`Registry` @ 0xe22d240b…(arbitrum), `RiskEngine` @ 0xc0ac97A0…(arbitrum)): prerequisites matched: ecrecover_without_zero_check; no guard found
    - deployed source read for Registry@0xe22d240b…(arbitrum), RiskEngine@0xc0ac97A0…(arbitrum); indicators matched: ecrecover_without_zero_check
- **Preconditions PRESENT / UNKNOWN:** src::ecrecover_without_zero_check, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** uses_oz_ecdsa / none in the reviewed path
- **Prior art:** `KNOWN_ISSUE_DEPLOYMENT_STATUS_UNKNOWN` — DefiLlama's hacks dataset records 1 prior on-chain incident(s) on this protocol, most recently 2023-04-04 for $1,000,000 [Reentrancy]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** OZ ECDSA library in the deployed bytecode (kills the ecrecover-zero shape); Signer address immutable and non-zero
- **Where to start:** On a fork, submit r=0,s=0,v=27 and an empty signature to every signature-gated entrypoint; all must revert.
- **Evidence:** `protocols/deep_screened.jsonl#sentiment|SIG-VERIFIER-DEFEATABLE`, `protocols/onchain_probes.json#sentiment`
- **Disclosure:** https://app.sentiment.xyz · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/arbitraryexecution/publications/blob/main/assessments/Sentiment_Protocol_20220727.pdf, https://github.com/arbitraryexecution/publications/blob/main/assessments/Sentiment_Oracle_20220727.pdf

### 3. Float Protocol  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 3
- **Protocol:** Float Protocol (`float-protocol`) · Yield · Ethereum
- **DefiLlama:** https://defillama.com/protocol/float-protocol
- **PRIORITY 50.57**  =  LIKELIHOOD 50.57 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 18.67/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $216,419 · **Band:** `IN_BAND`
- **Previously hacked:** 2022-01-15 for $1,160,000 [Spot Price Manipulation]
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`Phase4Pool` @ 0x08D7e47B…(ethereum), `MultiplierPool` @ 0x52eadaFf…(ethereum)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for Phase4Pool@0x08D7e47B…(ethereum), MultiplierPool@0x52eadaFf…(ethereum); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `KNOWN_ISSUE_DEPLOYMENT_STATUS_UNKNOWN` — DefiLlama's hacks dataset records 1 prior on-chain incident(s) on this protocol, most recently 2022-01-15 for $1,160,000 [Spot Price Manipulation]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#float-protocol|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#float-protocol`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://drive.google.com/file/d/1Vg3nCThlArC44JFj7Di5HMWziPGMFbvl/view

### 4. CIAN Automation  —  `SIG-VERIFIER-DEFEATABLE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 4
- **Protocol:** CIAN Automation (`cian-automation`) · Yield · Avalanche, Polygon, Ethereum
- **DefiLlama:** https://defillama.com/protocol/cian-automation
- **PRIORITY 49.32**  =  LIKELIHOOD 49.32 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 12.42/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $712,935 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A verification routine must reject malformed, empty or zero-recovered signatures, and must never treat address(0) as a match.
    - Deployed source (`AStETH` @ 0xbd233d4f…(ethereum)): prerequisites matched: ecrecover_without_zero_check; no guard found
    - deployed source read for AStETH@0xbd233d4f…(ethereum); indicators matched: ecrecover_without_zero_check
- **Preconditions PRESENT / UNKNOWN:** src::ecrecover_without_zero_check, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** uses_oz_ecdsa / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** OZ ECDSA library in the deployed bytecode (kills the ecrecover-zero shape); Signer address immutable and non-zero
- **Where to start:** On a fork, submit r=0,s=0,v=27 and an empty signature to every signature-gated entrypoint; all must revert.
- **Evidence:** `protocols/deep_screened.jsonl#cian-automation|SIG-VERIFIER-DEFEATABLE`, `protocols/onchain_probes.json#cian-automation`
- **Disclosure:** https://yieldlayer.cian.app/vaults/0xB13aa2d0345b0439b064f26B82D8dCf3f508775d?chainId=1&utm_source=TPFDZE · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.cian.app/security-and-risk/audit-report

### 5. Turtle Club  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 5
- **Protocol:** Turtle Club (`turtle-club`) · Onchain Capital Allocator · Ethereum, Avalanche, Linea
- **DefiLlama:** https://defillama.com/protocol/turtle-club
- **PRIORITY 48.4**  =  LIKELIHOOD 48.4 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 16.5/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $795,077 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 84.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`Turtle` @ 0x67e718f4…(ethereum)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for Turtle@0x67e718f4…(ethereum); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#turtle-club|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#turtle-club`
- **Disclosure:** https://app.turtle.xyz/ · no audit link listed

### 6. Bracket LST  —  `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 6
- **Protocol:** Bracket LST (`bracket-lst`) · Liquid Staking · Ethereum
- **DefiLlama:** https://defillama.com/protocol/bracket-lst
- **PRIORITY 47.92**  =  LIKELIHOOD 47.92 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 11.02/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $251,914 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.
    - Deployed source (`BrktETH` @ 0x22ad51ad…(ethereum)): prerequisites matched: caller_named_asset_no_registry_check; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): value_fn_moves_caller_named_asset=yes
    - deployed source read for BrktETH@0x22ad51ad…(ethereum); indicators matched: caller_named_asset_no_registry_check, value_fn_moves_caller_named_asset
- **Preconditions PRESENT / UNKNOWN:** src::caller_named_asset_no_registry_check, live_value_present, deployment_reachable_on_chain / src::token_hook_credits_without_sender_check
- **Guards searched / found:** asset_registry_check_present / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Every identifier derived or verified against the factory/registry (kills the pair); Routing restricted to an immutable venue allowlist
- **Where to start:** On a fork, create a fake pool/mint and pass it to every identifier-accepting entrypoint; all must revert.
- **Evidence:** `protocols/deep_screened.jsonl#bracket-lst|ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`, `protocols/onchain_probes.json#bracket-lst`
- **Disclosure:** https://app.bracket.fi/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.bracket.fi/security/audits

### 7. Ape Finance  —  `SIG-VERIFIER-DEFEATABLE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 7
- **Protocol:** Ape Finance (`ape-finance`) · Lending · Ethereum
- **DefiLlama:** https://defillama.com/protocol/ape-finance
- **PRIORITY 47.57**  =  LIKELIHOOD 47.57 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 10.67/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $55,553 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A verification routine must reject malformed, empty or zero-recovered signatures, and must never treat address(0) as a match.
    - Deployed source (`GnosisSafeProxy` @ 0x02ca76e8…(ethereum), `Vyper_contract` @ 0x04b727C7…(ethereum)): prerequisites matched: ecrecover_without_zero_check; no guard found
    - deployed source read for GnosisSafeProxy@0x02ca76e8…(ethereum), Vyper_contract@0x04b727C7…(ethereum); indicators matched: ecrecover_without_zero_check
- **Preconditions PRESENT / UNKNOWN:** src::ecrecover_without_zero_check, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** uses_oz_ecdsa / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** OZ ECDSA library in the deployed bytecode (kills the ecrecover-zero shape); Signer address immutable and non-zero
- **Where to start:** On a fork, submit r=0,s=0,v=27 and an empty signature to every signature-gated entrypoint; all must revert.
- **Evidence:** `protocols/deep_screened.jsonl#ape-finance|SIG-VERIFIER-DEFEATABLE`, `protocols/onchain_probes.json#ape-finance`
- **Disclosure:** https://ape.fi · no audit link listed

### 8. Deq  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 8
- **Protocol:** Deq (`deq`) · Liquid Staking · Ethereum
- **DefiLlama:** https://defillama.com/protocol/deq
- **PRIORITY 47.33**  =  LIKELIHOOD 47.33 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 15.43/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $59,100 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`StakedAvail` @ 0x3ce617ef…(ethereum)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for StakedAvail@0x3ce617ef…(ethereum); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#deq|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#deq`
- **Disclosure:** https://deq.fi · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.deq.fi/addresses#audits

### 9. Minterest  —  `ACC-DONATION-UNACCOUNTED-BALANCE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 9
- **Protocol:** Minterest (`minterest`) · Lending · Mantle, Ethereum, Taiko, Morph
- **DefiLlama:** https://defillama.com/protocol/minterest
- **PRIORITY 47.05**  =  LIKELIHOOD 47.05 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 15.15/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $100,579 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
- **Broken invariant tested:** A share price, exchange rate or totalAssets must be a function of value the protocol accounted for on entry. Reading a raw balance makes any direct transfer into the accounting boundary an unpriced increase in every holder's claim.
    - Deployed source (`CErc20Immutable` @ 0x004c0908…(ethereum), `TransparentUpgradeableProxy` @ 0x02451015…(ethereum)): prerequisites matched: getCashPrior_balanceOf; no guard found
    - deployed source read for CErc20Immutable@0x004c0908…(ethereum), TransparentUpgradeableProxy@0x02451015…(ethereum); indicators matched: getCashPrior_balanceOf
- **Preconditions PRESENT / UNKNOWN:** src::getCashPrior_balanceOf, unprivileged_inbound_transfer_possible, live_value_exposed / src::totalAssets_reads_balanceOf
- **Guards searched / found:** internal_cash_counter / none in the reviewed path
- **Prior art:** `KNOWN_ISSUE_DEPLOYMENT_STATUS_UNKNOWN` — The Compound-fork donation vector is publicly documented and was raised in Venus's own Code4rena audit before the March 2026 exploit.
- **Falsified by:** totalAssets derived from an internal counter, not balanceOf (kills the pair); Rate is monotonic and rate-limited per block; Inbound transfers to the accounting boundary are rejected or swept to a reserve
- **Where to start:** On a fork, transfer an arbitrary amount of each counted asset directly into every accounting boundary; the share price, exchange rate and derived borrow power must not change.
- **Evidence:** `protocols/deep_screened.jsonl#minterest|ACC-DONATION-UNACCOUNTED-BALANCE`, `protocols/onchain_probes.json#minterest`
- **Disclosure:** https://minterest.com · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://minterest.com/audit-report-trail-of-bits/, https://minterest.com/audit-report-hacken/

### 10. Solid Yield  —  `ACC-DUPLICATE-ID-ACCUMULATION`

- **Rank (Ranking A — priority (likelihood × actionability)):** 10
- **Protocol:** Solid Yield (`solid-yield`) · Yield · Fuse, Ethereum
- **DefiLlama:** https://defillama.com/protocol/solid-yield
- **PRIORITY 46.67**  =  LIKELIHOOD 46.67 × ACTIONABILITY 100.0%
    - likelihood = family evidence 30.0/50 (MATCH 60 × evidence weight 1.0) + learned attack surface 16.67/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $215,384 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 60 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `unverified_implementation` — raises likelihood, measured lift ×2.007 (weight +0.70)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** An entitlement attached to an identifier may be counted at most once per period. A caller-supplied ID list must be deduplicated, or each ID's claim state consumed before the next read.
    - Deployed source (`AccountantWithRateProviders` @ 0x10f39969…(ethereum)): prerequisites matched: id_array_loop_without_dedup; no guard found
    - deployed source read for AccountantWithRateProviders@0x10f39969…(ethereum); indicators matched: id_array_loop_without_dedup
    - 1 implementation(s) behind a proxy are NOT verified on the explorer: implementation identity unresolved, score capped at 60
- **Preconditions PRESENT / UNKNOWN:** src::id_array_loop_without_dedup, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Consumed marker written inside the loop (kills the pair); IDs required strictly increasing
- **Where to start:** On a fork, call the batch function with one ID repeated k times; payout must equal the single-ID payout.
- **Evidence:** `protocols/deep_screened.jsonl#solid-yield|ACC-DUPLICATE-ID-ACCUMULATION`, `protocols/onchain_probes.json#solid-yield`
- **Disclosure:** https://solid.xyz · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.solid.xyz/safety-and-trust/security-and-audits#audits

### 11. Strike Finance Perpetuals  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 11
- **Protocol:** Strike Finance Perpetuals (`strike-finance-perpetuals`) · Derivatives · Cardano, Ethereum
- **DefiLlama:** https://defillama.com/protocol/strike-finance-perpetuals
- **PRIORITY 46.26**  =  LIKELIHOOD 54.42 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 22.52/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $2,633,301 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#strike-finance-perpetuals|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#strike-finance-perpetuals`
- **Disclosure:** https://www.strikefinance.org/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/strike-finance/forwards-smart-contracts/blob/main/audit/audit.pdf

### 12. CLever  —  `SIG-VERIFIER-DEFEATABLE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 12
- **Protocol:** CLever (`clever`) · Yield · Ethereum
- **DefiLlama:** https://defillama.com/protocol/clever
- **PRIORITY 46.1**  =  LIKELIHOOD 54.23 × ACTIONABILITY 85.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 17.33/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $6,626,612 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A verification routine must reject malformed, empty or zero-recovered signatures, and must never treat address(0) as a match.
    - Deployed source (`BeaconProxy` @ 0x2C37F1Dc…(ethereum), `Vyper_contract` @ 0x6C280dB0…(ethereum)): prerequisites matched: ecrecover_without_zero_check; no guard found
    - deployed source read for BeaconProxy@0x2C37F1Dc…(ethereum), Vyper_contract@0x6C280dB0…(ethereum); indicators matched: ecrecover_without_zero_check
- **Preconditions PRESENT / UNKNOWN:** src::ecrecover_without_zero_check, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** uses_oz_ecdsa / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** OZ ECDSA library in the deployed bytecode (kills the ecrecover-zero shape); Signer address immutable and non-zero
- **Where to start:** On a fork, submit r=0,s=0,v=27 and an empty signature to every signature-gated entrypoint; all must revert.
- **Evidence:** `protocols/deep_screened.jsonl#clever|SIG-VERIFIER-DEFEATABLE`, `protocols/onchain_probes.json#clever`
- **Disclosure:** https://clever.aladdin.club/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/AladdinDAO/aladdin-v3-contracts/blob/main/audit-reports/SECBIT_CLever_Report_v1.1.pdf

### 13. HMX  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 13
- **Protocol:** HMX (`hmx`) · Derivatives · Arbitrum, Blast, Polygon
- **DefiLlama:** https://defillama.com/protocol/hmx
- **PRIORITY 46.08**  =  LIKELIHOOD 46.08 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 9.18/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $263,928 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`MarketToken` @ 0x70d95587…(arbitrum), `PerpStorage` @ 0x4862b734…(arbitrum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for MarketToken@0x70d95587…(arbitrum), PerpStorage@0x4862b734…(arbitrum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#hmx|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#hmx`
- **Disclosure:** https://hmx.org/arbitrum · no audit link listed

### 14. Tizi  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 14
- **Protocol:** Tizi (`tizi`) · Yield Aggregator · Base
- **DefiLlama:** https://defillama.com/protocol/tizi
- **PRIORITY 45.03**  =  LIKELIHOOD 45.03 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 13.13/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $223,724 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`TiziDollar` @ 0x469bbd88…(base)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for TiziDollar@0x469bbd88…(base); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#tizi|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#tizi`
- **Disclosure:**   · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://2781107368-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FlxAaGBCj8m8RA8EcZ25F%2Fuploads%2FEJb3Xu5zhoktjv1DRmti%2FTizi%20audit%20by%20Beosin.pdf?alt=media&token=738f8007-4817-4b9d-9709-697fcc6bd6a4

### 15. wstGBP  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 15
- **Protocol:** wstGBP (`wstgbp`) · RWA · Ethereum
- **DefiLlama:** https://defillama.com/protocol/wstgbp
- **PRIORITY 44.83**  =  LIKELIHOOD 44.83 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 12.93/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $114,770 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`StableTokenV1OFT` @ 0x94321d80…(ethereum), `MaseerOne` @ 0x57C3571f…(ethereum)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for StableTokenV1OFT@0x94321d80…(ethereum), MaseerOne@0x57C3571f…(ethereum); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#wstgbp|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#wstgbp`
- **Disclosure:** https://wstgbp.com · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.wstgbp.com/audits/2026-04-29-prototech-wstgbp-audit.pdf

### 16. Hyperbeat USD  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 16
- **Protocol:** Hyperbeat USD (`hyperbeat-usd`) · Lending · Hyperliquid L1, Ethereum
- **DefiLlama:** https://defillama.com/protocol/hyperbeat-usd
- **PRIORITY 44.56**  =  LIKELIHOOD 52.42 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 20.52/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,766,161 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#hyperbeat-usd|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#hyperbeat-usd`
- **Disclosure:** https://app.hyperbeat.org · no audit link listed

### 17. KUMA Protocol  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking A — priority (likelihood × actionability)):** 17
- **Protocol:** KUMA Protocol (`kuma-protocol`) · RWA · Ethereum, Linea, Polygon, Telos
- **DefiLlama:** https://defillama.com/protocol/kuma-protocol
- **PRIORITY 43.95**  =  LIKELIHOOD 51.7 × ACTIONABILITY 85.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 14.8/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $3,168,105 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source (`KIBToken` @ 0x3cd09352…(ethereum), `KIBToken` @ 0x94abc288…(ethereum)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for KIBToken@0x3cd09352…(ethereum), KIBToken@0x94abc288…(ethereum); indicators matched: unsafe_cross_sign_cast
- **Preconditions PRESENT / UNKNOWN:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** safecast_used / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#kuma-protocol|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#kuma-protocol`
- **Disclosure:** https://kuma.bond · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.kuma.bond/kuma-protocol/ressources/security-and-audits

### 18. Primitive  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 18
- **Protocol:** Primitive (`primitive`) · Dexs · Ethereum
- **DefiLlama:** https://defillama.com/protocol/primitive
- **PRIORITY 43.95**  =  LIKELIHOOD 43.95 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 12.05/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $59,652 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `owner_is_eoa` — raises likelihood, measured lift ×1.729 (weight +0.55)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`Registry` @ 0x16274044…(ethereum), `PrimitiveEngine` @ 0xd3541aD1…(ethereum)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for Registry@0x16274044…(ethereum), PrimitiveEngine@0xd3541aD1…(ethereum); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#primitive|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#primitive`
- **Disclosure:** https://primitive.xyz/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://library.primitive.xyz/technical/security/audits

### 19. Birch Hill  —  `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 19
- **Protocol:** Birch Hill (`birch-hill`) · Risk Curators · Base
- **DefiLlama:** https://defillama.com/protocol/birch-hill
- **PRIORITY 43.62**  =  LIKELIHOOD 43.62 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 6.72/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $101,136 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.
    - Deployed source (`GnosisSafeProxy` @ 0x0000aeB7…(base), `PlasmaVault` @ 0x01a6ff6e…(base)): prerequisites matched: caller_named_asset_no_registry_check; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): value_fn_moves_caller_named_asset=yes
    - deployed source read for GnosisSafeProxy@0x0000aeB7…(base), PlasmaVault@0x01a6ff6e…(base); indicators matched: caller_named_asset_no_registry_check, value_fn_moves_caller_named_asset
- **Preconditions PRESENT / UNKNOWN:** src::caller_named_asset_no_registry_check, live_value_present, deployment_reachable_on_chain / src::token_hook_credits_without_sender_check
- **Guards searched / found:** asset_registry_check_present / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Every identifier derived or verified against the factory/registry (kills the pair); Routing restricted to an immutable venue allowlist
- **Where to start:** On a fork, create a fake pool/mint and pass it to every identifier-accepting entrypoint; all must revert.
- **Evidence:** `protocols/deep_screened.jsonl#birch-hill|ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`, `protocols/onchain_probes.json#birch-hill`
- **Disclosure:** https://www.birchhill.io/ · no audit link listed

### 20. Asymmetry Finance  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 20
- **Protocol:** Asymmetry Finance (`asymmetry-finance`) · Indexes · Ethereum
- **DefiLlama:** https://defillama.com/protocol/asymmetry-finance
- **PRIORITY 43.58**  =  LIKELIHOOD 51.27 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 19.37/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $2,284,932 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`SimpleProxy` @ 0x00000000…(ethereum), `AsfToken` @ 0x59a52907…(ethereum)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for SimpleProxy@0x00000000…(ethereum), AsfToken@0x59a52907…(ethereum); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#asymmetry-finance|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#asymmetry-finance`
- **Disclosure:** https://www.asymmetry.finance · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.asymmetry.finance/security/audits-bug-bounties

### 21. BitSwap  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking A — priority (likelihood × actionability)):** 21
- **Protocol:** BitSwap (`bitswap`) · Cross Chain Bridge · Ethereum
- **DefiLlama:** https://defillama.com/protocol/bitswap
- **PRIORITY 42.93**  =  LIKELIHOOD 42.93 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 6.03/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $62,979 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `owner_is_eoa` — raises likelihood, measured lift ×1.729 (weight +0.55)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source (`LiquidityManager` @ 0x2BDE2040…(ethereum), `BRC20` @ 0xC881255e…(ethereum)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for LiquidityManager@0x2BDE2040…(ethereum), BRC20@0xC881255e…(ethereum); indicators matched: unsafe_cross_sign_cast
- **Preconditions PRESENT / UNKNOWN:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** safecast_used / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#bitswap|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#bitswap`
- **Disclosure:** https://bitswap.site · no audit link listed

### 22. YieldFlow-YTrade  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 22
- **Protocol:** YieldFlow-YTrade (`yieldflow-ytrade`) · Derivatives · Arbitrum
- **DefiLlama:** https://defillama.com/protocol/yieldflow-ytrade
- **PRIORITY 42.45**  =  LIKELIHOOD 42.45 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 5.55/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $55,042 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`GridBotFactory` @ 0x356e1f9a…(arbitrum), `Reader` @ 0xe739e72E…(arbitrum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for GridBotFactory@0x356e1f9a…(arbitrum), Reader@0xe739e72E…(arbitrum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#yieldflow-ytrade|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#yieldflow-ytrade`
- **Disclosure:** https://yieldflow.com · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://skynet.certik.com/projects/yieldflow

### 23. Syntropia  —  `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 23
- **Protocol:** Syntropia (`syntropia`) · Yield Aggregator · Ethereum
- **DefiLlama:** https://defillama.com/protocol/syntropia
- **PRIORITY 41.72**  =  LIKELIHOOD 49.08 × ACTIONABILITY 85.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 12.18/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $5,465,297 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.
    - Deployed source (`Vault` @ 0xe50554ec…(ethereum)): prerequisites matched: caller_named_asset_no_registry_check; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): value_fn_moves_caller_named_asset=yes
    - deployed source read for Vault@0xe50554ec…(ethereum); indicators matched: caller_named_asset_no_registry_check, value_fn_moves_caller_named_asset
- **Preconditions PRESENT / UNKNOWN:** src::caller_named_asset_no_registry_check, live_value_present, deployment_reachable_on_chain / src::token_hook_credits_without_sender_check
- **Guards searched / found:** asset_registry_check_present / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Every identifier derived or verified against the factory/registry (kills the pair); Routing restricted to an immutable venue allowlist
- **Where to start:** On a fork, create a fake pool/mint and pass it to every identifier-accepting entrypoint; all must revert.
- **Evidence:** `protocols/deep_screened.jsonl#syntropia|ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`, `protocols/onchain_probes.json#syntropia`
- **Disclosure:** https://syntropia.ai/ · no audit link listed

### 24. Gamma  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 24
- **Protocol:** Gamma (`gamma`) · Liquidity Manager · Ethereum, Binance, Polygon, Arbitrum, xDai, Linea …
- **DefiLlama:** https://defillama.com/protocol/gamma
- **PRIORITY 41.4**  =  LIKELIHOOD 48.7 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 16.8/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $3,105,706 · **Band:** `IN_BAND`
- **REPEAT VICTIM — 3 recorded hacks.** 2024-01-04 $4,500,000 [Spot Price Manipulation]
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`xGamma` @ 0x26805021…(ethereum), `Gamma` @ 0x6bea7cfe…(ethereum)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for xGamma@0x26805021…(ethereum), Gamma@0x6bea7cfe…(ethereum); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `UNREMEDIATED_KNOWN_ISSUE` — DefiLlama's hacks dataset records 1 prior on-chain incident(s) on this protocol, most recently 2024-01-04 for $4,500,000 [Spot Price Manipulation]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#gamma|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#gamma`
- **Disclosure:** https://www.gamma.xyz · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/GammaStrategies/hypervisor/blob/master/ConsenSys-Diligence-Audit-28-03-22.pdf, https://github.com/GammaStrategies/hypervisor/blob/master/AE_Gamma_audit_09_03_22.pdf

### 25. ZAMM  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 25
- **Protocol:** ZAMM (`zamm`) · Dexs · Ethereum
- **DefiLlama:** https://defillama.com/protocol/zamm
- **PRIORITY 41.1**  =  LIKELIHOOD 41.1 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 4.2/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $72,729 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `zCurve` @ 0x00000000…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), zCurve@0x00000000…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#zamm|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#zamm`
- **Disclosure:** https://www.zamm.finance/swap · no audit link listed

### 26. Supernova CL  —  `ACC-DUPLICATE-ID-ACCUMULATION`

- **Rank (Ranking A — priority (likelihood × actionability)):** 26
- **Protocol:** Supernova CL (`supernova-cl`) · Dexs · Ethereum
- **DefiLlama:** https://defillama.com/protocol/supernova-cl
- **PRIORITY 41.05**  =  LIKELIHOOD 41.05 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 9.15/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $770,613 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** An entitlement attached to an identifier may be counted at most once per period. A caller-supplied ID list must be deduplicated, or each ID's claim state consumed before the next read.
    - Deployed source (`GSCORE` @ 0x0fd4a527…(ethereum)): prerequisites matched: id_array_loop_without_dedup; no guard found
    - deployed source read for GSCORE@0x0fd4a527…(ethereum); indicators matched: id_array_loop_without_dedup
- **Preconditions PRESENT / UNKNOWN:** src::id_array_loop_without_dedup, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Consumed marker written inside the loop (kills the pair); IDs required strictly increasing
- **Where to start:** On a fork, call the batch function with one ID repeated k times; payout must equal the single-ID payout.
- **Evidence:** `protocols/deep_screened.jsonl#supernova-cl|ACC-DUPLICATE-ID-ACCUMULATION`, `protocols/onchain_probes.json#supernova-cl`
- **Disclosure:** https://supernova.xyz/ · no audit link listed

### 27. Spreads Finance Yield  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 27
- **Protocol:** Spreads Finance Yield (`spreads-finance-yield`) · Yield · Ethereum
- **DefiLlama:** https://defillama.com/protocol/spreads-finance-yield
- **PRIORITY 41.05**  =  LIKELIHOOD 41.05 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 9.15/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $60,300 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`VaultToken` @ 0xc59f7870…(ethereum)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for VaultToken@0xc59f7870…(ethereum); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#spreads-finance-yield|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#spreads-finance-yield`
- **Disclosure:** https://spreads.fi/ · no audit link listed

### 28. MUX Perps  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 28
- **Protocol:** MUX Perps (`mux-perps`) · Derivatives · Arbitrum, Avalanche, Binance, Optimism, Fantom
- **DefiLlama:** https://defillama.com/protocol/mux-perps
- **PRIORITY 39.61**  =  LIKELIHOOD 46.6 × ACTIONABILITY 85.0%
    - likelihood = family evidence 30.0/50 (MATCH 60 × evidence weight 1.0) + learned attack surface 16.6/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $9,913,739 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 60 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `unverified_implementation` — raises likelihood, measured lift ×2.007 (weight +0.70)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`LibLiquidity` @ 0xfb0DCDC3…(bsc)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for LibLiquidity@0xfb0DCDC3…(bsc); indicators matched: owner_compare_without_nonzero
    - 1 implementation(s) behind a proxy are NOT verified on the explorer: implementation identity unresolved, score capped at 60
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `EOA_SINGLE_KEY`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#mux-perps|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#mux-perps`
- **Disclosure:** https://mux.network/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://www.certik.com/projects/mux-protocol

### 29. IDEX Classic  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 29
- **Protocol:** IDEX Classic (`idex-classic`) · Dexs · Ethereum, Polygon, Binance
- **DefiLlama:** https://defillama.com/protocol/idex-classic
- **PRIORITY 39.37**  =  LIKELIHOOD 46.32 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 14.42/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,381,050 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`Custodian` @ 0xE5c405C5…(ethereum), `Exchange` @ 0xa36972e3…(ethereum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for Custodian@0xE5c405C5…(ethereum), Exchange@0xa36972e3…(ethereum); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#idex-classic|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#idex-classic`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/idexio/idex-contracts/tree/master/audits, https://callisto.network/idex-security-audit/

### 30. Hemi  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 30
- **Protocol:** Hemi (`hemi`) · Canonical Bridge · Ethereum
- **DefiLlama:** https://defillama.com/protocol/hemi
- **PRIORITY 39.13**  =  LIKELIHOOD 39.13 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 7.23/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $882,892 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ChiToken` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ChiToken@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#hemi|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#hemi`
- **Disclosure:** https://hemi.xyz/ · no audit link listed

### 31. iAero Protocol  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking A — priority (likelihood × actionability)):** 31
- **Protocol:** iAero Protocol (`iaero-protocol`) · Liquid Staking · Base
- **DefiLlama:** https://defillama.com/protocol/iaero-protocol
- **PRIORITY 38.79**  =  LIKELIHOOD 45.63 × ACTIONABILITY 85.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 8.73/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $2,241,398 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source (`Aero` @ 0x940181a9…(base)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for Aero@0x940181a9…(base); indicators matched: unsafe_cross_sign_cast
- **Preconditions PRESENT / UNKNOWN:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** safecast_used / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#iaero-protocol|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#iaero-protocol`
- **Disclosure:** https://app.iaero.finance/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.iaero.finance/technical-documentation/contracts-overview

### 32. Seer  —  `ACC-DUPLICATE-ID-ACCUMULATION`

- **Rank (Ranking A — priority (likelihood × actionability)):** 32
- **Protocol:** Seer (`seer`) · Prediction Market · xDai, Ethereum
- **DefiLlama:** https://defillama.com/protocol/seer
- **PRIORITY 37.5**  =  LIKELIHOOD 37.5 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 5.6/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $709,999 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
- **Broken invariant tested:** An entitlement attached to an identifier may be counted at most once per period. A caller-supplied ID list must be deduplicated, or each ID's claim state consumed before the next read.
    - Deployed source (`MarketView` @ 0xAb797C4C…(ethereum), `ConditionalTokens` @ 0xC59b0e4D…(ethereum)): prerequisites matched: id_array_loop_without_dedup; no guard found
    - deployed source read for MarketView@0xAb797C4C…(ethereum), ConditionalTokens@0xC59b0e4D…(ethereum); indicators matched: id_array_loop_without_dedup
- **Preconditions PRESENT / UNKNOWN:** src::id_array_loop_without_dedup, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Consumed marker written inside the loop (kills the pair); IDs required strictly increasing
- **Where to start:** On a fork, call the batch function with one ID repeated k times; payout must equal the single-ID payout.
- **Evidence:** `protocols/deep_screened.jsonl#seer|ACC-DUPLICATE-ID-ACCUMULATION`, `protocols/onchain_probes.json#seer`
- **Disclosure:** https://seer.pm/ · no audit link listed

### 33. Goldfinch  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 33
- **Protocol:** Goldfinch (`goldfinch`) · RWA Lending · Ethereum
- **DefiLlama:** https://defillama.com/protocol/goldfinch
- **PRIORITY 36.66**  =  LIKELIHOOD 43.13 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 11.23/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,645,216 · **Band:** `IN_BAND`
- **Previously hacked:** 2025-12-02 for $330,000 [Token Approval Abuse]
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`EIP173Proxy` @ 0x57686612…(ethereum), `EIP173Proxy` @ 0x8481a6Eb…(ethereum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for EIP173Proxy@0x57686612…(ethereum), EIP173Proxy@0x8481a6Eb…(ethereum); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `KNOWN_ISSUE_DEPLOYMENT_STATUS_UNKNOWN` — DefiLlama's hacks dataset records 1 prior on-chain incident(s) on this protocol, most recently 2025-12-02 for $330,000 [Token Approval Abuse]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#goldfinch|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#goldfinch`
- **Disclosure:** https://goldfinch.finance · no audit link listed

### 34. Kernel Protocol  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 34
- **Protocol:** Kernel Protocol (`kernel-protocol`) · Liquid Restaking · Ethereum
- **DefiLlama:** https://defillama.com/protocol/kernel-protocol
- **PRIORITY 36.1**  =  LIKELIHOOD 36.1 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 4.2/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $50,340 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`kUSD` @ 0x0bB9aB78…(ethereum), `ksETH` @ 0x513D27c9…(ethereum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for kUSD@0x0bB9aB78…(ethereum), ksETH@0x513D27c9…(ethereum); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#kernel-protocol|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#kernel-protocol`
- **Disclosure:** https://kernelprotocol.com · no audit link listed

### 35. Stryke CLAMM  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 35
- **Protocol:** Stryke CLAMM (`stryke-clamm`) · Options · Arbitrum, Sonic, Base, Blast, Mantle
- **DefiLlama:** https://defillama.com/protocol/stryke-clamm
- **PRIORITY 35.68**  =  LIKELIHOOD 35.68 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 3.78/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $175,955 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 84.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`ArbRdpxToken` @ 0xEec2bE5c…(arbitrum)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for ArbRdpxToken@0xEec2bE5c…(arbitrum); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#stryke-clamm|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#stryke-clamm`
- **Disclosure:** https://www.stryke.xyz/en · no audit link listed

### 36. TokenWorks  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 36
- **Protocol:** TokenWorks (`tokenworks`) · NFT Automated Strategies · Ethereum
- **DefiLlama:** https://defillama.com/protocol/tokenworks
- **PRIORITY 34.89**  =  LIKELIHOOD 41.05 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 9.15/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $3,195,334 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`PunkStrategyPatch` @ 0x1244EAe9…(ethereum), `NFTStrategyFactory` @ 0xA1a196b5…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for PunkStrategyPatch@0x1244EAe9…(ethereum), NFTStrategyFactory@0xA1a196b5…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#tokenworks|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#tokenworks`
- **Disclosure:** https://www.nftstrategy.fun/ · no audit link listed

### 37. set.wtf  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking A — priority (likelihood × actionability)):** 37
- **Protocol:** set.wtf (`set.wtf`) · Yield · Ethereum
- **DefiLlama:** https://defillama.com/protocol/set.wtf
- **PRIORITY 34.54**  =  LIKELIHOOD 46.05 × ACTIONABILITY 75.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 9.15/50
    - actionability: small enough to be unwatched, large enough to matter; no public disclosure channel listed
- **Value at risk:** $320,265 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source (`LiquidityPool` @ 0x2506CB86…(ethereum)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for LiquidityPool@0x2506CB86…(ethereum); indicators matched: unsafe_cross_sign_cast
- **Preconditions PRESENT / UNKNOWN:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** safecast_used / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#set.wtf|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#set.wtf`
- **Disclosure:** not listed · no audit link listed

### 38. ZyFAI  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 38
- **Protocol:** ZyFAI (`zyfai`) · AI Agents · Base, Arbitrum, Ethereum, Sonic, Plasma
- **DefiLlama:** https://defillama.com/protocol/zyfai
- **PRIORITY 33.67**  =  LIKELIHOOD 56.12 × ACTIONABILITY 60.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 19.22/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $10,278,463 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`BeaconProxy` @ 0x05d28A86…(arbitrum), `PendleStargateLPSY` @ 0x068def65…(arbitrum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for BeaconProxy@0x05d28A86…(arbitrum), PendleStargateLPSY@0x068def65…(arbitrum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#zyfai|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#zyfai`
- **Disclosure:** https://zyf.ai · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.zyf.ai/audits

### 39. Connext  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 39
- **Protocol:** Connext (`connext`) · Bridge · Ethereum, Linea, Arbitrum, Metis, Base, Mode …
- **DefiLlama:** https://defillama.com/protocol/connext
- **PRIORITY 33.17**  =  LIKELIHOOD 55.28 × ACTIONABILITY 60.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 23.38/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $29,891,550 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`TransparentUpgradeableProxy` @ 0xC8140dA3…(ethereum), `ConnextERC20` @ 0xfe67a445…(ethereum)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for TransparentUpgradeableProxy@0xC8140dA3…(ethereum), ConnextERC20@0xfe67a445…(ethereum); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#connext|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#connext`
- **Disclosure:** https://connext.network/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://drive.google.com/file/d/1l42vxzHwLXrKU10v3FutG2DWthU43vB8/view?pli=1

### 40. Fake World Assets  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 40
- **Protocol:** Fake World Assets (`fake-world-assets`) · Gamified Mining · Ethereum
- **DefiLlama:** https://defillama.com/protocol/fake-world-assets
- **PRIORITY 32.58**  =  LIKELIHOOD 38.33 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 6.43/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $3,669,630 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#fake-world-assets|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#fake-world-assets`
- **Disclosure:** https://www.fwa.fun · no audit link listed

### 41. Zora Bridge  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 41
- **Protocol:** Zora Bridge (`zora-bridge`) · Canonical Bridge · Ethereum
- **DefiLlama:** https://defillama.com/protocol/zora-bridge
- **PRIORITY 32.58**  =  LIKELIHOOD 38.33 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 6.43/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $5,590,658 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ChiToken` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ChiToken@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#zora-bridge|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#zora-bridge`
- **Disclosure:** https://zora.co/ · no audit link listed

### 42. OpenEden USDO  —  `SIG-VERIFIER-DEFEATABLE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 42
- **Protocol:** OpenEden USDO (`openeden-usdo`) · RWA · Ripple, Ethereum, Polygon, Binance, Base, Arbitrum
- **DefiLlama:** https://defillama.com/protocol/openeden-usdo
- **PRIORITY 32.19**  =  LIKELIHOOD 53.65 × ACTIONABILITY 60.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 16.75/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $24,618,886 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A verification routine must reject malformed, empty or zero-recovered signatures, and must never treat address(0) as a match.
    - Deployed source (`YieldCoin` @ 0xbf0f2f3a…(ethereum), `DSToken` @ 0xaf884853…(ethereum)): prerequisites matched: ecrecover_without_zero_check; no guard found
    - deployed source read for YieldCoin@0xbf0f2f3a…(ethereum), DSToken@0xaf884853…(ethereum); indicators matched: ecrecover_without_zero_check
- **Preconditions PRESENT / UNKNOWN:** src::ecrecover_without_zero_check, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** uses_oz_ecdsa / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** OZ ECDSA library in the deployed bytecode (kills the ecrecover-zero shape); Signer address immutable and non-zero
- **Where to start:** On a fork, submit r=0,s=0,v=27 and an empty signature to every signature-gated entrypoint; all must revert.
- **Evidence:** `protocols/deep_screened.jsonl#openeden-usdo|SIG-VERIFIER-DEFEATABLE`, `protocols/onchain_probes.json#openeden-usdo`
- **Disclosure:** https://openeden.com/usdo · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://www.chainsecurity.com/security-audit/openeden-usdoexpress

### 43. Zethr  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 43
- **Protocol:** Zethr (`zethr`) · Prediction Market · Ethereum
- **DefiLlama:** https://defillama.com/protocol/zethr
- **PRIORITY 31.03**  =  LIKELIHOOD 41.37 × ACTIONABILITY 75.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 9.47/50
    - actionability: small enough to be unwatched, large enough to matter; no public disclosure channel listed
- **Value at risk:** $676,424 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#zethr|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#zethr`
- **Disclosure:** not listed · no audit link listed

### 44. Rook  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 44
- **Protocol:** Rook (`rook`) · Dexs · Ethereum
- **DefiLlama:** https://defillama.com/protocol/rook
- **PRIORITY 30.93**  =  LIKELIHOOD 48.48 × ACTIONABILITY 63.8%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 16.58/50
    - actionability: mid-band: a team of this size will usually take an outside report; no public disclosure channel listed
- **Value at risk:** $1,124,358 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`LiquidityPoolV2` @ 0x35fFd6E2…(ethereum), `Unitroller` @ 0x3d981921…(ethereum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for LiquidityPoolV2@0x35fFd6E2…(ethereum), Unitroller@0x3d981921…(ethereum); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#rook|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#rook`
- **Disclosure:** not listed · no audit link listed

### 45. Sprinter  —  `ACC-DONATION-UNACCOUNTED-BALANCE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 45
- **Protocol:** Sprinter (`sprinter`) · Yield · Base
- **DefiLlama:** https://defillama.com/protocol/sprinter
- **PRIORITY 30.33**  =  LIKELIHOOD 35.68 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 3.78/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,139,725 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A share price, exchange rate or totalAssets must be a function of value the protocol accounted for on entry. Reading a raw balance makes any direct transfer into the accounting boundary an unpriced increase in every holder's claim.
    - Deployed source (`ArcisVault` @ 0x00325d9d…(base), `ReturnFinanceCompoundV3USDCVault` @ 0x0271A46c…(base)): prerequisites matched: totalAssets_reads_balanceOf; no guard found
    - deployed source read for ArcisVault@0x00325d9d…(base), ReturnFinanceCompoundV3USDCVault@0x0271A46c…(base); indicators matched: totalAssets_reads_balanceOf
- **Preconditions PRESENT / UNKNOWN:** src::totalAssets_reads_balanceOf, unprivileged_inbound_transfer_possible, live_value_exposed / src::getCashPrior_balanceOf
- **Guards searched / found:** internal_cash_counter / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** totalAssets derived from an internal counter, not balanceOf (kills the pair); Rate is monotonic and rate-limited per block; Inbound transfers to the accounting boundary are rejected or swept to a reserve
- **Where to start:** On a fork, transfer an arbitrary amount of each counted asset directly into every accounting boundary; the share price, exchange rate and derived borrow power must not change.
- **Evidence:** `protocols/deep_screened.jsonl#sprinter|ACC-DONATION-UNACCOUNTED-BALANCE`, `protocols/onchain_probes.json#sprinter`
- **Disclosure:** https://sprinter.tech/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/sprintertech/sprinter-stash-contracts/tree/main/audits

### 46. DxSale  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 46
- **Protocol:** DxSale (`dxsale`) · Launchpad · Binance, Ethereum, Base, Arbitrum, Polygon, Avalanche …
- **DefiLlama:** https://defillama.com/protocol/dxsale
- **PRIORITY 28.7**  =  LIKELIHOOD 47.83 × ACTIONABILITY 60.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 15.93/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $15,934,950 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 79.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`MainToken` @ 0xF063fE1a…(ethereum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for MainToken@0xF063fE1a…(ethereum); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#dxsale|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#dxsale`
- **Disclosure:** https://dx.app · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://www.certik.org/projects/dxsale

### 47. Superform  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 47
- **Protocol:** Superform (`superform`) · Yield Aggregator · Ethereum, Base, Polygon, Optimism, Arbitrum, Linea …
- **DefiLlama:** https://defillama.com/protocol/superform
- **PRIORITY 27.88**  =  LIKELIHOOD 46.47 × ACTIONABILITY 60.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 14.57/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $17,426,155 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`SuperVaultAggregator` @ 0x10AC0b33…(base)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for SuperVaultAggregator@0x10AC0b33…(base); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#superform|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#superform`
- **Disclosure:** https://app.superform.xyz · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/superform-xyz/superform-core/tree/main/security-review, https://github.com/superform-xyz/v2-core/tree/dev/audits

### 48. g8keep  —  `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 48
- **Protocol:** g8keep (`g8keep`) · Launchpad · Base
- **DefiLlama:** https://defillama.com/protocol/g8keep
- **PRIORITY 27.67**  =  LIKELIHOOD 36.9 × ACTIONABILITY 75.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 0.0/50
    - actionability: small enough to be unwatched, large enough to matter; no public disclosure channel listed
- **Value at risk:** $151,873 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.
    - Deployed source (`g8keepFactory` @ 0x3C0B4386…(base)): prerequisites matched: caller_named_asset_no_registry_check; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): value_fn_moves_caller_named_asset=yes
    - deployed source read for g8keepFactory@0x3C0B4386…(base); indicators matched: caller_named_asset_no_registry_check, value_fn_moves_caller_named_asset
- **Preconditions PRESENT / UNKNOWN:** src::caller_named_asset_no_registry_check, live_value_present, deployment_reachable_on_chain / src::token_hook_credits_without_sender_check
- **Guards searched / found:** asset_registry_check_present / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Every identifier derived or verified against the factory/registry (kills the pair); Routing restricted to an immutable venue allowlist
- **Where to start:** On a fork, create a fake pool/mint and pass it to every identifier-accepting entrypoint; all must revert.
- **Evidence:** `protocols/deep_screened.jsonl#g8keep|ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`, `protocols/onchain_probes.json#g8keep`
- **Disclosure:** not listed · no audit link listed

### 49. HOPE Collateral  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 49
- **Protocol:** HOPE Collateral (`hope-collateral`) · Basis Trading · Bitcoin, Ethereum
- **DefiLlama:** https://defillama.com/protocol/hope-collateral
- **PRIORITY 26.99**  =  LIKELIHOOD 42.3 × ACTIONABILITY 63.8%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 10.4/50
    - actionability: mid-band: a team of this size will usually take an outside report; no public disclosure channel listed
- **Value at risk:** $1,571,980 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#hope-collateral|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#hope-collateral`
- **Disclosure:** not listed · no audit link listed

### 50. Sobal  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 50
- **Protocol:** Sobal (`sobal`) · Dexs · Base, Neon
- **DefiLlama:** https://defillama.com/protocol/sobal
- **PRIORITY 26.64**  =  LIKELIHOOD 35.52 × ACTIONABILITY 75.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 3.62/50
    - actionability: small enough to be unwatched, large enough to matter; no public disclosure channel listed
- **Value at risk:** $58,376 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`Vault` @ 0x03c01aca…(base)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for Vault@0x03c01aca…(base); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#sobal|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#sobal`
- **Disclosure:** not listed · no audit link listed

### 51. Camelot V3  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking A — priority (likelihood × actionability)):** 51
- **Protocol:** Camelot V3 (`camelot-v3`) · Dexs · Arbitrum, ApeChain, Superposition, Gravity, Plume Mainnet, EDU Chain …
- **DefiLlama:** https://defillama.com/protocol/camelot-v3
- **PRIORITY 25.74**  =  LIKELIHOOD 42.9 × ACTIONABILITY 60.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 6.0/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $14,825,186 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
- **Broken invariant tested:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source (`AlgebraFactory` @ 0x1a3c9B1d…(arbitrum), `StakedUSDX` @ 0x7788a353…(arbitrum)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for AlgebraFactory@0x1a3c9B1d…(arbitrum), StakedUSDX@0x7788a353…(arbitrum); indicators matched: unsafe_cross_sign_cast
- **Preconditions PRESENT / UNKNOWN:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** safecast_used / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#camelot-v3|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#camelot-v3`
- **Disclosure:** https://camelot.exchange/ · no audit link listed

### 52. Yield Yak Aggregator  —  `BRIDGE-MESSAGE-NOT-BOUND-TO-SOURCE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 52
- **Protocol:** Yield Yak Aggregator (`yield-yak-aggregator`) · Yield Aggregator · Avalanche, Arbitrum, Base, Mantle
- **DefiLlama:** https://defillama.com/protocol/yield-yak-aggregator
- **PRIORITY 24.14**  =  LIKELIHOOD 40.23 × ACTIONABILITY 60.0%
    - likelihood = family evidence 30.0/50 (MATCH 60.0 × evidence weight 1.0) + learned attack surface 10.23/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $15,139,245 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 60.0 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
- **Broken invariant tested:** A release, mint or payout on the destination domain must be authorised only by a proof that binds, simultaneously: the source chain identity, the source channel/route, the exact asset, the exact amount, the recipient, and a nonce that is consumed exactly once. Verifying that a message is well-formed or correctly signed is not the same as verifying that it corresponds to a real deposit of equal value.
    - Deployed source (`YakTokenOFTV2` @ 0x7f4dB37D…(arbitrum)): prerequisites matched: xdomain_entrypoint_present, xdomain_no_endpoint_check; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): xdomain_nonce_not_consumed=yes
    - deployed source read for YakTokenOFTV2@0x7f4dB37D…(arbitrum); indicators matched: xdomain_entrypoint_present, xdomain_no_endpoint_check, xdomain_nonce_not_consumed
- **Preconditions PRESENT / UNKNOWN:** src::xdomain_entrypoint_present, src::xdomain_no_endpoint_check, live_value_present, deployment_reachable_on_chain / src::xdomain_source_not_bound, src::token_hook_credits_without_sender_check
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Destination mint requires a Merkle/zk proof against a source state root that itself commits to the amount; Reserve reconciliation is enforced on-chain (mint reverts if supply would exceed escrow); Bridge is one-way with no destination-side release
- **Where to start:** On a pinned fork of the destination chain, no sequence of destination-side calls may increase redeemable value without a matching, previously unconsumed source commitment of equal value.
- **Evidence:** `protocols/deep_screened.jsonl#yield-yak-aggregator|BRIDGE-MESSAGE-NOT-BOUND-TO-SOURCE`, `protocols/onchain_probes.json#yield-yak-aggregator`
- **Disclosure:** https://yieldyak.com · no audit link listed

### 53. Metronome Synth  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 53
- **Protocol:** Metronome Synth (`metronome-synth`) · Synthetics · Ethereum, Optimism, Base
- **DefiLlama:** https://defillama.com/protocol/metronome-synth
- **PRIORITY 23.84**  =  LIKELIHOOD 39.73 × ACTIONABILITY 60.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 7.83/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $11,377,509 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ChiToken` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ChiToken@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#metronome-synth|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#metronome-synth`
- **Disclosure:** https://www.metronome.io/synth · no audit link listed
