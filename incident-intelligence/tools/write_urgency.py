#!/usr/bin/env python3
"""Urgency-ranked candidate list in the triage spec's output format."""
import json,os,sys,collections,datetime
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
B=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')
R=json.load(open(f'{B}/protocols/urgency_pairs.json'))
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

fresh=[r for r in R if r['protocol_slug'] not in DELIVERED]
held =[r for r in R if r['protocol_slug'] in DELIVERED and r['tier']<=2]
FB=sorted(best_per_protocol(fresh),key=lambda x:(x['tier'],-x['URGENCY']))
HB=sorted(best_per_protocol(held), key=lambda x:(x['tier'],-x['URGENCY']))
chosen=FB[:N]

def block(r,rank):
    f=FAM[r['family_id']]; p=E.get(r['protocol_slug'],{})
    ph=r.get('prior_hacks') or []
    cs={}
    L=[]
    L.append("### %d. %s — Tier %d — URGENCY %s\n" % (rank,r['protocol_name'],r['tier'],r['URGENCY']))
    L.append("- **Protocol:** `%s` · %s · %s" % (r['protocol_slug'],r.get('category') or '?',
             ", ".join((r.get('chains') or [])[:5])))
    L.append("- **DefiLlama:** %s" % r.get('defillama_url'))
    L.append("- **Value at risk (beside the score, not in it):** $%s · band `%s`"
             % (f"{r['tvl']:,.0f}",r.get('band_status')))
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
"## The axis changed\n",
"The previous list ranked by how **likely** a protocol was to be hacked. That treats a novel bug "
"nobody has found the same as one whose exploit is already written and circulating. This ranks by "
"**how little stands between an attacker and the money now** — remediation status is no longer a "
"footnote at the bottom of a block, it is 40 of the 100 points.\n",
"**The honest ceiling in this run is 28 of those 40, not 40.** The full band requires confirming that "
"the specific fixed line is *absent from the deployed artifact* — an L4 read of runtime bytecode at the "
"live address. This run has not performed that per-protocol check, so every Tier-1/2 row carries "
"`KNOWN_ISSUE_STATUS_UNKNOWN` and names the decisive check that would settle it. That check is the "
"first thing to run, and it is fast.\n",
"## What the tiers found\n",
"| Tier | What it means | Fresh protocols |","|---|---|---:|",
"| **1 — UNREMEDIATED-KNOWN** | a public technique exists for this protocol's own code, and it still holds funds | **%d** |" % tier_counts.get(1,0),
"| **2 — SHARED-DEPENDENCY** | an advisory or template live across a population with no patch-compliance mechanism | **%d** |" % tier_counts.get(2,0),
"| 3 — DEPENDENCY-IMPAIRMENT | the target holds or is backed by a system that is itself exposed | %d |" % tier_counts.get(3,0),
"| 4 — FORK-OF-RECENT-VICTIM | forked from a protocol exploited in-window | %d |" % tier_counts.get(4,0),
"| 5 — NOVEL-HIGH-FIT | strong match, no public disclosure — the clock has not started | %d |" % tier_counts.get(5,0),
"",
"This list leads with **%d Tier 1–2 candidates**. Spend the first hours entirely there.\n" % len(hot),
"## Handoff lines for CORE.md\n",
"```"]
for r in chosen:
    L.append("TARGET=%s || TIER=%d || FAMILY=%s || DECISIVE_CHECK=%s || VALUE_AT_RISK=%d || PINNED=<pin at handoff> || REMEDIATION=%s || MODULES=%s"
             % (r.get('defillama_url'),r['tier'],r['family_id'],
                " ".join((r['decisive_check'] or '').split())[:170],int(r['tvl']),r['remediation'],modules(r)))
L.append("```\n")
L.append("## Candidates\n")
for i,r in enumerate(chosen,1): L.append(block(r,i))

if HB:
    L.append("---\n")
    L.append("## Withheld by the no-repetition ledger — but now classified Tier 1–2\n")
    L.append("These **%d** protocols were handed over in earlier runs and are excluded from the list "
             "above. They are named here rather than silently dropped because the ranking axis changed "
             "underneath them: they were delivered as likelihood candidates and now classify as hot "
             "clocks. Withholding a Tier-1 item because it was once served cold would be the wrong "
             "call, so this is your decision, not mine.\n" % len(HB))
    L.append("| Protocol | Tier | URGENCY | Family | At risk | First delivered |")
    L.append("|---|---:|---:|---|---:|---|")
    for r in HB[:40]:
        L.append("| [%s](%s) | %d | %s | `%s` | $%s | `%s` |" % (r['protocol_name'],r['defillama_url'],
                 r['tier'],r['URGENCY'],r['family_id'],f"{r['tvl']:,.0f}",
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
