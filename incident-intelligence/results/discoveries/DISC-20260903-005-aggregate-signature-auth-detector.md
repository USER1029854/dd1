# DISC-20260903-005 — What SOFA actually was, the real mechanism, and a code-level detector for it

**This corrects a shallow run.** The `OLD_AUTOMATOR_BATCH` picked protocols by *age + category + revenue*
and called them "forgotten automators." That was metadata sorting, and it could never have found the SOFA
bug — because the SOFA bug had **nothing to do with age**. It was a specific flaw in the *authorization
math* of one function, findable only by **reading the code**. This file re-derives the true mechanism from
the deployed bytecode-bound source, turns it into a **reusable code-level detector**, and reports the
honest result of running that detector across GitHub (including verified-source mirrors).

---

## 1. The real finding (deployed-source, not repo)

Contract: SOFA `Automator` — ARB impl `0x0338c2d1908549f4fcbca9da84039de1bac5c6c1` (Arbiscan-verified;
diffs identical to `sofa-org/sofa-protocol`). The exploited entrypoint, verbatim
(`sources/sofa/mintProducts_deployed_extract.sol`):

```solidity
function mintProducts(ProductMint[] calldata products, bytes calldata signature) external nonReentrant {
    bytes32 signatures;                                   // accumulator = 0
    for (uint256 i = 0; i < products.length; i++) {
        require(vaults[products[i].vault], "Automator: invalid vault");
        IVault(products[i].vault).mint(products[i].totalCollateral, products[i].mintParams, referral);
        ...
        signatures = signatures ^ keccak256(abi.encodePacked(products[i].mintParams.maker,
                                                             products[i].mintParams.makerSignature));
    }
    (address signer, ) = signatures.toEthSignedMessageHash().tryRecover(signature);
    require(makers[signer], "Automator: invalid maker");   // the ONLY trusted-counterparty gate
    ...
}
```

The automator is a **pooled-capital counterparty**: for each product it posts the depositors' collateral
via `IVault.mint(...)`. Four independent defects turn that into a public drain (operator's fork PoC:
**+10,800 USD₮0** from an unwhitelisted outsider):

1. **Permissionless entrypoint.** `mintProducts` has no caller gate.
2. **Per-item counterparty is unchecked.** The child vault verifies each `mintParams.makerSignature`
   matches `mintParams.maker`, but never requires `maker ∈ makers`. Only the **aggregate** `signer` must be
   a whitelisted maker. So every product can carry `maker = attacker`.
3. **The aggregate commitment is XOR** — order-independent and GF(2)-linear, so an attacker can craft a
   basket of their own products whose XOR equals a *target value a real maker already signed*.
4. **The outer signature has no nonce / deadline / consumption** — it is **replayable**. Read any past
   `mintProducts` tx, lift the whitelisted maker's `signature` and its XOR target from calldata, and reuse
   it over the collided basket.

Chain: replay real maker's sig over a GF(2)-collided basket of attacker-maker products → `mintProducts`
passes → attacker rigs each product's economics (`collateralAtRisk≈totalCollateral`, extreme
`anchorPrices`) so the *maker* wins `maxPayoff` → permissionless `settle()` → `burn(isMaker=1)` → withdraws
the pool. **Any one of (1)–(4) fixed closes it** (EIP-712 over the ordered basket hash + per-automator
nonce + deadline, consumed on use; or a per-item `makers[maker]` check).

---

## 2. The real family — `AGGREGATE-OR-REPLAYABLE-SIGNATURE-AUTH-NONBINDING`

> A value-moving **batch/pooled** entrypoint authorizes the whole action with **one signature**, and that
> signature does not actually bind the thing being done. It breaks along four axes; a finding needs the
> pooled-funds context plus **any** of B/C/D:

- **A · Pooled counterparty, permissionless call.** The contract posts *other people's* funds as one side
  of each item, and anyone can call the batch entrypoint.
- **B · Non-binding aggregate.** The signed commitment is an **XOR / sum / unordered-set** of per-item
  hashes (order-independent, collision-craftable) instead of a hash of the *exact ordered basket*.
- **C · Replayable.** The signature carries **no nonce, no deadline, no consumption / domain binding** — a
  past valid signature can be reused.
- **D · Per-item party unauthorized.** Only the *aggregate* signer is trusted; each item's
  counterparty/maker/recipient is attacker-choosable.

This is substrate-general (the same mistake exists in RFQ settlement, DOV/structured-product minting,
batch-claim, and meta-tx relayers). It is **not** an "old contract" or "unused function" property — SOFA's
`mintProducts` was live and current.

---

## 3. The reusable detector (hunt code, not metadata)

**Stage 1 — GitHub / verified-source-mirror code search** (run these exact queries; they cover deployed
code too, via the `smart-contract-sanctuary` and audit-dataset mirrors):

| Indicator | Query | Why |
|---|---|---|
| XOR-accumulated commitment | `"^= keccak256(abi.encodePacked" language:solidity` and `"= signatures ^ keccak256"` | axis B — the rarest, highest-signal tell |
| aggregate-then-recover | `"toEthSignedMessageHash().tryRecover" language:solidity` near a loop | recover over an accumulator |
| trusted-signer-only gate | `"require(makers[signer]" / "isSigner[recovered]"` in a batch fn | axis D |
| maker-signed batch mint | `"makerSignature" "totalCollateral"` / `"mintParams" "maker"` | structured-product family |
| replay-missing | signed struct with **no** `nonce`/`deadline`/`nonces[...]++` in the verify path | axis C |

**Stage 2 — read each hit's deployed source and fill this table** (the finding is any row where the
answer is "no"):

| Question | Look for |
|---|---|
| Is the entrypoint permissionless AND does the contract post pooled funds as counterparty? | external fn, `IVault.mint`/transfer of `address(this)` balance |
| Does the signature bind the **exact ordered** action? | `keccak256(abi.encode(orderedArray))`, **not** XOR/sum |
| Is there replay protection? | `nonce`/`nonces[signer]++`, `deadline`/`block.timestamp` check, EIP-712 domain |
| Is **each item's** counterparty authorized, not just the aggregate signer? | per-item `require(whitelist[item.party])` |

**Stage 3 — falsifiers** (any one shuts the door): EIP-712 hash over the ordered basket; per-automator
nonce consumed on use; per-item party whitelist; caller gate on the entrypoint.

Artifacts: `sources/sofa/automator_flat.sol` (full deployed source), `sources/sofa/mintProducts_deployed_extract.sol`.

---

## 4. The hunt, run — honest result

Ran Stage-1 across all of GitHub (repos **and** verified-source mirrors):

- **`makerSignature` + `totalCollateral`** → **only `sofa-org/sofa-protocol`** (+ ML/audit-dataset copies
  of it: `HelayLiu/AccessControlVulnerabilities`, `shenyimings/FORGE-Curated`, `imranpollob/…`). **No other
  live protocol** implements the maker-signed structured-product automator. The exact sibling does not exist.
- **`signatures = signatures ^ keccak256`** → sofa-protocol + those same dataset mirrors only.
- **`^= keccak256(abi.encodePacked`** (broader XOR-commitment) → 91 hits, all of which are **fingerprints /
  checksums / off-chain roots, not on-chain fund-authorizing signatures**:
  - `decentraland/land` `EstateRegistry.getFingerprint` — XOR of land ids, used in NFT transfer
    fingerprint verification. The canonical "XOR fingerprint is collision-forgeable" case; not fund theft,
    but the same math error, and worth citing as the class's textbook example.
  - `bancorprotocol/airdrop` `AirDropper` — a `crc` checksum. Not auth.
  - `aethelred-foundation/aethelred` `StAETHEL` — a vault maintains `stakerRegistryRoot` by XOR, **but it is
    read only off-chain** (a "Cruzible"/TEE reward verifier); it never gates funds on-chain, and the project
    is experimental/unfunded. Real instance of the *math* error, out of on-chain scope.
  - The remaining hits are `smart-contract-sanctuary` / benchmark corpora mirroring the above.

**Conclusion:** SOFA's fund-authorizing form of this bug was **effectively unique on-chain** at the time —
which matches the operator's own read ("there were no similar bugs anywhere"). The right takeaway is not
"find SOFA clones" (there are none) but to **keep the Stage-1 detector running against newly deployed /
newly upgraded verified source**, because this class is (a) catastrophic, (b) rare, and (c) precisely
grep-detectable — the exact combination a standing code screen should own.

---

## 5. What this corrects

`results/OLD_AUTOMATOR_BATCH.md` (age/category/revenue sort) is **superseded as a lens** for this pattern:
the SOFA bug was not age-related and would not surface in that list by construction. That batch remains a
fine generic "unwatched" coverage list, but the *mechanism* here — replayable / non-binding aggregate
signature authorization on a pooled-counterparty entrypoint, found by reading code — is the real lesson,
and the detector in §3 is how to act on it. It may still be that the next such bug is essentially random;
the detector is the cheapest way to be holding the net when it appears.
