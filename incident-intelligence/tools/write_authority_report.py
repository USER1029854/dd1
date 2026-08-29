#!/usr/bin/env python3
"""Custody-exposure report: who can replace the code, and how many keys it takes.

Deliberately independent of the family model. A family match answers "could this
code be made to misbehave"; this answers "how many signatures stand between the
funds and a replaced implementation". The two are scored separately on purpose --
an off-chain key compromise is an EXCLUDED root cause under the run's inclusion
gate, so it must never inflate a code-defect likelihood. It is reported here
instead, because for a small independent reviewer it is the single most useful
and most fixable thing to hand a team.

Everything below is public chain state. Nothing identifies a key holder.
"""
import json,sys,os,collections
sys.path.insert(0,'/home/user/dd1/incident-intelligence/tools')
B='/home/user/dd1/incident-intelligence'
AD=json.load(open(f'{B}/protocols/admin_posture.json'))
BS={r['slug']:r for r in json.load(open(f'{B}/protocols/band_screen.json'))}
E={r['slug']:r for r in json.load(open(f'{B}/protocols/eligibility.json'))}
PR=json.load(open(f'{B}/protocols/onchain_probes.json'))

SINGLE={'EOA_SINGLE_KEY','SAFE_1_OF_N'}
DESC={'EOA_SINGLE_KEY':'one externally-owned account — a single private key',
      'SAFE_1_OF_N':'a Safe with threshold 1 — any one of its signers acts alone',
      'TIMELOCK_ZERO_DELAY':'a timelock configured with zero delay — no warning window',
      'SAFE_M_OF_N':'a Safe requiring several signatures',
      'TIMELOCK':'a timelock with a real delay','GOVERNOR':'an on-chain governor',
      'UNKNOWN_CONTRACT':'a contract this run could not fingerprint',
      'NONE_FOUND':'no authority slot or owner() was exposed'}

RANK={'EOA_SINGLE_KEY':0,'SAFE_1_OF_N':1,'TIMELOCK_ZERO_DELAY':2,'UNKNOWN_CONTRACT':3,
      'SAFE_M_OF_N':4,'TIMELOCK':5,'GOVERNOR':6,'NONE_FOUND':7}

def seed_provenance(slug):
    """Which seed addresses came from an ERC-1967 admin slot (a genuine upgrade
    authority) rather than from a plain owner() (a privileged role, not upgrade)."""
    adm=set(); own=set()
    for a in (PR.get(slug,{}).get('deployment',{}).get('addresses_probed') or []):
        x=a.get('erc1967_admin')
        if isinstance(x,str) and x.startswith('0x'): adm.add(x.lower())
        y=a.get('owner')
        if isinstance(y,str) and y.startswith('0x'): own.add(y.lower())
    return adm,own

rows=[]
for slug,rec in AD.items():
    b=BS.get(slug)
    if not b or b['band_status']=='ABOVE_BAND_DROPPED': continue
    tvl=b['tvl']
    if tvl<50_000: continue
    adm,own=seed_provenance(slug)
    auths=rec.get('authorities') or {}
    # Terminal authority reached specifically from an upgrade-admin slot. This is the
    # only chain that can actually replace an implementation; an owner() that happens
    # to be an EOA is a privileged role, which is a different and lesser claim.
    def terminal_of(root):
        hops=auths[root].get('hops') or []
        real=[h for h in hops if h['posture']!='UNKNOWN_CONTRACT'] or hops
        return real[-1] if real else None
    upg_terms=[terminal_of(r) for r in auths if r.lower() in adm]
    upg_terms=[t for t in upg_terms if t]
    upg_post=min((t['posture'] for t in upg_terms),key=lambda x:RANK.get(x,9)) if upg_terms else None
    post=rec.get('posture'); d=rec.get('posture_detail') or {}
    rows.append({"slug":slug,"name":E.get(slug,{}).get('name',slug),"tvl":tvl,"posture":post,
      "upgrade_authority_posture":upg_post,
      "has_proxy":any(a.get('is_proxy') for a in (PR.get(slug,{}).get('deployment',{}).get('addresses_probed') or [])),
      "threshold":d.get('threshold'),"signers":d.get('signers'),
      "delay_seconds":d.get('delay_seconds'),"authority":d.get('address'),
      "band":b['band_status'],"hops":d.get('hop'),"chain":next((v['chain'] for v in auths.values()
          if any(h['address']==d.get('address') for h in (v.get('hops') or []))),None),
      "category":E.get(slug,{}).get('_cat'),"url":E.get(slug,{}).get('_defillama_url')})
json.dump(rows,open(f'{B}/protocols/authority_exposure.json','w'),indent=1)

# Restricted to IN_BAND. Above-band protocols kept for explicit danger are excluded here
# because attributing protocol-wide TVL to one privileged role is exactly the misreading
# this table has to avoid -- see the worked example in "Limits" below.
sing=[r for r in rows if r['posture'] in SINGLE and r['band']=='IN_BAND'
      and r['upgrade_authority_posture'] not in SINGLE]
sing_upg=[r for r in rows if r['upgrade_authority_posture'] in SINGLE]
sing.sort(key=lambda r:-r['tvl']); sing_upg.sort(key=lambda r:-r['tvl'])
cnt=collections.Counter(r['posture'] for r in rows)

L=["# Custody exposure — who can replace the code\n",
"> **This is not a vulnerability report.** Nothing here says any protocol is exploitable, and nothing "
"here is an attack instruction. Every value below is public chain state, read with `eth_call` and "
"`eth_getCode`. A single-key authority is a *design posture*, not a defect: plenty of small teams run "
"one deliberately. It is listed because it is the cheapest thing in DeFi to fix and the most expensive "
"to get wrong.\n",
"**Why this is scored separately from everything else in this run.** An off-chain key compromise is an "
"excluded root cause under the inclusion gate (§6), so it may not inflate a code-defect likelihood "
"score. It is also the amplifier that decides what a code defect *costs*. Keeping the two apart is the "
"only way to avoid one quietly contaminating the other.\n",
"## Method\n",
"For every address probed, the ERC-1967 admin slot and `owner()` were read, then the authority chain was "
"walked up to three hops — a proxy's admin is usually an OpenZeppelin `ProxyAdmin` whose own `owner()` is "
"the real authority, which is in turn often a Safe or a timelock. The **terminal** authority is "
"fingerprinted by the functions it answers: `getThreshold()` + `getOwners()` for a Safe, `getMinDelay()` "
"or `delay()`+`GRACE_PERIOD()` for a timelock, `votingDelay()` for a governor, zero code size for an "
"externally-owned account. A protocol is reported at its **weakest** terminal authority, because that is "
"the one a defender has to plan around.\n",
"## Distribution across %d in-band protocols with a readable authority\n" % len(rows),
"| Terminal authority | Protocols | Meaning |","|---|---:|---|"]
for k,n in cnt.most_common():
    L.append("| `%s` | %d | %s |" % (k,n,DESC.get(k,'')))
L.append("")
L.append("## Single-signature authority over an upgradeable deployment\n")
L.append("The sharpest subset, and the only one that can actually replace code: the chain walked here starts "
         "at an **ERC-1967 admin slot**, not at a plain `owner()`, and it terminates in one key or one "
         "signature. Total at stake below: **$%s** across **%d** protocols.\n"
         % (f"{sum(r['tvl'] for r in sing_upg):,.0f}",len(sing_upg)))
L.append("| # | Protocol | Category | Value at risk | Terminal authority | Hops | Chain |")
L.append("|---:|---|---|---:|---|---:|---|")
for i,r in enumerate(sing_upg[:60],1):
    L.append("| %d | [%s](%s) | %s | $%s | `%s` | %s | %s |" % (i,r['name'],r['url'],r['category'] or '',
             f"{r['tvl']:,.0f}",r['posture'],r['hops'],r['chain'] or ''))
L.append("")
L.append("## Single-signature *privileged role*, no upgrade path proven\n")
L.append("A weaker and much noisier claim than the table above, kept separate for that reason: somewhere in "
         "the protocol a single key answers `owner()` — on a pool, an oracle setter, a fee recipient, a "
         "treasury — but no ERC-1967 admin chain terminating in that key was proven, so this is a privileged "
         "role, **not** an upgrade path. The money column is the protocol's whole TVL, and **most of it is "
         "usually not behind this key**. Read it as a pointer to a contract worth opening, nothing more. "
         "%d protocols.\n" % len(sing))
L.append("| # | Protocol | Protocol TVL (not all behind this key) | Weakest terminal authority | Proxy present |")
L.append("|---:|---|---:|---|---|")
for i,r in enumerate(sing[:60],1):
    L.append("| %d | [%s](%s) | $%s | `%s` | %s |" % (i,r['name'],r['url'],f"{r['tvl']:,.0f}",
             r['posture'],"yes" if r['has_proxy'] else "no"))
L.append("")
zd=[r for r in rows if r['posture']=='TIMELOCK_ZERO_DELAY']
if zd:
    L.append("## Timelocks configured with zero delay\n")
    L.append("A timelock with `delay == 0` executes immediately. The contract is present, so tooling and "
             "dashboards report the protocol as timelocked; the warning window it exists to provide is not "
             "there. This is worth a message to the team on its own.\n")
    L.append("| Protocol | Value at risk | Authority |"); L.append("|---|---:|---|")
    for r in sorted(zd,key=lambda x:-x['tvl']):
        L.append("| [%s](%s) | $%s | `%s` |" % (r['name'],r['url'],f"{r['tvl']:,.0f}",r['authority']))
    L.append("")
L.append("## What to do with this\n")
L.append("For any protocol above, the defensive ask is small, specific and free: move the terminal authority "
         "behind a multi-signature account with a threshold above one, and put a non-zero delay in front of "
         "upgrades so that a replacement can be seen before it lands. That is a configuration change, not a "
         "rewrite, and it is the kind of report a small team will usually act on.\n")
L.append("## Limits of this measurement\n")
L.append("- **Worked example of the second table's limitation.** Curve DEX resolves to `EOA_SINGLE_KEY` "
         "under weakest-link semantics, because one pool among many answers `owner()` with an externally-owned "
         "account. Curve's actual protocol authority is DAO-governed and nothing here contradicts that. The "
         "protocol-wide TVL figure is therefore not the amount behind that key, which is why the second table "
         "is restricted to in-band protocols and its money column is labelled as protocol TVL. The first table "
         "does not have this problem: it only counts chains that begin at an ERC-1967 admin slot.\n"
         "- Only addresses this run already probed were walked. A privileged role held by an address never "
         "surfaced in a TVL adapter is invisible here.\n"
         "- `UNKNOWN_CONTRACT` means the fingerprint did not match, not that the authority is safe. Some are "
         "custom governance; some are Safes behind a non-standard proxy.\n"
         "- A Safe's threshold is read now; signer sets change.\n"
         "- Role-based access (`AccessControl`) is not enumerated — a protocol reading as `NONE_FOUND` may "
         "still have privileged roles granted to single keys.\n"
         "- Posture is read today, so a team that hardened after an incident reads as hardened. That biases "
         "every measurement here toward understating exposure, never overstating it.\n")
open(f'{B}/results/upgrade_authority_exposure.md','w').write("\n".join(L))
print(json.dumps({"protocols_with_readable_authority":len(rows),"by_posture":dict(cnt),
 "single_signature_any_role":len(sing),"single_signature_upgrade_authority":len(sing_upg),
 "protocols_with_admin_slot_chain":sum(1 for r in rows if r['upgrade_authority_posture']),
 "tvl_single_sig_upgradeable":round(sum(r['tvl'] for r in sing_upg),2),
 "tvl_single_sig_total":round(sum(r['tvl'] for r in sing),2),
 "zero_delay_timelocks":len(zd)},indent=2))
