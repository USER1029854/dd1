# DISC-20260829-001 — LayerZero OApp unprivileged-arbitrary-call → delegate-hijack screen

**Type:** population screen (EVM), executed. **Origin incident:** The Sandbox SAND OFT, 2026-08-21.
**Pinned:** Base `#50596624`, ETH `#25858924`. **Chain access:** read-only.
**Dedup:** the two candidate contracts named below (`itETH`, `RZR`/`lstRZR` adapters) are **not** in
`_exclusion_set.json` (805 names across all prior pushes); SAND appears only as a run-2 *incident*
(evidence), never as a delivered candidate. This screen and its result are new.

## Why this screen exists

The SAND bridge exploit is the **third LayerZero OFT unbacked-mint event of 2026**, but the three have
*different root causes*, and only one is in this audit's scope:

| Incident | Date | Loss | Root cause | In scope here? |
|---|---|---:|---|---|
| KelpDAO rsETH | 2026-04-18 | ~$292M | LayerZero **DVN-infrastructure** compromise + single-DVN config | **No** (infra) |
| StakeDAO vsdCRV | 2026-05-27 | ~$91k realized | **Compromised deployer key** reset the OFT peer | **No** (off-chain key) |
| **The Sandbox SAND** | **2026-08-21** | **~$675k realized** | **On-chain contract bug:** an *unprivileged* `approveAndCall` on the OFT reached `endpoint.setDelegate(attacker)` | **Yes** (contract) |

The class — *seize an OFT's LayerZero config, then mint unbacked and unlock the backing* — has put
**$300M+** at risk in six months. The one instance a code screen can catch **before** the fact is the
SAND shape: a smart-contract path that lets an outsider take the OApp's delegate. This discovery builds
that exact detector and runs it across the live OApp population.

## The mechanism (verified on SAND — see run-2 evidence `sources/sandbox/`)

`OFTSand` inherits `ERC20BasicApproveExtension`: `approveAndCall(target,amount,data)` / `paidCall(...)`
perform **`target.call(data)` from the token's own context**, guarded only by
`doFirstParamEqualsAddress(data, msg.sender)`. That guard stops a spoofed `transferFrom`, but not
`endpoint.setDelegate(attacker)` — the attacker's own address legitimately *is* the first param. Because
`EndpointV2.setDelegate` keys the delegate by `msg.sender` (the OApp), the OApp sets the attacker as its
own delegate → malicious DVN / receive-library → forged inbound mint → unlock adapter backing.

**Generalized precondition:** a contract that (a) is a LayerZero OApp (`endpoint()` + `peers()`) and
(b) exposes an **unprivileged** method doing an **arbitrary-target `call` with attacker-chosen calldata**
(`approveAndCall` / `paidCall` / `execute(address,bytes)` / `functionCall` / arbitrary `multicall`).

## The detector, and how it was run

1. **Enumerate the OApp population** from every `DelegateSet(sender,delegate)` log emitted by the
   canonical EndpointV2 (`0x1a44076050125825900e736c501f859c50fe728c`). Base via Blockscout, Ethereum
   via Etherscan V2. → **Base 3,453 OApps; Ethereum 4,947 OApps.**
   (`sources/lz_screen/oapps_base.json`, `oapps_mainnet.json`.)
2. **Screen each contract's runtime bytecode** for the arbitrary-call selectors
   (`approveAndCall` `0xcae9ca51`, `paidCall` `0xbb1e23cb`, `execute(address,bytes)` `0x1cff79cd`,
   `execute(address,uint256,bytes)` `0xb61d27f6`, `functionCall` `0xa0b5ffb0`,
   `transferAndCall` `0x4000aea0`). (`tools/lz_code_fast.py`, results in `sources/lz_screen/*_screen_result.json`.)
3. **Read the source of every hit** and classify the guard on the arbitrary-call method, and confirm
   OApp status.

**Screen validation:** SAND (`0xac531Eb2…`) is present in the Base enumeration and its bytecode carries
`approveAndCall` + `paidCall` + `setDelegate` — the detector flags the known positive.

## Result

**Base — fully covered (3,453 / 3,453).** Three hits, all dispositioned:

| OApp | Name | Method | Guard | Disposition |
|---|---|---|---|---|
| `0xac531Eb2…9002DcF` | OFTSand (SAND) | `approveAndCall`,`paidCall` | **unprivileged** | the exploited contract; **contained** (all `peers` zeroed, delegate = multisig) |
| `0xf17926de…54c83` | itETH | `execute(address,bytes)` | `onlyRole(DEFAULT_ADMIN_ROLE)` | **admin-gated**, and **dormant** (`totalSupply == 0`, no backing) |
| `0xbd880531…36c0d` | itETH | `execute(address,bytes)` | `onlyRole(DEFAULT_ADMIN_ROLE)` | **admin-gated**, dormant |

**Ethereum — coverage 4,762 / 4,947 (96%).** Two hits: the `RZROFTAdapter` (`0xe97493f0…`) and
`lstRZROFTAdapter` (`0xd3e53663…`), both `execute(address,bytes)` guarded by `onlyGovernor` —
**admin-gated**. The RZR adapter locks ~172,034 RZR (~$106k at head) that its governor's `execute` could
move; that is a centralization/admin hazard, **not** an unprivileged theft path. No unprivileged
arbitrary-call OApp in the covered set.

## Verdict

**On the fully-covered Base population there is no live, un-hit OApp with an unprivileged arbitrary-call
path to `setDelegate` — the SAND-class is closed except SAND itself, which is contained.** Every other
arbitrary-call surface found is **admin-gated** (`onlyRole`/`onlyGovernor`). Admin-gated `execute` on an
OFT is a real centralization/backing-drain hazard, but it is **out of this audit's theft scope**
(a privileged party misusing non-acquirable power, or an off-chain key compromise — the StakeDAO shape),
so it is recorded here as context, not as a finding.

This is a **clean negative, and a useful one**: it says the next SAND-style hijack has **no currently-live
un-hit instance** on the two screened chains, and it leaves behind the exact mechanical detector to keep
running as new OFTs deploy. The screen would have flagged SAND before the fact.

## Decisive check / falsifier / residual

- **A live positive** would be an OApp with an **unprivileged** arbitrary-calldata method (no
  `onlyOwner`/`onlyRole`/`onlyGovernor` on the call path) **and** real backing in its OFT adapter. None
  found on Base; none in the covered Ethereum set.
- **Residual (honest gaps):** (1) **Ethereum coverage is 4,762/4,947** — finish it to close the
  mainnet claim (rate-limited free RPC; the cache resumes). (2) **BNB Chain unscreened** — nodereal quota
  exhausted; SAND was also exploited there, so BNB is the highest-value next chain. (3) **Arbitrum,
  Optimism, Polygon and other OFT chains unscreened.** (4) The bytecode-selector filter can miss a method
  whose selector is constructed dynamically; positives are always source-confirmed, but a byte-absent
  negative should be confirmed by ABI where a contract is unverified.
- **Standing action:** add this detector (OApp ∩ unprivileged arbitrary-call) to the recurring screen so
  any *newly deployed* OFT with the SAND shape is caught at deploy time.

## Evidence on disk

- `sources/lz_screen/oapps_base.json`, `oapps_mainnet.json` — enumerated OApp populations
- `sources/lz_screen/base_screen_result.json`, `mainnet_screen_result.json` — screen output + hits
- `sources/lz_screen/hit_f179_src.sol` — itETH source (admin-gated `execute`)
- `sources/rzr/rzr_adapter_flat.sol` — RZR adapter source (`onlyGovernor execute`)
- `sources/sandbox/` — the SAND mechanism this detector is built from (run 2)
- `tools/lz_oapp_screen.py`, `tools/lz_base_enum.py`, `tools/lz_code_fast.py` — enumeration + screen
