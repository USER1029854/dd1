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
| Candidates | 60 |
| Previously hacked | 3 |
| Repeat victims (2+ recorded hacks) | 1 |
| Median value at risk | $345,413 |
| Total value at risk | $41,079,177 |
| At L4 guard review | 38 |
| Previously delivered (withheld from this list) | 316 |

### Every protocol here is one you have not been given before

A candidate list is a queue of work, not a leaderboard. **316 protocols that survive screening were withheld from this run because earlier runs already handed them over** across 7 previous deliveries. They are not resolved and not ruled out — they were already given to you, so repeating them would hand you no new work.

| Previous delivery | Protocols handed over |
|---|---:|
| `7d49c12` — Add six-month DeFi incident intelligence and DefiLlama audit pri | 24 |
| `ccb5273` — Expand the screen to a $50k floor with a condition layer and dep | 49 |
| `3bc30a7` — Re-target the screen at what actually gets hacked, in a reviewab | 72 |
| `2ce88d1` — Validate the ranking model and measure custody exposure separate | 111 |
| `5a3468f` — Remove leftovers from earlier iterations of this run | 111 |
| `7e319ee` — Extend beyond EVM: verify Maya at source, kill the THORChain lea | 108 |
| `1ad898f` — Never hand over the same protocol twice | 130 |

The full ledger is `protocols/delivered_ledger.json`, reconstructed from git history rather than from anything remembered between runs. Every withheld protocol still appears in `candidates_all.csv` with `previously_delivered=YES` and the run that delivered it, so nothing is hidden — it is only kept out of the queue.

<details><summary>The 316 withheld protocols</summary>

`88mph`, `8lends`, `aave-v1`, `aave-v3`, `aavegotchi`, `abracadabra-spell`, `abstradex`, `accountable`, `accumulated-finance-liquid-staking`, `across`, `adi-bridge`, `aerodrome-ignition`, `agave`, `ajna-v1`, `ajna-v2`, `aloe`, `ammalgam-dlex`, `angle`, `ankr`, `ante-finance`, `antfarm-finance`, `anzen-v2`, `aperocket`, `apostro`, `arbinyan`, `arcade.xyz`, `arch`, `asseto-cash+`, `astaria-v2`, `asymmetry-usdaf`, `aura`, `axelar-cross-chain`, `b.protocol`, `b.protocol-curator`, `babydoge-bridge`, `badger-dao`, `balancer-v2`, `balancer-v3`, `bancor-v2.1`, `base-dollar`, `basedbid`, `bearnfi`, `bella-protocol`, `bifi`, `bima-cdp`, `bitstable-finance`, `blackwing`, `bond-protocol`, `boringdao`, `bridge-mutual`, `bunni-v2`, `bunny`, `burgerswap`, `cache.gold`, `cakepie`, `capyfi`, `caviar-v1`, `cega-v1`, `charm-finance-v1`, `clearpool-lending`, `clipper`, `conic-finance`, `contango-v1`, `convex-finance`, `cook-finance`, `cover-protocol`, `cream-lending`, `credit-coop`, `cronos-zkevm-bridge`, `crosschain-bridge`, `csigma-finance`, `cub-finance`, `curve-dex`, `curve-llamalend`, `cytonic-airdrop-campaign`, `ddex`, `de1`, `debridge`, `defibox`, `defil`, `deri-protocol`, `derive-v1`, `dforce-lending`, `domani-protocol`, `dooar-v2`, `dopple-finance`, `dsf.finance`, `dtrinity-dlend`, `elk`, `enosys-bridge`, `equilibria`, `ether.fi-liquid`, `everything`, `ezmoney`, `finext-finance`, `finnexus`, `flux-finance`, `flying-tulip-lend`, `frax-fpi`, `fuji-v1`, `fungify`, `gaib`, `gammaswap-open-interest`, `gauntlet`, `gearbox`, `geyser`, `gnosis-protocol-v1`, `goldsand-by-inshallah`, `goplus-locker-v2`, `granary-finance`, `gravita-protocol`, `grizzlyfi-hives`, `gro`, `guru-network-classic`, `gyroscope-protocol`, `harvest-finance`, `hashflow`, `hop-protocol`, `horizon-protocol`, `hundred-finance`, `hunny-finance`, `hydt-protocol`, `ichi`, `ideamarket`, `idle`, `impermax-v2`, `impossible`, `infinite-trading-protocol`, `insurace`, `international-meme-fund-v2`, `ipor-derivatives`, `iron-bank`, `itrust-finance`, `iziswap`, `izumi-liquidbox`, `jetfuel-finance`, `joe-dex`, `joe-v2`, `juicebox-v3`, `kine-finance`, `kokonut-swap`, `kromatika`, `krystal-community-vault`, `kyberswap-classic`, `kyberswap-elastic`, `landshare`, `landx-finance`, `lendflare`, `likwid`, `lista-cdp`, `listapie`, `liveart`, `lixir-finance`, `lockon`, `loop`, `lucidly-finance`, `lybra-v1`, `magic-eden`, `makina`, `maverick-v1`, `mcdex`, `mellow-yield`, `mero`, `mesher`, `meter-passport`, `midas-capital`, `mim-swap`, `mochifi`, `moneyfi`, `monolith-market`, `moonwell-lending`, `morpheusai`, `morpho-optimizer-aavev2`, `mortgagefi`, `mountain-protocol`, `muffin`, `multichain`, `myx-finance`, `nested`, `nftx`, `niob-finance`, `nomad`, `nomiswap`, `nucleus`, `olive-network`, `openeden-prism`, `openleverage`, `opium`, `orbit-bridge`, `orderly-bridge`, `ordernchaos`, `oreoswap`, `orion-pools`, `otsea`, `overtime`, `padswap`, `peapods-finance`, `pell-network`, `pepeteam-bridge`, `percent-finance`, `picwe`, `piku-finance`, `planet-farm`, `pooltogether-v3`, `pooltogether-v4`, `pooltogether-v5`, `prdt`, `premia-v2`, `preon-finance`, `printr`, `prismalst`, `privacy-cash`, `privacy-pools`, `pstake-lsd`, `qidao`, `radiant-v2`, `radioshack`, `rari-capital`, `reservoir-protocol`, `resonate-finance`, `revest-finance`, `rubicon`, `sablier-legacy`, `saddle-finance`, `saffron-vaults`, `satlayer`, `sato`, `savvy`, `sectorone-dlmm`, `segment-finance`, `sentora`, `set-protocol`, `shift-protocol`, `shimmerbridge`, `sigma-money`, `silo-v2`, `silo-v3`, `single-finance`, `singular-farm`, `singularitydao`, `sir`, `smardex-amm`, `smartcredit`, `snowswap`, `sofa.org`, `solo-top`, `sparklend`, `spectra-metavaults-outside-v2`, `spectra-v1`, `sperax-usd`, `stability`, `stabull-finance`, `stafi`, `stake-dao`, `stargate-v1`, `steakhut-liquidity`, `steer-protocol`, `stonedefi`, `strata-season-0`, `sturdy-v2`, `sumer.money`, `sunx-bridge`, `swaap-maker-v2`, `swapr-v2`, `swell-earn`, `synapse-cross-chain-bridge`, `synfutures-v1`, `tarot`, `tau-labs`, `termfinance-vaults`, `terminal-finance-pre-deposits`, `tetu-earn`, `the-idols`, `thedeep`, `theoriq-alphavault-eth`, `threshold-thusd`, `thruster-v2`, `tidaldex`, `tranchess-yield`, `treedefi`, `trevee-earn`, `twindex`, `ufarm-digital`, `unagii`, `unitus`, `unsheth`, `unslashed`, `uwu-lend`, `valuedefi`, `varen`, `vault-street-primeusd`, `vaultcraft`, `velvet-v2`, `velvet-v3`, `venombridge`, `venus-core-pool`, `wasabi-perps`, `wasabix`, `wavesbridge`, `wepiggy`, `wing-finance`, `wombex-finance`, `wompie`, `xgld`, `xtoken`, `xwin-finance`, `yala`, `yaxis`, `yearn-finance`, `yield-millionaire`, `yield-protocol`, `yieldflow-yield-farming`, `yieldnest`, `yieldwolf`, `zero-network`, `zunami-protocol`

</details>

### Repeat victims in this list

Whatever allowed a second incident has not necessarily been removed. These are the highest-conviction entries in the set.

| Protocol | Hacks | Family | Priority | At risk |
|---|---:|---|---:|---:|
| [Indexed Finance](https://defillama.com/protocol/indexed-finance) | 2 | `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY` | 46.45 | $120,981 |

### Diversified shortlist — top 3 per family

| # | Protocol | Family | Priority | Likelihood | At risk | Evidence |
|---:|---|---|---:|---:|---:|---|
| 1 | [Yam Finance](https://defillama.com/protocol/yam-finance) | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | 62.87 | 62.87 | $237,414 | `L4_GUARD_REVIEW` |
| 2 | [Mummy Finance](https://defillama.com/protocol/mummy-finance) | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | 60.6 | 60.6 | $54,685 | `L4_GUARD_REVIEW` |
| 3 | [Keep3r Network](https://defillama.com/protocol/keep3r-network) | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | 58.69 | 69.05 | $3,186,925 | `L4_GUARD_REVIEW` |
| 4 | [Sommelier](https://defillama.com/protocol/sommelier) | `SIG-VERIFIER-DEFEATABLE` | 56.3 | 56.3 | $906,670 | `L4_GUARD_REVIEW` |
| 5 | [Clovis](https://defillama.com/protocol/clovis) | `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY` | 52.5 | 52.5 | $234,245 | `L3_STATE` |
| 6 | [Tokenlon AMM](https://defillama.com/protocol/tokenlon-amm) | `SIG-VERIFIER-DEFEATABLE` | 51.85 | 51.85 | $588,461 | `L4_GUARD_REVIEW` |
| 7 | [JPEG'd](https://defillama.com/protocol/jpegd) | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | 51.77 | 51.77 | $564,479 | `L4_GUARD_REVIEW` |
| 8 | [OnX Finance](https://defillama.com/protocol/onx-finance) | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | 51.32 | 51.32 | $305,022 | `L4_GUARD_REVIEW` |
| 9 | [Theoriq Gold Vault](https://defillama.com/protocol/theoriq-gold-vault) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 50.85 | 50.85 | $131,019 | `L4_GUARD_REVIEW` |
| 10 | [Cryptex V1](https://defillama.com/protocol/cryptex-v1) | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | 50.38 | 50.38 | $428,629 | `L4_GUARD_REVIEW` |
| 11 | [Sudoswap V1](https://defillama.com/protocol/sudoswap-v1) | `ACC-DUPLICATE-ID-ACCUMULATION` | 50.13 | 50.13 | $660,847 | `L4_GUARD_REVIEW` |
| 12 | [PEAKDEFI](https://defillama.com/protocol/peakdefi) | `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY` | 50.12 | 50.12 | $110,630 | `L3_STATE` |
| 13 | [CANA Holdings California Carbon Credits](https://defillama.com/protocol/cana-holdings-california-carbon-credits) | `SIG-VERIFIER-DEFEATABLE` | 49.83 | 49.83 | $893,977 | `L4_GUARD_REVIEW` |
| 14 | [Umami Finance](https://defillama.com/protocol/umami-finance) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 49.57 | 49.57 | $387,748 | `L4_GUARD_REVIEW` |
| 15 | [Tanken Capital](https://defillama.com/protocol/tanken-capital) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 49.22 | 49.22 | $85,381 | `L4_GUARD_REVIEW` |
| 16 | [Thesauros](https://defillama.com/protocol/thesauros) | `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY` | 48.68 | 48.68 | $51,215 | `L3_STATE` |
| 17 | [Alongside](https://defillama.com/protocol/alongside) | `ACC-CREDIT-NOT-RECEIVED` | 47.68 | 47.68 | $467,535 | `L4_GUARD_REVIEW` |
| 18 | [InsureDAO](https://defillama.com/protocol/insuredao) | `SECRET-EMBEDDED-IN-PUBLIC-CODE-AS-AUTH` | 47.6 | 47.6 | $123,685 | `L4_GUARD_REVIEW` |
| 19 | [Cozy V1](https://defillama.com/protocol/cozy-v1) | `AUTH-ZERO-ADDRESS-ACCEPTED` | 47.5 | 47.5 | $72,293 | `L4_GUARD_REVIEW` |
| 20 | [Mint Club V2](https://defillama.com/protocol/mint-club-v2) | `AUTH-ZERO-ADDRESS-ACCEPTED` | 47.32 | 47.32 | $697,219 | `L4_GUARD_REVIEW` |
| 21 | [DELV Yield](https://defillama.com/protocol/delv-yield) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 47.12 | 47.12 | $741,190 | `L4_GUARD_REVIEW` |
| 22 | [Dyson](https://defillama.com/protocol/dyson) | `AUTH-ZERO-ADDRESS-ACCEPTED` | 46.85 | 46.85 | $265,697 | `L4_GUARD_REVIEW` |
| 23 | [SuperReturn](https://defillama.com/protocol/superreturn) | `ACC-DONATION-UNACCOUNTED-BALANCE` | 46.05 | 46.05 | $94,461 | `L4_GUARD_REVIEW` |
| 24 | [Amphor](https://defillama.com/protocol/amphor) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 45.75 | 45.75 | $62,416 | `L4_GUARD_REVIEW` |
| 25 | [DFX V2](https://defillama.com/protocol/dfx-v2) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 45.72 | 45.72 | $84,226 | `L4_GUARD_REVIEW` |
| 26 | [Flying Tulip ftUSD](https://defillama.com/protocol/flying-tulip-ftusd) | `ACC-DUPLICATE-ID-ACCUMULATION` | 45.62 | 53.67 | $2,273,825 | `L4_GUARD_REVIEW` |
| 27 | [Jones DAO](https://defillama.com/protocol/jones-dao) | `ACC-DONATION-UNACCOUNTED-BALANCE` | 45.22 | 45.22 | $982,466 | `L4_GUARD_REVIEW` |
| 28 | [Sera](https://defillama.com/protocol/sera) | `AUTH-IDENTITY-SATISFIABLE-BY-ATTACKER-CONTRACT` | 44.83 | 44.83 | $152,113 | `L4_GUARD_REVIEW` |
| 29 | [MORE Vaults](https://defillama.com/protocol/more-vaults) | `ACC-DONATION-UNACCOUNTED-BALANCE` | 44.68 | 44.68 | $822,973 | `L4_GUARD_REVIEW` |
| 30 | [ZeroLend Lending](https://defillama.com/protocol/zerolend-lending) | `ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE` | 44.26 | 52.07 | $3,903,136 | `L3_STATE` |

---

### 1. Yam Finance  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 1
- **Protocol:** Yam Finance (`yam-finance`) · Synthetics · Ethereum
- **DefiLlama:** https://defillama.com/protocol/yam-finance
- **PRIORITY 62.87**  =  LIKELIHOOD 62.87 × ACTIONABILITY 100.0%
    - likelihood = family evidence 42.5/50 (MATCH 85.0 × evidence weight 1.0) + learned attack surface 20.37/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $237,414 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 85.0 · CONFIDENCE 84.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** After deployment, no caller may (re)establish ownership, admin, or implementation wiring. Initialization state must be provably consumed.
    - Deployed source (`YAMDelegate3` @ 0x27c5736b…(ethereum)): prerequisites matched: initialize_without_modifier; no guard found
    - deployed source read for YAMDelegate3@0x27c5736b…(ethereum); indicators matched: initialize_without_modifier
    - 1/1 live proxies read a zero ERC-7201 Initializable slot (inconclusive alone: older OZ versions store the flag elsewhere)
- **Preconditions PRESENT / UNKNOWN:** src::initialize_without_modifier, upgradeable_architecture, initializer_flag_unset, live_value_or_approvals / none
- **Guards searched / found:** initializer_modifier_present, upgrade_timelocked / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Simulated re-initialization reverts (kills the pair); Contract is non-upgradeable and holds no approvals
- **Where to start:** Read the initialization slot on every live proxy/facet and simulate re-initialization from an unprivileged address; it must revert.
- **Evidence:** `protocols/deep_screened.jsonl#yam-finance|UPGRADE-INITIALIZER-REACHABLE-LIVE`, `protocols/onchain_probes.json#yam-finance`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/yam-finance/audits

### 2. Mummy Finance  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 2
- **Protocol:** Mummy Finance (`mummy-finance`) · Derivatives · Optimism, Arbitrum, Fantom, Base
- **DefiLlama:** https://defillama.com/protocol/mummy-finance
- **PRIORITY 60.6**  =  LIKELIHOOD 60.6 × ACTIONABILITY 100.0%
    - likelihood = family evidence 37.5/50 (MATCH 75.0 × evidence weight 1.0) + learned attack surface 23.1/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $54,685 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 75.0 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
- **Broken invariant tested:** After deployment, no caller may (re)establish ownership, admin, or implementation wiring. Initialization state must be provably consumed.
    - Deployed source (`Reader` @ 0x04f23404…(arbitrum), `Vault` @ 0x304951d7…(arbitrum)): prerequisites matched: initialize_without_modifier; no guard found
    - deployed source read for Reader@0x04f23404…(arbitrum), Vault@0x304951d7…(arbitrum); indicators matched: initialize_without_modifier
    - 1/1 live proxies read a zero ERC-7201 Initializable slot (inconclusive alone: older OZ versions store the flag elsewhere)
    - 1 proxy/proxies expose a non-zero owner()
- **Preconditions PRESENT / UNKNOWN:** src::initialize_without_modifier, upgradeable_architecture, initializer_flag_unset, live_value_or_approvals / none
- **Guards searched / found:** initializer_modifier_present, upgrade_timelocked / upgrade_timelocked
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Simulated re-initialization reverts (kills the pair); Contract is non-upgradeable and holds no approvals
- **Where to start:** Read the initialization slot on every live proxy/facet and simulate re-initialization from an unprivileged address; it must revert.
- **Evidence:** `protocols/deep_screened.jsonl#mummy-finance|UPGRADE-INITIALIZER-REACHABLE-LIVE`, `protocols/onchain_probes.json#mummy-finance`
- **Disclosure:** https://www.mummy.finance · no audit link listed

### 3. Keep3r Network  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 3
- **Protocol:** Keep3r Network (`keep3r-network`) · Derivatives · Ethereum
- **DefiLlama:** https://defillama.com/protocol/keep3r-network
- **PRIORITY 58.69**  =  LIKELIHOOD 69.05 × ACTIONABILITY 85.0%
    - likelihood = family evidence 42.5/50 (MATCH 85.0 × evidence weight 1.0) + learned attack surface 26.55/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $3,186,925 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 85.0 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** After deployment, no caller may (re)establish ownership, admin, or implementation wiring. Initialization state must be provably consumed.
    - Deployed source (`CCollateralCapErc20Delegate` @ 0x7e8844ea…(ethereum), `Spell` @ 0x090185f2…(ethereum)): prerequisites matched: initialize_without_modifier; no guard found
    - deployed source read for CCollateralCapErc20Delegate@0x7e8844ea…(ethereum), Spell@0x090185f2…(ethereum); indicators matched: initialize_without_modifier
    - 1/1 live proxies read a zero ERC-7201 Initializable slot (inconclusive alone: older OZ versions store the flag elsewhere)
- **Preconditions PRESENT / UNKNOWN:** src::initialize_without_modifier, upgradeable_architecture, initializer_flag_unset, live_value_or_approvals / none
- **Guards searched / found:** initializer_modifier_present, upgrade_timelocked / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Simulated re-initialization reverts (kills the pair); Contract is non-upgradeable and holds no approvals
- **Where to start:** Read the initialization slot on every live proxy/facet and simulate re-initialization from an unprivileged address; it must revert.
- **Evidence:** `protocols/deep_screened.jsonl#keep3r-network|UPGRADE-INITIALIZER-REACHABLE-LIVE`, `protocols/onchain_probes.json#keep3r-network`
- **Disclosure:** https://keep3r.network · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/keep3r-network/keep3r.network/tree/master/audits

### 4. Cozy V1  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 4
- **Protocol:** Cozy V1 (`cozy-v1`) · Insurance · Ethereum
- **DefiLlama:** https://defillama.com/protocol/cozy-v1
- **PRIORITY 58.1**  =  LIKELIHOOD 58.1 × ACTIONABILITY 100.0%
    - likelihood = family evidence 42.5/50 (MATCH 85.0 × evidence weight 1.0) + learned attack surface 15.6/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $72,293 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 85.0 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `owner_is_eoa` — raises likelihood, measured lift ×1.729 (weight +0.55)
    - `version_sibling_legacy` — raises likelihood, measured lift ×1.699 (weight +0.53)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** After deployment, no caller may (re)establish ownership, admin, or implementation wiring. Initialization state must be provably consumed.
    - Conditions: `VERSION_SIBLING_LEGACY`
    - Deployed source (`CErc20Immutable` @ 0x004c0908…(ethereum), `TransparentUpgradeableProxy` @ 0x02451015…(ethereum)): prerequisites matched: initialize_without_modifier; no guard found
    - deployed source read for CErc20Immutable@0x004c0908…(ethereum), TransparentUpgradeableProxy@0x02451015…(ethereum); indicators matched: initialize_without_modifier
    - condition VERSION_SIBLING_LEGACY (PRECOND): Shares a parent protocol with a higher-version sibling while still holding value: the classic sibling-deployment-retains-the-old-version shape.
    - 1/1 live proxies read a zero ERC-7201 Initializable slot (inconclusive alone: older OZ versions store the flag elsewhere)
- **Preconditions PRESENT / UNKNOWN:** src::initialize_without_modifier, upgradeable_architecture, initializer_flag_unset, live_value_or_approvals / none
- **Guards searched / found:** initializer_modifier_present, upgrade_timelocked / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Simulated re-initialization reverts (kills the pair); Contract is non-upgradeable and holds no approvals
- **Where to start:** Read the initialization slot on every live proxy/facet and simulate re-initialization from an unprivileged address; it must revert.
- **Evidence:** `protocols/deep_screened.jsonl#cozy-v1|UPGRADE-INITIALIZER-REACHABLE-LIVE`, `protocols/onchain_probes.json#cozy-v1`
- **Disclosure:** https://www.cozy.finance · no audit link listed

### 5. Sommelier  —  `SIG-VERIFIER-DEFEATABLE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 5
- **Protocol:** Sommelier (`sommelier`) · Onchain Capital Allocator · Ethereum, Arbitrum, Optimism
- **DefiLlama:** https://defillama.com/protocol/sommelier
- **PRIORITY 56.3**  =  LIKELIHOOD 56.3 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 19.4/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $906,670 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
- **Broken invariant tested:** A verification routine must reject malformed, empty or zero-recovered signatures, and must never treat address(0) as a match.
    - Deployed source (`CellarWithOracleWithBalancerFlashLoansWithMultiAssetDepositWithNativeSupport` @ 0x1dffb366…(ethereum), `CellarWithOracleWithBalancerFlashLoans` @ 0x5195222f…(ethereum)): prerequisites matched: ecrecover_without_zero_check; no guard found
    - deployed source read for CellarWithOracleWithBalancerFlashLoansWithMultiAssetDepositWithNativeSupport@0x1dffb366…(ethereum), CellarWithOracleWithBalancerFlashLoans@0x5195222f…(ethereum); indicators matched: ecrecover_without_zero_check
- **Preconditions PRESENT / UNKNOWN:** src::ecrecover_without_zero_check, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** uses_oz_ecdsa / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** OZ ECDSA library in the deployed bytecode (kills the ecrecover-zero shape); Signer address immutable and non-zero
- **Where to start:** On a fork, submit r=0,s=0,v=27 and an empty signature to every signature-gated entrypoint; all must revert.
- **Evidence:** `protocols/deep_screened.jsonl#sommelier|SIG-VERIFIER-DEFEATABLE`, `protocols/onchain_probes.json#sommelier`
- **Disclosure:** https://somm.finance/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://somm.finance/audits, https://github.com/PeggyJV/cellar-contracts/tree/main/audits

### 6. Venus Isolated Pools  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 6
- **Protocol:** Venus Isolated Pools (`venus-isolated-pools`) · Lending · Binance, Ethereum, Arbitrum
- **DefiLlama:** https://defillama.com/protocol/venus-isolated-pools
- **PRIORITY 53.87**  =  LIKELIHOOD 63.38 × ACTIONABILITY 85.0%
    - likelihood = family evidence 42.5/50 (MATCH 85.0 × evidence weight 1.0) + learned attack surface 20.88/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,122,520 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 85.0 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** After deployment, no caller may (re)establish ownership, admin, or implementation wiring. Initialization state must be provably consumed.
    - Deployed source (`Unitroller` @ 0xfd36e2c2…(bsc)): prerequisites matched: initialize_without_modifier; no guard found
    - deployed source read for Unitroller@0xfd36e2c2…(bsc); indicators matched: initialize_without_modifier
    - 1/1 live proxies read a zero ERC-7201 Initializable slot (inconclusive alone: older OZ versions store the flag elsewhere)
    - 1 proxy/proxies expose a non-zero owner()
- **Preconditions PRESENT / UNKNOWN:** src::initialize_without_modifier, upgradeable_architecture, initializer_flag_unset, live_value_or_approvals / none
- **Guards searched / found:** initializer_modifier_present, upgrade_timelocked / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Simulated re-initialization reverts (kills the pair); Contract is non-upgradeable and holds no approvals
- **Where to start:** Read the initialization slot on every live proxy/facet and simulate re-initialization from an unprivileged address; it must revert.
- **Evidence:** `protocols/deep_screened.jsonl#venus-isolated-pools|UPGRADE-INITIALIZER-REACHABLE-LIVE`, `protocols/onchain_probes.json#venus-isolated-pools`
- **Disclosure:** https://app.venus.io/#/isolated-pools/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs-v4.venus.io/links/security-and-audits#isolated-pools

### 7. Clovis  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 7
- **Protocol:** Clovis (`clovis`) · Yield Aggregator · Sei, Arbitrum, Base, Ethereum, Binance, Avalanche …
- **DefiLlama:** https://defillama.com/protocol/clovis
- **PRIORITY 52.5**  =  LIKELIHOOD 52.5 × ACTIONABILITY 100.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 26.1/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $234,245 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - Conditions: `MULTICHAIN_VERSION_DRIFT`
    - condition MULTICHAIN_VERSION_DRIFT (PRIORITY): Deployed across many chains, where per-chain deployments drift and the least-watched chain sets the risk.
    - 3 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** prior_version_still_callable, still_holds_value_or_authority, not_paused / unmaintained_or_differing_code_path
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#clovis|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#clovis`
- **Disclosure:** https://clovis.network/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.clovis.network/security/audits

### 8. Thesauros  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 8
- **Protocol:** Thesauros (`thesauros`) · Yield · Arbitrum, Base, Plasma, Monad
- **DefiLlama:** https://defillama.com/protocol/thesauros
- **PRIORITY 52.28**  =  LIKELIHOOD 52.28 × ACTIONABILITY 100.0%
    - likelihood = family evidence 30.0/50 (MATCH 60 × evidence weight 1.0) + learned attack surface 22.28/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $51,215 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 60 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `unverified_implementation` — raises likelihood, measured lift ×2.007 (weight +0.70)
    - `owner_is_eoa` — raises likelihood, measured lift ×1.729 (weight +0.55)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`Rebalancer` @ 0xed329611…(arbitrum)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for Rebalancer@0xed329611…(arbitrum); indicators matched: hook_zero_amount_unguarded
    - 1 implementation(s) behind a proxy are NOT verified on the explorer: implementation identity unresolved, score capped at 60
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#thesauros|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#thesauros`
- **Disclosure:** https://thesauros.io · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/Hexens/Smart-Contract-Review-Public-Reports/blob/main/thesauros-oct-25(Final).pdf, https://github.com/Thesauros/contracts/blob/dev/audit/Hexens.pdf

### 9. Tokenlon AMM  —  `SIG-VERIFIER-DEFEATABLE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 9
- **Protocol:** Tokenlon AMM (`tokenlon-amm`) · Dexs · Ethereum
- **DefiLlama:** https://defillama.com/protocol/tokenlon-amm
- **PRIORITY 51.85**  =  LIKELIHOOD 51.85 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 14.95/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $588,461 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A verification routine must reject malformed, empty or zero-recovered signatures, and must never treat address(0) as a match.
    - Deployed source (`Lon` @ 0x00000000…(ethereum), `StakingMultiRewards` @ 0x11520d50…(ethereum)): prerequisites matched: ecrecover_without_zero_check; no guard found
    - deployed source read for Lon@0x00000000…(ethereum), StakingMultiRewards@0x11520d50…(ethereum); indicators matched: ecrecover_without_zero_check
- **Preconditions PRESENT / UNKNOWN:** src::ecrecover_without_zero_check, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** uses_oz_ecdsa / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** OZ ECDSA library in the deployed bytecode (kills the ecrecover-zero shape); Signer address immutable and non-zero
- **Where to start:** On a fork, submit r=0,s=0,v=27 and an empty signature to every signature-gated entrypoint; all must revert.
- **Evidence:** `protocols/deep_screened.jsonl#tokenlon-amm|SIG-VERIFIER-DEFEATABLE`, `protocols/onchain_probes.json#tokenlon-amm`
- **Disclosure:** https://tokenlon.im · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/consenlabs/tokenlon-contracts/tree/v5/audits

### 10. JPEG'd  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 10
- **Protocol:** JPEG'd (`jpegd`) · NFT Lending · Ethereum
- **DefiLlama:** https://defillama.com/protocol/jpegd
- **PRIORITY 51.77**  =  LIKELIHOOD 51.77 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 19.87/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $564,479 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 84.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`JPGD` @ 0xCE722f60…(ethereum)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for JPGD@0xCE722f60…(ethereum); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#jpegd|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#jpegd`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.jpegd.io/other-links/audits

### 11. OnX Finance  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 11
- **Protocol:** OnX Finance (`onx-finance`) · Yield Aggregator · Ethereum, Polygon, Fantom, Avalanche
- **DefiLlama:** https://defillama.com/protocol/onx-finance
- **PRIORITY 51.32**  =  LIKELIHOOD 51.32 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 19.42/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $305,022 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`UniswapV2Pair` @ 0x0652687e…(ethereum), `UniswapV2Pair` @ 0x06da0fd4…(ethereum)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for UniswapV2Pair@0x0652687e…(ethereum), UniswapV2Pair@0x06da0fd4…(ethereum); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#onx-finance|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#onx-finance`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://onx-finance.gitbook.io/docs/audits-and-contracts

### 12. Theoriq Gold Vault  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 12
- **Protocol:** Theoriq Gold Vault (`theoriq-gold-vault`) · Onchain Capital Allocator · Ethereum
- **DefiLlama:** https://defillama.com/protocol/theoriq-gold-vault
- **PRIORITY 50.85**  =  LIKELIHOOD 50.85 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 13.95/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $131,019 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`TokenizedVault` @ 0xee95a5ab…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for TokenizedVault@0xee95a5ab…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#theoriq-gold-vault|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#theoriq-gold-vault`
- **Disclosure:** https://theoriq.ai/ · no audit link listed

### 13. Penpie  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 13
- **Protocol:** Penpie (`penpie`) · Yield · Arbitrum, Ethereum, Hyperliquid L1, Binance, Sonic, Base …
- **DefiLlama:** https://defillama.com/protocol/penpie
- **PRIORITY 50.49**  =  LIKELIHOOD 59.4 × ACTIONABILITY 85.0%
    - likelihood = family evidence 42.5/50 (MATCH 85.0 × evidence weight 1.0) + learned attack surface 16.9/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $4,503,553 · **Band:** `IN_BAND`
- **Previously hacked:** 2024-09-03 for $27,000,000 [Reentrancy]
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 85.0 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
- **Broken invariant tested:** After deployment, no caller may (re)establish ownership, admin, or implementation wiring. Initialization state must be provably consumed.
    - Deployed source (`TransparentUpgradeableProxy` @ 0x0776C069…(arbitrum), `ClonableBeaconProxy` @ 0x0c880f67…(arbitrum)): prerequisites matched: initialize_without_modifier; no guard found
    - deployed source read for TransparentUpgradeableProxy@0x0776C069…(arbitrum), ClonableBeaconProxy@0x0c880f67…(arbitrum); indicators matched: initialize_without_modifier
    - 1/1 live proxies read a zero ERC-7201 Initializable slot (inconclusive alone: older OZ versions store the flag elsewhere)
- **Preconditions PRESENT / UNKNOWN:** src::initialize_without_modifier, upgradeable_architecture, initializer_flag_unset, live_value_or_approvals / none
- **Guards searched / found:** initializer_modifier_present, upgrade_timelocked / none in the reviewed path
- **Prior art:** `KNOWN_ISSUE_DEPLOYMENT_STATUS_UNKNOWN` — DefiLlama's hacks dataset records 1 prior on-chain incident(s) on this protocol, most recently 2024-09-03 for $27,000,000 [Reentrancy]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** Simulated re-initialization reverts (kills the pair); Contract is non-upgradeable and holds no approvals
- **Where to start:** Read the initialization slot on every live proxy/facet and simulate re-initialization from an unprivileged address; it must revert.
- **Evidence:** `protocols/deep_screened.jsonl#penpie|UPGRADE-INITIALIZER-REACHABLE-LIVE`, `protocols/onchain_probes.json#penpie`
- **Disclosure:** https://www.pendle.magpiexyz.io/stake · no audit link listed

### 14. Cryptex V1  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 14
- **Protocol:** Cryptex V1 (`cryptex-v1`) · Indexes · Ethereum, Optimism
- **DefiLlama:** https://defillama.com/protocol/cryptex-v1
- **PRIORITY 50.38**  =  LIKELIHOOD 50.38 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 18.48/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $428,629 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `version_sibling_legacy` — raises likelihood, measured lift ×1.699 (weight +0.53)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`UniswapV2Pair` @ 0x2A93167E…(ethereum), `ERC20VaultHandler` @ 0x443366a7…(ethereum)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for UniswapV2Pair@0x2A93167E…(ethereum), ERC20VaultHandler@0x443366a7…(ethereum); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#cryptex-v1|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#cryptex-v1`
- **Disclosure:** https://cryptex.finance/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://cryptex.finance/Cryptex_-_Final_Report.pdf, https://certificate.quantstamp.com/full/cryptex

### 15. Sudoswap V1  —  `ACC-DUPLICATE-ID-ACCUMULATION`

- **Rank (Ranking A — priority (likelihood × actionability)):** 15
- **Protocol:** Sudoswap V1 (`sudoswap-v1`) · NFT Marketplace · Ethereum
- **DefiLlama:** https://defillama.com/protocol/sudoswap-v1
- **PRIORITY 50.13**  =  LIKELIHOOD 50.13 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 18.23/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $660,847 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `owner_is_eoa` — raises likelihood, measured lift ×1.729 (weight +0.55)
    - `version_sibling_legacy` — raises likelihood, measured lift ×1.699 (weight +0.53)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** An entitlement attached to an identifier may be counted at most once per period. A caller-supplied ID list must be deduplicated, or each ID's claim state consumed before the next read.
    - Deployed source (`LSSVMPairEnumerableETH` @ 0x08142348…(ethereum), `LSSVMPairFactory` @ 0xb16c1342…(ethereum)): prerequisites matched: id_array_loop_without_dedup; no guard found
    - deployed source read for LSSVMPairEnumerableETH@0x08142348…(ethereum), LSSVMPairFactory@0xb16c1342…(ethereum); indicators matched: id_array_loop_without_dedup
- **Preconditions PRESENT / UNKNOWN:** src::id_array_loop_without_dedup, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Consumed marker written inside the loop (kills the pair); IDs required strictly increasing
- **Where to start:** On a fork, call the batch function with one ID repeated k times; payout must equal the single-ID payout.
- **Evidence:** `protocols/deep_screened.jsonl#sudoswap-v1|ACC-DUPLICATE-ID-ACCUMULATION`, `protocols/onchain_probes.json#sudoswap-v1`
- **Disclosure:** https://sudoswap.xyz · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/sudoswap/audits

### 16. PEAKDEFI  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 16
- **Protocol:** PEAKDEFI (`peakdefi`) · Yield · Ethereum, Binance
- **DefiLlama:** https://defillama.com/protocol/peakdefi
- **PRIORITY 50.12**  =  LIKELIHOOD 50.12 × ACTIONABILITY 100.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 23.72/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $110,630 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - Conditions: `DEAD_FRONTEND_FUNDED`
    - condition DEAD_FRONTEND_FUNDED (PRECOND): Front end is dead while contracts still hold value: nobody is watching the deployment that still holds funds.
    - 5 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** unmaintained_or_differing_code_path, prior_version_still_callable, still_holds_value_or_authority / not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#peakdefi|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#peakdefi`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://certificate.quantstamp.com/full/peakdefi

### 17. CANA Holdings California Carbon Credits  —  `SIG-VERIFIER-DEFEATABLE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 17
- **Protocol:** CANA Holdings California Carbon Credits (`cana-holdings-california-carbon-credits`) · RWA · Ethereum
- **DefiLlama:** https://defillama.com/protocol/cana-holdings-california-carbon-credits
- **PRIORITY 49.83**  =  LIKELIHOOD 49.83 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 12.93/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $893,977 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A verification routine must reject malformed, empty or zero-recovered signatures, and must never treat address(0) as a match.
    - Deployed source (`MaseerOne` @ 0x01995A69…(ethereum), `SafeProxy` @ 0xb56F413d…(ethereum)): prerequisites matched: ecrecover_without_zero_check; no guard found
    - deployed source read for MaseerOne@0x01995A69…(ethereum), SafeProxy@0xb56F413d…(ethereum); indicators matched: ecrecover_without_zero_check
- **Preconditions PRESENT / UNKNOWN:** src::ecrecover_without_zero_check, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** uses_oz_ecdsa / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** OZ ECDSA library in the deployed bytecode (kills the ecrecover-zero shape); Signer address immutable and non-zero
- **Where to start:** On a fork, submit r=0,s=0,v=27 and an empty signature to every signature-gated entrypoint; all must revert.
- **Evidence:** `protocols/deep_screened.jsonl#cana-holdings-california-carbon-credits|SIG-VERIFIER-DEFEATABLE`, `protocols/onchain_probes.json#cana-holdings-california-carbon-credits`
- **Disclosure:** https://maseer.finance/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/maseer-finance/maseer-one/blob/master/docs/audits/Prototech%20Labs%20-%20Maseer%20Security%20Report.pdf

### 18. Umami Finance  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 18
- **Protocol:** Umami Finance (`umami-finance`) · Yield · Arbitrum, Avalanche
- **DefiLlama:** https://defillama.com/protocol/umami-finance
- **PRIORITY 49.57**  =  LIKELIHOOD 49.57 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 12.67/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $387,748 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`UMAMI` @ 0x1622bf67…(arbitrum), `MarinateV2` @ 0x2adabd6e…(arbitrum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for UMAMI@0x1622bf67…(arbitrum), MarinateV2@0x2adabd6e…(arbitrum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#umami-finance|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#umami-finance`
- **Disclosure:** https://umami.finance/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://2316168122-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMxcGyx5kIW5oBPBlyRqM%2Fuploads%2FgraEwSrcK8twmgCxivTx%2FUmami%20Audit.pdf?alt=media&token=ccac6185-814e-4284-9b15-b868b00933a0, https://2316168122-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMxcGyx5kIW5oBPBlyRqM%2Fuploads%2Fwpi8lo0iYzlsGyFzSXsR%2FUmami%20DAO%20-%20mUMAMI%20(Zokyo).pdf?alt=media&token=c2d1256c-3660-48cb-95ae-ab38728c9c75

### 19. Tanken Capital  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 19
- **Protocol:** Tanken Capital (`tanken-capital`) · Risk Curators · Ethereum, Base
- **DefiLlama:** https://defillama.com/protocol/tanken-capital
- **PRIORITY 49.22**  =  LIKELIHOOD 49.22 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 12.32/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $85,381 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`GnosisSafeProxy` @ 0x0000aeB7…(base), `PlasmaVault` @ 0x01a6ff6e…(base)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for GnosisSafeProxy@0x0000aeB7…(base), PlasmaVault@0x01a6ff6e…(base); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#tanken-capital|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#tanken-capital`
- **Disclosure:** https://tankencapital.notion.site/Tanken-Capital-1841505ced0680d88c31feb5f6f83433 · no audit link listed

### 20. Swellchain Bridge  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 20
- **Protocol:** Swellchain Bridge (`swellchain-bridge`) · Canonical Bridge · Ethereum
- **DefiLlama:** https://defillama.com/protocol/swellchain-bridge
- **PRIORITY 48.55**  =  LIKELIHOOD 48.55 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 11.65/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $368,677 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
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
- **Evidence:** `protocols/deep_screened.jsonl#swellchain-bridge|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#swellchain-bridge`
- **Disclosure:** https://superbridge.swellnetwork.io · no audit link listed

### 21. MaxShot  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 21
- **Protocol:** MaxShot (`maxshot`) · Onchain Capital Allocator · Ethereum, Base, Arbitrum, Plasma, Optimism
- **DefiLlama:** https://defillama.com/protocol/maxshot
- **PRIORITY 48.53**  =  LIKELIHOOD 48.53 × ACTIONABILITY 100.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 22.13/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $165,700 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - 2 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** prior_version_still_callable, still_holds_value_or_authority, not_paused / unmaintained_or_differing_code_path
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#maxshot|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#maxshot`
- **Disclosure:** https://maxshot.ai/ · no audit link listed

### 22. Alongside  —  `ACC-CREDIT-NOT-RECEIVED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 22
- **Protocol:** Alongside (`alongside`) · Indexes · Ethereum
- **DefiLlama:** https://defillama.com/protocol/alongside
- **PRIORITY 47.68**  =  LIKELIHOOD 47.68 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 15.78/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $467,535 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** Reward credit must be derived from economic value actually transferred to, or spent through, the protocol. A balance delta observed on a third-party venue is not proof of a purchase.
    - Deployed source (`AstETH` @ 0x27C2B9fd…(ethereum), `Vault` @ 0xf3bCeDaB…(ethereum)): prerequisites matched: balance_delta_credit; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): public_claim_fn=no
    - deployed source read for AstETH@0x27C2B9fd…(ethereum), Vault@0xf3bCeDaB…(ethereum); indicators matched: balance_delta_credit
- **Preconditions PRESENT / UNKNOWN:** src::balance_delta_credit, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Credit derived from transferFrom into the protocol (kills the pair); Entitlements written only by a trusted settlement path
- **Where to start:** On a fork, fabricate the observable precondition without transferring value to the protocol; the entitlement must not increase.
- **Evidence:** `protocols/deep_screened.jsonl#alongside|ACC-CREDIT-NOT-RECEIVED`, `protocols/onchain_probes.json#alongside`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/Alongside-Finance/Audits

### 23. Revert Compoundor  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 23
- **Protocol:** Revert Compoundor (`revert-compoundor`) · Liquidity Automation · Ethereum, Arbitrum, Polygon, Optimism, Binance
- **DefiLlama:** https://defillama.com/protocol/revert-compoundor
- **PRIORITY 47.6**  =  LIKELIHOOD 47.6 × ACTIONABILITY 100.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 21.2/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $146,380 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - 6 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** prior_version_still_callable, still_holds_value_or_authority / unmaintained_or_differing_code_path, not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#revert-compoundor|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#revert-compoundor`
- **Disclosure:** https://revert.finance/#/ref/w6vno3 · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://immunefi.com/bounty/revert, https://github.com/peckshield/publications/blob/master/audit_reports/PeckShield-Audit-Report-Revert-Compoundor-v1.0.pdf

### 24. Fira  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 24
- **Protocol:** Fira (`fira`) · Lending · Ethereum
- **DefiLlama:** https://defillama.com/protocol/fira
- **PRIORITY 47.6**  =  LIKELIHOOD 56.0 × ACTIONABILITY 85.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 19.1/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $9,852,774 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`TransparentUpgradeableProxy` @ 0x35D89493…(ethereum), `USDCFW` @ 0x62F5366C…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for TransparentUpgradeableProxy@0x35D89493…(ethereum), USDCFW@0x62F5366C…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#fira|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#fira`
- **Disclosure:** https://www.fira.money/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.fira.money/resources-and-ecosystem/contracts-and-audits

### 25. InsureDAO  —  `SECRET-EMBEDDED-IN-PUBLIC-CODE-AS-AUTH`

- **Rank (Ranking A — priority (likelihood × actionability)):** 25
- **Protocol:** InsureDAO (`insuredao`) · Insurance · Ethereum, Arbitrum, Astar, Optimism
- **DefiLlama:** https://defillama.com/protocol/insuredao
- **PRIORITY 47.6**  =  LIKELIHOOD 47.6 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 15.7/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $123,685 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Deployed bytecode is public. Nothing inside it can be a secret, so no authorisation may depend on knowledge of a value present in the contract.
    - Deployed source (`Vault` @ 0x131fb74c…(ethereum), `ReportingToken` @ 0x190dA1B9…(ethereum)): prerequisites matched: constant_secret_like; no guard found
    - deployed source read for Vault@0x131fb74c…(ethereum), ReportingToken@0x190dA1B9…(ethereum); indicators matched: constant_secret_like
- **Preconditions PRESENT / UNKNOWN:** src::constant_secret_like, live_value_present, deployment_reachable_on_chain / src::hardcoded_signer_address
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Only public keys/addresses appear in code, never private material or shared secrets (kills the pair); No module rights or approvals held
- **Where to start:** Extract every constant from deployed bytecode and test whether presenting it authorises anything.
- **Evidence:** `protocols/deep_screened.jsonl#insuredao|SECRET-EMBEDDED-IN-PUBLIC-CODE-AS-AUTH`, `protocols/onchain_probes.json#insuredao`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://drive.google.com/file/d/1RTwAYuPBmQCVrmor-iZ9dFAGlCkdMtdR/view?usp=sharing

### 26. EZManager  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 26
- **Protocol:** EZManager (`ezmanager`) · Liquidity Manager · Base, Hyperliquid L1, Robinhood Chain, Ethereum, Binance, Arbitrum
- **DefiLlama:** https://defillama.com/protocol/ezmanager
- **PRIORITY 47.4**  =  LIKELIHOOD 47.4 × ACTIONABILITY 100.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 21.0/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $430,190 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `unverified_implementation` — raises likelihood, measured lift ×2.007 (weight +0.70)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - Conditions: `MULTICHAIN_VERSION_DRIFT`
    - condition MULTICHAIN_VERSION_DRIFT (PRIORITY): Deployed across many chains, where per-chain deployments drift and the least-watched chain sets the risk.
    - 1 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** prior_version_still_callable, still_holds_value_or_authority / unmaintained_or_differing_code_path, not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#ezmanager|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#ezmanager`
- **Disclosure:** https://ezmanager.finance · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/cyberscope-io/audits/blob/main/ezmanager/audit.pdf

### 27. Mayan Bridge  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 27
- **Protocol:** Mayan Bridge (`mayan-bridge`) · Bridge · Base, Arbitrum, Ethereum, Binance, Optimism, Polygon …
- **DefiLlama:** https://defillama.com/protocol/mayan-bridge
- **PRIORITY 47.4**  =  LIKELIHOOD 47.4 × ACTIONABILITY 100.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 21.0/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $123,829 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `unverified_implementation` — raises likelihood, measured lift ×2.007 (weight +0.70)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - Conditions: `MULTICHAIN_VERSION_DRIFT`
    - condition MULTICHAIN_VERSION_DRIFT (PRIORITY): Deployed across many chains, where per-chain deployments drift and the least-watched chain sets the risk.
    - 6 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** prior_version_still_callable, still_holds_value_or_authority / unmaintained_or_differing_code_path, not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#mayan-bridge|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#mayan-bridge`
- **Disclosure:** https://mayan.finance/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.mayan.finance/resources/audits

### 28. Rezerve Money  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 28
- **Protocol:** Rezerve Money (`rezerve-money`) · Reserve Currency · Ethereum, Sonic, Binance, Hyperliquid L1, Base
- **DefiLlama:** https://defillama.com/protocol/rezerve-money
- **PRIORITY 47.38**  =  LIKELIHOOD 47.38 × ACTIONABILITY 100.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 20.98/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $598,045 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - Conditions: `DEAD_FRONTEND_FUNDED`
    - condition DEAD_FRONTEND_FUNDED (PRECOND): Front end is dead while contracts still hold value: nobody is watching the deployment that still holds funds.
    - 4 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** unmaintained_or_differing_code_path, prior_version_still_callable, still_holds_value_or_authority, not_paused / none
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#rezerve-money|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#rezerve-money`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://rezerve.gitbook.io/protocol/security/audits

### 29. Mint Club V2  —  `ACC-DUPLICATE-ID-ACCUMULATION`

- **Rank (Ranking A — priority (likelihood × actionability)):** 29
- **Protocol:** Mint Club V2 (`mint-club-v2`) · Launchpad · Base, Ethereum, Zora, Binance, Klaytn, Unichain …
- **DefiLlama:** https://defillama.com/protocol/mint-club-v2
- **PRIORITY 47.32**  =  LIKELIHOOD 47.32 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 15.42/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $697,219 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** An entitlement attached to an identifier may be counted at most once per period. A caller-supplied ID list must be deduplicated, or each ID's claim state consumed before the next read.
    - Deployed source (`DixelClubV2NFT` @ 0x1f3Af095…(base), `BulkSender` @ 0x29b0E6D2…(base)): prerequisites matched: id_array_loop_without_dedup; no guard found
    - deployed source read for DixelClubV2NFT@0x1f3Af095…(base), BulkSender@0x29b0E6D2…(base); indicators matched: id_array_loop_without_dedup
- **Preconditions PRESENT / UNKNOWN:** src::id_array_loop_without_dedup, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `EOA_SINGLE_KEY`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Consumed marker written inside the loop (kills the pair); IDs required strictly increasing
- **Where to start:** On a fork, call the batch function with one ID repeated k times; payout must equal the single-ID payout.
- **Evidence:** `protocols/deep_screened.jsonl#mint-club-v2|ACC-DUPLICATE-ID-ACCUMULATION`, `protocols/onchain_probes.json#mint-club-v2`
- **Disclosure:** https://mint.club · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/Steemhunt/mint.club-v2-contract/blob/main/security-audits/CertiK-20240118.pdf

### 30. UniFarm  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 30
- **Protocol:** UniFarm (`unifarm`) · Yield · Ethereum, Binance, Polygon
- **DefiLlama:** https://defillama.com/protocol/unifarm
- **PRIORITY 47.28**  =  LIKELIHOOD 47.28 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 15.38/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $238,839 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `owner_is_eoa` — raises likelihood, measured lift ×1.729 (weight +0.55)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`DVTT` @ 0x00d46727…(ethereum), `CentaurToken` @ 0x03042482…(ethereum)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for DVTT@0x00d46727…(ethereum), CentaurToken@0x03042482…(ethereum); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#unifarm|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#unifarm`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://blog.oropocket.com/wp-content/uploads/2021/02/OpenDeFi-Unifarm-Audit-Report-QuillAudits.pdf

### 31. Mitosis  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 31
- **Protocol:** Mitosis (`mitosis`) · Onchain Capital Allocator · Binance, Linea, Arbitrum, Ethereum, Morph, Base …
- **DefiLlama:** https://defillama.com/protocol/mitosis
- **PRIORITY 47.24**  =  LIKELIHOOD 55.58 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 23.68/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $1,379,158 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`ProxyAdmin` @ 0x096430ef…(ethereum), `TheoDepositVault` @ 0x0B75e167…(ethereum)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for ProxyAdmin@0x096430ef…(ethereum), TheoDepositVault@0x0B75e167…(ethereum); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#mitosis|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#mitosis`
- **Disclosure:** https://mitosis.org · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://omniscia.io/reports/mitosis-core-protocol-65d72c4f31a85a00186cf5f8

### 32. DELV Yield  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking A — priority (likelihood × actionability)):** 32
- **Protocol:** DELV Yield (`delv-yield`) · Yield · Ethereum
- **DefiLlama:** https://defillama.com/protocol/delv-yield
- **PRIORITY 47.12**  =  LIKELIHOOD 47.12 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 10.22/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $741,190 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source (`WeightedPool` @ 0x2D6e3515…(ethereum), `TrancheFactory` @ 0x62F161BF…(ethereum)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for WeightedPool@0x2D6e3515…(ethereum), TrancheFactory@0x62F161BF…(ethereum); indicators matched: unsafe_cross_sign_cast
- **Preconditions PRESENT / UNKNOWN:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** safecast_used / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#delv-yield|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#delv-yield`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.element.fi/developers/bug-bounty-programs#b93e

### 33. Union Protocol  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 33
- **Protocol:** Union Protocol (`union-protocol`) · Uncollateralized Lending · Optimism, Ethereum, Base, Arbitrum
- **DefiLlama:** https://defillama.com/protocol/union-protocol
- **PRIORITY 47.12**  =  LIKELIHOOD 47.12 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 10.22/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $266,411 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`UUPSProxy` @ 0x954F20DF…(ethereum), `UserManager` @ 0xb71F3D43…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for UUPSProxy@0x954F20DF…(ethereum), UserManager@0xb71F3D43…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#union-protocol|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#union-protocol`
- **Disclosure:** https://union.finance · no audit link listed

### 34. Dyson  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 34
- **Protocol:** Dyson (`dyson`) · Liquidity Manager · Arbitrum, Polygon, Base, Avalanche, Optimism, Binance …
- **DefiLlama:** https://defillama.com/protocol/dyson
- **PRIORITY 46.85**  =  LIKELIHOOD 46.85 × ACTIONABILITY 100.0%
    - likelihood = family evidence 30.0/50 (MATCH 60 × evidence weight 1.0) + learned attack surface 16.85/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $265,697 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 60 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `unverified_implementation` — raises likelihood, measured lift ×2.007 (weight +0.70)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `owner_is_eoa` — raises likelihood, measured lift ×1.729 (weight +0.55)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`SterlingStaker` @ 0x2a71d8f8…(arbitrum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for SterlingStaker@0x2a71d8f8…(arbitrum); indicators matched: owner_compare_without_nonzero
    - 1 implementation(s) behind a proxy are NOT verified on the explorer: implementation identity unresolved, score capped at 60
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#dyson|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#dyson`
- **Disclosure:** https://www.dyson.money/ · no audit link listed

### 35. Electra  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 35
- **Protocol:** Electra (`electra`) · Derivatives · Binance, TON, Ethereum
- **DefiLlama:** https://defillama.com/protocol/electra
- **PRIORITY 46.7**  =  LIKELIHOOD 46.7 × ACTIONABILITY 100.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 20.3/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $81,945 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `unverified_implementation` — raises likelihood, measured lift ×2.007 (weight +0.70)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `owner_is_eoa` — raises likelihood, measured lift ×1.729 (weight +0.55)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - 1 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** prior_version_still_callable, still_holds_value_or_authority / unmaintained_or_differing_code_path, not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#electra|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#electra`
- **Disclosure:** https://electra.trade/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/EXVUL-Sec/AuditReport/blob/main/Smartcontract/Electra%20Smart%20Contract%20Audit%20Report-Exvul.pdf

### 36. Indexed Finance  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 36
- **Protocol:** Indexed Finance (`indexed-finance`) · Indexes · Ethereum
- **DefiLlama:** https://defillama.com/protocol/indexed-finance
- **PRIORITY 46.45**  =  LIKELIHOOD 46.45 × ACTIONABILITY 100.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 20.05/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $120,981 · **Band:** `IN_BAND`
- **REPEAT VICTIM — 2 recorded hacks.** 2023-03-21 $9,925 [Swap Logic Flaw]
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - Conditions: `DEAD_FRONTEND_FUNDED`
    - condition DEAD_FRONTEND_FUNDED (PRECOND): Front end is dead while contracts still hold value: nobody is watching the deployment that still holds funds.
    - 2 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** unmaintained_or_differing_code_path, prior_version_still_callable, still_holds_value_or_authority / not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `UNREMEDIATED_KNOWN_ISSUE` — DefiLlama's hacks dataset records 1 prior on-chain incident(s) on this protocol, most recently 2023-03-21 for $9,925 [Swap Logic Flaw]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#indexed-finance|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#indexed-finance`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.indexed.finance/protocol/security

### 37. Yay!  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 37
- **Protocol:** Yay! (`yay!`) · SoFi · Ethereum, Soneium
- **DefiLlama:** https://defillama.com/protocol/yay!
- **PRIORITY 46.28**  =  LIKELIHOOD 46.28 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 9.38/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $735,231 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `TrueGBP` @ 0x00000000…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for ZAMM@0x00000000…(ethereum), TrueGBP@0x00000000…(ethereum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#yay!|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#yay!`
- **Disclosure:** https://portal.yay.space/stake · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://yay.gitbook.io/yay-staking/audits

### 38. MoreMarkets.xyz  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 38
- **Protocol:** MoreMarkets.xyz (`moremarkets.xyz`) · Yield · Ethereum, Flare, Ripple, Near
- **DefiLlama:** https://defillama.com/protocol/moremarkets.xyz
- **PRIORITY 46.15**  =  LIKELIHOOD 46.15 × ACTIONABILITY 100.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 19.75/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $478,707 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - Conditions: `DEAD_FRONTEND_FUNDED`
    - condition DEAD_FRONTEND_FUNDED (PRECOND): Front end is dead while contracts still hold value: nobody is watching the deployment that still holds funds.
    - 5 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** unmaintained_or_differing_code_path, prior_version_still_callable, still_holds_value_or_authority, not_paused / none
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#moremarkets.xyz|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#moremarkets.xyz`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.moremarkets.xyz/developers/contracts

### 39. CVI Finance  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 39
- **Protocol:** CVI Finance (`cvi-finance`) · Synthetics · Polygon, Ethereum, Arbitrum
- **DefiLlama:** https://defillama.com/protocol/cvi-finance
- **PRIORITY 46.13**  =  LIKELIHOOD 46.13 × ACTIONABILITY 100.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 19.73/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $118,194 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - 2 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** prior_version_still_callable, still_holds_value_or_authority / unmaintained_or_differing_code_path, not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#cvi-finance|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#cvi-finance`
- **Disclosure:** https://cvi.finance/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://cvi.finance/files/usdt-audit.pdf, https://cvi.finance/files/eth-audit.pdf

### 40. SuperReturn  —  `ACC-DONATION-UNACCOUNTED-BALANCE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 40
- **Protocol:** SuperReturn (`superreturn`) · Onchain Capital Allocator · Soneium, Arbitrum, Plume Mainnet, Ethereum
- **DefiLlama:** https://defillama.com/protocol/superreturn
- **PRIORITY 46.05**  =  LIKELIHOOD 46.05 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 14.15/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $94,461 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
- **Broken invariant tested:** A share price, exchange rate or totalAssets must be a function of value the protocol accounted for on entry. Reading a raw balance makes any direct transfer into the accounting boundary an unpriced increase in every holder's claim.
    - Deployed source (`MetaMorphoV1_1` @ 0x4B6F1C9E…(arbitrum)): prerequisites matched: totalAssets_reads_balanceOf; no guard found
    - deployed source read for MetaMorphoV1_1@0x4B6F1C9E…(arbitrum); indicators matched: totalAssets_reads_balanceOf
- **Preconditions PRESENT / UNKNOWN:** src::totalAssets_reads_balanceOf, unprivileged_inbound_transfer_possible, live_value_exposed / src::getCashPrior_balanceOf
- **Guards searched / found:** internal_cash_counter / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** totalAssets derived from an internal counter, not balanceOf (kills the pair); Rate is monotonic and rate-limited per block; Inbound transfers to the accounting boundary are rejected or swept to a reserve
- **Where to start:** On a fork, transfer an arbitrary amount of each counted asset directly into every accounting boundary; the share price, exchange rate and derived borrow power must not change.
- **Evidence:** `protocols/deep_screened.jsonl#superreturn|ACC-DONATION-UNACCOUNTED-BALANCE`, `protocols/onchain_probes.json#superreturn`
- **Disclosure:** https://www.superreturn.ai/ · no audit link listed

### 41. PlutusDAO  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 41
- **Protocol:** PlutusDAO (`plutusdao`) · Yield · Arbitrum
- **DefiLlama:** https://defillama.com/protocol/plutusdao
- **PRIORITY 45.9**  =  LIKELIHOOD 45.9 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 14.0/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $345,413 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`PlsSpaToken` @ 0x0D111e48…(arbitrum), `PlutusEpochStaking` @ 0x27Aaa9D5…(arbitrum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for PlsSpaToken@0x0D111e48…(arbitrum), PlutusEpochStaking@0x27Aaa9D5…(arbitrum); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#plutusdao|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#plutusdao`
- **Disclosure:** https://plutusdao.io · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://solidity.finance/audits/PlvGLP, https://www.certik.com/projects/plutusdao

### 42. Altitude.Fi  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 42
- **Protocol:** Altitude.Fi (`altitude.fi`) · Lending · Ethereum
- **DefiLlama:** https://defillama.com/protocol/altitude.fi
- **PRIORITY 45.88**  =  LIKELIHOOD 45.88 × ACTIONABILITY 100.0%
    - likelihood = family evidence 30.0/50 (MATCH 60 × evidence weight 1.0) + learned attack surface 15.88/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $520,834 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 60 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `unverified_implementation` — raises likelihood, measured lift ×2.007 (weight +0.70)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`SupplyToken` @ 0x5f12942a…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for SupplyToken@0x5f12942a…(ethereum); indicators matched: claim_without_eligibility_map
    - 1 implementation(s) behind a proxy are NOT verified on the explorer: implementation identity unresolved, score capped at 60
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **one externally-owned account** (`EOA_SINGLE_KEY`) — a code fix here does not remove that exposure, and it is the cheaper thing to raise first
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#altitude.fi|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#altitude.fi`
- **Disclosure:** https://www.altitude.fi/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.altitude.fi/smart-contracts/audits#completed-audits

### 43. DerivaDEX  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 43
- **Protocol:** DerivaDEX (`derivadex`) · Derivatives · Ethereum
- **DefiLlama:** https://defillama.com/protocol/derivadex
- **PRIORITY 45.82**  =  LIKELIHOOD 45.82 × ACTIONABILITY 100.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 19.42/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $613,548 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - 6 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** prior_version_still_callable, still_holds_value_or_authority / unmaintained_or_differing_code_path, not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#derivadex|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#derivadex`
- **Disclosure:** http://derivadex.com · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://certificate.quantstamp.com/full/deriva-dex

### 44. Voltz  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 44
- **Protocol:** Voltz (`voltz`) · Derivatives · Ethereum, Arbitrum, Avalanche
- **DefiLlama:** https://defillama.com/protocol/voltz
- **PRIORITY 45.8**  =  LIKELIHOOD 45.8 × ACTIONABILITY 100.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 19.4/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $239,032 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - 1 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** prior_version_still_callable, still_holds_value_or_authority / unmaintained_or_differing_code_path, not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#voltz|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#voltz`
- **Disclosure:** https://www.voltz.xyz · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://certificate.quantstamp.com/full/voltz-protocol, https://www.certik.com/projects/voltz

### 45. ImmutableX  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 45
- **Protocol:** ImmutableX (`immutablex`) · NFT Marketplace · Ethereum
- **DefiLlama:** https://defillama.com/protocol/immutablex
- **PRIORITY 45.77**  =  LIKELIHOOD 45.77 × ACTIONABILITY 100.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 19.37/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $593,149 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - 6 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** prior_version_still_callable, still_holds_value_or_authority / unmaintained_or_differing_code_path, not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#immutablex|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#immutablex`
- **Disclosure:** https://imx.community/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://skynet.certik.com/projects/immutable-x

### 46. Amphor  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking A — priority (likelihood × actionability)):** 46
- **Protocol:** Amphor (`amphor`) · Yield · Ethereum
- **DefiLlama:** https://defillama.com/protocol/amphor
- **PRIORITY 45.75**  =  LIKELIHOOD 45.75 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 8.85/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $62,416 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source (`AmphorVaultWithPermit` @ 0x0498b85F…(ethereum), `BeaconProxy` @ 0x06824C27…(ethereum)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for AmphorVaultWithPermit@0x0498b85F…(ethereum), BeaconProxy@0x06824C27…(ethereum); indicators matched: unsafe_cross_sign_cast
- **Preconditions PRESENT / UNKNOWN:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** safecast_used / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#amphor|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#amphor`
- **Disclosure:** https://amphor.io · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/AmphorProtocol/synthetic-vault/blob/main/audits/Salus_final_report.pdf, https://github.com/AmphorProtocol/synthetic-vault/blob/main/audits/Bailsec_final_report.pdf

### 47. Skate Fi  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 47
- **Protocol:** Skate Fi (`skate-fi`) · Liquidity Manager · Ethereum, ZetaChain, Manta, Binance, Mantle, Arbitrum …
- **DefiLlama:** https://defillama.com/protocol/skate-fi
- **PRIORITY 45.73**  =  LIKELIHOOD 45.73 × ACTIONABILITY 100.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 19.33/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $118,982 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - Conditions: `MULTICHAIN_VERSION_DRIFT`
    - condition MULTICHAIN_VERSION_DRIFT (PRIORITY): Deployed across many chains, where per-chain deployments drift and the least-watched chain sets the risk.
    - 2 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** prior_version_still_callable, still_holds_value_or_authority / unmaintained_or_differing_code_path, not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#skate-fi|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#skate-fi`
- **Disclosure:** https://www.rangeprotocol.com · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/Range-Protocol/contracts/blob/master/audits/Certik-Audit.pdf, https://github.com/Range-Protocol/contracts/blob/master/audits/Halborn-Audit.pdf

### 48. DFX V2  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking A — priority (likelihood × actionability)):** 48
- **Protocol:** DFX V2 (`dfx-v2`) · Dexs · Ethereum, Polygon, Arbitrum
- **DefiLlama:** https://defillama.com/protocol/dfx-v2
- **PRIORITY 45.72**  =  LIKELIHOOD 45.72 × ACTIONABILITY 100.0%
    - likelihood = family evidence 30.0/50 (MATCH 60 × evidence weight 1.0) + learned attack surface 15.72/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $84,226 · **Band:** `IN_BAND`
- **Previously hacked:** 2022-11-10 for $4,000,000 [Reentrancy]
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 60 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `unverified_implementation` — raises likelihood, measured lift ×2.007 (weight +0.70)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `version_sibling_legacy` — raises likelihood, measured lift ×1.699 (weight +0.53)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source (`CurveFactoryV2` @ 0x9adeac3b…(ethereum)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for CurveFactoryV2@0x9adeac3b…(ethereum); indicators matched: unsafe_cross_sign_cast
    - 1 implementation(s) behind a proxy are NOT verified on the explorer: implementation identity unresolved, score capped at 60
- **Preconditions PRESENT / UNKNOWN:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** safecast_used / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `KNOWN_ISSUE_DEPLOYMENT_STATUS_UNKNOWN` — DefiLlama's hacks dataset records 1 prior on-chain incident(s) on this protocol, most recently 2022-11-10 for $4,000,000 [Reentrancy]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#dfx-v2|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#dfx-v2`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/dfx-finance/protocol/blob/main/audits/2021-05-03-Trail_of_Bits.pdf

### 49. Yellow  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 49
- **Protocol:** Yellow (`yellow`) · Dexs · Polygon, Linea, Ethereum, Scroll
- **DefiLlama:** https://defillama.com/protocol/yellow
- **PRIORITY 45.62**  =  LIKELIHOOD 45.62 × ACTIONABILITY 100.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 19.22/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $75,772 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - 6 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** prior_version_still_callable, still_holds_value_or_authority / unmaintained_or_differing_code_path, not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#yellow|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#yellow`
- **Disclosure:** https://www.yellow.org · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://audits.hacken.io/openware-yellow-network

### 50. Flying Tulip ftUSD  —  `ACC-DUPLICATE-ID-ACCUMULATION`

- **Rank (Ranking A — priority (likelihood × actionability)):** 50
- **Protocol:** Flying Tulip ftUSD (`flying-tulip-ftusd`) · Yield Aggregator · Ethereum, Sonic
- **DefiLlama:** https://defillama.com/protocol/flying-tulip-ftusd
- **PRIORITY 45.62**  =  LIKELIHOOD 53.67 × ACTIONABILITY 85.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 21.77/50
    - actionability: mid-band: a team of this size will usually take an outside report
- **Value at risk:** $2,273,825 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** An entitlement attached to an identifier may be counted at most once per period. A caller-supplied ID list must be deduplicated, or each ID's claim state consumed before the next read.
    - Deployed source (`MintAndRedeem` @ 0x8852b132…(ethereum)): prerequisites matched: id_array_loop_without_dedup; no guard found
    - deployed source read for MintAndRedeem@0x8852b132…(ethereum); indicators matched: id_array_loop_without_dedup
- **Preconditions PRESENT / UNKNOWN:** src::id_array_loop_without_dedup, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Consumed marker written inside the loop (kills the pair); IDs required strictly increasing
- **Where to start:** On a fork, call the batch function with one ID repeated k times; payout must equal the single-ID payout.
- **Evidence:** `protocols/deep_screened.jsonl#flying-tulip-ftusd|ACC-DUPLICATE-ID-ACCUMULATION`, `protocols/onchain_probes.json#flying-tulip-ftusd`
- **Disclosure:** https://flyingtulip.com/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.flyingtulip.com/risks/

### 51. B-Lucky  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 51
- **Protocol:** B-Lucky (`b-lucky`) · Luck Games · Binance
- **DefiLlama:** https://defillama.com/protocol/b-lucky
- **PRIORITY 45.52**  =  LIKELIHOOD 45.52 × ACTIONABILITY 100.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 19.12/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $264,169 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `unverified_implementation` — raises likelihood, measured lift ×2.007 (weight +0.70)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - 5 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** prior_version_still_callable, still_holds_value_or_authority, not_paused / unmaintained_or_differing_code_path
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#b-lucky|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#b-lucky`
- **Disclosure:** https://b-lucky.gg/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://b-lucky.gg/audit/bailsec.pdf

### 52. Fortunafi  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 52
- **Protocol:** Fortunafi (`fortunafi`) · RWA · Ethereum, Canto, Arbitrum, Blast
- **DefiLlama:** https://defillama.com/protocol/fortunafi
- **PRIORITY 45.5**  =  LIKELIHOOD 45.5 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 13.6/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $221,821 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `owner_is_eoa` — raises likelihood, measured lift ×1.729 (weight +0.55)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`OffchainFund` @ 0x108Ec61b…(ethereum), `OffchainFund` @ 0x2378aC4E…(ethereum)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for OffchainFund@0x108Ec61b…(ethereum), OffchainFund@0x2378aC4E…(ethereum); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `EOA_SINGLE_KEY`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#fortunafi|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#fortunafi`
- **Disclosure:** https://fortunafi.com/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://fortunafi.gitbook.io/fortunafi/audits

### 53. Sector Finance  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 53
- **Protocol:** Sector Finance (`sector-finance`) · Yield · Arbitrum, Optimism, Ethereum, Moonriver
- **DefiLlama:** https://defillama.com/protocol/sector-finance
- **PRIORITY 45.42**  =  LIKELIHOOD 45.42 × ACTIONABILITY 100.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 19.02/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $69,124 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `unverified_implementation` — raises likelihood, measured lift ×2.007 (weight +0.70)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `owner_is_eoa` — raises likelihood, measured lift ×1.729 (weight +0.55)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - 1 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** prior_version_still_callable, still_holds_value_or_authority / unmaintained_or_differing_code_path, not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#sector-finance|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#sector-finance`
- **Disclosure:** https://sector.finance · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://1194552491-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Faizh7QHFZ0AM4JGHZRn6%2Fuploads%2Fj3nsS4VbUkK4j5ucSRq8%2FSector_Finance_Smart_Contract_Security_Audit_Report_Halborn_Final.pdf?alt=media&token=baabd2bb-7f8d-40ee-b8ff-b66f84c1345a, https://1194552491-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Faizh7QHFZ0AM4JGHZRn6%2Fuploads%2FhOfiANzdgcROK65IdYip%2FSector_Finance_New_Strategies_and_Vaults_Upgradeable_Contracts_Smart_Contract_Security_Audit_Report_Halborn_Final.pdf?alt=media&token=567d90c1-5bcc-4ae9-91f5-b48acc0515d3

### 54. ChainPort  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 54
- **Protocol:** ChainPort (`chainport`) · Bridge · Ethereum, Cardano, Binance, Polygon, Fantom
- **DefiLlama:** https://defillama.com/protocol/chainport
- **PRIORITY 45.37**  =  LIKELIHOOD 45.37 × ACTIONABILITY 100.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 18.97/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $502,574 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.475 (weight +0.91)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - 6 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** prior_version_still_callable, still_holds_value_or_authority / unmaintained_or_differing_code_path, not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#chainport|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#chainport`
- **Disclosure:** https://app.chainport.io · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://www.certik.com/projects/chainport

### 55. HyperJump  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 55
- **Protocol:** HyperJump (`hyperjump`) · Dexs · Binance, Fantom, Metis
- **DefiLlama:** https://defillama.com/protocol/hyperjump
- **PRIORITY 45.33**  =  LIKELIHOOD 45.33 × ACTIONABILITY 100.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 18.93/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $227,581 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `unverified_implementation` — raises likelihood, measured lift ×2.007 (weight +0.70)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `owner_is_eoa` — raises likelihood, measured lift ×1.729 (weight +0.55)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - Conditions: `DEAD_FRONTEND_FUNDED`
    - condition DEAD_FRONTEND_FUNDED (PRECOND): Front end is dead while contracts still hold value: nobody is watching the deployment that still holds funds.
    - 2 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** unmaintained_or_differing_code_path, prior_version_still_callable, still_holds_value_or_authority / not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#hyperjump|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#hyperjump`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.hyperjump.fi/essentials/audits

### 56. Biswap V3  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 56
- **Protocol:** Biswap V3 (`biswap-v3`) · Dexs · Binance, Base, Arbitrum, Ethereum
- **DefiLlama:** https://defillama.com/protocol/biswap-v3
- **PRIORITY 45.3**  =  LIKELIHOOD 45.3 × ACTIONABILITY 100.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 18.9/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $406,484 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `unverified_implementation` — raises likelihood, measured lift ×2.007 (weight +0.70)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - 1 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** prior_version_still_callable, still_holds_value_or_authority / unmaintained_or_differing_code_path, not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#biswap-v3|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#biswap-v3`
- **Disclosure:** https://biswap.org/pool · no audit link listed

### 57. KEEP Network  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 57
- **Protocol:** KEEP Network (`keep-network`) · Cross Chain Bridge · Ethereum
- **DefiLlama:** https://defillama.com/protocol/keep-network
- **PRIORITY 45.25**  =  LIKELIHOOD 45.25 × ACTIONABILITY 100.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 18.85/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $875,059 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×3.73 (weight +1.32)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - 3 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** prior_version_still_callable, still_holds_value_or_authority / unmaintained_or_differing_code_path, not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#keep-network|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#keep-network`
- **Disclosure:** https://app.threshold.network/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://consensys.net/diligence/audits/2020/02/thesis-tbtc-and-keep/

### 58. Jones DAO  —  `ACC-DONATION-UNACCOUNTED-BALANCE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 58
- **Protocol:** Jones DAO (`jones-dao`) · Yield Aggregator · Arbitrum, Ethereum
- **DefiLlama:** https://defillama.com/protocol/jones-dao
- **PRIORITY 45.22**  =  LIKELIHOOD 45.22 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 13.32/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $982,466 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A share price, exchange rate or totalAssets must be a function of value the protocol accounted for on entry. Reading a raw balance makes any direct transfer into the accounting boundary an unpriced increase in every holder's claim.
    - Deployed source (`JonesToken` @ 0x10393c20…(arbitrum), `JonesGlpVaultRouter` @ 0x2F43c647…(arbitrum)): prerequisites matched: totalAssets_reads_balanceOf; no guard found
    - deployed source read for JonesToken@0x10393c20…(arbitrum), JonesGlpVaultRouter@0x2F43c647…(arbitrum); indicators matched: totalAssets_reads_balanceOf
- **Preconditions PRESENT / UNKNOWN:** src::totalAssets_reads_balanceOf, unprivileged_inbound_transfer_possible, live_value_exposed / src::getCashPrior_balanceOf
- **Guards searched / found:** internal_cash_counter / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** totalAssets derived from an internal counter, not balanceOf (kills the pair); Rate is monotonic and rate-limited per block; Inbound transfers to the accounting boundary are rejected or swept to a reserve
- **Where to start:** On a fork, transfer an arbitrary amount of each counted asset directly into every accounting boundary; the share price, exchange rate and derived borrow power must not change.
- **Evidence:** `protocols/deep_screened.jsonl#jones-dao|ACC-DONATION-UNACCOUNTED-BALANCE`, `protocols/onchain_probes.json#jones-dao`
- **Disclosure:** https://jonesdao.io · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.jonesdao.io/jones-dao/other/security

### 59. Sherlock  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 59
- **Protocol:** Sherlock (`sherlock`) · Insurance · Ethereum
- **DefiLlama:** https://defillama.com/protocol/sherlock
- **PRIORITY 45.08**  =  LIKELIHOOD 45.08 × ACTIONABILITY 100.0%
    - likelihood = family evidence 30.0/50 (MATCH 60 × evidence weight 1.0) + learned attack surface 15.08/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $501,696 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 60 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `unverified_implementation` — raises likelihood, measured lift ×2.007 (weight +0.70)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`Sherlock` @ 0x0865a889…(ethereum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for Sherlock@0x0865a889…(ethereum); indicators matched: owner_compare_without_nonzero
    - 1 implementation(s) behind a proxy are NOT verified on the explorer: implementation identity unresolved, score capped at 60
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#sherlock|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#sherlock`
- **Disclosure:** https://sherlock.xyz · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/sherlock-protocol/sherlock-v2-core/tree/main/audits

### 60. USDFI Lending  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 60
- **Protocol:** USDFI Lending (`usdfi-lending`) · Lending · Binance
- **DefiLlama:** https://defillama.com/protocol/usdfi-lending
- **PRIORITY 45.08**  =  LIKELIHOOD 45.08 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 13.18/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $80,449 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `owner_is_eoa` — raises likelihood, measured lift ×1.729 (weight +0.55)
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
- **Evidence:** `protocols/deep_screened.jsonl#usdfi-lending|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#usdfi-lending`
- **Disclosure:** https://lending.usdfi.com/usdlend · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.usdfi.com/developers/audits, https://olafinance.gitbook.io/ola-finance/security-reports/audit-reports
