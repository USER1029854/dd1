# Urgency-first candidates — ranked by the clock, not by likelihood

> **Discovery stage.** Nothing here says any protocol is exploitable. Each entry is a *high-urgency audit candidate*: named evidence matches a family's prerequisites, named evidence is unknown, and a named guard would falsify it. A high `URGENCY` is a triage order, never an exploit probability.

## The incident is the evidence. The un-hit relative is the target.

The previous version of this list put the **victim** in Tier 1. That was backwards. A drained victim's value is already gone — a hot clock over an empty vault is not a candidate. What the incident actually gives you is proof that the technique is public and the code was unpatched; the money is in the *other* deployments of that code.

Measured, not assumed: **155 of 283 recorded victims hold less than the $50,000 floor today.** The old Tier-1 list was largely empty vaults, and the ones that were not empty were giants — aave-v3 at $17.4bn, venus-core-pool at $1.27bn — which is exactly the exposure weighting that was rejected.

### Three rules, in this order

1. **Gate on live value, read at head (2026-08-27T09:59:26Z).** Never historical TVL, never the amount a past incident moved. Empty → out, *before* anything is scored. A drained victim is excluded however fresh its incident is.
2. **Score reachability, never magnitude.** A small wide-open vault outranks a large hard-to-reach one. No dollar term appears anywhere in the 100 points — putting size back into the score would re-create the $3bn-tops-the-list failure.
3. **Tiebreak on magnitude.** Among equals on the same code, prefer the fuller sibling.

### The one exception: the restore window

A protocol restarted, refunded or whitehat-restored **without the fix in the deployed artifact** is holding real money again on the same open door, and the first hours after it resumes are the highest-sensitivity moment in this whole model. Six qualify, identified from their TVL series rather than a snapshot: they fell hard around their incident and have since recovered materially.

**The honest ceiling in this run is 28 of those 40, not 40.** The full band requires confirming that the specific fixed line is *absent from the deployed artifact* — an L4 read of runtime bytecode at the live address. This run has not performed that per-protocol check, so every Tier-1/2 row carries `KNOWN_ISSUE_STATUS_UNKNOWN` and names the decisive check that would settle it. That check is the first thing to run, and it is fast.

## What the tiers found

| Tier | What it means | Fresh protocols |
|---|---|---:|
| **1 — UNREMEDIATED-KNOWN** | restore-window victim, or an un-hit deployment on the *same code* as a hit sibling | **2** |
| **2 — SHARED-DEPENDENCY** | an advisory or template live across a population with no patch-compliance mechanism | **115** |
| 3 — DEPENDENCY-IMPAIRMENT | the target holds or is backed by a system that is itself exposed | 0 |
| **4 — FORK-OF-RECENT-VICTIM** | version sibling of a victim — *this is where the un-hit relatives are* | **58** |
| 5 — NOVEL-HIGH-FIT | strong match, no public disclosure — the clock has not started | 1425 |

This list delivers **every fresh candidate in the hot tiers (1–4): 175 protocols**, not a round number. Tier 5 — novel high-fit, where the clock has not started — is excluded by construction; it is the old likelihood-first list and it belongs below everything here.

**Where Tier 4 is:** it is the biggest hot tier in this run at **58 fresh protocols**, and under this framing it is the point. A Tier-4 row is an un-hit version sibling of a protocol that was exploited — the sibling supplies the technique, this deployment still holds the money. The previous list buried them because it filled every slot with Tier 1–2; they are ranked in line here.

## Handoff lines for CORE.md

```
TARGET=https://defillama.com/protocol/save || TIER=1 || FAMILY=ORACLE-STALE-OR-SILENT-FALLBACK || DECISIVE_CHECK=Confirm the fix from the 2022-11-02 postmortem is present in the DEPLOYED artifact at the live address, not merely in the repo or a release note. Absent -> act now. || VALUE_AT_RISK=85337343 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM|SOLANA
TARGET=https://defillama.com/protocol/tinyman || TIER=1 || FAMILY=ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED || DECISIVE_CHECK=Confirm the fix from the 2022-01-01 postmortem is present in the DEPLOYED artifact at the live address, not merely in the repo or a release note. Absent -> act now. || VALUE_AT_RISK=5523729 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/connext || TIER=2 || FAMILY=HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=30648382 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=BRIDGE|EVM
TARGET=https://defillama.com/protocol/dxsale || TIER=2 || FAMILY=AUTH-ZERO-ADDRESS-ACCEPTED || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=15934950 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/feather || TIER=2 || FAMILY=ACC-DONATION-UNACCOUNTED-BALANCE || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=13525457 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=COSMOS_APPCHAIN|EVM
TARGET=https://defillama.com/protocol/mev-capital || TIER=2 || FAMILY=ACC-DONATION-UNACCOUNTED-BALANCE || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=11932214 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM|MOVE_SUI
TARGET=https://defillama.com/protocol/flokifi-locker || TIER=2 || FAMILY=ACC-DONATION-UNACCOUNTED-BALANCE || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=11876885 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/yieldfi || TIER=2 || FAMILY=ACC-DONATION-UNACCOUNTED-BALANCE || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=11413933 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/autofarm || TIER=2 || FAMILY=ACC-DONATION-UNACCOUNTED-BALANCE || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=6212863 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/pickle || TIER=2 || FAMILY=ACC-DONATION-UNACCOUNTED-BALANCE || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=4850576 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/zerolend-vaults || TIER=2 || FAMILY=ACC-DONATION-UNACCOUNTED-BALANCE || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=1812677 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/avalon-finance || TIER=2 || FAMILY=ACC-DONATION-UNACCOUNTED-BALANCE || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=1326615 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/vendor-v2 || TIER=2 || FAMILY=ACC-DONATION-UNACCOUNTED-BALANCE || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=692211 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/adamant-finance || TIER=2 || FAMILY=ACC-DONATION-UNACCOUNTED-BALANCE || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=175359 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/scrubvault || TIER=2 || FAMILY=ACC-DONATION-UNACCOUNTED-BALANCE || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=132836 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=COSMOS_APPCHAIN|EVM
TARGET=https://defillama.com/protocol/meson || TIER=2 || FAMILY=UPGRADE-INITIALIZER-REACHABLE-LIVE || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=615403 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=BRIDGE|EVM
TARGET=https://defillama.com/protocol/symmio || TIER=2 || FAMILY=ORACLE-SPOT-THIN-LIQUIDITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=2760657 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/symbiosis || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=8735933 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=BRIDGE|EVM
TARGET=https://defillama.com/protocol/empiredex || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=2733454 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/carbon-defi || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=1490463 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=COSMOS_APPCHAIN|EVM
TARGET=https://defillama.com/protocol/hashport || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=1173479 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=BRIDGE|EVM
TARGET=https://defillama.com/protocol/sudoswap-v2 || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=705817 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/nervebridge || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=609902 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=BRIDGE|EVM
TARGET=https://defillama.com/protocol/wagmi || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=225181 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=COSMOS_APPCHAIN|EVM
TARGET=https://defillama.com/protocol/brownfi-v3 || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=184933 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/kinetix-amm-v3 || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=128064 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=COSMOS_APPCHAIN|EVM
TARGET=https://defillama.com/protocol/nabla-finance || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=75291 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/crypto.com-liquid-staking || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=30941481 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM|SOLANA
TARGET=https://defillama.com/protocol/pumpbtc || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=27038551 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=BRIDGE|EVM
TARGET=https://defillama.com/protocol/kodiak-islands || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=24651773 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/infrared-finance || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=19294546 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/moonlander || TIER=2 || FAMILY=ORACLE-STALE-OR-SILENT-FALLBACK || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=19097589 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/kodiak-v3 || TIER=2 || FAMILY=QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=15900560 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/saphyre-v3 || TIER=2 || FAMILY=QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=13393930 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=COSMOS_APPCHAIN
TARGET=https://defillama.com/protocol/fulcrom-perps || TIER=2 || FAMILY=ORACLE-STALE-OR-SILENT-FALLBACK || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=12578371 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/kava-mint || TIER=2 || FAMILY=ORACLE-STALE-OR-SILENT-FALLBACK || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=11970990 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=COSMOS_APPCHAIN
TARGET=https://defillama.com/protocol/acryptos || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=10538629 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/bend || TIER=2 || FAMILY=ORACLE-STALE-OR-SILENT-FALLBACK || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=10080252 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/hydro-lst || TIER=2 || FAMILY=AUTH-MISSING-ON-VALUE-MOVING-PATH || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=10022163 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=COSMOS_APPCHAIN
TARGET=https://defillama.com/protocol/astroport || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=9590425 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=COSMOS_APPCHAIN|EVM
TARGET=https://defillama.com/protocol/scrub-invest || TIER=2 || FAMILY=ACC-DONATION-UNACCOUNTED-BALANCE || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=7196157 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=COSMOS_APPCHAIN
TARGET=https://defillama.com/protocol/kava-lend || TIER=2 || FAMILY=ORACLE-STALE-OR-SILENT-FALLBACK || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=6543869 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=COSMOS_APPCHAIN
TARGET=https://defillama.com/protocol/stride || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=5745325 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=COSMOS_APPCHAIN|EVM
TARGET=https://defillama.com/protocol/folks-finance-xchain || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=5461568 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/hydro-lending || TIER=2 || FAMILY=ORACLE-STALE-OR-SILENT-FALLBACK || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=4939361 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=COSMOS_APPCHAIN
TARGET=https://defillama.com/protocol/vvs-flawless || TIER=2 || FAMILY=QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=4935111 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/takara-lend || TIER=2 || FAMILY=ORACLE-STALE-OR-SILENT-FALLBACK || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=4831963 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=COSMOS_APPCHAIN
TARGET=https://defillama.com/protocol/splashing-stake || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=4562730 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=COSMOS_APPCHAIN
TARGET=https://defillama.com/protocol/blueshift || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=4461164 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=COSMOS_APPCHAIN|EVM
TARGET=https://defillama.com/protocol/yeilend || TIER=2 || FAMILY=ORACLE-STALE-OR-SILENT-FALLBACK || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=4240357 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=COSMOS_APPCHAIN
TARGET=https://defillama.com/protocol/trustake || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=4045526 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=COSMOS_APPCHAIN|EVM|MOVE_SUI|SOLANA
TARGET=https://defillama.com/protocol/ferro || TIER=2 || FAMILY=AMM-POOL-RATIO-SKEW-EXTRACTION || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=3611583 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/sablier-lockup || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=3008551 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM|SOLANA
TARGET=https://defillama.com/protocol/lair-finance || TIER=2 || FAMILY=AUTH-MISSING-ON-VALUE-MOVING-PATH || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=2868726 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/layerbank || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=2745374 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/hiyield || TIER=2 || FAMILY=SETTLEMENT-EPOCH-BOUNDARY-CREDIT || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=2740577 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/neptune-finance || TIER=2 || FAMILY=ORACLE-STALE-OR-SILENT-FALLBACK || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=2570126 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=COSMOS_APPCHAIN
TARGET=https://defillama.com/protocol/dyorswap-amm || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=2548809 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/cabal || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=2512485 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/balanced-exchange || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=2143905 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM|SOLANA
TARGET=https://defillama.com/protocol/eris-protocol || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=2121837 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/initiadex || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=1946107 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/pumex || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=1865900 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=COSMOS_APPCHAIN
TARGET=https://defillama.com/protocol/llamapay || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=1593539 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/canto-lending || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=1444823 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/mm-finance-cronos || TIER=2 || FAMILY=AUTH-MISSING-ON-VALUE-MOVING-PATH || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=1338790 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/cgo-finance || TIER=2 || FAMILY=AUTH-MISSING-ON-VALUE-MOVING-PATH || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=1069136 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/kava-earn || TIER=2 || FAMILY=ACC-ZERO-SUPPLY-INFLATION || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=936230 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=COSMOS_APPCHAIN
TARGET=https://defillama.com/protocol/kava-liquid || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=914768 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=COSMOS_APPCHAIN
TARGET=https://defillama.com/protocol/bex || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=788002 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/smilee-finance-gbera || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=726230 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/sablier-flow || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=689782 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/helix-spot || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=654431 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=COSMOS_APPCHAIN
TARGET=https://defillama.com/protocol/goldilocks || TIER=2 || FAMILY=AUTH-MISSING-ON-VALUE-MOVING-PATH || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=545784 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/shido-dex-v3 || TIER=2 || FAMILY=QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=512898 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/ebisus-bay || TIER=2 || FAMILY=AUTH-MISSING-ON-VALUE-MOVING-PATH || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=503133 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/counterstake || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=464930 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=BRIDGE|EVM
TARGET=https://defillama.com/protocol/obsidian || TIER=2 || FAMILY=AUTH-MISSING-ON-VALUE-MOVING-PATH || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=461666 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/beradrome || TIER=2 || FAMILY=AUTH-MISSING-ON-VALUE-MOVING-PATH || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=448174 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/white-whale-dex || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=445848 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=COSMOS_APPCHAIN|EVM
TARGET=https://defillama.com/protocol/mito-finance || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=423545 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=COSMOS_APPCHAIN
TARGET=https://defillama.com/protocol/dojoswap-amm || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=415362 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=COSMOS_APPCHAIN
TARGET=https://defillama.com/protocol/kodiak-v2 || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=410822 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/cronaswap || TIER=2 || FAMILY=AUTH-MISSING-ON-VALUE-MOVING-PATH || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=410470 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/shoebill-v2 || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=388865 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/knit-finance || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=383875 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=BRIDGE|COSMOS_APPCHAIN|EVM
TARGET=https://defillama.com/protocol/black-panther || TIER=2 || FAMILY=ACC-ZERO-SUPPLY-INFLATION || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=373618 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=COSMOS_APPCHAIN
TARGET=https://defillama.com/protocol/saphyre-v2 || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=372239 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=COSMOS_APPCHAIN
TARGET=https://defillama.com/protocol/teahouse-managed || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=326424 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=COSMOS_APPCHAIN|EVM
TARGET=https://defillama.com/protocol/beraborrow || TIER=2 || FAMILY=ORACLE-STALE-OR-SILENT-FALLBACK || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=286442 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/choice-exchange || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=238153 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=COSMOS_APPCHAIN
TARGET=https://defillama.com/protocol/argo-finance || TIER=2 || FAMILY=AUTH-MISSING-ON-VALUE-MOVING-PATH || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=237101 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/shido-dex-v2 || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=216754 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/crystl-finance || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=208950 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/inertia-bridge || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=194856 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=BRIDGE|EVM
TARGET=https://defillama.com/protocol/sai || TIER=2 || FAMILY=ORACLE-STALE-OR-SILENT-FALLBACK || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=194197 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/backbone-labs || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=184056 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=COSMOS_APPCHAIN|EVM
TARGET=https://defillama.com/protocol/hard-swap || TIER=2 || FAMILY=QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=168195 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=COSMOS_APPCHAIN
TARGET=https://defillama.com/protocol/kava-swap || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=166883 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=COSMOS_APPCHAIN
TARGET=https://defillama.com/protocol/kogefarm || TIER=2 || FAMILY=AUTH-MISSING-ON-VALUE-MOVING-PATH || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=158988 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=COSMOS_APPCHAIN|EVM
TARGET=https://defillama.com/protocol/accumulated-finance-lending || TIER=2 || FAMILY=ORACLE-STALE-OR-SILENT-FALLBACK || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=156893 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/echelon-initia-bridge || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=136323 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=BRIDGE|EVM
TARGET=https://defillama.com/protocol/astrovault || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=123761 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/jiko || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=121608 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/crodex || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=114254 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/photonswap-finance || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=109725 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=COSMOS_APPCHAIN|EVM
TARGET=https://defillama.com/protocol/silostake || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=109483 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=COSMOS_APPCHAIN
TARGET=https://defillama.com/protocol/crow-finance || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=103776 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/canto-dex || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=100175 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/dojoswap-lsd || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=93480 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=COSMOS_APPCHAIN
TARGET=https://defillama.com/protocol/equilibre || TIER=2 || FAMILY=AUTH-MISSING-ON-VALUE-MOVING-PATH || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=71785 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=COSMOS_APPCHAIN
TARGET=https://defillama.com/protocol/noxa-dex-v2 || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=71262 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/avalon-usdalend || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=69968 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=COSMOS_APPCHAIN|EVM
TARGET=https://defillama.com/protocol/eddyfinance-amm || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=69530 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/winnieswap || TIER=2 || FAMILY=QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=57656 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/milkyway-rollup-bridge || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=53078 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=BRIDGE|EVM
TARGET=https://defillama.com/protocol/zearn-protocol || TIER=2 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency s || VALUE_AT_RISK=51445 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/hope-collateral || TIER=4 || FAMILY=QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=1604842 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/arrakis-v2 || TIER=4 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=156016 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/allbridge-classic || TIER=4 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=1057520 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=BRIDGE|EVM|SOLANA
TARGET=https://defillama.com/protocol/solv-vesting || TIER=4 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=142310 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/lpeth || TIER=4 || FAMILY=UPGRADE-INITIALIZER-REACHABLE-LIVE || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=639047 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/radiant-v1 || TIER=4 || FAMILY=ACC-DONATION-UNACCOUNTED-BALANCE || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=255920 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/balancer-cow-amm || TIER=4 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=59803 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/paraluni-dex || TIER=4 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=323497 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/usual-eur0 || TIER=4 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=237079 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/hope-swap || TIER=4 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=114226 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/aave-v2 || TIER=4 || FAMILY=ORACLE-SPOT-THIN-LIQUIDITY || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=110942327 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/rhea-dex || TIER=4 || FAMILY=ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=28024983 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/wemix.fi-staking || TIER=4 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=19923463 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/rhea-lst || TIER=4 || FAMILY=AUTH-MISSING-ON-VALUE-MOVING-PATH || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=17309580 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/summer.fi-pro || TIER=4 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=17019560 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/termfinance-lend || TIER=4 || FAMILY=ORACLE-STALE-OR-SILENT-FALLBACK || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=5167045 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/venus-flux || TIER=4 || FAMILY=ORACLE-STALE-OR-SILENT-FALLBACK || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=3421097 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/aftermath-afsui || TIER=4 || FAMILY=ORACLE-STALE-OR-SILENT-FALLBACK || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=2393115 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=MOVE_SUI
TARGET=https://defillama.com/protocol/aftermath-amm || TIER=4 || FAMILY=ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=2273092 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=MOVE_SUI
TARGET=https://defillama.com/protocol/wemix-concentrated-range-deposit || TIER=4 || FAMILY=QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=2169898 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/aftermath-aflp || TIER=4 || FAMILY=ACC-ZERO-SUPPLY-INFLATION || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=1900087 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=MOVE_SUI
TARGET=https://defillama.com/protocol/kernel || TIER=4 || FAMILY=AUTH-MISSING-ON-VALUE-MOVING-PATH || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=1361876 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/solv-others || TIER=4 || FAMILY=AUTH-MISSING-ON-VALUE-MOVING-PATH || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=936697 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/wemix-full-range-deposit || TIER=4 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=824781 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/defituna-liquidity || TIER=4 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=647101 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=SOLANA
TARGET=https://defillama.com/protocol/bonzo-vaults || TIER=4 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=425571 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/aave-aptos || TIER=4 || FAMILY=ORACLE-STALE-OR-SILENT-FALLBACK || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=308734 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=MOVE_SUI
TARGET=https://defillama.com/protocol/wemix-liquid-staking || TIER=4 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=254157 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/defituna-amm || TIER=4 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=244514 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=SOLANA
TARGET=https://defillama.com/protocol/solido-flow || TIER=4 || FAMILY=ACC-DONATION-UNACCOUNTED-BALANCE || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=241245 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/aave-arc || TIER=4 || FAMILY=ORACLE-SPOT-THIN-LIQUIDITY || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=57263 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/cozy-earn || TIER=4 || FAMILY=AUTH-MISSING-ON-VALUE-MOVING-PATH || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=1043001 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/typus-dov || TIER=4 || FAMILY=AUTH-MISSING-ON-VALUE-MOVING-PATH || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=996301 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=MOVE_SUI
TARGET=https://defillama.com/protocol/velar-amm || TIER=4 || FAMILY=ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=401394 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/hyperdrive-hl-earn || TIER=4 || FAMILY=ACC-ZERO-SUPPLY-INFLATION || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=278407 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/typus-safu || TIER=4 || FAMILY=ACC-ZERO-SUPPLY-INFLATION || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=191193 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=MOVE_SUI
TARGET=https://defillama.com/protocol/ribbon-lend || TIER=4 || FAMILY=AUTH-MISSING-ON-VALUE-MOVING-PATH || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=52339 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/apertureswap || TIER=4 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=51432 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/pando-leaf || TIER=4 || FAMILY=ORACLE-STALE-OR-SILENT-FALLBACK || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=11396230 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/curve-llamalend-v2 || TIER=4 || FAMILY=ORACLE-STALE-OR-SILENT-FALLBACK || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=2057612 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/thala-cdp || TIER=4 || FAMILY=ORACLE-STALE-OR-SILENT-FALLBACK || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=476431 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=MOVE_SUI
TARGET=https://defillama.com/protocol/ethos-reserve || TIER=4 || FAMILY=ORACLE-STALE-OR-SILENT-FALLBACK || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=233361 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/ironclad-finance || TIER=4 || FAMILY=ORACLE-STALE-OR-SILENT-FALLBACK || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=160923 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/save-sol || TIER=4 || FAMILY=PROOF-VERIFICATION-BYPASSED || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=6180608 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=SOLANA
TARGET=https://defillama.com/protocol/eigenpie || TIER=4 || FAMILY=AUTH-MISSING-ON-VALUE-MOVING-PATH || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=4468919 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/woofi-earn || TIER=4 || FAMILY=ACC-ZERO-SUPPLY-INFLATION || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=2694195 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/nirvana-v2 || TIER=4 || FAMILY=AUTH-MISSING-ON-VALUE-MOVING-PATH || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=2586219 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=SOLANA
TARGET=https://defillama.com/protocol/thalaswap-v3 || TIER=4 || FAMILY=ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=2160250 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=MOVE_SUI
TARGET=https://defillama.com/protocol/thala-lsd || TIER=4 || FAMILY=PROOF-VERIFICATION-BYPASSED || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=1737748 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=MOVE_SUI
TARGET=https://defillama.com/protocol/arena-dex || TIER=4 || FAMILY=ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=1548374 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/thalaswap-v2 || TIER=4 || FAMILY=ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=586042 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=MOVE_SUI
TARGET=https://defillama.com/protocol/4swap || TIER=4 || FAMILY=ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=494167 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/basin-exchange || TIER=4 || FAMILY=ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=438854 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/cetus-dlmm || TIER=4 || FAMILY=ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=433422 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=MOVE_SUI
TARGET=https://defillama.com/protocol/swapx-algebra || TIER=4 || FAMILY=ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=404169 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/voltage-v4 || TIER=4 || FAMILY=ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=186232 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/velocore-v1 || TIER=4 || FAMILY=UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=126571 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
TARGET=https://defillama.com/protocol/voltage-liquid-staking || TIER=4 || FAMILY=PROOF-VERIFICATION-BYPASSED || DECISIVE_CHECK=Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding. || VALUE_AT_RISK=86834 || PINNED=<pin at handoff> || REMEDIATION=KNOWN_ISSUE_STATUS_UNKNOWN || MODULES=EVM
```

## Candidates

### 1. Save — Tier 1 — URGENCY 40.75

- **Protocol:** `save` · Lending · Solana, Eclipse
- **DefiLlama:** https://defillama.com/protocol/save
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $85,337,344
    - **RESTORE WINDOW** — fell 91% around 2022-11-02 ($269,197,907 -> $25,259,893) and has since recovered to $85,337,344
- **Matched family:** `ORACLE-STALE-OR-SILENT-FALLBACK`
    - broken invariant: A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
- **URGENCY 40.75 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - RESTORE WINDOW: fell 91% around 2022-11-02 ($269,197,907 -> $25,259,893) and has since recovered to $85,337,344. It is holding real money again; if the fix is not in the deployed artifact it is the same open door.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 1394d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Confirm the fix from the 2022-11-02 postmortem is present in the DEPLOYED artifact at the live address, not merely in the repo or a release note. Absent -> act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Disclosure channel, if public:** https://www.save.finance/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 2. Tinyman — Tier 1 — URGENCY 40.38

- **Protocol:** `tinyman` · Dexs · Algorand
- **DefiLlama:** https://defillama.com/protocol/tinyman
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $5,523,730
    - **RESTORE WINDOW** — fell 100% around 2022-01-01 ($38,434,474 -> $22,593) and has since recovered to $5,523,730
- **Matched family:** `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`
    - broken invariant: Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.
- **URGENCY 40.38 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - RESTORE WINDOW: fell 100% around 2022-01-01 ($38,434,474 -> $22,593) and has since recovered to $5,523,730. It is holding real money again; if the fix is not in the deployed artifact it is the same open door.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 1699d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Confirm the fix from the 2022-01-01 postmortem is present in the DEPLOYED artifact at the live address, not merely in the repo or a release note. Absent -> act now.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Every identifier derived or verified against the factory/registry (kills the pair); Routing restricted to an immutable venue allowlist
- **Disclosure channel, if public:** https://tinyman.org
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 3. Connext — Tier 2 — URGENCY 79.57

- **Protocol:** `connext` · Bridge · Ethereum, Linea, Arbitrum, Metis, Base
- **DefiLlama:** https://defillama.com/protocol/connext
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $30,648,382
- **Matched family:** `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`
    - broken invariant: A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.
- **URGENCY 79.57 / EVIDENCE_CONFIDENCE 90.4** — evidence level `L4_GUARD_REVIEW`
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 25.0/25 · precondition match 9.57/15
- **Why the clock is hot:**
    - deployed on Cronos, Evmos, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: 3 precondition(s) present at L4_GUARD_REVIEW, no guard found in the reviewed path
    - recency: technique public 65d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Zero-amount transfers revert or short-circuit before the hook (kills the pair); Hooks are pure bookkeeping with no mint/transfer
- **Disclosure channel, if public:** https://connext.network/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 4. DxSale — Tier 2 — URGENCY 76.57

- **Protocol:** `dxsale` · Launchpad · Binance, Ethereum, Base, Arbitrum, Polygon
- **DefiLlama:** https://defillama.com/protocol/dxsale
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $15,934,950
- **Matched family:** `AUTH-ZERO-ADDRESS-ACCEPTED`
    - broken invariant: Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.
- **URGENCY 76.57 / EVIDENCE_CONFIDENCE 79.4** — evidence level `L4_GUARD_REVIEW`
    - remediation gap 28/40 · technique recency+propagation 14.0/20 · reachable live value 25.0/25 · precondition match 9.57/15
- **Why the clock is hot:**
    - deployed on Cronos, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: 3 precondition(s) present at L4_GUARD_REVIEW, no guard found in the reviewed path
    - recency: technique public 91d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Modifier asserts non-zero owner (kills the pair); Renounce removes the functions' effect, not just the address
- **Disclosure channel, if public:** https://dx.app
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 5. Feather — Tier 2 — URGENCY 71.38

- **Protocol:** `feather` · Risk Curators · Sei, Celo, MegaETH, Klaytn, Polygon
- **DefiLlama:** https://defillama.com/protocol/feather
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $13,525,458
- **Matched family:** `ACC-DONATION-UNACCOUNTED-BALANCE`
    - broken invariant: A share price, exchange rate or totalAssets must be a function of value the protocol accounted for on entry. Reading a raw balance makes any direct transfer into the accounting boundary an unpriced increase in every holder's claim.
- **URGENCY 71.38 / EVIDENCE_CONFIDENCE 69.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 20.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - deployed on Sei, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: 2 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 52d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** totalAssets derived from an internal counter, not balanceOf (kills the pair); Rate is monotonic and rate-limited per block; Inbound transfers to the accounting boundary are rejected or swept to a reserve
- **Disclosure channel, if public:** https://app.feather.zone/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 6. MEV Capital — Tier 2 — URGENCY 71.38

- **Protocol:** `mev-capital` · Risk Curators · Ethereum, Hyperliquid L1, Sui, Base, Avalanche
- **DefiLlama:** https://defillama.com/protocol/mev-capital
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $11,932,215
- **Matched family:** `ACC-DONATION-UNACCOUNTED-BALANCE`
    - broken invariant: A share price, exchange rate or totalAssets must be a function of value the protocol accounted for on entry. Reading a raw balance makes any direct transfer into the accounting boundary an unpriced increase in every holder's claim.
- **URGENCY 71.38 / EVIDENCE_CONFIDENCE 69.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 20.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - deployed on Berachain, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: 2 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 52d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** totalAssets derived from an internal counter, not balanceOf (kills the pair); Rate is monotonic and rate-limited per block; Inbound transfers to the accounting boundary are rejected or swept to a reserve
- **Disclosure channel, if public:** https://mevcapital.com
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 7. FlokiFi Locker — Tier 2 — URGENCY 71.38

- **Protocol:** `flokifi-locker` · Token Locker · Binance, Ethereum, Base, Cronos, Arbitrum
- **DefiLlama:** https://defillama.com/protocol/flokifi-locker
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $11,876,885
- **Matched family:** `ACC-DONATION-UNACCOUNTED-BALANCE`
    - broken invariant: A share price, exchange rate or totalAssets must be a function of value the protocol accounted for on entry. Reading a raw balance makes any direct transfer into the accounting boundary an unpriced increase in every holder's claim.
- **URGENCY 71.38 / EVIDENCE_CONFIDENCE 63.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 20.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - deployed on Cronos, Evmos, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: 2 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 52d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** totalAssets derived from an internal counter, not balanceOf (kills the pair); Rate is monotonic and rate-limited per block; Inbound transfers to the accounting boundary are rejected or swept to a reserve
- **Disclosure channel, if public:** https://flokifi.com
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 8. YieldFi — Tier 2 — URGENCY 71.38

- **Protocol:** `yieldfi` · Yield Aggregator · Ethereum, Base, Arbitrum, Plume Mainnet, Sonic
- **DefiLlama:** https://defillama.com/protocol/yieldfi
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $11,413,933
- **Matched family:** `ACC-DONATION-UNACCOUNTED-BALANCE`
    - broken invariant: A share price, exchange rate or totalAssets must be a function of value the protocol accounted for on entry. Reading a raw balance makes any direct transfer into the accounting boundary an unpriced increase in every holder's claim.
- **URGENCY 71.38 / EVIDENCE_CONFIDENCE 69.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 20.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - deployed on Saga, TAC, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: 2 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 52d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** totalAssets derived from an internal counter, not balanceOf (kills the pair); Rate is monotonic and rate-limited per block; Inbound transfers to the accounting boundary are rejected or swept to a reserve
- **Disclosure channel, if public:** https://yield.fi/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 9. Autofarm — Tier 2 — URGENCY 71.38

- **Protocol:** `autofarm` · Yield Aggregator · Binance, Polygon, Cronos, OKExChain, Avalanche
- **DefiLlama:** https://defillama.com/protocol/autofarm
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $6,212,864
- **Matched family:** `ACC-DONATION-UNACCOUNTED-BALANCE`
    - broken invariant: A share price, exchange rate or totalAssets must be a function of value the protocol accounted for on entry. Reading a raw balance makes any direct transfer into the accounting boundary an unpriced increase in every holder's claim.
- **URGENCY 71.38 / EVIDENCE_CONFIDENCE 69.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 20.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - deployed on Cronos, Evmos, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: 2 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 52d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** totalAssets derived from an internal counter, not balanceOf (kills the pair); Rate is monotonic and rate-limited per block; Inbound transfers to the accounting boundary are rejected or swept to a reserve
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 10. Pickle — Tier 2 — URGENCY 71.38

- **Protocol:** `pickle` · Yield Aggregator · Ethereum, Polygon, Optimism, Aurora, Arbitrum
- **DefiLlama:** https://defillama.com/protocol/pickle
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $4,850,577
- **Matched family:** `ACC-DONATION-UNACCOUNTED-BALANCE`
    - broken invariant: A share price, exchange rate or totalAssets must be a function of value the protocol accounted for on entry. Reading a raw balance makes any direct transfer into the accounting boundary an unpriced increase in every holder's claim.
- **URGENCY 71.38 / EVIDENCE_CONFIDENCE 69.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 20.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - deployed on Cronos, Kava, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: 2 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 52d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** totalAssets derived from an internal counter, not balanceOf (kills the pair); Rate is monotonic and rate-limited per block; Inbound transfers to the accounting boundary are rejected or swept to a reserve
- **Disclosure channel, if public:** https://pickle.finance/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 11. ZeroLend Vaults — Tier 2 — URGENCY 71.38

- **Protocol:** `zerolend-vaults` · Risk Curators · Ethereum, Berachain, Linea, Sonic
- **DefiLlama:** https://defillama.com/protocol/zerolend-vaults
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $1,812,678
- **Matched family:** `ACC-DONATION-UNACCOUNTED-BALANCE`
    - broken invariant: A share price, exchange rate or totalAssets must be a function of value the protocol accounted for on entry. Reading a raw balance makes any direct transfer into the accounting boundary an unpriced increase in every holder's claim.
- **URGENCY 71.38 / EVIDENCE_CONFIDENCE 69.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 20.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - deployed on Berachain, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: 2 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 52d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** totalAssets derived from an internal counter, not balanceOf (kills the pair); Rate is monotonic and rate-limited per block; Inbound transfers to the accounting boundary are rejected or swept to a reserve
- **Disclosure channel, if public:** https://zerolend.xyz/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 12. Avalon Finance — Tier 2 — URGENCY 71.38

- **Protocol:** `avalon-finance` · Lending · IoTeX, Merlin, Pharos, Binance, Bitlayer
- **DefiLlama:** https://defillama.com/protocol/avalon-finance
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $1,326,615
- **Matched family:** `ACC-DONATION-UNACCOUNTED-BALANCE`
    - broken invariant: A share price, exchange rate or totalAssets must be a function of value the protocol accounted for on entry. Reading a raw balance makes any direct transfer into the accounting boundary an unpriced increase in every holder's claim.
- **URGENCY 71.38 / EVIDENCE_CONFIDENCE 69.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 20.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - deployed on Sei, ZetaChain, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: 2 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 52d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** totalAssets derived from an internal counter, not balanceOf (kills the pair); Rate is monotonic and rate-limited per block; Inbound transfers to the accounting boundary are rejected or swept to a reserve
- **Disclosure channel, if public:** https://www.avalonfinance.xyz
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 13. Vendor V2 — Tier 2 — URGENCY 71.38

- **Protocol:** `vendor-v2` · Lending · Base, Arbitrum, Berachain, Superposition
- **DefiLlama:** https://defillama.com/protocol/vendor-v2
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $692,212
- **Matched family:** `ACC-DONATION-UNACCOUNTED-BALANCE`
    - broken invariant: A share price, exchange rate or totalAssets must be a function of value the protocol accounted for on entry. Reading a raw balance makes any direct transfer into the accounting boundary an unpriced increase in every holder's claim.
- **URGENCY 71.38 / EVIDENCE_CONFIDENCE 69.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 20.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - deployed on Berachain, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: 2 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 52d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** totalAssets derived from an internal counter, not balanceOf (kills the pair); Rate is monotonic and rate-limited per block; Inbound transfers to the accounting boundary are rejected or swept to a reserve
- **Disclosure channel, if public:** https://vendor.finance
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 14. Adamant Finance — Tier 2 — URGENCY 71.38

- **Protocol:** `adamant-finance` · Yield · Polygon, Arbitrum, Cronos, Fraxtal
- **DefiLlama:** https://defillama.com/protocol/adamant-finance
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $175,359
- **Matched family:** `ACC-DONATION-UNACCOUNTED-BALANCE`
    - broken invariant: A share price, exchange rate or totalAssets must be a function of value the protocol accounted for on entry. Reading a raw balance makes any direct transfer into the accounting boundary an unpriced increase in every holder's claim.
- **URGENCY 71.38 / EVIDENCE_CONFIDENCE 69.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 20.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - deployed on Cronos, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: 2 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 52d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** totalAssets derived from an internal counter, not balanceOf (kills the pair); Rate is monotonic and rate-limited per block; Inbound transfers to the accounting boundary are rejected or swept to a reserve
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 15. ScrubVault — Tier 2 — URGENCY 71.38

- **Protocol:** `scrubvault` · Basis Trading · Kava, Arbitrum
- **DefiLlama:** https://defillama.com/protocol/scrubvault
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $132,836
- **Matched family:** `ACC-DONATION-UNACCOUNTED-BALANCE`
    - broken invariant: A share price, exchange rate or totalAssets must be a function of value the protocol accounted for on entry. Reading a raw balance makes any direct transfer into the accounting boundary an unpriced increase in every holder's claim.
- **URGENCY 71.38 / EVIDENCE_CONFIDENCE 69.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 20.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - deployed on Kava, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: 2 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 52d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** totalAssets derived from an internal counter, not balanceOf (kills the pair); Rate is monotonic and rate-limited per block; Inbound transfers to the accounting boundary are rejected or swept to a reserve
- **Disclosure channel, if public:** https://invest.scrub.money/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 16. Meson — Tier 2 — URGENCY 71.0

- **Protocol:** `meson` · Cross Chain Bridge · Merlin, Binance, Tron, BSquared, Arbitrum
- **DefiLlama:** https://defillama.com/protocol/meson
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $615,403
- **Matched family:** `UPGRADE-INITIALIZER-REACHABLE-LIVE`
    - broken invariant: After deployment, no caller may (re)establish ownership, admin, or implementation wiring. Initialization state must be provably consumed.
- **URGENCY 71.0 / EVIDENCE_CONFIDENCE 69.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 14.0/20 · reachable live value 20.0/25 · precondition match 9.0/15
- **Why the clock is hot:**
    - deployed on Cronos, Kava, ZetaChain, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: 3 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 107d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Simulated re-initialization reverts (kills the pair); Contract is non-upgradeable and holds no approvals
- **Disclosure channel, if public:** https://meson.fi/home
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 17. SYMMIO — Tier 2 — URGENCY 67.88

- **Protocol:** `symmio` · Derivatives · Base, Arbitrum, Berachain, Coti, Binance
- **DefiLlama:** https://defillama.com/protocol/symmio
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $2,760,658
- **Matched family:** `ORACLE-SPOT-THIN-LIQUIDITY`
    - broken invariant: Borrowing capacity, mint size, reward size or collateral value must not be derived from a price that a single actor can move within the manipulation window, and the value unlocked must never exceed the cost of moving that price.
- **URGENCY 67.88 / EVIDENCE_CONFIDENCE 69.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 20.0/20 · reachable live value 12.0/25 · precondition match 7.88/15
- **Why the clock is hot:**
    - deployed on Berachain, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: 2 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 12d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** All collateral priced by a deep aggregated feed with a deviation cap (kills the pair); Caps are set from measured venue depth and enforced on-chain; The action is sized from realised transfer amounts, so price is never an input
- **Disclosure channel, if public:** https://www.symm.io/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 18. Symbiosis — Tier 2 — URGENCY 66.0

- **Protocol:** `symbiosis` · Cross Chain Bridge · Ethereum, Tron, Bitcoin, TON, Binance
- **DefiLlama:** https://defillama.com/protocol/symbiosis
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $8,735,933
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 66.0 / EVIDENCE_CONFIDENCE 71.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 12.0/25 · precondition match 9.0/15
- **Why the clock is hot:**
    - deployed on Berachain, Cronos, Kava, Sei, ZetaChain, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: 2 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://symbiosis.finance
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 19. EmpireDEX — Tier 2 — URGENCY 66.0

- **Protocol:** `empiredex` · Dexs · Binance, Cronos, Ethereum, xDai, Avalanche
- **DefiLlama:** https://defillama.com/protocol/empiredex
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $2,733,455
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 66.0 / EVIDENCE_CONFIDENCE 77.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 12.0/25 · precondition match 9.0/15
- **Why the clock is hot:**
    - deployed on Cronos, Kava, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: 3 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 20. Carbon Defi — Tier 2 — URGENCY 66.0

- **Protocol:** `carbon-defi` · Dexs · Ethereum, Sei, Coti, Celo, TAC
- **DefiLlama:** https://defillama.com/protocol/carbon-defi
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $1,490,464
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 66.0 / EVIDENCE_CONFIDENCE 77.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 12.0/25 · precondition match 9.0/15
- **Why the clock is hot:**
    - deployed on Sei, TAC, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: 2 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://app.carbondefi.xyz/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 21. Hashport — Tier 2 — URGENCY 66.0

- **Protocol:** `hashport` · Bridge · Ethereum, Hedera, Avalanche, Binance, Polygon
- **DefiLlama:** https://defillama.com/protocol/hashport
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $1,173,479
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 66.0 / EVIDENCE_CONFIDENCE 77.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 12.0/25 · precondition match 9.0/15
- **Why the clock is hot:**
    - deployed on Cronos, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: 3 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://www.hashport.network
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 22. Sudoswap V2 — Tier 2 — URGENCY 66.0

- **Protocol:** `sudoswap-v2` · NFT Marketplace · Ethereum, Base, Berachain, Arbitrum
- **DefiLlama:** https://defillama.com/protocol/sudoswap-v2
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $705,817
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 66.0 / EVIDENCE_CONFIDENCE 77.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 12.0/25 · precondition match 9.0/15
- **Why the clock is hot:**
    - deployed on Berachain, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: 2 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://sudoswap.xyz
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 23. NerveBridge — Tier 2 — URGENCY 66.0

- **Protocol:** `nervebridge` · Bridge · Binance, Ethereum, Tron, Linea, Polygon
- **DefiLlama:** https://defillama.com/protocol/nervebridge
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $609,902
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 66.0 / EVIDENCE_CONFIDENCE 77.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 12.0/25 · precondition match 9.0/15
- **Why the clock is hot:**
    - deployed on Cronos, Kava, ZetaChain, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: 2 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://nerve.network/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 24. WAGMI — Tier 2 — URGENCY 66.0

- **Protocol:** `wagmi` · Dexs · Sonic, Kava, Metis, IOTA EVM, zkSync Era
- **DefiLlama:** https://defillama.com/protocol/wagmi
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $225,182
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 66.0 / EVIDENCE_CONFIDENCE 77.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 12.0/25 · precondition match 9.0/15
- **Why the clock is hot:**
    - deployed on Kava, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: 2 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://wagmi.com/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 25. BrownFi V3 — Tier 2 — URGENCY 66.0

- **Protocol:** `brownfi-v3` · Dexs · Berachain, Hyperliquid L1, Robinhood Chain, Linea, Arbitrum
- **DefiLlama:** https://defillama.com/protocol/brownfi-v3
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $184,934
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 66.0 / EVIDENCE_CONFIDENCE 77.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 12.0/25 · precondition match 9.0/15
- **Why the clock is hot:**
    - deployed on Berachain, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: 2 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://brownfi.io/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 26. Kinetix AMM V3 — Tier 2 — URGENCY 66.0

- **Protocol:** `kinetix-amm-v3` · Dexs · Kava, Base
- **DefiLlama:** https://defillama.com/protocol/kinetix-amm-v3
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $128,064
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 66.0 / EVIDENCE_CONFIDENCE 77.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 12.0/25 · precondition match 9.0/15
- **Why the clock is hot:**
    - deployed on Kava, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: 3 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 27. Nabla Finance — Tier 2 — URGENCY 66.0

- **Protocol:** `nabla-finance` · Dexs · Arbitrum, Hyperliquid L1, Monad, Berachain, Base
- **DefiLlama:** https://defillama.com/protocol/nabla-finance
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $75,291
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 66.0 / EVIDENCE_CONFIDENCE 77.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 12.0/25 · precondition match 9.0/15
- **Why the clock is hot:**
    - deployed on Berachain, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: 4 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 28. Crypto.com Liquid Staking — Tier 2 — URGENCY 45

- **Protocol:** `crypto.com-liquid-staking` · Liquid Staking · Cronos, Solana
- **DefiLlama:** https://defillama.com/protocol/crypto.com-liquid-staking
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $30,941,482
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - deployed on Cronos, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://crypto.com/staking
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 29. PumpBTC — Tier 2 — URGENCY 45

- **Protocol:** `pumpbtc` · Bridge · Bitcoin, Binance, Ethereum, Base, Arbitrum
- **DefiLlama:** https://defillama.com/protocol/pumpbtc
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $27,038,551
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - deployed on Sei, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://pumpbtc.xyz/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 30. Kodiak Islands — Tier 2 — URGENCY 45

- **Protocol:** `kodiak-islands` · Liquidity Manager · Berachain
- **DefiLlama:** https://defillama.com/protocol/kodiak-islands
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $24,651,774
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - deployed on Berachain, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://app.kodiak.finance
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 31. Infrared Finance — Tier 2 — URGENCY 45

- **Protocol:** `infrared-finance` · Liquid Staking · Berachain
- **DefiLlama:** https://defillama.com/protocol/infrared-finance
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $19,294,546
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - deployed on Berachain, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://infrared.finance
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 32. Moonlander — Tier 2 — URGENCY 45

- **Protocol:** `moonlander` · Derivatives · Cronos, Cronos zkEVM
- **DefiLlama:** https://defillama.com/protocol/moonlander
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $19,097,589
- **Matched family:** `ORACLE-STALE-OR-SILENT-FALLBACK`
    - broken invariant: A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - deployed on Cronos, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 35d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Disclosure channel, if public:** https://moonlander.trade/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 33. Kodiak V3 — Tier 2 — URGENCY 45

- **Protocol:** `kodiak-v3` · Dexs · Berachain
- **DefiLlama:** https://defillama.com/protocol/kodiak-v3
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $15,900,561
- **Matched family:** `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`
    - broken invariant: A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 14.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - deployed on Berachain, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 127d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Disclosure channel, if public:** https://app.kodiak.finance
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 34. Saphyre V3 — Tier 2 — URGENCY 45

- **Protocol:** `saphyre-v3` · Dexs · Sei
- **DefiLlama:** https://defillama.com/protocol/saphyre-v3
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $13,393,930
- **Matched family:** `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`
    - broken invariant: A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 14.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - deployed on Sei, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 127d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Disclosure channel, if public:** https://saphyre.xyz/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 35. Fulcrom Perps — Tier 2 — URGENCY 45

- **Protocol:** `fulcrom-perps` · Derivatives · Cronos, zkSync Era, Cronos zkEVM
- **DefiLlama:** https://defillama.com/protocol/fulcrom-perps
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $12,578,372
- **Matched family:** `ORACLE-STALE-OR-SILENT-FALLBACK`
    - broken invariant: A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - deployed on Cronos, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 35d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Disclosure channel, if public:** https://fulcrom.finance
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 36. Kava Mint — Tier 2 — URGENCY 45

- **Protocol:** `kava-mint` · CDP · Kava
- **DefiLlama:** https://defillama.com/protocol/kava-mint
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $11,970,990
- **Matched family:** `ORACLE-STALE-OR-SILENT-FALLBACK`
    - broken invariant: A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - deployed on Kava, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 35d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Disclosure channel, if public:** https://www.kava.io/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 37. ACryptoS — Tier 2 — URGENCY 45

- **Protocol:** `acryptos` · Liquidity Manager · Binance, Arbitrum, Avalanche, Base, Astar
- **DefiLlama:** https://defillama.com/protocol/acryptos
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $10,538,629
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - deployed on Canto, Cronos, Kava, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://www.acryptos.com/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 38. BEND — Tier 2 — URGENCY 45

- **Protocol:** `bend` · Lending · Berachain
- **DefiLlama:** https://defillama.com/protocol/bend
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $10,080,252
- **Matched family:** `ORACLE-STALE-OR-SILENT-FALLBACK`
    - broken invariant: A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - deployed on Berachain, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 35d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Disclosure channel, if public:** https://bend.berachain.com
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 39. Hydro LST — Tier 2 — URGENCY 45

- **Protocol:** `hydro-lst` · Liquid Staking · Injective
- **DefiLlama:** https://defillama.com/protocol/hydro-lst
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $10,022,164
- **Matched family:** `AUTH-MISSING-ON-VALUE-MOVING-PATH`
    - broken invariant: Every function that moves value or rebinds a privileged address must require a role the caller cannot obtain.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 20.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - deployed on Injective, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 30d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Every value-moving selector reverts for an unprivileged caller in simulation (kills the pair); Contract holds no value and controls no role
- **Disclosure channel, if public:** https://app.hydroprotocol.finance
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 40. Astroport — Tier 2 — URGENCY 45

- **Protocol:** `astroport` · Dexs · Neutron, Terra2, Injective, Osmosis, Sei
- **DefiLlama:** https://defillama.com/protocol/astroport
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $9,590,425
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - deployed on Injective, Sei, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://astroport.fi
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 41. Scrub Invest — Tier 2 — URGENCY 45

- **Protocol:** `scrub-invest` · Yield · Kava
- **DefiLlama:** https://defillama.com/protocol/scrub-invest
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $7,196,158
- **Matched family:** `ACC-DONATION-UNACCOUNTED-BALANCE`
    - broken invariant: A share price, exchange rate or totalAssets must be a function of value the protocol accounted for on entry. Reading a raw balance makes any direct transfer into the accounting boundary an unpriced increase in every holder's claim.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - deployed on Kava, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 52d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** totalAssets derived from an internal counter, not balanceOf (kills the pair); Rate is monotonic and rate-limited per block; Inbound transfers to the accounting boundary are rejected or swept to a reserve
- **Disclosure channel, if public:** https://invest.scrub.money/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 42. Kava Lend — Tier 2 — URGENCY 45

- **Protocol:** `kava-lend` · Lending · Kava
- **DefiLlama:** https://defillama.com/protocol/kava-lend
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $6,543,869
- **Matched family:** `ORACLE-STALE-OR-SILENT-FALLBACK`
    - broken invariant: A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - deployed on Kava, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 35d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Disclosure channel, if public:** https://app.kava.io/lend
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 43. Stride — Tier 2 — URGENCY 45

- **Protocol:** `stride` · Liquid Staking · Cosmos, HAQQ, Celestia, Osmosis, Injective
- **DefiLlama:** https://defillama.com/protocol/stride
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $5,745,325
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - deployed on Berachain, Dymension, Evmos, Injective, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://stride.zone/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 44. Folks Finance xChain — Tier 2 — URGENCY 45

- **Protocol:** `folks-finance-xchain` · Lending · Avalanche, Polygon, Monad, Ethereum, Arbitrum
- **DefiLlama:** https://defillama.com/protocol/folks-finance-xchain
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $5,461,569
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - deployed on Sei, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://xapp.folks.finance
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 45. Hydro Lending — Tier 2 — URGENCY 45

- **Protocol:** `hydro-lending` · Lending · Injective
- **DefiLlama:** https://defillama.com/protocol/hydro-lending
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $4,939,361
- **Matched family:** `ORACLE-STALE-OR-SILENT-FALLBACK`
    - broken invariant: A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - deployed on Injective, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 35d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Disclosure channel, if public:** https://app.hydroprotocol.finance/lending
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 46. VVS Flawless — Tier 2 — URGENCY 45

- **Protocol:** `vvs-flawless` · Dexs · Cronos
- **DefiLlama:** https://defillama.com/protocol/vvs-flawless
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $4,935,112
- **Matched family:** `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`
    - broken invariant: A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 14.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - deployed on Cronos, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 127d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Disclosure channel, if public:** https://vvs.finance/liquidity
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 47. Takara Lend — Tier 2 — URGENCY 45

- **Protocol:** `takara-lend` · Lending · Sei
- **DefiLlama:** https://defillama.com/protocol/takara-lend
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $4,831,963
- **Matched family:** `ORACLE-STALE-OR-SILENT-FALLBACK`
    - broken invariant: A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - deployed on Sei, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 35d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Disclosure channel, if public:** https://app.takaralend.com/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 48. Splashing Stake — Tier 2 — URGENCY 45

- **Protocol:** `splashing-stake` · Liquid Staking · Sei
- **DefiLlama:** https://defillama.com/protocol/splashing-stake
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $4,562,731
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - deployed on Sei, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://www.splashing.xyz/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 49. Blueshift — Tier 2 — URGENCY 45

- **Protocol:** `blueshift` · Dexs · BOB, Kava, Polygon, Milkomeda, Milkomeda A1
- **DefiLlama:** https://defillama.com/protocol/blueshift
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $4,461,165
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - deployed on Kava, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://blueshift.fi/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 50. YeiLend — Tier 2 — URGENCY 45

- **Protocol:** `yeilend` · Lending · Sei
- **DefiLlama:** https://defillama.com/protocol/yeilend
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $4,240,357
- **Matched family:** `ORACLE-STALE-OR-SILENT-FALLBACK`
    - broken invariant: A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - deployed on Sei, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 35d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Disclosure channel, if public:** https://www.yei.finance
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 51. TruStake — Tier 2 — URGENCY 45

- **Protocol:** `trustake` · Liquid Staking · Aptos, Injective, Near, Solana, Ethereum
- **DefiLlama:** https://defillama.com/protocol/trustake
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $4,045,526
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - deployed on Injective, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://app.truyields.com
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 52. Ferro — Tier 2 — URGENCY 45

- **Protocol:** `ferro` · Dexs · Cronos
- **DefiLlama:** https://defillama.com/protocol/ferro
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $3,611,584
- **Matched family:** `AMM-POOL-RATIO-SKEW-EXTRACTION`
    - broken invariant: A pool's invariant and fee schedule must ensure that any round trip through it costs the trader at least the fees, for every reachable ratio, including extreme imbalance.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 42.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - deployed on Cronos, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 39d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Round-trip non-profitability proven across the ratio range (kills the pair); Standard constant-product with a fee floor
- **Disclosure channel, if public:** https://ferroprotocol.com
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 53. Sablier Lockup — Tier 2 — URGENCY 45

- **Protocol:** `sablier-lockup` · Payments · Ethereum, Sonic, Polygon, Solana, Arbitrum
- **DefiLlama:** https://defillama.com/protocol/sablier-lockup
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $3,008,551
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - deployed on Berachain, Sei, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://sablier.com/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 54. Lair Finance — Tier 2 — URGENCY 45

- **Protocol:** `lair-finance` · Liquid Staking · Klaytn, Somnia, Berachain
- **DefiLlama:** https://defillama.com/protocol/lair-finance
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $2,868,726
- **Matched family:** `AUTH-MISSING-ON-VALUE-MOVING-PATH`
    - broken invariant: Every function that moves value or rebinds a privileged address must require a role the caller cannot obtain.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 20.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - deployed on Berachain, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 30d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Every value-moving selector reverts for an unprivileged caller in simulation (kills the pair); Contract holds no value and controls no role
- **Disclosure channel, if public:** https://lair.fi
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 55. LayerBank — Tier 2 — URGENCY 45

- **Protocol:** `layerbank` · Lending · RSK, Manta, BOB, Plume Mainnet, Taiko
- **DefiLlama:** https://defillama.com/protocol/layerbank
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $2,745,375
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - deployed on Nibiru, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://layerbank.finance
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 56. HiYield — Tier 2 — URGENCY 45

- **Protocol:** `hiyield` · RWA · Avalanche, Canto
- **DefiLlama:** https://defillama.com/protocol/hiyield
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $2,740,578
- **Matched family:** `SETTLEMENT-EPOCH-BOUNDARY-CREDIT`
    - broken invariant: A quantity fixed for an epoch must not be claimable against a position established after that quantity was set, and entitlement must be prorated by time actually held.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 42.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 20.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - deployed on Canto, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 25d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Entitlement time-weighted (kills the pair); Deposits queued to the next epoch
- **Disclosure channel, if public:** https://www.hiyield.xyz
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 57. Neptune Finance — Tier 2 — URGENCY 45

- **Protocol:** `neptune-finance` · Lending · Injective
- **DefiLlama:** https://defillama.com/protocol/neptune-finance
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $2,570,126
- **Matched family:** `ORACLE-STALE-OR-SILENT-FALLBACK`
    - broken invariant: A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - deployed on Injective, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 35d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Disclosure channel, if public:** https://nept.finance/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 58. DyorSwap AMM — Tier 2 — URGENCY 45

- **Protocol:** `dyorswap-amm` · Dexs · X Layer, Blast, Ink, Plasma, Unichain
- **DefiLlama:** https://defillama.com/protocol/dyorswap-amm
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $2,548,809
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - deployed on ZetaChain, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://dyorswap.finance/?chainId=34443
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 59. Cabal — Tier 2 — URGENCY 45

- **Protocol:** `cabal` · Governance Incentives · Cabal, Initia
- **DefiLlama:** https://defillama.com/protocol/cabal
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $2,512,486
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - deployed on Initia, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://thecabal.xyz
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 60. Balanced Exchange — Tier 2 — URGENCY 45

- **Protocol:** `balanced-exchange` · Dexs · Avalanche, Icon, Solana, Arbitrum, Binance
- **DefiLlama:** https://defillama.com/protocol/balanced-exchange
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $2,143,905
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - deployed on Injective, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://app.balanced.network/trade
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 61. Eris Protocol — Tier 2 — URGENCY 45

- **Protocol:** `eris-protocol` · Liquid Staking · Terra2, Nibiru, Terra, Chihuahua, Injective
- **DefiLlama:** https://defillama.com/protocol/eris-protocol
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $2,121,837
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - deployed on Injective, Nibiru, Sei, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://www.erisprotocol.com
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 62. InitiaDEX — Tier 2 — URGENCY 45

- **Protocol:** `initiadex` · Dexs · Initia
- **DefiLlama:** https://defillama.com/protocol/initiadex
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $1,946,108
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - deployed on Initia, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://app.initia.xyz/swap
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 63. Pumex — Tier 2 — URGENCY 45

- **Protocol:** `pumex` · DEX Aggregator · Injective
- **DefiLlama:** https://defillama.com/protocol/pumex
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $1,865,901
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - deployed on Injective, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://www.pumex.fi/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 64. LlamaPay — Tier 2 — URGENCY 45

- **Protocol:** `llamapay` · Payments · Binance, Ethereum, Arbitrum, Optimism, xDai
- **DefiLlama:** https://defillama.com/protocol/llamapay
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $1,593,539
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - deployed on Berachain, Cronos, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://llamapay.io
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 65. Canto Lending — Tier 2 — URGENCY 45

- **Protocol:** `canto-lending` · Lending · Canto
- **DefiLlama:** https://defillama.com/protocol/canto-lending
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $1,444,823
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - deployed on Canto, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 66. MM Finance Cronos — Tier 2 — URGENCY 45

- **Protocol:** `mm-finance-cronos` · Dexs · Cronos
- **DefiLlama:** https://defillama.com/protocol/mm-finance-cronos
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $1,338,790
- **Matched family:** `AUTH-MISSING-ON-VALUE-MOVING-PATH`
    - broken invariant: Every function that moves value or rebinds a privileged address must require a role the caller cannot obtain.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 20.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - deployed on Cronos, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 30d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Every value-moving selector reverts for an unprivileged caller in simulation (kills the pair); Contract holds no value and controls no role
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 67. CGO Finance — Tier 2 — URGENCY 45

- **Protocol:** `cgo-finance` · Yield Aggregator · Cronos
- **DefiLlama:** https://defillama.com/protocol/cgo-finance
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $1,069,137
- **Matched family:** `AUTH-MISSING-ON-VALUE-MOVING-PATH`
    - broken invariant: Every function that moves value or rebinds a privileged address must require a role the caller cannot obtain.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 20.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - deployed on Cronos, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 30d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Every value-moving selector reverts for an unprivileged caller in simulation (kills the pair); Contract holds no value and controls no role
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 68. Kava Earn — Tier 2 — URGENCY 45

- **Protocol:** `kava-earn` · Yield Aggregator · Kava
- **DefiLlama:** https://defillama.com/protocol/kava-earn
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $936,230
- **Matched family:** `ACC-ZERO-SUPPLY-INFLATION`
    - broken invariant: The first depositor must not be able to set an arbitrary asset-per-share ratio, and no operation may drive supply low enough to restore that branch.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 20.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - deployed on Kava, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 9d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Dead shares minted at creation (kills the pair); Vault creation is permissioned and every vault is seeded; Virtual offset present in the deployed bytecode
- **Disclosure channel, if public:** https://app.kava.io/home
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 69. Kava Liquid — Tier 2 — URGENCY 45

- **Protocol:** `kava-liquid` · Liquid Staking · Kava
- **DefiLlama:** https://defillama.com/protocol/kava-liquid
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $914,769
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - deployed on Kava, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://app.kava.io/mint
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 70. BEX — Tier 2 — URGENCY 45

- **Protocol:** `bex` · Dexs · Berachain
- **DefiLlama:** https://defillama.com/protocol/bex
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $788,003
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - deployed on Berachain, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://hub.berachain.com/swap/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 71. Smilee Finance gBERA — Tier 2 — URGENCY 45

- **Protocol:** `smilee-finance-gbera` · Liquid Staking · Berachain
- **DefiLlama:** https://defillama.com/protocol/smilee-finance-gbera
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $726,230
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - deployed on Berachain, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://smilee.finance/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 72. Sablier Flow — Tier 2 — URGENCY 45

- **Protocol:** `sablier-flow` · Payments · Ethereum, Arbitrum, Binance, Base, Optimism
- **DefiLlama:** https://defillama.com/protocol/sablier-flow
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $689,782
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - deployed on Berachain, Sei, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://app.sablier.com/payments/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 73. Helix Spot — Tier 2 — URGENCY 45

- **Protocol:** `helix-spot` · Dexs · Injective
- **DefiLlama:** https://defillama.com/protocol/helix-spot
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $654,431
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - deployed on Injective, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://helixapp.com
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 74. Goldilocks — Tier 2 — URGENCY 45

- **Protocol:** `goldilocks` · Yield · Berachain
- **DefiLlama:** https://defillama.com/protocol/goldilocks
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $545,784
- **Matched family:** `AUTH-MISSING-ON-VALUE-MOVING-PATH`
    - broken invariant: Every function that moves value or rebinds a privileged address must require a role the caller cannot obtain.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 20.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - deployed on Berachain, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 30d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Every value-moving selector reverts for an unprivileged caller in simulation (kills the pair); Contract holds no value and controls no role
- **Disclosure channel, if public:** https://www.goldilocksdao.io/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 75. Shido Dex V3 — Tier 2 — URGENCY 45

- **Protocol:** `shido-dex-v3` · Dexs · Shido
- **DefiLlama:** https://defillama.com/protocol/shido-dex-v3
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $512,899
- **Matched family:** `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`
    - broken invariant: A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 14.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - deployed on Shido, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 127d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Disclosure channel, if public:** https://shido.io/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 76. Ebisus Bay — Tier 2 — URGENCY 45

- **Protocol:** `ebisus-bay` · Dexs · Cronos, Cronos zkEVM
- **DefiLlama:** https://defillama.com/protocol/ebisus-bay
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $503,133
- **Matched family:** `AUTH-MISSING-ON-VALUE-MOVING-PATH`
    - broken invariant: Every function that moves value or rebinds a privileged address must require a role the caller cannot obtain.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 20.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - deployed on Cronos, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 30d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Every value-moving selector reverts for an unprivileged caller in simulation (kills the pair); Contract holds no value and controls no role
- **Disclosure channel, if public:** https://app.ebisusbay.com/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 77. Counterstake — Tier 2 — URGENCY 45

- **Protocol:** `counterstake` · Cross Chain Bridge · Obyte, Ethereum, Binance, Polygon, Kava
- **DefiLlama:** https://defillama.com/protocol/counterstake
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $464,930
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - deployed on Kava, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://counterstake.org
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 78. Obsidian — Tier 2 — URGENCY 45

- **Protocol:** `obsidian` · DEX Aggregator · Cronos, Cronos zkEVM
- **DefiLlama:** https://defillama.com/protocol/obsidian
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $461,667
- **Matched family:** `AUTH-MISSING-ON-VALUE-MOVING-PATH`
    - broken invariant: Every function that moves value or rebinds a privileged address must require a role the caller cannot obtain.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 20.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - deployed on Cronos, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 30d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Every value-moving selector reverts for an unprivileged caller in simulation (kills the pair); Contract holds no value and controls no role
- **Disclosure channel, if public:** https://obsidian.finance
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 79. Beradrome — Tier 2 — URGENCY 45

- **Protocol:** `beradrome` · Yield · Berachain
- **DefiLlama:** https://defillama.com/protocol/beradrome
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $448,175
- **Matched family:** `AUTH-MISSING-ON-VALUE-MOVING-PATH`
    - broken invariant: Every function that moves value or rebinds a privileged address must require a role the caller cannot obtain.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 20.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - deployed on Berachain, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 30d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Every value-moving selector reverts for an unprivileged caller in simulation (kills the pair); Contract holds no value and controls no role
- **Disclosure channel, if public:** https://www.beradrome.com
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 80. White Whale Dex — Tier 2 — URGENCY 45

- **Protocol:** `white-whale-dex` · Dexs · Terra2, Chihuahua, Osmosis, Juno, Sei
- **DefiLlama:** https://defillama.com/protocol/white-whale-dex
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $445,849
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - deployed on Injective, Sei, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://app.whitewhale.money/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 81. Mito Finance — Tier 2 — URGENCY 45

- **Protocol:** `mito-finance` · Liquidity Manager · Injective
- **DefiLlama:** https://defillama.com/protocol/mito-finance
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $423,546
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - deployed on Injective, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://mito.fi
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 82. Dojoswap AMM — Tier 2 — URGENCY 45

- **Protocol:** `dojoswap-amm` · Dexs · Injective
- **DefiLlama:** https://defillama.com/protocol/dojoswap-amm
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $415,362
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - deployed on Injective, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 83. Kodiak V2 — Tier 2 — URGENCY 45

- **Protocol:** `kodiak-v2` · Dexs · Berachain
- **DefiLlama:** https://defillama.com/protocol/kodiak-v2
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $410,823
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - deployed on Berachain, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://app.kodiak.finance
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 84. CronaSwap — Tier 2 — URGENCY 45

- **Protocol:** `cronaswap` · Dexs · Cronos
- **DefiLlama:** https://defillama.com/protocol/cronaswap
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $410,471
- **Matched family:** `AUTH-MISSING-ON-VALUE-MOVING-PATH`
    - broken invariant: Every function that moves value or rebinds a privileged address must require a role the caller cannot obtain.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 20.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - deployed on Cronos, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 30d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Every value-moving selector reverts for an unprivileged caller in simulation (kills the pair); Contract holds no value and controls no role
- **Disclosure channel, if public:** https://app.cronaswap.org
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 85. Shoebill V2 — Tier 2 — URGENCY 45

- **Protocol:** `shoebill-v2` · Lending · Manta, BSquared, zkLink, BOB, Mode
- **DefiLlama:** https://defillama.com/protocol/shoebill-v2
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $388,866
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - deployed on ZetaChain, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://shoebill.finance
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 86. Knit Finance — Tier 2 — URGENCY 45

- **Protocol:** `knit-finance` · Bridge · Ethereum, Polygon, Kava, Avalanche, Heco
- **DefiLlama:** https://defillama.com/protocol/knit-finance
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $383,876
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - deployed on Kava, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://knit.finance
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 87. Black Panther — Tier 2 — URGENCY 45

- **Protocol:** `black-panther` · Yield · Injective
- **DefiLlama:** https://defillama.com/protocol/black-panther
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $373,619
- **Matched family:** `ACC-ZERO-SUPPLY-INFLATION`
    - broken invariant: The first depositor must not be able to set an arbitrary asset-per-share ratio, and no operation may drive supply low enough to restore that branch.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 20.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - deployed on Injective, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 9d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Dead shares minted at creation (kills the pair); Vault creation is permissioned and every vault is seeded; Virtual offset present in the deployed bytecode
- **Disclosure channel, if public:** https://blackpanther.fi
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 88. Saphyre V2 — Tier 2 — URGENCY 45

- **Protocol:** `saphyre-v2` · Dexs · Sei
- **DefiLlama:** https://defillama.com/protocol/saphyre-v2
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $372,239
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - deployed on Sei, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://saphyre.xyz/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 89. Teahouse Managed — Tier 2 — URGENCY 45

- **Protocol:** `teahouse-managed` · Yield Aggregator · Ethereum, Arbitrum, Sei, Optimism, Polygon
- **DefiLlama:** https://defillama.com/protocol/teahouse-managed
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $326,424
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - deployed on Sei, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://vault.teahouse.finance
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 90. Beraborrow — Tier 2 — URGENCY 45

- **Protocol:** `beraborrow` · CDP · Berachain
- **DefiLlama:** https://defillama.com/protocol/beraborrow
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $286,442
- **Matched family:** `ORACLE-STALE-OR-SILENT-FALLBACK`
    - broken invariant: A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - deployed on Berachain, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 35d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Disclosure channel, if public:** https://app.beraborrow.com/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 91. Choice Exchange — Tier 2 — URGENCY 45

- **Protocol:** `choice-exchange` · Dexs · Injective
- **DefiLlama:** https://defillama.com/protocol/choice-exchange
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $238,154
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - deployed on Injective, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://choice.exchange
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 92. Argo Finance — Tier 2 — URGENCY 45

- **Protocol:** `argo-finance` · Liquid Staking · Cronos
- **DefiLlama:** https://defillama.com/protocol/argo-finance
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $237,101
- **Matched family:** `AUTH-MISSING-ON-VALUE-MOVING-PATH`
    - broken invariant: Every function that moves value or rebinds a privileged address must require a role the caller cannot obtain.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 20.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - deployed on Cronos, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 30d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Every value-moving selector reverts for an unprivileged caller in simulation (kills the pair); Contract holds no value and controls no role
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 93. Shido Dex V2 — Tier 2 — URGENCY 45

- **Protocol:** `shido-dex-v2` · Dexs · Shido
- **DefiLlama:** https://defillama.com/protocol/shido-dex-v2
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $216,754
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - deployed on Shido, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://shido.io/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 94. Crystl Finance — Tier 2 — URGENCY 45

- **Protocol:** `crystl-finance` · Yield · Binance, Cronos, Polygon
- **DefiLlama:** https://defillama.com/protocol/crystl-finance
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $208,951
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - deployed on Cronos, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 95. Inertia Bridge — Tier 2 — URGENCY 45

- **Protocol:** `inertia-bridge` · Canonical Bridge · Initia
- **DefiLlama:** https://defillama.com/protocol/inertia-bridge
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $194,856
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - deployed on Initia, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://inrt.fi/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 96. Sai — Tier 2 — URGENCY 45

- **Protocol:** `sai` · Derivatives · Nibiru
- **DefiLlama:** https://defillama.com/protocol/sai
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $194,198
- **Matched family:** `ORACLE-STALE-OR-SILENT-FALLBACK`
    - broken invariant: A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - deployed on Nibiru, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 35d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Disclosure channel, if public:** https://sai.fun/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 97. BackBone Labs — Tier 2 — URGENCY 45

- **Protocol:** `backbone-labs` · Liquid Staking · Terra2, Osmosis, Injective, Chihuahua, Juno
- **DefiLlama:** https://defillama.com/protocol/backbone-labs
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $184,057
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - deployed on Injective, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://app.backbonelabs.io/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 98. HARD Swap — Tier 2 — URGENCY 45

- **Protocol:** `hard-swap` · Dexs · Kava
- **DefiLlama:** https://defillama.com/protocol/hard-swap
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $168,195
- **Matched family:** `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`
    - broken invariant: A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 14.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - deployed on Kava, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 127d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Disclosure channel, if public:** https://swap.hard.fun/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 99. Kava Swap — Tier 2 — URGENCY 45

- **Protocol:** `kava-swap` · Dexs · Kava
- **DefiLlama:** https://defillama.com/protocol/kava-swap
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $166,883
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - deployed on Kava, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://app.kava.io/swap/pools
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 100. Kogefarm — Tier 2 — URGENCY 45

- **Protocol:** `kogefarm` · Yield · Polygon, Fantom, Kava, Moonriver
- **DefiLlama:** https://defillama.com/protocol/kogefarm
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $158,988
- **Matched family:** `AUTH-MISSING-ON-VALUE-MOVING-PATH`
    - broken invariant: Every function that moves value or rebinds a privileged address must require a role the caller cannot obtain.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 20.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - deployed on Kava, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 30d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Every value-moving selector reverts for an unprivileged caller in simulation (kills the pair); Contract holds no value and controls no role
- **Disclosure channel, if public:** https://kogefarm.io
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 101. Accumulated Finance Lending — Tier 2 — URGENCY 45

- **Protocol:** `accumulated-finance-lending` · Lending · Bitkub, Coti, ZetaChain, Velas, Sapphire
- **DefiLlama:** https://defillama.com/protocol/accumulated-finance-lending
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $156,894
- **Matched family:** `ORACLE-STALE-OR-SILENT-FALLBACK`
    - broken invariant: A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - deployed on ZetaChain, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 35d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Disclosure channel, if public:** https://accumulated.finance/lend
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 102. Echelon Initia Bridge — Tier 2 — URGENCY 45

- **Protocol:** `echelon-initia-bridge` · Canonical Bridge · Initia
- **DefiLlama:** https://defillama.com/protocol/echelon-initia-bridge
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $136,323
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - deployed on Initia, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://echelon.market/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 103. Astrovault — Tier 2 — URGENCY 45

- **Protocol:** `astrovault` · Dexs · Archway, Nibiru, Neutron
- **DefiLlama:** https://defillama.com/protocol/astrovault
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $123,761
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - deployed on Nibiru, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://astrovault.io
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 104. Jiko — Tier 2 — URGENCY 45

- **Protocol:** `jiko` · Gaming · Berachain
- **DefiLlama:** https://defillama.com/protocol/jiko
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $121,608
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - deployed on Berachain, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://app.jiko.finance/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 105. Crodex — Tier 2 — URGENCY 45

- **Protocol:** `crodex` · Dexs · Cronos
- **DefiLlama:** https://defillama.com/protocol/crodex
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $114,255
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - deployed on Cronos, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://swap.crodex.app
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 106. PhotonSwap Finance — Tier 2 — URGENCY 45

- **Protocol:** `photonswap-finance` · Dexs · Cronos, Kava, Evmos
- **DefiLlama:** https://defillama.com/protocol/photonswap-finance
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $109,726
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - deployed on Cronos, Evmos, Kava, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://photonswap.finance
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 107. SiloStake — Tier 2 — URGENCY 45

- **Protocol:** `silostake` · Liquid Staking · Sei
- **DefiLlama:** https://defillama.com/protocol/silostake
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $109,483
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - deployed on Sei, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 108. Crow Finance — Tier 2 — URGENCY 45

- **Protocol:** `crow-finance` · Dexs · Cronos
- **DefiLlama:** https://defillama.com/protocol/crow-finance
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $103,776
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - deployed on Cronos, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 109. Canto Dex — Tier 2 — URGENCY 45

- **Protocol:** `canto-dex` · Dexs · Canto
- **DefiLlama:** https://defillama.com/protocol/canto-dex
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $100,175
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - deployed on Canto, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 110. Dojoswap LSD — Tier 2 — URGENCY 45

- **Protocol:** `dojoswap-lsd` · Liquid Staking · Injective
- **DefiLlama:** https://defillama.com/protocol/dojoswap-lsd
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $93,480
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - deployed on Injective, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 111. Equilibre — Tier 2 — URGENCY 45

- **Protocol:** `equilibre` · Dexs · Kava
- **DefiLlama:** https://defillama.com/protocol/equilibre
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $71,785
- **Matched family:** `AUTH-MISSING-ON-VALUE-MOVING-PATH`
    - broken invariant: Every function that moves value or rebinds a privileged address must require a role the caller cannot obtain.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 20.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - deployed on Kava, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 30d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Every value-moving selector reverts for an unprivileged caller in simulation (kills the pair); Contract holds no value and controls no role
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 112. NOXA DEX V2 — Tier 2 — URGENCY 45

- **Protocol:** `noxa-dex-v2` · Dexs · Abstract, Hyperliquid L1, Monad, Berachain, Plasma
- **DefiLlama:** https://defillama.com/protocol/noxa-dex-v2
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $71,263
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - deployed on Berachain, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://fun.noxa.eth.limo/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 113. Avalon USDaLend — Tier 2 — URGENCY 45

- **Protocol:** `avalon-usdalend` · Lending · IoTeX, Sonic, Sei, Zircuit, Taiko
- **DefiLlama:** https://defillama.com/protocol/avalon-usdalend
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $69,969
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - deployed on Sei, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://usdalend.avalonfinance.xyz/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 114. EddyFinance AMM — Tier 2 — URGENCY 45

- **Protocol:** `eddyfinance-amm` · Dexs · ZetaChain
- **DefiLlama:** https://defillama.com/protocol/eddyfinance-amm
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $69,531
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - deployed on ZetaChain, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 115. WinnieSwap — Tier 2 — URGENCY 45

- **Protocol:** `winnieswap` · Dexs · Berachain
- **DefiLlama:** https://defillama.com/protocol/winnieswap
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $57,656
- **Matched family:** `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`
    - broken invariant: A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 14.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - deployed on Berachain, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 127d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Disclosure channel, if public:** https://winnieswap.com
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 116. Milkyway Rollup Bridge — Tier 2 — URGENCY 45

- **Protocol:** `milkyway-rollup-bridge` · Canonical Bridge · Initia
- **DefiLlama:** https://defillama.com/protocol/milkyway-rollup-bridge
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $53,078
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - deployed on Initia, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 117. Zearn Protocol — Tier 2 — URGENCY 45

- **Protocol:** `zearn-protocol` · Liquid Staking · Bitlayer, ZetaChain
- **DefiLlama:** https://defillama.com/protocol/zearn-protocol
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $51,445
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - deployed on ZetaChain, a chain running a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 precompile advisories; patch state NOT_DETERMINED
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 71d ago; 222-member population already falling
- **THE decisive check (single fastest confirm/kill):** Pin the chain's running github.com/cosmos/evm version AND query live module params for the enabled precompile set. A vendored x/evm tree will not appear in a dependency scan.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://zearn.xyz/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 118. HOPE Collateral — Tier 4 — URGENCY 66.57

- **Protocol:** `hope-collateral` · Basis Trading · Bitcoin, Ethereum
- **DefiLlama:** https://defillama.com/protocol/hope-collateral
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $1,604,842
    - relative of **hope-lend** via version sibling — that sibling is *drained or dead* and holds $158 now
- **Matched family:** `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`
    - broken invariant: A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
- **URGENCY 66.57 / EVIDENCE_CONFIDENCE 90.4** — evidence level `L4_GUARD_REVIEW`
    - remediation gap 28/40 · technique recency+propagation 4.0/20 · reachable live value 25.0/25 · precondition match 9.57/15
- **Why the clock is hot:**
    - version sibling of hope-lend, exploited on 2023-10-18; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $1,604,842.
    - reachability: 3 precondition(s) present at L4_GUARD_REVIEW, no guard found in the reviewed path
    - recency: technique public 1044d ago; 3 siblings
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 119. Arrakis V2 — Tier 4 — URGENCY 66.0

- **Protocol:** `arrakis-v2` · Liquidity Manager · Ethereum, Polygon, Arbitrum, Optimism
- **DefiLlama:** https://defillama.com/protocol/arrakis-v2
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $156,016
    - relative of **arrakis-v1** via version sibling — that sibling is *never materially hit* and holds $1,405,300 now
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 66.0 / EVIDENCE_CONFIDENCE 77.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 12.0/25 · precondition match 9.0/15
- **Why the clock is hot:**
    - version sibling of arrakis-v1, exploited on 2026-08-23; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is never materially hit; this one holds $156,016.
    - reachability: 2 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 4d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://arrakis.finance/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 120. Allbridge Classic — Tier 4 — URGENCY 63.0

- **Protocol:** `allbridge-classic` · Bridge · Ethereum, Solana, Terra, Binance, Near
- **DefiLlama:** https://defillama.com/protocol/allbridge-classic
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $1,057,520
    - relative of **allbridge-core** via version sibling — that sibling is *drained or dead* and holds $322,827 now
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 63.0 / EVIDENCE_CONFIDENCE 77.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 14.0/20 · reachable live value 12.0/25 · precondition match 9.0/15
- **Why the clock is hot:**
    - version sibling of allbridge-core, exploited on 2026-07-19; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $1,057,520.
    - reachability: 2 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 39d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://app.allbridge.io
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 121. Solv Vesting — Tier 4 — URGENCY 60.0

- **Protocol:** `solv-vesting` · RWA · Ethereum, Binance, Polygon, Arbitrum
- **DefiLlama:** https://defillama.com/protocol/solv-vesting
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $142,311
    - relative of **solvbtc** via version sibling — that sibling is *never materially hit* and holds $517,288,957 now
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 60.0 / EVIDENCE_CONFIDENCE 71.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 11.0/20 · reachable live value 12.0/25 · precondition match 9.0/15
- **Why the clock is hot:**
    - version sibling of solvbtc, exploited on 2026-03-06; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is never materially hit; this one holds $142,311.
    - reachability: 2 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 174d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://solv.finance/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 122. lpETH — Tier 4 — URGENCY 59.88

- **Protocol:** `lpeth` · Dexs · Ethereum
- **DefiLlama:** https://defillama.com/protocol/lpeth
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $639,048
    - relative of **tenderize-v2** via version sibling — that sibling is *never materially hit* and holds $340,858 now
- **Matched family:** `UPGRADE-INITIALIZER-REACHABLE-LIVE`
    - broken invariant: After deployment, no caller may (re)establish ownership, admin, or implementation wiring. Initialization state must be provably consumed.
- **URGENCY 59.88 / EVIDENCE_CONFIDENCE 69.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 4.0/20 · reachable live value 20.0/25 · precondition match 7.88/15
- **Why the clock is hot:**
    - version sibling of tenderize-v2, exploited on 2025-04-07; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is never materially hit; this one holds $639,048.
    - reachability: 2 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 507d ago; 2 siblings
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Simulated re-initialization reverts (kills the pair); Contract is non-upgradeable and holds no approvals
- **Disclosure channel, if public:** https://www.lpeth.xyz
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 123. Radiant V1 — Tier 4 — URGENCY 58.38

- **Protocol:** `radiant-v1` · Lending · Arbitrum
- **DefiLlama:** https://defillama.com/protocol/radiant-v1
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $255,921
    - relative of **radiant-v2** via version sibling — that sibling is *never materially hit* and holds $700,053 now
- **Matched family:** `ACC-DONATION-UNACCOUNTED-BALANCE`
    - broken invariant: A share price, exchange rate or totalAssets must be a function of value the protocol accounted for on entry. Reading a raw balance makes any direct transfer into the accounting boundary an unpriced increase in every holder's claim.
- **URGENCY 58.38 / EVIDENCE_CONFIDENCE 69.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 4.0/20 · reachable live value 20.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - version sibling of radiant-v2, exploited on 2024-01-02; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is never materially hit; this one holds $255,921.
    - reachability: 2 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 968d ago; 3 siblings
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** totalAssets derived from an internal counter, not balanceOf (kills the pair); Rate is monotonic and rate-limited per block; Inbound transfers to the accounting boundary are rejected or swept to a reserve
- **Disclosure channel, if public:** https://radiant.capital/#/markets
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 124. Balancer CoW AMM — Tier 4 — URGENCY 57.0

- **Protocol:** `balancer-cow-amm` · Dexs · xDai, Ethereum, Arbitrum, Base
- **DefiLlama:** https://defillama.com/protocol/balancer-cow-amm
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $59,804
    - relative of **balancer-v2** via version sibling — that sibling is *drained or dead* and holds $28,168,365 now
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 57.0 / EVIDENCE_CONFIDENCE 77.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 8.0/20 · reachable live value 12.0/25 · precondition match 9.0/15
- **Why the clock is hot:**
    - version sibling of balancer-v2, exploited on 2025-11-03; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $59,804.
    - reachability: 2 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 297d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://balancer.fi
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 125. Paraluni Dex — Tier 4 — URGENCY 55.0

- **Protocol:** `paraluni-dex` · Dexs · Binance
- **DefiLlama:** https://defillama.com/protocol/paraluni-dex
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $323,498
    - relative of **paraluni-masterchef** via version sibling — that sibling is *drained or dead* and holds $2,641 now
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 55.0 / EVIDENCE_CONFIDENCE 77.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 12.0/25 · precondition match 9.0/15
- **Why the clock is hot:**
    - version sibling of paraluni-masterchef, exploited on 2022-03-13; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $323,498.
    - reachability: 2 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 1628d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://paraluni.org
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 126. Usual EUR0 — Tier 4 — URGENCY 55.0

- **Protocol:** `usual-eur0` · RWA · Ethereum
- **DefiLlama:** https://defillama.com/protocol/usual-eur0
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $237,080
    - relative of **usual-usd0** via version sibling — that sibling is *never materially hit* and holds $91,816,484 now
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 55.0 / EVIDENCE_CONFIDENCE 77.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 12.0/25 · precondition match 9.0/15
- **Why the clock is hot:**
    - version sibling of usual-usd0, exploited on 2025-05-27; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is never materially hit; this one holds $237,080.
    - reachability: 2 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 457d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://usual.money
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 127. HOPE Swap — Tier 4 — URGENCY 55.0

- **Protocol:** `hope-swap` · Dexs · Ethereum
- **DefiLlama:** https://defillama.com/protocol/hope-swap
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $114,227
    - relative of **hope-lend** via version sibling — that sibling is *drained or dead* and holds $158 now
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 55.0 / EVIDENCE_CONFIDENCE 77.0** — evidence level `L3_STATE`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 12.0/25 · precondition match 9.0/15
- **Why the clock is hot:**
    - version sibling of hope-lend, exploited on 2023-10-18; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $114,227.
    - reachability: 3 precondition(s) present at L3_STATE, no guard found in the reviewed path
    - recency: technique public 1044d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 128. Aave V2 — Tier 4 — URGENCY 45

- **Protocol:** `aave-v2` · Lending · Ethereum, Polygon, Avalanche
- **DefiLlama:** https://defillama.com/protocol/aave-v2
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $110,942,328
    - relative of **aave-v3** via version sibling — that sibling is *never materially hit* and holds $17,400,461,288 now
- **Matched family:** `ORACLE-SPOT-THIN-LIQUIDITY`
    - broken invariant: Borrowing capacity, mint size, reward size or collateral value must not be derived from a price that a single actor can move within the manipulation window, and the value unlocked must never exceed the cost of moving that price.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 11.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - version sibling of aave-v3, exploited on 2026-03-12; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is never materially hit; this one holds $110,942,328.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 168d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** All collateral priced by a deep aggregated feed with a deviation cap (kills the pair); Caps are set from measured venue depth and enforced on-chain; The action is sized from realised transfer amounts, so price is never an input
- **Disclosure channel, if public:** https://aave.com
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 129. Rhea Dex — Tier 4 — URGENCY 45

- **Protocol:** `rhea-dex` · Dexs · Near
- **DefiLlama:** https://defillama.com/protocol/rhea-dex
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $28,024,984
    - relative of **rhea-lend** via version sibling — that sibling is *never materially hit* and holds $79,226,748 now
- **Matched family:** `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`
    - broken invariant: Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 11.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - version sibling of rhea-lend, exploited on 2026-04-16; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is never materially hit; this one holds $28,024,984.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 133d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Every identifier derived or verified against the factory/registry (kills the pair); Routing restricted to an immutable venue allowlist
- **Disclosure channel, if public:** https://dex.rhea.finance/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 130. WEMIX.FI Staking — Tier 4 — URGENCY 45

- **Protocol:** `wemix.fi-staking` · Staking Pool · WEMIX
- **DefiLlama:** https://defillama.com/protocol/wemix.fi-staking
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $19,923,463
    - relative of **wemix.fi-lend** via version sibling — that sibling is *drained or dead* and holds $1,971 now
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 14.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - version sibling of wemix.fi-lend, exploited on 2026-07-26; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $19,923,463.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 32d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://wemix.fi
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 131. RHEA LST — Tier 4 — URGENCY 45

- **Protocol:** `rhea-lst` · Liquid Staking · Near
- **DefiLlama:** https://defillama.com/protocol/rhea-lst
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $17,309,580
    - relative of **rhea-lend** via version sibling — that sibling is *never materially hit* and holds $79,226,748 now
- **Matched family:** `AUTH-MISSING-ON-VALUE-MOVING-PATH`
    - broken invariant: Every function that moves value or rebinds a privileged address must require a role the caller cannot obtain.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 11.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - version sibling of rhea-lend, exploited on 2026-04-16; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is never materially hit; this one holds $17,309,580.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 133d ago; 4-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Every value-moving selector reverts for an unprivileged caller in simulation (kills the pair); Contract holds no value and controls no role
- **Disclosure channel, if public:** https://www.rhea.finance/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 132. Summer.fi Pro — Tier 4 — URGENCY 45

- **Protocol:** `summer.fi-pro` · CDP Manager · Ethereum, Arbitrum, Optimism, Base
- **DefiLlama:** https://defillama.com/protocol/summer.fi-pro
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $17,019,561
    - relative of **lazy-summer-protocol** via version sibling — that sibling is *drained or dead* and holds $1,134 now
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 14.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - version sibling of lazy-summer-protocol, exploited on 2026-07-05; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $17,019,561.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 53d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://summer.fi/earn?referralCode=2001317
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 133. TermFinance Lend — Tier 4 — URGENCY 45

- **Protocol:** `termfinance-lend` · Lending · Ethereum, Arbitrum, Plasma, Base, Avalanche
- **DefiLlama:** https://defillama.com/protocol/termfinance-lend
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $5,167,046
    - relative of **termfinance-vaults** via version sibling — that sibling is *drained or dead* and holds $1,608,407 now
- **Matched family:** `ORACLE-STALE-OR-SILENT-FALLBACK`
    - broken invariant: A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 17.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - version sibling of termfinance-vaults, exploited on 2026-08-23; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $5,167,046.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 4d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Disclosure channel, if public:** https://term.finance
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 134. Venus Flux — Tier 4 — URGENCY 45

- **Protocol:** `venus-flux` · Lending · Binance
- **DefiLlama:** https://defillama.com/protocol/venus-flux
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $3,421,097
    - relative of **venus-core-pool** via version sibling — that sibling is *never materially hit* and holds $1,270,393,387 now
- **Matched family:** `ORACLE-STALE-OR-SILENT-FALLBACK`
    - broken invariant: A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 11.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - version sibling of venus-core-pool, exploited on 2026-03-15; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is never materially hit; this one holds $3,421,097.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 165d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Disclosure channel, if public:** https://flux.venus.io/lending/56
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 135. Aftermath afSUI — Tier 4 — URGENCY 45

- **Protocol:** `aftermath-afsui` · Liquid Staking · Sui
- **DefiLlama:** https://defillama.com/protocol/aftermath-afsui
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $2,393,116
    - relative of **aftermath-perps** via version sibling — that sibling is *unknown series* and holds $0 now
- **Matched family:** `ORACLE-STALE-OR-SILENT-FALLBACK`
    - broken invariant: A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 11.0/20 · reachable live value 0.0/25 · precondition match 6.18/15
- **Why the clock is hot:**
    - version sibling of aftermath-perps, exploited on 2026-04-29; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is unknown series; this one holds $2,393,116.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 120d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Disclosure channel, if public:** https://aftermath.finance
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 136. Aftermath AMM — Tier 4 — URGENCY 45

- **Protocol:** `aftermath-amm` · Dexs · Sui
- **DefiLlama:** https://defillama.com/protocol/aftermath-amm
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $2,273,092
    - relative of **aftermath-perps** via version sibling — that sibling is *unknown series* and holds $0 now
- **Matched family:** `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`
    - broken invariant: Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 11.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - version sibling of aftermath-perps, exploited on 2026-04-29; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is unknown series; this one holds $2,273,092.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 120d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Every identifier derived or verified against the factory/registry (kills the pair); Routing restricted to an immutable venue allowlist
- **Disclosure channel, if public:** https://aftermath.finance
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 137. WEMIX Concentrated Range Deposit — Tier 4 — URGENCY 45

- **Protocol:** `wemix-concentrated-range-deposit` · Dexs · WEMIX
- **DefiLlama:** https://defillama.com/protocol/wemix-concentrated-range-deposit
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $2,169,898
    - relative of **wemix.fi-lend** via version sibling — that sibling is *drained or dead* and holds $1,971 now
- **Matched family:** `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`
    - broken invariant: A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 12.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - version sibling of wemix.fi-lend, exploited on 2026-07-26; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $2,169,898.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 32d ago; 3 siblings
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Amount taken from a measured post-transfer balance delta (kills the pair); Per-hop minimums enforced; Router restricted to assets the quoter supports
- **Disclosure channel, if public:** https://wemix.fi
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 138. Aftermath afLP — Tier 4 — URGENCY 45

- **Protocol:** `aftermath-aflp` · Yield · Sui
- **DefiLlama:** https://defillama.com/protocol/aftermath-aflp
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $1,900,087
    - relative of **aftermath-perps** via version sibling — that sibling is *unknown series* and holds $0 now
- **Matched family:** `ACC-ZERO-SUPPLY-INFLATION`
    - broken invariant: The first depositor must not be able to set an arbitrary asset-per-share ratio, and no operation may drive supply low enough to restore that branch.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 11.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - version sibling of aftermath-perps, exploited on 2026-04-29; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is unknown series; this one holds $1,900,087.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 120d ago; 4-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Dead shares minted at creation (kills the pair); Vault creation is permissioned and every vault is seeded; Virtual offset present in the deployed bytecode
- **Disclosure channel, if public:** https://aftermath.finance
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 139. Kernel — Tier 4 — URGENCY 45

- **Protocol:** `kernel` · Restaking · Binance
- **DefiLlama:** https://defillama.com/protocol/kernel
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $1,361,877
    - relative of **kelp** via version sibling — that sibling is *never materially hit* and holds $1,117,129,917 now
    - relative of **gain** via version sibling — that sibling is *never materially hit* and holds $32,795,428 now
- **Matched family:** `AUTH-MISSING-ON-VALUE-MOVING-PATH`
    - broken invariant: Every function that moves value or rebinds a privileged address must require a role the caller cannot obtain.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 11.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - version sibling of kelp, exploited on 2026-04-18; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is never materially hit; this one holds $1,361,877.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 131d ago; 4-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Every value-moving selector reverts for an unprivileged caller in simulation (kills the pair); Contract holds no value and controls no role
- **Disclosure channel, if public:** https://kelpdao.xyz/restake/?utm_source=0x798fF1e6D7AFd28c333eE6eBe03125d30ec6eF10
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 140. Solv Others — Tier 4 — URGENCY 45

- **Protocol:** `solv-others` · Anchor BTC · Merlin
- **DefiLlama:** https://defillama.com/protocol/solv-others
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $936,697
    - relative of **solvbtc** via version sibling — that sibling is *never materially hit* and holds $517,288,957 now
- **Matched family:** `AUTH-MISSING-ON-VALUE-MOVING-PATH`
    - broken invariant: Every function that moves value or rebinds a privileged address must require a role the caller cannot obtain.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 11.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - version sibling of solvbtc, exploited on 2026-03-06; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is never materially hit; this one holds $936,697.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 174d ago; 4-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Every value-moving selector reverts for an unprivileged caller in simulation (kills the pair); Contract holds no value and controls no role
- **Disclosure channel, if public:** https://solv.finance
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 141. WEMIX Full Range Deposit — Tier 4 — URGENCY 45

- **Protocol:** `wemix-full-range-deposit` · Dexs · WEMIX
- **DefiLlama:** https://defillama.com/protocol/wemix-full-range-deposit
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $824,781
    - relative of **wemix.fi-lend** via version sibling — that sibling is *drained or dead* and holds $1,971 now
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 14.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - version sibling of wemix.fi-lend, exploited on 2026-07-26; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $824,781.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 32d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://wemix.fi
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 142. DefiTuna Liquidity — Tier 4 — URGENCY 45

- **Protocol:** `defituna-liquidity` · Liquidity Manager · Solana
- **DefiLlama:** https://defillama.com/protocol/defituna-liquidity
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $647,102
    - relative of **defituna-lending** via version sibling — that sibling is *never materially hit* and holds $1,068,097 now
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 14.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - version sibling of defituna-lending, exploited on 2026-07-16; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is never materially hit; this one holds $647,102.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 42d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://defituna.com/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 143. Bonzo Vaults — Tier 4 — URGENCY 45

- **Protocol:** `bonzo-vaults` · Liquidity Manager · Hedera
- **DefiLlama:** https://defillama.com/protocol/bonzo-vaults
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $425,571
    - relative of **bonzo-lend** via version sibling — that sibling is *drained or dead* and holds $4,199,410 now
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 14.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - version sibling of bonzo-lend, exploited on 2026-07-11; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $425,571.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 47d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://bonzo.finance/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 144. Aave Aptos — Tier 4 — URGENCY 45

- **Protocol:** `aave-aptos` · Lending · Aptos
- **DefiLlama:** https://defillama.com/protocol/aave-aptos
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $308,734
    - relative of **aave-v3** via version sibling — that sibling is *never materially hit* and holds $17,400,461,288 now
- **Matched family:** `ORACLE-STALE-OR-SILENT-FALLBACK`
    - broken invariant: A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 11.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - version sibling of aave-v3, exploited on 2026-03-12; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is never materially hit; this one holds $308,734.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 168d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Disclosure channel, if public:** https://aave.com
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 145. WEMIX Liquid Staking — Tier 4 — URGENCY 45

- **Protocol:** `wemix-liquid-staking` · Liquid Staking · WEMIX
- **DefiLlama:** https://defillama.com/protocol/wemix-liquid-staking
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $254,158
    - relative of **wemix.fi-lend** via version sibling — that sibling is *drained or dead* and holds $1,971 now
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 14.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - version sibling of wemix.fi-lend, exploited on 2026-07-26; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $254,158.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 32d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://wemix.fi/en/liquid-staking
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 146. DefiTuna AMM — Tier 4 — URGENCY 45

- **Protocol:** `defituna-amm` · Dexs · Solana
- **DefiLlama:** https://defillama.com/protocol/defituna-amm
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $244,514
    - relative of **defituna-lending** via version sibling — that sibling is *never materially hit* and holds $1,068,097 now
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 14.0/20 · reachable live value 0.0/25 · precondition match 4.68/15
- **Why the clock is hot:**
    - version sibling of defituna-lending, exploited on 2026-07-16; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is never materially hit; this one holds $244,514.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 42d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** https://defituna.com
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 147. Solido Flow — Tier 4 — URGENCY 45

- **Protocol:** `solido-flow` · Liquid Staking · Supra
- **DefiLlama:** https://defillama.com/protocol/solido-flow
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $241,245
    - relative of **solido-cash** via version sibling — that sibling is *never materially hit* and holds $470,482 now
- **Matched family:** `ACC-DONATION-UNACCOUNTED-BALANCE`
    - broken invariant: A share price, exchange rate or totalAssets must be a function of value the protocol accounted for on entry. Reading a raw balance makes any direct transfer into the accounting boundary an unpriced increase in every holder's claim.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 12.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - version sibling of solido-cash, exploited on 2026-07-23; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is never materially hit; this one holds $241,245.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 35d ago; 3 siblings
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** totalAssets derived from an internal counter, not balanceOf (kills the pair); Rate is monotonic and rate-limited per block; Inbound transfers to the accounting boundary are rejected or swept to a reserve
- **Disclosure channel, if public:** https://solido.money/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 148. Aave Arc — Tier 4 — URGENCY 45

- **Protocol:** `aave-arc` · Lending · Ethereum
- **DefiLlama:** https://defillama.com/protocol/aave-arc
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $57,264
    - relative of **aave-v3** via version sibling — that sibling is *never materially hit* and holds $17,400,461,288 now
- **Matched family:** `ORACLE-SPOT-THIN-LIQUIDITY`
    - broken invariant: Borrowing capacity, mint size, reward size or collateral value must not be derived from a price that a single actor can move within the manipulation window, and the value unlocked must never exceed the cost of moving that price.
- **URGENCY 45 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`, capped at 45 by evidence depth
    - remediation gap 28/40 · technique recency+propagation 11.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - version sibling of aave-v3, exploited on 2026-03-12; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is never materially hit; this one holds $57,264.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 168d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** All collateral priced by a deep aggregated feed with a deviation cap (kills the pair); Caps are set from measured venue depth and enforced on-chain; The action is sized from realised transfer amounts, so price is never an input
- **Disclosure channel, if public:** https://aave.com
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 149. Cozy Earn — Tier 4 — URGENCY 42.38

- **Protocol:** `cozy-earn` · Insurance · Ethereum
- **DefiLlama:** https://defillama.com/protocol/cozy-earn
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $1,043,001
    - relative of **cozy-v2** via version sibling — that sibling is *drained or dead* and holds $172,358 now
- **Matched family:** `AUTH-MISSING-ON-VALUE-MOVING-PATH`
    - broken invariant: Every function that moves value or rebinds a privileged address must require a role the caller cannot obtain.
- **URGENCY 42.38 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 8.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - version sibling of cozy-v2, exploited on 2025-08-30; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $1,043,001.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 362d ago; 4-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Every value-moving selector reverts for an unprivileged caller in simulation (kills the pair); Contract holds no value and controls no role
- **Disclosure channel, if public:** https://www.cozy.finance
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 150. Typus DOV — Tier 4 — URGENCY 42.38

- **Protocol:** `typus-dov` · Options Vault · Sui
- **DefiLlama:** https://defillama.com/protocol/typus-dov
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $996,302
    - relative of **typus-perp** via version sibling — that sibling is *drained or dead* and holds $16,004 now
- **Matched family:** `AUTH-MISSING-ON-VALUE-MOVING-PATH`
    - broken invariant: Every function that moves value or rebinds a privileged address must require a role the caller cannot obtain.
- **URGENCY 42.38 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 8.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - version sibling of typus-perp, exploited on 2025-10-15; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $996,302.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 316d ago; 4-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Every value-moving selector reverts for an unprivileged caller in simulation (kills the pair); Contract holds no value and controls no role
- **Disclosure channel, if public:** https://typus.finance
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 151. Velar AMM — Tier 4 — URGENCY 42.38

- **Protocol:** `velar-amm` · Dexs · Stacks
- **DefiLlama:** https://defillama.com/protocol/velar-amm
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $401,394
    - relative of **velar-perps** via version sibling — that sibling is *drained or dead* and holds $13,986 now
- **Matched family:** `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`
    - broken invariant: Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.
- **URGENCY 42.38 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 8.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - version sibling of velar-perps, exploited on 2026-02-19; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $401,394.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 189d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Every identifier derived or verified against the factory/registry (kills the pair); Routing restricted to an immutable venue allowlist
- **Disclosure channel, if public:** https://velar.com/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 152. Hyperdrive HL Earn — Tier 4 — URGENCY 42.38

- **Protocol:** `hyperdrive-hl-earn` · Yield · Hyperliquid L1
- **DefiLlama:** https://defillama.com/protocol/hyperdrive-hl-earn
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $278,408
    - relative of **hyperdrive-hl-lending** via version sibling — that sibling is *never materially hit* and holds $879,869 now
- **Matched family:** `ACC-ZERO-SUPPLY-INFLATION`
    - broken invariant: The first depositor must not be able to set an arbitrary asset-per-share ratio, and no operation may drive supply low enough to restore that branch.
- **URGENCY 42.38 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 8.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - version sibling of hyperdrive-hl-lending, exploited on 2025-09-27; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is never materially hit; this one holds $278,408.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 334d ago; 4-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Dead shares minted at creation (kills the pair); Vault creation is permissioned and every vault is seeded; Virtual offset present in the deployed bytecode
- **Disclosure channel, if public:** https://hyperdrive.fi/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 153. Typus Safu — Tier 4 — URGENCY 42.38

- **Protocol:** `typus-safu` · Yield · Sui
- **DefiLlama:** https://defillama.com/protocol/typus-safu
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $191,194
    - relative of **typus-perp** via version sibling — that sibling is *drained or dead* and holds $16,004 now
- **Matched family:** `ACC-ZERO-SUPPLY-INFLATION`
    - broken invariant: The first depositor must not be able to set an arbitrary asset-per-share ratio, and no operation may drive supply low enough to restore that branch.
- **URGENCY 42.38 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 8.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - version sibling of typus-perp, exploited on 2025-10-15; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $191,194.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 316d ago; 4-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Dead shares minted at creation (kills the pair); Vault creation is permissioned and every vault is seeded; Virtual offset present in the deployed bytecode
- **Disclosure channel, if public:** https://typus.finance/safu
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 154. Ribbon Lend — Tier 4 — URGENCY 42.38

- **Protocol:** `ribbon-lend` · Uncollateralized Lending · Ethereum
- **DefiLlama:** https://defillama.com/protocol/ribbon-lend
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $52,340
    - relative of **ribbon** via version sibling — that sibling is *never materially hit* and holds $4,266,106 now
- **Matched family:** `AUTH-MISSING-ON-VALUE-MOVING-PATH`
    - broken invariant: Every function that moves value or rebinds a privileged address must require a role the caller cannot obtain.
- **URGENCY 42.38 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 8.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - version sibling of ribbon, exploited on 2025-12-12; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is never materially hit; this one holds $52,340.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 258d ago; 4-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Every value-moving selector reverts for an unprivileged caller in simulation (kills the pair); Contract holds no value and controls no role
- **Disclosure channel, if public:** https://www.ribbon.finance/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 155. ApertureSwap — Tier 4 — URGENCY 42.38

- **Protocol:** `apertureswap` · Dexs · Manta
- **DefiLlama:** https://defillama.com/protocol/apertureswap
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $51,433
    - relative of **aperture-lm** via version sibling — that sibling is *drained or dead* and holds $12,779 now
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 42.38 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 8.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - version sibling of aperture-lm, exploited on 2026-01-25; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $51,433.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 214d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 156. Pando Leaf — Tier 4 — URGENCY 40.75

- **Protocol:** `pando-leaf` · CDP · Mixin
- **DefiLlama:** https://defillama.com/protocol/pando-leaf
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $11,396,231
    - relative of **pando-rings** via version sibling — that sibling is *drained or dead* and holds $6,076,001 now
- **Matched family:** `ORACLE-STALE-OR-SILENT-FALLBACK`
    - broken invariant: A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
- **URGENCY 40.75 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - version sibling of pando-rings, exploited on 2022-11-06; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $11,396,231.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 1390d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Disclosure channel, if public:** https://pando.im
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 157. Curve LlamaLend V2 — Tier 4 — URGENCY 40.75

- **Protocol:** `curve-llamalend-v2` · Lending · Optimism
- **DefiLlama:** https://defillama.com/protocol/curve-llamalend-v2
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $2,057,612
    - relative of **curve-dex** via version sibling — that sibling is *never materially hit* and holds $1,342,226,339 now
    - relative of **curve-llamalend** via version sibling — that sibling is *never materially hit* and holds $77,979,276 now
- **Matched family:** `ORACLE-STALE-OR-SILENT-FALLBACK`
    - broken invariant: A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
- **URGENCY 40.75 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - version sibling of curve-dex, exploited on 2023-07-30; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is never materially hit; this one holds $2,057,612.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 1124d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Disclosure channel, if public:** https://www.curve.finance/lend/ethereum/markets/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 158. Thala CDP — Tier 4 — URGENCY 40.75

- **Protocol:** `thala-cdp` · CDP · Aptos
- **DefiLlama:** https://defillama.com/protocol/thala-cdp
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $476,431
    - relative of **thalaswap** via version sibling — that sibling is *never materially hit* and holds $645,216 now
- **Matched family:** `ORACLE-STALE-OR-SILENT-FALLBACK`
    - broken invariant: A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
- **URGENCY 40.75 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - version sibling of thalaswap, exploited on 2024-11-15; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is never materially hit; this one holds $476,431.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 650d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Disclosure channel, if public:** https://www.thala.fi/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 159. Ethos Reserve — Tier 4 — URGENCY 40.75

- **Protocol:** `ethos-reserve` · CDP · Optimism
- **DefiLlama:** https://defillama.com/protocol/ethos-reserve
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $233,361
    - relative of **reaper-farm** via version sibling — that sibling is *never materially hit* and holds $1,463,479 now
- **Matched family:** `ORACLE-STALE-OR-SILENT-FALLBACK`
    - broken invariant: A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
- **URGENCY 40.75 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - version sibling of reaper-farm, exploited on 2022-08-01; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is never materially hit; this one holds $233,361.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 1487d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 160. Ironclad Finance — Tier 4 — URGENCY 40.75

- **Protocol:** `ironclad-finance` · Lending · Mode
- **DefiLlama:** https://defillama.com/protocol/ironclad-finance
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $160,924
    - relative of **reaper-farm** via version sibling — that sibling is *never materially hit* and holds $1,463,479 now
- **Matched family:** `ORACLE-STALE-OR-SILENT-FALLBACK`
    - broken invariant: A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.
- **URGENCY 40.75 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.75/15
- **Why the clock is hot:**
    - version sibling of reaper-farm, exploited on 2022-08-01; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is never materially hit; this one holds $160,924.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 1487d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape); Every feed read reverts on zero/stale (kills the silent-fallback shape); Asset valuations cross-checked against a second independent oracle with a hard deviation cap
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 161. Save SOL — Tier 4 — URGENCY 40.38

- **Protocol:** `save-sol` · Liquid Staking · Solana
- **DefiLlama:** https://defillama.com/protocol/save-sol
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $6,180,608
    - relative of **save** via version sibling — that sibling is *restored* and holds $85,337,344 now
- **Matched family:** `PROOF-VERIFICATION-BYPASSED`
    - broken invariant: A withdrawal or mint gated by a proof must verify that proof against the correct verifying key, over all the public inputs that bind the action, and must reject when any component is absent.
- **URGENCY 40.38 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - version sibling of save, exploited on 2022-11-02; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is restored; this one holds $6,180,608.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 1394d ago; 6-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Verifying key immutable and attested (kills the misconfiguration shape); No alternative release path exists (enumerate selectors)
- **Disclosure channel, if public:** https://save.finance/saveSOL
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 162. Eigenpie — Tier 4 — URGENCY 40.38

- **Protocol:** `eigenpie` · Liquid Restaking · Ethereum, Zircuit
- **DefiLlama:** https://defillama.com/protocol/eigenpie
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $4,468,920
    - relative of **penpie** via version sibling — that sibling is *never materially hit* and holds $4,779,078 now
- **Matched family:** `AUTH-MISSING-ON-VALUE-MOVING-PATH`
    - broken invariant: Every function that moves value or rebinds a privileged address must require a role the caller cannot obtain.
- **URGENCY 40.38 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - version sibling of penpie, exploited on 2024-09-03; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is never materially hit; this one holds $4,468,920.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 723d ago; 4-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Every value-moving selector reverts for an unprivileged caller in simulation (kills the pair); Contract holds no value and controls no role
- **Disclosure channel, if public:** https://www.eigenlayer.magpiexyz.io
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 163. WOOFi Earn — Tier 4 — URGENCY 40.38

- **Protocol:** `woofi-earn` · Yield · Arbitrum, Optimism, Base, Avalanche, Polygon
- **DefiLlama:** https://defillama.com/protocol/woofi-earn
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $2,694,195
    - relative of **woofi-swap** via version sibling — that sibling is *drained or dead* and holds $2,418,019 now
- **Matched family:** `ACC-ZERO-SUPPLY-INFLATION`
    - broken invariant: The first depositor must not be able to set an arbitrary asset-per-share ratio, and no operation may drive supply low enough to restore that branch.
- **URGENCY 40.38 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - version sibling of woofi-swap, exploited on 2024-03-05; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $2,694,195.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 905d ago; 4-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Dead shares minted at creation (kills the pair); Vault creation is permissioned and every vault is seeded; Virtual offset present in the deployed bytecode
- **Disclosure channel, if public:** https://fi.woo.org/earn
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 164. Nirvana V2 — Tier 4 — URGENCY 40.38

- **Protocol:** `nirvana-v2` · Reserve Currency · Solana
- **DefiLlama:** https://defillama.com/protocol/nirvana-v2
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $2,586,219
    - relative of **nirvana-v1** via version sibling — that sibling is *drained or dead* and holds $3 now
- **Matched family:** `AUTH-MISSING-ON-VALUE-MOVING-PATH`
    - broken invariant: Every function that moves value or rebinds a privileged address must require a role the caller cannot obtain.
- **URGENCY 40.38 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - version sibling of nirvana-v1, exploited on 2022-07-28; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $2,586,219.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 1491d ago; 4-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Every value-moving selector reverts for an unprivileged caller in simulation (kills the pair); Contract holds no value and controls no role
- **Disclosure channel, if public:** https://www.nirvana.finance/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 165. ThalaSwap V3 — Tier 4 — URGENCY 40.38

- **Protocol:** `thalaswap-v3` · Dexs · Aptos
- **DefiLlama:** https://defillama.com/protocol/thalaswap-v3
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $2,160,250
    - relative of **thalaswap** via version sibling — that sibling is *never materially hit* and holds $645,216 now
- **Matched family:** `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`
    - broken invariant: Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.
- **URGENCY 40.38 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - version sibling of thalaswap, exploited on 2024-11-15; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is never materially hit; this one holds $2,160,250.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 650d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Every identifier derived or verified against the factory/registry (kills the pair); Routing restricted to an immutable venue allowlist
- **Disclosure channel, if public:** https://www.thala.fi/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 166. Thala LSD — Tier 4 — URGENCY 40.38

- **Protocol:** `thala-lsd` · Liquid Staking · Aptos
- **DefiLlama:** https://defillama.com/protocol/thala-lsd
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $1,737,749
    - relative of **thalaswap** via version sibling — that sibling is *never materially hit* and holds $645,216 now
- **Matched family:** `PROOF-VERIFICATION-BYPASSED`
    - broken invariant: A withdrawal or mint gated by a proof must verify that proof against the correct verifying key, over all the public inputs that bind the action, and must reject when any component is absent.
- **URGENCY 40.38 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - version sibling of thalaswap, exploited on 2024-11-15; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is never materially hit; this one holds $1,737,749.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 650d ago; 6-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Verifying key immutable and attested (kills the misconfiguration shape); No alternative release path exists (enumerate selectors)
- **Disclosure channel, if public:** https://app.thala.fi/lsd
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 167. Arena DEX — Tier 4 — URGENCY 40.38

- **Protocol:** `arena-dex` · Dexs · Avalanche
- **DefiLlama:** https://defillama.com/protocol/arena-dex
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $1,548,375
    - relative of **arena-socialfi** via version sibling — that sibling is *never materially hit* and holds $142,634 now
- **Matched family:** `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`
    - broken invariant: Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.
- **URGENCY 40.38 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - version sibling of arena-socialfi, exploited on 2023-10-07; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is never materially hit; this one holds $1,548,375.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 1055d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Every identifier derived or verified against the factory/registry (kills the pair); Routing restricted to an immutable venue allowlist
- **Disclosure channel, if public:** https://arena.social/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 168. ThalaSwap V2 — Tier 4 — URGENCY 40.38

- **Protocol:** `thalaswap-v2` · Dexs · Aptos
- **DefiLlama:** https://defillama.com/protocol/thalaswap-v2
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $586,043
    - relative of **thalaswap** via version sibling — that sibling is *never materially hit* and holds $645,216 now
- **Matched family:** `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`
    - broken invariant: Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.
- **URGENCY 40.38 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - version sibling of thalaswap, exploited on 2024-11-15; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is never materially hit; this one holds $586,043.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 650d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Every identifier derived or verified against the factory/registry (kills the pair); Routing restricted to an immutable venue allowlist
- **Disclosure channel, if public:** https://www.thala.fi/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 169. 4Swap — Tier 4 — URGENCY 40.38

- **Protocol:** `4swap` · Dexs · Mixin
- **DefiLlama:** https://defillama.com/protocol/4swap
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $494,167
    - relative of **pando-rings** via version sibling — that sibling is *drained or dead* and holds $6,076,001 now
- **Matched family:** `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`
    - broken invariant: Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.
- **URGENCY 40.38 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - version sibling of pando-rings, exploited on 2022-11-06; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $494,167.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 1390d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Every identifier derived or verified against the factory/registry (kills the pair); Routing restricted to an immutable venue allowlist
- **Disclosure channel, if public:** https://pando.im
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 170. Basin Exchange — Tier 4 — URGENCY 40.38

- **Protocol:** `basin-exchange` · Dexs · Arbitrum, Ethereum
- **DefiLlama:** https://defillama.com/protocol/basin-exchange
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $438,854
    - relative of **beanstalk** via version sibling — that sibling is *drained or dead* and holds $0 now
- **Matched family:** `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`
    - broken invariant: Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.
- **URGENCY 40.38 / EVIDENCE_CONFIDENCE 41.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - version sibling of beanstalk, exploited on 2022-04-17; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $438,854.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 1593d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Every identifier derived or verified against the factory/registry (kills the pair); Routing restricted to an immutable venue allowlist
- **Disclosure channel, if public:** https://basin.exchange
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 171. Cetus DLMM — Tier 4 — URGENCY 40.38

- **Protocol:** `cetus-dlmm` · Dexs · Sui
- **DefiLlama:** https://defillama.com/protocol/cetus-dlmm
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $433,423
    - relative of **cetus-clmm** via version sibling — that sibling is *drained or dead* and holds $25,461,685 now
- **Matched family:** `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`
    - broken invariant: Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.
- **URGENCY 40.38 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - version sibling of cetus-clmm, exploited on 2025-05-22; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $433,423.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 462d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Every identifier derived or verified against the factory/registry (kills the pair); Routing restricted to an immutable venue allowlist
- **Disclosure channel, if public:** https://www.cetus.zone
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 172. SwapX Algebra — Tier 4 — URGENCY 40.38

- **Protocol:** `swapx-algebra` · Dexs · Sonic
- **DefiLlama:** https://defillama.com/protocol/swapx-algebra
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $404,170
    - relative of **swapx-v2** via version sibling — that sibling is *drained or dead* and holds $43,833 now
- **Matched family:** `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`
    - broken invariant: Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.
- **URGENCY 40.38 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - version sibling of swapx-v2, exploited on 2023-02-27; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $404,170.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 1277d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Every identifier derived or verified against the factory/registry (kills the pair); Routing restricted to an immutable venue allowlist
- **Disclosure channel, if public:** https://swapx.fi/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 173. Voltage V4 — Tier 4 — URGENCY 40.38

- **Protocol:** `voltage-v4` · Dexs · Fuse
- **DefiLlama:** https://defillama.com/protocol/voltage-v4
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $186,233
    - relative of **voltage-v3** via version sibling — that sibling is *drained or dead* and holds $550 now
- **Matched family:** `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`
    - broken invariant: Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.
- **URGENCY 40.38 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - version sibling of voltage-v3, exploited on 2025-03-18; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $186,233.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 527d ago; 5-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Every identifier derived or verified against the factory/registry (kills the pair); Routing restricted to an immutable venue allowlist
- **Disclosure channel, if public:** https://app.voltage.finance/
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 174. Velocore V1 — Tier 4 — URGENCY 40.38

- **Protocol:** `velocore-v1` · Dexs · zkSync Era
- **DefiLlama:** https://defillama.com/protocol/velocore-v1
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $126,572
    - relative of **velocore-v2** via version sibling — that sibling is *drained or dead* and holds $1,175 now
- **Matched family:** `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`
    - broken invariant: Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.
- **URGENCY 40.38 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - version sibling of velocore-v2, exploited on 2024-06-02; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $126,572.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 816d ago; 7-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed); Contract reverts on every state-changing entrypoint (verified paused)
- **Disclosure channel, if public:** not listed in metadata
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

### 175. Voltage Liquid Staking — Tier 4 — URGENCY 40.38

- **Protocol:** `voltage-liquid-staking` · Liquid Staking · Fuse
- **DefiLlama:** https://defillama.com/protocol/voltage-liquid-staking
- **Live value, read at head 2026-08-27T09:59:26Z (beside the score, never inside it):** $86,834
    - relative of **voltage-v3** via version sibling — that sibling is *drained or dead* and holds $550 now
- **Matched family:** `PROOF-VERIFICATION-BYPASSED`
    - broken invariant: A withdrawal or mint gated by a proof must verify that proof against the correct verifying key, over all the public inputs that bind the action, and must reject when any component is absent.
- **URGENCY 40.38 / EVIDENCE_CONFIDENCE 47.0** — evidence level `L1_ADAPTER`
    - remediation gap 28/40 · technique recency+propagation 6.0/20 · reachable live value 0.0/25 · precondition match 6.38/15
- **Why the clock is hot:**
    - version sibling of voltage-v3, exploited on 2025-03-18; forks and siblings inherit the parent's bug and rarely the parent's fix. That sibling is drained or dead; this one holds $86,834.
    - reachability: not read deeply enough to judge reachability
    - recency: technique public 527d ago; 6-member population
- **THE decisive check (single fastest confirm/kill):** Diff this deployment against the sibling at the guard the incident turned on. A missing or REMOVED guard is the finding.
- **Prior-art & remediation status:** `KNOWN_ISSUE_STATUS_UNKNOWN`
- **What would falsify it:** Verifying key immutable and attested (kills the misconfiguration shape); No alternative release path exists (enumerate selectors)
- **Disclosure channel, if public:** https://app.voltage.finance/#/stake
- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number

---

## Withheld by the no-repetition ledger — but now classified Tier 1–2

These **45** protocols were handed over in earlier runs and are excluded from the list above. They are named here rather than silently dropped because the ranking axis changed underneath them: they were delivered as likelihood candidates and now classify as hot clocks. Withholding a Tier-1 item because it was once served cold would be the wrong call, so this is your decision, not mine.

| Protocol | Tier | URGENCY | Family | Live value | First delivered |
|---|---:|---:|---|---:|---|
| [SIR](https://defillama.com/protocol/sir) | 1 | 68.07 | `SIG-VERIFIER-DEFEATABLE` | $109,365 | `2ce88d1` |
| [Nomad](https://defillama.com/protocol/nomad) | 1 | 66.57 | `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET` | $359,084 | `1ad898f` |
| [UwU Lend](https://defillama.com/protocol/uwu-lend) | 1 | 66.57 | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | $94,541 | `3bc30a7` |
| [Agave](https://defillama.com/protocol/agave) | 1 | 40.75 | `ORACLE-STALE-OR-SILENT-FALLBACK` | $89,754 | `7d49c12` |
| [Extra Finance Leverage Farming](https://defillama.com/protocol/extra-finance-leverage-farming) | 2 | 84.07 | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | $25,914,028 | `6e7df7a` |
| [Synapse Cross Chain Bridge](https://defillama.com/protocol/synapse-cross-chain-bridge) | 2 | 84.07 | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | $11,489,644 | `ccb5273` |
| [YieldWolf](https://defillama.com/protocol/yieldwolf) | 2 | 84.07 | `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | $58,475 | `2ce88d1` |
| [Orderly Bridge](https://defillama.com/protocol/orderly-bridge) | 2 | 83.12 | `BRIDGE-MESSAGE-NOT-BOUND-TO-SOURCE` | $23,469,186 | `1ad898f` |
| [Equilibria](https://defillama.com/protocol/equilibria) | 2 | 83.12 | `BRIDGE-MESSAGE-NOT-BOUND-TO-SOURCE` | $11,722,605 | `1ad898f` |
| [Stargate V1](https://defillama.com/protocol/stargate-v1) | 2 | 82.0 | `BRIDGE-MESSAGE-NOT-BOUND-TO-SOURCE` | $10,837,460 | `3bc30a7` |
| [Lynx](https://defillama.com/protocol/lynx) | 2 | 82.0 | `BRIDGE-MESSAGE-NOT-BOUND-TO-SOURCE` | $196,381 | `693e2ed` |
| [Zoo Finance](https://defillama.com/protocol/zoo-finance) | 2 | 81.07 | `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED` | $19,747,598 | `6e7df7a` |
| [Charm Finance V2](https://defillama.com/protocol/charm-finance-v2) | 2 | 81.07 | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | $1,955,484 | `693e2ed` |
| [iZiSwap](https://defillama.com/protocol/iziswap) | 2 | 81.07 | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | $1,546,947 | `2ce88d1` |
| [Accumulated Finance Liquid Staking](https://defillama.com/protocol/accumulated-finance-liquid-staking) | 2 | 81.07 | `SIG-VERIFIER-DEFEATABLE` | $616,333 | `3bc30a7` |
| [Sturdy V2](https://defillama.com/protocol/sturdy-v2) | 2 | 81.07 | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | $273,549 | `ccb5273` |
| [Pell Network](https://defillama.com/protocol/pell-network) | 2 | 81.07 | `ACC-SIGN-OR-BOUND-CHECK-MISSING` | $227,574 | `2ce88d1` |
| [SatLayer](https://defillama.com/protocol/satlayer) | 2 | 81.07 | `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED` | $187,791 | `2ce88d1` |
| [Royco V1](https://defillama.com/protocol/royco-v1) | 2 | 80.05 | `BRIDGE-MESSAGE-NOT-BOUND-TO-SOURCE` | $1,550,293 | `6e7df7a` |
| [SushiSwap](https://defillama.com/protocol/sushiswap) | 2 | 79.57 | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | $39,927,157 | `6e7df7a` |
| [Impermax V2](https://defillama.com/protocol/impermax-v2) | 2 | 79.57 | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | $597,991 | `3bc30a7` |
| [RadioShack](https://defillama.com/protocol/radioshack) | 2 | 79.57 | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | $453,693 | `2ce88d1` |
| [Clovis](https://defillama.com/protocol/clovis) | 2 | 79.57 | `ACC-DUPLICATE-ID-ACCUMULATION` | $224,836 | `6e7df7a` |
| [Fortunafi](https://defillama.com/protocol/fortunafi) | 2 | 79.57 | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | $221,821 | `6e7df7a` |
| [Elk](https://defillama.com/protocol/elk) | 2 | 79.57 | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | $160,743 | `7e319ee` |
| [IMPOSSIBLE](https://defillama.com/protocol/impossible) | 2 | 79.57 | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | $134,668 | `2ce88d1` |
| [iZUMi LiquidBox](https://defillama.com/protocol/izumi-liquidbox) | 2 | 79.57 | `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | $121,581 | `2ce88d1` |
| [Quickswap V4](https://defillama.com/protocol/quickswap-v4) | 2 | 77.88 | `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED` | $5,346,067 | `6e7df7a` |
| [Reservoir Protocol](https://defillama.com/protocol/reservoir-protocol) | 2 | 76.57 | `AUTH-ZERO-ADDRESS-ACCEPTED` | $25,859,012 | `1ad898f` |
| [Sumer.money](https://defillama.com/protocol/sumer.money) | 2 | 76.57 | `AUTH-ZERO-ADDRESS-ACCEPTED` | $1,298,852 | `7d49c12` |
| [Dyson](https://defillama.com/protocol/dyson) | 2 | 76.57 | `AUTH-ZERO-ADDRESS-ACCEPTED` | $270,955 | `6e7df7a` |
| [MIM Swap](https://defillama.com/protocol/mim-swap) | 2 | 76.57 | `AUTH-ZERO-ADDRESS-ACCEPTED` | $120,830 | `1ad898f` |
| [Tarot](https://defillama.com/protocol/tarot) | 2 | 74.07 | `ORACLE-SPOT-THIN-LIQUIDITY` | $610,295 | `3bc30a7` |
| [ICHI](https://defillama.com/protocol/ichi) | 2 | 71.38 | `ACC-DONATION-UNACCOUNTED-BALANCE` | $7,793,615 | `1ad898f` |
| [De1](https://defillama.com/protocol/de1) | 2 | 71.38 | `ACC-DONATION-UNACCOUNTED-BALANCE` | $128,687 | `1ad898f` |
| [Single Finance](https://defillama.com/protocol/single-finance) | 2 | 71.38 | `ACC-DONATION-UNACCOUNTED-BALANCE` | $66,011 | `2ce88d1` |
| [Wasabi Perps](https://defillama.com/protocol/wasabi-perps) | 2 | 67.88 | `ORACLE-SPOT-THIN-LIQUIDITY` | $756,080 | `1ad898f` |
| [Steer Protocol](https://defillama.com/protocol/steer-protocol) | 2 | 66.18 | `ORACLE-SPOT-THIN-LIQUIDITY` | $20,608,221 | `1ad898f` |
| [PRDT](https://defillama.com/protocol/prdt) | 2 | 66.18 | `ORACLE-SPOT-THIN-LIQUIDITY` | $517,805 | `1ad898f` |
| [Skate Fi](https://defillama.com/protocol/skate-fi) | 2 | 66.18 | `ORACLE-SPOT-THIN-LIQUIDITY` | $118,982 | `6e7df7a` |

---

## Limits of this ranking

- **No fix-in-artifact check was run.** That is the single highest-value next action and it is what separates 28 points from 40. Until it runs, no row here is `UNREMEDIATED_KNOWN`.
- **Tier 3 is barely populated (0 protocols).** The only dependency this run can evidence is the *declared oracle*, and only where the provider's user population is small enough for one incident to mean something. Backing, collateral, LP and vault-share holdings are **not** resolved — the Blend case (contracts sound, backstop composed of another protocol's LP) is exactly what this run cannot yet see.

- **Fork lineage is weak, and that caps Tier 1.** DefiLlama populates `forkedFrom` on **6 protocols out of 8,135**, so it carries nothing. The only code-lineage evidence available is `parentProtocol` (version siblings), which is why Tier 1 holds 6 and Tier 4 holds 83 — the relatives are real but the link is a sibling relationship, not proven shared code.
- **A grouping this pass rejected.** Grouping protocols by shared adapter module first produced a 7-member "fork cluster" around a victim, headed by a $19.3M protocol. The shared module was `dummy.js` — DefiLlama's placeholder for *no adapter*, carried by 1,124 protocols including Fantom, 0x, Jupiter and OpenSea Seaport. Not shared code at all. Placeholder modules and groups above 12 members are now rejected.
- **The capability that would fix this: runtime bytecode similarity.** Hashing deployed code across the probed population would find literal clones of a victim — the "byte-similar" half of Tier 4 that lineage metadata cannot reach. Not run in this pass.
- **Tier 1 rests on DefiLlama's incident dataset plus this run's corpus.** A protocol with no recorded incident may simply have no record.

- **Value at risk sits beside the score and never inside it.** A real finding on $60k of dust is a low-value save; check the column before spending time.

- Read-only throughout. No transaction, no calldata, no credential use.

