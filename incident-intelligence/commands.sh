#!/usr/bin/env bash
# Reproduction script for the six-month DeFi incident intelligence + DefiLlama
# prioritization run. Every command below is READ-ONLY: HTTP GET against public
# indexes/APIs, and eth_call / eth_getStorageAt / eth_getCode against public RPC.
# No transaction is constructed, signed, simulated against live user state as a
# broadcast, or submitted. No credential is recovered or used.
#
# Commands appear in execution order. Secrets are referenced by environment
# variable only; none are embedded here.
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

# --------------------------------------- 4. Phase F: DefiLlama protocol universe
TS=$(date -u +%Y-%m-%dT%H:%M:%SZ)
curl -sS -m 120 -o sources/defillama/protocols.json "https://api.llama.fi/protocols"
sha256sum sources/defillama/protocols.json > sources/defillama/protocols.sha256
python3 tools/build_universe.py
#   -> protocols/defillama_universe.json, protocols/eligibility.json

# ------------------------------- 5. Phase G/H.1: features + protocol-family pairs
python3 tools/gen_pairs.py
#   -> protocols/pairs_l0.json, protocols/deep_screen_worklist.json,
#      protocols/families_not_screenable_in_universe.json

# ------------------------------------------ 6. Phase F.3 (L1): adapter evidence
# Primary path: projects/<module>. Fallback: the authoritative tvlCodePath, which
# resolves the shared registry adapters (registries/compound.js, curators.js).
python3 tools/fetch_adapters.py
python3 tools/fetch_adapters2.py
python3 tools/parse_registries.py
#   -> protocols/adapters_index.json, registry_configs.json, registry_slug_map.json

# ---------------------- 6b. EXPANSION PASS (hard $50k floor + condition layer)
# Rebuild the universe at a hard $50,000 floor and compute the observable condition layer:
# fork-of-an-in-window-victim, dead adapter with residual TVL, version-sibling legacy,
# declared fallback oracle, RWA pricing surface, co-curated vaults, architecture tags.
python3 tools/build_universe2.py
#   -> protocols/{defillama_universe,eligibility,conditions,victim_map,
#                 subfloor_authority_deferred}.json
python3 tools/gen_pairs2.py          # conditions can create a pair, not just re-rank one
python3 tools/fetch_adapters3.py     # adapters for the expanded worklist
python3 tools/parse_registries.py    # compound.js + aave.js + curators.js + deadAdapters.json

# --------------------------------- 7. Phase H.3 (L2/L3): read-only chain probes
# eth_call / eth_getStorageAt / eth_getCode + explorer getsourcecode only.
python3 tools/deep_screen.py 60        # first pass, sequential
python3 tools/deep_screen2.py          # registry-aware probes
python3 tools/deep_screen3.py          # corrected slug->registry mapping, multi-chain
python3 tools/resolve_impl.py          # follow delegator/beacon proxies to implementations
python3 tools/deep_screen4.py 700      # batched JSON-RPC probe over the expanded worklist
#   -> protocols/onchain_probes.json

# ------------------- 7b. Phase H.3 (L4): deployed-source static-indicator sweep
# Fetches verified source for the contracts actually found on-chain, follows proxies to their
# implementations, and evaluates each family's documented static_indicators. Source is cached
# under sources/deployments/, so re-analysis after an indicator change is free:
#   python3 tools/source_sweep.py 400 --reanalyze
python3 tools/source_sweep.py 400

# ------------ 7c. BAND PASS: likelihood-first screen for an independent reviewer
# Derive the empirical victim profile from this run's own corpus (loss distribution,
# chain and category hazard ratios), apply the $50k-$30M band with an explicit-danger
# override above it, and order by hazard x attention deficit.
#   tools/hazard.py holds the measured hazard tables.
python3 tools/gen_pairs3.py 700       # -> protocols/band_screen.json + a band-targeted worklist
python3 tools/fetch_adapters3.py      # adapters for the band worklist
python3 tools/deep_screen4.py 800 --force   # batched probe incl. the owner-is-EOA second hop
python3 tools/source_sweep.py 700     # deployed-source indicators (view helpers excluded)

# ------------------------------------- 8. Phase H/13: gate, scoring, rankings
# score2 applies the precision controls: relevance gate, prevalence demotion (>25% of the
# swept population), metadata-cannot-prove-code, and UNKNOWN exposure for approval-dependent
# families.
python3 tools/score2.py               # gate + MATCH_SCORE + precision controls
python3 tools/score3.py               # + HACK_LIKELIHOOD (hazard x neglect x economics)
#   -> protocols/deep_screened.jsonl
python3 tools/write_results3.py 45    # -> candidates_by_likelihood.md, candidates_by_match.md,
                                      #    candidates_all.csv, audit_variables.txt, near_miss_library
python3 tools/write_summary3.py
python3 tools/write_quality3.py
#   -> results/candidates_all.csv, candidates_by_match.md, candidates_by_prevention.md,
#      audit_variables.txt, excluded_protocols.md, run_summary.md
#   -> families/near_miss_library.jsonl

# --------------------------------------------- 9. Manifest + mechanical checks
python3 tools/build_manifest.py     # -> manifest.json
python3 tools/check_manifest.py     # -> results/manifest_check.txt (must pass)
