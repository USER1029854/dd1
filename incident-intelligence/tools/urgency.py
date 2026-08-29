#!/usr/bin/env python3
"""Urgency-first triage: rank by time-to-exploitation, not by likelihood in the abstract.

The axis change
---------------
The previous scorer ranked by how LIKELY a protocol was to be hacked, which treats a
novel bug nobody has found the same as one whose exploit is already written and
circulating. This ranks by how little stands between an attacker and the money now:

    URGENCY is highest where the technique is already public
    AND the fix is not in the deployed artifact
    AND live value is reachable by an unprivileged caller.

Remediation status stops being a footnote at the bottom of a candidate block and
becomes the primary ranking driver, worth 40 of 100 points.

What this file will NOT do
--------------------------
Claim a fix is absent from a deployed artifact without having read that artifact. The
full 40 points requires an L4 confirmation that the specific fixed line/behaviour is
missing from the runtime bytecode. This run has not performed that per-protocol check,
so the honest ceiling here is 28 -- "a public technique exists for this code and its
fix status is unverified at the artifact". Every row says which it is. An urgency claim
that cannot be evidenced at the artifact is UNKNOWN, never URGENT.
"""
import json,os,sys,datetime,collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import hazard as HZ
B=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')
NOW=datetime.date(2026,8,27)

# ---- remediation status vocabulary (spec §6) ----
UNREMEDIATED_KNOWN        ='UNREMEDIATED_KNOWN'
FIX_DEPLOYED              ='FIX_DEPLOYED'
FIX_IN_REPO_ONLY          ='FIX_IN_REPO_ONLY'
KNOWN_ISSUE_STATUS_UNKNOWN='KNOWN_ISSUE_STATUS_UNKNOWN'
SIMILAR_ALREADY_REPORTED  ='SIMILAR_ALREADY_REPORTED'
NO_PUBLIC_MATCH           ='NO_PUBLIC_MATCH'

# §5 remediation-gap band -> points out of 40
REMEDIATION_POINTS={
  UNREMEDIATED_KNOWN:40,          # fix PROVEN absent in the deployed artifact (needs L4)
  KNOWN_ISSUE_STATUS_UNKNOWN:28,  # public technique exists, fix status unverifiable at the artifact
  FIX_IN_REPO_ONLY:28,            # repo says fixed, deployment unconfirmed -- same gap
  SIMILAR_ALREADY_REPORTED:24,    # mitigation/config-only, reversible by governance
  NO_PUBLIC_MATCH:0,              # novel high-fit; scored 0-10 by match strength below
  FIX_DEPLOYED:0}

def _days(d):
    try: return (NOW-datetime.date.fromisoformat(d)).days
    except Exception: return None

def recency_points(days,population):
    """20 pts: how recently the technique went public, and whether it is spreading.
    A fresh postmortem outranks an old one; a cluster with siblings already falling
    outranks a lone incident."""
    if days is None: return 0.0,'no dated public technique'
    if   days<=30:  base,why=12.0,'technique public %dd ago' % days
    elif days<=90:  base,why=9.0,'technique public %dd ago' % days
    elif days<=180: base,why=6.0,'technique public %dd ago' % days
    elif days<=365: base,why=3.0,'technique public %dd ago' % days
    else:           base,why=1.0,'technique public %dd ago' % days
    # propagation: how many independent deployments carry the same template/dependency
    if   population>=10: pr,pw=8.0,'%d-member population already falling' % population
    elif population>=4:  pr,pw=5.0,'%d-member population' % population
    elif population>=2:  pr,pw=3.0,'%d siblings' % population
    else:                pr,pw=0.0,'no population established'
    return base+pr, why+'; '+pw

def reachable_points(pair):
    """25 pts: unprivileged, cheap path to live value appears plausible on the read paths.
    Scaled by how directly value moves and how deeply it was actually read. Unknown
    scores zero."""
    lvl=pair.get('evidence_level')
    if lvl not in ('L2_DEPLOYMENT','L3_STATE','L4_GUARD_REVIEW'): return 0.0,'not read deeply enough to judge reachability'
    cs={**(pair.get('code') or {}),**(pair.get('state') or {})}
    present=[k for k,v in cs.items() if v=='PRESENT']
    if not present: return 0.0,'no precondition confirmed present'
    guards=pair.get('guards') or {}
    if any(v=='FOUND' for v in guards.values()):
        return 6.0,'a decisive guard was found in the reviewed path'
    reach=1.0 if any('reachable' in p or 'live_value' in p for p in present) else 0.6
    depth={'L2_DEPLOYMENT':0.6,'L3_STATE':0.8,'L4_GUARD_REVIEW':1.0}[lvl]
    return round(25.0*depth*reach,2), '%d precondition(s) present at %s, no guard found in the reviewed path' % (len(present),lvl)

def precondition_points(pair):
    """15 pts: mandatory preconditions observed live, coverage-weighted against the
    family's FULL signature. Unevaluated preconditions score zero, never a default."""
    m=pair.get('MATCH_SCORE') or 0
    return round(15.0*(m/100.0),2), 'MATCH %.1f coverage-weighted over the family signature' % m

# evidence ceilings (§5)
CEILING={'L0_METADATA':20,'L1_ADAPTER':45,'L2_DEPLOYMENT':60,'L3_STATE':100,'L4_GUARD_REVIEW':100}

def score(pair, tier, remediation, tech_days, population, impl_unresolved=False):
    rp=REMEDIATION_POINTS.get(remediation,0)
    if remediation==NO_PUBLIC_MATCH:
        rp=round(10.0*((pair.get('MATCH_SCORE') or 0)/100.0),1)
    rc,rcw=recency_points(tech_days,population)
    rv,rvw=reachable_points(pair)
    pc,pcw=precondition_points(pair)
    raw=rp+rc+rv+pc
    cap=CEILING.get(pair.get('evidence_level'),20)
    if impl_unresolved: cap=min(cap,60)
    return {"URGENCY":round(min(raw,cap),2),"tier":tier,"remediation":remediation,
            "components":{"remediation_gap":rp,"remediation_gap_max":40,
                          "technique_recency_propagation":rc,"max":20,"recency_basis":rcw,
                          "reachable_live_value":rv,"reachable_max":25,"reachable_basis":rvw,
                          "precondition_match":pc,"precondition_max":15,"precondition_basis":pcw},
            "raw_before_cap":round(raw,2),"evidence_cap":cap,
            "capped":raw>cap}
