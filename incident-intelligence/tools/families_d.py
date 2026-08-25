# -*- coding: utf-8 -*-
"""Mechanism families, part D: handler-runtime classes, plus one reference-derived family.

Why this file exists separately
-------------------------------
Parts A-C were derived from an EVM-shaped corpus, and it shows: every static
indicator in them is Solidity. Four of the five families here describe defects
that CANNOT occur on the EVM, because the EVM's revert semantics unwind all state
when a call fails. On Cosmos SDK, Substrate, Move and Solana runtimes a handler
can write state, fail, and have the write survive -- so "did the failure roll the
write back" becomes a real question with a real answer, and the answer is
sometimes no.

They are derived from INC-2026-08-18-MAY (Maya Protocol, 2026-08-18, in window),
whose six chained bugs were verified against the live public mayanode source at
exact file and line. See incidents/included.jsonl for the corroboration record.

ACC-QUOTE-STALE-ACROSS-OWN-SWAP is different in provenance and is marked as such:
it is derived from operator-supplied prior art on a protocol that is NOT in this
run's window corpus and NOT listed on DefiLlama. It therefore contributes zero
incidents and zero loss to every window statistic in this run, and is carried only
because the shape is screenable on the EVM universe that the rest of the run covers.
"""
def F(**kw): return kw

FAM_D = {

"RUNTIME-STATE-COMMITTED-BEFORE-FUNDING-TRANSFER": F(
 title="A credit is written and persisted before the transfer meant to fund it, and the transfer can fail without undoing the credit",
 broken_invariant="A balance may not be credited until the value backing it has actually moved. Where a runtime lets a handler persist state and then fail, the write and the funding transfer must be one atomic unit, or the write must come strictly after the transfer succeeds.",
 mechanism="Maya Protocol's slash-subsidy path added the subsidy to the pool's native balance and called SetPool() -- committing it -- and only then attempted SendFromModuleToModule(Reserve -> Asgard) to actually fund it. The Reserve held ~168k CACAO against a ~49.45M CACAO subsidy, so the send failed and returned an error, but the inflated pool balance was already in state. On the EVM the failing send would have reverted the whole call; on a Cosmos SDK handler it does not.",
 mandatory_preconditions=[
   "A runtime where a handler can persist state and then return an error without the runtime discarding the write",
   "A credit or balance increase written through a setter (SetX / store.Set / borrow_global_mut) before the transfer that funds it",
   "The funding transfer can fail on a condition an external caller can reach (insufficient module balance, paused, rate limit)",
   "The credited balance is spendable by a subsequent transaction"],
 optional_amplifiers=["A module account whose balance is normally far below the largest possible credit",
   "Subsidy, rebate, slash or insurance logic that sizes a credit from a ratio",
   "No closing invariant assert over module totals"],
 applicable_protocol_archetypes=["Cosmos SDK app-chain","cross-chain liquidity network","Substrate/Polkadot parachain",
   "Move (Sui/Aptos) module","Solana program with CPI","any handler-based L1"],
 static_indicators=[
   "SetPool/SetX/store.Set called before SendFromModuleToModule or bank.SendCoins in the same function",
   "a keeper setter followed later by a transfer whose error is returned rather than panicked",
   "balance mutation followed by a transfer guarded only by if err != nil { return err }",
   "no cosmos CacheContext()/Snapshot()/write() wrapper around a multi-step balance change"],
 adapter_indicators=["adapter reads a module or vault balance the protocol itself credits",
   "adapter treats a subsidy/reserve module as part of TVL"],
 runtime_state_indicators=["a module account balance materially smaller than the largest credit its own code can compute",
   "pool or vault balances that do not reconcile against the sum of module holdings"],
 cross_contract_indicators=["credit written in one module, funding sourced from another module's account"],
 decisive_guards=[
   "The whole credit-and-fund sequence runs inside a cached context that is only written on success (CacheContext + write())",
   "The transfer is executed first and the credit is derived from the amount actually received",
   "A closing assert that total credited equals total transferred, panicking on mismatch"],
 false_positive_killers=[
   "The sequence is wrapped in a cache context committed only on success (kills the pair)",
   "The setter runs strictly after the transfer returns nil",
   "The handler panics rather than returning an error, so the runtime discards the write"],
 local_defensive_property="On a local devnet, drive the funding transfer to fail (drain or cap the funding module) and re-read the credited balance; it must be unchanged.",
 evidence_strength="HIGH",
 derivation="WINDOW_CORPUS: INC-2026-08-18-MAY, verified against live public source",
 propagation_notes="Structurally impossible on the EVM. Applies to every Cosmos SDK chain that mutates balances outside a cache context, which is the common case in hand-written keeper code."),

"RUNTIME-HANDLER-ERROR-NO-ROLLBACK": F(
 title="A handler's error is logged and execution continues in the same context, so whatever it already wrote survives",
 broken_invariant="A failed operation must leave no trace. When a dispatcher calls a handler that can write state, an error from that handler must discard the writes, not merely be recorded.",
 mechanism="Maya's observed-outbound dispatcher called each message handler and, on error, logged 'handler failed', slashed, marked the voter done and executed `continue` -- in the same cosmos context, with no rollback. The partially applied subsidy from the failed inner handler stayed in state, and the loop moved to the next message. The inner code even carried a comment noting it mirrored upstream behaviour.",
 mandatory_preconditions=[
   "A dispatcher loop that invokes handlers able to write state",
   "The error branch logs, records or slashes but does not discard the context",
   "Execution continues (continue / next / ignore) rather than aborting the transaction",
   "At least one reachable handler writes value-bearing state before it can fail"],
 optional_amplifiers=["Batched messages so one failure does not stop the rest",
   "A voter/consensus object marked done on the error path, preventing re-processing",
   "Metrics or slashing on the error path that make the failure look handled"],
 applicable_protocol_archetypes=["Cosmos SDK app-chain","bridge or observer network with vote aggregation",
   "Substrate parachain","any runtime with a message dispatcher"],
 static_indicators=[
   "ctx.Logger().Error(...) immediately followed by continue inside a range over messages",
   "handler(ctx, m) whose returned error is logged but not propagated",
   "SetDone()/MarkProcessed() called on the error branch",
   "err != nil branches that neither return nor panic inside a dispatcher loop"],
 adapter_indicators=["adapter depends on an observer/voter module's accounting"],
 runtime_state_indicators=["voters or observation records marked done whose corresponding effect never completed",
   "error-path counters non-zero on a chain whose balances still reconcile only approximately"],
 cross_contract_indicators=["dispatcher and the handlers it calls live in different modules with separate state"],
 decisive_guards=[
   "Each handler invocation runs in its own cache context, written only on nil error",
   "The dispatcher aborts the transaction on handler error",
   "A post-loop invariant check over module balances that panics on drift"],
 false_positive_killers=[
   "Handlers are invoked through a cache context discarded on error (kills the pair)",
   "The dispatcher returns the error and the runtime aborts",
   "Handlers on that path are proven side-effect-free before the failure point"],
 local_defensive_property="On a devnet, force one handler in a batch to fail after it writes, then assert that no state it touched changed and that no completion marker was set.",
 evidence_strength="HIGH",
 derivation="WINDOW_CORPUS: INC-2026-08-18-MAY, verified against live public source",
 propagation_notes="Pairs with RUNTIME-STATE-COMMITTED-BEFORE-FUNDING-TRANSFER: the first creates the orphaned write, this one keeps it. Either alone is usually survivable."),

"RUNTIME-BATCHED-MESSAGE-SHARED-KEY-CLOBBER": F(
 title="Several messages in one transaction key state by a value they all share, so the last one silently overwrites the rest",
 broken_invariant="Distinct logical operations must not share a mutable state key. Where a batch is keyed by transaction identity rather than by message identity, each message must occupy its own slot.",
 mechanism="Maya's deposit handler built a fresh ObservedTxVoter keyed on the native transaction ID and stored it with SetObservedTxInVoter() for every message in the batch. A single MsgDeposit carrying 23 messages therefore wrote the same key 23 times; the final DONATE message's voter overwrote all twenty-two trade-withdrawal voters, resetting OutboundHeight to 0 and marking the transaction done. The withdrawals became invisible to the outbound matcher.",
 mandatory_preconditions=[
   "A transaction may carry several messages that the runtime processes in one pass",
   "Per-message state is keyed by something all the messages share (tx hash, sender, block height)",
   "The write is an unconditional overwrite rather than an append or a keyed insert",
   "A later message can therefore erase an earlier message's record"],
 optional_amplifiers=["No cap on messages per transaction","A message type that resets a height, nonce or done-flag",
   "Downstream logic that treats a missing record as evidence of loss"],
 applicable_protocol_archetypes=["Cosmos SDK app-chain","bridge with observation voters","Solana program processing instruction batches",
   "any protocol accepting multi-message transactions"],
 static_indicators=[
   "NewXVoter(tx.ID, ...) / New*(txHash) constructed inside a per-message loop",
   "SetX(ctx, obj) with a key derived from tx hash inside a range over msgs",
   "state keyed by GetTxID()/hash without a message index or sequence suffix",
   "a struct rebuilt from scratch per message rather than fetched-then-appended"],
 adapter_indicators=["adapter relies on observation or voter records to establish balances"],
 runtime_state_indicators=["voter/observation records whose message count is lower than the transaction's message count",
   "records whose height fields are zero where a height was expected"],
 cross_contract_indicators=["the overwritten record is consumed by a different module than the one that writes it"],
 decisive_guards=[
   "State keyed by (tx id, message index) or by a per-message hash",
   "Fetch-then-append semantics, with an assert that no existing record is dropped",
   "An explicit per-transaction message-count limit combined with a uniqueness check"],
 false_positive_killers=[
   "The voter is fetched and appended to rather than reconstructed (kills the pair)",
   "The key includes a message index or per-message nonce",
   "The runtime rejects transactions carrying more than one such message"],
 local_defensive_property="On a devnet, submit one transaction carrying two operations of the same type and assert both records survive with their own heights.",
 evidence_strength="HIGH",
 derivation="WINDOW_CORPUS: INC-2026-08-18-MAY, verified against live public source",
 propagation_notes="The entry point of the Maya chain. Harmless alone; dangerous because downstream code reads a missing record as proof that funds were stolen."),

"RECONCILIATION-STRIDE-SKIPS-TRUE-VALUE": F(
 title="A reconciliation scan steps by a fixed stride, so the true value can fall between steps and read as missing",
 broken_invariant="A search for a record that exists must find it. A reconciliation loop must enumerate the actual candidate set, not sample it at an interval, and a miss must never by itself be treated as proof of loss.",
 mechanism="Maya's outbound matcher read voter.OutboundHeight -- zeroed by the voter clobber -- fell back to FinalisedHeight, then looped `for height := outHeight; height <= now; height += signingTransPeriod`. The LINK outbounds had landed at FinalisedHeight+1, one block into a 300-block stride, so the loop never examined that height. The outbounds were declared missing and the slash-for-theft path fired against assets that had in fact been sent.",
 mandatory_preconditions=[
   "A loop that scans for a record by stepping a counter by a fixed interval",
   "The origin of the scan is derived from state an external caller can influence or reset",
   "The true location can lie strictly between two steps",
   "A miss triggers a compensating, punitive or minting path rather than a retry or an abort"],
 optional_amplifiers=["The stride is a governance constant far larger than one block",
   "The fallback origin is a different quantity than the one the stride was designed around",
   "The compensating path sizes a payout from a ratio rather than a fixed amount"],
 applicable_protocol_archetypes=["cross-chain liquidity network","bridge","observer/oracle network",
   "epoch settlement system","any protocol with slash-for-theft or insurance logic"],
 static_indicators=[
   "for height := start; height <= end; height += period  with period a constant, not 1",
   "a scan origin taken from a field that can be zero, with a fallback to a different field",
   "a not-found branch that slashes, subsidises, mints or compensates",
   "range steps derived from SigningTransactionPeriod / epoch length used as a search stride"],
 adapter_indicators=["adapter models a bridge or settlement network with outbound queues"],
 runtime_state_indicators=["outbound or settlement records whose recorded height differs from where the effect landed",
   "slash or compensation events with no corresponding confirmed loss"],
 cross_contract_indicators=["the scanned records are written by a different module than the scanner"],
 decisive_guards=[
   "The scan enumerates the real index (by tx id or by a stored pointer) instead of walking heights",
   "Stride of one, or an inclusive range check rather than equality at sampled points",
   "A miss requires independent confirmation of loss before any compensating path runs"],
 false_positive_killers=[
   "Lookup is by identifier against an index, not by walking a counter (kills the pair)",
   "The not-found branch only retries or aborts and cannot move value",
   "The compensating amount is capped by an independently measured balance"],
 local_defensive_property="On a devnet, place the record one unit past the scan origin and confirm the reconciler finds it and that no compensating path fires.",
 evidence_strength="HIGH",
 derivation="WINDOW_CORPUS: INC-2026-08-18-MAY, verified against live public source",
 propagation_notes="Not runtime-specific -- the same shape appears in EVM epoch-settlement and claim-window code. Listed here because the Maya instance is the corroborated one."),

"ACC-QUOTE-STALE-ACROSS-OWN-SWAP": F(
 title="An accounting value is fixed from a spot quote taken before the protocol's own swap moves the very reserves it quoted",
 broken_invariant="A value used for minting, crediting or reward must be derived from what the protocol actually received, not from a quote taken before the protocol itself moved the market. Where the protocol's own action changes the price it just read, the value must be recomputed after the fact.",
 mechanism="A staking entrypoint computed a stake amount from a spot quote on an AMM pair, then executed its own large swap into that same pair, then added liquidity at the drastically skewed post-swap ratio. The stake amount was never recomputed from the assets actually deposited or from the fair value of the LP tokens received. Treasury logic trusted the stale figure, minted against it, and paid an inviter reward to an attacker-controlled referral address in the same transaction; the newly minted tokens were sold straight back into the pair. Flash liquidity set the scale, but the defect is that the protocol priced itself before moving the price.",
 mandatory_preconditions=[
   "A quote or price read taken from a venue the protocol is about to trade against",
   "The protocol's own swap or deposit materially moves that venue's reserves in the same transaction",
   "The accounting value is not recomputed from assets actually received or LP tokens actually minted",
   "Something of value is minted, credited or paid out against the stale figure"],
 optional_amplifiers=["Flash-loan liquidity to size the swap","A referral or inviter reward paid in the same transaction",
   "Minted tokens immediately sellable into the same pair","No slippage bound on the protocol's own swap"],
 applicable_protocol_archetypes=["bonding/staking with LP deposit","treasury-backed token issuer","launchpad",
   "liquidity bond protocol","reward distributor sized from a quote"],
 static_indicators=[
   "getAmountsOut/getAmountOut/quote called before a swap in the same function",
   "an amount captured into a local variable before addLiquidity and used after it",
   "mint or reward sized from a pre-swap quote rather than from the LP balance delta",
   "addLiquidity called without recomputing value from the returned amountA/amountB/liquidity",
   "referral or inviter transfer in the same function as a mint"],
 adapter_indicators=["adapter values a bond or staking position from a pair quote",
   "protocol methodology describes LP bonds or treasury-backed issuance"],
 runtime_state_indicators=["a bonding entrypoint reachable permissionlessly with no per-transaction size cap",
   "pair reserves small relative to the maximum accepted deposit"],
 cross_contract_indicators=["the quoting venue and the venue the protocol trades against are the same pair",
   "treasury mints against a figure computed in a separate staking contract"],
 decisive_guards=[
   "Value recomputed from the LP token balance delta actually received",
   "A manipulation-resistant price (TWAP or an independent feed) used for accounting, with a deviation bound against spot",
   "An assert that minted value does not exceed backing actually added to the treasury",
   "Reward settlement deferred past the transaction that created the position"],
 false_positive_killers=[
   "The minted amount is derived from the LP balance delta or from a TWAP (kills the pair)",
   "The protocol's swap is bounded so it cannot move reserves materially",
   "Rewards settle in a later block against re-measured backing"],
 local_defensive_property="On a fork, run the bonding path with a flash-funded swap sized to skew the pair, then assert that the minted or credited amount tracks the LP tokens actually received rather than the pre-swap quote.",
 evidence_strength="MEDIUM",
 derivation="REFERENCE_PRIOR_ART: operator-supplied root cause for a protocol not in this run's window corpus and not listed on DefiLlama. Contributes zero incidents and zero loss to every window statistic in this run.",
 propagation_notes="Carried because the shape is screenable across the EVM universe this run already covers, and because 'quote, then move the price yourself, then never re-measure' is a distinct defect from ordinary oracle manipulation: no external attacker input is needed to move the price, the protocol does it to itself."),

"PRECOMPILE-NESTED-CALL-STATE-NOT-PROPAGATED": F(
 title="State written inside a nested or partially-executed precompile call is not propagated to, or reverted with, the outer execution context",
 broken_invariant="State written during EVM execution must be committed or discarded atomically with the execution that produced it. A precompile bridging the EVM into host-chain state must propagate its writes to the outer context on success and leave nothing behind on failure. Where the two state models disagree, the same balance becomes spendable twice.",
 mechanism="Cosmos EVM's ICS20 precompile (ASA-2026-002 / GHSA-54gx-3cgr-7mfm / GO-2026-4677) did not correctly reflect state updates performed during recursive calls in the outer execution context, so under certain execution conditions the same token balance could be used repeatedly within a single transaction -- an unbacked-supply primitive. A sibling advisory (GHSA-mjfq-3qr2-6g84) reaches the same outcome from the other direction: setting a lower EVM call gas limit lets a caller partially execute a precompile and error at a chosen point WITHOUT reverting the partially written state, which on the distribution precompile transfers funds without resetting claimable rewards, and can also induce non-deterministic execution and halt validators. The vulnerable code lived upstream from July 2024 and was found by exploitation in January 2026, not by audit.",
 mandatory_preconditions=[
   "An execution environment that calls out to host-chain state through precompiles or an equivalent bridge",
   "State written inside that call is staged separately from the outer context, or committed separately from it",
   "A caller can cause the inner call to nest, or to terminate early at a point of their choosing (for example by bounding gas)",
   "A balance, reward or supply figure is read or written on both sides of that boundary"],
 optional_amplifiers=["The precompile moves value directly (ICS20 transfer, distribution rewards)",
   "The native asset is used as collateral elsewhere, turning unbacked supply into cross-protocol contagion",
   "Bridged or wrapped representations of the native asset exist on other chains, so reconciliation must span chains",
   "A small validator set that can ship an emergency upgrade without full review"],
 applicable_protocol_archetypes=["Cosmos SDK app-chain with an EVM execution layer","evmOS / Evmos-derived chain",
   "any runtime exposing host-state precompiles to a general-purpose VM","chain-level module, not a deployed contract"],
 static_indicators=[
   "a precompile Run/Execute path that writes host state without a snapshot/revert wrapper",
   "stateDB.Snapshot()/RevertToSnapshot absent around a precompile that mutates keeper state",
   "precompile state committed via a keeper call rather than through the EVM journal",
   "a precompile invoked recursively, or reachable from within another precompile's execution",
   "go.mod requiring github.com/cosmos/evm below v0.6.0, or a vendored x/evm tree with no module requirement"],
 adapter_indicators=["adapter values assets native to a Cosmos SDK chain with an EVM layer"],
 runtime_state_indicators=["total supply of the native asset not reconciling against the sanctioned minting path",
   "module-account and IBC-escrow balances not conserving across a block",
   "the enabled static-precompile set differing before and after a chain restart"],
 cross_contract_indicators=["the defect lives in a shared upstream module, so it is simultaneously live across every chain that vendors or requires it, each with independent upgrade authority"],
 decisive_guards=[
   "Every precompile execution wrapped in an atomic function that reverts partially committed state on error",
   "Precompile state changes journaled through the EVM state object so the outer context reverts them",
   "A per-block supply-conservation invariant that halts on any delta outside the sanctioned minting path",
   "Upgrade to a release where the advisory is fixed, rather than disabling the feature by configuration"],
 false_positive_killers=[
   "The precompile stages writes in a snapshot the outer context commits or reverts (kills the pair)",
   "The chain is on a release at or above the patched version AND the enabled precompile set is verified on-chain",
   "The feature is not compiled into the running binary at all, not merely disabled by parameter"],
 local_defensive_property="On a local devnet, call the precompile from inside another call and bound the gas so it errors partway; then assert that no host-chain balance changed and that total supply is unchanged.",
 evidence_strength="MEDIUM",
 derivation=("OPERATOR_SUPPLIED_THREAT_INTELLIGENCE + VENDOR ADVISORIES. The confirmed exploitation "
   "(Saga EVM, 2026-01-21, ~$7M) falls OUTSIDE this run's window and contributes nothing to any window "
   "statistic. The two in-window events carrying this family (MANTRA 2026-08-20, TAC chain 2026-08-22) are "
   "PROVISIONAL grade C: the subsystem is named, the mechanism is not, no loss is published, and attribution "
   "is explicitly unresolved by both the chain teams and the vendor."),
 propagation_notes=("Converges with two families this run derived independently from INC-2026-08-18-MAY. "
   "GHSA-mjfq-3qr2-6g84 -- partial precompile execution that errors at a chosen point without reverting "
   "already-written state -- is the same broken invariant as RUNTIME-STATE-COMMITTED-BEFORE-FUNDING-TRANSFER "
   "and RUNTIME-HANDLER-ERROR-NO-ROLLBACK, reached through a different mechanism on a different chain. Two "
   "independent derivations landing on one invariant is the strongest evidence this run has that the "
   "EVM-semantics / SDK-state-commitment boundary is a durable defect class rather than a set of one-off bugs. "
   "The distribution shape is the distinguishing feature: this is a shared upstream module live across "
   "sovereign networks with independent upgrade authority and no patch-compliance mechanism, so remediation "
   "lag is measured in quarters and a fix shipping upstream says nothing about any given downstream chain."),
),

}
