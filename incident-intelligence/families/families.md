# Mechanism Family Library — six-month window 2026-02-22 to 2026-08-22

Families are clustered by **broken invariant + mechanism + mandatory prerequisite signature + decisive missing guard**, never by the source database's attack-method label. The SlowMist `Attack method` string is carried on each incident record only as `slowmist_attack_method_label_NOT_USED_FOR_CLUSTERING`.

**43 families** derived from 110 grade-A/B incidents. 8 are single-event families and are labelled as such: they make no recurrence claim.

## Index

| Family | Incidents | Unique root causes | 6-month loss | Most recent | Evidence |
|---|---:|---:|---:|---|---|
| `TOKEN-DEFERRED-BURN-LP-RESERVE-DESYNC` | 14 | 14 | $5,425,242 | 2026-07-28 | HIGH |
| `BRIDGE-MESSAGE-NOT-BOUND-TO-SOURCE` | 7 | 6 | $26,666,000 | 2026-08-09 | HIGH |
| `ORACLE-SPOT-THIN-LIQUIDITY` | 7 | 7 | $21,658,540 | 2026-08-15 | HIGH |
| `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY` | 7 | 7 | $6,971,179 | 2026-06-17 | HIGH |
| `PROOF-VERIFICATION-BYPASSED` | 6 | 6 | $7,372,966 | 2026-07-02 | HIGH |
| `ORACLE-STALE-OR-SILENT-FALLBACK` | 5 | 5 | $2,688,400 | 2026-07-23 | HIGH |
| `GOV-CHEAP-CONTROL-NO-TIMELOCK` | 4 | 4 | $22,356,000 | 2026-07-15 | HIGH |
| `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED` | 4 | 4 | $19,864,350 | 2026-06-10 | HIGH |
| `CALLDATA-CALLER-CONTROLLED-TARGET` | 4 | 4 | $3,798,750 | 2026-08-06 | HIGH |
| `LIQUIDATION-ON-MANIPULABLE-VALUATION` | 4 | 4 | $3,360,921 | 2026-07-22 | HIGH |
| `AUTH-MISSING-ON-VALUE-MOVING-PATH` | 4 | 4 | $814,000 | 2026-07-28 | HIGH |
| `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET` | 3 | 3 | $18,524,350 | 2026-04-22 | HIGH |
| `ACC-DONATION-UNACCOUNTED-BALANCE` | 3 | 3 | $9,980,000 | 2026-07-06 | HIGH |
| `ACC-NAV-SHAREPRICE-MANIPULABLE` | 3 | 3 | $6,856,000 | 2026-07-06 | HIGH |
| `SECRET-EMBEDDED-IN-PUBLIC-CODE-AS-AUTH` | 3 | 3 | $4,171,100 | 2026-07-30 | HIGH |
| `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 3 | 3 | $3,064,900 | 2026-07-14 | HIGH |
| `ACC-MULTI-PATH-CREDIT-DRIFT` | 3 | 3 | $2,725,779 | 2026-08-18 | HIGH |
| `CALLBACK-UNAUTHENTICATED-CALLER-USES-APPROVALS` | 3 | 3 | $1,687,200 | 2026-07-13 | HIGH |
| `TOKEN-TRANSFER-OVERRIDE-BREAKS-CONSERVATION` | 3 | 3 | $475,500 | 2026-06-28 | HIGH |
| `ACC-ZERO-SUPPLY-INFLATION` | 3 | 3 | $412,000 | 2026-06-15 | HIGH |
| `AUTH-IDENTITY-SATISFIABLE-BY-ATTACKER-CONTRACT` | 3 | 3 | $278,700 | 2026-05-23 | HIGH |
| `ACC-REWARD-INDEX-INIT-AND-ORDERING` | 3 | 3 | $244,035 | 2026-06-09 | HIGH |
| `CALLBACK-STATE-LOCK-INCOMPLETE` | 3 | 3 | $68,300 | 2026-07-30 | HIGH |
| `SIG-DIGEST-AMBIGUOUS-OR-UNBOUND` | 2 | 2 | $1,480,000 | 2026-05-20 | HIGH |
| `APPROVALS-TO-UPGRADEABLE-SPENDER` | 2 | 2 | $1,232,000 | 2026-07-15 | MEDIUM |
| `SETTLEMENT-EPOCH-BOUNDARY-CREDIT` | 2 | 2 | $703,700 | 2026-08-02 | MEDIUM |
| `ACC-SPLIT-NONINVARIANT` | 2 | 2 | $678,000 | 2026-08-10 | MEDIUM |
| `UPGRADE-INITIALIZER-REACHABLE-LIVE` | 2 | 2 | $665,000 | 2026-05-12 | HIGH |
| `ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE` | 2 | 2 | $643,000 | 2026-07-01 | HIGH |
| `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | 2 | 2 | $630,000 | 2026-06-23 | HIGH |
| `METATX-SENDER-IDENTITY-CONFUSION` | 2 | 2 | $282,700 | 2026-05-13 | MEDIUM |
| `TOKEN-TRANSFER-INTENT-HEURISTIC-FORGEABLE` | 2 | 2 | $277,041 | 2026-06-05 | MEDIUM |
| `SIG-VERIFIER-DEFEATABLE` | 2 | 2 | $97,819 | 2026-06-25 | HIGH |
| `TOKEN-PACKED-OWNERSHIP-UNDERFLOW` | 2 | 1 | $40,000 | 2026-06-09 | HIGH |
| `ACC-DUPLICATE-ID-ACCUMULATION` | 2 | 2 | $13,021 | 2026-06-03 | MEDIUM |
| `AMM-POOL-RATIO-SKEW-EXTRACTION` *(single-event)* | 1 | 1 | $1,650,000 | 2026-07-19 | MEDIUM |
| `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` *(single-event)* | 1 | 1 | $907,700 | 2026-08-02 | MEDIUM |
| `ACC-CREDIT-NOT-RECEIVED` *(single-event)* | 1 | 1 | $560,000 | 2026-07-25 | MEDIUM |
| `INCENTIVE-PER-ADDRESS-NO-SYBIL-COST` *(single-event)* | 1 | 1 | $200,000 | 2026-05-25 | MEDIUM |
| `AUTH-ZERO-ADDRESS-ACCEPTED` *(single-event)* | 1 | 1 | $98,200 | 2026-05-28 | MEDIUM |
| `SIG-REPLAY-CROSS-POSITION` *(single-event)* | 1 | 1 | $29,984 | 2026-08-08 | MEDIUM |
| `STORAGE-LAYOUT-COLLISION-PHANTOM-CREDIT` *(single-event)* | 1 | 1 | $25,000 | 2026-06-01 | MEDIUM |
| `ACC-HARDCODED-PEG-REDEMPTION` *(single-event)* | 1 | 1 | $8,500 | 2026-07-13 | MEDIUM |


---

## `TOKEN-DEFERRED-BURN-LP-RESERVE-DESYNC`

**Token logic mutates an AMM pair's token balance out-of-band, then reserves are resynced**

- **Incidents:** 14 (unique root causes: 14) · **6-month loss:** $5,425,242 · **Most recent:** 2026-07-28 · **Evidence strength:** HIGH

### Broken invariant
An AMM pair's recorded reserves may change only through the pair's own swap/mint/burn accounting. A token contract must never move or destroy tokens already held by the pair, because any unpriced change to the pair's balance is realizable as profit by the next caller once reserves are resynchronised.

### Mechanism
The token implements fee-on-transfer, deflation, dividend or 'maintenance' logic that (a) accumulates a pending burn/fee amount in storage on sells, and (b) on a later, often unrelated, transfer burns or transfers that amount directly from the pair address and calls pair.sync() (or relies on the next skim/sync). The pair's reserve is rewritten to a value that no swap produced. An unprivileged caller sequences: accumulate pending amount -> buy out the pair inventory -> trigger the deferred burn -> sell back into the now-skewed curve.

### Mandatory preconditions (all must hold; any proven absent kills the hypothesis)
- Token contract contains logic that transfers or burns from, or mints to, the AMM pair address (not merely from msg.sender)
- That logic is reachable by an unprivileged caller (public function, or a hook on any transfer, including a zero-value transfer)
- The pair's reserves are re-synchronised after the out-of-band balance change (explicit pair.sync()/skim(), or a subsequent swap that reads stale reserves)
- A live AMM pair holds material quote-asset liquidity for the token

### Optional amplifiers (never the root cause)
- Flash-loan liquidity to buy out inventory
- Thin pair depth
- Multiple router paths
- Whitelisted router/pair bypassing transfer restrictions

### Applicable protocol archetypes
token with custom transfer logic, farm, reward distributor, launchpad token, DEX/AMM pair (as victim venue)

### Observable indicators

**Static (code)**
- _transfer/_update override referencing a stored pair/lpPair/uniswapV2Pair address
- state variables named toBurnAmount, pendingBurn, sellBurn, pendingBurnAmount, deferred*
- direct calls to IUniswapV2Pair.sync() or .skim() from the token or a helper
- _burn(pair, amount) / super._transfer(pair, dead, amount) / mintReward(pair, ...)
- balanceOf(pair) read inside transfer logic

**Adapter**
- DefiLlama adapter values a single token/LP pair via getReserves on a pair whose token has custom transfer logic
- adapter hardcodes one pair address as the protocol's whole TVL

**Runtime state**
- pair token balance != pair reserve for the custom token (balance/reserve drift)
- non-zero pending-burn storage slot
- historical Sync events not immediately preceded by Swap/Mint/Burn from the pair itself

**Cross-contract**
- token contract is not the pair, yet appears as `from` in Transfer events whose `from` is the pair address

### Decisive guards (presence normally kills the hypothesis)
- Token never writes to the pair's balance: burns/fees are taken from msg.sender's amount only
- Pair address is excluded from all fee/burn/dividend logic (isExcluded[pair] == true) for balance-mutating paths
- No public path invokes pair.sync()/skim() after a protocol-initiated balance change
- Post-transfer assertion that balanceOf(pair) >= reserve for that token

### False-positive killers
- Token is a plain OpenZeppelin ERC-20 with no _update/_transfer override (kills the hypothesis)
- Fee logic only reduces the amount credited to `to`, never touches third-party balances
- All burn targets are msg.sender or address(this), never a pair

### Local defensive property (fork-only test)
For every reachable public call sequence, balanceOf(pair, token) must never decrease except through the pair's own burn()/swap() accounting; assert reserve-vs-balance parity before and after each token operation in a fork test.

### Recommended audit questions
- Does any code path let a caller change the pair's balance of this token without going through the pair?
- Is sync()/skim() reachable in the same transaction as such a change?
- Can a zero-value or dust transfer trigger the deferred branch?
- What is the maximum reserve skew achievable in one transaction, and what does it cost?

### Incidents
- `INC-2026-07-28-LUL` — 2026-07-28 — **LULA** — $578,100
- `INC-2026-06-20-LAB` — 2026-06-20 — **LABUBU/OLPC** — $1,100,000
- `INC-2026-06-19-JBX` — 2026-06-19 — **JB** — $50,000
- `INC-2026-06-17-LIT` — 2026-06-17 — **Little Boy Plus** — $367,000
- `INC-2026-06-04-BYT` — 2026-06-04 — **BYToken** — $87,402
- `INC-2026-05-26-SKP` — 2026-05-26 — **SKP** — $212,850
- `INC-2026-04-28-JUD` — 2026-04-28 — **JUDAO** — $228,000
- `INC-2026-04-13-MON` — 2026-04-13 — **MONA** — $60,950
- `INC-2026-04-07-TGA` — 2026-04-07 — **TGAI** — $11,940
- `INC-2026-04-04-BSC` — 2026-04-04 — **BSC TMM/USDT** — $1,665,000
- `INC-2026-04-02-SAS` — 2026-04-02 — **SAS Token** — $12,000
- `INC-2026-03-23-BCE` — 2026-03-23 — **BCE-USDT liquidity pool** — $679,000
- `INC-2026-03-12-AMU` — 2026-03-12 — **AM/USDT pool** — $131,000
- `INC-2026-03-10-MTW` — 2026-03-10 — **MT-WBNB liquidity pool** — $242,000

**Provisional (grade C, not counted in statistics or ranking weight):**
- `INC-2026-05-29-YSD` — 2026-05-29 — YSDAO

### Propagation
Template-propagated rather than fork-propagated: independent BSC token deployments repeatedly reimplement the same deferred-burn pattern. Independent code lineages are counted separately; the Computility-associated pair (TGAI/YSDAO) is one lineage. DARKNAVY documents additional 2026 instances (STO, Movie Token) confirming the template. Expect continued recurrence on any chain with cheap deployment and copy-pasted deflationary token templates.

> **Not screenable as a protocol-family pair in the DefiLlama universe.** Victims are individually deployed BSC/Base tokens with custom transfer logic that are not listed as DefiLlama protocols; the family has no addressable protocol population in this universe. Handed to the token-level monitoring workstream instead.

---

## `BRIDGE-MESSAGE-NOT-BOUND-TO-SOURCE`

**Cross-domain payout or mint is not bound to a proven, value-matched, single-use source event**

- **Incidents:** 7 (unique root causes: 6) · **6-month loss:** $26,666,000 · **Most recent:** 2026-08-09 · **Evidence strength:** HIGH

### Broken invariant
A release, mint or payout on the destination domain must be authorised only by a proof that binds, simultaneously: the source chain identity, the source channel/route, the exact asset, the exact amount, the recipient, and a nonce that is consumed exactly once. Verifying that a message is well-formed or correctly signed is not the same as verifying that it corresponds to a real deposit of equal value.

### Mechanism
The destination-side contract validates some fields but omits at least one binding. Observed omissions: value equality between source commitment and destination payout (Verus checkCCEValues); source channel / denomination path (Secret CW20-ICS20, deleted checks); economic reality of the deposit, so the bridge's own wrapped token self-transferred with a valid memo counts as a deposit (Coreum); the event that relayers key on can be spoofed by an unrelated program (Across on Solana); authority granted by a forged message (Hyperbridge); external-chain block/state data injected through a peripheral updater (Stake DAO Votemarket).

### Mandatory preconditions (all must hold; any proven absent kills the hypothesis)
- A destination-side contract mints, releases or grants authority in response to a message asserting a source-domain event
- That path is reachable by, or on behalf of, an unprivileged party (permissionless relay, or a relayer whose input is attacker-shapeable)
- At least one of {source chain id, channel/route, asset, amount, recipient, nonce-consumption} is not enforced against the proof
- The destination side holds redeemable reserves, or the minted asset is redeemable through a legitimate route

### Optional amplifiers (never the root cause)
- Attacker can stand up their own source chain / IBC channel cheaply
- Privacy-by-default chain delays detection
- Redeposits after a known-unfixed flaw refill the reserve

### Applicable protocol archetypes
bridge, canonical bridge, cross-chain messaging, IBC/CosmWasm bridge contract, intents/solver relayer, liquid staking with cross-chain mint, OFT/omnichain token

### Observable indicators

**Static (code)**
- mint/release keyed on a message struct without an amount-equality assertion against the source commitment
- commented-out or removed channel/denom validation
- processedNonces / usedHashes mapping absent, or written after external calls
- message hash built with abi.encodePacked over dynamic fields
- trusted-remote / peer mapping settable without timelock

**Adapter**
- adapter counts destination-side wrapped supply as TVL
- adapter treats escrow balance and wrapped supply as independent
- bridge adapter enumerates vaults but not the mint authority

**Runtime state**
- wrapped supply on destination > escrowed backing on source
- peers/trusted remotes pointing at addresses with no deployed code or recent changes
- relayer/prover set with a single member, or a single DVN
- reserve refilled after a publicly known unfixed flaw

**Cross-contract**
- escrow contract on source vs mint authority on destination not reconcilable from public data
- light client / prover registry mutable by a non-timelocked role

### Decisive guards (presence normally kills the hypothesis)
- Destination asserts payout amount == amount committed on source, in the same proof
- Proof binds source chain id AND channel/port AND denomination path
- Nonce/message hash marked consumed before any external call, and replay reverts
- Deposit validity requires an external asset actually escrowed, so the bridge's own wrapped token cannot be a deposit
- Independent verification set (>1 DVN/prover) with no single failover

### False-positive killers
- Destination mint requires a Merkle/zk proof against a source state root that itself commits to the amount
- Reserve reconciliation is enforced on-chain (mint reverts if supply would exceed escrow)
- Bridge is one-way with no destination-side release

### Local defensive property (fork-only test)
On a pinned fork of the destination chain, no sequence of destination-side calls may increase redeemable value without a matching, previously unconsumed source commitment of equal value.

### Recommended audit questions
- Is every mandatory precondition present in the live deployment?
- Is any decisive guard present in the deployed bytecode, not just the repository?
- What live value, authority or approval is reachable through this path?
- What single observation would falsify the hypothesis?

### Incidents
- `INC-2026-08-09-COR` — 2026-08-09 — **Coreum Bridge** — $200,000
- `INC-2026-07-23-VER` — 2026-07-23 — **Verus Ethereum Bridge** — $7,540,000
- `INC-2026-07-17-ACR` — 2026-07-17 — **Across** — not disclosed
- `INC-2026-06-10-SEC` — 2026-06-10 — **Secret Network** — $4,670,000
- `INC-2026-05-18-VER` — 2026-05-18 — **Verus-Ethereum Bridge** — $11,580,000
- `INC-2026-04-13-HYP` — 2026-04-13 — **Hyperbridge** — $2,500,000
- `INC-2026-03-12-STA` — 2026-03-12 — **Stake DAO** — $176,000

**Provisional (grade C, not counted in statistics or ranking weight):**
- `INC-2026-08-09-ORA` — 2026-08-09 — Oraichain
- `INC-2026-06-19-NAM` — 2026-06-19 — Namada Shielded Pools
- `INC-2026-06-08-SYS` — 2026-06-08 — Syscoin Bridge
- `INC-2026-05-15-ADS` — 2026-05-15 — Adshares Bridge

### Propagation
Verus is a repeat of one unremediated root cause (May and July 2026 are the same defect, not two mechanisms) and counts once toward unique root causes. Secret Network's defect existed in the repo from its first commit in 2023 and ran live for three years, which is the general shape: bridge validation gaps are long-lived and only surface when reserves grow.

---

## `ORACLE-SPOT-THIN-LIQUIDITY`

**Capacity or reward sized from a price movable inside the attacker's own transaction on a venue thinner than the capacity it unlocks**

- **Incidents:** 7 (unique root causes: 7) · **6-month loss:** $21,658,540 · **Most recent:** 2026-08-15 · **Evidence strength:** HIGH

### Broken invariant
Borrowing capacity, mint size, reward size or collateral value must not be derived from a price that a single actor can move within the manipulation window, and the value unlocked must never exceed the cost of moving that price.

### Mechanism
The protocol reads a spot price or reserve ratio (AMM getReserves, a single-DEX quote, or an external oracle that itself tracks a thin venue) and immediately sizes a value-bearing action from it. The attacker funds a large swap (often flash-borrowed), moves the price on the thin venue, takes the oversized action, and unwinds in the same transaction or shortly after. Flash liquidity is an amplifier that supplies temporary capital; the root cause is the unbounded, unaveraged, un-deviation-checked price input.

### Mandatory preconditions (all must hold; any proven absent kills the hypothesis)
- A value-bearing action is sized from a price or reserve reading
- That reading is derived from a venue an unprivileged actor can move (directly, or via an oracle that tracks it)
- No TWAP, no deviation bound, and no liquidity/notional cap gates the action
- The value unlocked by the moved price exceeds the cost of moving it

### Optional amplifiers (never the root cause)
- Flash loans
- Same-block entry and exit
- Low-float or newly listed collateral
- Referral/multiplier logic on top of the sized value

### Applicable protocol archetypes
lending, CDP, staking pool, reward distributor, bonding, yield, liquidity manager, stablecoin issuer

### Observable indicators

**Static (code)**
- getReserves()/slot0()/getAmountsOut() feeding a mint, borrow, stake or reward computation
- quote taken once and reused after a state-changing swap in the same function
- reward = f(price) with price read from a pair the protocol also trades against
- no OBSERVATION/TWAP window parameter anywhere in the pricing path

**Adapter**
- adapter prices the protocol's own token from a single pair
- protocol TVL concentrated in one thin pair
- adapter lists collateral assets with no major-venue liquidity

**Runtime state**
- collateral/listed asset whose deepest venue depth is small relative to the borrow capacity it unlocks
- borrow caps absent or far above venue depth
- reward contract holding a reserve larger than the cost to move the reference pair

**Cross-contract**
- the pricing pair and the protocol's own reserve are the same pool
- oracle contract reads a DEX the protocol itself seeds

### Decisive guards (presence normally kills the hypothesis)
- TWAP over a window long enough that manipulation cost exceeds the value unlocked
- Hard deviation bound against an independent deep-market source, reverting on breach
- Per-asset borrow/mint caps set below the manipulation cost on the deepest available venue
- Value sized from the amount actually transferred in, not from a quoted price

### False-positive killers
- All collateral priced by a deep aggregated feed with a deviation cap (kills the pair)
- Caps are set from measured venue depth and enforced on-chain
- The action is sized from realised transfer amounts, so price is never an input

### Local defensive property (fork-only test)
On a fork, execute a max-size flash-funded swap against every venue in the pricing path and assert that no value-bearing entrypoint changes its output beyond the configured deviation bound.

### Recommended audit questions
- Is every mandatory precondition present in the live deployment?
- Is any decisive guard present in the deployed bytecode, not just the repository?
- What live value, authority or approval is reachable through this path?
- What single observation would falsify the hypothesis?

### Incidents
- `INC-2026-08-15-FOX` — 2026-08-15 — **FoxMarket** — $118,700
- `INC-2026-08-02-LOO` — 2026-08-02 — **LOOPSDAO** — $690,000
- `INC-2026-07-11-BON` — 2026-07-11 — **Bonzo Lend** — $9,050,000
- `INC-2026-03-31-LML` — 2026-03-31 — **LML/USDT staking protocol** — $950,000
- `INC-2026-03-26-UNK` — 2026-03-26 — **Unknown Stake Contract** — $133,000
- `INC-2026-03-22-CYR` — 2026-03-22 — **Cyrus Finance** — $516,840
- `INC-2026-02-22-BLE` — 2026-02-22 — **Blend Pools V2** — $10,200,000

### Propagation
The distinguishing screening question is not 'does it use an oracle' but 'is the deepest venue behind that price thinner than the capacity it unlocks'. Blend/YieldBlox is the clearest case: unmodified core contracts, a curator-listed asset (USTRY) with an SDEX market thin enough to move ~100x in one trade.

---

## `UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY`

**A deprecated or superseded deployment retains funds, approvals or authority**

- **Incidents:** 7 (unique root causes: 7) · **6-month loss:** $6,971,179 · **Most recent:** 2026-06-17 · **Evidence strength:** HIGH

### Broken invariant
Deprecation must remove capability, not just remove the user interface. A contract that is no longer maintained must not still hold value, still hold user approvals, or still be able to mint, release or authorise anything.

### Mechanism
The team ships a v2/new deployment and stops maintaining the old one, but the old contract is immutable or unpaused and still holds residual liquidity, still has live ERC-20/ERC-721 approvals from users, or still holds a role in a live system. Attackers find the old contract long after attention moved on. Sub-shapes seen: immutable escape hatch with no ownership check (Aztec Bridge); incomplete proof verification in a deprecated router (Aztec Connect); LP-mint validation gap in a retired AMM program (Raydium V3); leftover rewards pool with an uninitialised accumulator (Scallop V2 rewards); old deposit path still callable alongside the new one (Haedal); legacy vault with different redemption math (Thetanuts); legacy pools still holding fees (Huma V1).

### Mandatory preconditions (all must hold; any proven absent kills the hypothesis)
- A prior-version deployment is still callable on a live chain
- It still holds value, live approvals, or an authority role
- Its code path differs from the maintained version (or is unmaintained/immutable)
- No pause/guardian can stop it, or the pause was never applied

### Optional amplifiers (never the root cause)
- Immutable contract with no owner
- Front end removed so nobody watches it
- Audit scope covered only the current version
- Value drifts back in via residual LP or fees

### Applicable protocol archetypes
any protocol with more than one deployed version, bridge, DEX/AMM, vault/share token, lending, reward distributor, rollup

### Observable indicators

**Static (code)**
- multiple deployment generations in docs/repo with only the newest audited
- immutable contracts with escape-hatch functions
- initializer/version counters that differ between deployments

**Adapter**
- DefiLlama adapter still lists v1/legacy addresses alongside v2
- adapter has a commented-out or removed legacy section while the addresses remain funded on-chain
- adapter module path contains v1/v2/legacy/deprecated/old

**Runtime state**
- legacy contract holds non-trivial token balances
- non-zero allowances from live EOAs to the legacy contract
- legacy contract holds a role (MINTER/BRIDGE/DISTRIBUTOR) in a current contract
- no Paused event; functions still succeed in eth_call simulation

**Cross-contract**
- legacy address appears in a current registry/whitelist
- legacy proxy admin still owned by a live multisig

### Decisive guards (presence normally kills the hypothesis)
- Legacy deployment is paused AND drained AND has no live role
- Approvals to legacy contracts revoked or rendered inert by a token-side blocklist
- Legacy contract self-destructed or upgraded to a no-op implementation

### False-positive killers
- Legacy address holds zero balance, zero allowances and zero roles (kills exposure even if code is flawed)
- Contract reverts on every state-changing entrypoint (verified paused)

### Local defensive property (fork-only test)
For each historical deployment generation, prove on a pinned fork that every state-changing entrypoint either reverts or cannot move value/authority.

### Recommended audit questions
- Is every mandatory precondition present in the live deployment?
- Is any decisive guard present in the deployed bytecode, not just the repository?
- What live value, authority or approval is reachable through this path?
- What single observation would falsify the hypothesis?

### Incidents
- `INC-2026-06-17-AZT` — 2026-06-17 — **Aztec Bridge** — $2,160,000
- `INC-2026-06-15-THE` — 2026-06-15 — **Thetanuts Finance** — $105,000
- `INC-2026-06-14-AZT` — 2026-06-14 — **Aztec Connect** — $2,100,000
- `INC-2026-06-10-RAY` — 2026-06-10 — **Raydium** — $1,340,000
- `INC-2026-06-09-HAE` — 2026-06-09 — **Haedal Vault** — $915,179
- `INC-2026-05-10-REN` — 2026-05-10 — **Renegade** — $209,000
- `INC-2026-04-26-SCA` — 2026-04-26 — **Scallop** — $142,000

**Provisional (grade C, not counted in statistics or ranking weight):**
- `INC-2026-05-13-TRA` — 2026-05-13 — Transit Finance
- `INC-2026-05-11-HUM` — 2026-05-11 — Huma Finance

### Propagation
Nine in-window incidents across five chains and every archetype. This is the highest-yield family for a discovery pass because the prerequisites are directly observable from public data (adapter history, balances, allowances, role reads) without reading any application logic.

---

## `PROOF-VERIFICATION-BYPASSED`

**A zk, rollup or attestation proof is not required, incompletely verified, or checked against a misconfigured key**

- **Incidents:** 6 (unique root causes: 6) · **6-month loss:** $7,372,966 · **Most recent:** 2026-07-02 · **Evidence strength:** HIGH

### Broken invariant
A withdrawal or mint gated by a proof must verify that proof against the correct verifying key, over all the public inputs that bind the action, and must reject when any component is absent.

### Mechanism
Observed shapes: a deposit path that accepts entries with no proof at all (Hinkal 'proofless deposit'); minting on forged proofs because proof validity was never enforced (Quicksilver unchecked proof minting); a verifying key misconfigured so forged zkSNARK proofs verify (FOOMCASH); an auxiliary withdrawal script whose key-reset defence could be bypassed while the core circuit stayed sound (HermesVault); incomplete verification logic in a deprecated rollup router (Aztec Connect) and an immutable escape hatch accepting fake rollup proofs with no ownership check (Aztec Bridge).

### Mandatory preconditions (all must hold; any proven absent kills the hypothesis)
- A value-releasing path is gated by a proof or attestation
- Verification omits a component, uses a wrong/settable key, or the path is reachable without a proof
- The releasing contract holds redeemable value
- Reachable by an unprivileged caller

### Optional amplifiers (never the root cause)
- Deprecated/immutable deployment nobody monitors
- Privacy design hiding the anomaly
- Auxiliary scripts outside the audited circuit

### Applicable protocol archetypes
privacy pool, rollup/canonical bridge, liquid staking with proof-based mint, cross-chain messaging, gaming with zk claims

### Observable indicators

**Static (code)**
- verifier address or verifying key settable post-deployment
- public inputs array shorter than the action's binding fields
- escape-hatch/emergency withdraw paths with weaker checks
- verification result assigned but not required

**Adapter**
- adapter counts a shielded pool balance it cannot decompose
- adapter references a verifier or rollup processor address

**Runtime state**
- verifying key hash not matching the published circuit artifact
- verifier address recently changed or owned by an EOA
- escape-hatch functions still callable on a deprecated deployment

**Cross-contract**
- prover/attestation registry mutable by a non-timelocked role
- multiple verifier generations live simultaneously

### Decisive guards (presence normally kills the hypothesis)
- Verifying key immutable and hash-matched to a published artifact
- All action-binding fields present in public inputs
- Every release path requires proof verification with no bypass branch
- Nullifier consumed before release

### False-positive killers
- Verifying key immutable and attested (kills the misconfiguration shape)
- No alternative release path exists (enumerate selectors)

### Local defensive property (fork-only test)
On a fork, submit an empty proof, a proof for different public inputs, and a proof under a foreign key; every release path must revert.

### Recommended audit questions
- Is every mandatory precondition present in the live deployment?
- Is any decisive guard present in the deployed bytecode, not just the repository?
- What live value, authority or approval is reachable through this path?
- What single observation would falsify the hypothesis?

### Incidents
- `INC-2026-07-02-HIN` — 2026-07-02 — **Hinkal** — $820,000
- `INC-2026-06-21-QUI` — 2026-06-21 — **Quicksilver Zone** — $3,500
- `INC-2026-06-17-AZT` — 2026-06-17 — **Aztec Bridge** — $2,160,000
- `INC-2026-06-14-AZT` — 2026-06-14 — **Aztec Connect** — $2,100,000
- `INC-2026-05-19-HER` — 2026-05-19 — **HermesVault** — $29,466
- `INC-2026-02-26-FOO` — 2026-02-26 — **FOOMCASH** — $2,260,000

**Provisional (grade C, not counted in statistics or ranking weight):**
- `INC-2026-06-21-TAI` — 2026-06-21 — Taiko Bridge

### Propagation
Two of the seven were deprecated Aztec deployments, which is why this family overlaps heavily with UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY: proof systems are hardest to fix once immutable.

---

## `ORACLE-STALE-OR-SILENT-FALLBACK`

**Price feed identity, freshness or failure mode is wrong, and the failure is silent**

- **Incidents:** 5 (unique root causes: 5) · **6-month loss:** $2,688,400 · **Most recent:** 2026-07-23 · **Evidence strength:** HIGH

### Broken invariant
A valuation used to size borrowing, minting, redemption or liquidation must come from a feed proven to describe that exact asset, be within a bounded age, and fail closed. A feed that returns a wrong asset's price, a stale price, a capped price, or zero must revert rather than be used.

### Mechanism
Configuration or fallback logic yields a price that does not describe the asset at its current economic value, and nothing reverts. Observed shapes: wrong feed assigned to an asset (Ploutos used BTC/USD for USDC; Solido fell back to the CASH oracle for SOLID); an invalid pool parameter makes the lookup return address(0) and the oracle returns zero instead of reverting (Singularity, Uniswap V3 fee tier 42 -> getPool()==0 -> totalAssets counted only idle USDC); a capped-price adapter mis-parameterised so the reported price is materially below true value (Aave V3 CAPO/wstETH, ~2.85% low, causing wrongful liquidations); a stored price with a long refresh cooldown used to size rewards while realisation happens at live price (LML, 3600s).

### Mandatory preconditions (all must hold; any proven absent kills the hypothesis)
- A value-bearing decision (borrow, mint, redeem, liquidate, reward-size) reads a configured feed
- Feed selection, fallback or cap is settable by configuration rather than fixed to the asset
- The failure/edge path returns a usable number instead of reverting (zero, stale, capped, or another asset's price)
- Live positions or reserves are exposed to that decision

### Optional amplifiers (never the root cause)
- Flash liquidity to enter and exit inside one block
- Long undetected misconfiguration window
- Asset with few independent feeds
- Newly listed asset

### Applicable protocol archetypes
lending, CDP, stablecoin issuer, vault/share token, risk curator, derivatives, yield

### Observable indicators

**Static (code)**
- latestRoundData() used without checking updatedAt/answeredInRound or answer > 0
- try/catch around a feed with a non-reverting fallback
- factory.getPool(...)/getFeed(...) result used without a zero-address check
- per-asset oracle mapping settable by an EOA or non-timelocked role
- price cap / growth-rate adapters with governance-set parameters

**Adapter**
- DefiLlama `oracles` field lists a single oracle
- adapter prices assets by hardcoded peg or by a pool read rather than the protocol's own oracle
- adapter's token list includes assets with no deep independent market

**Runtime state**
- oracle mapping entries pointing at address(0) or at a feed whose description() names a different asset
- feed updatedAt older than the protocol's own heartbeat
- configured pool/fee-tier parameters that do not resolve to a deployed pool
- reported asset price materially divergent from independent venues

**Cross-contract**
- oracle admin != protocol timelock
- the same feed reused across assets in the mapping

### Decisive guards (presence normally kills the hypothesis)
- Staleness check on updatedAt with a bound tighter than the feed heartbeat, reverting on breach
- answer > 0 and zero-address checks that revert
- Feed-to-asset binding asserted on registration (description/decimals/base-quote validated)
- Deviation bound against an independent second source
- Sequencer-uptime check on L2s

### False-positive killers
- Oracle registration is timelocked AND the adapter asserts the feed's base/quote on set (kills the misassignment shape)
- Every feed read reverts on zero/stale (kills the silent-fallback shape)
- Asset valuations cross-checked against a second independent oracle with a hard deviation cap

### Local defensive property (fork-only test)
On a fork, force each configured feed to return zero, a stale timestamp, and a 10x/0.1x value; every value-bearing entrypoint must revert rather than transact.

### Recommended audit questions
- Is every mandatory precondition present in the live deployment?
- Is any decisive guard present in the deployed bytecode, not just the repository?
- What live value, authority or approval is reachable through this path?
- What single observation would falsify the hypothesis?

### Incidents
- `INC-2026-07-23-SOL` — 2026-07-23 — **Solido Cash** — $73,400
- `INC-2026-04-27-SIN` — 2026-04-27 — **Singularity Finance** — $413,000
- `INC-2026-03-31-LML` — 2026-03-31 — **LML/USDT staking protocol** — $950,000
- `INC-2026-03-12-AAV` — 2026-03-12 — **Aave V3** — $862,000
- `INC-2026-02-26-PLO` — 2026-02-26 — **Ploutos Money** — $390,000

**Provisional (grade C, not counted in statistics or ranking weight):**
- `INC-2026-07-15-OST` — 2026-07-15 — Ostium
- `INC-2026-04-03-SIL` — 2026-04-03 — Silo V2
- `INC-2026-03-28-GOO` — 2026-03-28 — GoonFi

### Propagation
The dominant lending-side family of the window and the one most often caused by curation rather than code: Blend/YieldBlox and Aave CAPO were both operator/curator parameter failures on unmodified core contracts. That makes DefiLlama's Risk Curators and Lending categories the highest-yield screening surface.

---

## `GOV-CHEAP-CONTROL-NO-TIMELOCK`

**Voting power is cheaply acquirable and executes without a delay long enough to respond**

- **Incidents:** 4 (unique root causes: 4) · **6-month loss:** $22,356,000 · **Most recent:** 2026-07-15 · **Evidence strength:** HIGH

### Broken invariant
The cost of acquiring decisive voting power must exceed the value governance controls, and execution must be separated from passage by a delay long enough for holders to exit or a guardian to veto.

### Mechanism
Low float, low quorum, or a small total supply lets an attacker buy control on the open market (or borrow it) and pass a proposal that mints, upgrades or transfers. With no timelock, passage and execution occur before anyone can react. Token of Power: >50% of a 16,384-token supply acquired with Tornado-funded capital, minted billions and drained 944 WETH from a Balancer V1 pool in a single transaction. BonkDAO: ~$4M of BONK bought to pass BIP-76 and move ~$20M of treasury. BarnBridge: DAO control used to upgrade a proxy to a malicious implementation and drain ~$776K through pre-existing approvals from ~50 addresses. Moonwell/Moonriver: ~$1,800 bought 40M MFAM and passed an initial vote in 11 minutes targeting seven markets, the comptroller and the oracle.

### Mandatory preconditions (all must hold; any proven absent kills the hypothesis)
- On-chain governance can move value, mint, or upgrade
- Decisive voting power is acquirable at a cost below the controlled value
- No timelock, or a timelock shorter than a realistic response window
- Reachable without stolen credentials

### Optional amplifiers (never the root cause)
- Governance token borrowable or flash-loanable
- Snapshot at proposal time rather than a historical block
- Proxy upgrade in scope of governance
- Live user approvals to governance-upgradeable contracts

### Applicable protocol archetypes
governance-controlled proxy, DAO treasury, lending with governance-set parameters, token with on-chain governance

### Observable indicators

**Static (code)**
- Governor with quorum as a small fraction of supply
- no TimelockController between passage and execution
- proposal threshold denominated in tokens rather than value
- upgrade/mint in the executor's capability set

**Adapter**
- adapter lists a treasury address controlled by governance
- governance-owned proxy admin appears in the adapter's address set

**Runtime state**
- market cost to reach quorum far below treasury + controlled TVL
- timelock delay zero or minimal
- recent proposals passing with tiny participation
- live approvals to governance-upgradeable spenders

**Cross-contract**
- governance executor holds MINTER or PROXY_ADMIN on funded contracts
- the same executor controls the oracle

### Decisive guards (presence normally kills the hypothesis)
- Timelock long enough for exit, with a guardian veto
- Quorum and threshold scaled to controlled value, not token count
- Voting power snapshot at a historical block, defeating same-block acquisition
- Upgrade and mint removed from governance's reach or separately gated

### False-positive killers
- Timelock plus an active guardian with veto (kills execution speed)
- Cost to acquire quorum exceeds controlled value by a wide margin
- Governance cannot upgrade or mint

### Local defensive property (fork-only test)
Compute, from live market depth, the capital required to reach quorum, and compare it with treasury plus TVL plus the value reachable through approvals; the ratio is the finding.

### Recommended audit questions
- Is every mandatory precondition present in the live deployment?
- Is any decisive guard present in the deployed bytecode, not just the repository?
- What live value, authority or approval is reachable through this path?
- What single observation would falsify the hypothesis?

### Incidents
- `INC-2026-07-15-BAR` — 2026-07-15 — **BarnBridge** — $776,000
- `INC-2026-07-06-BON` — 2026-07-06 — **BonkDAO** — $20,000,000
- `INC-2026-06-09-TOK` — 2026-06-09 — **Token of Power** — $1,580,000
- `INC-2026-03-24-MOO` — 2026-03-24 — **Moonwell** — not disclosed

### Propagation
Ranking must use value controlled through approvals and roles, not just treasury size: BarnBridge's treasury was not the target, users' pre-existing approvals were.

---

## `ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED`

**A caller-supplied token, pool, mint or market is accepted without registry validation**

- **Incidents:** 4 (unique root causes: 4) · **6-month loss:** $19,864,350 · **Most recent:** 2026-06-10 · **Evidence strength:** HIGH

### Broken invariant
Every asset, pool or market a value-bearing operation touches must be resolved from a protocol-controlled registry. An identifier supplied by the caller is a request, not a fact.

### Mechanism
Raydium's deprecated AMM V3 program insufficiently validated LP mint addresses, so a fake LP token bypassed proportion checks and drained ~$1.34M from five inactive pools. Juicebox V3's REVLoans borrowFrom accepted a caller-supplied REVLoanSource struct (.terminal, .token), forging the accounting context so the oracle was skipped and attacker-controlled decimals/balances set the share price. Rhea Finance's attacker pre-created fake token pools on Ref Finance to construct a malicious swap route for its margin engine.

### Mandatory preconditions (all must hold; any proven absent kills the hypothesis)
- A value-bearing function accepts a token, pool, market or mint identifier from the caller
- No check that the identifier is registered/derived by the protocol
- The identifier determines pricing, proportion or destination
- Protocol-held value is reachable through it

### Optional amplifiers (never the root cause)
- Permissionless pool creation on the venue
- Deprecated program with weaker validation
- Multi-hop routing across arbitrary pools

### Applicable protocol archetypes
DEX/AMM, DEX aggregator/router, lending with leverage, token launch platform, cross-chain aggregator

### Observable indicators

**Static (code)**
- pool/mint/terminal addresses taken as parameters without a registry lookup
- PDA/seed derivation not asserted (Solana)
- struct parameters carrying accounting context
- no allowlist of routable venues

**Adapter**
- adapter enumerates pools from a factory but the protocol accepts arbitrary pools
- adapter routes through third-party venues

**Runtime state**
- registry/whitelist empty or permissive
- recently created pools reachable by the router
- deprecated programs still callable

**Cross-contract**
- routing venue permits permissionless pool creation while the consumer trusts any pool

### Decisive guards (presence normally kills the hypothesis)
- Registry/factory-derivation check on every identifier (assert factory.getPool(a,b,fee) == suppliedPool, or PDA derivation)
- Allowlist of routable venues and assets
- Per-hop economic validation, not just endpoint validation

### False-positive killers
- Every identifier derived or verified against the factory/registry (kills the pair)
- Routing restricted to an immutable venue allowlist

### Local defensive property (fork-only test)
On a fork, create a fake pool/mint and pass it to every identifier-accepting entrypoint; all must revert.

### Recommended audit questions
- Is every mandatory precondition present in the live deployment?
- Is any decisive guard present in the deployed bytecode, not just the repository?
- What live value, authority or approval is reachable through this path?
- What single observation would falsify the hypothesis?

### Incidents
- `INC-2026-06-10-RAY` — 2026-06-10 — **Raydium** — $1,340,000
- `INC-2026-04-22-KIP` — 2026-04-22 — **Kipseli** — $72,350
- `INC-2026-04-20-JUI` — 2026-04-20 — **Juicebox V3** — $52,000
- `INC-2026-04-16-RHE` — 2026-04-16 — **Rhea Finance** — $18,400,000

### Propagation
The general prerequisite is composability with permissionless venues: any protocol that routes through, or prices from, a venue where anyone can create a market inherits it.

---

## `CALLDATA-CALLER-CONTROLLED-TARGET`

**A public entrypoint executes caller-specified target and calldata while the contract holds authority or approvals**

- **Incidents:** 4 (unique root causes: 4) · **6-month loss:** $3,798,750 · **Most recent:** 2026-08-06 · **Evidence strength:** HIGH

### Broken invariant
A contract that holds allowances, credit delegation or roles must never execute a call whose target and calldata the caller chooses. Its authority may only be spent on calls the contract itself constructs from validated inputs.

### Mechanism
A multicall, router, executor, adapter or 'helper' exposes run(Call[] calls) / execute(target,data) / an unnamed selector taking (address,bytes) and performs target.call(data) or delegatecall. Because the contract is the msg.sender for that inner call, everything it is trusted for is spendable: victims' ERC-20 allowances via transferFrom, ERC-721 setApprovalForAll, Aave credit delegation borrow(), or an arbitrary approval grant. Squid Multicall drained users who approved the multicall instead of the router; a custom sAVAX Aave rebalancer let any caller borrow against the victim's delegated credit; Unistreets' factory custodied launched LP NFTs and accepted injected setApprovalForAll calldata; the third-party SquidRouterModule combined this with a constant-string 'secret' as its only authentication.

### Mandatory preconditions (all must hold; any proven absent kills the hypothesis)
- Public/permissionless function accepting a call target and calldata (or an array of them)
- The executing contract holds spendable authority: live ERC-20/721 allowances, credit delegation, a role, or custody
- No allowlist restricting target/selector, and no binding of the moved value to msg.sender
- Reachable without privileged status

### Optional amplifiers (never the root cause)
- Contract name resembling a well-known safe contract, attracting misdirected approvals
- Long-lived unlimited approvals
- Module installed into user smart accounts

### Applicable protocol archetypes
DEX aggregator/router, bridge, smart account module, account abstraction, token launch platform, leveraged staking helper, MEV/keeper contract

### Observable indicators

**Static (code)**
- function run/execute/multicall/aggregate taking (address,bytes) or Call[]
- low-level .call(data) or delegatecall with unvalidated target
- no allowlist mapping for targets or selectors
- authentication by comparing to a constant string/hash present in the deployed bytecode

**Adapter**
- adapter references a Multicall/Executor/Router address distinct from the main router
- adapter enumerates helper contracts users may approve

**Runtime state**
- non-zero ERC-20 allowances or setApprovalForAll from live EOAs to the executor
- credit delegation (DELEGATION_WITH_SIG / approveDelegation) granted to the contract
- contract holds custody of NFTs/LP positions it did not create per-user

**Cross-contract**
- executor address appears in a lending market's delegation registry
- executor installed as a Safe module or 7702 delegate

### Decisive guards (presence normally kills the hypothesis)
- Target/selector allowlist enforced on every call
- Value moved only from msg.sender (payer bound to caller)
- Contract holds no persistent approvals; allowances are per-flow and revoked at the end
- Executor cannot be the approval target by construction (separate, non-approvable contract)

### False-positive killers
- Every target is checked against an immutable allowlist (kills the pair)
- Contract holds zero live allowances and no delegation (kills exposure)
- transferFrom is always from msg.sender

### Local defensive property (fork-only test)
On a fork, with a victim account holding a live approval to the contract, prove no permissionless entrypoint can move the victim's tokens.

### Recommended audit questions
- Is every mandatory precondition present in the live deployment?
- Is any decisive guard present in the deployed bytecode, not just the repository?
- What live value, authority or approval is reachable through this path?
- What single observation would falsify the hypothesis?

### Incidents
- `INC-2026-08-06-UNI` — 2026-08-06 — **Unistreets** — $17,750
- `INC-2026-05-25-THI` — 2026-05-25 — **Third-party Gnosis Safe Module (SquidRouterModule)** — $3,200,000
- `INC-2026-04-19-CUS` — 2026-04-19 — **Custom sAVAX Aave Rebalancer contract** — $64,000
- `INC-2026-04-07-SQU` — 2026-04-07 — **Squid Multicall** — $517,000

**Provisional (grade C, not counted in statistics or ranking weight):**
- `INC-2026-06-20-MEV` — 2026-06-20 — MEV Bot
- `INC-2026-05-07-TRU` — 2026-05-07 — TrustedVolumes
- `INC-2026-04-27-ZET` — 2026-04-27 — ZetaChain GatewayEVM

### Propagation
Exposure here is measurable without reading any logic: enumerate live allowances and delegations to each helper address. Approval-bearing helper contracts, not TVL, are the value at risk, so this family routinely applies to protocols whose DefiLlama TVL is small.

---

## `LIQUIDATION-ON-MANIPULABLE-VALUATION`

**Liquidation or mark price is movable by the party who profits from the liquidation**

- **Incidents:** 4 (unique root causes: 4) · **6-month loss:** $3,360,921 · **Most recent:** 2026-07-22 · **Evidence strength:** HIGH

### Broken invariant
A position may be liquidated only on a valuation that the liquidator cannot move, and the discount captured must not exceed the cost of moving the price.

### Mechanism
The health/mark computation reads a price the liquidator can move in the same transaction (thin AMM, mark price on a shallow market, or a share rate inflatable by donation). The attacker forces positions unhealthy and captures the liquidation discount, or profits from a hedged position on the other side. 42DAO pushed a median oracle's BTCB price abnormally low to force BTCB-vault liquidations (~$915K, BLC depegged >99%). Cascade accumulated longs in a low-liquidity market to push the mark price and liquidate CLS shorts (~$1.34M). Curve LlamaLend forced positions into soft liquidation, then donated to lift the sDOLA rate so they became hard-liquidatable (27 borrowers, ~$10.9M debt, ~$822K borrower equity lost). Aave's CAPO misparameterisation liquidated 34 healthy positions.

### Mandatory preconditions (all must hold; any proven absent kills the hypothesis)
- Liquidation eligibility derived from a price/rate readable at call time
- That price is movable by the liquidator, or misparameterised
- A liquidation incentive or a hedged position makes the move profitable
- Live borrower positions exist near the threshold

### Optional amplifiers (never the root cause)
- Flash loans
- Soft-liquidation (LLAMMA) bands amplifying the effect
- Thin mark-price market
- Large notional near the threshold

### Applicable protocol archetypes
lending, CDP, derivatives/perpetuals, basis trading, RWA lending

### Observable indicators

**Static (code)**
- health factor computed from a spot or convertToAssets read
- no deviation bound or grace period between price update and liquidation
- liquidation bonus fixed and large relative to venue depth

**Adapter**
- adapter shows collateral concentrated in one asset
- adapter lists markets whose collateral has thin external liquidity

**Runtime state**
- large borrow notional clustered near the liquidation threshold
- collateral asset whose deepest venue depth is small relative to that notional
- no liquidation circuit breaker or cooldown

**Cross-contract**
- the price source is a pool the liquidator can trade in the same transaction
- the mark price venue is the protocol's own book

### Decisive guards (presence normally kills the hypothesis)
- Liquidation prices from a deep aggregated feed with a deviation cap
- Grace period / cooldown between a large price move and liquidation eligibility
- Liquidation size caps per block
- Circuit breaker on abnormal price deltas

### False-positive killers
- Deviation-capped, independently sourced price plus a grace period (kills the pair)
- Liquidations rate-limited per block
- Collateral only in deep assets with caps sized to depth

### Local defensive property (fork-only test)
On a fork, execute the largest flash-funded move available on each pricing venue and assert that no position becomes liquidatable beyond the configured deviation bound.

### Recommended audit questions
- Is every mandatory precondition present in the live deployment?
- Is any decisive guard present in the deployed bytecode, not just the repository?
- What live value, authority or approval is reachable through this path?
- What single observation would falsify the hypothesis?

### Incidents
- `INC-2026-07-22-42D` — 2026-07-22 — **42DAO** — $915,000
- `INC-2026-07-15-CAS` — 2026-07-15 — **Cascade** — $1,343,921
- `INC-2026-03-12-AAV` — 2026-03-12 — **Aave V3** — $862,000
- `INC-2026-03-02-CUR` — 2026-03-02 — **Curve LlamaLend** — $240,000

**Provisional (grade C, not counted in statistics or ranking weight):**
- `INC-2026-03-02-INV` — 2026-03-02 — Inverse Finance

### Propagation
Distinct from the borrow-side oracle families because the guards differ: liquidation-side needs grace periods, size caps and circuit breakers, not just a better price. Two of the five did not steal protocol funds at all; the loss fell on borrowers, which loss-only rankings miss.

---

## `AUTH-MISSING-ON-VALUE-MOVING-PATH`

**A value-moving or configuration-setting function has no access control, or lost it in a refactor**

- **Incidents:** 4 (unique root causes: 4) · **6-month loss:** $814,000 · **Most recent:** 2026-07-28 · **Evidence strength:** HIGH

### Broken invariant
Every function that moves value or rebinds a privileged address must require a role the caller cannot obtain.

### Mechanism
A modifier is absent or was dropped during a refactor. SubQuery's Settings.setContractAddress() lost onlyOwner in a prior refactor, letting anyone install themselves as StakingManager and RewardsDistributor and drain pooled SQT from 272 stakers. Crypto DAO's Pro token exposed vault functions publicly; a permissionlessly-listed YieldCore vault omitted a caller check and was emptied in one call; Gondi V3's Sell-and-Repay bundler bypassed ownership checks on escrowed NFTs.

### Mandatory preconditions (all must hold; any proven absent kills the hypothesis)
- A function moves value or sets a privileged address/role
- No effective access control on that function
- Reachable by an ordinary caller
- The contract holds or controls value at call time

### Optional amplifiers (never the root cause)
- Recent refactor or upgrade
- Contract not covered by the latest audit
- Permissionless listing so nobody reviews the specific instance

### Applicable protocol archetypes
any

### Observable indicators

**Static (code)**
- external/public state-changing functions with no modifier
- setters for manager/distributor/treasury addresses without onlyOwner/role
- git history showing a modifier removed
- unverified implementation behind a verified proxy

**Adapter**
- adapter lists per-market or per-vault contracts created permissionlessly
- adapter's address list far larger than the audited set

**Runtime state**
- role holders that are EOAs
- config setters callable in eth_call from an arbitrary address without revert
- recently deployed contracts holding value with no audit reference

**Cross-contract**
- one contract's unguarded setter rebinds an address another contract trusts

### Decisive guards (presence normally kills the hypothesis)
- Role check on every state-changing external function, verified by selector enumeration
- Timelock on address-rebinding setters
- Automated deployment-time assertion that all setters revert for a random caller

### False-positive killers
- Every value-moving selector reverts for an unprivileged caller in simulation (kills the pair)
- Contract holds no value and controls no role

### Local defensive property (fork-only test)
Enumerate every external selector on the live implementation and prove, from an unprivileged address on a fork, that each either reverts or cannot move value or authority.

### Recommended audit questions
- Is every mandatory precondition present in the live deployment?
- Is any decisive guard present in the deployed bytecode, not just the repository?
- What live value, authority or approval is reachable through this path?
- What single observation would falsify the hypothesis?

### Incidents
- `INC-2026-07-28-CRY` — 2026-07-28 — **Crypto DAO** — $52,000
- `INC-2026-04-28-YIE` — 2026-04-28 — **YieldCore** — $398,000
- `INC-2026-04-12-SUB` — 2026-04-12 — **SubQuery Network** — $134,000
- `INC-2026-03-09-GON` — 2026-03-09 — **Gondi V3** — $230,000

**Provisional (grade C, not counted in statistics or ranking weight):**
- `INC-2026-08-03-RIS` — 2026-08-03 — RISEx
- `INC-2026-04-29-SWE` — 2026-04-29 — Sweat Foundation
- `INC-2026-04-09-AET` — 2026-04-09 — Aethir
- `INC-2026-02-27-STA` — 2026-02-27 — Stake Nova

### Propagation
Frequently introduced by refactors and by permissionless listing surfaces, where each new instance is unreviewed. Detection is cheap and fully read-only: selector enumeration plus simulated calls from an unprivileged address.

---

## `QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET`

**A quoted or aggregated output is applied to a different asset, unit or route than it was computed for**

- **Incidents:** 3 (unique root causes: 3) · **6-month loss:** $18,524,350 · **Most recent:** 2026-04-22 · **Evidence strength:** HIGH

### Broken invariant
A quantity produced by a quoter or accumulated across a route must be re-bound to the asset, decimals and per-hop economics it describes before it is used to transfer value.

### Mechanism
Kipseli's Base router took the amount from a USDC-only quoter and used it as the raw tokenOut transfer amount without checking the output token matched the quote token; a WETH -> cbBTC path produced a 6-decimal USDC value transferred as 8-decimal cbBTC, so ~0.04 WETH bought ~0.926 cbBTC (~$72.35K). Rhea aggregated expected output across multi-step swaps without accounting for tokens reused across steps, so a constructed route bypassed slippage protection for ~$18.4M. Juicebox skipped the oracle when currency matched the destination and used attacker-controlled decimals and balances.

### Mandatory preconditions (all must hold; any proven absent kills the hypothesis)
- A quote, expected-output or aggregate figure is computed in one context and consumed in another
- No assertion binding it to the output asset, its decimals, or per-hop reality
- The consumed figure sizes a transfer, mint or borrow
- Reachable by a caller who supplies the route or path

### Optional amplifiers (never the root cause)
- Multi-hop routes
- Caller-supplied route construction
- Assets with differing decimals
- Fee-on-transfer tokens in the path

### Applicable protocol archetypes
DEX aggregator/router, leveraged trading engine, cross-chain aggregator, lending extension, launch platform

### Observable indicators

**Static (code)**
- quoter output used directly as a transfer amount
- no decimals normalisation between quote and settlement asset
- slippage checked only on the aggregate route result
- currency-match branches skipping the oracle

**Adapter**
- adapter references a router/quoter pair
- protocol methodology describes multi-hop routing or margin/leverage swaps

**Runtime state**
- router supporting arbitrary token pairs while the quoter supports one base asset
- no per-hop minimum-out enforcement

**Cross-contract**
- quoter and settlement contract maintained separately, with differing supported-asset sets

### Decisive guards (presence normally kills the hypothesis)
- Assert quoteToken == outputToken and normalise decimals before transfer
- Per-hop minimum-out enforcement, not aggregate-only
- Post-swap balance-delta measurement as the authoritative amount

### False-positive killers
- Amount taken from a measured post-transfer balance delta (kills the pair)
- Per-hop minimums enforced
- Router restricted to assets the quoter supports

### Local defensive property (fork-only test)
On a fork, route through an unsupported or mismatched-decimals pair and assert the router reverts rather than transferring a mis-scaled amount.

### Recommended audit questions
- Is every mandatory precondition present in the live deployment?
- Is any decisive guard present in the deployed bytecode, not just the repository?
- What live value, authority or approval is reachable through this path?
- What single observation would falsify the hypothesis?

### Incidents
- `INC-2026-04-22-KIP` — 2026-04-22 — **Kipseli** — $72,350
- `INC-2026-04-20-JUI` — 2026-04-20 — **Juicebox V3** — $52,000
- `INC-2026-04-16-RHE` — 2026-04-16 — **Rhea Finance** — $18,400,000

### Propagation
Produced the largest single included loss of the window (Rhea, $18.4M). Routers and leverage engines that accept caller-constructed routes are the screening surface.

---

## `ACC-DONATION-UNACCOUNTED-BALANCE`

**An exchange rate or totalAssets is derived from a raw token balance, so an unaccounted transfer inflates it**

- **Incidents:** 3 (unique root causes: 3) · **6-month loss:** $9,980,000 · **Most recent:** 2026-07-06 · **Evidence strength:** HIGH

### Broken invariant
A share price, exchange rate or totalAssets must be a function of value the protocol accounted for on entry. Reading a raw balance makes any direct transfer into the accounting boundary an unpriced increase in every holder's claim.

### Mechanism
The rate is computed as (cash + borrows - reserves) / totalSupply, or as sum(balanceOf(component)), where cash is read via balanceOf(address(this)) or a component's balance. A direct transfer into that boundary raises the numerator with no new shares minted. Venus: getCashPrior() reads the vTHE contract's THE balance, so donations lifted the rate 1.03 -> 3.17 and bypassed the supply cap entirely (supply reached 367% of cap). Curve LlamaLend: DolaSavings.stake() donation lifted sDOLA's convertToAssets() 13.79%, and the market used that rate as its oracle. Lazy Summer: an impaired Silo Ark left active in the NAV let the attacker transfer economically worthless but on-chain-par tokens into the still-counted Ark, raising totalAssets() without realizable USDC.

### Mandatory preconditions (all must hold; any proven absent kills the hypothesis)
- A rate/NAV/exchange-rate read includes a raw balance of the protocol or a counted component
- An unprivileged party can transfer that asset into the accounting boundary (no allowlist on inbound transfers)
- The inflated rate is consumed by a value-bearing decision (redeem, borrow-power, liquidation, oracle)
- Other holders' claims or third-party positions are exposed to the inflated rate

### Optional amplifiers (never the root cause)
- Flash liquidity
- Long pre-accumulation of the donated asset
- Supply-cap bypass because the cap is checked on mint but the rate is not
- Impaired asset still carried at book value

### Applicable protocol archetypes
lending (Compound fork), CDP, vault/share token (ERC-4626), yield aggregator, risk curator, liquid staking, basis trading

### Observable indicators

**Static (code)**
- getCashPrior()/totalAssets() returning IERC20(x).balanceOf(address(this))
- exchangeRateStored = (cash + borrows - reserves)/totalSupply
- convertToAssets/pricePerShare with no internally tracked asset counter
- supply caps checked at mint but not against the rate

**Adapter**
- adapter sums balanceOf across strategy/Ark/silo addresses
- adapter treats a component vault's share price as authoritative
- Compound-fork adapter template (cToken/vToken enumeration)

**Runtime state**
- exchange rate materially above 1 and rising without proportional supply growth
- market supply exceeding the configured supply cap
- components in totalAssets whose underlying market is impaired or halted
- donation-shaped Transfer events into the vault/cToken with no matching Mint

**Cross-contract**
- a counted component is itself an ERC-4626 whose rate is externally manipulable
- offboarding partially complete: strategy removed from UI but still in the assets array

### Decisive guards (presence normally kills the hypothesis)
- Internally tracked totalAssets counter incremented only on accounted deposits
- Rate floors/ceilings and per-block rate-change caps that revert
- Virtual shares/assets offset (ERC-4626 OZ v5 style)
- Explicit skim of unaccounted balance to reserves rather than to the rate
- Offboarding removes the component from the assets array atomically with pausing it

### False-positive killers
- totalAssets derived from an internal counter, not balanceOf (kills the pair)
- Rate is monotonic and rate-limited per block
- Inbound transfers to the accounting boundary are rejected or swept to a reserve

### Local defensive property (fork-only test)
On a fork, transfer an arbitrary amount of each counted asset directly into every accounting boundary; the share price, exchange rate and derived borrow power must not change.

### Recommended audit questions
- Is every mandatory precondition present in the live deployment?
- Is any decisive guard present in the deployed bytecode, not just the repository?
- What live value, authority or approval is reachable through this path?
- What single observation would falsify the hypothesis?

### Incidents
- `INC-2026-07-06-LAZ` — 2026-07-06 — **Lazy Summer Protocol** — $6,040,000
- `INC-2026-03-15-VEN` — 2026-03-15 — **Venus Protocol** — $3,700,000
- `INC-2026-03-02-CUR` — 2026-03-02 — **Curve LlamaLend** — $240,000

### Propagation
Venus is a Compound-fork lineage defect that was raised in the protocol's own Code4rena audit and disputed at the time, so every unmodified Compound/Venus fork inherits it. Lazy Summer and Curve show the ERC-4626 variant. Because Compound forks and ERC-4626 vaults are the two most-copied templates in DeFi, this family has the widest live prerequisite base of any in the corpus.

---

## `ACC-NAV-SHAREPRICE-MANIPULABLE`

**Vault NAV counts positions whose on-chain valuation is inflatable or stale relative to realizable value**

- **Incidents:** 3 (unique root causes: 3) · **6-month loss:** $6,856,000 · **Most recent:** 2026-07-06 · **Evidence strength:** HIGH

### Broken invariant
totalAssets() must equal value the vault could actually realise now. Any component valued at book, at a manipulable rate, or after economic impairment lets a redeemer convert other depositors' claims into their own.

### Mechanism
The vault sums component valuations. At least one component is (a) an impaired or halted position still carried at par, (b) an externally manipulable share rate, or (c) priced by an oracle that can return zero or a wrong number. The attacker inflates or exploits the mismatch, mints or redeems at the wrong ratio, and extracts the difference from other depositors. Lazy Summer combined an incompletely offboarded Silo Ark with a $65.4M flash loan; Singularity's silent-zero oracle made totalAssets() report ~$100 so a flash deposit minted ~99.99% of shares; Edel inflated a wrapped-token exchange rate ~78x through repeated deposit/borrow loops.

### Mandatory preconditions (all must hold; any proven absent kills the hypothesis)
- Share price computed from a multi-component totalAssets()
- At least one component's valuation is externally influenceable, stale, or can return an absurd value
- Deposit and redeem are both reachable in a short window (same tx or same block)
- Other depositors' value is pooled with the attacker's

### Optional amplifiers (never the root cause)
- Flash loans
- Offboarding in progress
- Impaired upstream market (e.g. a collapsed strategy)
- Zero/near-zero reported totalAssets making share minting cheap

### Applicable protocol archetypes
yield aggregator, vault/share token, risk curator, structured product, onchain capital allocator, basis trading, indexes

### Observable indicators

**Static (code)**
- totalAssets() looping over a strategies/arks array
- component valuation via an external convertToAssets or oracle without sanity bounds
- no per-block deposit/redeem rate-change cap
- no minimum totalAssets floor before share minting

**Adapter**
- adapter enumerates strategies/arks/silos dynamically
- adapter includes addresses of upstream markets that are paused or impaired
- risk-curator adapters aggregating third-party vault positions

**Runtime state**
- strategies array containing addresses whose upstream market is halted
- reported APY/share-price discontinuities
- totalAssets small relative to component notional
- components whose own share price recently moved sharply

**Cross-contract**
- vault depends on another protocol's vault token whose rate is donation-inflatable
- curator multisig can add components without timelock

### Decisive guards (presence normally kills the hypothesis)
- Per-block share-price change cap that reverts
- Deposit and redeem in the same block disallowed or fee-penalised
- Component valuation bounded by an independent price with deviation caps
- Offboarding atomically removes the component from totalAssets
- Minimum totalAssets floor and virtual-share offset

### False-positive killers
- Share price rate-limited per block (kills same-transaction extraction)
- Single-asset vault with no external valuation
- Withdrawals queued with a delay and priced at settlement

### Local defensive property (fork-only test)
On a fork, for each component, force its valuation to zero and to 10x; the vault's mint/redeem must revert or be bounded, never transfer more than the depositor's pro-rata realisable share.

### Recommended audit questions
- Is every mandatory precondition present in the live deployment?
- Is any decisive guard present in the deployed bytecode, not just the repository?
- What live value, authority or approval is reachable through this path?
- What single observation would falsify the hypothesis?

### Incidents
- `INC-2026-07-06-LAZ` — 2026-07-06 — **Lazy Summer Protocol** — $6,040,000
- `INC-2026-07-01-EDE` — 2026-07-01 — **Edel Finance** — $403,000
- `INC-2026-04-27-SIN` — 2026-04-27 — **Singularity Finance** — $413,000

**Provisional (grade C, not counted in statistics or ranking weight):**
- `INC-2026-02-28-WIS` — 2026-02-28 — Wise Lending V2

### Propagation
The DefiLlama 'Risk Curators' and 'Onchain Capital Allocator' categories exist precisely because curators assemble third-party components into vaults; every added component is a new valuation dependency. Lazy Summer's root cause was an incomplete offboarding process, i.e. an operational failure expressed on-chain, which is invisible to a code-only audit.

---

## `SECRET-EMBEDDED-IN-PUBLIC-CODE-AS-AUTH`

**A signing key or constant secret embedded in deployed code is used as authorisation**

- **Incidents:** 3 (unique root causes: 3) · **6-month loss:** $4,171,100 · **Most recent:** 2026-07-30 · **Evidence strength:** HIGH

### Broken invariant
Deployed bytecode is public. Nothing inside it can be a secret, so no authorisation may depend on knowledge of a value present in the contract.

### Mechanism
Swan Treasury's ZhaiquanBuy contract hardcoded the off-chain _signer key, so anyone could forge valid signatures and buy ~687,000 STY at roughly a 100x discount for ~$625K profit. The third-party SquidRouterModule authenticated arbitrary calldata execution by comparing against a publicly visible constant string, draining ~$3.2M from 86 Gnosis Safes. SQ Protocol's verified Staking contract contained a hardcoded owner backdoor, taken over via an EIP-7702 type-4 authorizationList transaction for ~$346K.

### Mandatory preconditions (all must hold; any proven absent kills the hypothesis)
- Authorisation depends on a value present in the deployed bytecode or verified source
- That value gates a value-moving action
- The contract holds value, or holds approvals/module rights over value
- Reachable by anyone who reads the code

### Optional amplifiers (never the root cause)
- Contract name resembling a reputable protocol
- Installed as a Safe module or 7702 delegate
- Verified source making the constant trivially findable

### Applicable protocol archetypes
token sale, staking pool, smart account module, asset management, any contract with an off-chain signer

### Observable indicators

**Static (code)**
- private/internal constants named signer, secret, password, key
- address constants used as signature recovery targets
- string constants compared for authentication
- hardcoded owner addresses alongside a public takeover path

**Adapter**
- adapter references a module or helper not published by the named protocol
- name collision between an adapter address and a well-known protocol

**Runtime state**
- module enabled on user Safes
- 7702 delegation designators pointing at the code
- contract holding approvals or custody

**Cross-contract**
- third-party module trusted by user accounts but unaffiliated with the protocol it is named after

### Decisive guards (presence normally kills the hypothesis)
- No authorisation derived from in-code constants; signer keys held off-chain and only their address stored
- Authentication by signature over a fresh nonce, not by knowledge of a constant
- Module installation gated by a reviewed registry

### False-positive killers
- Only public keys/addresses appear in code, never private material or shared secrets (kills the pair)
- No module rights or approvals held

### Local defensive property (fork-only test)
Extract every constant from deployed bytecode and test whether presenting it authorises anything.

### Recommended audit questions
- Is every mandatory precondition present in the live deployment?
- Is any decisive guard present in the deployed bytecode, not just the repository?
- What live value, authority or approval is reachable through this path?
- What single observation would falsify the hypothesis?

### Incidents
- `INC-2026-07-30-SWA` — 2026-07-30 — **Swan Treasury** — $625,000
- `INC-2026-05-25-THI` — 2026-05-25 — **Third-party Gnosis Safe Module (SquidRouterModule)** — $3,200,000
- `INC-2026-05-12-SQP` — 2026-05-12 — **SQ Protocol** — $346,100

### Propagation
Explicitly an on-chain design failure rather than a key leak: the secrecy assumption is embedded in the deployment. Name-squatting third-party modules are the most dangerous variant because users grant them standing authority.

> **Not screenable as a protocol-family pair in the DefiLlama universe.** Requires bytecode constant analysis per contract; run as a sweep over deep-screened deployments rather than as a ranked pair.

---

## `ACC-SIGN-OR-BOUND-CHECK-MISSING`

**A signed or unbounded parameter inverts or inflates a value transfer**

- **Incidents:** 3 (unique root causes: 3) · **6-month loss:** $3,064,900 · **Most recent:** 2026-07-14 · **Evidence strength:** HIGH

### Broken invariant
A quantity that must be non-negative and bounded must be checked at the boundary. Casts between signed and unsigned types must be range-checked.

### Mechanism
Drips Network cast uint128 to int128 in DaiDripsHub.give(), so a large positive value became negative and reversed the transfer direction, draining 24,882.99 DAI from DaiReserve. Aftermath Finance allowed negative 'builder code' fees, inflating synthetic collateral and draining ~$1.14M across 11 transactions. Dango's insurance fund accepted donations without verifying the amount was positive.

### Mandatory preconditions (all must hold; any proven absent kills the hypothesis)
- A caller-influenced numeric parameter feeds a transfer, fee or collateral computation
- No range/sign check, or an unchecked cast between signed and unsigned
- The sign or magnitude change is realisable as value
- Reachable by an unprivileged caller

### Optional amplifiers (never the root cause)
- Solidity unchecked blocks
- Custom fixed-point libraries
- Move/Rust integer semantics differing from EVM

### Applicable protocol archetypes
derivatives/perpetuals, streaming payments, insurance fund, fee/rebate system, any protocol with configurable fees

### Observable indicators

**Static (code)**
- int128(uint128(x)) / int256(uint256(x)) casts without SafeCast
- fee parameters typed as signed integers
- donate/deposit functions with no amount > 0 require
- unchecked { } around arithmetic on user input

**Adapter**
- adapter reads a fee or funding parameter
- protocol methodology mentions builder codes, rebates or negative fees

**Runtime state**
- fee/rebate parameters currently negative or outside a sane range
- insurance/reserve balances reachable by a public donate path

**Cross-contract**
- fee parameters settable per-integrator rather than globally

### Decisive guards (presence normally kills the hypothesis)
- SafeCast on every cross-sign cast
- require(amount > 0) and explicit upper bounds on every caller-influenced quantity
- Fee parameters clamped to [0, max] at the setter

### False-positive killers
- SafeCast used throughout and fees clamped at the setter (kills the pair)
- No signed arithmetic in the value path

### Local defensive property (fork-only test)
Fuzz every external numeric parameter across type boundaries and assert no entrypoint produces a transfer to the caller exceeding their entitlement.

### Recommended audit questions
- Is every mandatory precondition present in the live deployment?
- Is any decisive guard present in the deployed bytecode, not just the repository?
- What live value, authority or approval is reachable through this path?
- What single observation would falsify the hypothesis?

### Incidents
- `INC-2026-07-14-DRI` — 2026-07-14 — **Drips Network** — $24,900
- `INC-2026-04-29-AFT` — 2026-04-29 — **Aftermath Finance** — $1,140,000
- `INC-2026-04-13-DAN` — 2026-04-13 — **Dango** — $1,900,000

**Provisional (grade C, not counted in statistics or ranking weight):**
- `INC-2026-08-11-HAR` — 2026-08-11 — Harmony Protocol

### Propagation
Appears across EVM, Move and a Cosmos-SDK chain in-window, so it is language-independent. Integrator-configurable fee parameters (builder codes, rebates) are the newest and least-audited surface.

> **Not screenable as a protocol-family pair in the DefiLlama universe.** Detected by parameter-shape sweep over deep-screened deployments.

---

## `ACC-MULTI-PATH-CREDIT-DRIFT`

**The same balance is reachable through multiple code paths that account for it differently**

- **Incidents:** 3 (unique root causes: 3) · **6-month loss:** $2,725,779 · **Most recent:** 2026-08-18 · **Evidence strength:** HIGH

### Broken invariant
Every path that can credit or debit a given balance must apply identical accounting. Where a protocol offers module sidecars, legacy plus current paths, or several entrypoints to one pool, cycling between them must be value-neutral.

### Mechanism
Ambient Finance's monolithic contract exposed HotProxy, WarmPath and ColdPath over shared surplus-collateral accounting; rapid cycling extracted ~83.72 ETH. Haedal's Sui vaults kept a deprecated deposit path alive after a 2025 upgrade: minting inflated LP shares through the old path and redeeming through the new one yielded ~$915K. Maya Protocol chained six edge cases across Trade Account, outbound handling and pool math to inflate accounting via a false subsidy, then extracted through add/remove liquidity.

### Mandatory preconditions (all must hold; any proven absent kills the hypothesis)
- Two or more reachable code paths mutate the same balance or share supply
- Their accounting differs (rounding, fee, subsidy, version, or ordering)
- A caller can cycle between them in one transaction or one block
- Value is realisable from the drift

### Optional amplifiers (never the root cause)
- Proxy/sidecar architecture
- Version migration in progress
- Cross-module subsidy or rebate logic
- Flash liquidity

### Applicable protocol archetypes
DEX/AMM (monolithic/singleton), vault/share token after upgrade, cross-chain liquidity network, lending with multiple entry modules

### Observable indicators

**Static (code)**
- several proxies/paths delegating into one storage layout
- deprecated deposit/withdraw retained alongside new ones
- subsidy or rebate logic spanning modules
- different rounding directions in sibling functions

**Adapter**
- adapter references several proxy/path addresses for one protocol
- adapter still lists a legacy path with the current one

**Runtime state**
- both old and new entrypoints succeed in simulation
- share supply reachable through more than one mint function
- surplus/credit balances non-zero for arbitrary addresses

**Cross-contract**
- shared storage across proxies
- module boundaries with no common invariant check

### Decisive guards (presence normally kills the hypothesis)
- One canonical accounting function all paths call
- Global invariant assert (total shares vs total assets) at the end of every external call
- Deprecated paths disabled atomically with the upgrade

### False-positive killers
- All mint/burn routes through a single internal function with a closing invariant assert (kills the pair)
- Only one live entrypoint per balance

### Local defensive property (fork-only test)
On a fork, enumerate all entrypoints touching a given balance and fuzz orderings; assert the global share/asset invariant holds after every sequence.

### Recommended audit questions
- Is every mandatory precondition present in the live deployment?
- Is any decisive guard present in the deployed bytecode, not just the repository?
- What live value, authority or approval is reachable through this path?
- What single observation would falsify the hypothesis?

### Incidents
- `INC-2026-08-18-MAY` — 2026-08-18 — **Maya Protocol** — $1,700,000
- `INC-2026-06-09-HAE` — 2026-06-09 — **Haedal Vault** — $915,179
- `INC-2026-06-08-AMB` — 2026-06-08 — **Ambient Finance** — $110,600

### Propagation
This is the failure mode of singleton and modular architectures, which are increasing. It is invisible to per-function review and only appears under cross-path fuzzing.

---

## `CALLBACK-UNAUTHENTICATED-CALLER-USES-APPROVALS`

**A callback or validation hook moves value from an address it never verified as the flow initiator**

- **Incidents:** 3 (unique root causes: 3) · **6-month loss:** $1,687,200 · **Most recent:** 2026-07-13 · **Evidence strength:** HIGH

### Broken invariant
When a contract pulls funds during a callback, the payer must be proven to be the initiator of the current flow, and the callback's caller must be proven to be the expected counterparty contract. Neither may be taken from caller-supplied payload.

### Mechanism
A flash-accounting or hook architecture passes a payload through a lock/callback. The callback implements pay() as token.transferFrom(payer, core, amount) with payer, token and amount read straight from that payload, and never asserts payer == lockInitiator. Any caller can therefore nominate a previously-approving victim as payer. Ekubo's v2 extension lost ~$1.4M (~17 WBTC) this way across ~85 transactions. The same shape appears where a swap callback (pancakeV3SwapCallback) on an EIP-7702-delegated account has no caller check, and where an account-abstraction validation phase grants an allowance as a side effect, letting a malicious paymaster harvest it (Lumi/Sodium).

### Mandatory preconditions (all must hold; any proven absent kills the hypothesis)
- A callback/hook pulls value using transferFrom or an allowance
- The payer/source address comes from caller-supplied payload or is unchecked
- The callback does not verify msg.sender is the expected pool/core contract
- Live approvals exist from third parties to the callback-implementing contract

### Optional amplifiers (never the root cause)
- Flash accounting / singleton lock architecture
- Router approvals carried over from a prior version
- Smart-account delegation (7702) adding callbacks to EOAs

### Applicable protocol archetypes
DEX/AMM with hooks or flash accounting, router/extension contract, account abstraction, paymaster, leveraged position manager

### Observable indicators

**Static (code)**
- pay/uniswapV3SwapCallback/lockAcquired implementations reading payer from calldata
- transferFrom(payer,...) where payer is a parameter
- callback without require(msg.sender == pool/core)
- approve() executed inside validateUserOp or a validation phase

**Adapter**
- adapter lists extension/hook contracts separately from core
- hook or extension addresses that users approve directly

**Runtime state**
- live allowances from EOAs to the extension/hook/router
- 7702 delegation designators on user EOAs pointing at code with public callbacks
- core contract's lock state readable and unbound to payer

**Cross-contract**
- extension trusted by core, but core does not forward the verified initiator
- paymaster allowed to spend allowances created during validation

### Decisive guards (presence normally kills the hypothesis)
- require(msg.sender == expectedPool/core) in every callback
- payer bound to the lock initiator recorded in transient storage at lock time
- allowance granted for exactly one flow and revoked before return
- no allowance side effects during validation phases

### False-positive killers
- Callback asserts both caller identity and payer == initiator (kills the pair)
- Contract never holds third-party approvals
- Payment always uses msg.sender as source

### Local defensive property (fork-only test)
On a fork, with a victim approval live, attempt to initiate the lock/callback path nominating the victim as payer; it must revert.

### Recommended audit questions
- Is every mandatory precondition present in the live deployment?
- Is any decisive guard present in the deployed bytecode, not just the repository?
- What live value, authority or approval is reachable through this path?
- What single observation would falsify the hypothesis?

### Incidents
- `INC-2026-07-13-LUM` — 2026-07-13 — **Lumi Finance** — $270,000
- `INC-2026-05-05-EKU` — 2026-05-05 — **Ekubo Protocol** — $1,400,000
- `INC-2026-04-03-EIP` — 2026-04-03 — **EIP-7702 Victim** — $17,200

### Propagation
Singleton/flash-accounting designs (Uniswap V4-style hooks, Ekubo, Ambient) push payment into callbacks, so the number of live protocols with this shape is growing. Custom third-party extensions, not the audited core, are where the gap appeared.

---

## `TOKEN-TRANSFER-OVERRIDE-BREAKS-CONSERVATION`

**A custom transfer override double-transfers, mis-deducts, or performs value-moving side effects**

- **Incidents:** 3 (unique root causes: 3) · **6-month loss:** $475,500 · **Most recent:** 2026-06-28 · **Evidence strength:** HIGH

### Broken invariant
A token transfer must conserve total supply plus balances: exactly `amount` leaves the sender and at most `amount` arrives, and the transfer must not move third-party or protocol-held value as a side effect.

### Mechanism
DIP's _transfer omitted a return statement on the PancakeSwap-routed branch, causing double transfers exploited with skim() and sync() for ~$111K. AIDC's _sellTransfer/burn accumulated burn fees without deducting them from the sender's balance, draining ~$121K WBNB. ATM's transferFrom automatically swapped ~20% of the transferred amount to BSC-USD, and repeatedly triggering it drained ~$243.5K. DGLD's legacy transferFrom edge case allowed unbacked wrapped supply on Base.

### Mandatory preconditions (all must hold; any proven absent kills the hypothesis)
- Token overrides _transfer/transferFrom/_update with non-standard logic
- A branch fails to conserve value (missing return, missing deduction, or a side-effect swap/mint)
- The branch is reachable by an unprivileged caller
- A pool or protocol holds value exposed to the branch

### Optional amplifiers (never the root cause)
- Router-specific branches
- skim()/sync() to realise the imbalance
- Flash loans

### Applicable protocol archetypes
token with custom transfer logic, RWA/wrapped token, bridged token

### Observable indicators

**Static (code)**
- multiple branches in _transfer with differing accounting
- missing return in a branch
- swap/mint invoked inside a transfer
- fee accumulated without a matching debit

**Adapter**
- adapter values a token whose contract has custom transfer logic
- misrepresentedTokens flag set

**Runtime state**
- totalSupply not reconciling with the sum of tracked balances
- pool balance drifting from reserves
- wrapped supply exceeding locked backing

**Cross-contract**
- the same token deployed on several chains with divergent transfer logic

### Decisive guards (presence normally kills the hypothesis)
- Property test asserting conservation across every transfer branch
- Fees taken only by reducing the credited amount
- No external calls inside transfer

### False-positive killers
- Standard OZ ERC-20 with no override (kills the pair)
- Conservation asserted by an invariant test on deployed bytecode

### Local defensive property (fork-only test)
Property test on deployed bytecode: for every branch, sum(balances) + burned is invariant across a transfer, and no third-party balance changes.

### Recommended audit questions
- Is every mandatory precondition present in the live deployment?
- Is any decisive guard present in the deployed bytecode, not just the repository?
- What live value, authority or approval is reachable through this path?
- What single observation would falsify the hypothesis?

### Incidents
- `INC-2026-06-28-AID` — 2026-06-28 — **AIDC** — $121,000
- `INC-2026-06-17-DIP` — 2026-06-17 — **DIP** — $111,000
- `INC-2026-06-04-ATM` — 2026-06-04 — **ATM** — $243,500

**Provisional (grade C, not counted in statistics or ranking weight):**
- `INC-2026-02-23-DGL` — 2026-02-23 — DGLD

### Propagation
Sibling of the deferred-burn family: same archetype, different broken step (conservation inside the transfer rather than out-of-band mutation of the pair).

> **Not screenable as a protocol-family pair in the DefiLlama universe.** Same population problem as the deferred-burn family.

---

## `ACC-ZERO-SUPPLY-INFLATION`

**Share math has an unguarded zero-supply or near-zero-supply branch**

- **Incidents:** 3 (unique root causes: 3) · **6-month loss:** $412,000 · **Most recent:** 2026-06-15 · **Evidence strength:** HIGH

### Broken invariant
The first depositor must not be able to set an arbitrary asset-per-share ratio, and no operation may drive supply low enough to restore that branch.

### Mechanism
With totalSupply == 0 and totalAssets == 0, a 1-wei deposit mints 1 share; a direct transfer of a large amount then makes each share worth that amount, so later depositors round to zero shares and the attacker redeems the pool. The same branch is reachable later if supply can be burned to near zero (Thetanuts' legacy vault reduced supply to near zero, then drained via redemption math). dTRINITY's dLEND took this on a live Ethereum deployment, leaving ~$257K of bad debt.

### Mandatory preconditions (all must hold; any proven absent kills the hypothesis)
- Share minting formula divides by totalSupply or totalAssets with a zero branch
- An unprivileged party can be the first depositor, or can drive supply to near zero
- Assets can be transferred in without minting shares
- A later depositor's funds are exposed to the manipulated ratio

### Optional amplifiers (never the root cause)
- Permissionless market/vault creation
- Newly deployed vaults with no seed
- Flash liquidity

### Applicable protocol archetypes
vault/share token (ERC-4626), lending market creation, options vault, yield aggregator

### Observable indicators

**Static (code)**
- shares = assets * totalSupply / totalAssets with no virtual offset
- no minimum initial deposit or dead-shares mint
- permissionless createVault/createMarket

**Adapter**
- adapter enumerates factory-created vaults/markets
- adapter includes very recently created vaults with tiny TVL

**Runtime state**
- live vaults/markets with totalSupply == 0 or dust supply
- factory able to create new markets permissionlessly
- no dead-shares balance at address(0) or address(1)

**Cross-contract**
- factory deploys vaults without seeding them
- router auto-lists new markets

### Decisive guards (presence normally kills the hypothesis)
- Virtual shares/assets offset (OZ ERC-4626 v5)
- Non-zero minimum initial shares burned to a dead address at creation
- Factory seeds every market at deploy time
- Minimum deposit floor

### False-positive killers
- Dead shares minted at creation (kills the pair)
- Vault creation is permissioned and every vault is seeded
- Virtual offset present in the deployed bytecode

### Local defensive property (fork-only test)
On a fork, for every vault with dust or zero supply, attempt the 1-wei-plus-donation sequence and assert a later depositor's shares are proportional.

### Recommended audit questions
- Is every mandatory precondition present in the live deployment?
- Is any decisive guard present in the deployed bytecode, not just the repository?
- What live value, authority or approval is reachable through this path?
- What single observation would falsify the hypothesis?

### Incidents
- `INC-2026-06-15-THE` — 2026-06-15 — **Thetanuts Finance** — $105,000
- `INC-2026-04-20-THE` — 2026-04-20 — **Thetanuts Finance** — $50,000
- `INC-2026-03-17-DTR` — 2026-03-17 — **dTRINITY dLEND** — $257,000

### Propagation
Still occurring on brand-new deployments in 2026 despite being a decade-old pattern, because factory-created markets are seeded by users rather than by the factory. Screen every factory's most recently created, least-funded children.

---

## `AUTH-IDENTITY-SATISFIABLE-BY-ATTACKER-CONTRACT`

**An authorisation check resolves identity through a caller-supplied address or an imitable property**

- **Incidents:** 3 (unique root causes: 3) · **6-month loss:** $278,700 · **Most recent:** 2026-05-23 · **Evidence strength:** HIGH

### Broken invariant
Authorisation must bind to an immutable identity the caller cannot supply, deploy or imitate. A check answered by code the caller controls is not a check.

### Mechanism
Mure's MureDistribution passed an attacker-supplied contract as the signature 'signer source', so SignatureChecker (ERC-1271 path) returned true and pre-approved QUEST tokens were drained via transferFrom. Ink Finance's Workspace Treasury accepted a deployed contract matching a whitelisted claimer identity, passing claim() authentication for ~$140K. Molt EVM's onlySpawnerToken modifier was satisfied by a deployed contract, allowing mintFromSpawner().

### Mandatory preconditions (all must hold; any proven absent kills the hypothesis)
- An authorisation path resolves identity via a caller-supplied address, an interface probe, or a property an attacker can reproduce
- No immutable allowlist or registry membership check
- The gated action moves value or mints
- Reachable permissionlessly

### Optional amplifiers (never the root cause)
- ERC-1271 support
- CREATE2 address grinding
- Interface-detection (ERC-165) used as authorisation
- Factory-registered identities

### Applicable protocol archetypes
reward distributor, DAO treasury, token with spawner/minter relationships, payments, any ERC-1271 integration

### Observable indicators

**Static (code)**
- SignatureChecker / isValidSignature with a caller-supplied signer
- modifiers checking an interface or a name rather than a registry
- authorisation via tx-supplied address parameters

**Adapter**
- adapter references factory-spawned contracts trusted by a parent

**Runtime state**
- whitelists keyed on something other than an immutable address
- registries writable without timelock
- pre-existing approvals to the distributor

**Cross-contract**
- parent token trusts any contract satisfying a shape rather than a registered address

### Decisive guards (presence normally kills the hypothesis)
- Immutable allowlist / registry membership required, checked by address
- Signer address fixed at deployment or set only through a timelock
- ERC-1271 accepted only from a registered set

### False-positive killers
- Authorisation checked against an immutable address set (kills the pair)
- No caller-supplied address enters the authorisation decision

### Local defensive property (fork-only test)
On a fork, deploy a contract that answers every probe affirmatively and attempt each gated action; all must revert.

### Recommended audit questions
- Is every mandatory precondition present in the live deployment?
- Is any decisive guard present in the deployed bytecode, not just the repository?
- What live value, authority or approval is reachable through this path?
- What single observation would falsify the hypothesis?

### Incidents
- `INC-2026-05-23-MUR` — 2026-05-23 — **Mure** — $11,700
- `INC-2026-05-11-INK` — 2026-05-11 — **Ink Finance** — $140,000
- `INC-2026-03-07-MOL` — 2026-03-07 — **Molt EVM** — $127,000

### Propagation
Growing with ERC-1271 and smart-account adoption: any integration that accepts a caller-nominated signer inherits this shape.

> **Not screenable as a protocol-family pair in the DefiLlama universe.** Detected by source-grep sweep over deep-screened deployments.

---

## `ACC-REWARD-INDEX-INIT-AND-ORDERING`

**Accrual index not initialised at join, or not updated before the balance change it prices**

- **Incidents:** 3 (unique root causes: 3) · **6-month loss:** $244,035 · **Most recent:** 2026-06-09 · **Evidence strength:** HIGH

### Broken invariant
A user's reward accrual must be computed against the index in force for the period they actually held the balance. The index must be initialised at join and updated before any balance change.

### Mechanism
Three shapes: dividends distributed before balance updates, so a small deposit sets the accrual basis and a large deposit is then priced on the old, small share (NovaBox: 427.5 WETH flash loan, ~145.82 ETH of phantom dividends, pool drained 65.11 -> 0.09 ETH); deposit/withdraw looped to mint inflated shares before rewards settle, redeemed after harvest (Goose Finance StrategyGooseEgg); an uninitialised variable in an accumulator so a 0.2 SUI stake generated 162 trillion points and drained ~150,000 SUI (Scallop's deprecated V2 rewards contract).

### Mandatory preconditions (all must hold; any proven absent kills the hypothesis)
- Reward/points accrual keyed on an index or checkpoint
- Index initialisation or update ordering is wrong relative to balance changes
- Deposit and claim reachable in a short window
- A funded reward pool is claimable

### Optional amplifiers (never the root cause)
- Flash loans
- Harvest triggerable by the caller
- Deprecated rewards contract with leftover funds

### Applicable protocol archetypes
reward distributor, farm, staking pool, yield aggregator, lending with incentives

### Observable indicators

**Static (code)**
- _distribute/_harvest called before _mint/_burn of shares
- userIndex not set on first interaction
- points formula reading an uninitialised struct field
- claim path not calling updateIndex first

**Adapter**
- adapter lists reward/gauge contracts separately
- adapter includes deprecated reward pools

**Runtime state**
- reward pool balance large relative to legitimate emissions
- user index entries at zero for active positions
- deprecated reward contracts still funded

**Cross-contract**
- strategy harvest callable by anyone and observable by the share math

### Decisive guards (presence normally kills the hypothesis)
- Checkpoint-before-mutate ordering enforced by a modifier on every balance-changing path
- User index initialised to the global index on first interaction
- Same-block deposit-and-claim disallowed

### False-positive killers
- Every balance-changing path calls the accrual update first (kills the pair)
- Rewards vest over time rather than being claimable immediately

### Local defensive property (fork-only test)
On a fork, deposit-claim-withdraw in one transaction from a fresh address; realised reward must be zero.

### Recommended audit questions
- Is every mandatory precondition present in the live deployment?
- Is any decisive guard present in the deployed bytecode, not just the repository?
- What live value, authority or approval is reachable through this path?
- What single observation would falsify the hypothesis?

### Incidents
- `INC-2026-06-09-NOV` — 2026-06-09 — **NovaBox** — $93,600
- `INC-2026-04-26-SCA` — 2026-04-26 — **Scallop** — $142,000
- `INC-2026-03-14-GOO` — 2026-03-14 — **Goose Finance** — $8,435

### Propagation
Two of three were on abandoned or deprecated reward contracts still holding funds, linking this family to UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY.

---

## `CALLBACK-STATE-LOCK-INCOMPLETE`

**The state lock does not cover the callback window, or state is written after the external call**

- **Incidents:** 3 (unique root causes: 3) · **6-month loss:** $68,300 · **Most recent:** 2026-07-30 · **Evidence strength:** HIGH

### Broken invariant
No externally reachable state may be read as authoritative while an external call from the same flow is outstanding. Effects must be written before interactions, and the lock must span every re-entrant path including sibling functions.

### Mechanism
Joe Agent's _removeLiquidityViaContract sent BNB by low-level call before updating lpInfo[user].lpAmount, permitting ~25 re-entrant loops for 62.5 BNB and ~1.196M JOE. Set Protocol / Index Coop's ExchangeIssuance lacked sufficient state locking, so a malicious manager pre-issue hook inflated positionMultiplier and the contract transferred assets on falsified data. Fractal Protocol's USDF vault was recursed through Balancer V2 batchSwap callbacks into deposit and withdraw with no invariant check across the re-entrant flow.

### Mandatory preconditions (all must hold; any proven absent kills the hypothesis)
- An external call (transfer, hook, callback) occurs before the state it depends on is finalised
- A re-entrant path can read or mutate that state
- The re-entered path moves value
- Reachable by an unprivileged caller, possibly via a third-party callback

### Optional amplifiers (never the root cause)
- Flash loans / batchSwap callbacks
- Manager or module hooks
- ERC-777/ERC-1363 callback tokens
- Cross-function re-entrancy where the guard covers only one function

### Applicable protocol archetypes
vault/share token, farm, liquidity manager, indexes, structured product, lending

### Observable indicators

**Static (code)**
- low-level call/transfer before state writes
- nonReentrant applied to some but not all mutating functions
- hooks invoked mid-computation
- no invariant assert at function exit

**Adapter**
- adapter references hook/module contracts
- protocol integrates external callback-bearing venues

**Runtime state**
- hook/module addresses settable by a manager
- integrations with callback-capable venues (Balancer vault, flash providers)

**Cross-contract**
- third-party callback re-enters a sibling function outside the guard

### Decisive guards (presence normally kills the hypothesis)
- Checks-Effects-Interactions applied throughout
- A single global re-entrancy lock covering every mutating entrypoint, including siblings
- Closing invariant assert (shares vs assets) at function exit
- Hooks restricted to a reviewed allowlist

### False-positive killers
- Global lock across all mutating functions plus CEI (kills the pair)
- No external calls before state finalisation

### Local defensive property (fork-only test)
On a fork, attempt re-entry into every mutating entrypoint from every reachable callback; each must revert or leave the global invariant intact.

### Recommended audit questions
- Is every mandatory precondition present in the live deployment?
- Is any decisive guard present in the deployed bytecode, not just the repository?
- What live value, authority or approval is reachable through this path?
- What single observation would falsify the hypothesis?

### Incidents
- `INC-2026-07-30-SET` — 2026-07-30 — **Set Protocol** — $9,600
- `INC-2026-05-28-JOE` — 2026-05-28 — **Joe Agent** — $45,000
- `INC-2026-05-22-FRA` — 2026-05-22 — **Fractal Protocol** — $13,700

### Propagation
Cross-function and cross-protocol re-entrancy through third-party callbacks (Balancer batchSwap, flash callbacks) is the live shape; single-function guards do not close it.

---

## `SIG-DIGEST-AMBIGUOUS-OR-UNBOUND`

**Critical action fields are outside the signed digest, or the digest encoding is ambiguous**

- **Incidents:** 2 (unique root causes: 2) · **6-month loss:** $1,480,000 · **Most recent:** 2026-05-20 · **Evidence strength:** HIGH

### Broken invariant
Every field that changes the economic effect of an authorised action must be inside the signed digest, and the encoding must be injective so no two distinct messages hash equal.

### Mechanism
Giddy's GiddyVaultV3 validated only part of the SwapInfo struct under EIP-712, leaving aggregator, fromToken, toToken and amount unsigned; the attacker replayed a valid signature with substituted fields (strategy LP tokens as fromToken, an attacker aggregator, a malicious toToken, max amount) for ~$1.3M. Butter Bridge's OmniServiceProxy hashed retry messages with abi.encodePacked over dynamic-bytes fields, so a colliding message forged authentication and minted ~10^15 MAPO.

### Mandatory preconditions (all must hold; any proven absent kills the hypothesis)
- A signed message authorises a parameterised action
- At least one economically decisive field is outside the digest, or encoding is ambiguous (packed dynamic fields)
- The action moves value or mints
- Reachable by presenting a valid-looking signature

### Optional amplifiers (never the root cause)
- Aggregator/router indirection
- Retry or replay paths
- Historic signatures available on-chain

### Applicable protocol archetypes
vault/share token, yield aggregator, bridge, cross-chain messaging, intents/RFQ, meta-transaction relayer

### Observable indicators

**Static (code)**
- EIP-712 typehash covering fewer fields than the function parameters
- abi.encodePacked over two or more dynamic types in a hash
- retry/replay entrypoints reusing an old digest

**Adapter**
- adapter references an aggregator or router the protocol calls with signed instructions

**Runtime state**
- historic signed calls whose parameters exceed the signed field set
- retry queues with unconsumed messages

**Cross-contract**
- signature verified in one contract, action executed in another with extra parameters

### Decisive guards (presence normally kills the hypothesis)
- Typehash covering every parameter that affects the outcome
- abi.encode (not encodePacked) for dynamic fields, or length-prefixed encoding
- Nonce and deadline in the digest, consumed once

### False-positive killers
- Typehash field set equals the function parameter set (kills the pair)
- abi.encode used throughout

### Local defensive property (fork-only test)
On a fork, take a valid signature and vary each unsigned parameter; every variation must revert.

### Recommended audit questions
- Is every mandatory precondition present in the live deployment?
- Is any decisive guard present in the deployed bytecode, not just the repository?
- What live value, authority or approval is reachable through this path?
- What single observation would falsify the hypothesis?

### Incidents
- `INC-2026-05-20-BUT` — 2026-05-20 — **Butter Bridge** — $180,000
- `INC-2026-04-23-GID` — 2026-04-23 — **Giddy** — $1,300,000

### Propagation
Cheap and decisive to check by diffing the EIP-712 typehash against the executing function's parameter list in verified source.

---

## `APPROVALS-TO-UPGRADEABLE-SPENDER`

**Live user approvals point at a contract whose implementation or authority can change**

- **Incidents:** 2 (unique root causes: 2) · **6-month loss:** $1,232,000 · **Most recent:** 2026-07-15 · **Evidence strength:** MEDIUM

### Broken invariant
The set of code that may spend a user's allowance must be fixed at the time the allowance is granted. If the spender is upgradeable, the user has approved future, unknown code.

### Mechanism
BarnBridge's attacker used DAO control to upgrade a proxy to a malicious implementation and then drained ~$776K through approvals ~50 addresses had already granted. Aurellion's re-initialisable diamond let the attacker add a facet with pullERC20/sweep and drain wallets that had approved the proxy. In both cases the approvals, not the TVL, were the value at risk.

### Mandatory preconditions (all must hold; any proven absent kills the hypothesis)
- Users hold live allowances to an upgradeable contract (proxy, diamond, beacon, or module)
- The upgrade path is reachable by governance, an EOA, or an initializer
- Approving accounts still hold balances
- No timelock or veto between upgrade and use

### Optional amplifiers (never the root cause)
- Unlimited approvals
- Long-lived integrations
- Diamond facets addable individually
- Beacon controlling many children

### Applicable protocol archetypes
governance-controlled proxy, router/aggregator, smart account module, diamond, any upgradeable spender

### Observable indicators

**Static (code)**
- proxy/diamond/beacon with an upgrade path plus a token-pulling role
- modules installable into user accounts

**Adapter**
- adapter references router/spender addresses users approve directly

**Runtime state**
- aggregate live allowance value to the spender
- proxy admin is an EOA or a non-timelocked governance executor
- recent implementation changes

**Cross-contract**
- governance executor holds PROXY_ADMIN over an approved spender
- beacon upgrade affects every child spender at once

### Decisive guards (presence normally kills the hypothesis)
- Timelock plus guardian veto on every upgrade path to an approved spender
- Non-upgradeable spender contracts (approvals only to immutable code)
- Per-flow allowances (Permit2 style) instead of standing approvals

### False-positive killers
- Spender is immutable (kills the pair)
- Aggregate live allowance is negligible (kills exposure)

### Local defensive property (fork-only test)
Enumerate live allowances to every upgradeable spender and treat their sum as value at risk in the upgrade path's threat model.

### Recommended audit questions
- Is every mandatory precondition present in the live deployment?
- Is any decisive guard present in the deployed bytecode, not just the repository?
- What live value, authority or approval is reachable through this path?
- What single observation would falsify the hypothesis?

### Incidents
- `INC-2026-07-15-BAR` — 2026-07-15 — **BarnBridge** — $776,000
- `INC-2026-05-12-AUR` — 2026-05-12 — **Aurellion Labs** — $456,000

### Propagation
An exposure multiplier rather than a standalone defect: it converts any governance or initializer weakness into direct user loss, and it is why TVL alone understates value at risk.

---

## `SETTLEMENT-EPOCH-BOUNDARY-CREDIT`

**Value credited using a per-epoch fixed figure that can be claimed across the boundary**

- **Incidents:** 2 (unique root causes: 2) · **6-month loss:** $703,700 · **Most recent:** 2026-08-02 · **Evidence strength:** MEDIUM

### Broken invariant
A quantity fixed for an epoch must not be claimable against a position established after that quantity was set, and entitlement must be prorated by time actually held.

### Mechanism
LOOPSDAO's LpdFi opened a hugely inflated interest-bearing position using a manipulated spot price and claimed interest right across the daily settlement boundary, forcing the protocol to burn its own Cake-LP and pay ~$690K. Fractal Protocol's USDF vault used a fixed daily-accrued tokenPrice (~1.27 USDC/USDF) that, combined with share rounding and re-entrant Balancer batchSwap callbacks, let deposit and withdraw be recursed inside one epoch.

### Mandatory preconditions (all must hold; any proven absent kills the hypothesis)
- A rate/price/accrual is fixed for an epoch and read at claim time
- A position can be created and claimed within, or straddling, one epoch
- No proration by holding time
- A funded pool honours the claim

### Optional amplifiers (never the root cause)
- Flash loans
- Predictable settlement timestamp
- Re-entrant callbacks inside the epoch
- Referral or multiplier logic

### Applicable protocol archetypes
epoch settlement, lending with daily accrual, yield vault with periodic pricing, structured product, perpetuals funding

### Observable indicators

**Static (code)**
- lastSettlement/epochId timestamps with a fixed stored price
- claim paths reading a stored price rather than a live one
- no time-weighting in the entitlement formula

**Adapter**
- adapter reads a stored price-per-share updated on a schedule
- methodology describes daily or periodic settlement

**Runtime state**
- stored epoch price stale relative to live market
- deposits spiking immediately before settlement
- no minimum holding period

**Cross-contract**
- settlement keeper callable by anyone
- epoch price set by an off-chain updater on a fixed cadence

### Decisive guards (presence normally kills the hypothesis)
- Time-weighted entitlement (prorate by seconds held within the epoch)
- Minimum holding period or deposit lock across settlement
- Deposits after the epoch price is fixed accrue from the next epoch

### False-positive killers
- Entitlement time-weighted (kills the pair)
- Deposits queued to the next epoch

### Local defensive property (fork-only test)
On a fork, deposit one second before settlement and claim one second after; realised value must be ~zero.

### Recommended audit questions
- Is every mandatory precondition present in the live deployment?
- Is any decisive guard present in the deployed bytecode, not just the repository?
- What live value, authority or approval is reachable through this path?
- What single observation would falsify the hypothesis?

### Incidents
- `INC-2026-08-02-LOO` — 2026-08-02 — **LOOPSDAO** — $690,000
- `INC-2026-05-22-FRA` — 2026-05-22 — **Fractal Protocol** — $13,700

### Propagation
Overlaps ORACLE-STALE-OR-SILENT-FALLBACK (a stored epoch price is a stale price) but the decisive guard is time-weighting, not a better feed, so it is kept separate.

---

## `ACC-SPLIT-NONINVARIANT`

**Per-operation pricing or state contraction is not invariant to splitting or recombining the same total amount**

- **Incidents:** 2 (unique root causes: 2) · **6-month loss:** $678,000 · **Most recent:** 2026-08-10 · **Evidence strength:** MEDIUM

### Broken invariant
Executing an operation once for amount N and executing it k times for N/k must produce the same total economic result. Any per-operation averaging, contraction factor or rounding that breaks this yields free value to whoever splits.

### Mechanism
USM's ethFromDefund() priced a redemption at the arithmetic mean of current and estimated final FUM sell prices; combined with a per-redemption contraction (adjShrinkFactor) and integer rounding, 64 small defund() calls extracted more ETH than one large call. Lien Finance's exchangeEquivalentBonds omitted multiset integrity checks, so a bond set could be exchanged for one that was not economically equivalent, minting unbacked bonds.

### Mandatory preconditions (all must hold; any proven absent kills the hypothesis)
- A public operation whose price/fee/state update is computed per call
- The formula is non-linear in amount, or applies a per-call contraction, or rounds directionally
- The operation can be repeated freely in one transaction
- Value is realisable from the difference

### Optional amplifiers (never the root cause)
- Flash loans to pre-position
- Low gas cost per call
- No minimum operation size

### Applicable protocol archetypes
stablecoin issuer, structured product, options, AMM with custom curve, bond/tranche protocol

### Observable indicators

**Static (code)**
- average-of-two-prices formulas
- shrink/contraction factors applied per call
- no assertion that f(N) == sum(f(N/k))
- exchange/split/merge functions without a value-conservation assert

**Adapter**
- adapter models a custom bonding curve or tranche system
- protocol methodology mentions a bespoke pricing formula

**Runtime state**
- contraction/shrink parameters non-neutral
- no per-transaction operation-count limit

**Cross-contract**
- split and merge handled by different modules with different math

### Decisive guards (presence normally kills the hypothesis)
- Explicit split-invariance assertion in tests and on-chain bounds
- Value-conservation assert across exchange/split/merge (sum of inputs == sum of outputs at one price)
- Rounding always against the caller

### False-positive killers
- Pricing is linear in amount
- A conservation assert reverts on any imbalance (kills the pair)

### Local defensive property (fork-only test)
Property test: for random N and k, assert result(N) >= sum(result(N/k)) within one wei, on the deployed bytecode.

### Recommended audit questions
- Is every mandatory precondition present in the live deployment?
- Is any decisive guard present in the deployed bytecode, not just the repository?
- What live value, authority or approval is reachable through this path?
- What single observation would falsify the hypothesis?

### Incidents
- `INC-2026-08-10-USM` — 2026-08-10 — **USM** — $136,000
- `INC-2026-07-24-LIE` — 2026-07-24 — **Lien Finance** — $542,000

### Propagation
Two independent protocols, both with bespoke pricing. Bespoke curve math, not forked code, is the prerequisite; look for protocols whose methodology describes a custom formula.

---

## `UPGRADE-INITIALIZER-REACHABLE-LIVE`

**An initializer remains callable on a live deployment**

- **Incidents:** 2 (unique root causes: 2) · **6-month loss:** $665,000 · **Most recent:** 2026-05-12 · **Evidence strength:** HIGH

### Broken invariant
After deployment, no caller may (re)establish ownership, admin, or implementation wiring. Initialization state must be provably consumed.

### Mechanism
An initializer is unprotected, or the initialized flag lives in a slot the deployment never wrote. Aurellion's Diamond (EIP-2535) had an owner set but OpenZeppelin's _initialized slot still 0, so initialize(address) could be called again; the attacker took ownership, used diamondCut to add a facet exposing pullERC20/sweep, and drained wallets that had approved the diamond. Renegade's V1 dark-pool proxy had an unprotected initializer plus a version counter left out of sync by an April 2025 migration, enabling malicious logic and a delegatecall drain of 27 ERC-20s.

### Mandatory preconditions (all must hold; any proven absent kills the hypothesis)
- An initializer/reinitializer is reachable on the live proxy or facet
- The initialized flag is unset, or the version counter allows re-entry
- Initialization can grant ownership or rewire implementation
- The deployment holds value or live approvals

### Optional amplifiers (never the root cause)
- Diamond/beacon architecture with many facets
- A migration that changed the initializer scheme
- Live unlimited approvals to the proxy

### Applicable protocol archetypes
governance-controlled proxy, diamond, beacon proxy, any upgradeable deployment

### Observable indicators

**Static (code)**
- initialize()/reinitializer(n) external without initializer modifier
- custom initialization flags not matching the OZ slot
- diamondCut callable by owner with no timelock

**Adapter**
- adapter references proxy addresses across several deployment generations
- adapter's addresses include facets or beacons

**Runtime state**
- ERC-1967 _initialized slot reads 0 on a live proxy
- implementation slot changed recently
- live approvals to the proxy
- owner is an EOA

**Cross-contract**
- beacon controls many child proxies, so one initializer covers all children
- proxy admin equals deployer EOA

### Decisive guards (presence normally kills the hypothesis)
- initializer/reinitializer modifiers with the flag asserted non-zero post-deploy
- Deployment-time assertion that re-initialization reverts
- diamondCut and upgrade behind a timelock

### False-positive killers
- Simulated re-initialization reverts (kills the pair)
- Contract is non-upgradeable and holds no approvals

### Local defensive property (fork-only test)
Read the initialization slot on every live proxy/facet and simulate re-initialization from an unprivileged address; it must revert.

### Recommended audit questions
- Is every mandatory precondition present in the live deployment?
- Is any decisive guard present in the deployed bytecode, not just the repository?
- What live value, authority or approval is reachable through this path?
- What single observation would falsify the hypothesis?

### Incidents
- `INC-2026-05-12-AUR` — 2026-05-12 — **Aurellion Labs** — $456,000
- `INC-2026-05-10-REN` — 2026-05-10 — **Renegade** — $209,000

### Propagation
Directly observable read-only: one storage read of the ERC-1967/OZ initialized slot plus one simulated call per proxy. Beacon architectures multiply the blast radius across every child.

---

## `ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE`

**An ERC-4626 share rate (convertToAssets / pricePerShare) is used directly as a collateral price feed**

- **Incidents:** 2 (unique root causes: 2) · **6-month loss:** $643,000 · **Most recent:** 2026-07-01 · **Evidence strength:** HIGH

### Broken invariant
A vault share rate is an accounting quantity of another protocol, not a market price. Using it as a feed imports every way that vault's rate can be moved, including donation inflation and same-transaction redemption effects.

### Mechanism
Curve LlamaLend's CryptoFromPoolVaultWAgg oracle called sDOLA.convertToAssets() as a spot feed. The rate was atomically manipulable by large redemptions and re-deposits and by a DolaSavings.stake() donation, which lifted it 13.79% (1.189 -> 1.353) and hard-liquidated 27 borrowers holding ~$10.9M of debt. Edel Finance's lending market valued wGOOGLx by its wrapper exchange rate, which repeated deposit/borrow loops inflated ~78x, creating ~$403K of bad debt.

### Mandatory preconditions (all must hold; any proven absent kills the hypothesis)
- A lending/CDP market prices collateral via a share rate or wrapper exchange rate
- That rate is influenceable by an unprivileged actor (donation, redemption, loop) in a short window
- No deviation bound or TWAP is applied to the rate
- Live borrow capacity or liquidation eligibility depends on it

### Optional amplifiers (never the root cause)
- Flash loans
- Large share supply held outside collateralised positions
- Soft-liquidation mechanics amplifying small rate moves
- Wrapper with a thin underlying

### Applicable protocol archetypes
lending, CDP, risk curator, leveraged vault, basis trading

### Observable indicators

**Static (code)**
- oracle contracts named *FromPoolVault*, *4626*, *WrapperRate*
- price = vault.convertToAssets(1e18) with no bounds
- pricePerShare()/getPricePerFullShare() in a price path

**Adapter**
- adapter lists ERC-4626 vault tokens as collateral
- adapter values a wrapper by its own exchange rate
- market list includes yield-bearing wrappers

**Runtime state**
- collateral assets that are ERC-4626 shares or wrappers
- the underlying vault's rate movable by donation (see ACC-DONATION family)
- share supply outside collateral positions large enough to move the rate

**Cross-contract**
- the priced vault is a different protocol with its own risk surface
- no rate-change cap between the two protocols

### Decisive guards (presence normally kills the hypothesis)
- Rate capped by a growth-rate adapter (max APR) with a hard deviation bound
- Rate smoothed over time and floored/ceilinged
- Underlying vault verified non-donation-inflatable before listing
- Independent market price cross-check for the wrapper

### False-positive killers
- Growth-capped rate adapter in the deployed oracle (kills the pair)
- Wrapper's own rate is monotonic and rate-limited
- Collateral priced by an independent market feed instead

### Local defensive property (fork-only test)
On a fork, donate to and cycle the underlying vault; assert the lending market's reported collateral price moves no more than the configured cap.

### Recommended audit questions
- Is every mandatory precondition present in the live deployment?
- Is any decisive guard present in the deployed bytecode, not just the repository?
- What live value, authority or approval is reachable through this path?
- What single observation would falsify the hypothesis?

### Incidents
- `INC-2026-07-01-EDE` — 2026-07-01 — **Edel Finance** — $403,000
- `INC-2026-03-02-CUR` — 2026-03-02 — **Curve LlamaLend** — $240,000

### Propagation
Yield-bearing collateral is now standard, so this shape is spreading fast. It is the intersection of ACC-DONATION-UNACCOUNTED-BALANCE (in the priced vault) and the lending market that trusts it; screen the pair, not either side alone.

---

## `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL`

**A zero-value or dust transfer triggers a privileged accrual, mint or burn hook**

- **Incidents:** 2 (unique root causes: 2) · **6-month loss:** $630,000 · **Most recent:** 2026-06-23 · **Evidence strength:** HIGH

### Broken invariant
A transfer of zero (or dust) must be economically inert. Hooks that accrue, mint, harvest or burn must not be reachable by an operation that moves no value and bypasses authorisation.

### Mechanism
Little Boy Plus' LBPHashrate._update() was triggered by a zero-value transferFrom, bypassing OpenZeppelin's allowance path, calling _harvest and minting LBP straight to the PancakeSwap pair, inflating the pair's balance without a reserve update and enabling a ~$367K drain. Royal.io's Royal1155LD used 100 zero-value ERC-1155 transfers to manipulate beforeLdaTransfer, inflating pro-rata royalty balances for ~$263K.

### Mandatory preconditions (all must hold; any proven absent kills the hypothesis)
- A transfer hook (_update, _beforeTokenTransfer, beforeLdaTransfer) performs accrual, mint, harvest or burn
- Zero-value or dust transfers are not rejected before the hook
- The hook's effect is value-bearing
- Reachable permissionlessly, including from an unrelated account

### Optional amplifiers (never the root cause)
- ERC-1155 batch transfers
- Allowance checks skipped for zero amounts
- Flash loans
- Hook minting directly to an AMM pair

### Applicable protocol archetypes
reward distributor, farm, NFT royalties, token with accrual hooks, staking

### Observable indicators

**Static (code)**
- accrual/mint/harvest logic inside a transfer hook
- no require(amount > 0) before the hook
- ERC-1155 hooks looping over ids with zero amounts

**Adapter**
- adapter references a royalty or accrual contract
- reward accrual tied to token transfers

**Runtime state**
- hook-bearing tokens with a funded reward or royalty pool
- historical zero-value Transfer events in unusual volume

**Cross-contract**
- the hook mints into a pool it does not control

### Decisive guards (presence normally kills the hypothesis)
- require(amount > 0) before any hook side effect
- Accrual moved out of transfer hooks into explicit, authorised functions
- Hooks made idempotent and caller-authorised

### False-positive killers
- Zero-amount transfers revert or short-circuit before the hook (kills the pair)
- Hooks are pure bookkeeping with no mint/transfer

### Local defensive property (fork-only test)
On a fork, issue zero-value transfers in a loop against every hook-bearing token and assert no state with economic value changes.

### Recommended audit questions
- Is every mandatory precondition present in the live deployment?
- Is any decisive guard present in the deployed bytecode, not just the repository?
- What live value, authority or approval is reachable through this path?
- What single observation would falsify the hypothesis?

### Incidents
- `INC-2026-06-23-ROY` — 2026-06-23 — **Royal.io** — $263,000
- `INC-2026-06-17-LIT` — 2026-06-17 — **Little Boy Plus** — $367,000

### Propagation
A general primitive rather than a chain-specific one, and unusually cheap for an attacker: the trigger costs only gas.

> **Not screenable as a protocol-family pair in the DefiLlama universe.** Applies to token contracts with accrual hooks; only reachable through per-token screening, not the protocol universe.

---

## `METATX-SENDER-IDENTITY-CONFUSION`

**Meta-transaction sender resolution disagrees across a trust boundary**

- **Incidents:** 2 (unique root causes: 2) · **6-month loss:** $282,700 · **Most recent:** 2026-05-13 · **Evidence strength:** MEDIUM

### Broken invariant
_msgSender() must resolve to the same principal everywhere authorisation is evaluated, and a contract must never be able to forward a call that makes itself the trusted forwarder for its own request.

### Mechanism
DBXen was drained ~$150K through an ERC-2771 sender identity inconsistency: the appended sender bytes were trusted in a context where the caller could control them. ShapeShift's FOX Colony on Arbitrum lost ~$132.7K via a meta-transaction self-call flaw combined with DSAuth authorisation, where a self-call let the contract authorise itself.

### Mandatory preconditions (all must hold; any proven absent kills the hypothesis)
- Contract supports meta-transactions (ERC-2771 or custom) or DSAuth-style self-authorisation
- The forwarder set is permissive, or self-calls are treated as authorised
- Authorisation is evaluated using the resolved sender
- Value or authority is reachable

### Optional amplifiers (never the root cause)
- Multiple forwarders
- Self-call helper functions
- Legacy DSAuth patterns
- Batch/multicall entrypoints appending sender bytes

### Applicable protocol archetypes
DAO treasury/governance, token with gasless transfers, farm, any ERC-2771 integration

### Observable indicators

**Static (code)**
- _msgSender() overrides with trustedForwarder checks
- address(this) accepted as an authorised caller
- multicall combined with ERC-2771 (the classic self-forward)
- DSAuth with a permissive authority

**Adapter**
- adapter references governance/colony contracts with meta-transaction support

**Runtime state**
- trustedForwarder set to a permissive or self address
- authority contract granting broad rights

**Cross-contract**
- forwarder trusted by several contracts with different authorisation models

### Decisive guards (presence normally kills the hypothesis)
- Single immutable trusted forwarder; self-address never trusted
- Multicall disabled on ERC-2771 contracts, or sender bytes stripped
- Authorisation on the true msg.sender for privileged actions

### False-positive killers
- No meta-transaction support (kills the pair)
- Forwarder immutable and address(this) explicitly rejected

### Local defensive property (fork-only test)
On a fork, craft a self-forwarded call appending an arbitrary sender and assert every privileged action reverts.

### Recommended audit questions
- Is every mandatory precondition present in the live deployment?
- Is any decisive guard present in the deployed bytecode, not just the repository?
- What live value, authority or approval is reachable through this path?
- What single observation would falsify the hypothesis?

### Incidents
- `INC-2026-05-13-SHA` — 2026-05-13 — **ShapeShift FOX Colony** — $132,700
- `INC-2026-03-11-DBX` — 2026-03-11 — **DBXen** — $150,000

### Propagation
Two independent protocols with different meta-transaction stacks, so the family is about the trust boundary rather than a specific library.

> **Not screenable as a protocol-family pair in the DefiLlama universe.** Requires ERC-2771 detection per contract; run as a sweep.

---

## `TOKEN-TRANSFER-INTENT-HEURISTIC-FORGEABLE`

**Buy/sell/liquidity classification is inferred from a forgeable heuristic**

- **Incidents:** 2 (unique root causes: 2) · **6-month loss:** $277,041 · **Most recent:** 2026-06-05 · **Evidence strength:** MEDIUM

### Broken invariant
If a token applies different rules to buys, sells and liquidity operations, the classification must be derived from evidence the caller cannot fabricate.

### Mechanism
DTXT classified transfers by inspecting the pair's balances, so sending a small amount of USDT directly to the pair made large sells look like liquidity additions, bypassing sell fees and draining ~$35K. Movie Token (MT) whitelisted the router and pair to make deflationary mode work, and the attacker swapped and removed liquidity through the router to acquire MT outside the restriction, then used a referral rule allowing the first 0.2 MT to bypass buyer checks.

### Mandatory preconditions (all must hold; any proven absent kills the hypothesis)
- Token applies different fee/restriction logic by inferred transfer intent
- Classification derived from balances, addresses or amounts a caller can influence
- Bypassing the classification yields value
- Reachable permissionlessly

### Optional amplifiers (never the root cause)
- Router and pair whitelists
- Referral exemptions
- Multiple pairs across routers

### Applicable protocol archetypes
token with custom transfer logic, launchpad token, farm token

### Observable indicators

**Static (code)**
- from == pair / to == pair used as buy/sell detection
- balance comparisons deciding fee branches
- hardcoded router/pair exemptions
- first-N-token referral exemptions

**Adapter**
- adapter values a fee-on-transfer token via pair reserves

**Runtime state**
- exemption mappings populated with routers/pairs
- multiple pairs for the token across routers

**Cross-contract**
- exemptions granted to contracts that can be called by anyone

### Decisive guards (presence normally kills the hypothesis)
- Classification from an explicit, protocol-minted receipt or an allowlisted entry function, not inference
- No address-based exemptions for callable contracts
- Same rules on every path

### False-positive killers
- No per-intent branching (kills the pair)
- Entry restricted to a protocol-controlled router that records intent explicitly

### Local defensive property (fork-only test)
On a fork, attempt each restricted operation through every alternative path (direct pair, router, add/remove liquidity) and assert the same fee/restriction applies.

### Recommended audit questions
- Is every mandatory precondition present in the live deployment?
- Is any decisive guard present in the deployed bytecode, not just the repository?
- What live value, authority or approval is reachable through this path?
- What single observation would falsify the hypothesis?

### Incidents
- `INC-2026-06-05-DTX` — 2026-06-05 — **DTXT/USDT liquidity pair on BSC** — $35,041
- `INC-2026-03-10-MTW` — 2026-03-10 — **MT-WBNB liquidity pool** — $242,000

### Propagation
Always co-occurs with the deferred-burn family in this corpus; the heuristic bypass is what makes the burn reachable.

> **Not screenable as a protocol-family pair in the DefiLlama universe.** Same population problem as the deferred-burn family.

---

## `SIG-VERIFIER-DEFEATABLE`

**Signature verification returns true for input that carries no authorisation**

- **Incidents:** 2 (unique root causes: 2) · **6-month loss:** $97,819 · **Most recent:** 2026-06-25 · **Evidence strength:** HIGH

### Broken invariant
A verification routine must reject malformed, empty or zero-recovered signatures, and must never treat address(0) as a match.

### Mechanism
MoneyMon's verify() checked only recoverSigner(...) == admin without handling ecrecover returning address(0); with admin set to the zero address, an invalid signature (r=0, s=0, v=27) passed and drained the contract. Lixir Finance's lv_* wrappers had broken EIP-2612 permit verification, so one dummy signature granted the attacker approval over dozens of holders' tokens.

### Mandatory preconditions (all must hold; any proven absent kills the hypothesis)
- A signature check gates a value-moving action
- The check can return true without a valid signer (ecrecover zero, unchecked return, malformed accepted)
- The gated action moves value or grants approval
- Reachable by an unprivileged caller

### Optional amplifiers (never the root cause)
- Admin/signer address set to zero
- Wrapper tokens holding many users' assets
- Permit-based approval flows

### Applicable protocol archetypes
reward distributor, wrapper/vault token, NFT staking, payments, any permit-enabled token

### Observable indicators

**Static (code)**
- ecrecover used without a require(signer != address(0))
- permit implementations diverging from the EIP-2612 reference
- verification result compared to a mutable address that may be zero

**Adapter**
- adapter lists wrapper tokens with custom permit implementations

**Runtime state**
- admin/signer variable reading address(0)
- wrapper tokens with many holders and live balances

**Cross-contract**
- one wrapper's permit governs assets held in another contract

### Decisive guards (presence normally kills the hypothesis)
- require(recovered != address(0) && recovered == expected)
- Use of ECDSA.recover (OZ) which reverts on invalid signatures
- Signer address immutable or non-zero-enforced at the setter

### False-positive killers
- OZ ECDSA library in the deployed bytecode (kills the ecrecover-zero shape)
- Signer address immutable and non-zero

### Local defensive property (fork-only test)
On a fork, submit r=0,s=0,v=27 and an empty signature to every signature-gated entrypoint; all must revert.

### Recommended audit questions
- Is every mandatory precondition present in the live deployment?
- Is any decisive guard present in the deployed bytecode, not just the repository?
- What live value, authority or approval is reachable through this path?
- What single observation would falsify the hypothesis?

### Incidents
- `INC-2026-06-25-LIX` — 2026-06-25 — **Lixir Finance** — $12,300
- `INC-2026-05-29-MON` — 2026-05-29 — **MoneyMon** — $85,519

### Propagation
Trivially screenable from verified source; the zero-address branch is the single highest-signal grep in the whole library.

> **Not screenable as a protocol-family pair in the DefiLlama universe.** Detected by source-grep sweep over deep-screened deployments.

---

## `TOKEN-PACKED-OWNERSHIP-UNDERFLOW`

**Packed ownership or alias encoding with unchecked arithmetic**

- **Incidents:** 2 (unique root causes: 1) · **6-month loss:** $40,000 · **Most recent:** 2026-06-09 · **Evidence strength:** HIGH

### Broken invariant
An identifier packed alongside data must be range-checked, and arithmetic over packed fields must not underflow into an adjacent field.

### Mechanism
The shared DN404/BT404 codebase packed ownership with token-ID aliases; a malicious high-bit token ID combined with an unchecked integer underflow let the attacker mint near-infinite fpTokens/$BMP for dust WETH, drain pools and extract high-value NFTs (Flooring Protocol V2 / BitmapPunks). Asterix Labs, a Flooring fork, was hit the following day through the same codebase.

### Mandatory preconditions (all must hold; any proven absent kills the hypothesis)
- Token packs ownership/alias/ID data into shared storage words
- Arithmetic over packed fields is unchecked or the ID range is unvalidated
- Mint or transfer quantity derives from the packed value
- Live liquidity or NFT custody is exposed

### Optional amplifiers (never the root cause)
- Hybrid ERC-20/ERC-721 (DN404/ERC-404 family)
- Shared upstream codebase across forks
- NFT custody alongside fungible liquidity

### Applicable protocol archetypes
NFT liquidity protocol, hybrid ERC-20/721 token, NFT fractionalisation

### Observable indicators

**Static (code)**
- DN404/BT404/ERC-404 lineage
- bit-packing helpers with unchecked blocks
- token-ID alias arithmetic
- no upper bound on token IDs

**Adapter**
- adapter values NFT liquidity vaults
- adapter's protocol forked from a hybrid-token codebase

**Runtime state**
- hybrid token contracts holding both NFT custody and AMM liquidity
- fork lineage matching a known-vulnerable upstream

**Cross-contract**
- several deployments sharing one upstream library version

### Decisive guards (presence normally kills the hypothesis)
- Checked arithmetic on all packed-field operations
- Explicit token-ID range validation
- Upgrade to the patched upstream, verified in deployed bytecode

### False-positive killers
- Deployed bytecode matches the patched upstream (kills the pair)
- No packed ownership encoding

### Local defensive property (fork-only test)
Differentially test the deployed bytecode against the patched upstream on boundary token IDs.

### Recommended audit questions
- Is every mandatory precondition present in the live deployment?
- Is any decisive guard present in the deployed bytecode, not just the repository?
- What live value, authority or approval is reachable through this path?
- What single observation would falsify the hypothesis?

### Incidents
- `INC-2026-06-09-AST` — 2026-06-09 — **Asterix Labs** — $40,000
- `INC-2026-06-08-FLO` — 2026-06-08 — **Flooring Protocol & BitmapPunks** — not disclosed

### Propagation
A genuine fork-clone lineage: Flooring and Asterix are one root cause across two deployments, one day apart, and count once toward unique root causes. Every unpatched DN404/BT404 deployment shares it.

> **Not screenable as a protocol-family pair in the DefiLlama universe.** Requires DN404/BT404 lineage; no in-universe protocol above the TVL threshold carries it.

---

## `ACC-DUPLICATE-ID-ACCUMULATION`

**An array of IDs is accumulated without deduplication or consumption**

- **Incidents:** 2 (unique root causes: 2) · **6-month loss:** $13,021 · **Most recent:** 2026-06-03 · **Evidence strength:** MEDIUM

### Broken invariant
An entitlement attached to an identifier may be counted at most once per period. A caller-supplied ID list must be deduplicated, or each ID's claim state consumed before the next read.

### Mechanism
A batch function loops a caller-supplied ID array, accumulating an amount per entry, and only writes the consumed marker after the loop. Repeating the same ID multiplies the payout. ApeBond's migrateToVotingEscrow accepted duplicate pool IDs, inflating a lock from ~1.71 to ~29 quadrillion ABOND. LootBot AI's redeem() accepted 7 NFT IDs each repeated 155 times because nextRedeem was updated only after payout.

### Mandatory preconditions (all must hold; any proven absent kills the hypothesis)
- Batch function takes a caller-supplied array of IDs
- Per-ID amount accumulated inside the loop
- Consumed/claimed state written after the loop, or not at all
- A funded pool pays the accumulated amount

### Optional amplifiers (never the root cause)
- Flash loans to trigger a fresh epoch
- No array length cap

### Applicable protocol archetypes
reward distributor, NFT staking, vote-escrow migration, airdrop claim, farm

### Observable indicators

**Static (code)**
- for-loops over calldata ID arrays with += accumulation
- state write after the loop rather than inside it
- no seen-set or sorted-strictly-increasing requirement

**Adapter**
- adapter enumerates pools/positions by ID
- adapter references a migration or claim helper

**Runtime state**
- claim pool funded
- claimed-marker mappings sparsely populated relative to activity

**Cross-contract**
- migration helper trusted by an escrow/lock contract

### Decisive guards (presence normally kills the hypothesis)
- Mark each ID consumed inside the loop before accruing
- Require strictly increasing IDs to make duplicates impossible
- Deduplicate into a set before accumulation

### False-positive killers
- Consumed marker written inside the loop (kills the pair)
- IDs required strictly increasing

### Local defensive property (fork-only test)
On a fork, call the batch function with one ID repeated k times; payout must equal the single-ID payout.

### Recommended audit questions
- Is every mandatory precondition present in the live deployment?
- Is any decisive guard present in the deployed bytecode, not just the repository?
- What live value, authority or approval is reachable through this path?
- What single observation would falsify the hypothesis?

### Incidents
- `INC-2026-06-03-APE` — 2026-06-03 — **ApeBond** — $3,421
- `INC-2026-04-15-LOO` — 2026-04-15 — **LootBot AI** — $9,600

### Propagation
Cheap to screen: find every external function taking an array of IDs and check for in-loop consumption.

> **Not screenable as a protocol-family pair in the DefiLlama universe.** Detected by selector-shape sweep over deep-screened deployments.

---

## `AMM-POOL-RATIO-SKEW-EXTRACTION`

> **SINGLE_EVENT_FAMILY** — one verified incident. No recurrence is claimed.

**A pool's own pricing curve can be skewed by flash-funded swaps to extract more than the fee compensates**

- **Incidents:** 1 (unique root causes: 1) · **6-month loss:** $1,650,000 · **Most recent:** 2026-07-19 · **Evidence strength:** MEDIUM

### Broken invariant
A pool's invariant and fee schedule must ensure that any round trip through it costs the trader at least the fees, for every reachable ratio, including extreme imbalance.

### Mechanism
Allbridge Core's Solana USDC/USDT pools were skewed by rapid swaps funded with a ~$1.12M Kamino flash loan, draining ~$1.65M. The stable-swap style curve mispriced at extreme imbalance so a round trip was profitable rather than fee-paying.

### Mandatory preconditions (all must hold; any proven absent kills the hypothesis)
- The protocol operates its own pricing curve (stable-swap, bonding, or custom)
- The curve's output at extreme imbalance is favourable to the trader
- Ratio can be moved and restored within one transaction or block
- Pool holds LP-owned value

### Optional amplifiers (never the root cause)
- Flash loans
- Low or flat fees
- Multiple correlated pools to cycle between
- Cross-chain pools sharing one curve

### Applicable protocol archetypes
DEX/AMM, bridge with liquidity pools, stable-swap, basis trading

### Observable indicators

**Static (code)**
- custom invariant implementations
- fee independent of imbalance
- no imbalance cap or per-block trade-size limit

**Adapter**
- adapter reads pool balances for a bridge or custom AMM
- liquidity concentrated in few pools

**Runtime state**
- pool ratio far from balanced
- fee parameters flat across the curve
- no per-block volume cap

**Cross-contract**
- the same curve deployed across chains with differing depth

### Decisive guards (presence normally kills the hypothesis)
- Imbalance-scaled fees making extreme-ratio round trips loss-making
- Per-block trade-size or ratio-change caps
- Curve tested to the boundary with a proof that round trips are non-profitable

### False-positive killers
- Round-trip non-profitability proven across the ratio range (kills the pair)
- Standard constant-product with a fee floor

### Local defensive property (fork-only test)
On a fork, fuzz round trips at every reachable ratio with flash-scale size; realised profit before gas must never be positive.

### Recommended audit questions
- Is every mandatory precondition present in the live deployment?
- Is any decisive guard present in the deployed bytecode, not just the repository?
- What live value, authority or approval is reachable through this path?
- What single observation would falsify the hypothesis?

### Incidents
- `INC-2026-07-19-ALL` — 2026-07-19 — **Allbridge Core** — $1,650,000

### Propagation
SINGLE_EVENT_FAMILY. Distinct from the oracle families because the pool is the victim of its own curve rather than a consumer of a manipulated price.

---

## `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY`

> **SINGLE_EVENT_FAMILY** — one verified incident. No recurrence is claimed.

**A public claim path pays from a reserve with no eligibility binding or consumption**

- **Incidents:** 1 (unique root causes: 1) · **6-month loss:** $907,700 · **Most recent:** 2026-08-02 · **Evidence strength:** MEDIUM

### Broken invariant
A claim must be bound to a caller-specific entitlement that is checked and consumed exactly once.

### Mechanism
MOKE's MokeToken.releaseContract() exposed claim() with no eligibility check on the caller; repeated calls drained ~166 million MOKE from the internal reserve, converted via flash loans, Venus leverage, LP removal and dividend distribution into ~1,546 BNB (~$907.7K).

### Mandatory preconditions (all must hold; any proven absent kills the hypothesis)
- Public claim/release function pays from a protocol-held reserve
- No mapping binding the caller to an entitlement, or the entitlement is not consumed
- The reserve is funded
- Reachable without privilege

### Optional amplifiers (never the root cause)
- Repeatable in a loop
- Dividend/LP mechanics to convert the claimed token
- Leverage venue for the claimed asset

### Applicable protocol archetypes
token with reserve/release schedule, reward distributor, airdrop claim, launchpad, vesting contract

### Observable indicators

**Static (code)**
- claim()/release() with no msg.sender lookup
- no claimed[msg.sender] mapping, or set after transfer
- amount derived from contract balance rather than entitlement

**Adapter**
- adapter counts a release/reserve contract's balance as TVL

**Runtime state**
- release/reserve contract holding a large balance
- claim entitlement mapping empty while the reserve is funded

**Cross-contract**
- reserve contract funded by the token contract on a schedule

### Decisive guards (presence normally kills the hypothesis)
- Caller eligibility mapping checked and consumed once before transfer
- Merkle-proof-gated claims with nullifiers
- Per-address and global claim caps

### False-positive killers
- Claim requires a proof or a populated entitlement mapping (kills the pair)
- Reserve holds zero balance

### Local defensive property (fork-only test)
On a fork, call the claim path from a fresh address with no prior interaction; it must transfer nothing.

### Recommended audit questions
- Is every mandatory precondition present in the live deployment?
- Is any decisive guard present in the deployed bytecode, not just the repository?
- What live value, authority or approval is reachable through this path?
- What single observation would falsify the hypothesis?

### Incidents
- `INC-2026-08-02-MOK` — 2026-08-02 — **MOKE** — $907,700

### Propagation
SINGLE_EVENT_FAMILY in-window but the canonical shape: exposure equals the reserve balance and is readable in one call.

> **Not screenable as a protocol-family pair in the DefiLlama universe.** Detected by selector sweep over deep-screened deployments.

---

## `ACC-CREDIT-NOT-RECEIVED`

> **SINGLE_EVENT_FAMILY** — one verified incident. No recurrence is claimed.

**Reward or entitlement credited from an observed balance delta rather than value actually spent with the protocol**

- **Incidents:** 1 (unique root causes: 1) · **6-month loss:** $560,000 · **Most recent:** 2026-07-25 · **Evidence strength:** MEDIUM

### Broken invariant
Reward credit must be derived from economic value actually transferred to, or spent through, the protocol. A balance delta observed on a third-party venue is not proof of a purchase.

### Mechanism
A permissionless tracking function reads a token balance change on an external pair and treats it as a purchase, sizing a reward allocation from it. Projekt's trackPurchase read only balance deltas without verifying ETH spent, so the attacker flash-loaned ~14K WETH, pushed it through memecoin pairs and used skim() to fabricate purchase records, inflating allocations and draining ~301.7 ETH via massWithdraw.

### Mandatory preconditions (all must hold; any proven absent kills the hypothesis)
- Permissionless function that records an entitlement
- Entitlement sized from an observed balance/state delta rather than a transfer into the protocol
- No binding between the recorded action and value received by the protocol
- A funded reward reserve is claimable against the recorded entitlement

### Optional amplifiers (never the root cause)
- Flash loans
- skim()/sync() to fabricate deltas
- Batch withdraw function

### Applicable protocol archetypes
reward distributor, points/airdrop system, farm, launchpad, loyalty/rebate system

### Observable indicators

**Static (code)**
- trackPurchase/recordBuy/registerAction style external functions
- balanceOf deltas used as the reward basis
- no msg.value or transferFrom in the crediting path

**Adapter**
- adapter counts a reward pool balance as TVL
- adapter references a distributor separate from the core protocol

**Runtime state**
- reward reserve balance large relative to protocol revenue
- entitlement mapping writable by arbitrary callers

**Cross-contract**
- crediting contract observes pools it does not control

### Decisive guards (presence normally kills the hypothesis)
- Credit amount taken from the post-transfer balance delta of the protocol's own accounting boundary
- Purchases proven by a receipt the protocol itself minted during the swap
- Per-address caps and eligibility consumption

### False-positive killers
- Credit derived from transferFrom into the protocol (kills the pair)
- Entitlements written only by a trusted settlement path

### Local defensive property (fork-only test)
On a fork, fabricate the observable precondition without transferring value to the protocol; the entitlement must not increase.

### Recommended audit questions
- Is every mandatory precondition present in the live deployment?
- Is any decisive guard present in the deployed bytecode, not just the repository?
- What live value, authority or approval is reachable through this path?
- What single observation would falsify the hypothesis?

### Incidents
- `INC-2026-07-25-PRO` — 2026-07-25 — **Projekt** — $560,000

### Propagation
SINGLE_EVENT_FAMILY in-window. Retained because the prerequisites are unusually observable and reward reserves are commonly funded well above the cost of fabricating a delta.

> **Not screenable as a protocol-family pair in the DefiLlama universe.** Reward-tracker contracts are rarely separate DefiLlama entries; folded into the reward-index sweep.

---

## `INCENTIVE-PER-ADDRESS-NO-SYBIL-COST`

> **SINGLE_EVENT_FAMILY** — one verified incident. No recurrence is claimed.

**A per-address grant is repeatable at negligible cost with fresh addresses**

- **Incidents:** 1 (unique root causes: 1) · **6-month loss:** $200,000 · **Most recent:** 2026-05-25 · **Evidence strength:** MEDIUM

### Broken invariant
An incentive granted per address must cost the claimant more than it pays, or must be bound to an identity or stake that cannot be cheaply duplicated.

### Mechanism
WUSD.fi / GLOVE granted rewards in the _englove path to addresses holding under 2 GLOVE with no Sybil resistance. Using EIP-7702 helper contracts and a Morpho USDT flash loan, the attacker repeatedly wrapped and unwrapped at least 100 WUSD across fresh addresses, harvesting nearly 2 GLOVE per cycle and dumping into Uniswap V3 for ~$200K of USDC/USDT.

### Mandatory preconditions (all must hold; any proven absent kills the hypothesis)
- A reward or bonus is granted per address, per epoch, or on a threshold condition
- Creating qualifying addresses is cheap
- The reward is immediately liquid
- A funded pool or liquid market absorbs the claimed value

### Optional amplifiers (never the root cause)
- EIP-7702 batching many addresses in one transaction
- Flash loans for the qualifying balance
- Thin market for the reward token making the incentive large in relative terms

### Applicable protocol archetypes
stablecoin issuer with incentives, reward distributor, points/airdrop, launchpad, loyalty program

### Observable indicators

**Static (code)**
- reward conditions keyed on balanceOf(msg.sender) < threshold
- first-time-user bonuses without proof of uniqueness
- no per-address lifetime cap

**Adapter**
- adapter counts an incentive pool as TVL
- protocol methodology describes per-user bonuses

**Runtime state**
- incentive pool funded and claimable now
- reward token thin relative to the pool
- many fresh addresses claiming in one block

**Cross-contract**
- 7702 delegation making batch address creation cheap

### Decisive guards (presence normally kills the hypothesis)
- Rewards proportional to stake and time, not per address
- Lifetime per-address caps with a global budget
- Proof-of-uniqueness or a minimum holding period
- Vesting so rewards cannot be dumped in the same transaction

### False-positive killers
- Rewards strictly proportional to time-weighted stake (kills the pair)
- Vesting or claim delay prevents same-transaction realisation

### Local defensive property (fork-only test)
On a fork, batch N fresh addresses through the qualifying flow in one transaction and assert total reward scales with capital committed, not with address count.

### Recommended audit questions
- Is every mandatory precondition present in the live deployment?
- Is any decisive guard present in the deployed bytecode, not just the repository?
- What live value, authority or approval is reachable through this path?
- What single observation would falsify the hypothesis?

### Incidents
- `INC-2026-05-25-WUS` — 2026-05-25 — **WUSD.fi / GLOVE** — $200,000

### Propagation
SINGLE_EVENT_FAMILY, but EIP-7702 materially lowered the cost of the address-multiplication step, so per-address incentive designs that were previously uneconomic to farm are now in range.

---

## `AUTH-ZERO-ADDRESS-ACCEPTED`

> **SINGLE_EVENT_FAMILY** — one verified incident. No recurrence is claimed.

**address(0) is accepted as valid authority, so renounced ownership can be reclaimed**

- **Incidents:** 1 (unique root causes: 1) · **6-month loss:** $98,200 · **Most recent:** 2026-05-28 · **Evidence strength:** MEDIUM

### Broken invariant
Renouncing ownership must permanently remove the capability. A check of the form caller == owner must never pass when owner is the zero address, and no default-zero role may be satisfiable.

### Mechanism
ONTR's onlyOwner check accepted owner == address(0), so a renounced token could be re-owned; combined with hidden balance-grant logic that fabricated balances without totalSupply or mint events, the attacker dumped into the ONTR/WETH pool. The same primitive appears in MoneyMon, where admin was the zero address and ecrecover's zero return matched it.

### Mandatory preconditions (all must hold; any proven absent kills the hypothesis)
- An authority check compares against a variable that may be address(0)
- That variable is currently zero, or reachable to zero via renounce
- The gated function moves value or grants authority
- Reachable by an unprivileged caller

### Optional amplifiers (never the root cause)
- Publicly advertised 'ownership renounced' status reducing scrutiny
- Hidden balance-granting logic
- Recovered signer defaulting to zero

### Applicable protocol archetypes
token, any contract advertising renounced ownership, reward distributor

### Observable indicators

**Static (code)**
- require(msg.sender == owner) with no owner != address(0) assertion
- custom Ownable variants
- role mappings whose default value is satisfiable

**Adapter**
- adapter includes tokens marketed as ownership-renounced

**Runtime state**
- owner()/admin reading address(0) on a contract that still holds value or authority
- renounce transaction in history with privileged functions still present

**Cross-contract**
- a renounced contract still holds a role in a funded system

### Decisive guards (presence normally kills the hypothesis)
- Assert owner != address(0) inside the modifier
- Renounce implemented as a permanent capability removal (functions self-disable), not an address write
- OZ Ownable2Step with zero-address rejection

### False-positive killers
- Modifier asserts non-zero owner (kills the pair)
- Renounce removes the functions' effect, not just the address

### Local defensive property (fork-only test)
Read owner/admin on every live contract; where zero, simulate every privileged selector from an arbitrary address and require a revert.

### Recommended audit questions
- Is every mandatory precondition present in the live deployment?
- Is any decisive guard present in the deployed bytecode, not just the repository?
- What live value, authority or approval is reachable through this path?
- What single observation would falsify the hypothesis?

### Incidents
- `INC-2026-05-28-ONT` — 2026-05-28 — **ONTR** — $98,200

### Propagation
Read-only detectable at scale: owner() == address(0) plus a non-zero balance is a two-call screen across an entire address set.

> **Not screenable as a protocol-family pair in the DefiLlama universe.** Screened as a cheap read-only sweep (owner()==address(0) with non-zero balance) rather than as a protocol-family pair.

---

## `SIG-REPLAY-CROSS-POSITION`

> **SINGLE_EVENT_FAMILY** — one verified incident. No recurrence is claimed.

**A signature is valid across positions, accounts or contexts because the digest omits the identifier**

- **Incidents:** 1 (unique root causes: 1) · **6-month loss:** $29,984 · **Most recent:** 2026-08-08 · **Evidence strength:** MEDIUM

### Broken invariant
A signed authorisation must bind to exactly one position, account, chain, contract and nonce, and must be consumable once.

### Mechanism
Atomic Green's manager signature was replayable across 21 different Uniswap V3 LP positions because the position ID was not part of the signed digest; combined with flash-loan price manipulation it triggered unauthorised full LP burns for ~29,984 USDC.

### Mandatory preconditions (all must hold; any proven absent kills the hypothesis)
- An off-chain signature authorises an on-chain action
- The digest omits the position/account/context identifier or a nonce
- Multiple instances exist that the same signature satisfies
- Those instances hold value

### Optional amplifiers (never the root cause)
- Many positions under one manager
- Signature published on-chain by first use
- Flash-loan price manipulation to make the burn profitable

### Applicable protocol archetypes
liquidity manager, leveraged trading, vault manager, NFT position manager, intents/RFQ

### Observable indicators

**Static (code)**
- EIP-712 structs lacking positionId/tokenId/nonce/deadline
- hash built from action type and amount only
- no usedSignature/nonce mapping

**Adapter**
- adapter enumerates many per-user positions under one manager
- manager-operated LP strategies

**Runtime state**
- many live positions under one manager address
- no nonce mapping populated
- manager signature reuse visible in historical calldata

**Cross-contract**
- one manager signs for positions across several pools or chains

### Decisive guards (presence normally kills the hypothesis)
- Position/token ID, chainId, verifying contract, nonce and deadline all in the signed struct
- Nonce consumed before external calls
- Signature bound to a single position by construction

### False-positive killers
- Digest includes the position ID and a consumed nonce (kills the pair)
- Actions authorised on-chain per position rather than by signature

### Local defensive property (fork-only test)
On a fork, capture a signature used on position A and replay it against position B; it must revert.

### Recommended audit questions
- Is every mandatory precondition present in the live deployment?
- Is any decisive guard present in the deployed bytecode, not just the repository?
- What live value, authority or approval is reachable through this path?
- What single observation would falsify the hypothesis?

### Incidents
- `INC-2026-08-08-ATO` — 2026-08-08 — **Atomic Green** — $29,984

### Propagation
SINGLE_EVENT_FAMILY. Blast radius scales with position count under one signer, so exposure can be far larger than the observed loss.

---

## `STORAGE-LAYOUT-COLLISION-PHANTOM-CREDIT`

> **SINGLE_EVENT_FAMILY** — one verified incident. No recurrence is claimed.

**A storage slot collision turns a control sentinel into spendable credit**

- **Incidents:** 1 (unique root causes: 1) · **6-month loss:** $25,000 · **Most recent:** 2026-06-01 · **Evidence strength:** MEDIUM

### Broken invariant
Distinct logical variables must occupy distinct storage slots. A library that writes a fixed slot must not overlap application storage, and no control value may be readable as a balance.

### Mechanism
ATOHook's rewards mapping collided with Solady's fixed ReentrancyGuard slot; the nonReentrant modifier in getReward() wrote a sentinel value that was then read as a reward balance for the colliding address, letting the attacker claim a fixed amount 200 times for ~14.41 ETH.

### Mandatory preconditions (all must hold; any proven absent kills the hypothesis)
- A library or pattern writes a hardcoded storage slot (transient or persistent)
- Application state maps into the same slot space
- The colliding value is interpreted as an amount or authorisation
- The contract holds claimable value

### Optional amplifiers (never the root cause)
- Solady/assembly-optimised libraries with fixed slots
- Diamond storage patterns
- Upgrades that reorder storage
- Repeatable claim path

### Applicable protocol archetypes
reward distributor, AMM hook, diamond/upgradeable contract, any contract using fixed-slot libraries

### Observable indicators

**Static (code)**
- Solady ReentrancyGuard or similar fixed-slot libraries alongside mappings at low slots
- assembly sstore/tstore to constant slots
- diamond storage without namespaced structs

**Adapter**
- adapter references hook or reward contracts built on assembly-optimised libraries

**Runtime state**
- reward/credit entries for addresses with no interaction history
- storage reads returning sentinel-like constants (1, 2, type(uint).max) as balances

**Cross-contract**
- upgrade history showing storage layout changes

### Decisive guards (presence normally kills the hypothesis)
- ERC-7201 namespaced storage
- Storage-layout diffing in CI across upgrades and libraries
- Sentinel values chosen outside any plausible amount range

### False-positive killers
- Namespaced storage throughout (kills the pair)
- No fixed-slot libraries in the deployed bytecode

### Local defensive property (fork-only test)
Dump the deployed storage layout and assert no application mapping's slot space intersects any library's fixed slot.

### Recommended audit questions
- Is every mandatory precondition present in the live deployment?
- Is any decisive guard present in the deployed bytecode, not just the repository?
- What live value, authority or approval is reachable through this path?
- What single observation would falsify the hypothesis?

### Incidents
- `INC-2026-06-01-ATO` — 2026-06-01 — **ATOHook** — $25,000

### Propagation
SINGLE_EVENT_FAMILY, but rising: gas-optimised fixed-slot libraries and hook architectures are both spreading, and the collision is invisible in source review without a layout dump.

> **Not screenable as a protocol-family pair in the DefiLlama universe.** Requires a storage-layout dump per contract; run as a sweep over deep-screened deployments.

---

## `ACC-HARDCODED-PEG-REDEMPTION`

> **SINGLE_EVENT_FAMILY** — one verified incident. No recurrence is claimed.

**Redemption honours a hardcoded peg that the mint side validates but the burn side does not**

- **Incidents:** 1 (unique root causes: 1) · **6-month loss:** $8,500 · **Most recent:** 2026-07-13 · **Evidence strength:** MEDIUM

### Broken invariant
If minting checks that the market price is at peg, redemption must apply the symmetric check. Asymmetric validation lets anyone buy the asset below peg and redeem it at par against real collateral.

### Mechanism
Chi Protocol's ArbitrageV5.burn() redeemed USC for weETH/stETH/WETH at a hardcoded $1 while mint checked the peg; the attacker flash-bought heavily depegged USC on a thin Uniswap V2 pool and redeemed at par, nearly draining reserves.

### Mandatory preconditions (all must hold; any proven absent kills the hypothesis)
- Redemption values the protocol asset at a fixed or hardcoded price
- The mint path applies a peg/market check the burn path omits
- The asset trades below that price on a reachable venue
- Redeemable collateral is held

### Optional amplifiers (never the root cause)
- Thin secondary market
- Flash loans
- Depeg already in progress

### Applicable protocol archetypes
stablecoin issuer, CDP, synthetic asset, RWA token

### Observable indicators

**Static (code)**
- burn/redeem using a constant 1e18 price while mint reads an oracle
- asymmetric require sets between mint and burn
- arbitrage module with one-sided checks

**Adapter**
- adapter prices the protocol's stablecoin at a hardcoded $1
- `misrepresentedTokens` or peg assumptions in methodology

**Runtime state**
- market price of the asset materially below the redemption price
- collateral reserve redeemable at par
- no redemption cap or fee scaling with the depeg

**Cross-contract**
- arbitrage/stability module holds the reserve while the token contract holds the peg logic

### Decisive guards (presence normally kills the hypothesis)
- Symmetric peg validation on mint and burn
- Redemption priced from the same oracle as minting
- Redemption fee or cap scaling with observed depeg

### False-positive killers
- Burn reads the same oracle as mint (kills the pair)
- Redemption disabled below a price band

### Local defensive property (fork-only test)
On a fork, depeg the asset on its deepest venue and attempt redemption; the protocol must price the redemption at market or revert.

### Recommended audit questions
- Is every mandatory precondition present in the live deployment?
- Is any decisive guard present in the deployed bytecode, not just the repository?
- What live value, authority or approval is reachable through this path?
- What single observation would falsify the hypothesis?

### Incidents
- `INC-2026-07-13-CHI` — 2026-07-13 — **Chi Protocol** — $8,500

### Propagation
SINGLE_EVENT_FAMILY. Directly checkable by diffing the require-sets of mint and burn in deployed source.

> **Not screenable as a protocol-family pair in the DefiLlama universe.** Folded into the stablecoin-issuer oracle screen.

---

## Families with no addressable population in the DefiLlama universe

These families are real and evidenced, but their live prerequisite base is not a set of DefiLlama-listed protocols. They are handled as read-only sweeps over the deployments that deep screening already touches, and are recorded here so the gap is explicit rather than silent.

| Family | Incidents | 6-month loss | Why it is not a protocol-family pair |
|---|---:|---:|---|
| `TOKEN-DEFERRED-BURN-LP-RESERVE-DESYNC` | 14 | $5,425,242 | Victims are individually deployed BSC/Base tokens with custom transfer logic that are not listed as DefiLlama protocols; the family has no addressable protocol population in this universe. Handed to the token-level monitoring workstream instead. |
| `TOKEN-TRANSFER-OVERRIDE-BREAKS-CONSERVATION` | 3 | $475,500 | Same population problem as the deferred-burn family. |
| `SECRET-EMBEDDED-IN-PUBLIC-CODE-AS-AUTH` | 3 | $4,171,100 | Requires bytecode constant analysis per contract; run as a sweep over deep-screened deployments rather than as a ranked pair. |
| `ACC-SIGN-OR-BOUND-CHECK-MISSING` | 3 | $3,064,900 | Detected by parameter-shape sweep over deep-screened deployments. |
| `AUTH-IDENTITY-SATISFIABLE-BY-ATTACKER-CONTRACT` | 3 | $278,700 | Detected by source-grep sweep over deep-screened deployments. |
| `TOKEN-TRANSFER-INTENT-HEURISTIC-FORGEABLE` | 2 | $277,041 | Same population problem as the deferred-burn family. |
| `HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL` | 2 | $630,000 | Applies to token contracts with accrual hooks; only reachable through per-token screening, not the protocol universe. |
| `TOKEN-PACKED-OWNERSHIP-UNDERFLOW` | 2 | $40,000 | Requires DN404/BT404 lineage; no in-universe protocol above the TVL threshold carries it. |
| `METATX-SENDER-IDENTITY-CONFUSION` | 2 | $282,700 | Requires ERC-2771 detection per contract; run as a sweep. |
| `ACC-DUPLICATE-ID-ACCUMULATION` | 2 | $13,021 | Detected by selector-shape sweep over deep-screened deployments. |
| `SIG-VERIFIER-DEFEATABLE` | 2 | $97,819 | Detected by source-grep sweep over deep-screened deployments. |
| `AUTH-ZERO-ADDRESS-ACCEPTED` | 1 | $98,200 | Screened as a cheap read-only sweep (owner()==address(0) with non-zero balance) rather than as a protocol-family pair. |
| `STORAGE-LAYOUT-COLLISION-PHANTOM-CREDIT` | 1 | $25,000 | Requires a storage-layout dump per contract; run as a sweep over deep-screened deployments. |
| `ACC-CREDIT-NOT-RECEIVED` | 1 | $560,000 | Reward-tracker contracts are rarely separate DefiLlama entries; folded into the reward-index sweep. |
| `ACC-HARDCODED-PEG-REDEMPTION` | 1 | $8,500 | Folded into the stablecoin-issuer oracle screen. |
| `AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY` | 1 | $907,700 | Detected by selector sweep over deep-screened deployments. |
