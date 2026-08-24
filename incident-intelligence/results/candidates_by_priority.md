# Candidates — Ranking A — priority (likelihood × actionability)

> **Discovery stage.** This file asserts no defect in any protocol named below. Each entry is a *review candidate*: named evidence matches a family's prerequisites, named evidence is unknown, and a named guard would falsify it. Verify on a local or pinned fork before concluding anything.

**Scoring is now validated, not asserted.** Attack-surface weights were fitted on 2022-24 hacks and tested against 2025-26 hacks: 95 protocols unseen during fitting, median victim landing at the **78.6th percentile**, **58%** of future victims in the model's top quartile — a **×2.32 lift** over chance.

**Likelihood and actionability are kept apart.** Bigger protocols are *more* likely to be attacked (`tvl_over_5m` carries lift ×1.75) and *less* actionable for an independent reviewer. Folding those together is what produced earlier rankings full of protocols you cannot help. PRIORITY multiplies them explicitly so you can see both halves.

**Exposure age beat every other addition, and it contradicts the obvious intuition.** Protocols under a year old carry lift ×1.87; protocols over three years old carry ×0.33. It is not the abandoned deployments that get hit — it is the new ones. Ablation attributes the whole out-of-sample gain to this one group (×2.19 → ×2.32).

**Custody posture was measured and then deliberately dropped from the score.** A single-key upgrade authority does not predict a code defect (measured ×0.98 over the full window; adding it moved out-of-sample lift ×2.19 → ×2.15, i.e. slightly worse). That is the expected answer, since key compromise is an excluded root cause here — so it is reported on its own in `results/upgrade_authority_exposure.md`, where 23 protocols holding $56.4M have an ERC-1967 upgrade authority terminating in a single key. Often the cheapest thing on this whole list to fix.

**A finding that overturned the earlier model:** measured against survivors only, neglect looked protective. It is not — 62.5% of victims that fell below $50k had no audit, versus 20.9% of those still listed. The population was censored by the very outcome being predicted. Weights are now fitted against the full listed universe.

### At a glance

| | |
|---|---:|
| Candidates | 60 |
| Previously hacked | 7 |
| Repeat victims (2+ recorded hacks) | 1 |
| Median value at risk | $203,354 |
| Total value at risk | $18,774,811 |
| At L4 guard review | 44 |
| Previously delivered (withheld from this list) | 169 |

### Every protocol here is one you have not been given before

A candidate list is a queue of work, not a leaderboard. **169 protocols that survive screening were withheld from this run because earlier runs already handed them over** across 5 previous deliveries. They are not resolved and not ruled out — they were already given to you, so repeating them would hand you no new work.

| Previous delivery | Protocols handed over |
|---|---:|
| `7d49c12` — Add six-month DeFi incident intelligence and DefiLlama audit pri | 24 |
| `ccb5273` — Expand the screen to a $50k floor with a condition layer and dep | 49 |
| `3bc30a7` — Re-target the screen at what actually gets hacked, in a reviewab | 72 |
| `2ce88d1` — Validate the ranking model and measure custody exposure separate | 111 |
| `5a3468f` — Remove leftovers from earlier iterations of this run | 111 |

The full ledger is `protocols/delivered_ledger.json`, reconstructed from git history rather than from anything remembered between runs. Every withheld protocol still appears in `candidates_all.csv` with `previously_delivered=YES` and the run that delivered it, so nothing is hidden — it is only kept out of the queue.

<details><summary>The 169 withheld protocols</summary>

`88mph`, `aave-v3`, `aavegotchi`, `abracadabra-spell`, `accountable`, `accumulated-finance-liquid-staking`, `across`, `agave`, `ajna-v1`, `aloe`, `angle`, `ante-finance`, `anzen-v2`, `aperocket`, `arcade.xyz`, `aura`, `badger-dao`, `balancer-v2`, `bancor-v2.1`, `bifi`, `blackwing`, `bond-protocol`, `boringdao`, `bridge-mutual`, `bunni-v2`, `bunny`, `burgerswap`, `cakepie`, `capyfi`, `caviar-v1`, `cega-v1`, `charm-finance-v1`, `conic-finance`, `contango-v1`, `convex-finance`, `cook-finance`, `cream-lending`, `crosschain-bridge`, `csigma-finance`, `cub-finance`, `curve-dex`, `curve-llamalend`, `cytonic-airdrop-campaign`, `ddex`, `debridge`, `defil`, `dforce-lending`, `dopple-finance`, `dtrinity-dlend`, `enosys-bridge`, `ether.fi-liquid`, `ezmoney`, `finnexus`, `flux-finance`, `flying-tulip-lend`, `fuji-v1`, `fungify`, `gaib`, `gauntlet`, `gearbox`, `goldsand-by-inshallah`, `goplus-locker-v2`, `granary-finance`, `gravita-protocol`, `grizzlyfi-hives`, `gro`, `horizon-protocol`, `hundred-finance`, `ideamarket`, `idle`, `impermax-v2`, `impossible`, `infinite-trading-protocol`, `insurace`, `iron-bank`, `iziswap`, `izumi-liquidbox`, `joe-v2`, `kine-finance`, `kokonut-swap`, `kyberswap-classic`, `landx-finance`, `likwid`, `lista-cdp`, `listapie`, `liveart`, `lixir-finance`, `lockon`, `loop`, `lybra-v1`, `magic-eden`, `maverick-v1`, `midas-capital`, `mochifi`, `monolith-market`, `morpheusai`, `morpho-optimizer-aavev2`, `multichain`, `nftx`, `olive-network`, `openleverage`, `pell-network`, `pepeteam-bridge`, `percent-finance`, `picwe`, `piku-finance`, `planet-farm`, `pooltogether-v3`, `pooltogether-v4`, `premia-v2`, `preon-finance`, `prismalst`, `privacy-pools`, `pstake-lsd`, `qidao`, `radiant-v2`, `radioshack`, `rari-capital`, `revest-finance`, `rubicon`, `saddle-finance`, `satlayer`, `segment-finance`, `sentora`, `set-protocol`, `shift-protocol`, `shimmerbridge`, `silo-v2`, `single-finance`, `singularitydao`, `sir`, `sofa.org`, `spectra-v1`, `sperax-usd`, `stabull-finance`, `stake-dao`, `stargate-v1`, `stonedefi`, `strata-season-0`, `sturdy-v2`, `sumer.money`, `synapse-cross-chain-bridge`, `synfutures-v1`, `tarot`, `termfinance-vaults`, `tetu-earn`, `the-idols`, `theoriq-alphavault-eth`, `tranchess-yield`, `twindex`, `uwu-lend`, `valuedefi`, `vaultcraft`, `velvet-v2`, `velvet-v3`, `venombridge`, `venus-core-pool`, `wasabix`, `wavesbridge`, `wepiggy`, `wombex-finance`, `wompie`, `xgld`, `xwin-finance`, `yala`, `yaxis`, `yieldflow-yield-farming`, `yieldwolf`, `zunami-protocol`

</details>

### Repeat victims in this list

Whatever allowed a second incident has not necessarily been removed. These are the highest-conviction entries in the set.

| Protocol | Hacks | Family | Priority | At risk |
|---|---:|---|---:|---:|
| [xToken](https://defillama.com/protocol/xtoken) | 2 | `AUTH-ZERO-ADDRESS-ACCEPTED` | 50.83 | $931,371 |

### Diversified shortlist — top 3 per family

| # | Protocol | Family | Priority | Likelihood | At risk | Evidence |
|---:|---|---|---:|---:|---:|---|
| 1 | [SMARDEX AMM](https://defillama.com/protocol/smardex-amm) | `ACC-QUOTE-STALE-ACROSS-OWN-SWAP` | 58.88 | 58.88 | $153,633 | `L4_GUARD_REVIEW` |
| 2 | [KyberSwap Elastic](https://defillama.com/protocol/kyberswap-elastic) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 57.23 | 57.23 | $127,719 | `L4_GUARD_REVIEW` |
| 3 | [MoneyFi](https://defillama.com/protocol/moneyfi) | `ACC-QUOTE-STALE-ACROSS-OWN-SWAP` | 54.47 | 54.47 | $117,775 | `L4_GUARD_REVIEW` |
| 4 | [Varen](https://defillama.com/protocol/varen) | `ACC-QUOTE-STALE-ACROSS-OWN-SWAP` | 53.82 | 53.82 | $135,783 | `L4_GUARD_REVIEW` |
| 5 | [basedbid](https://defillama.com/protocol/basedbid) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 51.42 | 51.42 | $59,576 | `L4_GUARD_REVIEW` |
| 6 | [De1](https://defillama.com/protocol/de1) | `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY` | 51.4 | 51.4 | $130,275 | `L3_STATE` |
| 7 | [SmartCredit](https://defillama.com/protocol/smartcredit) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 51.3 | 51.3 | $204,900 | `L4_GUARD_REVIEW` |
| 8 | [Krystal Community Vault](https://defillama.com/protocol/krystal-community-vault) | `ACC-DUPLICATE-ID-ACCUMULATION` | 51.18 | 51.18 | $229,978 | `L4_GUARD_REVIEW` |
| 9 | [xToken](https://defillama.com/protocol/xtoken) | `AUTH-ZERO-ADDRESS-ACCEPTED` | 50.83 | 50.83 | $931,371 | `L4_GUARD_REVIEW` |
| 10 | [Clipper](https://defillama.com/protocol/clipper) | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | 50.32 | 50.32 | $781,257 | `L4_GUARD_REVIEW` |
| 11 | [Antfarm finance](https://defillama.com/protocol/antfarm-finance) | `SIG-VERIFIER-DEFEATABLE` | 50.15 | 50.15 | $179,394 | `L4_GUARD_REVIEW` |
| 12 | [Astaria V2](https://defillama.com/protocol/astaria-v2) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 49.95 | 49.95 | $60,757 | `L4_GUARD_REVIEW` |
| 13 | [Yield Protocol](https://defillama.com/protocol/yield-protocol) | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 49.95 | 49.95 | $203,354 | `L4_GUARD_REVIEW` |
| 14 | [MIM Swap](https://defillama.com/protocol/mim-swap) | `AUTH-ZERO-ADDRESS-ACCEPTED` | 49.87 | 49.87 | $123,612 | `L4_GUARD_REVIEW` |
| 15 | [Derive V1](https://defillama.com/protocol/derive-v1) | `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY` | 49.82 | 49.82 | $134,673 | `L3_STATE` |
| 16 | [MYX Finance](https://defillama.com/protocol/myx-finance) | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 49.73 | 49.73 | $102,579 | `L4_GUARD_REVIEW` |
| 17 | [BitStable Finance](https://defillama.com/protocol/bitstable-finance) | `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY` | 49.72 | 49.72 | $57,986 | `L3_STATE` |
| 18 | [Deri Protocol](https://defillama.com/protocol/deri-protocol) | `ACC-DUPLICATE-ID-ACCUMULATION` | 49.4 | 49.4 | $309,264 | `L4_GUARD_REVIEW` |
| 19 | [OpenEden PRISM](https://defillama.com/protocol/openeden-prism) | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | 49.37 | 49.37 | $570,927 | `L4_GUARD_REVIEW` |
| 20 | [Domani Protocol](https://defillama.com/protocol/domani-protocol) | `ACC-DUPLICATE-ID-ACCUMULATION` | 48.98 | 48.98 | $111,093 | `L4_GUARD_REVIEW` |
| 21 | [unshETH](https://defillama.com/protocol/unsheth) | `ACC-HARDCODED-PEG-REDEMPTION` | 48.93 | 48.93 | $191,478 | `L4_GUARD_REVIEW` |
| 22 | [Resonate Finance](https://defillama.com/protocol/resonate-finance) | `AUTH-ZERO-ADDRESS-ACCEPTED` | 48.87 | 48.87 | $90,498 | `L4_GUARD_REVIEW` |
| 23 | [Arch](https://defillama.com/protocol/arch) | `SIG-VERIFIER-DEFEATABLE` | 48.23 | 48.23 | $119,539 | `L4_GUARD_REVIEW` |
| 24 | [Wasabi Perps](https://defillama.com/protocol/wasabi-perps) | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | 48.1 | 48.1 | $739,832 | `L3_STATE` |
| 25 | [Gyroscope Protocol](https://defillama.com/protocol/gyroscope-protocol) | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | 48.02 | 48.02 | $426,046 | `L4_GUARD_REVIEW` |
| 26 | [Juicebox V3](https://defillama.com/protocol/juicebox-v3) | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | 47.57 | 47.57 | $163,511 | `L3_STATE` |
| 27 | [Mesher](https://defillama.com/protocol/mesher) | `ACC-DONATION-UNACCOUNTED-BALANCE` | 47.42 | 47.42 | $298,882 | `L4_GUARD_REVIEW` |
| 28 | [IPOR Derivatives](https://defillama.com/protocol/ipor-derivatives) | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | 47.33 | 47.33 | $685,621 | `L3_STATE` |
| 29 | [Ammalgam DLEX](https://defillama.com/protocol/ammalgam-dlex) | `ACC-DONATION-UNACCOUNTED-BALANCE` | 47.08 | 47.08 | $62,650 | `L4_GUARD_REVIEW` |
| 30 | [MortgageFi](https://defillama.com/protocol/mortgagefi) | `SIG-VERIFIER-DEFEATABLE` | 46.98 | 46.98 | $990,527 | `L4_GUARD_REVIEW` |

---

### 1. SMARDEX AMM  —  `ACC-QUOTE-STALE-ACROSS-OWN-SWAP`

- **Rank (Ranking A — priority (likelihood × actionability)):** 1
- **Protocol:** SMARDEX AMM (`smardex-amm`) · Dexs · Ethereum, Arbitrum, Binance, Base, Polygon
- **DefiLlama:** https://defillama.com/protocol/smardex-amm
- **PRIORITY 58.88**  =  LIKELIHOOD 58.88 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 21.98/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $153,633 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A value used for minting, crediting or reward must be derived from what the protocol actually received, not from a quote taken before the protocol itself moved the market. Where the protocol's own action changes the price it just read, the value must be recomputed after the fact.
    - Deployed source (`SmardexFactory` @ 0x41A00e3F…(arbitrum), `SmardexRouter` @ 0xdd4536dD…(arbitrum)): prerequisites matched: quote_then_own_swap; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): referral_reward_with_mint=no
    - deployed source read for SmardexFactory@0x41A00e3F…(arbitrum), SmardexRouter@0xdd4536dD…(arbitrum); indicators matched: quote_then_own_swap
- **Preconditions PRESENT / UNKNOWN:** src::quote_then_own_swap, live_value_present, deployment_reachable_on_chain / src::quote_then_addliquidity
- **Guards searched / found:** lp_delta_measured, twap_or_feed_for_accounting / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** The minted amount is derived from the LP balance delta or from a TWAP (kills the pair); The protocol's swap is bounded so it cannot move reserves materially; Rewards settle in a later block against re-measured backing
- **Where to start:** On a fork, run the bonding path with a flash-funded swap sized to skew the pair, then assert that the minted or credited amount tracks the LP tokens actually received rather than the pre-swap quote.
- **Evidence:** `protocols/deep_screened.jsonl#smardex-amm|ACC-QUOTE-STALE-ACROSS-OWN-SWAP`, `protocols/onchain_probes.json#smardex-amm`
- **Disclosure:** https://smardex.io · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol):  https://smardex.io/audit-reports

### 2. KyberSwap Elastic  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 2
- **Protocol:** KyberSwap Elastic (`kyberswap-elastic`) · Dexs · Linea, Scroll, Arbitrum, Optimism, Polygon, Ethereum …
- **DefiLlama:** https://defillama.com/protocol/kyberswap-elastic
- **PRIORITY 57.23**  =  LIKELIHOOD 57.23 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 20.33/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $127,719 · **Band:** `IN_BAND`
- **Previously hacked:** 2023-11-22 for $48,000,000 [Rounding Error]
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`AToken` @ 0x88ef6bef…(arbitrum), `MetaAggregationRouterV2` @ 0x6131b5fa…(arbitrum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for AToken@0x88ef6bef…(arbitrum), MetaAggregationRouterV2@0x6131b5fa…(arbitrum); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `KNOWN_ISSUE_DEPLOYMENT_STATUS_UNKNOWN` — DefiLlama's hacks dataset records 1 prior on-chain incident(s) on this protocol, most recently 2023-11-22 for $48,000,000 [Rounding Error]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#kyberswap-elastic|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#kyberswap-elastic`
- **Disclosure:** https://kyberswap.com/#/swap · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://chainsecurity.com/security-audit/kyber-network-dynamic-market-maker-dmm/

### 3. MoneyFi  —  `ACC-QUOTE-STALE-ACROSS-OWN-SWAP`

- **Rank (Ranking A — priority (likelihood × actionability)):** 3
- **Protocol:** MoneyFi (`moneyfi`) · Yield Aggregator · Aptos, Base, Binance, CORE, Soneium, Optimism …
- **DefiLlama:** https://defillama.com/protocol/moneyfi
- **PRIORITY 54.47**  =  LIKELIHOOD 54.47 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 17.57/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $117,775 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
- **Broken invariant tested:** A value used for minting, crediting or reward must be derived from what the protocol actually received, not from a quote taken before the protocol itself moved the market. Where the protocol's own action changes the price it just read, the value must be recomputed after the fact.
    - Deployed source (`TetherTokenOFTExtension` @ 0x9895d81b…(base), `MoneyFiCrossChainRouter` @ 0xd9535326…(base)): prerequisites matched: quote_then_own_swap; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): referral_reward_with_mint=yes
    - deployed source read for TetherTokenOFTExtension@0x9895d81b…(base), MoneyFiCrossChainRouter@0xd9535326…(base); indicators matched: quote_then_own_swap, referral_reward_with_mint
- **Preconditions PRESENT / UNKNOWN:** src::quote_then_own_swap, live_value_present, deployment_reachable_on_chain / src::quote_then_addliquidity
- **Guards searched / found:** lp_delta_measured, twap_or_feed_for_accounting / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** The minted amount is derived from the LP balance delta or from a TWAP (kills the pair); The protocol's swap is bounded so it cannot move reserves materially; Rewards settle in a later block against re-measured backing
- **Where to start:** On a fork, run the bonding path with a flash-funded swap sized to skew the pair, then assert that the minted or credited amount tracks the LP tokens actually received rather than the pre-swap quote.
- **Evidence:** `protocols/deep_screened.jsonl#moneyfi|ACC-QUOTE-STALE-ACROSS-OWN-SWAP`, `protocols/onchain_probes.json#moneyfi`
- **Disclosure:** https://app.moneyfi.fund/ · no audit link listed

### 4. Varen  —  `ACC-QUOTE-STALE-ACROSS-OWN-SWAP`

- **Rank (Ranking A — priority (likelihood × actionability)):** 4
- **Protocol:** Varen (`varen`) · Dexs · Ethereum
- **DefiLlama:** https://defillama.com/protocol/varen
- **PRIORITY 53.82**  =  LIKELIHOOD 53.82 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 16.92/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $135,783 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A value used for minting, crediting or reward must be derived from what the protocol actually received, not from a quote taken before the protocol itself moved the market. Where the protocol's own action changes the price it just read, the value must be recomputed after the fact.
    - Deployed source (`StakingRewards` @ 0x25a25e2f…(ethereum), `LinkswapFactory` @ 0x696708db…(ethereum)): prerequisites matched: quote_then_own_swap; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): referral_reward_with_mint=no
    - deployed source read for StakingRewards@0x25a25e2f…(ethereum), LinkswapFactory@0x696708db…(ethereum); indicators matched: quote_then_own_swap
- **Preconditions PRESENT / UNKNOWN:** src::quote_then_own_swap, live_value_present, deployment_reachable_on_chain / src::quote_then_addliquidity
- **Guards searched / found:** lp_delta_measured, twap_or_feed_for_accounting / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** The minted amount is derived from the LP balance delta or from a TWAP (kills the pair); The protocol's swap is bounded so it cannot move reserves materially; Rewards settle in a later block against re-measured backing
- **Where to start:** On a fork, run the bonding path with a flash-funded swap sized to skew the pair, then assert that the minted or credited amount tracks the LP tokens actually received rather than the pre-swap quote.
- **Evidence:** `protocols/deep_screened.jsonl#varen|ACC-QUOTE-STALE-ACROSS-OWN-SWAP`, `protocols/onchain_probes.json#varen`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://certificate.quantstamp.com/full/linkswap

### 5. Elk  —  `ACC-QUOTE-STALE-ACROSS-OWN-SWAP`

- **Rank (Ranking A — priority (likelihood × actionability)):** 5
- **Protocol:** Elk (`elk`) · Dexs · Binance, Avalanche, Kucoin, xDai, Polygon, Arbitrum …
- **DefiLlama:** https://defillama.com/protocol/elk
- **PRIORITY 52.45**  =  LIKELIHOOD 52.45 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 15.55/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $160,743 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A value used for minting, crediting or reward must be derived from what the protocol actually received, not from a quote taken before the protocol itself moved the market. Where the protocol's own action changes the price it just read, the value must be recomputed after the fact.
    - Deployed source (`ElkFactory` @ 0x31aFfd87…(bsc)): prerequisites matched: quote_then_own_swap; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): referral_reward_with_mint=no
    - deployed source read for ElkFactory@0x31aFfd87…(bsc); indicators matched: quote_then_own_swap
- **Preconditions PRESENT / UNKNOWN:** src::quote_then_own_swap, live_value_present, deployment_reachable_on_chain / src::quote_then_addliquidity
- **Guards searched / found:** lp_delta_measured, twap_or_feed_for_accounting / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** The minted amount is derived from the LP balance delta or from a TWAP (kills the pair); The protocol's swap is bounded so it cannot move reserves materially; Rewards settle in a later block against re-measured backing
- **Where to start:** On a fork, run the bonding path with a flash-funded swap sized to skew the pair, then assert that the minted or credited amount tracks the LP tokens actually received rather than the pre-swap quote.
- **Evidence:** `protocols/deep_screened.jsonl#elk|ACC-QUOTE-STALE-ACROSS-OWN-SWAP`, `protocols/onchain_probes.json#elk`
- **Disclosure:** https://elk.finance · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://blog.hashex.org/elk-finance-smart-contracts-audit-report-a18deaa5890b

### 6. SectorOne DLMM  —  `ACC-QUOTE-STALE-ACROSS-OWN-SWAP`

- **Rank (Ranking A — priority (likelihood × actionability)):** 6
- **Protocol:** SectorOne DLMM (`sectorone-dlmm`) · Dexs · Robinhood Chain, Base, MegaETH, Ethereum
- **DefiLlama:** https://defillama.com/protocol/sectorone-dlmm
- **PRIORITY 51.82**  =  LIKELIHOOD 51.82 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 14.92/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $253,917 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
- **Broken invariant tested:** A value used for minting, crediting or reward must be derived from what the protocol actually received, not from a quote taken before the protocol itself moved the market. Where the protocol's own action changes the price it just read, the value must be recomputed after the fact.
    - Deployed source (`LBFactory` @ 0x20918F4B…(base), `TransparentUpgradeableProxy` @ 0x304BaEB3…(base)): prerequisites matched: quote_then_own_swap; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): referral_reward_with_mint=no
    - deployed source read for LBFactory@0x20918F4B…(base), TransparentUpgradeableProxy@0x304BaEB3…(base); indicators matched: quote_then_own_swap
- **Preconditions PRESENT / UNKNOWN:** src::quote_then_own_swap, live_value_present, deployment_reachable_on_chain / src::quote_then_addliquidity
- **Guards searched / found:** lp_delta_measured, twap_or_feed_for_accounting / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `EOA_SINGLE_KEY`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** The minted amount is derived from the LP balance delta or from a TWAP (kills the pair); The protocol's swap is bounded so it cannot move reserves materially; Rewards settle in a later block against re-measured backing
- **Where to start:** On a fork, run the bonding path with a flash-funded swap sized to skew the pair, then assert that the minted or credited amount tracks the LP tokens actually received rather than the pre-swap quote.
- **Evidence:** `protocols/deep_screened.jsonl#sectorone-dlmm|ACC-QUOTE-STALE-ACROSS-OWN-SWAP`, `protocols/onchain_probes.json#sectorone-dlmm`
- **Disclosure:** https://sectorone.xyz · no audit link listed

### 7. Hunny Finance  —  `ACC-QUOTE-STALE-ACROSS-OWN-SWAP`

- **Rank (Ranking A — priority (likelihood × actionability)):** 7
- **Protocol:** Hunny Finance (`hunny-finance`) · Yield · Binance
- **DefiLlama:** https://defillama.com/protocol/hunny-finance
- **PRIORITY 51.75**  =  LIKELIHOOD 51.75 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 14.85/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $528,141 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A value used for minting, crediting or reward must be derived from what the protocol actually received, not from a quote taken before the protocol itself moved the market. Where the protocol's own action changes the price it just read, the value must be recomputed after the fact.
    - Deployed source (`CakeFlipVault` @ 0x12180BB3…(bsc), `VaultHunny` @ 0x09fd83e5…(bsc)): prerequisites matched: quote_then_own_swap; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): referral_reward_with_mint=no
    - deployed source read for CakeFlipVault@0x12180BB3…(bsc), VaultHunny@0x09fd83e5…(bsc); indicators matched: quote_then_own_swap
- **Preconditions PRESENT / UNKNOWN:** src::quote_then_own_swap, live_value_present, deployment_reachable_on_chain / src::quote_then_addliquidity
- **Guards searched / found:** lp_delta_measured, twap_or_feed_for_accounting / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** The minted amount is derived from the LP balance delta or from a TWAP (kills the pair); The protocol's swap is bounded so it cannot move reserves materially; Rewards settle in a later block against re-measured backing
- **Where to start:** On a fork, run the bonding path with a flash-funded swap sized to skew the pair, then assert that the minted or credited amount tracks the LP tokens actually received rather than the pre-swap quote.
- **Evidence:** `protocols/deep_screened.jsonl#hunny-finance|ACC-QUOTE-STALE-ACROSS-OWN-SWAP`, `protocols/onchain_probes.json#hunny-finance`
- **Disclosure:** https://hunny.finance · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://www.certik.org/projects/pancakehunny

### 8. basedbid  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking A — priority (likelihood × actionability)):** 8
- **Protocol:** basedbid (`basedbid`) · Launchpad · Robinhood Chain, Solana, Base, Binance, Ethereum, MegaETH
- **DefiLlama:** https://defillama.com/protocol/basedbid
- **PRIORITY 51.42**  =  LIKELIHOOD 51.42 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 14.52/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $59,576 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
- **Broken invariant tested:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source (`NonfungiblePositionManager` @ 0x03a520b3…(base), `NonfungiblePositionManager` @ 0x46A15B0b…(base)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for NonfungiblePositionManager@0x03a520b3…(base), NonfungiblePositionManager@0x46A15B0b…(base); indicators matched: unsafe_cross_sign_cast
- **Preconditions PRESENT / UNKNOWN:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** safecast_used / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#basedbid|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#basedbid`
- **Disclosure:**   · no audit link listed

### 9. De1  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 9
- **Protocol:** De1 (`de1`) · DEX Aggregator · Binance, Arbitrum, Avalanche, Ethereum, Polygon, Manta …
- **DefiLlama:** https://defillama.com/protocol/de1
- **PRIORITY 51.4**  =  LIKELIHOOD 51.4 × ACTIONABILITY 100.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 25.0/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $130,275 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `unverified_implementation` — raises likelihood, measured lift ×2.062 (weight +0.72)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - Conditions: `REBRANDED_DEPLOYMENT`, `MULTICHAIN_VERSION_DRIFT`
    - condition REBRANDED_DEPLOYMENT (PRIORITY): Operated under previous names, so contracts deployed under the old identity may still be live and unwatched.
    - condition MULTICHAIN_VERSION_DRIFT (PRIORITY): Deployed across many chains, where per-chain deployments drift and the least-watched chain sets the risk.
    - 6 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** prior_version_still_callable, still_holds_value_or_authority / unmaintained_or_differing_code_path, not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **one externally-owned account** (`EOA_SINGLE_KEY`) — a code fix here does not remove that exposure, and it is the cheaper thing to raise first
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#de1|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#de1`
- **Disclosure:** https://app.de1.exchange/swap/eth/ETH/USDT · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.openocean.finance/protocol/introduction/security-and-audits

### 10. Landshare  —  `ACC-QUOTE-STALE-ACROSS-OWN-SWAP`

- **Rank (Ranking A — priority (likelihood × actionability)):** 10
- **Protocol:** Landshare (`landshare`) · RWA · Binance
- **DefiLlama:** https://defillama.com/protocol/landshare
- **PRIORITY 51.38**  =  LIKELIHOOD 51.38 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 14.48/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $621,293 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A value used for minting, crediting or reward must be derived from what the protocol actually received, not from a quote taken before the protocol itself moved the market. Where the protocol's own action changes the price it just read, the value must be recomputed after the fact.
    - Deployed source (`PancakePair` @ 0x13f80c53…(bsc), `MasterChef` @ 0x3f945889…(bsc)): prerequisites matched: quote_then_own_swap; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): referral_reward_with_mint=no
    - deployed source read for PancakePair@0x13f80c53…(bsc), MasterChef@0x3f945889…(bsc); indicators matched: quote_then_own_swap
- **Preconditions PRESENT / UNKNOWN:** src::quote_then_own_swap, live_value_present, deployment_reachable_on_chain / src::quote_then_addliquidity
- **Guards searched / found:** lp_delta_measured, twap_or_feed_for_accounting / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** The minted amount is derived from the LP balance delta or from a TWAP (kills the pair); The protocol's swap is bounded so it cannot move reserves materially; Rewards settle in a later block against re-measured backing
- **Where to start:** On a fork, run the bonding path with a flash-funded swap sized to skew the pair, then assert that the minted or credited amount tracks the LP tokens actually received rather than the pre-swap quote.
- **Evidence:** `protocols/deep_screened.jsonl#landshare|ACC-QUOTE-STALE-ACROSS-OWN-SWAP`, `protocols/onchain_probes.json#landshare`
- **Disclosure:** https://landshare.io · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://landshare.io/wp-content/uploads/2022/06/Audit.pdf

### 11. SmartCredit  —  `ORACLE-SPOT-THIN-LIQUIDITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 11
- **Protocol:** SmartCredit (`smartcredit`) · Lending · Ethereum
- **DefiLlama:** https://defillama.com/protocol/smartcredit
- **PRIORITY 51.3**  =  LIKELIHOOD 51.3 × ACTIONABILITY 100.0%
    - likelihood = family evidence 30.0/50 (MATCH 60 × evidence weight 1.0) + learned attack surface 21.3/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $204,900 · **Band:** `IN_BAND`
- **Previously hacked:** 2026-05-04 for $72,000 [Unknown]
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 60 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `unverified_implementation` — raises likelihood, measured lift ×2.062 (weight +0.72)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Borrowing capacity, mint size, reward size or collateral value must not be derived from a price that a single actor can move within the manipulation window, and the value unlocked must never exceed the cost of moving that price.
    - Conditions: `PRICING_SURFACE_UNDECLARED`
    - Deployed source (`ReputationToken` @ 0x22165777…(ethereum)): prerequisites matched: spot_without_twap; no guard found
    - deployed source read for ReputationToken@0x22165777…(ethereum); indicators matched: spot_without_twap
    - 1 implementation(s) behind a proxy are NOT verified on the explorer: implementation identity unresolved, score capped at 60
    - condition PRICING_SURFACE_UNDECLARED (PRIORITY): A lending, CDP, derivatives or curation archetype with no oracle declared at all: the pricing path is unmapped.
- **Preconditions PRESENT / UNKNOWN:** src::spot_without_twap, value_decision_reads_configured_feed, live_positions_exposed / feed_selection_is_configuration
- **Guards searched / found:** twap_present, supply_cap_present, deviation_bound_vs_independent_source / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **one externally-owned account** (`EOA_SINGLE_KEY`) — a code fix here does not remove that exposure, and it is the cheaper thing to raise first
- **Prior art:** `KNOWN_ISSUE_DEPLOYMENT_STATUS_UNKNOWN` — DefiLlama's hacks dataset records 1 prior on-chain incident(s) on this protocol, most recently 2026-05-04 for $72,000 [Unknown]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** All collateral priced by a deep aggregated feed with a deviation cap (kills the pair); Caps are set from measured venue depth and enforced on-chain; The action is sized from realised transfer amounts, so price is never an input
- **Where to start:** On a fork, execute a max-size flash-funded swap against every venue in the pricing path and assert that no value-bearing entrypoint changes its output beyond the configured deviation bound.
- **Evidence:** `protocols/deep_screened.jsonl#smartcredit|ORACLE-SPOT-THIN-LIQUIDITY`, `protocols/onchain_probes.json#smartcredit`
- **Disclosure:** https://smartcredit.io · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/pessimistic-io/audits/blob/ca048cb8eaba4f7959fb83c1c6f5cb4803c85718/SmartCredit%20Security%20Analysis%20by%20Pessimistic.pdf

### 12. Krystal Community Vault  —  `ACC-DUPLICATE-ID-ACCUMULATION`

- **Rank (Ranking A — priority (likelihood × actionability)):** 12
- **Protocol:** Krystal Community Vault (`krystal-community-vault`) · Liquidity Manager · Base, Polygon, Hyperliquid L1, Arbitrum, Binance, Ethereum
- **DefiLlama:** https://defillama.com/protocol/krystal-community-vault
- **PRIORITY 51.18**  =  LIKELIHOOD 51.18 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 19.28/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $229,978 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
- **Broken invariant tested:** An entitlement attached to an identifier may be counted at most once per period. A caller-supplied ID list must be deduplicated, or each ID's claim state consumed before the next read.
    - Deployed source (`SharedVaultFactory` @ 0xefdf2e68…(arbitrum)): prerequisites matched: id_array_loop_without_dedup; no guard found
    - deployed source read for SharedVaultFactory@0xefdf2e68…(arbitrum); indicators matched: id_array_loop_without_dedup
- **Preconditions PRESENT / UNKNOWN:** src::id_array_loop_without_dedup, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Consumed marker written inside the loop (kills the pair); IDs required strictly increasing
- **Where to start:** On a fork, call the batch function with one ID repeated k times; payout must equal the single-ID payout.
- **Evidence:** `protocols/deep_screened.jsonl#krystal-community-vault|ACC-DUPLICATE-ID-ACCUMULATION`, `protocols/onchain_probes.json#krystal-community-vault`
- **Disclosure:** https://krystal.app · no audit link listed

### 13. TreeDefi  —  `ACC-QUOTE-STALE-ACROSS-OWN-SWAP`

- **Rank (Ranking A — priority (likelihood × actionability)):** 13
- **Protocol:** TreeDefi (`treedefi`) · Yield · Binance
- **DefiLlama:** https://defillama.com/protocol/treedefi
- **PRIORITY 51.08**  =  LIKELIHOOD 51.08 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 14.18/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $71,298 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A value used for minting, crediting or reward must be derived from what the protocol actually received, not from a quote taken before the protocol itself moved the market. Where the protocol's own action changes the price it just read, the value must be recomputed after the fact.
    - Deployed source (`MeatToken` @ 0x00438AE9…(bsc), `MasterChef` @ 0x0283527f…(bsc)): prerequisites matched: quote_then_own_swap; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): referral_reward_with_mint=no
    - deployed source read for MeatToken@0x00438AE9…(bsc), MasterChef@0x0283527f…(bsc); indicators matched: quote_then_own_swap
- **Preconditions PRESENT / UNKNOWN:** src::quote_then_own_swap, live_value_present, deployment_reachable_on_chain / src::quote_then_addliquidity
- **Guards searched / found:** lp_delta_measured, twap_or_feed_for_accounting / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `EOA_SINGLE_KEY`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** The minted amount is derived from the LP balance delta or from a TWAP (kills the pair); The protocol's swap is bounded so it cannot move reserves materially; Rewards settle in a later block against re-measured backing
- **Where to start:** On a fork, run the bonding path with a flash-funded swap sized to skew the pair, then assert that the minted or credited amount tracks the LP tokens actually received rather than the pre-swap quote.
- **Evidence:** `protocols/deep_screened.jsonl#treedefi|ACC-QUOTE-STALE-ACROSS-OWN-SWAP`, `protocols/onchain_probes.json#treedefi`
- **Disclosure:** https://treedefi.com · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://www.certik.org/projects/treedefi

### 14. xToken  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 14
- **Protocol:** xToken (`xtoken`) · Liquidity Manager · Ethereum, Optimism, Arbitrum, Polygon
- **DefiLlama:** https://defillama.com/protocol/xtoken
- **PRIORITY 50.83**  =  LIKELIHOOD 50.83 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 18.93/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $931,371 · **Band:** `IN_BAND`
- **REPEAT VICTIM — 2 recorded hacks.** 
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`LMTerminalProxy` @ 0x090559D5…(ethereum), `XTKProxy` @ 0x7f3edcdd…(ethereum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for LMTerminalProxy@0x090559D5…(ethereum), XTKProxy@0x7f3edcdd…(ethereum); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#xtoken|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#xtoken`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/xtokenmarket/terminal-mining/tree/master/audits

### 15. Clipper  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 15
- **Protocol:** Clipper (`clipper`) · Dexs · Ethereum, Base, Optimism, Arbitrum, Polygon, Mantle …
- **DefiLlama:** https://defillama.com/protocol/clipper
- **PRIORITY 50.32**  =  LIKELIHOOD 50.32 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 18.42/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $781,257 · **Band:** `IN_BAND`
- **Previously hacked:** 2024-12-01 for $450,000 [Deposit Logic Flaw]
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`ClipperPool` @ 0xe82906b6…(ethereum), `SailToken` @ 0xd8f14600…(ethereum)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for ClipperPool@0xe82906b6…(ethereum), SailToken@0xd8f14600…(ethereum); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `KNOWN_ISSUE_DEPLOYMENT_STATUS_UNKNOWN` — DefiLlama's hacks dataset records 1 prior on-chain incident(s) on this protocol, most recently 2024-12-01 for $450,000 [Deposit Logic Flaw]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#clipper|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#clipper`
- **Disclosure:** https://clipper.exchange · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.clipper.exchange/audits

### 16. Antfarm finance  —  `SIG-VERIFIER-DEFEATABLE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 16
- **Protocol:** Antfarm finance (`antfarm-finance`) · Liquidity Manager · Ethereum, Arbitrum, Avalanche, Polygon zkEVM
- **DefiLlama:** https://defillama.com/protocol/antfarm-finance
- **PRIORITY 50.15**  =  LIKELIHOOD 50.15 × ACTIONABILITY 100.0%
    - likelihood = family evidence 30.0/50 (MATCH 60 × evidence weight 1.0) + learned attack surface 20.15/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $179,394 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 60 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `unverified_implementation` — raises likelihood, measured lift ×2.062 (weight +0.72)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A verification routine must reject malformed, empty or zero-recovered signatures, and must never treat address(0) as a match.
    - Deployed source (`AntfarmToken` @ 0x61f4ECD1…(ethereum)): prerequisites matched: ecrecover_without_zero_check; no guard found
    - deployed source read for AntfarmToken@0x61f4ECD1…(ethereum); indicators matched: ecrecover_without_zero_check
    - 1 implementation(s) behind a proxy are NOT verified on the explorer: implementation identity unresolved, score capped at 60
- **Preconditions PRESENT / UNKNOWN:** src::ecrecover_without_zero_check, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** uses_oz_ecdsa / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** OZ ECDSA library in the deployed bytecode (kills the ecrecover-zero shape); Signer address immutable and non-zero
- **Where to start:** On a fork, submit r=0,s=0,v=27 and an empty signature to every signature-gated entrypoint; all must revert.
- **Evidence:** `protocols/deep_screened.jsonl#antfarm-finance|SIG-VERIFIER-DEFEATABLE`, `protocols/onchain_probes.json#antfarm-finance`
- **Disclosure:** https://antfarm.finance · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://www.docdroid.net/MxzpjSg/antfarmfinance-11-smart-contract-audit-report-pdf

### 17. Astaria V2  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking A — priority (likelihood × actionability)):** 17
- **Protocol:** Astaria V2 (`astaria-v2`) · Lending · Base, Ethereum
- **DefiLlama:** https://defillama.com/protocol/astaria-v2
- **PRIORITY 49.95**  =  LIKELIHOOD 49.95 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 13.05/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $60,757 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source (`Custodian` @ 0x00000000…(ethereum)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for Custodian@0x00000000…(ethereum); indicators matched: unsafe_cross_sign_cast
- **Preconditions PRESENT / UNKNOWN:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** safecast_used / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#astaria-v2|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#astaria-v2`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.astaria.xyz/docs/smart-contracts/audits

### 18. Swapr V2  —  `ACC-QUOTE-STALE-ACROSS-OWN-SWAP`

- **Rank (Ranking A — priority (likelihood × actionability)):** 18
- **Protocol:** Swapr V2 (`swapr-v2`) · Dexs · xDai, Arbitrum, Ethereum
- **DefiLlama:** https://defillama.com/protocol/swapr-v2
- **PRIORITY 49.95**  =  LIKELIHOOD 49.95 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 13.05/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $335,996 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `version_sibling_legacy` — raises likelihood, measured lift ×1.699 (weight +0.53)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A value used for minting, crediting or reward must be derived from what the protocol actually received, not from a quote taken before the protocol itself moved the market. Where the protocol's own action changes the price it just read, the value must be recomputed after the fact.
    - Deployed source (`DXswapFactory` @ 0x359f20ad…(arbitrum)): prerequisites matched: quote_then_own_swap; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): referral_reward_with_mint=no
    - deployed source read for DXswapFactory@0x359f20ad…(arbitrum); indicators matched: quote_then_own_swap
- **Preconditions PRESENT / UNKNOWN:** src::quote_then_own_swap, live_value_present, deployment_reachable_on_chain / src::quote_then_addliquidity
- **Guards searched / found:** lp_delta_measured, twap_or_feed_for_accounting / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** The minted amount is derived from the LP balance delta or from a TWAP (kills the pair); The protocol's swap is bounded so it cannot move reserves materially; Rewards settle in a later block against re-measured backing
- **Where to start:** On a fork, run the bonding path with a flash-funded swap sized to skew the pair, then assert that the minted or credited amount tracks the LP tokens actually received rather than the pre-swap quote.
- **Evidence:** `protocols/deep_screened.jsonl#swapr-v2|ACC-QUOTE-STALE-ACROSS-OWN-SWAP`, `protocols/onchain_probes.json#swapr-v2`
- **Disclosure:** https://swapr.eth.link/#/swap · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://gateway.ipfs.io/ipfs/QmNspbn2dQgQMQ9uXkMc7Fjf12RUVVJTzB27ywGeLUXXdn

### 19. Yield Protocol  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking A — priority (likelihood × actionability)):** 19
- **Protocol:** Yield Protocol (`yield-protocol`) · Lending · Arbitrum, Ethereum
- **DefiLlama:** https://defillama.com/protocol/yield-protocol
- **PRIORITY 49.95**  =  LIKELIHOOD 49.95 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 13.05/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $203,354 · **Band:** `IN_BAND`
- **Previously hacked:** 2024-04-30 for $181,000 [Incorrect Share Accounting]
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source (`nProxy` @ 0x1344A36A…(ethereum), `Pool` @ 0x2e4B70D0…(ethereum)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for nProxy@0x1344A36A…(ethereum), Pool@0x2e4B70D0…(ethereum); indicators matched: unsafe_cross_sign_cast
- **Preconditions PRESENT / UNKNOWN:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** safecast_used / none in the reviewed path
- **Prior art:** `KNOWN_ISSUE_DEPLOYMENT_STATUS_UNKNOWN` — DefiLlama's hacks dataset records 1 prior on-chain incident(s) on this protocol, most recently 2024-04-30 for $181,000 [Incorrect Share Accounting]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#yield-protocol|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#yield-protocol`
- **Disclosure:** https://www.yo.xyz/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/trailofbits/publications/blob/master/reviews/YieldV2.pdf

### 20. MIM Swap  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 20
- **Protocol:** MIM Swap (`mim-swap`) · Dexs · Arbitrum, Blast, Kava, Nibiru, Ethereum
- **DefiLlama:** https://defillama.com/protocol/mim-swap
- **PRIORITY 49.87**  =  LIKELIHOOD 49.87 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 17.97/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $123,612 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`FooBar` @ 0x7Ad0e580…(arbitrum), `MagicLP` @ 0x2958db35…(arbitrum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for FooBar@0x7Ad0e580…(arbitrum), MagicLP@0x2958db35…(arbitrum); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#mim-swap|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#mim-swap`
- **Disclosure:** https://app.abracadabra.money/#/mim-swap · no audit link listed

### 21. Derive V1  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 21
- **Protocol:** Derive V1 (`derive-v1`) · Options · Ethereum, Arbitrum, Optimism
- **DefiLlama:** https://defillama.com/protocol/derive-v1
- **PRIORITY 49.82**  =  LIKELIHOOD 49.82 × ACTIONABILITY 100.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 23.42/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $134,673 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `version_sibling_legacy` — raises likelihood, measured lift ×1.699 (weight +0.53)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - Conditions: `VERSION_SIBLING_LEGACY`, `REBRANDED_DEPLOYMENT`
    - condition REBRANDED_DEPLOYMENT (PRIORITY): Operated under previous names, so contracts deployed under the old identity may still be live and unwatched.
    - condition VERSION_SIBLING_LEGACY (PRECOND): Shares a parent protocol with a higher-version sibling while still holding value: the classic sibling-deployment-retains-the-old-version shape.
    - 6 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** prior_version_still_callable, still_holds_value_or_authority / unmaintained_or_differing_code_path, not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#derive-v1|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#derive-v1`
- **Disclosure:** https://derive.xyz · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.lyra.finance/overview/audits

### 22. MYX Finance  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking A — priority (likelihood × actionability)):** 22
- **Protocol:** MYX Finance (`myx-finance`) · Derivatives · Linea, Binance, Arbitrum, Op_Bnb
- **DefiLlama:** https://defillama.com/protocol/myx-finance
- **PRIORITY 49.73**  =  LIKELIHOOD 49.73 × ACTIONABILITY 100.0%
    - likelihood = family evidence 30.0/50 (MATCH 60 × evidence weight 1.0) + learned attack surface 19.73/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $102,579 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 60 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `unverified_implementation` — raises likelihood, measured lift ×2.062 (weight +0.72)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
- **Broken invariant tested:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source (`StakerV2` @ 0x3984ac3a…(bsc)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for StakerV2@0x3984ac3a…(bsc); indicators matched: unsafe_cross_sign_cast
    - 1 implementation(s) behind a proxy are NOT verified on the explorer: implementation identity unresolved, score capped at 60
- **Preconditions PRESENT / UNKNOWN:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** safecast_used / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#myx-finance|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#myx-finance`
- **Disclosure:** https://app.myx.finance · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://1570067552-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHCv4CkXABCLemz93mpi7%2Fuploads%2FuhcjNXBHA9yHn3b49ibX%2FPeckShield-Audit-Report-MYX-v1.0.pdf?alt=media&token=0b011c50-cb83-432b-a37b-84fd88c3f5f9, https://1570067552-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHCv4CkXABCLemz93mpi7%2Fuploads%2FjSF3929CurPBEmPKgS1C%2FSlowMist%20Audit%20Report%20-%20MYX%20Protocol.pdf?alt=media&token=1000fd1e-f8b1-42dc-b95b-5aad70928c31

### 23. BitStable Finance  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 23
- **Protocol:** BitStable Finance (`bitstable-finance`) · CDP · BounceBit, Bitcoin, Binance, Ethereum
- **DefiLlama:** https://defillama.com/protocol/bitstable-finance
- **PRIORITY 49.72**  =  LIKELIHOOD 49.72 × ACTIONABILITY 100.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 23.32/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $57,986 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `unverified_implementation` — raises likelihood, measured lift ×2.062 (weight +0.72)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - 2 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** prior_version_still_callable, still_holds_value_or_authority, not_paused / unmaintained_or_differing_code_path
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#bitstable-finance|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#bitstable-finance`
- **Disclosure:** https://bitstable.finance · no audit link listed

### 24. Deri Protocol  —  `ACC-DUPLICATE-ID-ACCUMULATION`

- **Rank (Ranking A — priority (likelihood × actionability)):** 24
- **Protocol:** Deri Protocol (`deri-protocol`) · Options · Binance, Arbitrum, zkSync Era, Polygon
- **DefiLlama:** https://defillama.com/protocol/deri-protocol
- **PRIORITY 49.4**  =  LIKELIHOOD 49.4 × ACTIONABILITY 100.0%
    - likelihood = family evidence 30.0/50 (MATCH 60 × evidence weight 1.0) + learned attack surface 19.4/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $309,264 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 60 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `unverified_implementation` — raises likelihood, measured lift ×2.062 (weight +0.72)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** An entitlement attached to an identifier may be counted at most once per period. A caller-supplied ID list must be deduplicated, or each ID's claim state consumed before the next read.
    - Deployed source (`EverlastingOption` @ 0x08aD0E0b…(bsc)): prerequisites matched: id_array_loop_without_dedup; no guard found
    - deployed source read for EverlastingOption@0x08aD0E0b…(bsc); indicators matched: id_array_loop_without_dedup
    - 1 implementation(s) behind a proxy are NOT verified on the explorer: implementation identity unresolved, score capped at 60
- **Preconditions PRESENT / UNKNOWN:** src::id_array_loop_without_dedup, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Consumed marker written inside the loop (kills the pair); IDs required strictly increasing
- **Where to start:** On a fork, call the batch function with one ID repeated k times; payout must equal the single-ID payout.
- **Evidence:** `protocols/deep_screened.jsonl#deri-protocol|ACC-DUPLICATE-ID-ACCUMULATION`, `protocols/onchain_probes.json#deri-protocol`
- **Disclosure:** https://deri.io/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.deri.io/library/code-audits

### 25. Saffron Vaults  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 25
- **Protocol:** Saffron Vaults (`saffron-vaults`) · Yield · Robinhood Chain, Arbitrum, Ethereum, Binance, Base, Optimism …
- **DefiLlama:** https://defillama.com/protocol/saffron-vaults
- **PRIORITY 49.37**  =  LIKELIHOOD 49.37 × ACTIONABILITY 100.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 22.97/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $546,015 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - Conditions: `REBRANDED_DEPLOYMENT`, `MULTICHAIN_VERSION_DRIFT`
    - condition REBRANDED_DEPLOYMENT (PRIORITY): Operated under previous names, so contracts deployed under the old identity may still be live and unwatched.
    - condition MULTICHAIN_VERSION_DRIFT (PRIORITY): Deployed across many chains, where per-chain deployments drift and the least-watched chain sets the risk.
    - 1 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** prior_version_still_callable, still_holds_value_or_authority / unmaintained_or_differing_code_path, not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#saffron-vaults|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#saffron-vaults`
- **Disclosure:** https://saffron.finance · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.saffron.finance/security/audits

### 26. OpenEden PRISM  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 26
- **Protocol:** OpenEden PRISM (`openeden-prism`) · Onchain Capital Allocator · Ethereum
- **DefiLlama:** https://defillama.com/protocol/openeden-prism
- **PRIORITY 49.37**  =  LIKELIHOOD 49.37 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 17.47/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $570,927 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 84.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`Token` @ 0xfc76fdc4…(ethereum)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for Token@0xfc76fdc4…(ethereum); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#openeden-prism|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#openeden-prism`
- **Disclosure:** https://openeden.com/prism · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.openeden.com/prism/security-and-audit-reports

### 27. PadSwap  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 27
- **Protocol:** PadSwap (`padswap`) · Dexs · Binance, Moonriver, Moonbeam
- **DefiLlama:** https://defillama.com/protocol/padswap
- **PRIORITY 49.15**  =  LIKELIHOOD 49.15 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 12.25/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $102,443 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`Toad` @ 0x463e737d…(bsc), `PadFarmsV2` @ 0x4992df07…(bsc)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for Toad@0x463e737d…(bsc), PadFarmsV2@0x4992df07…(bsc); indicators matched: claim_without_eligibility_map
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `EOA_SINGLE_KEY`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#padswap|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#padswap`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://dapps.padswap.exchange/pad_audit_report.pdf, https://toad.network/toad_audit_report.pdf

### 28. PRDT  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 28
- **Protocol:** PRDT (`prdt`) · Prediction Market · Ethereum, Binance, Polygon, Arbitrum, Solana, Nibiru
- **DefiLlama:** https://defillama.com/protocol/prdt
- **PRIORITY 49.08**  =  LIKELIHOOD 49.08 × ACTIONABILITY 100.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 22.68/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $505,783 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `unverified_implementation` — raises likelihood, measured lift ×2.062 (weight +0.72)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
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
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#prdt|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#prdt`
- **Disclosure:** https://prdt.finance · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://www.certik.com/projects/prdt-finance

### 29. Nested  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 29
- **Protocol:** Nested (`nested`) · Indexes · Binance, Polygon, Optimism, Arbitrum, Ethereum, Avalanche
- **DefiLlama:** https://defillama.com/protocol/nested
- **PRIORITY 49.08**  =  LIKELIHOOD 49.08 × ACTIONABILITY 100.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 22.68/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $152,552 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `unverified_implementation` — raises likelihood, measured lift ×2.062 (weight +0.72)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - Conditions: `MULTICHAIN_VERSION_DRIFT`
    - condition MULTICHAIN_VERSION_DRIFT (PRIORITY): Deployed across many chains, where per-chain deployments drift and the least-watched chain sets the risk.
    - 4 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** prior_version_still_callable, still_holds_value_or_authority / unmaintained_or_differing_code_path, not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `TIMELOCK`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#nested|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#nested`
- **Disclosure:** https://nested.fi · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/NestedFinance/nested-core-lego/tree/master/audits

### 30. Geyser  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking A — priority (likelihood × actionability)):** 30
- **Protocol:** Geyser (`geyser`) · Yield · Ethereum, Polygon, Optimism
- **DefiLlama:** https://defillama.com/protocol/geyser
- **PRIORITY 49.07**  =  LIKELIHOOD 49.07 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 12.17/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $81,623 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
- **Broken invariant tested:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source (`PoolFactory` @ 0xc517a08a…(ethereum), `GeyserFactory` @ 0xcada3423…(ethereum)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for PoolFactory@0xc517a08a…(ethereum), GeyserFactory@0xcada3423…(ethereum); indicators matched: unsafe_cross_sign_cast
- **Preconditions PRESENT / UNKNOWN:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** safecast_used / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#geyser|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#geyser`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://resources.gysr.io/gysr_v1_audit_pessimistic.pdf, https://resources.gysr.io/gysr_v2_audit_certik.pdf

### 31. Orion Pools  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 31
- **Protocol:** Orion Pools (`orion-pools`) · Dexs · Binance, Ethereum, Polygon, Fantom
- **DefiLlama:** https://defillama.com/protocol/orion-pools
- **PRIORITY 49.03**  =  LIKELIHOOD 49.03 × ACTIONABILITY 100.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 22.63/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $274,685 · **Band:** `IN_BAND`
- **Previously hacked:** 2023-02-02 for $3,000,000 [Reentrancy]
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
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
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **one externally-owned account** (`EOA_SINGLE_KEY`) — a code fix here does not remove that exposure, and it is the cheaper thing to raise first
- **Prior art:** `KNOWN_ISSUE_DEPLOYMENT_STATUS_UNKNOWN` — DefiLlama's hacks dataset records 1 prior on-chain incident(s) on this protocol, most recently 2023-02-02 for $3,000,000 [Reentrancy]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#orion-pools|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#orion-pools`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://www.certik.org/projects/orionprotocol

### 32. Domani Protocol  —  `ACC-DUPLICATE-ID-ACCUMULATION`

- **Rank (Ranking A — priority (likelihood × actionability)):** 32
- **Protocol:** Domani Protocol (`domani-protocol`) · Indexes · Ethereum, zkSync Era, Avalanche
- **DefiLlama:** https://defillama.com/protocol/domani-protocol
- **PRIORITY 48.98**  =  LIKELIHOOD 48.98 × ACTIONABILITY 100.0%
    - likelihood = family evidence 30.0/50 (MATCH 60 × evidence weight 1.0) + learned attack surface 18.98/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $111,093 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 60 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `unverified_implementation` — raises likelihood, measured lift ×2.062 (weight +0.72)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** An entitlement attached to an identifier may be counted at most once per period. A caller-supplied ID list must be deduplicated, or each ID's claim state consumed before the next read.
    - Deployed source (`Controller` @ 0xE0CF093C…(ethereum)): prerequisites matched: id_array_loop_without_dedup; no guard found
    - deployed source read for Controller@0xE0CF093C…(ethereum); indicators matched: id_array_loop_without_dedup
    - 1 implementation(s) behind a proxy are NOT verified on the explorer: implementation identity unresolved, score capped at 60
- **Preconditions PRESENT / UNKNOWN:** src::id_array_loop_without_dedup, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Consumed marker written inside the loop (kills the pair); IDs required strictly increasing
- **Where to start:** On a fork, call the batch function with one ID repeated k times; payout must equal the single-ID payout.
- **Evidence:** `protocols/deep_screened.jsonl#domani-protocol|ACC-DUPLICATE-ID-ACCUMULATION`, `protocols/onchain_probes.json#domani-protocol`
- **Disclosure:** https://mementoblockchain.com/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.dextf.com/documentation/introduction/security-assessment-report

### 33. unshETH  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 33
- **Protocol:** unshETH (`unsheth`) · Indexes · Ethereum
- **DefiLlama:** https://defillama.com/protocol/unsheth
- **PRIORITY 48.93**  =  LIKELIHOOD 48.93 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 17.03/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $191,478 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`LSDVault` @ 0x51A80238…(ethereum), `LSDVault` @ 0xE76Ffee8…(ethereum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for LSDVault@0x51A80238…(ethereum), LSDVault@0xE76Ffee8…(ethereum); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `EOA_SINGLE_KEY`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#unsheth|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#unsheth`
- **Disclosure:** https://unsheth.xyz · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://skynet.certik.com/projects/unsheth

### 34. Resonate Finance  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 34
- **Protocol:** Resonate Finance (`resonate-finance`) · Yield · Optimism, Arbitrum, Ethereum, Polygon, Fantom
- **DefiLlama:** https://defillama.com/protocol/resonate-finance
- **PRIORITY 48.87**  =  LIKELIHOOD 48.87 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 16.97/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $90,498 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`Resonate` @ 0x80ca8476…(ethereum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for Resonate@0x80ca8476…(ethereum); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#resonate-finance|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#resonate-finance`
- **Disclosure:** https://resonate.finance · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.resonate.finance/resources/security-and-audits#zellic-audit-part-1, https://docs.resonate.finance/resources/security-and-audits#zellic-audit-part-2

### 35. Printr  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 35
- **Protocol:** Printr (`printr`) · Launchpad · Solana, Ethereum, Mantle, Monad, Binance, Base …
- **DefiLlama:** https://defillama.com/protocol/printr
- **PRIORITY 48.7**  =  LIKELIHOOD 48.7 × ACTIONABILITY 100.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 22.3/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $103,029 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `unverified_implementation` — raises likelihood, measured lift ×2.062 (weight +0.72)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - Conditions: `MULTICHAIN_VERSION_DRIFT`
    - condition MULTICHAIN_VERSION_DRIFT (PRIORITY): Deployed across many chains, where per-chain deployments drift and the least-watched chain sets the risk.
    - 1 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** prior_version_still_callable, still_holds_value_or_authority, not_paused / unmaintained_or_differing_code_path
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `EOA_SINGLE_KEY`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#printr|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#printr`
- **Disclosure:** https://www.printr.money/ · no audit link listed

### 36. UFarm Digital  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking A — priority (likelihood × actionability)):** 36
- **Protocol:** UFarm Digital (`ufarm-digital`) · Onchain Capital Allocator · Ethereum, Arbitrum
- **DefiLlama:** https://defillama.com/protocol/ufarm-digital
- **PRIORITY 48.52**  =  LIKELIHOOD 48.52 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 11.62/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $523,062 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source (`ERC1967Proxy` @ 0x46Df84E7…(arbitrum), `NonfungiblePositionManager` @ 0xc36442b4…(arbitrum)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for ERC1967Proxy@0x46Df84E7…(arbitrum), NonfungiblePositionManager@0xc36442b4…(arbitrum); indicators matched: unsafe_cross_sign_cast
- **Preconditions PRESENT / UNKNOWN:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** safecast_used / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#ufarm-digital|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#ufarm-digital`
- **Disclosure:** https://ufarm.digital · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/Decurity/audits/blob/master/UFarm/ufarm-audit-report-2023-1.1.pdf

### 37. Meter Passport  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 37
- **Protocol:** Meter Passport (`meter-passport`) · Bridge · Ethereum, Meter, Binance, Theta, Moonriver, Moonbeam …
- **DefiLlama:** https://defillama.com/protocol/meter-passport
- **PRIORITY 48.52**  =  LIKELIHOOD 48.52 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 16.62/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $805,895 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`TokenVault` @ 0x805c7ecb…(ethereum), `AdminUpgradeabilityProxy` @ 0xd46ba6d9…(ethereum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for TokenVault@0x805c7ecb…(ethereum), AdminUpgradeabilityProxy@0xd46ba6d9…(ethereum); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#meter-passport|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#meter-passport`
- **Disclosure:** https://passport.meter.io · no audit link listed

### 38. GammaSwap Open Interest  —  `ACC-QUOTE-STALE-ACROSS-OWN-SWAP`

- **Rank (Ranking A — priority (likelihood × actionability)):** 38
- **Protocol:** GammaSwap Open Interest (`gammaswap-open-interest`) · Options · Arbitrum, Base, Ethereum
- **DefiLlama:** https://defillama.com/protocol/gammaswap-open-interest
- **PRIORITY 48.35**  =  LIKELIHOOD 48.35 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 11.45/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $515,965 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A value used for minting, crediting or reward must be derived from what the protocol actually received, not from a quote taken before the protocol itself moved the market. Where the protocol's own action changes the price it just read, the value must be recomputed after the fact.
    - Deployed source (`DeltaSwapRouter02` @ 0x5fbe219e…(arbitrum), `DeltaSwapFactory` @ 0xcb85e122…(arbitrum)): prerequisites matched: quote_then_own_swap; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): referral_reward_with_mint=no
    - deployed source read for DeltaSwapRouter02@0x5fbe219e…(arbitrum), DeltaSwapFactory@0xcb85e122…(arbitrum); indicators matched: quote_then_own_swap
- **Preconditions PRESENT / UNKNOWN:** src::quote_then_own_swap, live_value_present, deployment_reachable_on_chain / src::quote_then_addliquidity
- **Guards searched / found:** lp_delta_measured, twap_or_feed_for_accounting / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `EOA_SINGLE_KEY`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** The minted amount is derived from the LP balance delta or from a TWAP (kills the pair); The protocol's swap is bounded so it cannot move reserves materially; Rewards settle in a later block against re-measured backing
- **Where to start:** On a fork, run the bonding path with a flash-funded swap sized to skew the pair, then assert that the minted or credited amount tracks the LP tokens actually received rather than the pre-swap quote.
- **Evidence:** `protocols/deep_screened.jsonl#gammaswap-open-interest|ACC-QUOTE-STALE-ACROSS-OWN-SWAP`, `protocols/onchain_probes.json#gammaswap-open-interest`
- **Disclosure:** https://app.gammaswap.com/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.gammaswap.com/more-info/audits

### 39. Arch  —  `SIG-VERIFIER-DEFEATABLE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 39
- **Protocol:** Arch (`arch`) · Indexes · Ethereum, Polygon
- **DefiLlama:** https://defillama.com/protocol/arch
- **PRIORITY 48.23**  =  LIKELIHOOD 48.23 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 11.33/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $119,539 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A verification routine must reject malformed, empty or zero-recovered signatures, and must never treat address(0) as a match.
    - Deployed source (`SetToken` @ 0x0d20e86a…(ethereum), `Chamber` @ 0x103bb3EB…(ethereum)): prerequisites matched: ecrecover_without_zero_check; no guard found
    - deployed source read for SetToken@0x0d20e86a…(ethereum), Chamber@0x103bb3EB…(ethereum); indicators matched: ecrecover_without_zero_check
- **Preconditions PRESENT / UNKNOWN:** src::ecrecover_without_zero_check, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** uses_oz_ecdsa / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** OZ ECDSA library in the deployed bytecode (kills the ecrecover-zero shape); Signer address immutable and non-zero
- **Where to start:** On a fork, submit r=0,s=0,v=27 and an empty signature to every signature-gated entrypoint; all must revert.
- **Evidence:** `protocols/deep_screened.jsonl#arch|SIG-VERIFIER-DEFEATABLE`, `protocols/onchain_probes.json#arch`
- **Disclosure:** https://www.arch.finance · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://arch-document.s3.amazonaws.com/Chambers-audit-report.pdf

### 40. Everything  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 40
- **Protocol:** Everything (`everything`) · Lending · Arbitrum, Ethereum, Base, Binance
- **DefiLlama:** https://defillama.com/protocol/everything
- **PRIORITY 48.12**  =  LIKELIHOOD 48.12 × ACTIONABILITY 100.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 21.72/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $567,238 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 69.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `unverified_implementation` — raises likelihood, measured lift ×2.062 (weight +0.72)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
- **Broken invariant tested:** After deployment, no caller may (re)establish ownership, admin, or implementation wiring. Initialization state must be provably consumed.
    - Deployed source (`ERC1967Proxy` @ 0xE7E7E741…(arbitrum)): no prerequisite matched; no guard found
    - RELEVANCE GATE: the contract(s) actually read (ERC1967Proxy) show no distinguishing indicator for this family, so they are probably not the contracts that implement it. Every source-derived signal is therefore UNKNOWN, including the absence of a guard: not finding a staleness check in a data-provider contract says nothing about the oracle.
    - 1/2 live proxies read a zero ERC-7201 Initializable slot (inconclusive alone: older OZ versions store the flag elsewhere)
- **Preconditions PRESENT / UNKNOWN:** upgradeable_architecture, initializer_flag_unset, live_value_or_approvals / none
- **Guards searched / found:** upgrade_timelocked / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Simulated re-initialization reverts (kills the pair); Contract is non-upgradeable and holds no approvals
- **Where to start:** Read the initialization slot on every live proxy/facet and simulate re-initialization from an unprivileged address; it must revert.
- **Evidence:** `protocols/deep_screened.jsonl#everything|UPGRADE-INITIALIZER-REACHABLE-LIVE`, `protocols/onchain_probes.json#everything`
- **Disclosure:** https://everything.inc/ · no audit link listed

### 41. Wasabi Perps  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 41
- **Protocol:** Wasabi Perps (`wasabi-perps`) · Derivatives · Base, Solana, Blast, Berachain, Ethereum
- **DefiLlama:** https://defillama.com/protocol/wasabi-perps
- **PRIORITY 48.1**  =  LIKELIHOOD 48.1 × ACTIONABILITY 100.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 21.7/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $739,832 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 69.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `unverified_implementation` — raises likelihood, measured lift ×2.062 (weight +0.72)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
- **Broken invariant tested:** After deployment, no caller may (re)establish ownership, admin, or implementation wiring. Initialization state must be provably consumed.
    - Deployed source (`ERC1967Proxy` @ 0x0da575D3…(base)): no prerequisite matched; no guard found
    - RELEVANCE GATE: the contract(s) actually read (ERC1967Proxy) show no distinguishing indicator for this family, so they are probably not the contracts that implement it. Every source-derived signal is therefore UNKNOWN, including the absence of a guard: not finding a staleness check in a data-provider contract says nothing about the oracle.
    - 1/2 live proxies read a zero ERC-7201 Initializable slot (inconclusive alone: older OZ versions store the flag elsewhere)
- **Preconditions PRESENT / UNKNOWN:** upgradeable_architecture, initializer_flag_unset, live_value_or_approvals / none
- **Guards searched / found:** upgrade_timelocked / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Simulated re-initialization reverts (kills the pair); Contract is non-upgradeable and holds no approvals
- **Where to start:** Read the initialization slot on every live proxy/facet and simulate re-initialization from an unprivileged address; it must revert.
- **Evidence:** `protocols/deep_screened.jsonl#wasabi-perps|UPGRADE-INITIALIZER-REACHABLE-LIVE`, `protocols/onchain_probes.json#wasabi-perps`
- **Disclosure:** https://app.wasabi.xyz · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://dkoda-public.s3.amazonaws.com/Narya.ai_Wasabi_Smart_Contract_Audit.pdf, https://dkoda-public.s3.amazonaws.com/Zellic_Wasabi_Smart_Contract_Audit.pdf

### 42. Solo Top  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 42
- **Protocol:** Solo Top (`solo-top`) · Yield · Binance, Polygon, OKExChain, Heco
- **DefiLlama:** https://defillama.com/protocol/solo-top
- **PRIORITY 48.1**  =  LIKELIHOOD 48.1 × ACTIONABILITY 100.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 21.7/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $928,246 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `unverified_implementation` — raises likelihood, measured lift ×2.062 (weight +0.72)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `owner_is_eoa` — raises likelihood, measured lift ×2.019 (weight +0.70)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - 1 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** prior_version_still_callable, still_holds_value_or_authority / unmaintained_or_differing_code_path, not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#solo-top|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#solo-top`
- **Disclosure:** https://solo.top · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://www.certik.com/projects/solotop

### 43. Clearpool Lending  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 43
- **Protocol:** Clearpool Lending (`clearpool-lending`) · Uncollateralized Lending · Base, Ethereum, Polygon, Optimism, Mantle, Avalanche …
- **DefiLlama:** https://defillama.com/protocol/clearpool-lending
- **PRIORITY 48.05**  =  LIKELIHOOD 48.05 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 16.15/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $257,221 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`CollectionFactory` @ 0x199A016F…(ethereum), `TransparentUpgradeableProxy` @ 0x629E39da…(ethereum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for CollectionFactory@0x199A016F…(ethereum), TransparentUpgradeableProxy@0x629E39da…(ethereum); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** the ERC-1967 upgrade authority terminates in **a contract not fingerprinted by this run** (`UNKNOWN_CONTRACT`)
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#clearpool-lending|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#clearpool-lending`
- **Disclosure:** https://clearpool.finance · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://www.certik.com/projects/clearpool, https://3929482601-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FhkiSI8bK3ThlypJ3jdEC%2Fuploads%2FOFonx1OQS6ni5lUsyiPx%2FClearpool%20Security%20Analysis%20by%20Pessimistic.pdf?alt=media&token=d584e7c3-993c-4ce4-8adf-6a2c77727ec2

### 44. Mellow Yield  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 44
- **Protocol:** Mellow Yield (`mellow-yield`) · Yield Aggregator · Ethereum, Polygon, Base, Polygon zkEVM
- **DefiLlama:** https://defillama.com/protocol/mellow-yield
- **PRIORITY 48.02**  =  LIKELIHOOD 48.02 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 16.12/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $98,934 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`VaultRegistry` @ 0xfd23f971…(ethereum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for VaultRegistry@0xfd23f971…(ethereum); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#mellow-yield|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#mellow-yield`
- **Disclosure:** https://mellow.finance · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/mellow-finance/mellow-audits

### 45. Gyroscope Protocol  —  `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

- **Rank (Ranking A — priority (likelihood × actionability)):** 45
- **Protocol:** Gyroscope Protocol (`gyroscope-protocol`) · Dexs · Sonic, Optimism, Polygon, xDai, Base, Arbitrum …
- **DefiLlama:** https://defillama.com/protocol/gyroscope-protocol
- **PRIORITY 48.02**  =  LIKELIHOOD 48.02 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 16.12/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $426,046 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
    - Deployed source (`WrappedBalancerPoolTokenFactory` @ 0x22625eED…(base), `GyroECLPPoolFactory` @ 0x5F684897…(base)): prerequisites matched: hook_zero_amount_unguarded; no guard found
    - deployed source read for WrappedBalancerPoolTokenFactory@0x22625eED…(base), GyroECLPPoolFactory@0x5F684897…(base); indicators matched: hook_zero_amount_unguarded
- **Preconditions PRESENT / UNKNOWN:** src::hook_zero_amount_unguarded, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Where to start:** On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.
- **Evidence:** `protocols/deep_screened.jsonl#gyroscope-protocol|HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`, `protocols/onchain_probes.json#gyroscope-protocol`
- **Disclosure:** https://app.gyro.finance/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.gyro.finance/gyroscope-protocol/audit-reports

### 46. Base Dollar  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking A — priority (likelihood × actionability)):** 46
- **Protocol:** Base Dollar (`base-dollar`) · CDP · Base
- **DefiLlama:** https://defillama.com/protocol/base-dollar
- **PRIORITY 47.88**  =  LIKELIHOOD 47.88 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 10.98/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $158,342 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source (`CollateralRegistry` @ 0x7551ebfc…(base)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for CollateralRegistry@0x7551ebfc…(base); indicators matched: unsafe_cross_sign_cast
- **Preconditions PRESENT / UNKNOWN:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** safecast_used / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#base-dollar|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#base-dollar`
- **Disclosure:** https://basedollar.org · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.basedollar.org/docs/technical-documentation/audits

### 47. Hashflow  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 47
- **Protocol:** Hashflow (`hashflow`) · DEX Aggregator · Ethereum, Arbitrum, Polygon, Binance, Avalanche, Optimism
- **DefiLlama:** https://defillama.com/protocol/hashflow
- **PRIORITY 47.57**  =  LIKELIHOOD 47.57 × ACTIONABILITY 100.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 21.17/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $263,708 · **Band:** `IN_BAND`
- **Previously hacked:** 2023-06-15 for $605,000 [Token Approval Abuse]
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `unverified_implementation` — raises likelihood, measured lift ×2.062 (weight +0.72)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - Conditions: `MULTICHAIN_VERSION_DRIFT`
    - condition MULTICHAIN_VERSION_DRIFT (PRIORITY): Deployed across many chains, where per-chain deployments drift and the least-watched chain sets the risk.
    - 2 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** prior_version_still_callable, still_holds_value_or_authority / unmaintained_or_differing_code_path, not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Prior art:** `KNOWN_ISSUE_DEPLOYMENT_STATUS_UNKNOWN` — DefiLlama's hacks dataset records 1 prior on-chain incident(s) on this protocol, most recently 2023-06-15 for $605,000 [Token Approval Abuse]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#hashflow|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#hashflow`
- **Disclosure:** https://www.hashflow.com · no audit link listed

### 48. Juicebox V3  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 48
- **Protocol:** Juicebox V3 (`juicebox-v3`) · Launchpad · Ethereum
- **DefiLlama:** https://defillama.com/protocol/juicebox-v3
- **PRIORITY 47.57**  =  LIKELIHOOD 47.57 × ACTIONABILITY 100.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 21.17/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $163,511 · **Band:** `IN_BAND`
- **Previously hacked:** 2026-04-20 for $52,000 [Missing Input Validation]
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 69.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** After deployment, no caller may (re)establish ownership, admin, or implementation wiring. Initialization state must be provably consumed.
    - Deployed source (`ZAMM` @ 0x00000000…(ethereum), `ZAMM` @ 0x00000000…(ethereum)): no prerequisite matched; no guard found
    - RELEVANCE GATE: the contract(s) actually read (ZAMM, ZAMM) show no distinguishing indicator for this family, so they are probably not the contracts that implement it. Every source-derived signal is therefore UNKNOWN, including the absence of a guard: not finding a staleness check in a data-provider contract says nothing about the oracle.
    - 2/2 live proxies read a zero ERC-7201 Initializable slot (inconclusive alone: older OZ versions store the flag elsewhere)
    - 1 proxy/proxies expose a non-zero owner()
- **Preconditions PRESENT / UNKNOWN:** upgradeable_architecture, initializer_flag_unset, live_value_or_approvals / none
- **Guards searched / found:** upgrade_timelocked / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `KNOWN_ISSUE_DEPLOYMENT_STATUS_UNKNOWN` — DefiLlama's hacks dataset records 1 prior on-chain incident(s) on this protocol, most recently 2026-04-20 for $52,000 [Missing Input Validation]. Whether the deployment in scope carries the fix is not established by read-only evidence.
- **Falsified by:** Simulated re-initialization reverts (kills the pair); Contract is non-upgradeable and holds no approvals
- **Where to start:** Read the initialization slot on every live proxy/facet and simulate re-initialization from an unprivileged address; it must revert.
- **Evidence:** `protocols/deep_screened.jsonl#juicebox-v3|UPGRADE-INITIALIZER-REACHABLE-LIVE`, `protocols/onchain_probes.json#juicebox-v3`
- **Disclosure:** https://juicebox.money/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://hackmd.io/@berndartmueller/2023-01-juice-v3-migration, https://code4rena.com/reports/2022-10-juicebox/

### 49. Ajna V2  —  `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 49
- **Protocol:** Ajna V2 (`ajna-v2`) · Lending · Ethereum, Arbitrum, Base, Rari, Optimism, Polygon …
- **DefiLlama:** https://defillama.com/protocol/ajna-v2
- **PRIORITY 47.47**  =  LIKELIHOOD 47.47 × ACTIONABILITY 100.0%
    - likelihood = family evidence 30.0/50 (MATCH 60 × evidence weight 1.0) + learned attack surface 17.47/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $449,783 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 60 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `unverified_implementation` — raises likelihood, measured lift ×2.062 (weight +0.72)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `age_1_3y` — lowers likelihood, measured lift ×0.514 (weight -0.67)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.
    - Deployed source (`PoolCommons` @ 0x1f172F88…(ethereum)): prerequisites matched: claim_without_eligibility_map; no guard found
    - deployed source read for PoolCommons@0x1f172F88…(ethereum); indicators matched: claim_without_eligibility_map
    - 1 implementation(s) behind a proxy are NOT verified on the explorer: implementation identity unresolved, score capped at 60
- **Preconditions PRESENT / UNKNOWN:** src::claim_without_eligibility_map, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** merkle_proof_gate / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Claim requires a proof or a populated entitlement mapping (kills the pair); Reserve holds zero balance
- **Where to start:** On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.
- **Evidence:** `protocols/deep_screened.jsonl#ajna-v2|AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`, `protocols/onchain_probes.json#ajna-v2`
- **Disclosure:** https://www.ajna.finance/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/ajna-finance/audits

### 50. CACHE.Gold  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 50
- **Protocol:** CACHE.Gold (`cache.gold`) · RWA · Ethereum
- **DefiLlama:** https://defillama.com/protocol/cache.gold
- **PRIORITY 47.47**  =  LIKELIHOOD 47.47 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 15.57/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $592,015 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`GoldGramConvertorPriceConsumer` @ 0x34BCe86E…(ethereum), `CacheGold` @ 0xf5238462…(ethereum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for GoldGramConvertorPriceConsumer@0x34BCe86E…(ethereum), CacheGold@0xf5238462…(ethereum); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `SAFE_M_OF_N`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#cache.gold|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#cache.gold`
- **Disclosure:** https://cache.gold/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/cache-token/docs/blob/master/CACHE_Gold_Audit_Zerotrust.pdf, https://github.com/cache-token/docs/blob/master/CACHE_Gold_CGT_Audit_Polygon_CertiK.pdf

### 51. Sablier Legacy  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 51
- **Protocol:** Sablier Legacy (`sablier-legacy`) · Payments · Ethereum, Polygon, Binance, Arbitrum, Ronin, Optimism …
- **DefiLlama:** https://defillama.com/protocol/sablier-legacy
- **PRIORITY 47.45**  =  LIKELIHOOD 47.45 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 15.55/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $518,378 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`Sablier` @ 0xA4fc3584…(ethereum), `Sablier` @ 0xCD18eAa1…(ethereum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for Sablier@0xA4fc3584…(ethereum), Sablier@0xCD18eAa1…(ethereum); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#sablier-legacy|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#sablier-legacy`
- **Disclosure:** https://legacy-recipient.sablier.com/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://certificate.quantstamp.com/full/sablier

### 52. Mesher  —  `ACC-DONATION-UNACCOUNTED-BALANCE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 52
- **Protocol:** Mesher (`mesher`) · Lending · Ethereum, Klaytn
- **DefiLlama:** https://defillama.com/protocol/mesher
- **PRIORITY 47.42**  =  LIKELIHOOD 47.42 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 15.52/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $298,882 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_oracle_declared` — raises likelihood, measured lift ×2.127 (weight +0.76)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** A share price, exchange rate or totalAssets must be a function of value the protocol accounted for on entry. Reading a raw balance makes any direct transfer into the accounting boundary an unpriced increase in every holder's claim.
    - Deployed source (`CErc20Immutable` @ 0x004c0908…(ethereum), `TransparentUpgradeableProxy` @ 0x02451015…(ethereum)): prerequisites matched: getCashPrior_balanceOf; no guard found
    - deployed source read for CErc20Immutable@0x004c0908…(ethereum), TransparentUpgradeableProxy@0x02451015…(ethereum); indicators matched: getCashPrior_balanceOf
- **Preconditions PRESENT / UNKNOWN:** src::getCashPrior_balanceOf, unprivileged_inbound_transfer_possible, live_value_exposed / src::totalAssets_reads_balanceOf
- **Guards searched / found:** internal_cash_counter / none in the reviewed path
- **Prior art:** `KNOWN_ISSUE_DEPLOYMENT_STATUS_UNKNOWN` — The Compound-fork donation vector is publicly documented and was raised in Venus's own Code4rena audit before the March 2026 exploit.
- **Falsified by:** totalAssets derived from an internal counter, not balanceOf (kills the pair); Rate is monotonic and rate-limited per block; Inbound transfers to the accounting boundary are rejected or swept to a reserve
- **Where to start:** On a fork, transfer an arbitrary amount of each counted asset directly into every accounting boundary; the share price, exchange rate and derived borrow power must not change.
- **Evidence:** `protocols/deep_screened.jsonl#mesher|ACC-DONATION-UNACCOUNTED-BALANCE`, `protocols/onchain_probes.json#mesher`
- **Disclosure:** https://center.mesher.io · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.donkey.fund/about/audit

### 53. Niob Finance  —  `ACC-QUOTE-STALE-ACROSS-OWN-SWAP`

- **Rank (Ranking A — priority (likelihood × actionability)):** 53
- **Protocol:** Niob Finance (`niob-finance`) · Dexs · Binance
- **DefiLlama:** https://defillama.com/protocol/niob-finance
- **PRIORITY 47.4**  =  LIKELIHOOD 47.4 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 10.5/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $111,461 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A value used for minting, crediting or reward must be derived from what the protocol actually received, not from a quote taken before the protocol itself moved the market. Where the protocol's own action changes the price it just read, the value must be recomputed after the fact.
    - Deployed source (`MeatToken` @ 0x00438AE9…(bsc), `MasterChef` @ 0x0283527f…(bsc)): prerequisites matched: quote_then_own_swap; no guard found
    - weak/ambiguous source indicators (ordering only, never scored): referral_reward_with_mint=no
    - deployed source read for MeatToken@0x00438AE9…(bsc), MasterChef@0x0283527f…(bsc); indicators matched: quote_then_own_swap
- **Preconditions PRESENT / UNKNOWN:** src::quote_then_own_swap, live_value_present, deployment_reachable_on_chain / src::quote_then_addliquidity
- **Guards searched / found:** lp_delta_measured, twap_or_feed_for_accounting / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `EOA_SINGLE_KEY`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** The minted amount is derived from the LP balance delta or from a TWAP (kills the pair); The protocol's swap is bounded so it cannot move reserves materially; Rewards settle in a later block against re-measured backing
- **Where to start:** On a fork, run the bonding path with a flash-funded swap sized to skew the pair, then assert that the minted or credited amount tracks the LP tokens actually received rather than the pre-swap quote.
- **Evidence:** `protocols/deep_screened.jsonl#niob-finance|ACC-QUOTE-STALE-ACROSS-OWN-SWAP`, `protocols/onchain_probes.json#niob-finance`
- **Disclosure:** https://niob.finance/ · no audit link listed

### 54. IPOR Derivatives  —  `UPGRADE-INITIALIZER-REACHABLE-LIVE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 54
- **Protocol:** IPOR Derivatives (`ipor-derivatives`) · Derivatives · Ethereum, Arbitrum, Base
- **DefiLlama:** https://defillama.com/protocol/ipor-derivatives
- **PRIORITY 47.33**  =  LIKELIHOOD 47.33 × ACTIONABILITY 100.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 20.93/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $685,621 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 69.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** After deployment, no caller may (re)establish ownership, admin, or implementation wiring. Initialization state must be provably consumed.
    - Deployed source (`AmmTreasury` @ 0x866d6c95…(ethereum), `AmmTreasury` @ 0xabcb3ad4…(ethereum)): no prerequisite matched; guards found: initializer_modifier_present
    - RELEVANCE GATE: the contract(s) actually read (AmmTreasury, AmmTreasury) show no distinguishing indicator for this family, so they are probably not the contracts that implement it. Every source-derived signal is therefore UNKNOWN, including the absence of a guard: not finding a staleness check in a data-provider contract says nothing about the oracle.
    - 3/3 live proxies read a zero ERC-7201 Initializable slot (inconclusive alone: older OZ versions store the flag elsewhere)
    - 3 proxy/proxies expose a non-zero owner()
- **Preconditions PRESENT / UNKNOWN:** upgradeable_architecture, initializer_flag_unset, live_value_or_approvals / none
- **Guards searched / found:** upgrade_timelocked / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Simulated re-initialization reverts (kills the pair); Contract is non-upgradeable and holds no approvals
- **Where to start:** Read the initialization slot on every live proxy/facet and simulate re-initialization from an unprivileged address; it must revert.
- **Evidence:** `protocols/deep_screened.jsonl#ipor-derivatives|UPGRADE-INITIALIZER-REACHABLE-LIVE`, `protocols/onchain_probes.json#ipor-derivatives`
- **Disclosure:** https://app.ipor.io/fusion?f=D0V4X4doim7oC8cTQZzAZXBOkbwaf · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://docs.ipor.io/audits

### 55. BabyDoge Bridge  —  `ACC-SIGN-OR-BOUND-CHECK-MISSING`

- **Rank (Ranking A — priority (likelihood × actionability)):** 55
- **Protocol:** BabyDoge Bridge (`babydoge-bridge`) · Bridge · Binance, TON, Base, Solana
- **DefiLlama:** https://defillama.com/protocol/babydoge-bridge
- **PRIORITY 47.32**  =  LIKELIHOOD 47.32 × ACTIONABILITY 100.0%
    - likelihood = family evidence 36.9/50 (MATCH 73.8 × evidence weight 1.0) + learned attack surface 10.42/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $620,408 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 73.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `no_audit_listed` — lowers likelihood, measured lift ×0.521 (weight -0.65)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
- **Broken invariant tested:** A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.
    - Deployed source (`BridgeAssist` @ 0x1d09d345…(bsc), `Vault` @ 0x58ecEF26…(bsc)): prerequisites matched: unsafe_cross_sign_cast; no guard found
    - deployed source read for BridgeAssist@0x1d09d345…(bsc), Vault@0x58ecEF26…(bsc); indicators matched: unsafe_cross_sign_cast
- **Preconditions PRESENT / UNKNOWN:** src::unsafe_cross_sign_cast, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** safecast_used / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** SafeCast used throughout and fees clamped at the setter (kills the pair); No signed arithmetic in the value path
- **Where to start:** Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.
- **Evidence:** `protocols/deep_screened.jsonl#babydoge-bridge|ACC-SIGN-OR-BOUND-CHECK-MISSING`, `protocols/onchain_probes.json#babydoge-bridge`
- **Disclosure:** https://bridge.babydoge.com/ · no audit link listed

### 56. SnowSwap  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 56
- **Protocol:** SnowSwap (`snowswap`) · Dexs · Polygon, Ethereum
- **DefiLlama:** https://defillama.com/protocol/snowswap
- **PRIORITY 47.28**  =  LIKELIHOOD 47.28 × ACTIONABILITY 100.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 20.88/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $79,240 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 77.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `owner_is_contract` — raises likelihood, measured lift ×4.297 (weight +1.46)
    - `is_proxy` — raises likelihood, measured lift ×2.601 (weight +0.96)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - Conditions: `DEAD_FRONTEND_FUNDED`
    - condition DEAD_FRONTEND_FUNDED (PRECOND): Front end is dead while contracts still hold value: nobody is watching the deployment that still holds funds.
    - 6 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** unmaintained_or_differing_code_path, prior_version_still_callable, still_holds_value_or_authority / not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `UNKNOWN_CONTRACT`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#snowswap|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#snowswap`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://hackmd.io/@9GUQpanJRF6cloQ0fwyPFw/r1_ctUuqv

### 57. Opium  —  `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

- **Rank (Ranking A — priority (likelihood × actionability)):** 57
- **Protocol:** Opium (`opium`) · Options · Ethereum, Polygon, Arbitrum, Binance
- **DefiLlama:** https://defillama.com/protocol/opium
- **PRIORITY 47.23**  =  LIKELIHOOD 47.23 × ACTIONABILITY 100.0%
    - likelihood = family evidence 26.4/50 (MATCH 60 × evidence weight 0.88) + learned attack surface 20.83/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $144,621 · **Band:** `IN_BAND`
- **Evidence level:** `L3_STATE` · MATCH 60 · CONFIDENCE 71.0
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `on_bsc` — raises likelihood, measured lift ×1.788 (weight +0.58)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
    - 1 address(es) still hold deployed code on-chain
- **Preconditions PRESENT / UNKNOWN:** prior_version_still_callable, still_holds_value_or_authority / unmaintained_or_differing_code_path, not_paused
- **Guards searched / found:** paused_and_drained, approvals_revoked / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Where to start:** For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.
- **Evidence:** `protocols/deep_screened.jsonl#opium|UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`, `protocols/onchain_probes.json#opium`
- **Disclosure:** https://app.opium.finance/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://blog.smartdec.net/opium-smart-contracts-security-analysis-4c1857cfd93f

### 58. Bella Protocol  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 58
- **Protocol:** Bella Protocol (`bella-protocol`) · Yield · Ethereum, Manta, Mantle, zkSync Era
- **DefiLlama:** https://defillama.com/protocol/bella-protocol
- **PRIORITY 47.22**  =  LIKELIHOOD 47.22 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 15.32/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $90,069 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `multichain_gt3` — raises likelihood, measured lift ×2.038 (weight +0.71)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `authority_addrs_beyond_tvl` — raises likelihood, measured lift ×1.664 (weight +0.51)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`bVault` @ 0x3fb6b07d…(ethereum), `TokenPool` @ 0x6731a6a2…(ethereum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for bVault@0x3fb6b07d…(ethereum), TokenPool@0x6731a6a2…(ethereum); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#bella-protocol|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#bella-protocol`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/peckshield/publications/blob/master/audit_reports/bella_audit_report_2020_48_en_1_0.pdf

### 59. Cover Protocol  —  `AUTH-ZERO-ADDRESS-ACCEPTED`

- **Rank (Ranking A — priority (likelihood × actionability)):** 59
- **Protocol:** Cover Protocol (`cover-protocol`) · Insurance · Ethereum
- **DefiLlama:** https://defillama.com/protocol/cover-protocol
- **PRIORITY 47.15**  =  LIKELIHOOD 47.15 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 15.25/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $808,743 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 85.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `has_governance` — raises likelihood, measured lift ×5.045 (weight +1.62)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `single_audit_only` — raises likelihood, measured lift ×1.613 (weight +0.48)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
    - Deployed source (`yDAI` @ 0x16de5909…(ethereum), `ProtocolFactory` @ 0xedfC81Bf…(ethereum)): prerequisites matched: owner_compare_without_nonzero; no guard found
    - deployed source read for yDAI@0x16de5909…(ethereum), ProtocolFactory@0xedfC81Bf…(ethereum); indicators matched: owner_compare_without_nonzero
- **Preconditions PRESENT / UNKNOWN:** src::owner_compare_without_nonzero, live_value_present, deployment_reachable_on_chain / none
- **Guards searched / found:** none / none in the reviewed path
- **Custody posture (scored separately, see `results/upgrade_authority_exposure.md`):** weakest privileged role reads as `EOA_SINGLE_KEY`; no ERC-1967 admin chain was proven
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Where to start:** Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.
- **Evidence:** `protocols/deep_screened.jsonl#cover-protocol|AUTH-ZERO-ADDRESS-ACCEPTED`, `protocols/onchain_probes.json#cover-protocol`
- **Disclosure:** not listed · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://github.com/CoverProtocol/cover-security/tree/master/audits

### 60. Ammalgam DLEX  —  `ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE`

- **Rank (Ranking A — priority (likelihood × actionability)):** 60
- **Protocol:** Ammalgam DLEX (`ammalgam-dlex`) · Lending · Ethereum
- **DefiLlama:** https://defillama.com/protocol/ammalgam-dlex
- **PRIORITY 47.08**  =  LIKELIHOOD 47.08 × ACTIONABILITY 100.0%
    - likelihood = family evidence 31.9/50 (MATCH 63.8 × evidence weight 1.0) + learned attack surface 15.18/50
    - actionability: small enough to be unwatched, large enough to matter
- **Value at risk:** $62,650 · **Band:** `IN_BAND`
- **Evidence level:** `L4_GUARD_REVIEW` · MATCH 63.8 · CONFIDENCE 90.4
- **Measured attack-surface signals** (weights learned from 2022-24 hacks, validated out of sample):
    - `age_under_1y` — raises likelihood, measured lift ×2.256 (weight +0.81)
    - `has_2plus_audits` — raises likelihood, measured lift ×2.084 (weight +0.73)
    - `on_ethereum` — raises likelihood, measured lift ×1.891 (weight +0.64)
    - `chain_hazard_ge2` — raises likelihood, measured lift ×1.858 (weight +0.62)
    - `pricing_surface_undeclared` — raises likelihood, measured lift ×1.691 (weight +0.53)
    - `single_chain` — lowers likelihood, measured lift ×0.66 (weight -0.42)
- **Broken invariant tested:** A vault share rate is an accounting quantity of another protocol, not a market price. Using it as a feed imports every way that vault's rate can be moved, including donation inflation and same-transaction redemption effects.
    - Deployed source (`AmmalgamFactory` @ 0x1a411b0f…(ethereum)): prerequisites matched: rate_used_as_price; no guard found
    - deployed source read for AmmalgamFactory@0x1a411b0f…(ethereum); indicators matched: rate_used_as_price
    - only one oracle (or none) is declared in DefiLlama metadata; this is a prioritisation signal about disclosure, not evidence that no cross-source deviation bound exists in code
    - declared oracles: none declared
- **Preconditions PRESENT / UNKNOWN:** src::rate_used_as_price, value_decision_reads_configured_feed, live_positions_exposed / feed_selection_is_configuration
- **Guards searched / found:** deviation_bound_vs_independent_source / none in the reviewed path
- **Prior art:** `PRIOR_ART_SEARCH_INCOMPLETE` — No per-deployment search of published audits, competitions, advisories and postmortems was performed. Novelty is therefore NOT claimed.
- **Falsified by:** Growth-capped rate adapter in the deployed oracle (kills the pair); Wrapper's own rate is monotonic and rate-limited; Collateral priced by an independent market feed instead
- **Where to start:** On a fork, donate to and cycle the underlying vault; assert the lending market's reported collateral price moves no more than the configured cap.
- **Evidence:** `protocols/deep_screened.jsonl#ammalgam-dlex|ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE`, `protocols/onchain_probes.json#ammalgam-dlex`
- **Disclosure:** https://ammalgam.xyz/ · audit links **as listed by DefiLlama** (not verified to cover this deployment; for fork lineages they sometimes point at a sibling protocol): https://cantina.xyz/competitions/02c29467-cb27-4beb-b2ef-500ad95e1a51, https://drive.google.com/file/d/1p3MtFZslf7sDdCoR6HH-sC8p3g-wENRR/view
