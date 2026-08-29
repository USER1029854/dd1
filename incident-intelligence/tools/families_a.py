# -*- coding: utf-8 -*-
"""Mechanism families, part A. Clustered by broken invariant + mechanism +
mandatory prerequisite signature + decisive missing guard (NOT by attack label)."""
FAM_A = {

"TOKEN-DEFERRED-BURN-LP-RESERVE-DESYNC": dict(
 title="Token logic mutates an AMM pair's token balance out-of-band, then reserves are resynced",
 broken_invariant="An AMM pair's recorded reserves may change only through the pair's own swap/mint/burn accounting. A token contract must never move or destroy tokens already held by the pair, because any unpriced change to the pair's balance is realizable as profit by the next caller once reserves are resynchronised.",
 mechanism="The token implements fee-on-transfer, deflation, dividend or 'maintenance' logic that (a) accumulates a pending burn/fee amount in storage on sells, and (b) on a later, often unrelated, transfer burns or transfers that amount directly from the pair address and calls pair.sync() (or relies on the next skim/sync). The pair's reserve is rewritten to a value that no swap produced. An unprivileged caller sequences: accumulate pending amount -> buy out the pair inventory -> trigger the deferred burn -> sell back into the now-skewed curve.",
 mandatory_preconditions=[
   "Token contract contains logic that transfers or burns from, or mints to, the AMM pair address (not merely from msg.sender)",
   "That logic is reachable by an unprivileged caller (public function, or a hook on any transfer, including a zero-value transfer)",
   "The pair's reserves are re-synchronised after the out-of-band balance change (explicit pair.sync()/skim(), or a subsequent swap that reads stale reserves)",
   "A live AMM pair holds material quote-asset liquidity for the token"],
 optional_amplifiers=["Flash-loan liquidity to buy out inventory","Thin pair depth","Multiple router paths","Whitelisted router/pair bypassing transfer restrictions"],
 applicable_protocol_archetypes=["token with custom transfer logic","farm","reward distributor","launchpad token","DEX/AMM pair (as victim venue)"],
 static_indicators=[
   "_transfer/_update override referencing a stored pair/lpPair/uniswapV2Pair address",
   "state variables named toBurnAmount, pendingBurn, sellBurn, pendingBurnAmount, deferred*",
   "direct calls to IUniswapV2Pair.sync() or .skim() from the token or a helper",
   "_burn(pair, amount) / super._transfer(pair, dead, amount) / mintReward(pair, ...)",
   "balanceOf(pair) read inside transfer logic"],
 adapter_indicators=["DefiLlama adapter values a single token/LP pair via getReserves on a pair whose token has custom transfer logic","adapter hardcodes one pair address as the protocol's whole TVL"],
 runtime_state_indicators=[
   "pair token balance != pair reserve for the custom token (balance/reserve drift)",
   "non-zero pending-burn storage slot",
   "historical Sync events not immediately preceded by Swap/Mint/Burn from the pair itself"],
 cross_contract_indicators=["token contract is not the pair, yet appears as `from` in Transfer events whose `from` is the pair address"],
 decisive_guards=[
   "Token never writes to the pair's balance: burns/fees are taken from msg.sender's amount only",
   "Pair address is excluded from all fee/burn/dividend logic (isExcluded[pair] == true) for balance-mutating paths",
   "No public path invokes pair.sync()/skim() after a protocol-initiated balance change",
   "Post-transfer assertion that balanceOf(pair) >= reserve for that token"],
 false_positive_killers=[
   "Token is a plain OpenZeppelin ERC-20 with no _update/_transfer override (kills the hypothesis)",
   "Fee logic only reduces the amount credited to `to`, never touches third-party balances",
   "All burn targets are msg.sender or address(this), never a pair"],
 local_defensive_property="For every reachable public call sequence, balanceOf(pair, token) must never decrease except through the pair's own burn()/swap() accounting; assert reserve-vs-balance parity before and after each token operation in a fork test.",
 recommended_audit_questions=[
   "Does any code path let a caller change the pair's balance of this token without going through the pair?",
   "Is sync()/skim() reachable in the same transaction as such a change?",
   "Can a zero-value or dust transfer trigger the deferred branch?",
   "What is the maximum reserve skew achievable in one transaction, and what does it cost?"],
 evidence_strength="HIGH",
 propagation_notes="Template-propagated rather than fork-propagated: independent BSC token deployments repeatedly reimplement the same deferred-burn pattern. Independent code lineages are counted separately; the Computility-associated pair (TGAI/YSDAO) is one lineage. DARKNAVY documents additional 2026 instances (STO, Movie Token) confirming the template. Expect continued recurrence on any chain with cheap deployment and copy-pasted deflationary token templates."),

"BRIDGE-MESSAGE-NOT-BOUND-TO-SOURCE": dict(
 title="Cross-domain payout or mint is not bound to a proven, value-matched, single-use source event",
 broken_invariant="A release, mint or payout on the destination domain must be authorised only by a proof that binds, simultaneously: the source chain identity, the source channel/route, the exact asset, the exact amount, the recipient, and a nonce that is consumed exactly once. Verifying that a message is well-formed or correctly signed is not the same as verifying that it corresponds to a real deposit of equal value.",
 mechanism="The destination-side contract validates some fields but omits at least one binding. Observed omissions: value equality between source commitment and destination payout (Verus checkCCEValues); source channel / denomination path (Secret CW20-ICS20, deleted checks); economic reality of the deposit, so the bridge's own wrapped token self-transferred with a valid memo counts as a deposit (Coreum); the event that relayers key on can be spoofed by an unrelated program (Across on Solana); authority granted by a forged message (Hyperbridge); external-chain block/state data injected through a peripheral updater (Stake DAO Votemarket).",
 mandatory_preconditions=[
   "A destination-side contract mints, releases or grants authority in response to a message asserting a source-domain event",
   "That path is reachable by, or on behalf of, an unprivileged party (permissionless relay, or a relayer whose input is attacker-shapeable)",
   "At least one of {source chain id, channel/route, asset, amount, recipient, nonce-consumption} is not enforced against the proof",
   "The destination side holds redeemable reserves, or the minted asset is redeemable through a legitimate route"],
 optional_amplifiers=["Attacker can stand up their own source chain / IBC channel cheaply","Privacy-by-default chain delays detection","Redeposits after a known-unfixed flaw refill the reserve"],
 applicable_protocol_archetypes=["bridge","canonical bridge","cross-chain messaging","IBC/CosmWasm bridge contract","intents/solver relayer","liquid staking with cross-chain mint","OFT/omnichain token"],
 static_indicators=[
   "mint/release keyed on a message struct without an amount-equality assertion against the source commitment",
   "commented-out or removed channel/denom validation",
   "processedNonces / usedHashes mapping absent, or written after external calls",
   "message hash built with abi.encodePacked over dynamic fields",
   "trusted-remote / peer mapping settable without timelock"],
 adapter_indicators=["adapter counts destination-side wrapped supply as TVL","adapter treats escrow balance and wrapped supply as independent","bridge adapter enumerates vaults but not the mint authority"],
 runtime_state_indicators=[
   "wrapped supply on destination > escrowed backing on source",
   "peers/trusted remotes pointing at addresses with no deployed code or recent changes",
   "relayer/prover set with a single member, or a single DVN",
   "reserve refilled after a publicly known unfixed flaw"],
 cross_contract_indicators=["escrow contract on source vs mint authority on destination not reconcilable from public data","light client / prover registry mutable by a non-timelocked role"],
 decisive_guards=[
   "Destination asserts payout amount == amount committed on source, in the same proof",
   "Proof binds source chain id AND channel/port AND denomination path",
   "Nonce/message hash marked consumed before any external call, and replay reverts",
   "Deposit validity requires an external asset actually escrowed, so the bridge's own wrapped token cannot be a deposit",
   "Independent verification set (>1 DVN/prover) with no single failover"],
 false_positive_killers=[
   "Destination mint requires a Merkle/zk proof against a source state root that itself commits to the amount",
   "Reserve reconciliation is enforced on-chain (mint reverts if supply would exceed escrow)",
   "Bridge is one-way with no destination-side release"],
 local_defensive_property="On a pinned fork of the destination chain, no sequence of destination-side calls may increase redeemable value without a matching, previously unconsumed source commitment of equal value.",
 evidence_strength="HIGH",
 propagation_notes="Verus is a repeat of one unremediated root cause (May and July 2026 are the same defect, not two mechanisms) and counts once toward unique root causes. Secret Network's defect existed in the repo from its first commit in 2023 and ran live for three years, which is the general shape: bridge validation gaps are long-lived and only surface when reserves grow."),

"UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY": dict(
 title="A deprecated or superseded deployment retains funds, approvals or authority",
 broken_invariant="Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.",
 mechanism="The team ships a v2/new deployment and stops maintaining the old one, but the old contract is immutable or unpaused and still holds residual liquidity, still has live ERC-20/ERC-721 approvals from users, or still holds a role in a live system. Attackers find the old contract long after attention moved on. Sub-shapes seen: immutable escape hatch with no ownership check (Aztec Bridge); incomplete proof verification in a deprecated router (Aztec Connect); LP-mint validation gap in a retired AMM program (Raydium V3); leftover rewards pool with an uninitialised accumulator (Scallop V2 rewards); old deposit path still callable alongside the new one (Haedal); legacy vault with different redemption math (Thetanuts); legacy pools still holding fees (Huma V1).",
 mandatory_preconditions=[
   "A prior-version deployment is still callable on a live chain",
   "It still holds value, live approvals, or an authority role",
   "Its code path differs from the maintained version (or is unmaintained/immutable)",
   "No pause/guardian can stop it, or the pause was never applied"],
 optional_amplifiers=["Immutable contract with no owner","Front end removed so nobody watches it","Audit scope covered only the current version","Value drifts back in via residual LP or fees"],
 applicable_protocol_archetypes=["any protocol with more than one deployed version","bridge","DEX/AMM","vault/share token","lending","reward distributor","rollup"],
 static_indicators=["multiple deployment generations in docs/repo with only the newest audited","immutable contracts with escape-hatch functions","initializer/version counters that differ between deployments"],
 adapter_indicators=[
   "DefiLlama adapter still lists v1/legacy addresses alongside v2",
   "adapter has a commented-out or removed legacy section while the addresses remain funded on-chain",
   "adapter module path contains v1/v2/legacy/deprecated/old"],
 runtime_state_indicators=[
   "legacy contract holds non-trivial token balances",
   "non-zero allowances from live EOAs to the legacy contract",
   "legacy contract holds a role (MINTER/BRIDGE/DISTRIBUTOR) in a current contract",
   "no Paused event; functions still succeed in eth_call simulation"],
 cross_contract_indicators=["legacy address appears in a current registry/whitelist","legacy proxy admin still owned by a live multisig"],
 decisive_guards=[
   "Legacy deployment is paused AND drained AND has no live role",
   "Approvals to legacy contracts revoked or rendered inert by a token-side blocklist",
   "Legacy contract self-destructed or upgraded to a no-op implementation"],
 false_positive_killers=["Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed)","Contract reverts on every state-changing entrypoint (verified paused)"],
 local_defensive_property="For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.",
 evidence_strength="HIGH",
 propagation_notes="Nine in-window incidents across five chains and every archetype. This is the highest-yield family for a discovery pass because the prerequisites are directly observable from public data (adapter history, balances, allowances, role reads) without reading any application logic."),

"ORACLE-STALE-OR-SILENT-FALLBACK": dict(
 title="Price feed identity, freshness or failure mode is wrong, and the failure is silent",
 broken_invariant="A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.",
 mechanism="Configuration or fallback logic yields a price that does not describe the asset at its current economic value, and nothing reverts. Observed shapes: wrong feed assigned to an asset (Ploutos used BTC/USD for USDC; Solido fell back to the CASH oracle for SOLID); an invalid pool parameter makes the lookup return address(0) and the oracle returns zero instead of reverting (Singularity, Uniswap V3 fee tier 42 -> getPool()==0 -> totalAssets counted only idle USDC); a capped-price adapter mis-parameterised so the reported price is materially below true value (Aave V3 CAPO/wstETH, ~2.85% low, causing wrongful liquidations); a stored price with a long refresh cooldown used to size rewards while realisation happens at live price (LML, 3600s).",
 mandatory_preconditions=[
   "A value-bearing decision (borrow, mint, redeem, liquidate, reward-size) reads a configured feed",
   "Feed selection, fallback or cap is settable by configuration rather than fixed to the asset",
   "The failure/edge path returns a usable number instead of reverting (zero, stale, capped, or another asset's price)",
   "Live positions or reserves are exposed to that decision"],
 optional_amplifiers=["Flash liquidity to enter and exit inside one block","Long undetected misconfiguration window","Asset with few independent feeds","Newly listed asset"],
 applicable_protocol_archetypes=["lending","CDP","stablecoin issuer","vault/share token","risk curator","derivatives","yield"],
 static_indicators=[
   "latestRoundData() used without checking updatedAt/answeredInRound or answer > 0",
   "try/catch around a feed with a non-reverting fallback",
   "factory.getPool(...)/getFeed(...) result used without a zero-address check",
   "per-asset oracle mapping settable by an EOA or non-timelocked role",
   "price cap / growth-rate adapters with governance-set parameters"],
 adapter_indicators=["DefiLlama `oracles` field lists a single oracle","adapter prices assets by hardcoded peg or by a pool read rather than the protocol's own oracle","adapter's token list includes assets with no deep independent market"],
 runtime_state_indicators=[
   "oracle mapping entries pointing at address(0) or at a feed whose description() names a different asset",
   "feed updatedAt older than the protocol's own heartbeat",
   "configured pool/fee-tier parameters that do not resolve to a deployed pool",
   "reported asset price materially divergent from independent venues"],
 cross_contract_indicators=["oracle admin != protocol timelock","the same feed reused across assets in the mapping"],
 decisive_guards=[
   "Staleness check on updatedAt with a bound tighter than the feed heartbeat, reverting on breach",
   "answer > 0 and zero-address checks that revert",
   "Feed-to-asset binding asserted on registration (description/decimals/base-quote validated)",
   "Deviation bound against an independent second source",
   "Sequencer-uptime check on L2s"],
 false_positive_killers=[
   "Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape)",
   "Every feed read reverts on zero/stale (kills the silent-fallback shape)",
   "Asset valuations cross-checked against a second independent oracle with a hard deviation cap"],
 local_defensive_property="On a fork, force each configured feed to return zero, a stale timestamp, and a 10x/0.1x value; every value-bearing entrypoint must revert rather than transact.",
 evidence_strength="HIGH",
 propagation_notes="The dominant lending-side family of the window and the one most often caused by curation rather than code: Blend/YieldBlox and Aave CAPO were both operator/curator parameter failures on unmodified core contracts. That makes DefiLlama's Risk Curators and Lending categories the highest-yield screening surface."),

"ORACLE-SPOT-THIN-LIQUIDITY": dict(
 title="Capacity or reward sized from a price movable inside the attacker's own transaction on a venue thinner than the capacity it unlocks",
 broken_invariant="Borrowing capacity, mint size, reward size or collateral value must not be derived from a price that a single actor can move within the manipulation window, and the value unlocked must never exceed the cost of moving that price.",
 mechanism="The protocol reads a spot price or reserve ratio (AMM getReserves, a single-DEX quote, or an external oracle that itself tracks a thin venue) and immediately sizes a value-bearing action from it. The attacker funds a large swap (often flash-borrowed), moves the price on the thin venue, takes the oversized action, and unwinds in the same transaction or shortly after. Flash liquidity is an amplifier that supplies temporary capital; the root cause is the unbounded, unaveraged, un-deviation-checked price input.",
 mandatory_preconditions=[
   "A value-bearing action is sized from a price or reserve reading",
   "That reading is derived from a venue an unprivileged actor can move (directly, or via an oracle that tracks it)",
   "No TWAP, no deviation bound, and no liquidity/notional cap gates the action",
   "The value unlocked by the moved price exceeds the cost of moving it"],
 optional_amplifiers=["Flash loans","Same-block entry and exit","Low-float or newly listed collateral","Referral/multiplier logic on top of the sized value"],
 applicable_protocol_archetypes=["lending","CDP","staking pool","reward distributor","bonding","yield","liquidity manager","stablecoin issuer"],
 static_indicators=[
   "getReserves()/slot0()/getAmountsOut() feeding a mint, borrow, stake or reward computation",
   "quote taken once and reused after a state-changing swap in the same function",
   "reward = f(price) with price read from a pair the protocol also trades against",
   "no OBSERVATION/TWAP window parameter anywhere in the pricing path"],
 adapter_indicators=["adapter prices the protocol's own token from a single pair","protocol TVL concentrated in one thin pair","adapter lists collateral assets with no major-venue liquidity"],
 runtime_state_indicators=[
   "collateral/listed asset whose deepest venue depth is small relative to the borrow capacity it unlocks",
   "borrow caps absent or far above venue depth",
   "reward contract holding a reserve larger than the cost to move the reference pair"],
 cross_contract_indicators=["the pricing pair and the protocol's own reserve are the same pool","oracle contract reads a DEX the protocol itself seeds"],
 decisive_guards=[
   "TWAP over a window long enough that manipulation cost exceeds the value unlocked",
   "Hard deviation bound against an independent deep-market source, reverting on breach",
   "Per-asset borrow/mint caps set below the manipulation cost on the deepest available venue",
   "Value sized from the amount actually transferred in, not from a quoted price"],
 false_positive_killers=[
   "All collateral priced by a deep aggregated feed with a deviation cap (kills the pair)",
   "Caps are set from measured venue depth and enforced on-chain",
   "The action is sized from realised transfer amounts, so price is never an input"],
 local_defensive_property="On a fork, execute a max-size flash-funded swap against every venue in the pricing path and assert that no value-bearing entrypoint changes its output beyond the configured deviation bound.",
 evidence_strength="HIGH",
 propagation_notes="The distinguishing screening question is not 'does it use an oracle' but 'is the deepest venue behind that price thinner than the capacity it unlocks'. Blend/YieldBlox is the clearest case: unmodified core contracts, a curator-listed asset (USTRY) with an SDEX market thin enough to move ~100x in one trade."),
}
