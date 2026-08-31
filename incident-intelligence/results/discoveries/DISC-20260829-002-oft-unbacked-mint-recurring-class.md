# DISC-20260829-002 — The recurring LayerZero-OFT unbacked-mint class, and the config that stops it

**Type:** forward intelligence + standing detector (cross-chain). **Not a re-delivery:** no protocol
named here is a delivered candidate in `_exclusion_set.json`; this synthesizes three 2026 incidents into
one prevention rule and one screen. **Companion to** `DISC-…-001` (the in-scope contract-bug screen).

## The pattern that keeps paying out

Three times in 2026 an attacker seized control of a LayerZero OFT's cross-chain trust and minted tokens
with no backing, then unlocked or sold the real asset. Same *outcome*, three *different enablers*:

| Incident | Enabler | Layer | This audit's scope |
|---|---|---|---|
| KelpDAO rsETH ($292M) | a **single DVN** verified a packet that never existed (DVN-infra compromise) | config + infra | out (infra) — but the **1-of-1 DVN** is an on-chain config choice |
| StakeDAO vsdCRV ($91k) | a **compromised deployer key** reset the OFT **peer** | off-chain key | out (key) — but a **mutable peer/delegate with no timelock** is the on-chain enabler |
| The Sandbox SAND ($675k) | an **unprivileged `approveAndCall`** reached `setDelegate` | contract | **in** — screened in DISC-…-001 |

The three enablers are different; the **standing invariant they each broke is the same**:
*the authority that can redirect an OFT's cross-chain trust must be as hard to seize as the value the
OFT backs.* When it is a single DVN, a single key, or an unprivileged contract call, it is not.

## Why it matters for the operator's band

An OFT's damage is bounded by the backing locked in its adapter, and mid-size project tokens — exactly
the operator's band — routinely ship an OFT with **the LayerZero defaults**: one or two DVNs, a delegate
that is the deployer EOA or a 1-of-1 "owner", and no timelock on `setPeer`/`setDelegate`/`setConfig`.
Those defaults are the KelpDAO and StakeDAO enablers, pre-installed.

## The detector (standing screen, partially built in DISC-…-001)

For every OFT/OApp that backs real value (adapter locks, or mints against a remote lock), read from live
state and flag any of:

1. **Delegate hardness.** Is `delegates[oapp]` an EOA or a 1-of-1 owner, and is `setDelegate` callable
   with no timelock? (KelpDAO/StakeDAO shape.) — read `endpoint.delegates(oapp)` and the owner/roles.
2. **DVN count.** Does the receive-config require **≥2 independent DVNs**, or a single one? (KelpDAO
   shape.) — read the OApp's receive `UlnConfig` on the endpoint.
3. **Unprivileged config reach.** Does the token layer expose any unprivileged arbitrary-call
   (`approveAndCall`/`paidCall`/`execute`/`multicall`) that can reach `setDelegate`/`setPeer`? (SAND
   shape.) — **this sub-screen is DISC-…-001**, and on Base it returned zero live un-hit instances.

A candidate is any value-backing OFT failing (1) or (2), or any OApp matching (3). The severity is the
adapter's locked balance, read at head.

## What was and wasn't done here

- **(3) is executed** across 3,453 Base + (partial) 4,947 Ethereum OApps in DISC-…-001 — the only one of
  the three that is a pure contract bug, and it is **clean/contained** on the fully-covered chain.
- **(1) and (2) are specified, not yet run at population scale.** They require reading each OApp's
  `delegates(...)` and receive-`UlnConfig` from the endpoint — a bounded next screen on the same
  enumerated population (`sources/lz_screen/oapps_*.json`). They are the highest-value continuation
  because they are where the **$292M** actually left, and because they land inside the operator's band.
- **Honest scope line:** (1) and (2) describe a **key-/infra-compromise attack surface**, which this
  audit's mandate excludes as *root causes*. They are included because the **mitigation is on-chain and
  permissionless to verify** (DVN count, delegate immutability), so the screen is a legitimate on-chain
  prevention check even though the trigger is off-chain. Findings from (1)/(2) must be labelled that way,
  never as permissionless-theft.

## Decisive check / falsifier

- Run (1)+(2) over `sources/lz_screen/oapps_*.json`; a value-backing OFT with a single DVN **and** a
  mutable non-timelocked delegate is the highest-urgency row (both KelpDAO and StakeDAO enablers present).
- Falsifier for any row: the delegate is a timelocked multisig **and** the receive-config requires ≥2
  independent DVNs — then neither the SAND, KelpDAO, nor StakeDAO path is open.

## Evidence / provenance

- Root-cause table sourced from public post-mortems (KelpDAO 2026-04-18; StakeDAO 2026-05-27; SAND
  2026-08-21); the SAND contract mechanism is verified on-chain in run 2 (`sources/sandbox/`).
- OApp populations already enumerated in `sources/lz_screen/`.
