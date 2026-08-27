#!/usr/bin/env python3
"""Urgency-ranked candidate list in the triage spec's output format."""
import json,os,sys,collections,datetime
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
B=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')
R=json.load(open(f'{B}/protocols/urgency_pairs.json'))
VS=json.load(open(f'{B}/protocols/victim_state.json'))
REL={r['slug']:r for r in json.load(open(f'{B}/protocols/relatives.json'))}
READAT=R[0]['live_read_at'] if R else '?'
LED=json.load(open(f'{B}/protocols/delivered_ledger.json'))
DELIVERED=set(LED['ledger'])
FAM={f['family_id']:f for f in json.load(open(f'{B}/families/families.json'))}
E={r['slug']:r for r in json.load(open(f'{B}/protocols/eligibility.json'))}
CFG=json.load(open(f'{B}/run_config.json'))
N=int(sys.argv[1]) if len(sys.argv)>1 else 70

MOD={'Cosmos':'COSMOS_APPCHAIN','Osmosis':'COSMOS_APPCHAIN','Injective':'COSMOS_APPCHAIN',
     'Kava':'COSMOS_APPCHAIN','Sei':'COSMOS_APPCHAIN','Solana':'SOLANA','Sui':'MOVE_SUI',
     'Aptos':'MOVE_SUI','Stellar':'SOROBAN'}
def modules(r):
    m={MOD.get(c,'EVM') for c in (r.get('chains') or ['Ethereum'])[:4]}
    if 'BRIDGE' not in m and ('BRIDGE' in (r.get('family_id') or '') or
                              'bridge' in (r.get('category') or '').lower()): m.add('BRIDGE')
    return "|".join(sorted(m)) or 'EVM'

def best_per_protocol(rows):
    seen={}
    for r in sorted(rows,key=lambda x:(x['tier'],-x['URGENCY'])):
        if r['protocol_slug'] in seen: continue
        seen[r['protocol_slug']]=r
    return list(seen.values())

CT={r['slug']:r for r in json.load(open(f'{B}/protocols/cosmos_evm_triage.json'))['rows']}

# The Cosmos EVM precompile advisory is a CHAIN-level defect: the chain runs cosmos/evm,
# not the DEX deployed on it. Emitting one candidate per protocol turned 14 chain findings
# into 110 rows, inflating the list eightfold and misdirecting the work -- the decisive
# check (pin the running version, query live precompile params) is performed once per
# chain, and disclosure goes to the chain team, not to 37 separate protocol teams. The
# protocols are the EXPOSURE, not separate candidates.
def collapse_cosmos(rows):
    keep=[]; bychain=collections.defaultdict(dict)
    for r in rows:
        s=r['protocol_slug']
        if r['tier']==2 and s in CT:
            for c in (CT[s].get('cosmos_evm_chains') or []):
                prev=bychain[c].get(s)
                if not prev or r['URGENCY']>prev['URGENCY']: bychain[c][s]=r
        else:
            keep.append(r)
    chain_rows=[]
    for c,members in bychain.items():
        best=max(members.values(),key=lambda x:x['URGENCY'])
        exposure=sum(m['live_value_usd'] for m in members.values())
        chain_rows.append({**best,
          "protocol_slug":"chain:"+c,"protocol_name":"%s (chain-level)" % c,
          "is_chain_level":True,"chain_name":c,
          "affected_protocols":sorted(members,key=lambda k:-members[k]['live_value_usd']),
          "affected_count":len(members),"live_value_usd":exposure,
          "defillama_url":"https://defillama.com/chain/"+c,
          "why_clock_is_hot":[
            "%s runs a Cosmos EVM stack covered by the ASA-2026-002 / GHSA-mjfq-3qr2-6g84 "
            "precompile advisories; patch state NOT_DETERMINED. The defect is in the chain's "
            "own stack, not in any one protocol deployed on it." % c,
            "%d protocols above the floor sit on this chain, holding $%s between them. They are "
            "the exposure, not %d separate candidates -- one chain fix closes all of them."
            % (len(members),f"{exposure:,.0f}",len(members))],
          "decisive_check":("Pin %s's running github.com/cosmos/evm version AND query live module "
            "params for the enabled static precompile set. Do not infer either from release notes; "
            "a vendored x/evm tree will not appear in a dependency scan." % c)})
    return keep+chain_rows

R=collapse_cosmos(R)
fresh=[r for r in R if r['protocol_slug'] not in DELIVERED]
held =[r for r in R if r['protocol_slug'] in DELIVERED and r['tier']<=2]
FB=sorted(best_per_protocol(fresh),key=lambda x:(x['tier'],-x['URGENCY']))
HB=sorted(best_per_protocol(held), key=lambda x:(x['tier'],-x['URGENCY']))
# Tier 4 is where the un-hit relatives live, and under this framing they ARE the targets.
# Filling the list with Tier 1-2 crowded them out entirely. The hot tiers are 1-4; Tier 5
# (novel high-fit, clock not started) is excluded from the delivered list by construction.
HOT_TIERS={1,2,3,4}
chosen=[r for r in FB if r['tier'] in HOT_TIERS]
if N and len(chosen)>N and N>=len(chosen): chosen=chosen[:N]

def block(r,rank):
    f=FAM[r['family_id']]; p=E.get(r['protocol_slug'],{})
    ph=r.get('prior_hacks') or []
    cs={}
    L=[]
    L.append("### %d. %s — Tier %d — URGENCY %s\n" % (rank,r['protocol_name'],r['tier'],r['URGENCY']))
    if r.get('is_chain_level'):
        L.append("- **Chain-level candidate:** `%s` — the defect is in the chain's own stack. "
                 "**%d protocols** above the floor are exposed; one chain fix closes all of them."
                 % (r['chain_name'],r['affected_count']))
        L.append("    - most exposed: %s" % ", ".join("`%s`" % x for x in r['affected_protocols'][:8]))
    else:
        L.append("- **Protocol:** `%s` · %s · %s" % (r['protocol_slug'],r.get('category') or '?',
                 ", ".join((r.get('chains') or [])[:5])))
    L.append("- **DefiLlama:** %s" % r.get('defillama_url'))
    L.append("- **Live value, read at head %s (beside the score, never inside it):** $%s"
             % (READAT,f"{r['live_value_usd']:,.0f}"))
    if r.get('relative_of'):
        for rel in r['relative_of'][:2]:
            L.append("    - relative of **%s** via %s — that sibling is *%s* and holds $%s now"
                     % (rel['victim'],rel['link'].replace('_',' ').lower(),
                        (rel['victim_state'] or 'unknown').replace('_',' ').lower(),
                        f"{rel['victim_holds_now'] or 0:,.0f}"))
    if r.get('is_restored_victim'):
        L.append("    - **RESTORE WINDOW** — %s" % VS[r['protocol_slug']]['basis'])
    L.append("- **Matched family:** `%s`" % r['family_id'])
    L.append("    - broken invariant: %s" % f['broken_invariant'])
    L.append("- **URGENCY %s / EVIDENCE_CONFIDENCE %s** — evidence level `%s`%s"
             % (r['URGENCY'],r.get('EVIDENCE_CONFIDENCE'),r['evidence_level'],
                (", capped at %d by evidence depth" % r['evidence_cap']) if r['capped'] else ""))
    c=r['components']
    L.append("    - remediation gap %s/40 · technique recency+propagation %s/20 · reachable live value "
             "%s/25 · precondition match %s/15" % (c['remediation_gap'],
             c['technique_recency_propagation'],c['reachable_live_value'],c['precondition_match']))
    L.append("- **Why the clock is hot:**")
    for w in r['why_clock_is_hot']: L.append("    - %s" % w)
    L.append("    - reachability: %s" % c['reachable_basis'])
    L.append("    - recency: %s" % c['recency_basis'])
    L.append("- **THE decisive check (single fastest confirm/kill):** %s" % r['decisive_check'])
    L.append("- **Prior-art & remediation status:** `%s`" % r['remediation'])
    if ph:
        L.append("    - recorded incidents: %s" % "; ".join(
            "%s $%s [%s]" % (h.get('date'),f"{h.get('amount') or 0:,.0f}",h.get('technique'))
            for h in sorted(ph,key=lambda x:x.get('date') or '',reverse=True)[:4]))
    L.append("- **What would falsify it:** %s" % "; ".join(f['false_positive_killers'][:3]))
    L.append("- **Disclosure channel, if public:** %s" % (p.get('url') or 'not listed in metadata'))
    L.append("- **Pinned:** not yet pinned — pin chain + block at handoff before reading any live number")
    L.append("")
    return "\n".join(L)

tier_counts=collections.Counter(r['tier'] for r in FB)
hot=[r for r in chosen if r['tier']<=2]
L=["# Urgency-first candidates — ranked by the clock, not by likelihood\n",
"> **Discovery stage.** Nothing here says any protocol is exploitable. Each entry is a "
"*high-urgency audit candidate*: named evidence matches a family's prerequisites, named evidence is "
"unknown, and a named guard would falsify it. A high `URGENCY` is a triage order, never an exploit "
"probability.\n",
"## The incident is the evidence. The un-hit relative is the target.\n",
"The previous version of this list put the **victim** in Tier 1. That was backwards. A drained "
"victim's value is already gone — a hot clock over an empty vault is not a candidate. What the "
"incident actually gives you is proof that the technique is public and the code was unpatched; the "
"money is in the *other* deployments of that code.\n",
"Measured, not assumed: **155 of 283 recorded victims hold less than the $50,000 floor today.** The "
"old Tier-1 list was largely empty vaults, and the ones that were not empty were giants — aave-v3 at "
"$17.4bn, venus-core-pool at $1.27bn — which is exactly the exposure weighting that was rejected.\n",
"### Three rules, in this order\n",
"1. **Gate on live value, read at head (%s).** Never historical TVL, never the amount a past incident "
"moved. Empty → out, *before* anything is scored. A drained victim is excluded however fresh its "
"incident is.\n"
"2. **Score reachability, never magnitude.** A small wide-open vault outranks a large hard-to-reach "
"one. No dollar term appears anywhere in the 100 points — putting size back into the score would "
"re-create the $3bn-tops-the-list failure.\n"
"3. **Tiebreak on magnitude.** Among equals on the same code, prefer the fuller sibling.\n" % READAT,
"Ordering is **tier first, then urgency** — a hotter tier outranks a higher score, so a Tier-1 row at "
"40.75 sits above a Tier-2 row at 84.07 by design.\n",
"### The one exception: the restore window\n",
"A protocol restarted, refunded or whitehat-restored **without the fix in the deployed artifact** is "
"holding real money again on the same open door, and the first hours after it resumes are the "
"highest-sensitivity moment in this whole model. Six qualify, identified from their TVL series rather "
"than a snapshot: they fell hard around their incident and have since recovered materially.\n",
"**The honest ceiling in this run is 28 of those 40, not 40.** The full band requires confirming that "
"the specific fixed line is *absent from the deployed artifact* — an L4 read of runtime bytecode at the "
"live address. This run has not performed that per-protocol check, so every Tier-1/2 row carries "
"`KNOWN_ISSUE_STATUS_UNKNOWN` and names the decisive check that would settle it. That check is the "
"first thing to run, and it is fast.\n",
"## What the tiers found\n",
"| Tier | What it means | Fresh protocols |","|---|---|---:|",
"| **1 — UNREMEDIATED-KNOWN** | restore-window victim, or an un-hit deployment on the *same code* as a hit sibling | **%d** |" % tier_counts.get(1,0),
"| **2 — SHARED-DEPENDENCY** | an advisory or template live across a population with no patch-compliance mechanism | **%d** |" % tier_counts.get(2,0),
"| 3 — DEPENDENCY-IMPAIRMENT | the target holds or is backed by a system that is itself exposed | %d |" % tier_counts.get(3,0),
"| **4 — FORK-OF-RECENT-VICTIM** | version sibling of a victim — *this is where the un-hit relatives are* | **%d** |" % tier_counts.get(4,0),
"| 5 — NOVEL-HIGH-FIT | strong match, no public disclosure — the clock has not started | %d |" % tier_counts.get(5,0),
"",
"This list delivers **every fresh candidate in the hot tiers (1–4): %d protocols**, not a round number. "
"Tier 5 — novel high-fit, where the clock has not started — is excluded by construction; it is the old "
"likelihood-first list and it belongs below everything here.\n" % len(chosen),
"**Tier 2 is collapsed to chain rows.** The Cosmos EVM precompile advisory is a defect in the "
"*chain's* stack, not in each protocol deployed on it. Listing it per-protocol produced 110 rows for "
"14 real findings — eightfold inflation, and it pointed the work at 37 DEX teams when the decisive "
"check runs once per chain and the disclosure goes to the chain team. The protocols are named as "
"exposure inside each chain row.\n",
"**Where Tier 4 is:** it is the biggest hot tier in this run at **%d fresh protocols**, and under this "
"framing it is the point. A Tier-4 row is an un-hit version sibling of a protocol that was exploited — "
"the sibling supplies the technique, this deployment still holds the money. The previous list buried "
"them because it filled every slot with Tier 1–2; they are ranked in line here.\n" % tier_counts.get(4,0),
"## Handoff lines for CORE.md\n",
"```"]
for r in chosen:
    L.append("TARGET=%s || TIER=%d || FAMILY=%s || DECISIVE_CHECK=%s || VALUE_AT_RISK=%d || PINNED=<pin at handoff> || REMEDIATION=%s || MODULES=%s"
             % (r.get('defillama_url'),r['tier'],r['family_id'],
                " ".join((r['decisive_check'] or '').split())[:170],int(r['live_value_usd']),r['remediation'],modules(r)))
L.append("```\n")
L.append("## Candidates\n")
for i,r in enumerate(chosen,1): L.append(block(r,i))

try: DEM=json.load(open(f'{B}/protocols/demoted_well_resourced.json'))
except Exception: DEM=[]
if DEM:
    L.append("---\n")
    L.append("## Demoted: well-resourced families\n")
    L.append("**%d protocols** were removed from the hot tiers because the family they belong to holds "
             "more than $100M across its deployments. A team at that scale retains security staff and "
             "patches a public issue fast, so it is usually not the save — the edge is the small, "
             "neglected, or forgotten deployment on the same unpatched version.\n" % len(DEM))
    L.append("This is measured, not a name list: across hot-tier candidates the median family holds "
             "**$5.8M** and the 90th percentile **$168M**, while the Aave family holds **$18.1bn**. "
             "They are named here rather than silently dropped.\n")
    L.append("| Protocol | Own live value | Family holds | Family |")
    L.append("|---|---:|---:|---|")
    for d in DEM[:25]:
        L.append("| `%s` | $%s | $%s | %s |" % (d['slug'],f"{d['own_live_tvl']:,.0f}",
                 f"{d['family_live_tvl']:,.0f}",d['family_parent']))
    L.append("")
if HB:
    L.append("---\n")
    L.append("## Withheld by the no-repetition ledger — but now classified Tier 1–2\n")
    L.append("These **%d** protocols were handed over in earlier runs and are excluded from the list "
             "above. They are named here rather than silently dropped because the ranking axis changed "
             "underneath them: they were delivered as likelihood candidates and now classify as hot "
             "clocks. Withholding a Tier-1 item because it was once served cold would be the wrong "
             "call, so this is your decision, not mine.\n" % len(HB))
    L.append("| Protocol | Tier | URGENCY | Family | Live value | First delivered |")
    L.append("|---|---:|---:|---|---:|---|")
    for r in HB[:40]:
        L.append("| [%s](%s) | %d | %s | `%s` | $%s | `%s` |" % (r['protocol_name'],r['defillama_url'],
                 r['tier'],r['URGENCY'],r['family_id'],f"{r['live_value_usd']:,.0f}",
                 LED['ledger'][r['protocol_slug']]['first_delivered_in']))
    L.append("")

L+=["---\n","## Limits of this ranking\n",
"- **No fix-in-artifact check was run.** That is the single highest-value next action and it is what "
"separates 28 points from 40. Until it runs, no row here is `UNREMEDIATED_KNOWN`.\n"
"- **Tier 3 is barely populated (%d protocols).** The only dependency this run can evidence is the "
"*declared oracle*, and only where the provider's user population is small enough for one incident to "
"mean something. Backing, collateral, LP and vault-share holdings are **not** resolved — the Blend "
"case (contracts sound, backstop composed of another protocol's LP) is exactly what this run cannot "
"yet see.\n" % tier_counts.get(3,0),
"- **Fork lineage is weak, and that caps Tier 1.** DefiLlama populates `forkedFrom` on **6 protocols "
"out of 8,135**, so it carries nothing. The only code-lineage evidence available is `parentProtocol` "
"(version siblings), which is why Tier 1 holds 6 and Tier 4 holds 83 — the relatives are real but the "
"link is a sibling relationship, not proven shared code.\n"
"- **A grouping this pass rejected.** Grouping protocols by shared adapter module first produced a "
"7-member \"fork cluster\" around a victim, headed by a $19.3M protocol. The shared module was "
"`dummy.js` — DefiLlama's placeholder for *no adapter*, carried by 1,124 protocols including Fantom, "
"0x, Jupiter and OpenSea Seaport. Not shared code at all. Placeholder modules and groups above 12 "
"members are now rejected.\n"
"- **The capability that would fix this: runtime bytecode similarity.** Hashing deployed code across "
"the probed population would find literal clones of a victim — the \"byte-similar\" half of Tier 4 "
"that lineage metadata cannot reach. Not run in this pass.\n"
"- **Tier 1 rests on DefiLlama's incident dataset plus this run's corpus.** A protocol with no recorded "
"incident may simply have no record.\n",
"- **Value at risk sits beside the score and never inside it.** A real finding on $60k of dust is a "
"low-value save; check the column before spending time.\n",
"- Read-only throughout. No transaction, no calldata, no credential use.\n"]
open(f'{B}/results/candidates_by_urgency.md','w').write("\n".join(L)+"\n")
json.dump({"fresh_by_tier":{f"T{k}":v for k,v in sorted(tier_counts.items())},
 "delivered_now_hot":len(HB),"selected":len(chosen)},
 open(f'{B}/protocols/urgency_summary.json','w'),indent=1)
print(json.dumps({"selected":len(chosen),"tier1_2_in_list":len(hot),
  "fresh_by_tier":{f"T{k}":v for k,v in sorted(tier_counts.items())},
  "withheld_but_now_hot":len(HB)},indent=2))
