#!/usr/bin/env bash
# Reproduction script for the six-month DeFi incident intelligence + DefiLlama
# prioritization run. Every command below is READ-ONLY: HTTP GET against public
# indexes/APIs, and eth_call / eth_getStorageAt / eth_getCode against public RPC.
# No transaction is constructed, signed, simulated against live user state as a
# broadcast, or submitted. No credential is recovered or used.
#
# Commands appear in execution order and each stage appears ONCE. Secrets are
# referenced by environment variable only; none are embedded here.
#
# On the two-pass structure in sections 4-6: it is a genuine bootstrap, not a
# repeated stage. parse_registries.py needs a worklist to know which adapters to
# parse, and build_universe2.py needs parse_registries' output to compute the
# dead-adapter and registry-lineage conditions. So a coarse universe and worklist
# are built first, used to fetch adapters, and then discarded and rebuilt.
set -euo pipefail
ROOT="${ROOT:-$(cd "$(dirname "$0")" && pwd)}"
cd "$ROOT"

: "${ETHERSCAN_V2_KEY:?export ETHERSCAN_V2_KEY before replay}"
: "${ALCHEMY_KEY:?export ALCHEMY_KEY before replay}"
: "${BSC_RPC:?export BSC_RPC before replay}"

# ---------------------------------------------------------------- 0. scaffold
mkdir -p sources/{slowmist,incident-references,defillama,deployments} \
         incidents families protocols results tools
#   run_config.json is authored by hand and pins WINDOW_START / WINDOW_END.

# ------------------------------------------- 1. Phase A: SlowMist incident index
# Crawl the all-category index until the date boundary is proven: continue until
# a full page contains no in-window incident and every row on it predates
# WINDOW_START. Saves raw HTML snapshots + SHA-256 + parsed rows per page.
python3 tools/crawl_slowmist.py 30 ""
#   -> sources/slowmist/all_page_###.html, crawl_log_all.json, parsed_rows_all.json

# Per-category crawls, used only to attribute SlowMist's category to each row.
for c in Blockchain Exchange Wallet ETH BSC Tron EOS Polygon HECO Fantom Solana \
         Avalanche Polkadot Arbitrum Optimism zkSync Base NFT Bridge Other; do
  python3 tools/crawl_slowmist.py 15 "$c"
done

# Merge + normalize into the raw corpus with stable incident IDs.
python3 tools/normalize_raw.py
#   -> incidents/all_raw.jsonl   (240 rows, 205 inside the window)

# -------------------------------------- 2. Phase B/C: corroboration + evidence
# Archive every reference URL for gate-passing incidents. Client-rendered social
# posts are recorded as LEAD_ONLY (SlowMist §2.2 rank 7), never as corroboration.
python3 tools/archive_refs.py
#   -> sources/incident-references/reference_index.json + HTML snapshots
#
# Independent technical corroboration for the family-anchor incidents was
# performed interactively against published postmortems and security-firm
# analyses; the resulting grade upgrades are recorded in
# tools/classification.py and listed in quality_report.md.

# --------------------------- 3. Phase C/D/E: records, families, guard library
python3 tools/build_incidents.py
#   -> incidents/{included,provisional,excluded}.jsonl, duplicate_groups.json
#   -> families/families.json, families/guard_library.jsonl
python3 tools/write_families_md.py
#   -> families/families.md

# ------------------ 4. Phase F: DefiLlama universe, bootstrap pass (see header)
curl -sS -m 120 -o sources/defillama/protocols.json "https://api.llama.fi/protocols"
sha256sum sources/defillama/protocols.json > sources/defillama/protocols.sha256
curl -sS -m 120 -o sources/defillama/hacks.json "https://api.llama.fi/hacks"
sha256sum sources/defillama/hacks.json > sources/defillama/hacks.sha256
python3 tools/build_universe.py
#   -> a coarse protocols/defillama_universe.json + eligibility.json
python3 tools/gen_pairs.py
#   -> protocols/pairs_l0.json, deep_screen_worklist.json,
#      families_not_screenable_in_universe.json

# ------------------------------------------ 5. Phase F.3 (L1): adapter evidence
# One fetcher, two strategies in order: projects/<module>, then the authoritative
# tvlCodePath, which is what resolves the shared registry adapters.
python3 tools/fetch_adapters3.py
python3 tools/parse_registries.py
#   -> protocols/adapters_index.json, registry_configs.json, registry_slug_map.json,
#      dead_adapters.json, dead_adapter_slug_map.json

# ------------- 6. Phase F rebuild: hard $50k floor + the observable condition layer
# Now that registry lineage and dead-adapter state are known, rebuild the universe:
# fork-of-an-in-window-victim, dead adapter with residual TVL, version-sibling legacy,
# declared fallback oracle, RWA pricing surface, co-curated vaults, architecture tags.
python3 tools/build_universe2.py
#   -> protocols/{defillama_universe,eligibility,conditions,victim_map,
#                 subfloor_authority_deferred}.json

# --------------------------------- 7. Phase H.3 (L2/L3): read-only chain probes
# eth_call / eth_getStorageAt / eth_getCode + explorer getsourcecode only.
# gen_pairs4 needs admin_posture.json and learned_weights.json, which need probe
# output, so the first probe pass runs against the bootstrap worklist.
python3 tools/deep_screen4.py 1300 --force   # batched JSON-RPC probe
python3 tools/resolve_impl.py                # follow delegator/beacon proxies to implementations
#   -> protocols/onchain_probes.json

# ------------------- 7b. Phase H.3 (L4): deployed-source static-indicator sweep
# Fetches verified source for the contracts actually found on-chain, follows proxies to
# their implementations, and evaluates each family's documented static_indicators. Source
# is cached under sources/deployments/, so re-analysis after an indicator change is free:
#   python3 tools/source_sweep.py 1300
# Re-analysis after an indicator change is free (source is cached):
#   python3 tools/source_sweep.py 1300 --reanalyze --reanalyze
python3 tools/source_sweep.py 1300
# Re-analysis after an indicator change is free (source is cached):
#   python3 tools/source_sweep.py 1300 --reanalyze

# ------------- 7c. Non-EVM: the cohort the eth_call instrument cannot see
# The main screen is an EVM instrument, so 717 protocols above the floor were never
# looked at. Classify them by execution runtime, because that decides which families
# may legitimately be applied: Solana, Move and the EVM all discard state when a call
# fails, so the two rollback families do NOT apply there; Cosmos SDK and Substrate
# handlers can leave a write behind, so they do.
python3 tools/nonevm_cohort.py          # -> protocols/nonevm_cohort.json
# app/app.go names every module a Cosmos chain wires in, so one fetch yields the real
# module list without guessing paths. Requires protocols/appchain_targets.json.
python3 tools/appchain_probe.py         # -> protocols/appchain_probe.json
python3 tools/write_nonevm_report.py    # -> results/nonevm_cohort.md
#
# NOT RUNNABLE IN THIS SESSION: tools/repo_sweep.py sweeps the whole non-EVM cohort's
# public source. It is written and validated against ground truth (it fires on Maya's
# confirmed defects and finds THORChain's CacheContext guard), but this session's
# network policy binds the GitHub API to the session's own repository and blocks
# github.com HTML and codeload tarballs, so a repository file tree cannot be
# enumerated. Left in place because it is a network-scope limit, not a missing method.

# ------------------------- 8. Validate the model instead of asserting it
# Read-only authority walk: ERC-1967 admin slot + owner(), up to 3 hops, terminal
# authority fingerprinted by the functions it answers. Selectors are DERIVED by
# tools/keccak.py, which self-checks against two publicly known ones at import.
python3 tools/admin_audit.py 9999 --force   # -> protocols/admin_posture.json
python3 tools/feature_lift.py --uncensored  # -> protocols/feature_lift_uncensored.json
python3 tools/ablation.py                   # -> protocols/ablation.json (which features earn their place)
python3 tools/learn_weights.py              # -> protocols/learned_weights.json (fit 2022-24, test 2025-26)
python3 tools/backtest.py --all --no-prior  # -> protocols/backtest.json (leakage controlled)
python3 tools/write_authority_report.py     # -> results/upgrade_authority_exposure.md

# ------------------------------------- 9. Phase H/13: gate, scoring, rankings
# The band screen and final worklist are ordered by the LEARNED surface, so they are
# rebuilt here rather than at section 4. Adapters are refetched for the protocols the
# widened worklist adds; both stages are incremental and skip what is already cached.
python3 tools/gen_pairs4.py 1200      # -> protocols/band_screen.json + the final worklist
python3 tools/fetch_adapters3.py      # adapters for the protocols the widened worklist adds
# score2 holds the precision controls: relevance gate, prevalence demotion (>25% of the
# swept population), metadata-cannot-prove-code, and UNKNOWN exposure for approval-dependent
# families. score4 imports it; it is not run standalone.
python3 tools/score4.py               # LIKELIHOOD (family evidence + learned surface), ACTIONABILITY, PRIORITY
#   -> protocols/deep_screened.jsonl
python3 tools/write_results4.py 60
#   -> results/candidates_by_{priority,likelihood,match}.md, candidates_all.csv,
#      audit_variables.txt, families/near_miss_library.jsonl
python3 tools/write_summary4.py       # -> results/run_summary.md
python3 tools/write_quality4.py       # -> quality_report.md

# --------------------------------------------- 10. Manifest + mechanical checks
python3 tools/compact_artifacts.py  # content-safe dedup of adapter snapshots
python3 tools/build_manifest.py     # -> manifest.json
python3 tools/check_manifest.py     # -> results/manifest_check.txt (must pass)
