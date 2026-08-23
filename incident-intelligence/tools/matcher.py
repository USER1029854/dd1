# -*- coding: utf-8 -*-
"""Family -> protocol applicability map and L0 pair generation."""
# Each entry: categories that make the archetype applicable, plus metadata-level
# signals that raise SCREENING PRIORITY (never MATCH_SCORE: L0 caps at 20).
APPLIC = {
"ACC-DONATION-UNACCOUNTED-BALANCE": dict(
  cats={"Lending","CDP","Yield","Yield Aggregator","Risk Curators","Onchain Capital Allocator",
        "Liquid Staking","Liquid Restaking","Basis Trading","RWA Lending","Leveraged Farming"},
  fork_lineage={"compound","venus","aave","cream","benqi","sonne","moonwell","iron bank","strike","tectonic","radiant"},
  prio_desc=("compound","ctoken","vtoken","erc-4626","erc4626","vault","exchange rate","supply cap")),
"ORACLE-STALE-OR-SILENT-FALLBACK": dict(
  cats={"Lending","CDP","RWA Lending","Risk Curators","Yield","Derivatives","Basis Trading",
        "Onchain Capital Allocator","Liquid Staking","Leveraged Farming"},
  prio_desc=("oracle","price feed","collateral","borrow","liquidat","nav")),
"ORACLE-SPOT-THIN-LIQUIDITY": dict(
  cats={"Lending","CDP","Farm","Staking Pool","Yield","Liquidity Manager","RWA Lending",
        "Leveraged Farming","Prediction Market","Options"},
  prio_desc=("borrow","collateral","reward","stake","apr","yield")),
"ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE": dict(
  cats={"Lending","CDP","Risk Curators","Leveraged Farming","Basis Trading","Yield","RWA Lending"},
  prio_desc=("yield-bearing","lst","lrt","vault token","wrapped","4626","savings")),
"ACC-NAV-SHAREPRICE-MANIPULABLE": dict(
  cats={"Yield","Yield Aggregator","Risk Curators","Onchain Capital Allocator","Indexes",
        "Basis Trading","Structured Products","Liquid Staking","Liquid Restaking","Options"},
  prio_desc=("vault","strateg","nav","curat","allocat","index","share price")),
"ACC-ZERO-SUPPLY-INFLATION": dict(
  cats={"Lending","Yield","Yield Aggregator","Options","Risk Curators","CDP","Leveraged Farming"},
  prio_desc=("permissionless","isolated market","create market","factory","vault")),
"BRIDGE-MESSAGE-NOT-BOUND-TO-SOURCE": dict(
  cats={"Bridge","Canonical Bridge","Cross Chain Bridge","Cross Chain","Liquid Staking"},
  prio_desc=("bridge","cross-chain","mint","wrapped","message","relayer","ibc")),
"UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY": dict(
  cats=None,  # applicable to any archetype
  prio_desc=("v1","v2","v3","legacy","deprecated","migrat","sunset")),
"UPGRADE-INITIALIZER-REACHABLE-LIVE": dict(
  cats=None,
  prio_desc=("proxy","upgradeable","diamond","beacon")),
"CALLDATA-CALLER-CONTROLLED-TARGET": dict(
  cats={"Dexs","DEX Aggregator","Bridge","Cross Chain Bridge","Services","Yield","Liquidity Manager",
        "Leveraged Farming","Basis Trading"},
  prio_desc=("router","aggregat","multicall","execut","zap","swap","adapter")),
"CALLBACK-UNAUTHENTICATED-CALLER-USES-APPROVALS": dict(
  cats={"Dexs","DEX Aggregator","Liquidity Manager","Yield","Leveraged Farming","Services"},
  prio_desc=("hook","callback","singleton","flash","router","extension","v4")),
"GOV-CHEAP-CONTROL-NO-TIMELOCK": dict(
  cats=None, requires_governance=True,
  prio_desc=("dao","governance","vote","proposal","timelock")),
"LIQUIDATION-ON-MANIPULABLE-VALUATION": dict(
  cats={"Lending","CDP","Derivatives","Basis Trading","RWA Lending","Leveraged Farming","Perps"},
  prio_desc=("liquidat","margin","perp","collateral","health")),
"PROOF-VERIFICATION-BYPASSED": dict(
  cats={"Bridge","Canonical Bridge","Cross Chain Bridge","Privacy","Liquid Staking","Gaming"},
  prio_desc=("zk","proof","privacy","shielded","rollup","verifier","light client")),
"ACC-REWARD-INDEX-INIT-AND-ORDERING": dict(
  cats={"Farm","Staking Pool","Yield","Yield Aggregator","Liquid Staking","Lending","Gauges"},
  prio_desc=("reward","gauge","emission","incentiv","harvest","points")),
"ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED": dict(
  cats={"Dexs","DEX Aggregator","Lending","Leveraged Farming","Launchpad","Cross Chain Bridge","Services"},
  prio_desc=("permissionless","any token","route","pool","market","list")),
"QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET": dict(
  cats={"Dexs","DEX Aggregator","Leveraged Farming","Basis Trading","Services","Lending"},
  prio_desc=("route","quote","aggregat","slippage","margin","leverage","swap")),
"CALLBACK-STATE-LOCK-INCOMPLETE": dict(
  cats={"Yield","Yield Aggregator","Farm","Liquidity Manager","Indexes","Lending","Dexs"},
  prio_desc=("vault","strateg","hook","flash","callback")),
"APPROVALS-TO-UPGRADEABLE-SPENDER": dict(
  cats={"Dexs","DEX Aggregator","Bridge","Services","Yield","Liquidity Manager","Lending"},
  prio_desc=("router","spender","approve","proxy","upgradeable")),
"ACC-MULTI-PATH-CREDIT-DRIFT": dict(
  cats={"Dexs","Yield","Lending","Liquid Staking","Cross Chain","Derivatives"},
  prio_desc=("singleton","monolith","proxy","module","v2","migrat")),
"AUTH-MISSING-ON-VALUE-MOVING-PATH": dict(cats=None, prio_desc=("",)),
"SIG-DIGEST-AMBIGUOUS-OR-UNBOUND": dict(
  cats={"Yield","Yield Aggregator","Bridge","Cross Chain Bridge","Dexs","DEX Aggregator","Services"},
  prio_desc=("signature","permit","intent","rfq","gasless","meta")),
"SIG-REPLAY-CROSS-POSITION": dict(
  cats={"Liquidity Manager","Leveraged Farming","Derivatives","Yield"},
  prio_desc=("position","manager","signature","lp")),
"SETTLEMENT-EPOCH-BOUNDARY-CREDIT": dict(
  cats={"Yield","Options","Derivatives","Basis Trading","RWA","RWA Lending","Structured Products"},
  prio_desc=("epoch","settle","daily","weekly","round","nav")),
"ACC-SPLIT-NONINVARIANT": dict(
  cats={"CDP","Options","Structured Products","Dexs","Indexes"},
  prio_desc=("bond","tranche","curve","custom","redeem")),
"AMM-POOL-RATIO-SKEW-EXTRACTION": dict(
  cats={"Dexs","Bridge","Cross Chain Bridge","Basis Trading"},
  prio_desc=("stable","pool","curve","liquidity")),
"INCENTIVE-PER-ADDRESS-NO-SYBIL-COST": dict(
  cats={"Farm","Staking Pool","Launchpad","Yield","Stablecoin","Algo-Stables"},
  prio_desc=("points","airdrop","reward","incentiv","referr")),
}
# families whose live prerequisite base is essentially absent from the DefiLlama universe
NOT_SCREENABLE = {
 "TOKEN-DEFERRED-BURN-LP-RESERVE-DESYNC":"Victims are individually deployed BSC/Base tokens with custom transfer logic that are not listed as DefiLlama protocols; the family has no addressable protocol population in this universe. Handed to the token-level monitoring workstream instead.",
 "TOKEN-TRANSFER-OVERRIDE-BREAKS-CONSERVATION":"Same population problem as the deferred-burn family.",
 "TOKEN-TRANSFER-INTENT-HEURISTIC-FORGEABLE":"Same population problem as the deferred-burn family.",
 "HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL":"Applies to token contracts with accrual hooks; only reachable through per-token screening, not the protocol universe.",
 "TOKEN-PACKED-OWNERSHIP-UNDERFLOW":"Requires DN404/BT404 lineage; no in-universe protocol above the TVL threshold carries it.",
 "AUTH-ZERO-ADDRESS-ACCEPTED":"Screened as a cheap read-only sweep (owner()==address(0) with non-zero balance) rather than as a protocol-family pair.",
 "SECRET-EMBEDDED-IN-PUBLIC-CODE-AS-AUTH":"Requires bytecode constant analysis per contract; run as a sweep over deep-screened deployments rather than as a ranked pair.",
 "STORAGE-LAYOUT-COLLISION-PHANTOM-CREDIT":"Requires a storage-layout dump per contract; run as a sweep over deep-screened deployments.",
 "METATX-SENDER-IDENTITY-CONFUSION":"Requires ERC-2771 detection per contract; run as a sweep.",
 "ACC-CREDIT-NOT-RECEIVED":"Reward-tracker contracts are rarely separate DefiLlama entries; folded into the reward-index sweep.",
 "ACC-DUPLICATE-ID-ACCUMULATION":"Detected by selector-shape sweep over deep-screened deployments.",
 "ACC-SIGN-OR-BOUND-CHECK-MISSING":"Detected by parameter-shape sweep over deep-screened deployments.",
 "ACC-HARDCODED-PEG-REDEMPTION":"Folded into the stablecoin-issuer oracle screen.",
 "SIG-VERIFIER-DEFEATABLE":"Detected by source-grep sweep over deep-screened deployments.",
 "AUTH-IDENTITY-SATISFIABLE-BY-ATTACKER-CONTRACT":"Detected by source-grep sweep over deep-screened deployments.",
 "AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY":"Detected by selector sweep over deep-screened deployments.",
}
