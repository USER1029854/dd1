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
| Candidates | 163 |
| Previously hacked | 8 |
| Repeat victims (2+ recorded hacks) | 2 |
| Median value at risk | $822,973 |
| Total value at risk | $559,378,737 |
| At L4 guard review | 163 |
| Distinct mechanism families | 16 |
| Previously delivered (withheld from this list) | 433 |

### The size of this list is set by evidence, not by a round number

Every fresh protocol reaching **`L4_GUARD_REVIEW`** is here — 163 of them — rather than the ranking being truncated at some count. A count is an arbitrary cut through a ranking; an evidence level is a statement about how deeply each entry was actually read. At this level the protocol's deployed source was fetched, proxies were followed to their implementations, the family's documented preconditions were evaluated against that source, and its decisive guards were searched for and not found in the reviewed path.

### Every protocol here is one you have not been given before

A candidate list is a queue of work, not a leaderboard. **433 protocols that survive screening were withheld from this run because earlier runs already handed them over** across 8 previous deliveries. They are not resolved and not ruled out — they were already given to you, so repeating them would hand you no new work.

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

The full ledger is `protocols/delivered_ledger.json`, reconstructed from git history rather than from anything remembered between runs. Every withheld protocol still appears in `candidates_all.csv` with `previously_delivered=YES` and the run that delivered it, so nothing is hidden — it is only kept out of the queue.

<details><summary>The 433 withheld protocols</summary>

`88mph`, `8lends`, `aave-v1`, `aave-v3`, `aavegotchi`, `abracadabra-spell`, `abstradex`, `accountable`, `accumulated-finance-liquid-staking`, `across`, `adi-bridge`, `aerodrome-ignition`, `agave`, `ajna-v1`, `ajna-v2`, `aloe`, `alongside`, `alphax`, `altitude.fi`, `ammalgam-dlex`, `amphor`, `angle`, `ankr`, `ante-finance`, `antfarm-finance`, `anthias-labs`, `anvil`, `anzen-v2`, `aperocket`, `apeswap-amm`, `apostro`, `arbinyan`, `arcade.xyz`, `arcadia-v2`, `arch`, `asseto-cash+`, `astaria-v2`, `asymmetry-usdaf`, `aura`, `autopilot`, `axelar-cross-chain`, `b-lucky`, `b.protocol`, `b.protocol-curator`, `babydoge-bridge`, `badger-dao`, `bakerfi`, `balancer-v1`, `balancer-v2`, `balancer-v3`, `bancor-v2.1`, `bancor-v3`, `basalt-vault`, `base-dollar`, `basedbid`, `bearnfi`, `bella-protocol`, `bifi`, `bima-cdp`, `biswap-v3`, `bitstable-finance`, `blackwing`, `bond-protocol`, `boringdao`, `bridge-mutual`, `bunni-v2`, `bunny`, `burgerswap`, `byzanlink-rwa-markets`, `cache.gold`, `cakepie`, `cana-holdings-california-carbon-credits`, `capyfi`, `caviar-v1`, `cega-v1`, `cega-v2`, `chainport`, `chamber-vaults`, `charm-finance-v1`, `clearpool-lending`, `clipper`, `clovis`, `conduit-bridge`, `conic-finance`, `contango-v1`, `convex-finance`, `cook-finance`, `cove-boosties`, `cover-protocol`, `cozy-v1`, `cream-lending`, `credit-coop`, `cronos-zkevm-bridge`, `crosschain-bridge`, `cryptex-v1`, `csigma-finance`, `cub-finance`, `curve-dex`, `curve-llamalend`, `cvi-finance`, `cytonic-airdrop-campaign`, `ddex`, `de1`, `debridge`, `defibox`, `defil`, `degenprime`, `deltaprime`, `delv-yield`, `deri-protocol`, `derivadex`, `derive-v1`, `dforce-lending`, `dfx-v2`, `dodo-amm`, `domani-protocol`, `dooar-v2`, `dopple-finance`, `dsf.finance`, `dtrinity-dlend`, `dtrinity-dusd`, `dydx-v3`, `dyson`, `easedefi.org`, `electra`, `elfi-protocol`, `elk`, `enosys-bridge`, `equilibria`, `ether.fi-liquid`, `everything`, `exactly`, `extra-finance-leverage-farming`, `ezmanager`, `ezmoney`, `finext-finance`, `finnexus`, `fira`, `flux-finance`, `flying-tulip-ftusd`, `flying-tulip-lend`, `fortunafi`, `fractional-art`, `frax-fpi`, `frax-swap`, `fuji-v1`, `fungify`, `gaib`, `gammaswap-open-interest`, `gauntlet`, `gearbox`, `geyser`, `gnosis-protocol-v1`, `goldsand-by-inshallah`, `goplus-locker-v2`, `granary-finance`, `gravita-protocol`, `grizzlyfi-hives`, `gro`, `guru-network-classic`, `gyroscope-protocol`, `harvest-finance`, `hashflow`, `hop-protocol`, `horizon-protocol`, `hundred-finance`, `hunny-finance`, `hydt-protocol`, `hyperjump`, `ichi`, `ideamarket`, `idle`, `immutablex`, `impermax-v2`, `impossible`, `indexed-finance`, `infinite-trading-protocol`, `insurace`, `insuredao`, `interest-protocol`, `international-meme-fund-v2`, `inverse-finance-firm`, `ipor-derivatives`, `iron-bank`, `itrust-finance`, `iziswap`, `izumi-liquidbox`, `jetfuel-finance`, `joe-dex`, `joe-v2`, `joe-v2.1`, `jones-dao`, `jpegd`, `juicebox-v3`, `katana-pre-launch`, `keep-network`, `keep3r-network`, `kine-finance`, `king-protocol`, `kinza-finance`, `kokonut-swap`, `kromatika`, `krystal-community-vault`, `kyberswap-classic`, `kyberswap-elastic`, `landshare`, `landx-finance`, `lendflare`, `likwid`, `liquid-finance`, `lista-cdp`, `listapie`, `liveart`, `lixir-finance`, `lockon`, `loop`, `lucidly-finance`, `lybra-v1`, `magic-eden`, `makina`, `maverick-v1`, `maxshot`, `mayan-bridge`, `mcdex`, `mellow-yield`, `mero`, `mesher`, `meter-passport`, `mezo-bridge`, `midas-capital`, `mim-swap`, `mint-club-v2`, `mitosis`, `mochifi`, `moneyfi`, `monolith-market`, `moonwell-lending`, `moremarkets.xyz`, `morph-bridge`, `morpheusai`, `morpho-optimizer-aavev2`, `mortgagefi`, `mountain-protocol`, `muffin`, `multichain`, `mummy-finance`, `muscadine`, `myx-finance`, `nerona`, `nested`, `nftx`, `niob-finance`, `nomad`, `nomiswap`, `nucleus`, `olive-network`, `onx-finance`, `openeden-prism`, `openleverage`, `opium`, `orbit-bridge`, `orderly-bridge`, `ordernchaos`, `oreoswap`, `orion-pools`, `otsea`, `overtime`, `padswap`, `peakdefi`, `peapods-finance`, `pell-network`, `penpie`, `pepeteam-bridge`, `percent-finance`, `picwe`, `piku-finance`, `planet-farm`, `plutusdao`, `pooltogether-v3`, `pooltogether-v4`, `pooltogether-v5`, `prdt`, `premia-v2`, `premia-v3`, `preon-finance`, `printr`, `prismalst`, `privacy-cash`, `privacy-pools`, `pstake-lsd`, `puffer-unifi`, `qidao`, `quickswap-v4`, `radiant-v2`, `radioshack`, `rank-trading`, `rari-capital`, `reflexer`, `reservoir-protocol`, `resonate-finance`, `revault`, `revert-compoundor`, `revest-finance`, `rezerve-money`, `ronin-bridge`, `royco-v1`, `royco-v2`, `rubicon`, `rumpel-labs`, `sablier-legacy`, `saddle-finance`, `saffron-vaults`, `satlayer`, `sato`, `savvy`, `sector-finance`, `sectorone-dlmm`, `segment-finance`, `sentora`, `set-protocol`, `shape-bridge`, `sherlock`, `shift-protocol`, `shimmerbridge`, `sigma-money`, `silo-v1`, `silo-v2`, `silo-v3`, `single-finance`, `singular-farm`, `singularitydao`, `singularx`, `sir`, `skate-fi`, `smardex-amm`, `smartcredit`, `snowswap`, `snuggle`, `sofa.org`, `solo-top`, `sommelier`, `sparklend`, `spectra-metavaults-outside-v2`, `spectra-v1`, `sperax-usd`, `stability`, `stabull-finance`, `stafi`, `stake-dao`, `stargate-v1`, `steakhut-liquidity`, `steer-protocol`, `stonedefi`, `strata-season-0`, `sturdy-v2`, `sudoswap-v1`, `sumer.money`, `sunx-bridge`, `superreturn`, `sushi-bentobox`, `sushiswap`, `swaap-maker-v2`, `swapr-v2`, `swell-earn`, `swellchain-bridge`, `synapse-cross-chain-bridge`, `synfutures-v1`, `tangent-finance`, `tanken-capital`, `tarot`, `tau-labs`, `termfinance-vaults`, `terminal-finance-pre-deposits`, `tetu-earn`, `the-idols`, `thedeep`, `theoriq-alphavault-eth`, `theoriq-gold-vault`, `thesauros`, `threshold-thusd`, `thruster-v2`, `tidaldex`, `tokenlon-amm`, `tranchess-yield`, `treedefi`, `trevee-earn`, `twindex`, `ufarm-digital`, `ultrayield-vaults`, `umami-finance`, `unagii`, `unifarm`, `union-protocol`, `unitus`, `unsheth`, `unslashed`, `usdfi-lending`, `uwu-lend`, `valuedefi`, `varen`, `vault-street-primeusd`, `vaultcraft`, `velvet-v2`, `velvet-v3`, `venombridge`, `venus-core-pool`, `venus-isolated-pools`, `voltz`, `wasabi-perps`, `wasabix`, `wavesbridge`, `wepiggy`, `wing-finance`, `wombex-finance`, `wompie`, `xgld`, `xtoken`, `xwin-finance`, `yala`, `yam-finance`, `yaxis`, `yay!`, `yearn-finance`, `yellow`, `yield-millionaire`, `yield-protocol`, `yieldflow-yield-farming`, `yieldnest`, `yieldwolf`, `zero-network`, `zerolend-lending`, `zoo-finance`, `zunami-protocol`

</details>

### Repeat victims in this list

Whatever allowed a second incident has not necessarily been removed. These are the highest-conviction entries in the set.

| Protocol | Hacks | Family | Priority | At risk |
|---|---:|---|---:|---:|
| [Impermax V3](https://defillama.com/protocol/impermax-v3) | 2 | `AUTH-ZERO-ADDRESS-ACCEPTED` | 42.08 | $98,183 |
| [Inverse Finance Frontier](https://defillama.com/protocol/inverse-finance-frontier) | 2 | `AUTH-ZERO-ADDRESS-ACCEPTED` | 37.82 | $4,540,643 |

### Diversified shortlist — top 3 per family

| # | Protocol | Family | Priority | Likelihood | At risk | Evidence |
|---:|---|---|---:|---:|---:|---|
| 1 | [Secured Finance Lending](https://defillama.com/protocol/secured-finance-lending) | `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED` | 53.47 | 53.47 | $255,358 | `L4_GUARD_REVIEW` |
| 2 | [Alvara](https://defillama.com/protocol/alvara) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 52.18 | 52.18 | $52,244 | `L4_GUARD_REVIEW` |
| 3 | [AirPuff](https://defillama.com/protocol/airpuff) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 52.15 | 52.15 | $663,289 | `L4_GUARD_REVIEW` |
| 4 | [Volmex](https://defillama.com/protocol/volmex) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 51.55 | 51.55 | $132,456 | `L4_GUARD_REVIEW` |
| 5 | [Sera](https://defillama.com/protocol/sera) | `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED` | 49.83 | 49.83 | $152,113 | `L4_GUARD_REVIEW` |
| 6 | [Legion](https://defillama.com/protocol/legion) | `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED` | 49.83 | 49.83 | $618,220 | `L4_GUARD_REVIEW` |
| 7 | [Alcum](https://defillama.com/protocol/alcum) | `ACC-NAV-SHAREPRICE-MANIPULABLE` | 49.72 | 49.72 | $231,089 | `L4_GUARD_REVIEW` |
| 8 | [APY Finance](https://defillama.com/protocol/apy-finance) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 49.65 | 49.65 | $413,977 | `L4_GUARD_REVIEW` |
| 9 | [Metronome V1](https://defillama.com/protocol/metronome-v1) | `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET` | 49.55 | 49.55 | $226,136 | `L4_GUARD_REVIEW` |
| 10 | [Wrap Protocol](https://defillama.com/protocol/wrap-protocol) | `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET` | 49.55 | 49.55 | $540,062 | `L4_GUARD_REVIEW` |
| 11 | [UniPower](https://defillama.com/protocol/unipower) | `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET` | 48.87 | 48.87 | $259,279 | `L4_GUARD_REVIEW` |
| 12 | [Hidden Hand](https://defillama.com/protocol/hidden-hand) | `PROOF-VERIFICATION-BYPASSED` | 47.83 | 47.83 | $67,215 | `L4_GUARD_REVIEW` |
| 13 | [ZKcandy Bridge](https://defillama.com/protocol/zkcandy-bridge) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 46.37 | 46.37 | $683,034 | `L4_GUARD_REVIEW` |
| 14 | [Nocturne](https://defillama.com/protocol/nocturne) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 44.88 | 44.88 | $78,408 | `L4_GUARD_REVIEW` |
| 15 | [Demeter](https://defillama.com/protocol/demeter) | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | 44.85 | 44.85 | $284,331 | `L4_GUARD_REVIEW` |
| 16 | [GMD Protocol](https://defillama.com/protocol/gmd-protocol) | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | 44.72 | 44.72 | $971,646 | `L4_GUARD_REVIEW` |
| 17 | [MORE Vaults](https://defillama.com/protocol/more-vaults) | `ACC-DONATION-UNACCOUNTED-BALANCE` | 44.68 | 44.68 | $822,973 | `L4_GUARD_REVIEW` |
| 18 | [Lynx](https://defillama.com/protocol/lynx) | `PROOF-VERIFICATION-BYPASSED` | 44.35 | 44.35 | $192,608 | `L4_GUARD_REVIEW` |
| 19 | [Etherfuse](https://defillama.com/protocol/etherfuse) | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | 44.1 | 44.1 | $977,586 | `L4_GUARD_REVIEW` |
| 20 | [Hats.V2](https://defillama.com/protocol/hats.v2) | `AUTH-ZERO-ADDRESS-ACCEPTED` | 44.05 | 44.05 | $161,281 | `L4_GUARD_REVIEW` |
| 21 | [Xave Finance](https://defillama.com/protocol/xave-finance) | `PROOF-VERIFICATION-BYPASSED` | 43.82 | 43.82 | $149,205 | `L4_GUARD_REVIEW` |
| 22 | [Aarna Protocol](https://defillama.com/protocol/aarna-protocol) | `ACC-DONATION-UNACCOUNTED-BALANCE` | 43.67 | 43.67 | $392,025 | `L4_GUARD_REVIEW` |
| 23 | [Hyperdrive](https://defillama.com/protocol/hyperdrive) | `ACC-DUPLICATE-ID-ACCUMULATION` | 43.67 | 43.67 | $71,676 | `L4_GUARD_REVIEW` |
| 24 | [ApeSwap Lending](https://defillama.com/protocol/apeswap-lending) | `AUTH-ZERO-ADDRESS-ACCEPTED` | 43.45 | 43.45 | $219,009 | `L4_GUARD_REVIEW` |
| 25 | [maxAPY](https://defillama.com/protocol/maxapy) | `AUTH-ZERO-ADDRESS-ACCEPTED` | 42.98 | 42.98 | $61,721 | `L4_GUARD_REVIEW` |
| 26 | [Fyde Protocol](https://defillama.com/protocol/fyde-protocol) | `BRIDGE-MESSAGE-NOT-BOUND-TO-SOURCE` | 42.03 | 42.03 | $376,264 | `L4_GUARD_REVIEW` |
| 27 | [RollX](https://defillama.com/protocol/rollx) | `BRIDGE-MESSAGE-NOT-BOUND-TO-SOURCE` | 41.8 | 41.8 | $444,294 | `L4_GUARD_REVIEW` |
| 28 | [Almanak](https://defillama.com/protocol/almanak) | `BRIDGE-MESSAGE-NOT-BOUND-TO-SOURCE` | 41.15 | 41.15 | $460,254 | `L4_GUARD_REVIEW` |
| 29 | [Gremlix](https://defillama.com/protocol/gremlix) | `ACC-NAV-SHAREPRICE-MANIPULABLE` | 39.88 | 39.88 | $118,352 | `L4_GUARD_REVIEW` |
| 30 | [Mycelium Perpetual Pools](https://defillama.com/protocol/mycelium-perpetual-pools) | `ACC-DUPLICATE-ID-ACCUMULATION` | 39.67 | 39.67 | $179,980 | `L4_GUARD_REVIEW` |

---

### 1. Secured Finance Lending  —  `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 1
- **Protocol:** Secured Finance Lending (`secured-finance-lending`) · Lending · Ethereum, Filecoin, Arbitrum, Avalanche, Polygon zkEVM
- **DefiLlama:** https://defillama.com/protocol/secured-finance-lending
- **PRIORITY 53.47**  =  LIKELIHOOD 53.47 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 16.57/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $255,358 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.
    - Deployed source (`CurrencyController` @ 0xd024f3d3…(ethereum), `TokenVault` @ 0x4675b157…(ethereum)): prerequisites matched: caller_named_asset_no_registry_check; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): value_fn_moves_caller_named_asset=yes
    - deployed source read for CurrencyController@0xd024f3d3…(ethereum), TokenVault@0x4675b157…(ethereum); indicators matched: caller_named_asset_no_registry_check, value_fn_moves_caller_named_asset
- **Preconditions PRESENT / UNKNOWN:** src::caller_named_asset_no_registry_check, live_value_present, deployment_reachable_on_chain / src::token_hook_credits_without_sender_check
- **Guards searched / found:** asset_registry_check_present / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Every identifier derived or verified against the factory/registry (kills the pair); Routing restricted to an immutable venue allowlist
- **Where to start:** On a fork, create a fake pool/mint and pass it to every identifier-accepting entrypoint; all must revert.
- **Evidence:** `protocols/deep_screened.jsonl#secured-finance-lending|ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`, `protocols/onchain_probes.json#secured-finance-lending`
- **Disclosure:** https://secured.finance · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/Secured-Finance/contracts/blob/develop/audits/2023-12-Quantstamp.pdf

### 2. Alvara  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking A — priority (likelihood × actionability)):** 2
- **Protocol:** Alvara (`alvara`) · Yield Aggregator · Ethereum, Base
- **DefiLlama:** https://defillama.com/protocol/alvara
- **PRIORITY 52.18**  =  LIKELIHOOD 52.18 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 15.28/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $52,244 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
- **Broken invariant tested:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source (`Alvara` @ 0x5669fa5a…(ethereum), `Factory` @ 0xcfd5475a…(ethereum)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for Alvara@0x5669fa5a…(ethereum), Factory@0xcfd5475a…(ethereum); indicators matched: unsafe_cross_sign_cast
- **Preconditions PRESENT / UNKNOWN:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** safecast_used / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#alvara|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#alvara`
- **Disclosure:** https://alvara.xyz · no audit link listed

### 3. AirPuff  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking A — priority (likelihood × actionability)):** 3
- **Protocol:** AirPuff (`airpuff`) · Leveraged Farming · Ethereum, Arbitrum, Mode, K2, zkLink, Mantle
- **DefiLlama:** https://defillama.com/protocol/airpuff
- **PRIORITY 52.15**  =  LIKELIHOOD 52.15 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 15.25/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $663,289 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
- **Broken invariant tested:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source (`AirPuff1XsvETH` @ 0x4265cfe1…(ethereum), `PendlePrincipalToken` @ 0x094bE6bD…(ethereum)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for AirPuff1XsvETH@0x4265cfe1…(ethereum), PendlePrincipalToken@0x094bE6bD…(ethereum); indicators matched: unsafe_cross_sign_cast
- **Preconditions PRESENT / UNKNOWN:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** safecast_used / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#airpuff|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#airpuff`
- **Disclosure:** https://www.airpuff.io · no audit link listed

### 4. Volmex  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 4
- **Protocol:** Volmex (`volmex`) · Yield · Arbitrum, Ethereum, Polygon
- **DefiLlama:** https://defillama.com/protocol/volmex
- **PRIORITY 51.55**  =  LIKELIHOOD 51.55 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 14.65/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $132,456 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`BlurPool` @ 0x01a65602…(ethereum), `TrueGBP` @ 0x00000000…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for BlurPool@0x01a65602…(ethereum), TrueGBP@0x00000000…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#volmex|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#volmex`
- **Disclosure:** https://volmex.finance/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.volmex.finance/smart-contracts/audits

### 5. Sera  —  `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 5
- **Protocol:** Sera (`sera`) · Dexs · Ethereum
- **DefiLlama:** https://defillama.com/protocol/sera
- **PRIORITY 49.83**  =  LIKELIHOOD 49.83 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 12.93/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $152,113 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.
    - Deployed source (`Sera` @ 0xB5C50C5D…(ethereum), `Vault` @ 0xC7d4Fd26…(ethereum)): prerequisites matched: caller_named_asset_no_registry_check; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): value_fn_moves_caller_named_asset=yes
    - deployed source read for Sera@0xB5C50C5D…(ethereum), Vault@0xC7d4Fd26…(ethereum); indicators matched: caller_named_asset_no_registry_check, value_fn_moves_caller_named_asset
- **Preconditions PRESENT / UNKNOWN:** src::caller_named_asset_no_registry_check, live_value_present, deployment_reachable_on_chain / src::token_hook_credits_without_sender_check
- **Guards searched / found:** asset_registry_check_present / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Every identifier derived or verified against the factory/registry (kills the pair); Routing restricted to an immutable venue allowlist
- **Where to start:** On a fork, create a fake pool/mint and pass it to every identifier-accepting entrypoint; all must revert.
- **Evidence:** `protocols/deep_screened.jsonl#sera|ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`, `protocols/onchain_probes.json#sera`
- **Disclosure:**   · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.sera.cx/contracts/audits/

### 6. Legion  —  `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 6
- **Protocol:** Legion (`legion`) · Launchpad · Ethereum
- **DefiLlama:** https://defillama.com/protocol/legion
- **PRIORITY 49.83**  =  LIKELIHOOD 49.83 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 12.93/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $618,220 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.
    - Deployed source (`LegionPreLiquidSaleV2Factory` @ 0xa0BeB0A8…(ethereum)): prerequisites matched: caller_named_asset_no_registry_check; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): value_fn_moves_caller_named_asset=yes
    - deployed source read for LegionPreLiquidSaleV2Factory@0xa0BeB0A8…(ethereum); indicators matched: caller_named_asset_no_registry_check, value_fn_moves_caller_named_asset
- **Preconditions PRESENT / UNKNOWN:** src::caller_named_asset_no_registry_check, live_value_present, deployment_reachable_on_chain / src::token_hook_credits_without_sender_check
- **Guards searched / found:** asset_registry_check_present / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Every identifier derived or verified against the factory/registry (kills the pair); Routing restricted to an immutable venue allowlist
- **Where to start:** On a fork, create a fake pool/mint and pass it to every identifier-accepting entrypoint; all must revert.
- **Evidence:** `protocols/deep_screened.jsonl#legion|ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`, `protocols/onchain_probes.json#legion`
- **Disclosure:** https://legion.cc · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/Legion-Team/legion-protocol-contracts/tree/master/audits

### 7. Alcum  —  `ACC-NAV-SHAREPRICE-MANIPULABLE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 7
- **Protocol:** Alcum (`alcum`) · Yield · Ethereum
- **DefiLlama:** https://defillama.com/protocol/alcum
- **PRIORITY 49.72**  =  LIKELIHOOD 49.72 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 17.82/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $231,089 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `owner_is_eoa` — raises likelihood, measured lift ×1.729 (weight +0.55)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** totalAssets() must equal value the vault could actually realise now. Any component valued at book, at a manipulable rate, or after economic impairment lets a redeemer convert other depositors' claims into their own.
    - Conditions: `MISREPRESENTED_TOKENS`
    - Deployed source (`EpochManager` @ 0x89a74594…(ethereum), `xCUP` @ 0x434a52ce…(ethereum)): prerequisites matched: totalAssets_reads_balanceOf; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): totalAssets_defined=yes
    - deployed source read for EpochManager@0x89a74594…(ethereum), xCUP@0x434a52ce…(ethereum); indicators matched: totalAssets_reads_balanceOf, totalAssets_defined
    - condition MISREPRESENTED_TOKENS (PRIORITY): DefiLlama flags this protocol's token accounting as misrepresented: its own indexer cannot reconcile the reported holdings, which is a direct accounting-integrity signal.
- **Preconditions PRESENT / UNKNOWN:** src::totalAssets_reads_balanceOf, erc4626_style_totalAssets_live, live_pooled_depositor_value / multi_component_totalAssets
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Share price rate-limited per block (kills same-transaction extraction); Single-asset vault with no external valuation; Withdrawals queued with a delay and priced at settlement
- **Where to start:** On a fork, for each component, force its valuation to zero and to 10x; the vault's mint/redeem must revert or be bounded, never transfer more than the depositor's pro-rata realisable share.
- **Evidence:** `protocols/deep_screened.jsonl#alcum|ACC-NAV-SHAREPRICE-MANIPULABLE`, `protocols/onchain_probes.json#alcum`
- **Disclosure:** https://web3.alcum.com/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/unusnullus/alcum-smart/tree/main/audit

### 8. MORE Vaults  —  `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 8
- **Protocol:** MORE Vaults (`more-vaults`) · Onchain Capital Allocator · Flow, Base, Ethereum, Avalanche, Arbitrum
- **DefiLlama:** https://defillama.com/protocol/more-vaults
- **PRIORITY 49.68**  =  LIKELIHOOD 49.68 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 12.78/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $822,973 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
- **Broken invariant tested:** Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.
    - Deployed source (`VaultsFactory` @ 0x9084cc13…(base)): prerequisites matched: caller_named_asset_no_registry_check; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): value_fn_moves_caller_named_asset=yes
    - deployed source read for VaultsFactory@0x9084cc13…(base); indicators matched: caller_named_asset_no_registry_check, value_fn_moves_caller_named_asset
- **Preconditions PRESENT / UNKNOWN:** src::caller_named_asset_no_registry_check, live_value_present, deployment_reachable_on_chain / src::token_hook_credits_without_sender_check
- **Guards searched / found:** asset_registry_check_present / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Every identifier derived or verified against the factory/registry (kills the pair); Routing restricted to an immutable venue allowlist
- **Where to start:** On a fork, create a fake pool/mint and pass it to every identifier-accepting entrypoint; all must revert.
- **Evidence:** `protocols/deep_screened.jsonl#more-vaults|ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`, `protocols/onchain_probes.json#more-vaults`
- **Disclosure:** https://www.more.markets/ · no audit link listed

### 9. APY Finance  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 9
- **Protocol:** APY Finance (`apy-finance`) · Yield · Ethereum
- **DefiLlama:** https://defillama.com/protocol/apy-finance
- **PRIORITY 49.65**  =  LIKELIHOOD 49.65 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 12.75/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $413,977 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`APYPoolTokenProxy` @ 0x75CE0E50…(ethereum), `APYGovernanceTokenProxy` @ 0x95a4492F…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for APYPoolTokenProxy@0x75CE0E50…(ethereum), APYGovernanceTokenProxy@0x95a4492F…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#apy-finance|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#apy-finance`
- **Disclosure:** https://apy.finance · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/apy-finance/apy-audits

### 10. Metronome V1  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 10
- **Protocol:** Metronome V1 (`metronome-v1`) · Yield · Ethereum
- **DefiLlama:** https://defillama.com/protocol/metronome-v1
- **PRIORITY 49.55**  =  LIKELIHOOD 49.55 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 17.65/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $226,136 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#metronome-v1|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#metronome-v1`
- **Disclosure:** https://metronome.io/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/autonomoussoftware/metronome-audits

### 11. Wrap Protocol  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 11
- **Protocol:** Wrap Protocol (`wrap-protocol`) · Synthetics · Ethereum
- **DefiLlama:** https://defillama.com/protocol/wrap-protocol
- **PRIORITY 49.55**  =  LIKELIHOOD 49.55 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 17.65/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $540,062 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#wrap-protocol|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#wrap-protocol`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://leastauthority.com/blog/audit-of-wrap-protocol-smart-contracts-for-tezos-foundation

### 12. UniPower  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 12
- **Protocol:** UniPower (`unipower`) · Yield · Ethereum, Polygon
- **DefiLlama:** https://defillama.com/protocol/unipower
- **PRIORITY 48.87**  =  LIKELIHOOD 48.87 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 16.97/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $259,279 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#unipower|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#unipower`
- **Disclosure:** https://unipower.network · no audit link listed

### 13. Bridgers  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 13
- **Protocol:** Bridgers (`bridgers`) · Dexs · Tron, Ethereum, Binance, Base, Linea, Optimism …
- **DefiLlama:** https://defillama.com/protocol/bridgers
- **PRIORITY 48.65**  =  LIKELIHOOD 48.65 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 16.75/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $677,138 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#bridgers|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#bridgers`
- **Disclosure:** https://bridgers.ai/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://skynet.certik.com/zh-CN/projects/swft

### 14. HaloDAO  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 14
- **Protocol:** HaloDAO (`halodao`) · Yield · Polygon, Ethereum, Arbitrum
- **DefiLlama:** https://defillama.com/protocol/halodao
- **PRIORITY 48.25**  =  LIKELIHOOD 48.25 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 16.35/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $61,790 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#halodao|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#halodao`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.halodao.com/contract-audits/overview

### 15. Origin Dollar  —  `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 15
- **Protocol:** Origin Dollar (`origin-dollar`) · Yield Aggregator · Ethereum
- **DefiLlama:** https://defillama.com/protocol/origin-dollar
- **PRIORITY 47.83**  =  LIKELIHOOD 56.27 × ACTIONABILITY 85.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 19.37/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $5,688,238 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.
    - Deployed source (`OUSD` @ 0xa7b7c59a…(ethereum), `ExponentialStaking` @ 0x97711c7a…(ethereum)): prerequisites matched: caller_named_asset_no_registry_check; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): value_fn_moves_caller_named_asset=yes
    - deployed source read for OUSD@0xa7b7c59a…(ethereum), ExponentialStaking@0x97711c7a…(ethereum); indicators matched: caller_named_asset_no_registry_check, value_fn_moves_caller_named_asset
- **Preconditions PRESENT / UNKNOWN:** src::caller_named_asset_no_registry_check, live_value_present, deployment_reachable_on_chain / src::token_hook_credits_without_sender_check
- **Guards searched / found:** asset_registry_check_present / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `TIMELOCK`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Every identifier derived or verified against the factory/registry (kills the pair); Routing restricted to an immutable venue allowlist
- **Where to start:** On a fork, create a fake pool/mint and pass it to every identifier-accepting entrypoint; all must revert.
- **Evidence:** `protocols/deep_screened.jsonl#origin-dollar|ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`, `protocols/onchain_probes.json#origin-dollar`
- **Disclosure:** https://www.originprotocol.com/ousd · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.ousd.com/v/en/security-and-risks/audits

### 16. Hidden Hand  —  `PROOF-VERIFICATION-BYPASSED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 16
- **Protocol:** Hidden Hand (`hidden-hand`) · Governance Incentives · Ethereum, Optimism, Binance, Arbitrum
- **DefiLlama:** https://defillama.com/protocol/hidden-hand
- **PRIORITY 47.83**  =  LIKELIHOOD 47.83 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 15.93/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $67,215 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A withdrawal or mint gated by a proof must verify that proof against the correct verifying key, over all the public inputs that bind the action, and must reject when any component is absent.
    - Deployed source (`RewardDistributor` @ 0x0b139682…(ethereum), `RewardSwapper` @ 0x8d89593c…(ethereum)): prerequisites matched: proof_result_unchecked; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): verifier_address_mutable=no
    - deployed source read for RewardDistributor@0x0b139682…(ethereum), RewardSwapper@0x8d89593c…(ethereum); indicators matched: proof_result_unchecked
- **Preconditions PRESENT / UNKNOWN:** src::proof_result_unchecked, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Verifying key immutable and attested (kills the misconfiguration shape); No alternative release path exists (enumerate selectors)
- **Where to start:** On a fork, submit an empty proof, a proof for different public inputs, and a proof under a foreign key; every release path must revert.
- **Evidence:** `protocols/deep_screened.jsonl#hidden-hand|PROOF-VERIFICATION-BYPASSED`, `protocols/onchain_probes.json#hidden-hand`
- **Disclosure:** https://hiddenhand.finance · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.redacted.finance/products/hidden-hand/audits

### 17. Vest Markets  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 17
- **Protocol:** Vest Markets (`vest-markets`) · Derivatives · Ethereum, Arbitrum, Base, Binance, Polygon, Optimism …
- **DefiLlama:** https://defillama.com/protocol/vest-markets
- **PRIORITY 47.37**  =  LIKELIHOOD 47.37 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 15.47/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $221,342 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#vest-markets|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#vest-markets`
- **Disclosure:** https://alpha.vestmarkets.com · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.vestmarkets.com/audits

### 18. Octus Bridge  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 18
- **Protocol:** Octus Bridge (`octus-bridge`) · Bridge · Avalanche, Binance, Ethereum, Polygon, Everscale, Fantom
- **DefiLlama:** https://defillama.com/protocol/octus-bridge
- **PRIORITY 47.08**  =  LIKELIHOOD 47.08 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 15.18/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $396,274 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#octus-bridge|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#octus-bridge`
- **Disclosure:** https://octusbridge.io/bridge · no audit link listed

### 19. Level  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 19
- **Protocol:** Level (`level`) · CDP · Ethereum
- **DefiLlama:** https://defillama.com/protocol/level
- **PRIORITY 47.02**  =  LIKELIHOOD 47.02 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 15.12/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $460,166 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#level|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#level`
- **Disclosure:** https://www.level.money · no audit link listed

### 20. ZKcandy Bridge  —  `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 20
- **Protocol:** ZKcandy Bridge (`zkcandy-bridge`) · Canonical Bridge · Ethereum
- **DefiLlama:** https://defillama.com/protocol/zkcandy-bridge
- **PRIORITY 46.37**  =  LIKELIHOOD 46.37 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 9.47/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $683,034 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.
    - Deployed source (`L1NativeTokenVault` @ 0x2fc2a2db…(ethereum), `StakedZentry` @ 0xa694c051…(ethereum)): prerequisites matched: caller_named_asset_no_registry_check; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): value_fn_moves_caller_named_asset=yes
    - deployed source read for L1NativeTokenVault@0x2fc2a2db…(ethereum), StakedZentry@0xa694c051…(ethereum); indicators matched: caller_named_asset_no_registry_check, value_fn_moves_caller_named_asset
- **Preconditions PRESENT / UNKNOWN:** src::caller_named_asset_no_registry_check, live_value_present, deployment_reachable_on_chain / src::token_hook_credits_without_sender_check
- **Guards searched / found:** asset_registry_check_present / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Every identifier derived or verified against the factory/registry (kills the pair); Routing restricted to an immutable venue allowlist
- **Where to start:** On a fork, create a fake pool/mint and pass it to every identifier-accepting entrypoint; all must revert.
- **Evidence:** `protocols/deep_screened.jsonl#zkcandy-bridge|ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`, `protocols/onchain_probes.json#zkcandy-bridge`
- **Disclosure:** https://zkcandy.io/ · no audit link listed

### 21. TYMIO  —  `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 21
- **Protocol:** TYMIO (`tymio`) · Options · Arbitrum, Ethereum
- **DefiLlama:** https://defillama.com/protocol/tymio
- **PRIORITY 46.28**  =  LIKELIHOOD 46.28 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 9.38/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $278,738 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.
    - Deployed source (`PayerV3` @ 0xB67D637B…(ethereum)): prerequisites matched: caller_named_asset_no_registry_check; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): value_fn_moves_caller_named_asset=yes
    - deployed source read for PayerV3@0xB67D637B…(ethereum); indicators matched: caller_named_asset_no_registry_check, value_fn_moves_caller_named_asset
- **Preconditions PRESENT / UNKNOWN:** src::caller_named_asset_no_registry_check, live_value_present, deployment_reachable_on_chain / src::token_hook_credits_without_sender_check
- **Guards searched / found:** asset_registry_check_present / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Every identifier derived or verified against the factory/registry (kills the pair); Routing restricted to an immutable venue allowlist
- **Where to start:** On a fork, create a fake pool/mint and pass it to every identifier-accepting entrypoint; all must revert.
- **Evidence:** `protocols/deep_screened.jsonl#tymio|ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`, `protocols/onchain_probes.json#tymio`
- **Disclosure:** https://tymio.com/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/pessimistic-io/audits/blob/f2c817cecb35ecd831f5cc73aa99c58b484c0d13/TYMIO%20Security%20Analysis%20by%20Pessimistic.pdf

### 22. Flexa  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 22
- **Protocol:** Flexa (`flexa`) · Payments · Ethereum
- **DefiLlama:** https://defillama.com/protocol/flexa
- **PRIORITY 45.5**  =  LIKELIHOOD 45.5 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 13.6/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $702,640 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
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
- **Evidence:** `protocols/deep_screened.jsonl#flexa|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#flexa`
- **Disclosure:** https://amp.xyz/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://consensys.net/diligence/audits/2020/06/amp, https://github.com/trailofbits/publications/blob/master/reviews/amp.pdf

### 23. Felix USDhl  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 23
- **Protocol:** Felix USDhl (`felix-usdhl`) · Yield · Hyperliquid L1, Ethereum
- **DefiLlama:** https://defillama.com/protocol/felix-usdhl
- **PRIORITY 44.93**  =  LIKELIHOOD 44.93 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 13.03/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $449,345 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#felix-usdhl|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#felix-usdhl`
- **Disclosure:** https://www.usefelix.xyz?ref=4BF702FF · no audit link listed

### 24. Nocturne  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 24
- **Protocol:** Nocturne (`nocturne`) · Privacy · Ethereum
- **DefiLlama:** https://defillama.com/protocol/nocturne
- **PRIORITY 44.88**  =  LIKELIHOOD 44.88 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 7.98/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $78,408 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`ChiToken` @ 0x00000000…(ethereum), `zCurve` @ 0x00000000…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for ChiToken@0x00000000…(ethereum), zCurve@0x00000000…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#nocturne|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#nocturne`
- **Disclosure:** https://nocturne.xyz/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://nocturne-xyz.gitbook.io/nocturne/developers/security

### 25. Demeter  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 25
- **Protocol:** Demeter (`demeter`) · Lending · Binance, Heco
- **DefiLlama:** https://defillama.com/protocol/demeter
- **PRIORITY 44.85**  =  LIKELIHOOD 44.85 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 12.95/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $284,331 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `owner_is_eoa` — raises likelihood, measured lift ×1.729 (weight +0.55)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`StakingPool` @ 0x004c0908…(bsc), `StakingPool` @ 0x04493F71…(bsc)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for StakingPool@0x004c0908…(bsc), StakingPool@0x04493F71…(bsc); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `EOA_SINGLE_KEY`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#demeter|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#demeter`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/peckshield/publications/blob/master/audit_reports/PeckShield-Audit-Report-Demeter-v1.0.pdf

### 26. The Tokenized Bitcoin  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 26
- **Protocol:** The Tokenized Bitcoin (`the-tokenized-bitcoin`) · Bridge · Bitcoin, Ethereum
- **DefiLlama:** https://defillama.com/protocol/the-tokenized-bitcoin
- **PRIORITY 44.75**  =  LIKELIHOOD 52.65 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 20.75/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,744,996 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#the-tokenized-bitcoin|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#the-tokenized-bitcoin`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://cure53.de/pentest-report_imtoken.pdf

### 27. GMD Protocol  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 27
- **Protocol:** GMD Protocol (`gmd-protocol`) · Yield Aggregator · Arbitrum, Avalanche
- **DefiLlama:** https://defillama.com/protocol/gmd-protocol
- **PRIORITY 44.72**  =  LIKELIHOOD 44.72 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 12.82/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $971,646 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`GMDstaking` @ 0x48c81451…(arbitrum), `GMD` @ 0x4945970E…(arbitrum)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for GMDstaking@0x48c81451…(arbitrum), GMD@0x4945970E…(arbitrum); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `EOA_SINGLE_KEY`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#gmd-protocol|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#gmd-protocol`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://solidity.finance/audits/GMDAOVault

### 28. Synthetix V4  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 28
- **Protocol:** Synthetix V4 (`synthetix-v4`) · Derivatives · Ethereum
- **DefiLlama:** https://defillama.com/protocol/synthetix-v4
- **PRIORITY 44.5**  =  LIKELIHOOD 44.5 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 12.6/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $938,544 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#synthetix-v4|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#synthetix-v4`
- **Disclosure:** https://synthetix.io · no audit link listed

### 29. Lynx  —  `PROOF-VERIFICATION-BYPASSED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 29
- **Protocol:** Lynx (`lynx`) · Derivatives · Sonic, Boba, Goat, Arbitrum, Base, Ethereum …
- **DefiLlama:** https://defillama.com/protocol/lynx
- **PRIORITY 44.35**  =  LIKELIHOOD 44.35 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 12.45/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $192,608 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
- **Broken invariant tested:** A withdrawal or mint gated by a proof must verify that proof against the correct verifying key, over all the public inputs that bind the action, and must reject when any component is absent.
    - Deployed source (`OFTChipAdapter` @ 0x094DE4d3…(arbitrum)): prerequisites matched: proof_result_unchecked; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): verifier_address_mutable=no
    - deployed source read for OFTChipAdapter@0x094DE4d3…(arbitrum); indicators matched: proof_result_unchecked
- **Preconditions PRESENT / UNKNOWN:** src::proof_result_unchecked, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Verifying key immutable and attested (kills the misconfiguration shape); No alternative release path exists (enumerate selectors)
- **Where to start:** On a fork, submit an empty proof, a proof for different public inputs, and a proof under a foreign key; every release path must revert.
- **Evidence:** `protocols/deep_screened.jsonl#lynx|PROOF-VERIFICATION-BYPASSED`, `protocols/onchain_probes.json#lynx`
- **Disclosure:** https://app.lynx.finance/ · no audit link listed

### 30. Injective Bridge  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 30
- **Protocol:** Injective Bridge (`injective-bridge`) · Bridge · Ethereum
- **DefiLlama:** https://defillama.com/protocol/injective-bridge
- **PRIORITY 44.27**  =  LIKELIHOOD 52.08 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 20.18/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $5,431,209 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#injective-bridge|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#injective-bridge`
- **Disclosure:** https://injective.com · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://www.certik.org/projects/injectiveprotocol

### 31. Bunicorn  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 31
- **Protocol:** Bunicorn (`bunicorn`) · Dexs · Binance
- **DefiLlama:** https://defillama.com/protocol/bunicorn
- **PRIORITY 44.25**  =  LIKELIHOOD 44.25 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 12.35/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $128,459 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `owner_is_eoa` — raises likelihood, measured lift ×1.729 (weight +0.55)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`BuniToken` @ 0x0e7beec3…(bsc), `BFactory` @ 0x48ab3121…(bsc)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for BuniToken@0x0e7beec3…(bsc), BFactory@0x48ab3121…(bsc); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `EOA_SINGLE_KEY`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#bunicorn|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#bunicorn`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://hacken.io/wp-content/uploads/2021/05/Bunicorndefi_03052021_SC_Audit_2Report.pdf, https://hacken.io/wp-content/uploads/2021/06/Bunicorndefi_11062021SC_Audit_Report_2.pdf

### 32. Etherfuse  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 32
- **Protocol:** Etherfuse (`etherfuse`) · RWA · Solana, Polygon, Base, Monad, Stellar
- **DefiLlama:** https://defillama.com/protocol/etherfuse
- **PRIORITY 44.1**  =  LIKELIHOOD 44.1 × ACTIONABILITY 100.0%
    - likelihood = family evidence 30.0/50 (MATCH 60 × evidence weight 1.0) + learned attack surface 14.1/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $977,586 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 60 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `unverified_implementation` — raises likelihood, measured lift ×2.007 (weight +0.70)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`TESOURO_OFT` @ 0x7108b2f7…(base)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for TESOURO_OFT@0x7108b2f7…(base); indicators matched: hook_zero_amount_unguarded
    - 1 implementation(s) behind a proxy are NOT verified on the explorer: implementation identity unresolved, score capped at 60
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#etherfuse|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#etherfuse`
- **Disclosure:** https://www.etherfuse.com/ · no audit link listed

### 33. Dango Bridge  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 33
- **Protocol:** Dango Bridge (`dango-bridge`) · Bridge · Ethereum
- **DefiLlama:** https://defillama.com/protocol/dango-bridge
- **PRIORITY 44.08**  =  LIKELIHOOD 44.08 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 12.18/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $121,764 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#dango-bridge|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#dango-bridge`
- **Disclosure:** https://dango.exchange/ · no audit link listed

### 34. Pepu Bridge  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 34
- **Protocol:** Pepu Bridge (`pepu-bridge`) · Bridge · Ethereum
- **DefiLlama:** https://defillama.com/protocol/pepu-bridge
- **PRIORITY 44.08**  =  LIKELIHOOD 44.08 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 12.18/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $313,690 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
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
- **Evidence:** `protocols/deep_screened.jsonl#pepu-bridge|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#pepu-bridge`
- **Disclosure:** https://pepubridge.com/ · no audit link listed

### 35. Hats.V2  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 35
- **Protocol:** Hats.V2 (`hats.v2`) · Bug Bounty · Arbitrum, Ethereum, Optimism, Polygon, Binance
- **DefiLlama:** https://defillama.com/protocol/hats.v2
- **PRIORITY 44.05**  =  LIKELIHOOD 44.05 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 12.15/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $161,281 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`HATVaultsRegistry` @ 0xa80d0a37…(arbitrum), `HATHackersNFT` @ 0xc570c434…(arbitrum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for HATVaultsRegistry@0xa80d0a37…(arbitrum), HATHackersNFT@0xc570c434…(arbitrum); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#hats.v2|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#hats.v2`
- **Disclosure:** https://hats.finance · no audit link listed

### 36. Xave Finance  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 36
- **Protocol:** Xave Finance (`xave-finance`) · Dexs · Polygon, Avalanche, Ethereum
- **DefiLlama:** https://defillama.com/protocol/xave-finance
- **PRIORITY 43.82**  =  LIKELIHOOD 43.82 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 11.92/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $149,205 · **Band:** `IN_BAND`
- **Previously hacked:** 2022-10-09 for $0 [Malicious Proposal]
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`Curve` @ 0x20E1d8Da…(ethereum), `FXPoolFactory` @ 0x81fE9e5B…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for Curve@0x20E1d8Da…(ethereum), FXPoolFactory@0x81fE9e5B…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `KNOWN_ISSUE_DEPLOYMENT_STATUS_UNKNOWN` — DefiLlama's hacks dataset records 1 prior on-chain incident(s) on this protocol, most recently 2022-10-09 for $0 [Malicious Proposal]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#xave-finance|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#xave-finance`
- **Disclosure:** https://xave.co · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.xave.co/contract-audits/fxpool-final-audit

### 37. Alchemist  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 37
- **Protocol:** Alchemist (`alchemist`) · Yield · Ethereum
- **DefiLlama:** https://defillama.com/protocol/alchemist
- **PRIORITY 43.75**  =  LIKELIHOOD 43.75 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 11.85/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $271,800 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`Alchemist` @ 0x88acdd2a…(ethereum), `RewardPoolFactory` @ 0xF016fa84…(ethereum)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for Alchemist@0x88acdd2a…(ethereum), RewardPoolFactory@0xF016fa84…(ethereum); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#alchemist|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#alchemist`
- **Disclosure:** https://www.alchemist.wtf · no audit link listed

### 38. RollX  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 38
- **Protocol:** RollX (`rollx`) · Derivatives · Base, Bitlayer
- **DefiLlama:** https://defillama.com/protocol/rollx
- **PRIORITY 43.7**  =  LIKELIHOOD 43.7 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 11.8/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $444,294 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `owner_is_eoa` — raises likelihood, measured lift ×1.729 (weight +0.55)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`Bfbtc` @ 0x128eb2ba…(base), `RollDex` @ 0x823e0F1E…(base)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for Bfbtc@0x128eb2ba…(base), RollDex@0x823e0F1E…(base); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `EOA_SINGLE_KEY`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#rollx|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#rollx`
- **Disclosure:** https://rollx.trade/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://skynet.certik.com/zh-CN/projects/rolldex

### 39. Aarna Protocol  —  `CALLBACK-UNAUTHENTICATED-CALLER-USES-APPROVALS`

- **Rank (Ranking A — priority (likelihood × actionability)):** 39
- **Protocol:** Aarna Protocol (`aarna-protocol`) · Yield · Ethereum, Sonic, Arbitrum, Base
- **DefiLlama:** https://defillama.com/protocol/aarna-protocol
- **PRIORITY 43.67**  =  LIKELIHOOD 43.67 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 11.77/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $392,025 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** When a contract pulls funds during a callback, the payer must be proven to be the initiator of the current flow, and the callback's caller must be proven to be the expected counterparty contract. Neither may be taken from caller-supplied payload.
    - Deployed source (`CErc20` @ 0x39aa39c0…(ethereum), `AtvBase` @ 0x60697825…(ethereum)): prerequisites matched: callback_without_caller_check, transferFrom_param_payer; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): callback_without_caller_check=yes (DEMOTED: fires on 46% of the 900 contracts swept, so it describes a common architecture rather than a distinguishing prerequisite)
    - deployed source read for CErc20@0x39aa39c0…(ethereum), AtvBase@0x60697825…(ethereum); indicators matched: callback_without_caller_check, transferFrom_param_payer
- **Preconditions PRESENT / UNKNOWN:** src::transferFrom_param_payer, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Callback asserts both caller identity and payer == initiator (kills the pair); Contract never holds third-party approvals; Payment always uses msg.sender as source
- **Where to start:** On a fork, with a victim approval live, attempt to initiate the lock/callback path nominating the victim as payer; it must revert.
- **Evidence:** `protocols/deep_screened.jsonl#aarna-protocol|CALLBACK-UNAUTHENTICATED-CALLER-USES-APPROVALS`, `protocols/onchain_probes.json#aarna-protocol`
- **Disclosure:** https://www.aarna.ai · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://skynet.certik.com/projects/aarna-protocol

### 40. Hyperdrive  —  `ACC-DUPLICATE-ID-ACCUMULATION`

- **Rank (Ranking A — priority (likelihood × actionability)):** 40
- **Protocol:** Hyperdrive (`hyperdrive`) · Yield · Ethereum, Linea, xDai, Base
- **DefiLlama:** https://defillama.com/protocol/hyperdrive
- **PRIORITY 43.67**  =  LIKELIHOOD 43.67 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 11.77/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $71,676 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** An entitlement attached to an identifier may be counted at most once per period. A caller-supplied ID list must be deduplicated, or each ID's claim state consumed before the next read.
    - Deployed source (`HyperdriveRegistry` @ 0xbe082293…(ethereum)): prerequisites matched: id_array_loop_without_dedup; no guard found
    - deployed source read for HyperdriveRegistry@0xbe082293…(ethereum); indicators matched: id_array_loop_without_dedup
- **Preconditions PRESENT / UNKNOWN:** src::id_array_loop_without_dedup, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Consumed marker written inside the loop (kills the pair); IDs required strictly increasing
- **Where to start:** On a fork, call the batch function with one ID repeated k times; payout must equal the single-ID payout.
- **Evidence:** `protocols/deep_screened.jsonl#hyperdrive|ACC-DUPLICATE-ID-ACCUMULATION`, `protocols/onchain_probes.json#hyperdrive`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/delvtech/hyperdrive/tree/main/audits

### 41. ShardingDAO  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 41
- **Protocol:** ShardingDAO (`shardingdao`) · Staking Pool · Ethereum
- **DefiLlama:** https://defillama.com/protocol/shardingdao
- **PRIORITY 43.55**  =  LIKELIHOOD 43.55 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 11.65/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $56,662 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#shardingdao|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#shardingdao`
- **Disclosure:** https://shardingdao.com/ · no audit link listed

### 42. ApeSwap Lending  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 42
- **Protocol:** ApeSwap Lending (`apeswap-lending`) · Lending · Binance
- **DefiLlama:** https://defillama.com/protocol/apeswap-lending
- **PRIORITY 43.45**  =  LIKELIHOOD 43.45 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 11.55/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $219,009 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `owner_is_eoa` — raises likelihood, measured lift ×1.729 (weight +0.55)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`StakingPool` @ 0x004c0908…(bsc), `StakingPool` @ 0x04493F71…(bsc)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for StakingPool@0x004c0908…(bsc), StakingPool@0x04493F71…(bsc); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `EOA_SINGLE_KEY`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#apeswap-lending|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#apeswap-lending`
- **Disclosure:** https://ape.bond/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://apeswap.gitbook.io/apeswap-finance/security/audits

### 43. Rosen Bridge  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 43
- **Protocol:** Rosen Bridge (`rosen-bridge`) · Bridge · Ergo, Cardano, Bitcoin, Ethereum, Binance, Doge
- **DefiLlama:** https://defillama.com/protocol/rosen-bridge
- **PRIORITY 43.32**  =  LIKELIHOOD 50.97 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 19.07/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,401,432 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#rosen-bridge|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#rosen-bridge`
- **Disclosure:** https://rosen.tech · no audit link listed

### 44. Almanak  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 44
- **Protocol:** Almanak (`almanak`) · Onchain Capital Allocator · Ethereum, Base
- **DefiLlama:** https://defillama.com/protocol/almanak
- **PRIORITY 43.05**  =  LIKELIHOOD 43.05 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 11.15/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $460,254 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`OptinProxy` @ 0xb523EeE5…(base), `AlmanakTokenL2` @ 0xdefa1d21…(base)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for OptinProxy@0xb523EeE5…(base), AlmanakTokenL2@0xdefa1d21…(base); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#almanak|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#almanak`
- **Disclosure:** https://almanak.co · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://zokyo.io/reports/almanak

### 45. maxAPY  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 45
- **Protocol:** maxAPY (`maxapy`) · Yield Aggregator · Base, Ethereum, Polygon
- **DefiLlama:** https://defillama.com/protocol/maxapy
- **PRIORITY 42.98**  =  LIKELIHOOD 42.98 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 11.08/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $61,721 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`VaultV2` @ 0x0463A5e9…(base)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for VaultV2@0x0463A5e9…(base); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#maxapy|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#maxapy`
- **Disclosure:** https://app.maxapy.io · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/UnlockdFinance/maxapy/tree/development/audits

### 46. Gudchain  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 46
- **Protocol:** Gudchain (`gudchain`) · Farm · Ethereum
- **DefiLlama:** https://defillama.com/protocol/gudchain
- **PRIORITY 42.92**  =  LIKELIHOOD 42.92 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 11.02/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $85,541 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ChiToken` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ChiToken@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#gudchain|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#gudchain`
- **Disclosure:** https://gudchain.com/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://cdn.gudchain.com/documents/Gudchain%20-%20Smart%20Contract%20Audit%20Report.pdf

### 47. ApeX Pro  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 47
- **Protocol:** ApeX Pro (`apex-pro`) · Derivatives · Ethereum, Polygon, Arbitrum, Binance, Mantle, Avalanche …
- **DefiLlama:** https://defillama.com/protocol/apex-pro
- **PRIORITY 42.81**  =  LIKELIHOOD 50.37 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 18.47/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,430,085 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#apex-pro|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#apex-pro`
- **Disclosure:** https://www.apex.exchange/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/ApeX-Protocol/core/blob/master/docs/audit_report.pdf

### 48. Bundles  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 48
- **Protocol:** Bundles (`bundles`) · Indexes · Ethereum
- **DefiLlama:** https://defillama.com/protocol/bundles
- **PRIORITY 42.77**  =  LIKELIHOOD 42.77 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 10.87/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $535,560 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`Factory` @ 0x661F8b1E…(ethereum), `BundlesToken` @ 0x695f7755…(ethereum)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for Factory@0x661F8b1E…(ethereum), BundlesToken@0x695f7755…(ethereum); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#bundles|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#bundles`
- **Disclosure:** https://bundles.fi/ · no audit link listed

### 49. Opyn Convexity  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 49
- **Protocol:** Opyn Convexity (`opyn-convexity`) · Options · Ethereum
- **DefiLlama:** https://defillama.com/protocol/opyn-convexity
- **PRIORITY 42.73**  =  LIKELIHOOD 42.73 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 10.83/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $569,982 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`OptionsFactory` @ 0xb529964F…(ethereum), `OptionsFactory` @ 0xcC5d905b…(ethereum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for OptionsFactory@0xb529964F…(ethereum), OptionsFactory@0xcC5d905b…(ethereum); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#opyn-convexity|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#opyn-convexity`
- **Disclosure:** https://www.opyn.co · no audit link listed

### 50. SUBFROST  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 50
- **Protocol:** SUBFROST (`subfrost`) · Decentralized BTC · Bitcoin, Ethereum
- **DefiLlama:** https://defillama.com/protocol/subfrost
- **PRIORITY 42.4**  =  LIKELIHOOD 49.88 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 17.98/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $8,631,381 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#subfrost|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#subfrost`
- **Disclosure:** https://app.subfrost.io/ · no audit link listed

### 51. Swerve  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 51
- **Protocol:** Swerve (`swerve`) · Dexs · Ethereum
- **DefiLlama:** https://defillama.com/protocol/swerve
- **PRIORITY 42.12**  =  LIKELIHOOD 42.12 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 10.22/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $305,359 · **Band:** `IN_BAND`
- **Previously hacked:** 2023-03-25 for $1,300,000 [Malicious Proposal]
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `KNOWN_ISSUE_DEPLOYMENT_STATUS_UNKNOWN` — DefiLlama's hacks dataset records 1 prior on-chain incident(s) on this protocol, most recently 2023-03-25 for $1,300,000 [Malicious Proposal]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#swerve|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#swerve`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/crypticlabs/swerve-audit-report/blob/master/Swerve%20Finance%20Audit%20-%20by%20Cryptic%20Labs%20v3.pdf

### 52. CreamSwap  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 52
- **Protocol:** CreamSwap (`creamswap`) · Dexs · Ethereum
- **DefiLlama:** https://defillama.com/protocol/creamswap
- **PRIORITY 42.12**  =  LIKELIHOOD 42.12 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 10.22/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $75,107 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`BFactory` @ 0x0d3303Ff…(ethereum), `BFactory` @ 0x136d6F80…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for BFactory@0x0d3303Ff…(ethereum), BFactory@0x136d6F80…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#creamswap|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#creamswap`
- **Disclosure:** https://app.cream.finance/swap · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/CreamFi/compound-protocol/blob/master/audits/trailofbits-CREAMSummary.pdf

### 53. TanX.fi  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 53
- **Protocol:** TanX.fi (`tanx.fi`) · Dexs · Ethereum, Arbitrum, Linea, Mode, Polygon, Scroll …
- **DefiLlama:** https://defillama.com/protocol/tanx.fi
- **PRIORITY 42.12**  =  LIKELIHOOD 42.12 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 10.22/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $284,190 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ChiToken` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ChiToken@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#tanx.fi|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#tanx.fi`
- **Disclosure:** https://www.tanx.fi · no audit link listed

### 54. cVault Finance  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 54
- **Protocol:** cVault Finance (`cvault-finance`) · Yield · Ethereum
- **DefiLlama:** https://defillama.com/protocol/cvault-finance
- **PRIORITY 42.12**  =  LIKELIHOOD 49.55 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 17.65/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $6,015,301 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#cvault-finance|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#cvault-finance`
- **Disclosure:** https://cvault.finance/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://arcadiamgroup.com/audits/CoreFinal.pdf

### 55. Cyclone  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 55
- **Protocol:** Cyclone (`cyclone`) · Yield · Ethereum, Binance, IoTeX, Polygon
- **DefiLlama:** https://defillama.com/protocol/cyclone
- **PRIORITY 42.12**  =  LIKELIHOOD 49.55 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 17.65/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,381,617 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
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
- **Evidence:** `protocols/deep_screened.jsonl#cyclone|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#cyclone`
- **Disclosure:** https://cyclone.xyz · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.cyclone.xyz/audit

### 56. Basis Cash  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 56
- **Protocol:** Basis Cash (`basis-cash`) · Algo-Stables · Ethereum
- **DefiLlama:** https://defillama.com/protocol/basis-cash
- **PRIORITY 42.12**  =  LIKELIHOOD 42.12 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 10.22/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $205,731 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#basis-cash|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#basis-cash`
- **Disclosure:** https://basis.cash/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/basisdollar/basisdollar-protocol#audit

### 57. YFII  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 57
- **Protocol:** YFII (`yfii`) · Yield Aggregator · Ethereum
- **DefiLlama:** https://defillama.com/protocol/yfii
- **PRIORITY 42.12**  =  LIKELIHOOD 42.12 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 10.22/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $442,371 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`iVault` @ 0x1e0DC67a…(ethereum), `iVault` @ 0x23B4dB3a…(ethereum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for iVault@0x1e0DC67a…(ethereum), iVault@0x23B4dB3a…(ethereum); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#yfii|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#yfii`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/yfii/audit

### 58. Impermax V3  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 58
- **Protocol:** Impermax V3 (`impermax-v3`) · Lending · Base, Unichain, Hyperliquid L1, Arbitrum
- **DefiLlama:** https://defillama.com/protocol/impermax-v3
- **PRIORITY 42.08**  =  LIKELIHOOD 42.08 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 10.18/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $98,183 · **Band:** `IN_BAND`
- **REPEAT VICTIM — 2 recorded hacks.** 2025-11-11 $380,000 [Liquidation Logic Flaw]; 2025-04-26 $300,000 [Incorrect Fee Accounting]
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`ImpermaxV3Factory` @ 0x175712cD…(base), `ImpermaxV3Factory` @ 0x870fd2c2…(base)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for ImpermaxV3Factory@0x175712cD…(base), ImpermaxV3Factory@0x870fd2c2…(base); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `UNREMEDIATED_KNOWN_ISSUE` — DefiLlama's hacks dataset records 2 prior on-chain incident(s) on this protocol, most recently 2025-11-11 for $380,000 [Liquidation Logic Flaw]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#impermax-v3|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#impermax-v3`
- **Disclosure:** https://impermax.finance · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/GuardianAudits/Audits/blob/main/Impermax/2025-02-08_Impermax.pdf, https://github.com/bailsec/BailSec/blob/main/Bailsec%20-%20Impermax%20-%20V3%20Core%20-%20Final%20Report.pdf

### 59. Fyde Protocol  —  `BRIDGE-MESSAGE-NOT-BOUND-TO-SOURCE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 59
- **Protocol:** Fyde Protocol (`fyde-protocol`) · Yield Aggregator · Ethereum
- **DefiLlama:** https://defillama.com/protocol/fyde-protocol
- **PRIORITY 42.03**  =  LIKELIHOOD 42.03 × ACTIONABILITY 100.0%
    - likelihood = family evidence 26.25/50 (MATCH 52.5 × evidence weight 1.0) + learned attack surface 15.78/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $376,264 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 52.5 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A release, mint or payout on the destination domain must be authorised only by a proof that binds, simultaneously: the source chain identity, the source channel/route, the exact asset, the exact amount, the recipient, and a nonce that is consumed exactly once. Verifying that a message is well-formed or correctly signed is not the same as verifying that it corresponds to a real deposit of equal value.
    - Deployed source (`OracleModule` @ 0x05198327…(ethereum), `PendlePrincipalToken` @ 0x1c085195…(ethereum)): prerequisites matched: xdomain_source_not_bound; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): xdomain_nonce_not_consumed=no
    - deployed source read for OracleModule@0x05198327…(ethereum), PendlePrincipalToken@0x1c085195…(ethereum); indicators matched: xdomain_source_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::xdomain_source_not_bound, live_value_present, deployment_reachable_on_chain / src::xdomain_entrypoint_present, src::xdomain_no_endpoint_check, src::token_hook_credits_without_sender_check
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_1_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Destination mint requires a Merkle/zk proof against a source state root that itself commits to the amount; Reserve reconciliation is enforced on-chain (mint reverts if supply would exceed escrow); Bridge is one-way with no destination-side release
- **Where to start:** On a pinned fork of the destination chain, no sequence of destination-side calls may increase redeemable value without a matching, previously unconsumed source commitment of equal value.
- **Evidence:** `protocols/deep_screened.jsonl#fyde-protocol|BRIDGE-MESSAGE-NOT-BOUND-TO-SOURCE`, `protocols/onchain_probes.json#fyde-protocol`
- **Disclosure:** http://www.fyde.fi · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://2610459056-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FbQllaeunfO4BPaZU1ABc%2Fuploads%2FDrOUIAG2nAdc0Lf0RxD8%2FFyde_Core_Smart_Contract_Security_Assessment_Report_Halborn_Final.pdf?alt=media&token=2c53c4fb-f125-4a91-abce-9c0dd3314c97, https://2610459056-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FbQllaeunfO4BPaZU1ABc%2Fuploads%2FKXNIVvRuIB6ImuEIo7dt%2FFyde-security-review.pdf?alt=media&token=830f255a-d7f2-442c-a23e-2d5aed9c2b33

### 60. Raindex  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 60
- **Protocol:** Raindex (`raindex`) · Dexs · Base, Flare, Binance, Polygon, Ethereum, Arbitrum …
- **DefiLlama:** https://defillama.com/protocol/raindex
- **PRIORITY 41.83**  =  LIKELIHOOD 41.83 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 9.93/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $122,285 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#raindex|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#raindex`
- **Disclosure:** https://rainlang.xyz/ · no audit link listed

### 61. Rysk V1  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking A — priority (likelihood × actionability)):** 61
- **Protocol:** Rysk V1 (`rysk-v1`) · Options · Arbitrum
- **DefiLlama:** https://defillama.com/protocol/rysk-v1
- **PRIORITY 41.65**  =  LIKELIHOOD 41.65 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 4.75/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $193,788 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source (`UniswapV3HedgingReactor` @ 0x00538491…(arbitrum), `LiquidityPool` @ 0x217749d9…(arbitrum)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for UniswapV3HedgingReactor@0x00538491…(arbitrum), LiquidityPool@0x217749d9…(arbitrum); indicators matched: unsafe_cross_sign_cast
- **Preconditions PRESENT / UNKNOWN:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** safecast_used / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#rysk-v1|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#rysk-v1`
- **Disclosure:** https://app.rysk.finance · no audit link listed

### 62. Charm Finance V2  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking A — priority (likelihood × actionability)):** 62
- **Protocol:** Charm Finance V2 (`charm-finance-v2`) · Liquidity Manager · Berachain, Ethereum, Katana, Arbitrum, Base, Polygon …
- **DefiLlama:** https://defillama.com/protocol/charm-finance-v2
- **PRIORITY 41.37**  =  LIKELIHOOD 48.67 × ACTIONABILITY 85.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 11.77/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,937,508 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source (`AlphaProVaultFactory` @ 0x5B7B8b48…(base), `AlphaProVaultFactory` @ 0x8C554F20…(base)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for AlphaProVaultFactory@0x5B7B8b48…(base), AlphaProVaultFactory@0x8C554F20…(base); indicators matched: unsafe_cross_sign_cast
- **Preconditions PRESENT / UNKNOWN:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** safecast_used / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#charm-finance-v2|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#charm-finance-v2`
- **Disclosure:** https://alpha.charm.fi/vaults · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://learn.charm.fi/charm/appendix/audit-reports

### 63. Factor Leverage Vault  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 63
- **Protocol:** Factor Leverage Vault (`factor-leverage-vault`) · Leveraged Farming · Arbitrum
- **DefiLlama:** https://defillama.com/protocol/factor-leverage-vault
- **PRIORITY 41.1**  =  LIKELIHOOD 41.1 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 9.2/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $70,198 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`FactorLeverageVault` @ 0xfcc82362…(arbitrum), `FactorTransparentUpgradeableProxy` @ 0x0ACFF63d…(arbitrum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for FactorLeverageVault@0xfcc82362…(arbitrum), FactorTransparentUpgradeableProxy@0x0ACFF63d…(arbitrum); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#factor-leverage-vault|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#factor-leverage-vault`
- **Disclosure:** https://app.factor.fi/studio · no audit link listed

### 64. SwingHook  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 64
- **Protocol:** SwingHook (`swinghook`) · Dexs · Ethereum
- **DefiLlama:** https://defillama.com/protocol/swinghook
- **PRIORITY 41.05**  =  LIKELIHOOD 41.05 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 9.15/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $104,136 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
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
- **Evidence:** `protocols/deep_screened.jsonl#swinghook|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#swinghook`
- **Disclosure:** https://swinghook.eth.limo · no audit link listed

### 65. RISE Bridge  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 65
- **Protocol:** RISE Bridge (`rise-bridge`) · Bridge · Ethereum
- **DefiLlama:** https://defillama.com/protocol/rise-bridge
- **PRIORITY 41.05**  =  LIKELIHOOD 41.05 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 9.15/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $179,612 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
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
- **Evidence:** `protocols/deep_screened.jsonl#rise-bridge|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#rise-bridge`
- **Disclosure:** https://risechain.com/ · no audit link listed

### 66. ZebraDAO  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking A — priority (likelihood × actionability)):** 66
- **Protocol:** ZebraDAO (`zebradao`) · Lending · Base
- **DefiLlama:** https://defillama.com/protocol/zebradao
- **PRIORITY 40.92**  =  LIKELIHOOD 40.92 × ACTIONABILITY 100.0%
    - likelihood = family evidence 30.0/50 (MATCH 60 × evidence weight 1.0) + learned attack surface 10.92/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $124,184 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 60 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `unverified_implementation` — raises likelihood, measured lift ×2.007 (weight +0.70)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source (`StakedDistributor` @ 0x5e615b52…(base)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for StakedDistributor@0x5e615b52…(base); indicators matched: unsafe_cross_sign_cast
    - 1 implementation(s) behind a proxy are NOT verified on the explorer: implementation identity unresolved, score capped at 60
- **Preconditions PRESENT / UNKNOWN:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** safecast_used / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#zebradao|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#zebradao`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/ZebraDAOFinance/AuditReport/blob/main/ZebraDao.pdf

### 67. EA Finance  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 67
- **Protocol:** EA Finance (`ea-finance`) · Liquid Restaking · Binance
- **DefiLlama:** https://defillama.com/protocol/ea-finance
- **PRIORITY 40.63**  =  LIKELIHOOD 40.63 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 8.73/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $310,606 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `owner_is_eoa` — raises likelihood, measured lift ×1.729 (weight +0.55)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`StakingRewardsWCC` @ 0x23EbC377…(bsc), `wCC` @ 0x6050D829…(bsc)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for StakingRewardsWCC@0x23EbC377…(bsc), wCC@0x6050D829…(bsc); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `EOA_SINGLE_KEY`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#ea-finance|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#ea-finance`
- **Disclosure:** https://app.ea.finance/vaults · no audit link listed

### 68. Yamato Protocol  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 68
- **Protocol:** Yamato Protocol (`yamato-protocol`) · CDP · Ethereum
- **DefiLlama:** https://defillama.com/protocol/yamato-protocol
- **PRIORITY 40.53**  =  LIKELIHOOD 47.68 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 15.78/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,639,592 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#yamato-protocol|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#yamato-protocol`
- **Disclosure:** https://app.yamato.fi/#/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://blockapex.io/yamato-protocol-audit-report/

### 69. BOB Fusion  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 69
- **Protocol:** BOB Fusion (`bob-fusion`) · Farm · Ethereum
- **DefiLlama:** https://defillama.com/protocol/bob-fusion
- **PRIORITY 40.52**  =  LIKELIHOOD 40.52 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 8.62/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $396,252 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#bob-fusion|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#bob-fusion`
- **Disclosure:** https://gobob.xyz · no audit link listed

### 70. 9inch V2  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 70
- **Protocol:** 9inch V2 (`9inch-v2`) · Dexs · Pulse, Ethereum
- **DefiLlama:** https://defillama.com/protocol/9inch-v2
- **PRIORITY 40.14**  =  LIKELIHOOD 47.22 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 15.32/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,049,596 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `owner_is_eoa` — raises likelihood, measured lift ×1.729 (weight +0.55)
    - `version_sibling_legacy` — raises likelihood, measured lift ×1.699 (weight +0.53)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`TokenFlexiblePool` @ 0x0022E0C2…(ethereum), `BBC` @ 0x015628ce…(ethereum)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for TokenFlexiblePool@0x0022E0C2…(ethereum), BBC@0x015628ce…(ethereum); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `EOA_SINGLE_KEY`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#9inch-v2|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#9inch-v2`
- **Disclosure:** https://app.9inch.io/?chain=pulsechain · no audit link listed

### 71. TProtocol V1  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 71
- **Protocol:** TProtocol V1 (`tprotocol-v1`) · RWA · Ethereum
- **DefiLlama:** https://defillama.com/protocol/tprotocol-v1
- **PRIORITY 40.1**  =  LIKELIHOOD 40.1 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 8.2/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $71,322 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `version_sibling_legacy` — raises likelihood, measured lift ×1.699 (weight +0.53)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#tprotocol-v1|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#tprotocol-v1`
- **Disclosure:** https://legacy.tprotocol.io/ · no audit link listed

### 72. Alphix  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 72
- **Protocol:** Alphix (`alphix`) · Dexs · Arbitrum, Base
- **DefiLlama:** https://defillama.com/protocol/alphix
- **PRIORITY 39.95**  =  LIKELIHOOD 39.95 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 8.05/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $225,700 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`Alphix` @ 0x5e645c3d…(arbitrum)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for Alphix@0x5e645c3d…(arbitrum); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#alphix|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#alphix`
- **Disclosure:** https://www.alphix.fi/swap · no audit link listed

### 73. Gremlix  —  `ACC-NAV-SHAREPRICE-MANIPULABLE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 73
- **Protocol:** Gremlix (`gremlix`) · Yield Aggregator · Arbitrum
- **DefiLlama:** https://defillama.com/protocol/gremlix
- **PRIORITY 39.88**  =  LIKELIHOOD 39.88 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 7.98/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $118,352 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** totalAssets() must equal value the vault could actually realise now. Any component valued at book, at a manipulable rate, or after economic impairment lets a redeemer convert other depositors' claims into their own.
    - Deployed source (`SafeUsdVault` @ 0x97cf7976…(arbitrum)): prerequisites matched: totalAssets_reads_balanceOf; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): totalAssets_defined=yes
    - deployed source read for SafeUsdVault@0x97cf7976…(arbitrum); indicators matched: totalAssets_reads_balanceOf, totalAssets_defined
    - 1 live contract(s) answer totalAssets()
- **Preconditions PRESENT / UNKNOWN:** src::totalAssets_reads_balanceOf, erc4626_style_totalAssets_live, live_pooled_depositor_value / multi_component_totalAssets
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Share price rate-limited per block (kills same-transaction extraction); Single-asset vault with no external valuation; Withdrawals queued with a delay and priced at settlement
- **Where to start:** On a fork, for each component, force its valuation to zero and to 10x; the vault's mint/redeem must revert or be bounded, never transfer more than the depositor's pro-rata realisable share.
- **Evidence:** `protocols/deep_screened.jsonl#gremlix|ACC-NAV-SHAREPRICE-MANIPULABLE`, `protocols/onchain_probes.json#gremlix`
- **Disclosure:**   · no audit link listed

### 74. Bondlink Finance  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 74
- **Protocol:** Bondlink Finance (`bondlink-finance`) · RWA · Ethereum
- **DefiLlama:** https://defillama.com/protocol/bondlink-finance
- **PRIORITY 39.88**  =  LIKELIHOOD 39.88 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 7.98/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $151,992 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`USDb` @ 0x1623A55e…(ethereum)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for USDb@0x1623A55e…(ethereum); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#bondlink-finance|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#bondlink-finance`
- **Disclosure:** https://www.bondlink.finance · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://beosin.com/audits/Bondlink_202412031841.pdf

### 75. Universe XYZ  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 75
- **Protocol:** Universe XYZ (`universe-xyz`) · Yield · Ethereum
- **DefiLlama:** https://defillama.com/protocol/universe-xyz
- **PRIORITY 39.82**  =  LIKELIHOOD 46.85 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 14.95/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $2,361,013 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#universe-xyz|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#universe-xyz`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/UniverseXYZ/xyzDAO-PM/tree/master/audits

### 76. UNCX Network V4  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 76
- **Protocol:** UNCX Network V4 (`uncx-network-v4`) · Token Locker · Ethereum, Base, Robinhood Chain, Unichain, Arbitrum, Binance …
- **DefiLlama:** https://defillama.com/protocol/uncx-network-v4
- **PRIORITY 39.76**  =  LIKELIHOOD 46.78 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 14.88/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $2,998,160 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`UniV4LiquidityLockerV3` @ 0x147aeca1…(ethereum), `UniV4LiquidityLockerV2` @ 0x30529ac6…(ethereum)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for UniV4LiquidityLockerV3@0x147aeca1…(ethereum), UniV4LiquidityLockerV2@0x30529ac6…(ethereum); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#uncx-network-v4|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#uncx-network-v4`
- **Disclosure:** https://uncx.network/ · no audit link listed

### 77. Maverick V2  —  `BRIDGE-MESSAGE-NOT-BOUND-TO-SOURCE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 77
- **Protocol:** Maverick V2 (`maverick-v2`) · Dexs · Ethereum, Base, Arbitrum, zkSync Era, Binance, Scroll
- **DefiLlama:** https://defillama.com/protocol/maverick-v2
- **PRIORITY 39.67**  =  LIKELIHOOD 46.67 × ACTIONABILITY 85.0%
    - likelihood = family evidence 30.0/50 (MATCH 60.0 × evidence weight 1.0) + learned attack surface 16.67/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,142,652 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 60.0 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `unverified_implementation` — raises likelihood, measured lift ×2.007 (weight +0.70)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
- **Broken invariant tested:** A release, mint or payout on the destination domain must be authorised only by a proof that binds, simultaneously: the source chain identity, the source channel/route, the exact asset, the exact amount, the recipient, and a nonce that is consumed exactly once. Verifying that a message is well-formed or correctly signed is not the same as verifying that it corresponds to a real deposit of equal value.
    - Conditions: `MULTICHAIN_VERSION_DRIFT`
    - Deployed source (`MaverickToken` @ 0x7448c745…(ethereum)): prerequisites matched: xdomain_entrypoint_present, xdomain_no_endpoint_check; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): xdomain_nonce_not_consumed=yes
    - deployed source read for MaverickToken@0x7448c745…(ethereum); indicators matched: xdomain_entrypoint_present, xdomain_no_endpoint_check, xdomain_nonce_not_consumed
    - 1 implementation(s) behind a proxy are NOT verified on the explorer: implementation identity unresolved, score capped at 60
- **Preconditions PRESENT / UNKNOWN:** src::xdomain_entrypoint_present, src::xdomain_no_endpoint_check, live_value_present, deployment_reachable_on_chain / src::xdomain_source_not_bound, src::token_hook_credits_without_sender_check
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Destination mint requires a Merkle/zk proof against a source state root that itself commits to the amount; Reserve reconciliation is enforced on-chain (mint reverts if supply would exceed escrow); Bridge is one-way with no destination-side release
- **Where to start:** On a pinned fork of the destination chain, no sequence of destination-side calls may increase redeemable value without a matching, previously unconsumed source commitment of equal value.
- **Evidence:** `protocols/deep_screened.jsonl#maverick-v2|BRIDGE-MESSAGE-NOT-BOUND-TO-SOURCE`, `protocols/onchain_probes.json#maverick-v2`
- **Disclosure:** https://www.mav.xyz · no audit link listed

### 78. Mycelium Perpetual Pools  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 78
- **Protocol:** Mycelium Perpetual Pools (`mycelium-perpetual-pools`) · Derivatives · Arbitrum
- **DefiLlama:** https://defillama.com/protocol/mycelium-perpetual-pools
- **PRIORITY 39.67**  =  LIKELIHOOD 39.67 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 7.77/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $179,980 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`PoolFactory` @ 0x3Feafee6…(arbitrum), `PoolFactory` @ 0x98C58c1c…(arbitrum)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for PoolFactory@0x3Feafee6…(arbitrum), PoolFactory@0x98C58c1c…(arbitrum); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#mycelium-perpetual-pools|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#mycelium-perpetual-pools`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://tracer.finance/radar/sigma-prime-audit-response

### 79. BTCD  —  `ACC-NAV-SHAREPRICE-MANIPULABLE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 79
- **Protocol:** BTCD (`btcd`) · Yield · Ethereum, Arbitrum
- **DefiLlama:** https://defillama.com/protocol/btcd
- **PRIORITY 39.3**  =  LIKELIHOOD 46.23 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 14.33/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,808,482 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** totalAssets() must equal value the vault could actually realise now. Any component valued at book, at a manipulable rate, or after economic impairment lets a redeemer convert other depositors' claims into their own.
    - Deployed source (`OFT` @ 0x06ea695B…(ethereum), `YieldBasisStrategy` @ 0x174A18b8…(ethereum)): prerequisites matched: totalAssets_reads_balanceOf; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): totalAssets_defined=yes
    - deployed source read for OFT@0x06ea695B…(ethereum), YieldBasisStrategy@0x174A18b8…(ethereum); indicators matched: totalAssets_reads_balanceOf, totalAssets_defined
    - 1 live contract(s) answer totalAssets()
- **Preconditions PRESENT / UNKNOWN:** src::totalAssets_reads_balanceOf, erc4626_style_totalAssets_live, live_pooled_depositor_value / multi_component_totalAssets
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Share price rate-limited per block (kills same-transaction extraction); Single-asset vault with no external valuation; Withdrawals queued with a delay and priced at settlement
- **Where to start:** On a fork, for each component, force its valuation to zero and to 10x; the vault's mint/redeem must revert or be bounded, never transfer more than the depositor's pro-rata realisable share.
- **Evidence:** `protocols/deep_screened.jsonl#btcd|ACC-NAV-SHAREPRICE-MANIPULABLE`, `protocols/onchain_probes.json#btcd`
- **Disclosure:**   · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.btcd.fi/security-and-audits

### 80. Zircuit Finance  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 80
- **Protocol:** Zircuit Finance (`zircuit-finance`) · Yield · Base, Ethereum
- **DefiLlama:** https://defillama.com/protocol/zircuit-finance
- **PRIORITY 39.3**  =  LIKELIHOOD 46.23 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 14.33/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,203,606 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`ERC1967Proxy` @ 0x075193D3…(ethereum), `InitializableImmutableAdminUpgradeabilityProxy` @ 0x23878914…(ethereum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for ERC1967Proxy@0x075193D3…(ethereum), InitializableImmutableAdminUpgradeabilityProxy@0x23878914…(ethereum); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#zircuit-finance|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#zircuit-finance`
- **Disclosure:** https://finance.zircuit.com/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.zircuit.com/zircuit-finance/zircuit-finance-vaults/security

### 81. Parallel Protocol V3  —  `ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 81
- **Protocol:** Parallel Protocol V3 (`parallel-protocol-v3`) · CDP · Ethereum, Hyperliquid L1, Avalanche, Base, Sonic
- **DefiLlama:** https://defillama.com/protocol/parallel-protocol-v3
- **PRIORITY 39.27**  =  LIKELIHOOD 46.2 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 14.3/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $2,131,744 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A vault share rate is an accounting quantity of another protocol, not a market price. Using it as a feed imports every way that vault's rate can be moved, including donation inflation and same-transaction redemption effects.
    - Deployed source (`DiamondProxy` @ 0x6efeDDF9…(ethereum), `PRL` @ 0x6c0aecee…(ethereum)): prerequisites matched: rate_used_as_price; no guard found
    - deployed source read for DiamondProxy@0x6efeDDF9…(ethereum), PRL@0x6c0aecee…(ethereum); indicators matched: rate_used_as_price
    - only one oracle (or none) is declared in DefiLlama metadata; this is a prioritisation signal about disclosure, not evidence that no cross-source deviation bound exists in code
    - declared oracles: DIA (types: Primary)
- **Preconditions PRESENT / UNKNOWN:** src::rate_used_as_price, value_decision_reads_configured_feed, live_positions_exposed / feed_selection_is_configuration
- **Guards searched / found:** deviation_bound_vs_independent_source / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Growth-capped rate adapter in the deployed oracle (kills the pair); Wrapper's own rate is monotonic and rate-limited; Collateral priced by an independent market feed instead
- **Where to start:** On a fork, donate to and cycle the underlying vault; assert the lending market's reported collateral price moves no more than the configured cap.
- **Evidence:** `protocols/deep_screened.jsonl#parallel-protocol-v3|ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE`, `protocols/onchain_probes.json#parallel-protocol-v3`
- **Disclosure:** https://parallel.best/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.parallel.best/resources/security-audits

### 82. DexFi Aggregator  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 82
- **Protocol:** DexFi Aggregator (`dexfi-aggregator`) · Yield Aggregator · Base, Robinhood Chain, Ethereum, Arbitrum, Binance, Avalanche …
- **DefiLlama:** https://defillama.com/protocol/dexfi-aggregator
- **PRIORITY 39.27**  =  LIKELIHOOD 46.2 × ACTIONABILITY 85.0%
    - likelihood = family evidence 30.0/50 (MATCH 60 × evidence weight 1.0) + learned attack surface 16.2/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $2,216,753 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 60 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `unverified_implementation` — raises likelihood, measured lift ×2.007 (weight +0.70)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`DexFiVaultFactory` @ 0x4c1a8a04…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for DexFiVaultFactory@0x4c1a8a04…(ethereum); indicators matched: claim_without_eligibility_map
    - 1 implementation(s) behind a proxy are NOT verified on the explorer: implementation identity unresolved, score capped at 60
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#dexfi-aggregator|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#dexfi-aggregator`
- **Disclosure:** https://dexfi.com/ · no audit link listed

### 83. Outcome Finance  —  `ACC-HARDCODED-PEG-REDEMPTION`

- **Rank (Ranking A — priority (likelihood × actionability)):** 83
- **Protocol:** Outcome Finance (`outcome-finance`) · Synthetics · Ethereum, Polygon, Boba
- **DefiLlama:** https://defillama.com/protocol/outcome-finance
- **PRIORITY 39.13**  =  LIKELIHOOD 46.03 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 14.13/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,342,626 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** If minting checks that the market price is at peg, redemption must apply the symmetric check. Asymmetric validation lets anyone buy the asset below peg and redeem it at par against real collateral.
    - Deployed source (`LongShortPairCreator` @ 0x0b8de441…(ethereum), `LongShortPairCreator` @ 0x31C89384…(ethereum)): prerequisites matched: redeem_hardcoded_peg; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): latestRoundData_used=no
    - deployed source read for LongShortPairCreator@0x0b8de441…(ethereum), LongShortPairCreator@0x31C89384…(ethereum); indicators matched: redeem_hardcoded_peg
- **Preconditions PRESENT / UNKNOWN:** src::redeem_hardcoded_peg, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Burn reads the same oracle as mint (kills the pair); Redemption disabled below a price band
- **Where to start:** On a fork, depeg the asset on its deepest venue and attempt redemption; the protocol must price the redemption at market or revert.
- **Evidence:** `protocols/deep_screened.jsonl#outcome-finance|ACC-HARDCODED-PEG-REDEMPTION`, `protocols/onchain_probes.json#outcome-finance`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.umaproject.org/resources/audit-and-bug-bounty-programs

### 84. Sorare Bridge  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 84
- **Protocol:** Sorare Bridge (`sorare-bridge`) · Canonical Bridge · Ethereum
- **DefiLlama:** https://defillama.com/protocol/sorare-bridge
- **PRIORITY 38.9**  =  LIKELIHOOD 45.77 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 13.87/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $4,348,374 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
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
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#sorare-bridge|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#sorare-bridge`
- **Disclosure:** https://sorare.com/ · no audit link listed

### 85. Snowbl Capital  —  `ACC-DONATION-UNACCOUNTED-BALANCE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 85
- **Protocol:** Snowbl Capital (`snowbl-capital`) · Onchain Capital Allocator · Base
- **DefiLlama:** https://defillama.com/protocol/snowbl-capital
- **PRIORITY 38.62**  =  LIKELIHOOD 38.62 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 6.72/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $90,437 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A share price, exchange rate or totalAssets must be a function of value the protocol accounted for on entry. Reading a raw balance makes any direct transfer into the accounting boundary an unpriced increase in every holder's claim.
    - Deployed source (`ReturnFinanceCompoundV3USDCVault` @ 0x0271A46c…(base), `ProjectTreasury` @ 0x07fF8bCe…(base)): prerequisites matched: totalAssets_reads_balanceOf; no guard found
    - deployed source read for ReturnFinanceCompoundV3USDCVault@0x0271A46c…(base), ProjectTreasury@0x07fF8bCe…(base); indicators matched: totalAssets_reads_balanceOf
- **Preconditions PRESENT / UNKNOWN:** src::totalAssets_reads_balanceOf, unprivileged_inbound_transfer_possible, live_value_exposed / src::getCashPrior_balanceOf
- **Guards searched / found:** internal_cash_counter / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** totalAssets derived from an internal counter, not balanceOf (kills the pair); Rate is monotonic and rate-limited per block; Inbound transfers to the accounting boundary are rejected or swept to a reserve
- **Where to start:** On a fork, transfer an arbitrary amount of each counted asset directly into every accounting boundary; the share price, exchange rate and derived borrow power must not change.
- **Evidence:** `protocols/deep_screened.jsonl#snowbl-capital|ACC-DONATION-UNACCOUNTED-BALANCE`, `protocols/onchain_probes.json#snowbl-capital`
- **Disclosure:** https://snowbl.capital · no audit link listed

### 86. Mars Poolin  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 86
- **Protocol:** Mars Poolin (`mars-poolin`) · Yield · Ethereum
- **DefiLlama:** https://defillama.com/protocol/mars-poolin
- **PRIORITY 38.33**  =  LIKELIHOOD 38.33 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 6.43/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $134,910 · **Band:** `IN_BAND`
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
- **Evidence:** `protocols/deep_screened.jsonl#mars-poolin|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#mars-poolin`
- **Disclosure:** https://mars.poolin.fi · no audit link listed

### 87. Rainbow Bridge  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 87
- **Protocol:** Rainbow Bridge (`rainbow-bridge`) · Bridge · Ethereum, Near
- **DefiLlama:** https://defillama.com/protocol/rainbow-bridge
- **PRIORITY 38.19**  =  LIKELIHOOD 44.93 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 13.03/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $2,413,425 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#rainbow-bridge|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#rainbow-bridge`
- **Disclosure:** https://rainbowbridge.app/transfer · no audit link listed

### 88. Latch  —  `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 88
- **Protocol:** Latch (`latch`) · Yield · Ethereum
- **DefiLlama:** https://defillama.com/protocol/latch
- **PRIORITY 38.15**  =  LIKELIHOOD 44.88 × ACTIONABILITY 85.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 7.98/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,631,769 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.
    - Deployed source (`DepositPool` @ 0x7cC08f23…(ethereum), `DepositPool` @ 0xFE606EEc…(ethereum)): prerequisites matched: caller_named_asset_no_registry_check; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): value_fn_moves_caller_named_asset=yes
    - deployed source read for DepositPool@0x7cC08f23…(ethereum), DepositPool@0xFE606EEc…(ethereum); indicators matched: caller_named_asset_no_registry_check, value_fn_moves_caller_named_asset
- **Preconditions PRESENT / UNKNOWN:** src::caller_named_asset_no_registry_check, live_value_present, deployment_reachable_on_chain / src::token_hook_credits_without_sender_check
- **Guards searched / found:** asset_registry_check_present / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Every identifier derived or verified against the factory/registry (kills the pair); Routing restricted to an immutable venue allowlist
- **Where to start:** On a fork, create a fake pool/mint and pass it to every identifier-accepting entrypoint; all must revert.
- **Evidence:** `protocols/deep_screened.jsonl#latch|ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`, `protocols/onchain_probes.json#latch`
- **Disclosure:** https://savings.latch.io/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.latch.io/overview/contracts-audit

### 89. Panoptic V2  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 89
- **Protocol:** Panoptic V2 (`panoptic-v2`) · Options · Ethereum
- **DefiLlama:** https://defillama.com/protocol/panoptic-v2
- **PRIORITY 38.11**  =  LIKELIHOOD 44.83 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 12.93/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,047,153 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`PanopticFactoryV3` @ 0x00000000…(ethereum), `PanopticFactoryV4` @ 0x00000000…(ethereum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for PanopticFactoryV3@0x00000000…(ethereum), PanopticFactoryV4@0x00000000…(ethereum); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#panoptic-v2|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#panoptic-v2`
- **Disclosure:** https://panoptic.xyz · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://panoptic.xyz/docs/security/security_audits

### 90. Untangled Vault  —  `ACC-NAV-SHAREPRICE-MANIPULABLE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 90
- **Protocol:** Untangled Vault (`untangled-vault`) · Onchain Capital Allocator · Celo, Polygon, Arbitrum
- **DefiLlama:** https://defillama.com/protocol/untangled-vault
- **PRIORITY 38.08**  =  LIKELIHOOD 38.08 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 6.18/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $151,334 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
- **Broken invariant tested:** totalAssets() must equal value the vault could actually realise now. Any component valued at book, at a manipulable rate, or after economic impairment lets a redeemer convert other depositors' claims into their own.
    - Deployed source (`SafeUsdVault` @ 0x97cf7976…(arbitrum)): prerequisites matched: totalAssets_reads_balanceOf; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): totalAssets_defined=yes
    - deployed source read for SafeUsdVault@0x97cf7976…(arbitrum); indicators matched: totalAssets_reads_balanceOf, totalAssets_defined
    - 1 live contract(s) answer totalAssets()
- **Preconditions PRESENT / UNKNOWN:** src::totalAssets_reads_balanceOf, erc4626_style_totalAssets_live, live_pooled_depositor_value / multi_component_totalAssets
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Share price rate-limited per block (kills same-transaction extraction); Single-asset vault with no external valuation; Withdrawals queued with a delay and priced at settlement
- **Where to start:** On a fork, for each component, force its valuation to zero and to 10x; the vault's mint/redeem must revert or be bounded, never transfer more than the depositor's pro-rata realisable share.
- **Evidence:** `protocols/deep_screened.jsonl#untangled-vault|ACC-NAV-SHAREPRICE-MANIPULABLE`, `protocols/onchain_probes.json#untangled-vault`
- **Disclosure:** https://untangled.finance · no audit link listed

### 91. Arca Labs ArCoin  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 91
- **Protocol:** Arca Labs ArCoin (`arca-labs-arcoin`) · RWA · Ethereum
- **DefiLlama:** https://defillama.com/protocol/arca-labs-arcoin
- **PRIORITY 37.93**  =  LIKELIHOOD 37.93 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 6.03/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $452,036 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `owner_is_eoa` — raises likelihood, measured lift ×1.729 (weight +0.55)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`Proxy` @ 0x25273948…(ethereum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for Proxy@0x25273948…(ethereum); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `EOA_SINGLE_KEY`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#arca-labs-arcoin|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#arca-labs-arcoin`
- **Disclosure:** https://www.arcalabs.com/ · no audit link listed

### 92. Flat Money V2  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 92
- **Protocol:** Flat Money V2 (`flat-money-v2`) · Partially Algorithmic Stablecoin · Arbitrum, Optimism
- **DefiLlama:** https://defillama.com/protocol/flat-money-v2
- **PRIORITY 37.87**  =  LIKELIHOOD 44.55 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 12.65/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,125,593 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`BeaconProxy` @ 0x29fAD9d4…(arbitrum), `StableModule` @ 0x86C7b964…(arbitrum)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for BeaconProxy@0x29fAD9d4…(arbitrum), StableModule@0x86C7b964…(arbitrum); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#flat-money-v2|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#flat-money-v2`
- **Disclosure:** https://flat.money · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/flat-money/flat-money-v2/blob/main/audits/audit-2025-09-08.pdf

### 93. ETH Strategy  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 93
- **Protocol:** ETH Strategy (`eth-strategy`) · Onchain Capital Allocator · Ethereum
- **DefiLlama:** https://defillama.com/protocol/eth-strategy
- **PRIORITY 37.84**  =  LIKELIHOOD 44.52 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 12.62/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $3,879,175 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`StratToken` @ 0x14cF922a…(ethereum)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for StratToken@0x14cF922a…(ethereum); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#eth-strategy|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#eth-strategy`
- **Disclosure:** https://www.ethstrat.xyz/ · no audit link listed

### 94. Inverse Finance Frontier  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 94
- **Protocol:** Inverse Finance Frontier (`inverse-finance-frontier`) · CDP · Ethereum
- **DefiLlama:** https://defillama.com/protocol/inverse-finance-frontier
- **PRIORITY 37.82**  =  LIKELIHOOD 44.5 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 12.6/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $4,540,643 · **Band:** `IN_BAND`
- **REPEAT VICTIM — 2 recorded hacks.** 2022-06-16 $5,800,000 [Spot Price Manipulation]; 2022-04-02 $15,600,000 [Spot Price Manipulation]
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`EthVault` @ 0x2dCdCA08…(ethereum), `Vault` @ 0x41D079ce…(ethereum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for EthVault@0x2dCdCA08…(ethereum), Vault@0x41D079ce…(ethereum); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `GOVERNOR`; no ERC-1967 admin chain was proven
- **Prior art:** `UNREMEDIATED_KNOWN_ISSUE` — DefiLlama's hacks dataset records 2 prior on-chain incident(s) on this protocol, most recently 2022-06-16 for $5,800,000 [Spot Price Manipulation]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#inverse-finance-frontier|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#inverse-finance-frontier`
- **Disclosure:** https://inverse.finance/ · no audit link listed

### 95. ApeChain Bridge  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 95
- **Protocol:** ApeChain Bridge (`apechain-bridge`) · Bridge · Ethereum
- **DefiLlama:** https://defillama.com/protocol/apechain-bridge
- **PRIORITY 37.82**  =  LIKELIHOOD 37.82 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 5.92/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $465,926 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#apechain-bridge|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#apechain-bridge`
- **Disclosure:** https://apechain.com/portal#bridge · no audit link listed

### 96. Pay Protocol  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 96
- **Protocol:** Pay Protocol (`pay-protocol`) · Payments · Tron, Binance, Ethereum
- **DefiLlama:** https://defillama.com/protocol/pay-protocol
- **PRIORITY 37.78**  =  LIKELIHOOD 44.45 × ACTIONABILITY 85.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 7.55/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,114,356 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`ChiToken` @ 0x00000000…(ethereum), `TrueGBP` @ 0x00000000…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for ChiToken@0x00000000…(ethereum), TrueGBP@0x00000000…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#pay-protocol|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#pay-protocol`
- **Disclosure:** https://payprotocol.network · no audit link listed

### 97. RateX DEX  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking A — priority (likelihood × actionability)):** 97
- **Protocol:** RateX DEX (`ratex-dex`) · Yield · Solana, Binance
- **DefiLlama:** https://defillama.com/protocol/ratex-dex
- **PRIORITY 37.68**  =  LIKELIHOOD 44.33 × ACTIONABILITY 85.0%
    - likelihood = family evidence 30.0/50 (MATCH 60 × evidence weight 1.0) + learned attack surface 14.33/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $2,899,456 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 60 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `unverified_implementation` — raises likelihood, measured lift ×2.007 (weight +0.70)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `owner_is_eoa` — raises likelihood, measured lift ×1.729 (weight +0.55)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source (`CollateralListaDistributor` @ 0x0c9a0f42…(bsc)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for CollateralListaDistributor@0x0c9a0f42…(bsc); indicators matched: unsafe_cross_sign_cast
    - 1 implementation(s) behind a proxy are NOT verified on the explorer: implementation identity unresolved, score capped at 60
- **Preconditions PRESENT / UNKNOWN:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** safecast_used / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#ratex-dex|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#ratex-dex`
- **Disclosure:** https://app.rate-x.io · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/RateX-Protocol/Audit-Report/blob/main/RateX-Sep-2024-OffsideLabs.final.pdf

### 98. Mars Ecosystem  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 98
- **Protocol:** Mars Ecosystem (`mars-ecosystem`) · CDP · Binance
- **DefiLlama:** https://defillama.com/protocol/mars-ecosystem
- **PRIORITY 37.67**  =  LIKELIHOOD 37.67 × ACTIONABILITY 100.0%
    - likelihood = family evidence 26.25/50 (MATCH 52.5 × evidence weight 1.0) + learned attack surface 11.42/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $234,866 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 52.5 · CONFIDENCE 76.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** After deployment, no caller may (re)establish ownership, admin, or implementation wiring. Initialization state must be provably consumed.
    - Deployed source (`MarsSwapFactory` @ 0x6f12482D…(bsc), `USDMToken` @ 0xBb0fA2fB…(bsc)): prerequisites matched: initialize_without_modifier; no guard found
    - deployed source read for MarsSwapFactory@0x6f12482D…(bsc), USDMToken@0xBb0fA2fB…(bsc); indicators matched: initialize_without_modifier
- **Preconditions PRESENT / UNKNOWN:** src::initialize_without_modifier, live_value_or_approvals / upgradeable_architecture, initializer_flag_unset
- **Guards searched / found:** initializer_modifier_present, upgrade_timelocked / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Simulated re-initialization reverts (kills the pair); Contract is non-upgradeable and holds no approvals
- **Where to start:** Read the initialization slot on every live proxy/facet and simulate re-initialization from an unprivileged address; it must revert.
- **Evidence:** `protocols/deep_screened.jsonl#mars-ecosystem|UPGRADE-INITIALIZER-REACHABLE-LIVE`, `protocols/onchain_probes.json#mars-ecosystem`
- **Disclosure:** https://marsecosystem.com/home · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://www.certik.org/projects/marsecosystem

### 99. Gondi V3  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 99
- **Protocol:** Gondi V3 (`gondi-v3`) · NFT Lending · Ethereum
- **DefiLlama:** https://defillama.com/protocol/gondi-v3
- **PRIORITY 37.65**  =  LIKELIHOOD 44.3 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 12.4/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $3,121,447 · **Band:** `IN_BAND`
- **Previously hacked:** 2026-03-09 for $230,000 [Token Approval Abuse]
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `KNOWN_ISSUE_DEPLOYMENT_STATUS_UNKNOWN` — DefiLlama's hacks dataset records 1 prior on-chain incident(s) on this protocol, most recently 2026-03-09 for $230,000 [Token Approval Abuse]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#gondi-v3|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#gondi-v3`
- **Disclosure:** https://www.gondi.xyz · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.gondi.xyz/security-and-audits

### 100. ZTLN-P  —  `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 100
- **Protocol:** ZTLN-P (`ztln-p`) · RWA · Ethereum
- **DefiLlama:** https://defillama.com/protocol/ztln-p
- **PRIORITY 37.51**  =  LIKELIHOOD 44.13 × ACTIONABILITY 85.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 7.23/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $2,199,757 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.
    - Deployed source (`ZTLNPrime` @ 0xf5429683…(ethereum)): prerequisites matched: caller_named_asset_no_registry_check; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): value_fn_moves_caller_named_asset=yes
    - deployed source read for ZTLNPrime@0xf5429683…(ethereum); indicators matched: caller_named_asset_no_registry_check, value_fn_moves_caller_named_asset
- **Preconditions PRESENT / UNKNOWN:** src::caller_named_asset_no_registry_check, live_value_present, deployment_reachable_on_chain / src::token_hook_credits_without_sender_check
- **Guards searched / found:** asset_registry_check_present / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Every identifier derived or verified against the factory/registry (kills the pair); Routing restricted to an immutable venue allowlist
- **Where to start:** On a fork, create a fake pool/mint and pass it to every identifier-accepting entrypoint; all must revert.
- **Evidence:** `protocols/deep_screened.jsonl#ztln-p|ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`, `protocols/onchain_probes.json#ztln-p`
- **Disclosure:** https://zoth.io/ · no audit link listed

### 101. Elysium Bridge  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 101
- **Protocol:** Elysium Bridge (`elysium-bridge`) · Bridge · Polygon, Ethereum
- **DefiLlama:** https://defillama.com/protocol/elysium-bridge
- **PRIORITY 37.5**  =  LIKELIHOOD 37.5 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 5.6/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $58,637 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
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
- **Evidence:** `protocols/deep_screened.jsonl#elysium-bridge|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#elysium-bridge`
- **Disclosure:** https://bridge.elysiumchain.tech · no audit link listed

### 102. Antarctic  —  `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 102
- **Protocol:** Antarctic (`antarctic`) · Derivatives · Arbitrum
- **DefiLlama:** https://defillama.com/protocol/antarctic
- **PRIORITY 37.33**  =  LIKELIHOOD 43.92 × ACTIONABILITY 85.0%
    - likelihood = family evidence 30.0/50 (MATCH 60 × evidence weight 1.0) + learned attack surface 13.92/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $9,494,061 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 60 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `unverified_implementation` — raises likelihood, measured lift ×2.007 (weight +0.70)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `owner_is_eoa` — raises likelihood, measured lift ×1.729 (weight +0.55)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.
    - Deployed source (`AMLP` @ 0x152f5E61…(arbitrum)): prerequisites matched: caller_named_asset_no_registry_check; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): value_fn_moves_caller_named_asset=yes
    - deployed source read for AMLP@0x152f5E61…(arbitrum); indicators matched: caller_named_asset_no_registry_check, value_fn_moves_caller_named_asset
    - 1 implementation(s) behind a proxy are NOT verified on the explorer: implementation identity unresolved, score capped at 60
- **Preconditions PRESENT / UNKNOWN:** src::caller_named_asset_no_registry_check, live_value_present, deployment_reachable_on_chain / src::token_hook_credits_without_sender_check
- **Guards searched / found:** asset_registry_check_present / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `EOA_SINGLE_KEY`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Every identifier derived or verified against the factory/registry (kills the pair); Routing restricted to an immutable venue allowlist
- **Where to start:** On a fork, create a fake pool/mint and pass it to every identifier-accepting entrypoint; all must revert.
- **Evidence:** `protocols/deep_screened.jsonl#antarctic|ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`, `protocols/onchain_probes.json#antarctic`
- **Disclosure:** https://www.antarctic.exchange/ · no audit link listed

### 103. NUVA  —  `ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 103
- **Protocol:** NUVA (`nuva`) · Yield · Ethereum, Provenance
- **DefiLlama:** https://defillama.com/protocol/nuva
- **PRIORITY 37.08**  =  LIKELIHOOD 43.62 × ACTIONABILITY 85.0%
    - likelihood = family evidence 26.25/50 (MATCH 52.5 × evidence weight 1.0) + learned attack surface 17.37/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $5,572,761 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 52.5 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A vault share rate is an accounting quantity of another protocol, not a market price. Using it as a feed imports every way that vault's rate can be moved, including donation inflation and same-transaction redemption effects.
    - Deployed source (`DedicatedVaultRouter` @ 0xe1cffb8b…(ethereum)): prerequisites matched: rate_used_as_price; no guard found
    - deployed source read for DedicatedVaultRouter@0xe1cffb8b…(ethereum); indicators matched: rate_used_as_price
    - only one oracle (or none) is declared in DefiLlama metadata; this is a prioritisation signal about disclosure, not evidence that no cross-source deviation bound exists in code
    - declared oracles: none declared
- **Preconditions PRESENT / UNKNOWN:** src::rate_used_as_price, live_positions_exposed / value_decision_reads_configured_feed, feed_selection_is_configuration
- **Guards searched / found:** deviation_bound_vs_independent_source / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `TIMELOCK`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Growth-capped rate adapter in the deployed oracle (kills the pair); Wrapper's own rate is monotonic and rate-limited; Collateral priced by an independent market feed instead
- **Where to start:** On a fork, donate to and cycle the underlying vault; assert the lending market's reported collateral price moves no more than the configured cap.
- **Evidence:** `protocols/deep_screened.jsonl#nuva|ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE`, `protocols/onchain_probes.json#nuva`
- **Disclosure:** https://nuva.finance · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://nuva.finance/docs/security-audits

### 104. Morpho Midnight  —  `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 104
- **Protocol:** Morpho Midnight (`morpho-midnight`) · Lending · Base
- **DefiLlama:** https://defillama.com/protocol/morpho-midnight
- **PRIORITY 37.08**  =  LIKELIHOOD 43.62 × ACTIONABILITY 85.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 6.72/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $4,311,379 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.
    - Deployed source (`Midnight` @ 0xAdedD8ab…(base)): prerequisites matched: caller_named_asset_no_registry_check; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): value_fn_moves_caller_named_asset=yes
    - deployed source read for Midnight@0xAdedD8ab…(base); indicators matched: caller_named_asset_no_registry_check, value_fn_moves_caller_named_asset
- **Preconditions PRESENT / UNKNOWN:** src::caller_named_asset_no_registry_check, live_value_present, deployment_reachable_on_chain / src::token_hook_credits_without_sender_check
- **Guards searched / found:** asset_registry_check_present / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Every identifier derived or verified against the factory/registry (kills the pair); Routing restricted to an immutable venue allowlist
- **Where to start:** On a fork, create a fake pool/mint and pass it to every identifier-accepting entrypoint; all must revert.
- **Evidence:** `protocols/deep_screened.jsonl#morpho-midnight|ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`, `protocols/onchain_probes.json#morpho-midnight`
- **Disclosure:** https://app.morpho.org · no audit link listed

### 105. Peridot  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 105
- **Protocol:** Peridot (`peridot`) · Lending · Stellar, Monad, Binance
- **DefiLlama:** https://defillama.com/protocol/peridot
- **PRIORITY 37.07**  =  LIKELIHOOD 37.07 × ACTIONABILITY 100.0%
    - likelihood = family evidence 26.25/50 (MATCH 52.5 × evidence weight 1.0) + learned attack surface 10.82/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $53,524 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 52.5 · CONFIDENCE 76.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
- **Broken invariant tested:** After deployment, no caller may (re)establish ownership, admin, or implementation wiring. Initialization state must be provably consumed.
    - Deployed source (`Unitroller` @ 0x6fC0c155…(bsc)): prerequisites matched: initialize_without_modifier; no guard found
    - deployed source read for Unitroller@0x6fC0c155…(bsc); indicators matched: initialize_without_modifier
- **Preconditions PRESENT / UNKNOWN:** src::initialize_without_modifier, live_value_or_approvals / upgradeable_architecture, initializer_flag_unset
- **Guards searched / found:** initializer_modifier_present, upgrade_timelocked / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Simulated re-initialization reverts (kills the pair); Contract is non-upgradeable and holds no approvals
- **Where to start:** Read the initialization slot on every live proxy/facet and simulate re-initialization from an unprivileged address; it must revert.
- **Evidence:** `protocols/deep_screened.jsonl#peridot|UPGRADE-INITIALIZER-REACHABLE-LIVE`, `protocols/onchain_probes.json#peridot`
- **Disclosure:** https://peridot.finance/ · no audit link listed

### 106. Cat in a Box  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 106
- **Protocol:** Cat in a Box (`cat-in-a-box`) · Lending · Ethereum
- **DefiLlama:** https://defillama.com/protocol/cat-in-a-box
- **PRIORITY 36.92**  =  LIKELIHOOD 49.23 × ACTIONABILITY 75.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 17.33/50
    - actionability: small enough to be unwatched, large enough to matter; no public disclosure channel listed
- **Value at risk:** $206,747 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#cat-in-a-box|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#cat-in-a-box`
- **Disclosure:** not listed · no audit link listed

### 107. Radpie  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 107
- **Protocol:** Radpie (`radpie`) · Yield · Arbitrum, Binance
- **DefiLlama:** https://defillama.com/protocol/radpie
- **PRIORITY 36.28**  =  LIKELIHOOD 42.68 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 10.78/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $6,831,163 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`RadiantStaking` @ 0xa9aa407d…(arbitrum)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for RadiantStaking@0xa9aa407d…(arbitrum); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#radpie|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#radpie`
- **Disclosure:** https://www.radiant.magpiexyz.io/stake · no audit link listed

### 108. Ample  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 108
- **Protocol:** Ample (`ample`) · Yield Lottery · Base, Solana, Arbitrum, Hyperliquid L1, Monad, Katana …
- **DefiLlama:** https://defillama.com/protocol/ample
- **PRIORITY 36.18**  =  LIKELIHOOD 42.57 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 10.67/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $4,585,344 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`AmpleEarn` @ 0x1688aeb3…(base)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for AmpleEarn@0x1688aeb3…(base); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#ample|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#ample`
- **Disclosure:** https://ample.money/ · no audit link listed

### 109. SPOT Cash  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 109
- **Protocol:** SPOT Cash (`spot-cash`) · Algo-Stables · Ethereum
- **DefiLlama:** https://defillama.com/protocol/spot-cash
- **PRIORITY 36.1**  =  LIKELIHOOD 36.1 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 4.2/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $245,572 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`TransparentUpgradeableProxy` @ 0x82A91a0D…(ethereum), `AdminUpgradeabilityProxy` @ 0xd46ba6d9…(ethereum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for TransparentUpgradeableProxy@0x82A91a0D…(ethereum), AdminUpgradeabilityProxy@0xd46ba6d9…(ethereum); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#spot-cash|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#spot-cash`
- **Disclosure:** https://www.spot.cash · no audit link listed

### 110. Citrea Bridge  —  `PROOF-VERIFICATION-BYPASSED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 110
- **Protocol:** Citrea Bridge (`citrea-bridge`) · Bridge · Bitcoin, Ethereum
- **DefiLlama:** https://defillama.com/protocol/citrea-bridge
- **PRIORITY 36.08**  =  LIKELIHOOD 42.45 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 10.55/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $5,967,379 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
- **Broken invariant tested:** A withdrawal or mint gated by a proof must verify that proof against the correct verifying key, over all the public inputs that bind the action, and must reject when any component is absent.
    - Deployed source (`WBTCOFTAdapter` @ 0x2c01390E…(ethereum), `TransparentUpgradeableProxy` @ 0x6925ccD2…(ethereum)): prerequisites matched: proof_result_unchecked; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): verifier_address_mutable=no
    - deployed source read for WBTCOFTAdapter@0x2c01390E…(ethereum), TransparentUpgradeableProxy@0x6925ccD2…(ethereum); indicators matched: proof_result_unchecked
- **Preconditions PRESENT / UNKNOWN:** src::proof_result_unchecked, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Verifying key immutable and attested (kills the misconfiguration shape); No alternative release path exists (enumerate selectors)
- **Where to start:** On a fork, submit an empty proof, a proof for different public inputs, and a proof under a foreign key; every release path must revert.
- **Evidence:** `protocols/deep_screened.jsonl#citrea-bridge|PROOF-VERIFICATION-BYPASSED`, `protocols/onchain_probes.json#citrea-bridge`
- **Disclosure:** https://citrea.xyz/bridge · no audit link listed

### 111. Ribbon Earn  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 111
- **Protocol:** Ribbon Earn (`ribbon-earn`) · Options · Ethereum
- **DefiLlama:** https://defillama.com/protocol/ribbon-earn
- **PRIORITY 35.8**  =  LIKELIHOOD 42.12 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 10.22/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,042,196 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`AdminUpgradeabilityProxy` @ 0x84c2b16F…(ethereum), `AdminUpgradeabilityProxy` @ 0xCE551347…(ethereum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for AdminUpgradeabilityProxy@0x84c2b16F…(ethereum), AdminUpgradeabilityProxy@0xCE551347…(ethereum); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#ribbon-earn|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#ribbon-earn`
- **Disclosure:** https://www.ribbon.finance/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.ribbon.finance/developers/security#audits

### 112. Baseline Protocol  —  `SIG-VERIFIER-DEFEATABLE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 112
- **Protocol:** Baseline Protocol (`baseline-protocol`) · Liquidity Manager · Ethereum, Base, Blast
- **DefiLlama:** https://defillama.com/protocol/baseline-protocol
- **PRIORITY 35.46**  =  LIKELIHOOD 41.72 × ACTIONABILITY 85.0%
    - likelihood = family evidence 30.0/50 (MATCH 60 × evidence weight 1.0) + learned attack surface 11.72/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,980,770 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 60 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `unverified_implementation` — raises likelihood, measured lift ×2.007 (weight +0.70)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A verification routine must reject malformed, empty or zero-recovered signatures, and must never treat address(0) as a match.
    - Deployed source (`BToken` @ 0x9fDbDE76…(ethereum)): prerequisites matched: ecrecover_without_zero_check; no guard found
    - deployed source read for BToken@0x9fDbDE76…(ethereum); indicators matched: ecrecover_without_zero_check
    - 1 implementation(s) behind a proxy are NOT verified on the explorer: implementation identity unresolved, score capped at 60
- **Preconditions PRESENT / UNKNOWN:** src::ecrecover_without_zero_check, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** uses_oz_ecdsa / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** OZ ECDSA library in the deployed bytecode (kills the ecrecover-zero shape); Signer address immutable and non-zero
- **Where to start:** On a fork, submit r=0,s=0,v=27 and an empty signature to every signature-gated entrypoint; all must revert.
- **Evidence:** `protocols/deep_screened.jsonl#baseline-protocol|SIG-VERIFIER-DEFEATABLE`, `protocols/onchain_probes.json#baseline-protocol`
- **Disclosure:** https://www.baseline.markets/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://www.baseline.markets/docs/contracts/security

### 113. Sovryn Bridge  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 113
- **Protocol:** Sovryn Bridge (`sovryn-bridge`) · Canonical Bridge · Binance, Ethereum
- **DefiLlama:** https://defillama.com/protocol/sovryn-bridge
- **PRIORITY 35.42**  =  LIKELIHOOD 41.67 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 9.77/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $3,104,665 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#sovryn-bridge|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#sovryn-bridge`
- **Disclosure:** https://alpha.sovryn.app · no audit link listed

### 114. StakeStone Berachain Vault  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 114
- **Protocol:** StakeStone Berachain Vault (`stakestone-berachain-vault`) · Onchain Capital Allocator · Ethereum
- **DefiLlama:** https://defillama.com/protocol/stakestone-berachain-vault
- **PRIORITY 35.4**  =  LIKELIHOOD 41.65 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 9.75/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $3,521,410 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`StoneBeraVault` @ 0x8f88aE37…(ethereum), `SBTCBeraVault` @ 0xf401Cc9f…(ethereum)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for StoneBeraVault@0x8f88aE37…(ethereum), SBTCBeraVault@0xf401Cc9f…(ethereum); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#stakestone-berachain-vault|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#stakestone-berachain-vault`
- **Disclosure:** https://app.stakestone.io/u/vault · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/slowmist/Knowledge-Base/blob/master/open-report-V2/smart-contract/Stone%20Bera%20Vault%20-%20SlowMist%20Audit%20Report.pdf

### 115. Decentralized Euro  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 115
- **Protocol:** Decentralized Euro (`decentralized-euro`) · CDP · Ethereum
- **DefiLlama:** https://defillama.com/protocol/decentralized-euro
- **PRIORITY 35.4**  =  LIKELIHOOD 41.65 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 9.75/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,380,340 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`DEPSWrapper` @ 0x10374792…(ethereum), `Equity` @ 0x1bA26788…(ethereum)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for DEPSWrapper@0x10374792…(ethereum), Equity@0x1bA26788…(ethereum); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#decentralized-euro|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#decentralized-euro`
- **Disclosure:** https://deuro.com/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/d-EURO/landingPage/blob/develop/audits/ChainSecurity_dEURO_intermediate_report.pdf

### 116. Governor DAO  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 116
- **Protocol:** Governor DAO (`governor-dao`) · Yield · Ethereum
- **DefiLlama:** https://defillama.com/protocol/governor-dao
- **PRIORITY 35.09**  =  LIKELIHOOD 46.78 × ACTIONABILITY 75.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 14.88/50
    - actionability: small enough to be unwatched, large enough to matter; no public disclosure channel listed
- **Value at risk:** $62,828 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
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
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#governor-dao|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#governor-dao`
- **Disclosure:** not listed · no audit link listed

### 117. Angstrom  —  `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 117
- **Protocol:** Angstrom (`angstrom`) · Dexs · Ethereum
- **DefiLlama:** https://defillama.com/protocol/angstrom
- **PRIORITY 34.94**  =  LIKELIHOOD 41.1 × ACTIONABILITY 85.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 4.2/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $5,726,056 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.
    - Deployed source (`Angstrom` @ 0x0000000a…(ethereum)): prerequisites matched: caller_named_asset_no_registry_check; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): value_fn_moves_caller_named_asset=yes
    - deployed source read for Angstrom@0x0000000a…(ethereum); indicators matched: caller_named_asset_no_registry_check, value_fn_moves_caller_named_asset
- **Preconditions PRESENT / UNKNOWN:** src::caller_named_asset_no_registry_check, live_value_present, deployment_reachable_on_chain / src::token_hook_credits_without_sender_check
- **Guards searched / found:** asset_registry_check_present / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Every identifier derived or verified against the factory/registry (kills the pair); Routing restricted to an immutable venue allowlist
- **Where to start:** On a fork, create a fake pool/mint and pass it to every identifier-accepting entrypoint; all must revert.
- **Evidence:** `protocols/deep_screened.jsonl#angstrom|ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`, `protocols/onchain_probes.json#angstrom`
- **Disclosure:** https://angstrom.xyz/ · no audit link listed

### 118. HLP0  —  `ACC-NAV-SHAREPRICE-MANIPULABLE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 118
- **Protocol:** HLP0 (`hlp0`) · Yield · Arbitrum
- **DefiLlama:** https://defillama.com/protocol/hlp0
- **PRIORITY 34.93**  =  LIKELIHOOD 34.93 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 3.03/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $387,861 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** totalAssets() must equal value the vault could actually realise now. Any component valued at book, at a manipulable rate, or after economic impairment lets a redeemer convert other depositors' claims into their own.
    - Deployed source (`SafeUsdVault` @ 0x97cf7976…(arbitrum)): prerequisites matched: totalAssets_reads_balanceOf; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): totalAssets_defined=yes
    - deployed source read for SafeUsdVault@0x97cf7976…(arbitrum); indicators matched: totalAssets_reads_balanceOf, totalAssets_defined
    - 1 live contract(s) answer totalAssets()
- **Preconditions PRESENT / UNKNOWN:** src::totalAssets_reads_balanceOf, erc4626_style_totalAssets_live, live_pooled_depositor_value / multi_component_totalAssets
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Share price rate-limited per block (kills same-transaction extraction); Single-asset vault with no external valuation; Withdrawals queued with a delay and priced at settlement
- **Where to start:** On a fork, for each component, force its valuation to zero and to 10x; the vault's mint/redeem must revert or be bounded, never transfer more than the depositor's pro-rata realisable share.
- **Evidence:** `protocols/deep_screened.jsonl#hlp0|ACC-NAV-SHAREPRICE-MANIPULABLE`, `protocols/onchain_probes.json#hlp0`
- **Disclosure:** https://www.hlp0.to/ · no audit link listed

### 119. Usual ETH0  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 119
- **Protocol:** Usual ETH0 (`usual-eth0`) · Synthetics · Ethereum
- **DefiLlama:** https://defillama.com/protocol/usual-eth0
- **PRIORITY 34.89**  =  LIKELIHOOD 41.05 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 9.15/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $2,272,053 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
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
- **Evidence:** `protocols/deep_screened.jsonl#usual-eth0|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#usual-eth0`
- **Disclosure:** https://usual.money · no audit link listed

### 120. Rho X  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 120
- **Protocol:** Rho X (`rho-x`) · Interest Rate Derivatives · Ethereum
- **DefiLlama:** https://defillama.com/protocol/rho-x
- **PRIORITY 34.89**  =  LIKELIHOOD 41.05 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 9.15/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,037,690 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
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
- **Evidence:** `protocols/deep_screened.jsonl#rho-x|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#rho-x`
- **Disclosure:** https://x.rho.trading/ · no audit link listed

### 121. Limitless Exchange  —  `ACC-DUPLICATE-ID-ACCUMULATION`

- **Rank (Ranking A — priority (likelihood × actionability)):** 121
- **Protocol:** Limitless Exchange (`limitless-exchange`) · Prediction Market · Base
- **DefiLlama:** https://defillama.com/protocol/limitless-exchange
- **PRIORITY 34.43**  =  LIKELIHOOD 34.43 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 2.53/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $395,169 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** An entitlement attached to an identifier may be counted at most once per period. A caller-supplied ID list must be deduplicated, or each ID's claim state consumed before the next read.
    - Deployed source (`FixedProductMarketMakerFactory` @ 0xc397D5d7…(base), `ConditionalTokens` @ 0xc9c98965…(base)): prerequisites matched: id_array_loop_without_dedup; no guard found
    - deployed source read for FixedProductMarketMakerFactory@0xc397D5d7…(base), ConditionalTokens@0xc9c98965…(base); indicators matched: id_array_loop_without_dedup
- **Preconditions PRESENT / UNKNOWN:** src::id_array_loop_without_dedup, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Consumed marker written inside the loop (kills the pair); IDs required strictly increasing
- **Where to start:** On a fork, call the batch function with one ID repeated k times; payout must equal the single-ID payout.
- **Evidence:** `protocols/deep_screened.jsonl#limitless-exchange|ACC-DUPLICATE-ID-ACCUMULATION`, `protocols/onchain_probes.json#limitless-exchange`
- **Disclosure:** https://limitless.exchange · no audit link listed

### 122. Reya Bridge  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 122
- **Protocol:** Reya Bridge (`reya-bridge`) · Canonical Bridge · Ethereum, Arbitrum, Optimism, Base, Polygon
- **DefiLlama:** https://defillama.com/protocol/reya-bridge
- **PRIORITY 33.9**  =  LIKELIHOOD 39.88 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 7.98/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $5,024,919 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ChiToken` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ChiToken@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#reya-bridge|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#reya-bridge`
- **Disclosure:** https://app.reya.xyz · no audit link listed

### 123. Gravity Bridge  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 123
- **Protocol:** Gravity Bridge (`gravity-bridge`) · Bridge · GravityBridge, Ethereum
- **DefiLlama:** https://defillama.com/protocol/gravity-bridge
- **PRIORITY 33.77**  =  LIKELIHOOD 39.73 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 7.83/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $5,126,360 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`BridgeToken` @ 0x07baC358…(ethereum), `GeoToken` @ 0x147faF8D…(ethereum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for BridgeToken@0x07baC358…(ethereum), GeoToken@0x147faF8D…(ethereum); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#gravity-bridge|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#gravity-bridge`
- **Disclosure:** https://www.gravitybridge.net · no audit link listed

### 124. Superfund  —  `ACC-DONATION-UNACCOUNTED-BALANCE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 124
- **Protocol:** Superfund (`superfund`) · Onchain Capital Allocator · Base
- **DefiLlama:** https://defillama.com/protocol/superfund
- **PRIORITY 33.67**  =  LIKELIHOOD 33.67 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 1.77/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $71,832 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A share price, exchange rate or totalAssets must be a function of value the protocol accounted for on entry. Reading a raw balance makes any direct transfer into the accounting boundary an unpriced increase in every holder's claim.
    - Deployed source (`EulerEarn` @ 0x10076ed2…(base)): prerequisites matched: totalAssets_reads_balanceOf; no guard found
    - deployed source read for EulerEarn@0x10076ed2…(base); indicators matched: totalAssets_reads_balanceOf
- **Preconditions PRESENT / UNKNOWN:** src::totalAssets_reads_balanceOf, unprivileged_inbound_transfer_possible, live_value_exposed / src::getCashPrior_balanceOf
- **Guards searched / found:** internal_cash_counter / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** totalAssets derived from an internal counter, not balanceOf (kills the pair); Rate is monotonic and rate-limited per block; Inbound transfers to the accounting boundary are rejected or swept to a reserve
- **Where to start:** On a fork, transfer an arbitrary amount of each counted asset directly into every accounting boundary; the share price, exchange rate and derived borrow power must not change.
- **Evidence:** `protocols/deep_screened.jsonl#superfund|ACC-DONATION-UNACCOUNTED-BALANCE`, `protocols/onchain_probes.json#superfund`
- **Disclosure:** https://funds.superlend.xyz/ · no audit link listed

### 125. 3F Mutual  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 125
- **Protocol:** 3F Mutual (`3f-mutual`) · Insurance · Ethereum
- **DefiLlama:** https://defillama.com/protocol/3f-mutual
- **PRIORITY 33.26**  =  LIKELIHOOD 39.13 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 7.23/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $4,654,547 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
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
- **Evidence:** `protocols/deep_screened.jsonl#3f-mutual|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#3f-mutual`
- **Disclosure:** https://3fmutual.com/ · no audit link listed

### 126. DeFi Franc  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 126
- **Protocol:** DeFi Franc (`defi-franc`) · CDP · Ethereum
- **DefiLlama:** https://defillama.com/protocol/defi-franc
- **PRIORITY 32.92**  =  LIKELIHOOD 43.9 × ACTIONABILITY 75.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 12.0/50
    - actionability: small enough to be unwatched, large enough to matter; no public disclosure channel listed
- **Value at risk:** $261,896 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#defi-franc|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#defi-franc`
- **Disclosure:** not listed · no audit link listed

### 127. Boba Bridge  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 127
- **Protocol:** Boba Bridge (`boba-bridge`) · Canonical Bridge · Ethereum
- **DefiLlama:** https://defillama.com/protocol/boba-bridge
- **PRIORITY 32.58**  =  LIKELIHOOD 38.33 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 6.43/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $2,861,464 · **Band:** `IN_BAND`
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
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#boba-bridge|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#boba-bridge`
- **Disclosure:** https://gateway.boba.network · no audit link listed

### 128. xSigma  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 128
- **Protocol:** xSigma (`xsigma`) · Dexs · Ethereum
- **DefiLlama:** https://defillama.com/protocol/xsigma
- **PRIORITY 32.3**  =  LIKELIHOOD 43.07 × ACTIONABILITY 75.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 11.17/50
    - actionability: small enough to be unwatched, large enough to matter; no public disclosure channel listed
- **Value at risk:** $317,096 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#xsigma|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#xsigma`
- **Disclosure:** not listed · no audit link listed

### 129. Orion Liquidity Nodes  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 129
- **Protocol:** Orion Liquidity Nodes (`orion-liquidity-nodes`) · Dexs · Binance, Ethereum, Polygon, Fantom
- **DefiLlama:** https://defillama.com/protocol/orion-liquidity-nodes
- **PRIORITY 31.37**  =  LIKELIHOOD 41.83 × ACTIONABILITY 75.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 9.93/50
    - actionability: small enough to be unwatched, large enough to matter; no public disclosure channel listed
- **Value at risk:** $96,999 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#orion-liquidity-nodes|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#orion-liquidity-nodes`
- **Disclosure:** not listed · no audit link listed

### 130. Lybra V2  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 130
- **Protocol:** Lybra V2 (`lybra-v2`) · CDP · Ethereum
- **DefiLlama:** https://defillama.com/protocol/lybra-v2
- **PRIORITY 31.25**  =  LIKELIHOOD 41.67 × ACTIONABILITY 75.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 9.77/50
    - actionability: small enough to be unwatched, large enough to matter; no public disclosure channel listed
- **Value at risk:** $51,036 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#lybra-v2|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#lybra-v2`
- **Disclosure:** not listed · no audit link listed

### 131. Fraxlend  —  `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 131
- **Protocol:** Fraxlend (`fraxlend`) · Lending · Ethereum, Fraxtal, Arbitrum
- **DefiLlama:** https://defillama.com/protocol/fraxlend
- **PRIORITY 31.0**  =  LIKELIHOOD 51.67 × ACTIONABILITY 60.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 14.77/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $23,124,638 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
- **Broken invariant tested:** Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.
    - Deployed source (`FraxlendPairRegistry` @ 0xD6E9D27C…(ethereum), `FRAXShares` @ 0x3432b6a6…(ethereum)): prerequisites matched: caller_named_asset_no_registry_check; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): value_fn_moves_caller_named_asset=yes
    - deployed source read for FraxlendPairRegistry@0xD6E9D27C…(ethereum), FRAXShares@0x3432b6a6…(ethereum); indicators matched: caller_named_asset_no_registry_check, value_fn_moves_caller_named_asset
- **Preconditions PRESENT / UNKNOWN:** src::caller_named_asset_no_registry_check, live_value_present, deployment_reachable_on_chain / src::token_hook_credits_without_sender_check
- **Guards searched / found:** asset_registry_check_present / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Every identifier derived or verified against the factory/registry (kills the pair); Routing restricted to an immutable venue allowlist
- **Where to start:** On a fork, create a fake pool/mint and pass it to every identifier-accepting entrypoint; all must revert.
- **Evidence:** `protocols/deep_screened.jsonl#fraxlend|ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`, `protocols/onchain_probes.json#fraxlend`
- **Disclosure:** https://frax.com/lend · no audit link listed

### 132. Aegis Markets  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 132
- **Protocol:** Aegis Markets (`aegis-markets`) · Liquidity Manager · Unichain, Base
- **DefiLlama:** https://defillama.com/protocol/aegis-markets
- **PRIORITY 30.92**  =  LIKELIHOOD 36.38 × ACTIONABILITY 85.0%
    - likelihood = family evidence 26.25/50 (MATCH 52.5 × evidence weight 1.0) + learned attack surface 10.13/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,862,507 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 52.5 · CONFIDENCE 76.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** After deployment, no caller may (re)establish ownership, admin, or implementation wiring. Initialization state must be provably consumed.
    - Deployed source (`Spot` @ 0x88c9ff9f…(base)): prerequisites matched: initialize_without_modifier; no guard found
    - deployed source read for Spot@0x88c9ff9f…(base); indicators matched: initialize_without_modifier
- **Preconditions PRESENT / UNKNOWN:** src::initialize_without_modifier, live_value_or_approvals / upgradeable_architecture, initializer_flag_unset
- **Guards searched / found:** initializer_modifier_present, upgrade_timelocked / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Simulated re-initialization reverts (kills the pair); Contract is non-upgradeable and holds no approvals
- **Where to start:** Read the initialization slot on every live proxy/facet and simulate re-initialization from an unprivileged address; it must revert.
- **Evidence:** `protocols/deep_screened.jsonl#aegis-markets|UPGRADE-INITIALIZER-REACHABLE-LIVE`, `protocols/onchain_probes.json#aegis-markets`
- **Disclosure:** https://aegis.markets/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.aegis.markets/audits

### 133. BOB Bridge  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 133
- **Protocol:** BOB Bridge (`bob-bridge`) · Bridge · Ethereum
- **DefiLlama:** https://defillama.com/protocol/bob-bridge
- **PRIORITY 30.68**  =  LIKELIHOOD 36.1 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 4.2/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $3,024,926 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
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
- **Evidence:** `protocols/deep_screened.jsonl#bob-bridge|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#bob-bridge`
- **Disclosure:** https://www.gobob.xyz · no audit link listed

### 134. Nsure  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 134
- **Protocol:** Nsure (`nsure`) · Insurance · Ethereum
- **DefiLlama:** https://defillama.com/protocol/nsure
- **PRIORITY 30.65**  =  LIKELIHOOD 40.87 × ACTIONABILITY 75.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 8.97/50
    - actionability: small enough to be unwatched, large enough to matter; no public disclosure channel listed
- **Value at risk:** $247,689 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
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
- **Evidence:** `protocols/deep_screened.jsonl#nsure|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#nsure`
- **Disclosure:** not listed · no audit link listed

### 135. cBridge  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 135
- **Protocol:** cBridge (`cbridge`) · Bridge · Ethereum, Binance, Polygon, Arbitrum, Optimism, zkSync Era …
- **DefiLlama:** https://defillama.com/protocol/cbridge
- **PRIORITY 30.52**  =  LIKELIHOOD 50.87 × ACTIONABILITY 60.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 18.97/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $14,619,877 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#cbridge|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#cbridge`
- **Disclosure:** https://cbridge.celer.network/#/transfer · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/celer-network/sgn-v2-contracts/tree/main/audit

### 136. Ekubo  —  `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 136
- **Protocol:** Ekubo (`ekubo`) · Dexs · Starknet, Ethereum, Robinhood Chain
- **DefiLlama:** https://defillama.com/protocol/ekubo
- **PRIORITY 30.41**  =  LIKELIHOOD 50.68 × ACTIONABILITY 60.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 13.78/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $25,947,903 · **Band:** `IN_BAND`
- **Previously hacked:** 2026-05-05 for $1,400,000 [Token Approval Abuse]
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.
    - Deployed source (`Core` @ 0x00000000…(ethereum), `Core` @ 0xe0e0e08a…(ethereum)): prerequisites matched: caller_named_asset_no_registry_check; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): value_fn_moves_caller_named_asset=yes
    - deployed source read for Core@0x00000000…(ethereum), Core@0xe0e0e08a…(ethereum); indicators matched: caller_named_asset_no_registry_check, value_fn_moves_caller_named_asset
- **Preconditions PRESENT / UNKNOWN:** src::caller_named_asset_no_registry_check, live_value_present, deployment_reachable_on_chain / src::token_hook_credits_without_sender_check
- **Guards searched / found:** asset_registry_check_present / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `KNOWN_ISSUE_DEPLOYMENT_STATUS_UNKNOWN` — DefiLlama's hacks dataset records 1 prior on-chain incident(s) on this protocol, most recently 2026-05-05 for $1,400,000 [Token Approval Abuse]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** Every identifier derived or verified against the factory/registry (kills the pair); Routing restricted to an immutable venue allowlist
- **Where to start:** On a fork, create a fake pool/mint and pass it to every identifier-accepting entrypoint; all must revert.
- **Evidence:** `protocols/deep_screened.jsonl#ekubo|ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`, `protocols/onchain_probes.json#ekubo`
- **Disclosure:** https://ekubo.org/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.ekubo.org/integration-guides/reference/audits

### 137. Mento V2  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 137
- **Protocol:** Mento V2 (`mento-v2`) · Algo-Stables · Ethereum, Celo, Monad, Bitcoin
- **DefiLlama:** https://defillama.com/protocol/mento-v2
- **PRIORITY 30.12**  =  LIKELIHOOD 50.2 × ACTIONABILITY 60.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 18.3/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $11,919,606 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `version_sibling_legacy` — raises likelihood, measured lift ×1.699 (weight +0.53)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#mento-v2|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#mento-v2`
- **Disclosure:** https://app.mento.org · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://celo.org/audits

### 138. Juicebox V1  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 138
- **Protocol:** Juicebox V1 (`juicebox-v1`) · Launchpad · Ethereum
- **DefiLlama:** https://defillama.com/protocol/juicebox-v1
- **PRIORITY 29.67**  =  LIKELIHOOD 49.45 × ACTIONABILITY 60.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 17.55/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $12,464,696 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `version_sibling_legacy` — raises likelihood, measured lift ×1.699 (weight +0.53)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#juicebox-v1|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#juicebox-v1`
- **Disclosure:** https://juicebox.money/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://hacken.io/wp-content/uploads/2022/01/%D0%A1onstitution-DAO_11012022Audit_Report.pdf

### 139. Origin ARM  —  `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 139
- **Protocol:** Origin ARM (`origin-arm`) · Yield · Ethereum, Sonic
- **DefiLlama:** https://defillama.com/protocol/origin-arm
- **PRIORITY 29.59**  =  LIKELIHOOD 49.32 × ACTIONABILITY 60.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 12.42/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $13,233,505 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.
    - Deployed source (`MultiAssetARM` @ 0xe0dba0ef…(ethereum), `OriginARM` @ 0x9a2be51e…(ethereum)): prerequisites matched: caller_named_asset_no_registry_check; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): value_fn_moves_caller_named_asset=yes
    - deployed source read for MultiAssetARM@0xe0dba0ef…(ethereum), OriginARM@0x9a2be51e…(ethereum); indicators matched: caller_named_asset_no_registry_check, value_fn_moves_caller_named_asset
- **Preconditions PRESENT / UNKNOWN:** src::caller_named_asset_no_registry_check, live_value_present, deployment_reachable_on_chain / src::token_hook_credits_without_sender_check
- **Guards searched / found:** asset_registry_check_present / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Every identifier derived or verified against the factory/registry (kills the pair); Routing restricted to an immutable venue allowlist
- **Where to start:** On a fork, create a fake pool/mint and pass it to every identifier-accepting entrypoint; all must revert.
- **Evidence:** `protocols/deep_screened.jsonl#origin-arm|ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`, `protocols/onchain_probes.json#origin-arm`
- **Disclosure:** https://www.originprotocol.com/arm · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.originprotocol.com/security-and-risk/audits

### 140. PyreSwap  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 140
- **Protocol:** PyreSwap (`pyreswap`) · Dexs · Binance, Avalanche, Fantom
- **DefiLlama:** https://defillama.com/protocol/pyreswap
- **PRIORITY 29.58**  =  LIKELIHOOD 29.58 × ACTIONABILITY 100.0%
    - likelihood = family evidence 26.25/50 (MATCH 52.5 × evidence weight 1.0) + learned attack surface 3.33/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $52,682 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 52.5 · CONFIDENCE 76.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
- **Broken invariant tested:** After deployment, no caller may (re)establish ownership, admin, or implementation wiring. Initialization state must be provably consumed.
    - Deployed source (`PyreswapFactory` @ 0x045d7208…(bsc)): prerequisites matched: initialize_without_modifier; no guard found
    - deployed source read for PyreswapFactory@0x045d7208…(bsc); indicators matched: initialize_without_modifier
- **Preconditions PRESENT / UNKNOWN:** src::initialize_without_modifier, live_value_or_approvals / upgradeable_architecture, initializer_flag_unset
- **Guards searched / found:** initializer_modifier_present, upgrade_timelocked / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Simulated re-initialization reverts (kills the pair); Contract is non-upgradeable and holds no approvals
- **Where to start:** Read the initialization slot on every live proxy/facet and simulate re-initialization from an unprivileged address; it must revert.
- **Evidence:** `protocols/deep_screened.jsonl#pyreswap|UPGRADE-INITIALIZER-REACHABLE-LIVE`, `protocols/onchain_probes.json#pyreswap`
- **Disclosure:** https://pyreswap.finance/ · no audit link listed

### 141. Native Credit Pool  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 141
- **Protocol:** Native Credit Pool (`native-credit-pool`) · Lending · Ethereum, Binance, Morph, Arbitrum, Base, Robinhood Chain …
- **DefiLlama:** https://defillama.com/protocol/native-credit-pool
- **PRIORITY 29.52**  =  LIKELIHOOD 49.2 × ACTIONABILITY 60.0%
    - likelihood = family evidence 30.0/50 (MATCH 60 × evidence weight 1.0) + learned attack surface 19.2/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $24,574,977 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 60 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `unverified_implementation` — raises likelihood, measured lift ×2.007 (weight +0.70)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`CreditVault` @ 0xe3D41d19…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for CreditVault@0xe3D41d19…(ethereum); indicators matched: route_output_not_bound
    - 1 implementation(s) behind a proxy are NOT verified on the explorer: implementation identity unresolved, score capped at 60
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#native-credit-pool|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#native-credit-pool`
- **Disclosure:** https://native.org · no audit link listed

### 142. Extra Finance Vaults  —  `ACC-DONATION-UNACCOUNTED-BALANCE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 142
- **Protocol:** Extra Finance Vaults (`extra-finance-vaults`) · Onchain Capital Allocator · Base
- **DefiLlama:** https://defillama.com/protocol/extra-finance-vaults
- **PRIORITY 28.62**  =  LIKELIHOOD 33.67 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 1.77/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,007,761 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A share price, exchange rate or totalAssets must be a function of value the protocol accounted for on entry. Reading a raw balance makes any direct transfer into the accounting boundary an unpriced increase in every holder's claim.
    - Deployed source (`MetaMorphoV1_1` @ 0x23479229…(base), `MetaMorphoV1_1` @ 0x5A320998…(base)): prerequisites matched: totalAssets_reads_balanceOf; no guard found
    - deployed source read for MetaMorphoV1_1@0x23479229…(base), MetaMorphoV1_1@0x5A320998…(base); indicators matched: totalAssets_reads_balanceOf
- **Preconditions PRESENT / UNKNOWN:** src::totalAssets_reads_balanceOf, unprivileged_inbound_transfer_possible, live_value_exposed / src::getCashPrior_balanceOf
- **Guards searched / found:** internal_cash_counter / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** totalAssets derived from an internal counter, not balanceOf (kills the pair); Rate is monotonic and rate-limited per block; Inbound transfers to the accounting boundary are rejected or swept to a reserve
- **Where to start:** On a fork, transfer an arbitrary amount of each counted asset directly into every accounting boundary; the share price, exchange rate and derived borrow power must not change.
- **Evidence:** `protocols/deep_screened.jsonl#extra-finance-vaults|ACC-DONATION-UNACCOUNTED-BALANCE`, `protocols/onchain_probes.json#extra-finance-vaults`
- **Disclosure:** https://app.extrafi.io/ · no audit link listed

### 143. Kasu  —  `ACC-DUPLICATE-ID-ACCUMULATION`

- **Rank (Ranking A — priority (likelihood × actionability)):** 143
- **Protocol:** Kasu (`kasu`) · RWA Lending · Base, XDC, Plume Mainnet
- **DefiLlama:** https://defillama.com/protocol/kasu
- **PRIORITY 28.61**  =  LIKELIHOOD 47.68 × ACTIONABILITY 60.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 15.78/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $11,276,942 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
- **Broken invariant tested:** An entitlement attached to an identifier may be counted at most once per period. A caller-supplied ID list must be deduplicated, or each ID's claim state consumed before the next read.
    - Deployed source (`KasuPoolExternalTVL` @ 0xe477a800…(base)): prerequisites matched: id_array_loop_without_dedup; no guard found
    - deployed source read for KasuPoolExternalTVL@0xe477a800…(base); indicators matched: id_array_loop_without_dedup
- **Preconditions PRESENT / UNKNOWN:** src::id_array_loop_without_dedup, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Consumed marker written inside the loop (kills the pair); IDs required strictly increasing
- **Where to start:** On a fork, call the batch function with one ID repeated k times; payout must equal the single-ID payout.
- **Evidence:** `protocols/deep_screened.jsonl#kasu|ACC-DUPLICATE-ID-ACCUMULATION`, `protocols/onchain_probes.json#kasu`
- **Disclosure:** https://kasu.finance/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/Kasu-Finance/security/tree/main/audits/Kasu_0xCommit.pdf, https://github.com/Kasu-Finance/security/tree/main/audits/Kasu_ChainSecurity.pdf

### 144. Solv RWA  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 144
- **Protocol:** Solv RWA (`solv-rwa`) · RWA · Binance, Mantle
- **DefiLlama:** https://defillama.com/protocol/solv-rwa
- **PRIORITY 28.36**  =  LIKELIHOOD 33.37 × ACTIONABILITY 85.0%
    - likelihood = family evidence 26.25/50 (MATCH 52.5 × evidence weight 1.0) + learned attack surface 7.12/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $8,864,405 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 52.5 · CONFIDENCE 70.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** After deployment, no caller may (re)establish ownership, admin, or implementation wiring. Initialization state must be provably consumed.
    - Deployed source (`VestingPool` @ 0x256f2d67…(bsc)): prerequisites matched: initialize_without_modifier; no guard found
    - deployed source read for VestingPool@0x256f2d67…(bsc); indicators matched: initialize_without_modifier
- **Preconditions PRESENT / UNKNOWN:** src::initialize_without_modifier, live_value_or_approvals / upgradeable_architecture, initializer_flag_unset
- **Guards searched / found:** initializer_modifier_present, upgrade_timelocked / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Simulated re-initialization reverts (kills the pair); Contract is non-upgradeable and holds no approvals
- **Where to start:** Read the initialization slot on every live proxy/facet and simulate re-initialization from an unprivileged address; it must revert.
- **Evidence:** `protocols/deep_screened.jsonl#solv-rwa|UPGRADE-INITIALIZER-REACHABLE-LIVE`, `protocols/onchain_probes.json#solv-rwa`
- **Disclosure:** https://solv.finance/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/solv-finance/Audit

### 145. Block Analitica  —  `ACC-NAV-SHAREPRICE-MANIPULABLE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 145
- **Protocol:** Block Analitica (`block-analitica`) · Risk Curators · Base, Ethereum, Arbitrum, Sonic
- **DefiLlama:** https://defillama.com/protocol/block-analitica
- **PRIORITY 28.09**  =  LIKELIHOOD 46.82 × ACTIONABILITY 60.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 14.92/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $19,175,855 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
- **Broken invariant tested:** totalAssets() must equal value the vault could actually realise now. Any component valued at book, at a manipulable rate, or after economic impairment lets a redeemer convert other depositors' claims into their own.
    - Deployed source (`HarborCommand` @ 0x09eb323d…(base), `MetaMorpho` @ 0x543257eF…(base)): prerequisites matched: totalAssets_reads_balanceOf; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): totalAssets_defined=yes
    - deployed source read for HarborCommand@0x09eb323d…(base), MetaMorpho@0x543257eF…(base); indicators matched: totalAssets_reads_balanceOf, totalAssets_defined
    - 3 live contract(s) answer totalAssets()
- **Preconditions PRESENT / UNKNOWN:** src::totalAssets_reads_balanceOf, erc4626_style_totalAssets_live, live_pooled_depositor_value / multi_component_totalAssets
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Share price rate-limited per block (kills same-transaction extraction); Single-asset vault with no external valuation; Withdrawals queued with a delay and priced at settlement
- **Where to start:** On a fork, for each component, force its valuation to zero and to 10x; the vault's mint/redeem must revert or be bounded, never transfer more than the depositor's pro-rata realisable share.
- **Evidence:** `protocols/deep_screened.jsonl#block-analitica|ACC-NAV-SHAREPRICE-MANIPULABLE`, `protocols/onchain_probes.json#block-analitica`
- **Disclosure:** https://blockanalitica.com/ · no audit link listed

### 146. MatrixDock STBT  —  `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 146
- **Protocol:** MatrixDock STBT (`matrixdock-stbt`) · RWA · Ethereum
- **DefiLlama:** https://defillama.com/protocol/matrixdock-stbt
- **PRIORITY 27.82**  =  LIKELIHOOD 46.37 × ACTIONABILITY 60.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 9.47/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $23,862,626 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.
    - Deployed source (`STBTv2` @ 0xe7efc506…(ethereum)): prerequisites matched: caller_named_asset_no_registry_check; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): value_fn_moves_caller_named_asset=yes
    - deployed source read for STBTv2@0xe7efc506…(ethereum); indicators matched: caller_named_asset_no_registry_check, value_fn_moves_caller_named_asset
- **Preconditions PRESENT / UNKNOWN:** src::caller_named_asset_no_registry_check, live_value_present, deployment_reachable_on_chain / src::token_hook_credits_without_sender_check
- **Guards searched / found:** asset_registry_check_present / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Every identifier derived or verified against the factory/registry (kills the pair); Routing restricted to an immutable venue allowlist
- **Where to start:** On a fork, create a fake pool/mint and pass it to every identifier-accepting entrypoint; all must revert.
- **Evidence:** `protocols/deep_screened.jsonl#matrixdock-stbt|ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`, `protocols/onchain_probes.json#matrixdock-stbt`
- **Disclosure:** https://www.matrixdock.com/home · no audit link listed

### 147. Switcheo Finance  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 147
- **Protocol:** Switcheo Finance (`switcheo-finance`) · Dexs · Ethereum
- **DefiLlama:** https://defillama.com/protocol/switcheo-finance
- **PRIORITY 27.78**  =  LIKELIHOOD 43.55 × ACTIONABILITY 63.8%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 11.65/50
    - actionability: mid-band: a team of this size will usually take an outside report; no public disclosure channel listed
- **Value at risk:** $1,323,041 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#switcheo-finance|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#switcheo-finance`
- **Disclosure:** not listed · no audit link listed

### 148. MegaETH Bridge  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 148
- **Protocol:** MegaETH Bridge (`megaeth-bridge`) · Canonical Bridge · Ethereum
- **DefiLlama:** https://defillama.com/protocol/megaeth-bridge
- **PRIORITY 27.46**  =  LIKELIHOOD 45.77 × ACTIONABILITY 60.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 13.87/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $10,276,318 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
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
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#megaeth-bridge|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#megaeth-bridge`
- **Disclosure:** https://www.megaeth.com/ · no audit link listed

### 149. Goose  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 149
- **Protocol:** Goose (`goose`) · CeDeFi · Binance, Op_Bnb, Arbitrum, Ethereum
- **DefiLlama:** https://defillama.com/protocol/goose
- **PRIORITY 27.37**  =  LIKELIHOOD 45.62 × ACTIONABILITY 60.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 13.72/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $12,809,163 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`USDVault` @ 0x0874F961…(arbitrum)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for USDVault@0x0874F961…(arbitrum); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#goose|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#goose`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://www.goose.farm/CERTIK_Golden_Goose_Report.pdf

### 150. Fuel Bridge  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 150
- **Protocol:** Fuel Bridge (`fuel-bridge`) · Bridge · Ethereum
- **DefiLlama:** https://defillama.com/protocol/fuel-bridge
- **PRIORITY 27.09**  =  LIKELIHOOD 45.15 × ACTIONABILITY 60.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 13.25/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $10,584,746 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#fuel-bridge|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#fuel-bridge`
- **Disclosure:** https://app.fuel.network/bridge · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/FuelLabs/audits/blob/master/fuel-audit-september-2024(Diffs%20on%20the%20Bridge%20and%20State%20Contracts)(Public).pdf

### 151. Jaypeggers  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 151
- **Protocol:** Jaypeggers (`jaypeggers`) · Yield · Ethereum
- **DefiLlama:** https://defillama.com/protocol/jaypeggers
- **PRIORITY 27.08**  =  LIKELIHOOD 36.1 × ACTIONABILITY 75.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 4.2/50
    - actionability: small enough to be unwatched, large enough to matter; no public disclosure channel listed
- **Value at risk:** $189,209 · **Band:** `IN_BAND`
- **Previously hacked:** 2022-12-29 for $18,500 [Reentrancy]
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `KNOWN_ISSUE_DEPLOYMENT_STATUS_UNKNOWN` — DefiLlama's hacks dataset records 1 prior on-chain incident(s) on this protocol, most recently 2022-12-29 for $18,500 [Reentrancy]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#jaypeggers|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#jaypeggers`
- **Disclosure:** not listed · no audit link listed

### 152. Syntetika  —  `ACC-NAV-SHAREPRICE-MANIPULABLE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 152
- **Protocol:** Syntetika (`syntetika`) · Risk Curators · Base
- **DefiLlama:** https://defillama.com/protocol/syntetika
- **PRIORITY 26.91**  =  LIKELIHOOD 44.85 × ACTIONABILITY 60.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 12.95/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $11,308,675 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `owner_is_eoa` — raises likelihood, measured lift ×1.729 (weight +0.55)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** totalAssets() must equal value the vault could actually realise now. Any component valued at book, at a manipulable rate, or after economic impairment lets a redeemer convert other depositors' claims into their own.
    - Deployed source (`ArcisVault` @ 0x00325d9d…(base), `ReturnFinanceCompoundV3USDCVault` @ 0x0271A46c…(base)): prerequisites matched: totalAssets_reads_balanceOf; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): totalAssets_defined=yes
    - deployed source read for ArcisVault@0x00325d9d…(base), ReturnFinanceCompoundV3USDCVault@0x0271A46c…(base); indicators matched: totalAssets_reads_balanceOf, totalAssets_defined
    - 2 live contract(s) answer totalAssets()
- **Preconditions PRESENT / UNKNOWN:** src::totalAssets_reads_balanceOf, erc4626_style_totalAssets_live, live_pooled_depositor_value / multi_component_totalAssets
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Share price rate-limited per block (kills same-transaction extraction); Single-asset vault with no external valuation; Withdrawals queued with a delay and priced at settlement
- **Where to start:** On a fork, for each component, force its valuation to zero and to 10x; the vault's mint/redeem must revert or be bounded, never transfer more than the depositor's pro-rata realisable share.
- **Evidence:** `protocols/deep_screened.jsonl#syntetika|ACC-NAV-SHAREPRICE-MANIPULABLE`, `protocols/onchain_probes.json#syntetika`
- **Disclosure:** https://syntetika.io/ · no audit link listed

### 153. Blur Bids  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 153
- **Protocol:** Blur Bids (`blur-bids`) · NFT Marketplace · Ethereum, Blast
- **DefiLlama:** https://defillama.com/protocol/blur-bids
- **PRIORITY 26.68**  =  LIKELIHOOD 44.47 × ACTIONABILITY 60.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 12.57/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $17,476,884 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#blur-bids|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#blur-bids`
- **Disclosure:** https://blur.io/ · no audit link listed

### 154. SX Rollup Bridge  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 154
- **Protocol:** SX Rollup Bridge (`sx-rollup-bridge`) · Canonical Bridge · Ethereum
- **DefiLlama:** https://defillama.com/protocol/sx-rollup-bridge
- **PRIORITY 25.84**  =  LIKELIHOOD 43.07 × ACTIONABILITY 60.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 11.17/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $11,196,433 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `BlurPool` @ 0x01a65602…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), BlurPool@0x01a65602…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#sx-rollup-bridge|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#sx-rollup-bridge`
- **Disclosure:** https://sx.bet/wallet/bridge · no audit link listed

### 155. Arbitrum Nova Bridge  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 155
- **Protocol:** Arbitrum Nova Bridge (`arbitrum-nova-bridge`) · Canonical Bridge · Ethereum
- **DefiLlama:** https://defillama.com/protocol/arbitrum-nova-bridge
- **PRIORITY 24.82**  =  LIKELIHOOD 41.37 × ACTIONABILITY 60.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 9.47/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $14,823,067 · **Band:** `IN_BAND`
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
- **Evidence:** `protocols/deep_screened.jsonl#arbitrum-nova-bridge|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#arbitrum-nova-bridge`
- **Disclosure:** https://portal.arbitrum.io/bridge?l2ChainId=42170 · no audit link listed

### 156. PoWH3D  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 156
- **Protocol:** PoWH3D (`powh3d`) · Farm · Ethereum
- **DefiLlama:** https://defillama.com/protocol/powh3d
- **PRIORITY 24.45**  =  LIKELIHOOD 38.33 × ACTIONABILITY 63.8%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 6.43/50
    - actionability: mid-band: a team of this size will usually take an outside report; no public disclosure channel listed
- **Value at risk:** $5,022,089 · **Band:** `IN_BAND`
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
- **Evidence:** `protocols/deep_screened.jsonl#powh3d|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#powh3d`
- **Disclosure:** not listed · no audit link listed

### 157. Wrapped  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 157
- **Protocol:** Wrapped (`wrapped`) · Bridge · Ripple, Celo, Ethereum
- **DefiLlama:** https://defillama.com/protocol/wrapped
- **PRIORITY 23.84**  =  LIKELIHOOD 39.73 × ACTIONABILITY 60.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 7.83/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $26,935,883 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
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
- **Evidence:** `protocols/deep_screened.jsonl#wrapped|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#wrapped`
- **Disclosure:** https://wrapped.com · no audit link listed

### 158. Belt Finance  —  `ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 158
- **Protocol:** Belt Finance (`belt-finance`) · Yield · Binance, Klaytn, Heco
- **DefiLlama:** https://defillama.com/protocol/belt-finance
- **PRIORITY 23.48**  =  LIKELIHOOD 39.13 × ACTIONABILITY 60.0%
    - likelihood = family evidence 26.25/50 (MATCH 52.5 × evidence weight 1.0) + learned attack surface 12.88/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $13,098,699 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 52.5 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `owner_is_eoa` — raises likelihood, measured lift ×1.729 (weight +0.55)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A vault share rate is an accounting quantity of another protocol, not a market price. Using it as a feed imports every way that vault's rate can be moved, including donation inflation and same-transaction redemption effects.
    - Deployed source (`NewBeltView` @ 0xB543248F…(bsc)): prerequisites matched: rate_used_as_price; no guard found
    - deployed source read for NewBeltView@0xB543248F…(bsc); indicators matched: rate_used_as_price
    - only one oracle (or none) is declared in DefiLlama metadata; this is a prioritisation signal about disclosure, not evidence that no cross-source deviation bound exists in code
    - declared oracles: none declared
- **Preconditions PRESENT / UNKNOWN:** src::rate_used_as_price, live_positions_exposed / value_decision_reads_configured_feed, feed_selection_is_configuration
- **Guards searched / found:** deviation_bound_vs_independent_source / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `EOA_SINGLE_KEY`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Growth-capped rate adapter in the deployed oracle (kills the pair); Wrapper's own rate is monotonic and rate-limited; Collateral priced by an independent market feed instead
- **Where to start:** On a fork, donate to and cycle the underlying vault; assert the lending market's reported collateral price moves no more than the configured cap.
- **Evidence:** `protocols/deep_screened.jsonl#belt-finance|ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE`, `protocols/onchain_probes.json#belt-finance`
- **Disclosure:** https://belt.fi/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/BeltFi/belt-contract/tree/main/audit

### 159. Taiko Bridge  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 159
- **Protocol:** Taiko Bridge (`taiko-bridge`) · Canonical Bridge · Ethereum
- **DefiLlama:** https://defillama.com/protocol/taiko-bridge
- **PRIORITY 23.48**  =  LIKELIHOOD 39.13 × ACTIONABILITY 60.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 7.23/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $11,647,101 · **Band:** `IN_BAND`
- **Previously hacked:** 2026-06-21 for $1,700,000 [Forged Proof]
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `KNOWN_ISSUE_DEPLOYMENT_STATUS_UNKNOWN` — DefiLlama's hacks dataset records 1 prior on-chain incident(s) on this protocol, most recently 2026-06-21 for $1,700,000 [Forged Proof]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#taiko-bridge|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#taiko-bridge`
- **Disclosure:** https://bridge.taiko.xyz/ · no audit link listed

### 160. TokenStore  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 160
- **Protocol:** TokenStore (`tokenstore`) · Dexs · Ethereum
- **DefiLlama:** https://defillama.com/protocol/tokenstore
- **PRIORITY 23.03**  =  LIKELIHOOD 36.1 × ACTIONABILITY 63.8%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 4.2/50
    - actionability: mid-band: a team of this size will usually take an outside report; no public disclosure channel listed
- **Value at risk:** $1,536,041 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
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
- **Evidence:** `protocols/deep_screened.jsonl#tokenstore|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#tokenstore`
- **Disclosure:** not listed · no audit link listed

### 161. EtherFlip  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 161
- **Protocol:** EtherFlip (`etherflip`) · Luck Games · Ethereum
- **DefiLlama:** https://defillama.com/protocol/etherflip
- **PRIORITY 23.03**  =  LIKELIHOOD 36.1 × ACTIONABILITY 63.8%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 4.2/50
    - actionability: mid-band: a team of this size will usually take an outside report; no public disclosure channel listed
- **Value at risk:** $1,827,849 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#etherflip|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#etherflip`
- **Disclosure:** not listed · no audit link listed

### 162. Paradex Bridge  —  `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

- **Rank (Ranking A — priority (likelihood × actionability)):** 162
- **Protocol:** Paradex Bridge (`paradex-bridge`) · Bridge · Ethereum
- **DefiLlama:** https://defillama.com/protocol/paradex-bridge
- **PRIORITY 21.66**  =  LIKELIHOOD 36.1 × ACTIONABILITY 60.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 4.2/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $17,867,715 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): prerequisites matched: route_output_not_bound; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), ZAMM@0x00000000…(ethereum); indicators matched: route_output_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::route_output_not_bound, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Where to start:** On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.
- **Evidence:** `protocols/deep_screened.jsonl#paradex-bridge|QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`, `protocols/onchain_probes.json#paradex-bridge`
- **Disclosure:** https://app.paradex.trade/r/defillama · no audit link listed

### 163. Moonwell Vaults  —  `BRIDGE-MESSAGE-NOT-BOUND-TO-SOURCE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 163
- **Protocol:** Moonwell Vaults (`moonwell-vaults`) · Onchain Capital Allocator · Base, Optimism
- **DefiLlama:** https://defillama.com/protocol/moonwell-vaults
- **PRIORITY 20.29**  =  LIKELIHOOD 33.82 × ACTIONABILITY 60.0%
    - likelihood = family evidence 26.25/50 (MATCH 52.5 × evidence weight 1.0) + learned attack surface 7.57/50
    - actionability: upper band: may already retain reviewers
- **Value at risk:** $18,198,287 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 52.5 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
- **Broken invariant tested:** A release, mint or payout on the destination domain must be authorised only by a proof that binds, simultaneously: the source chain identity, the source channel/route, the exact asset, the exact amount, the recipient, and a nonce that is consumed exactly once. Verifying that a message is well-formed or correctly signed is not the same as verifying that it corresponds to a real deposit of equal value.
    - Deployed source (`TemporalGovernor` @ 0x8b621804…(base)): prerequisites matched: xdomain_source_not_bound; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): xdomain_nonce_not_consumed=no
    - deployed source read for TemporalGovernor@0x8b621804…(base); indicators matched: xdomain_source_not_bound
- **Preconditions PRESENT / UNKNOWN:** src::xdomain_source_not_bound, live_value_present, deployment_reachable_on_chain / src::xdomain_entrypoint_present, src::xdomain_no_endpoint_check, src::token_hook_credits_without_sender_check
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Destination mint requires a Merkle/zk proof against a source state root that itself commits to the amount; Reserve reconciliation is enforced on-chain (mint reverts if supply would exceed escrow); Bridge is one-way with no destination-side release
- **Where to start:** On a pinned fork of the destination chain, no sequence of destination-side calls may increase redeemable value without a matching, previously unconsumed source commitment of equal value.
- **Evidence:** `protocols/deep_screened.jsonl#moonwell-vaults|BRIDGE-MESSAGE-NOT-BOUND-TO-SOURCE`, `protocols/onchain_probes.json#moonwell-vaults`
- **Disclosure:** https://moonwell.fi/vaults · no audit link listed
