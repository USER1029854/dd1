# Excluded protocols and killed protocol-family pairs

Exclusion here means *not carried into candidate ranking*. It is **never** a statement that a protocol is safe.

## 1. Universe-level exclusions (Phase F eligibility)

| Reason | Protocols |
|---|---:|
| `BELOW_50K_FLOOR` | 5159 |
| `EXCLUDED_CEX_OR_NON_PROTOCOL_CHAIN_ENTRY` | 166 |
| `EXCLUDED_FLAGGED_RUGGED` | 116 |

Of the 0 protocols below the $1,000,000 TVL threshold, 0 were preserved in the sub-threshold high-fit queue because they are deprecated, hold authority over external value, curate third-party vaults, operate routers that hold user approvals, or carry on-chain governance authority. TVL is not equated with total value at risk.

## 2. Pairs killed at the mandatory-precondition gate

| Protocol | Family | Kill reason | Condition proven absent / guard found |
|---|---|---|---|
| `3f` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `9mm-v2` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `aave-arc` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `aave-horizon-rwa` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `aave-v2` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | DECISIVE_GUARD_FOUND | upgrade_timelocked |
| `aave-v3` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `across` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `aegis-markets` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `aerodrome-ignition` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `afi-protocol` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `agave` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | DECISIVE_GUARD_FOUND | upgrade_timelocked |
| `ajna-v1` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `alcum` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `alphix` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `anemoy-capital` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `angstrom` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `anzen-v2` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `aperocket` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | DECISIVE_GUARD_FOUND | upgrade_timelocked |
| `apollo-diversified-credit-securitize-fund` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | DECISIVE_GUARD_FOUND | initializer_modifier_present |
| `apx-bridge` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | DECISIVE_GUARD_FOUND | upgrade_timelocked |
| `arch` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `aura` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `avalon-finance` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `axelar` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `backedfi` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | DECISIVE_GUARD_FOUND | upgrade_timelocked |
| `balancer-v2` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `balancer-v3` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `base-bridge` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `beefy` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `belt-finance` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `biswap-v2` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `blackrock-buidl` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | DECISIVE_GUARD_FOUND | initializer_modifier_present |
| `bondlink-finance` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `boringdao` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `brickken` | `ORACLE-STALE-OR-SILENT-FALLBACK` | DECISIVE_GUARD_FOUND | staleness_check |
| `btcst` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `bunni-v2` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `byzanlink-rwa-markets` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `cache.gold` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `camelot-v2` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `cana-holdings-california-carbon-credits` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `cap-finance-v1-v3` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `capyfi` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `caviar-v1` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `cbridge` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `ccip` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `cega-v1` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `centrifuge-protocol` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `chamber-vaults` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `charm-finance-v1` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `clearpool-tpool` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `compound-v2` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `contango-v1` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `convex-finance` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `cooler-loans` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `credit-coop` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `cryptex-v1` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `csigma-finance` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | DECISIVE_GUARD_FOUND | initializer_modifier_present |
| `cub-finance` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `curve-llamalend` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `cvault-finance` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `debridge` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | DECISIVE_GUARD_FOUND | upgrade_timelocked |
| `dfx-v2` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `digift` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `dolomite` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `dooar-v2` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `dtrinity-dlend` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | DECISIVE_GUARD_FOUND | initializer_modifier_present |
| `ether.fi-liquid` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `ezmanager` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `feather` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `fortunafi` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `fraxlend` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `fuji-v1` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `gammaswap-open-interest` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `gauntlet` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `gearbox` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `gmd-protocol` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `goldfinch` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | DECISIVE_GUARD_FOUND | initializer_modifier_present |
| `goldfinger` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `gondi-v3` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `goplus-locker-v2` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `harmonix-finance` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | DECISIVE_GUARD_FOUND | upgrade_timelocked |
| `inverse-finance-frontier` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `joe-v2` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `joe-v2.1` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `k3-capital` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | DECISIVE_GUARD_FOUND | upgrade_timelocked |
| `kasu` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `kim-exchange-v2` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `kinza-finance` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `kokonut-swap` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `kpk` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `kyberswap-elastic` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `landshare` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `landx-finance` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `lido` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | DECISIVE_GUARD_FOUND | upgrade_timelocked |
| `lighter-bridge` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `lista-cdp` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | DECISIVE_GUARD_FOUND | upgrade_timelocked |
| `liveart` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | DECISIVE_GUARD_FOUND | upgrade_timelocked |
| `lixir-finance` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `lockon` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `lybra-v1` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `makina` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `mansory` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | DECISIVE_GUARD_FOUND | upgrade_timelocked |
| `matrixdock-stbt` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `maverick-v1` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `mcdex` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | DECISIVE_GUARD_FOUND | upgrade_timelocked |
| `mento-v2` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `midas-capital` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `morpho-blue` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `morpho-optimizer-aavev2` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | DECISIVE_GUARD_FOUND | upgrade_timelocked |
| `multichain` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `native-credit-pool` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `near-intents` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `octus-bridge` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `ondo-global-markets` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `orderly-bridge` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | DECISIVE_GUARD_FOUND | upgrade_timelocked |
| `orion-pools` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | DECISIVE_GUARD_FOUND | upgrade_timelocked |
| `ostium` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `pancakeswap-amm` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `pancakeswap-amm-v3` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `pancakeswap-infinity` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `pancakeswap-stableswap` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `parallel-protocol-v2` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `pareto-credit` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | DECISIVE_GUARD_FOUND | upgrade_timelocked |
| `paxos-gold` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `percent-finance` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `pickle` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `picwe` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `piedao` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `premia-v2` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `quickswap-dex` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `ra-exchange` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | DECISIVE_GUARD_FOUND | initializer_modifier_present |
| `railgun` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `re` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `renegade` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `reserve-protocol` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `saddle-finance` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `sato` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `sectorone-dlmm` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `segment-finance` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `sentora` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | DECISIVE_GUARD_FOUND | upgrade_timelocked |
| `set-protocol` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `shimmerbridge` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `silo-v1` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `silo-v2` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `singularitydao` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | DECISIVE_GUARD_FOUND | upgrade_timelocked |
| `sky-lending` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `snuggle` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `spark-savings` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `sparklend` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `spectra-v1` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `spiko` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `squadswap-thanos` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `stake-dao` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | DECISIVE_GUARD_FOUND | upgrade_timelocked |
| `stargate-v1` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `steakhouse-financial` | `ACC-NAV-SHAREPRICE-MANIPULABLE` | DECISIVE_GUARD_FOUND | curator_action_timelock_plus_guardian_veto |
| `steakhouse-financial` | `AUTH-MISSING-ON-VALUE-MOVING-PATH` | DECISIVE_GUARD_FOUND | multisig_plus_timelock_plus_guardian_veto |
| `steakhouse-financial` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `strata-season-0` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | DECISIVE_GUARD_FOUND | upgrade_timelocked |
| `sturdy-v2` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `sushiswap` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `sushiswap-v3` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `swamp-finance` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `swapr-v2` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `synapse-cross-chain-bridge` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `synfutures-v1` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `taiko-bridge` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `tangent-finance` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `termmax` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `the-tokenized-bitcoin` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `theo-network-thbill` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `topaz-cl` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `tornado-cash` | `AUTH-MISSING-ON-VALUE-MOVING-PATH` | SANCTIONS_DESIGNATED_NO_LAWFUL_ENGAGEMENT | responsible-disclosure recipient |
| `tornado-cash` | `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY` | SANCTIONS_DESIGNATED_NO_LAWFUL_ENGAGEMENT | responsible-disclosure recipient |
| `tornado-cash` | `CALLDATA-CALLER-CONTROLLED-TARGET` | SANCTIONS_DESIGNATED_NO_LAWFUL_ENGAGEMENT | responsible-disclosure recipient |
| `tornado-cash` | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | SANCTIONS_DESIGNATED_NO_LAWFUL_ENGAGEMENT | responsible-disclosure recipient |
| `tornado-cash` | `SIG-VERIFIER-DEFEATABLE` | SANCTIONS_DESIGNATED_NO_LAWFUL_ENGAGEMENT | responsible-disclosure recipient |
| `tornado-cash` | `AUTH-ZERO-ADDRESS-ACCEPTED` | SANCTIONS_DESIGNATED_NO_LAWFUL_ENGAGEMENT | responsible-disclosure recipient |
| `tornado-cash` | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | SANCTIONS_DESIGNATED_NO_LAWFUL_ENGAGEMENT | responsible-disclosure recipient |
| `tornado-cash` | `ACC-HARDCODED-PEG-REDEMPTION` | SANCTIONS_DESIGNATED_NO_LAWFUL_ENGAGEMENT | responsible-disclosure recipient |
| `tornado-cash` | `METATX-SENDER-IDENTITY-CONFUSION` | SANCTIONS_DESIGNATED_NO_LAWFUL_ENGAGEMENT | responsible-disclosure recipient |
| `tornado-cash` | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | SANCTIONS_DESIGNATED_NO_LAWFUL_ENGAGEMENT | responsible-disclosure recipient |
| `tornado-cash` | `ACC-DUPLICATE-ID-ACCUMULATION` | SANCTIONS_DESIGNATED_NO_LAWFUL_ENGAGEMENT | responsible-disclosure recipient |
| `tornado-cash` | `ACC-CREDIT-NOT-RECEIVED` | SANCTIONS_DESIGNATED_NO_LAWFUL_ENGAGEMENT | responsible-disclosure recipient |
| `tornado-cash` | `AUTH-IDENTITY-SATISFIABLE-BY-ATTACKER-CONTRACT` | SANCTIONS_DESIGNATED_NO_LAWFUL_ENGAGEMENT | responsible-disclosure recipient |
| `tornado-cash` | `SECRET-EMBEDDED-IN-PUBLIC-CODE-AS-AUTH` | SANCTIONS_DESIGNATED_NO_LAWFUL_ENGAGEMENT | responsible-disclosure recipient |
| `tornado-cash` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | SANCTIONS_DESIGNATED_NO_LAWFUL_ENGAGEMENT | responsible-disclosure recipient |
| `trevee-earn` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `uncx-network-v3` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `uniswap-v1` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `uniswap-v2` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `uniswap-v3` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `uniswap-v4` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `usd-ai` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | DECISIVE_GUARD_FOUND | upgrade_timelocked |
| `usdt0` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | DECISIVE_GUARD_FOUND | upgrade_timelocked |
| `usual-usd0` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `vaneck-treasury-fund` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | DECISIVE_GUARD_FOUND | initializer_modifier_present |
| `vault-street-primeusd` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | DECISIVE_GUARD_FOUND | upgrade_timelocked |
| `vaultedge` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `venus-core-pool` | `ACC-DONATION-UNACCOUNTED-BALANCE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | rate_reads_raw_balance |
| `venus-core-pool` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `vesper` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `wisdomtree` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `wise-token` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `woofi-swap` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `wstgbp` | `SIG-VERIFIER-DEFEATABLE` | DECISIVE_GUARD_FOUND | uses_oz_ecdsa |
| `wstgbp` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | DECISIVE_GUARD_FOUND | upgrade_timelocked |
| `xstocks` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `xtoken` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `yield-basis` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `yieldfi` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | DECISIVE_GUARD_FOUND | upgrade_timelocked |
| `zerolend-lending` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `zksync-era-txbridge` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |
| `ztln-p` | `UPGRADE-INITIALIZER-REACHABLE-LIVE` | MANDATORY_PRECONDITION_PROVEN_ABSENT | upgradeable_architecture |

Every killed pair is written in full to `families/near_miss_library.jsonl` with its initial similarity, the decisive guard or absent precondition, and the uncertainty that remains. Near misses are first-class results: they are what make the next pass more precise.

## 3. Families with no addressable population in this universe

| Family | Incidents | Why no protocol-family pair was generated |
|---|---:|---|
| `TOKEN-DEFERRED-BURN-LP-RESERVE-DESYNC` | 14 | Victims are individually deployed BSC/Base tokens with custom transfer logic that are not listed as DefiLlama protocols; the family has no addressable protocol population in this universe. Handed to the token-level monitoring workstream instead. |
| `TOKEN-TRANSFER-OVERRIDE-BREAKS-CONSERVATION` | 3 | Same population problem as the deferred-burn family. |
| `SECRET-EMBEDDED-IN-PUBLIC-CODE-AS-AUTH` | 3 | Requires bytecode constant analysis per contract; run as a sweep over deep-screened deployments rather than as a ranked pair. |
| `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 3 | Detected by parameter-shape sweep over deep-screened deployments. |
| `AUTH-IDENTITY-SATISFIABLE-BY-ATTACKER-CONTRACT` | 3 | Detected by source-grep sweep over deep-screened deployments. |
| `TOKEN-TRANSFER-INTENT-HEURISTIC-FORGEABLE` | 2 | Same population problem as the deferred-burn family. |
| `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | 2 | Applies to token contracts with accrual hooks; only reachable through per-token screening, not the protocol universe. |
| `TOKEN-PACKED-OWNERSHIP-UNDERFLOW` | 2 | Requires DN404/BT404 lineage; no in-universe protocol above the TVL threshold carries it. |
| `METATX-SENDER-IDENTITY-CONFUSION` | 2 | Requires ERC-2771 detection per contract; run as a sweep. |
| `ACC-DUPLICATE-ID-ACCUMULATION` | 2 | Detected by selector-shape sweep over deep-screened deployments. |
| `SIG-VERIFIER-DEFEATABLE` | 2 | Detected by source-grep sweep over deep-screened deployments. |
| `AUTH-ZERO-ADDRESS-ACCEPTED` | 1 | Screened as a cheap read-only sweep (owner()==address(0) with non-zero balance) rather than as a protocol-family pair. |
| `STORAGE-LAYOUT-COLLISION-PHANTOM-CREDIT` | 1 | Requires a storage-layout dump per contract; run as a sweep over deep-screened deployments. |
| `ACC-CREDIT-NOT-RECEIVED` | 1 | Reward-tracker contracts are rarely separate DefiLlama entries; folded into the reward-index sweep. |
| `ACC-HARDCODED-PEG-REDEMPTION` | 1 | Folded into the stablecoin-issuer oracle screen. |
| `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 1 | Detected by selector sweep over deep-screened deployments. |
