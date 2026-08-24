# -*- coding: utf-8 -*-
"""Empirical hazard and neglect model, derived from THIS run's incident corpus.

Purpose: rank by how likely a protocol is to actually be attacked, for an independent
reviewer who can realistically engage small and mid-sized teams. Exposure is reported
but deliberately does NOT drive the ranking, because the corpus says exposure is a poor
predictor of being hit: median in-window loss was $252,000 and 84% of incidents cost
under $2M.
"""

# Hazard ratio = (share of in-window incidents) / (share of eligible protocols).
# >1 means the segment is over-represented among real victims.
import json as _json, os as _os
_V2=_os.path.join(_os.path.dirname(__file__),'..','protocols','hazard_tables_v2.json')
_T=_json.load(open(_V2)) if _os.path.exists(_V2) else {}
# Blended tables: geometric mean of the six-month SlowMist corpus (which captures small
# token/farm/BSC incidents) and DefiLlama's 2022+ hacks dataset (far better n for DeFi
# protocols, four-year window). Neither source alone is representative.
CHAIN_HAZARD_BLENDED=_T.get('chain_hazard_blended') or {}
CATEGORY_HAZARD_BLENDED=_T.get('category_hazard_blended') or {}
REPEAT_VICTIMS=_T.get('repeat_victims') or {}
PRIOR_HACKS=_T.get('prior_hacks_by_slug') or {}
CHAIN_ALIASES={'BSC':'Binance','Binance':'BSC','NEAR':'Near','Near':'NEAR'}

CHAIN_HAZARD={'Supra':6.42,'Near':4.08,'NEAR':4.08,'Binance':3.61,'BSC':3.61,'Ethereum':2.54,
 'Sui':1.93,'Arbitrum':1.29,'Solana':1.11,'Base':0.96,'Polygon':0.56,'Avalanche':0.37}
CHAIN_DEFAULT=0.80

CATEGORY_HAZARD={'Farm':13.74,'Algo-Stables':13.20,'Privacy':12.10,'Staking Pool':5.04,
 'Bridge':3.59,'Cross Chain Bridge':3.59,'Canonical Bridge':3.59,'Liquidity Manager':3.36,
 'Options':2.42,'Leveraged Farming':2.00,'Launchpad':1.50,'NFT Lending':1.50,'Lending':1.49,
 'Indexes':1.20,'CDP':1.15,'Yield':1.03,'Dexs':1.00,'Yield Aggregator':0.90,'Basis Trading':0.80,
 'Derivatives':0.81,'Liquid Staking':0.70,'Liquid Restaking':0.70,'Prediction Market':0.70,
 'Onchain Capital Allocator':0.70,'Risk Curators':0.50,'RWA':0.46,'RWA Lending':0.60}
CATEGORY_DEFAULT=0.70

# Observed loss distribution of in-window on-chain incidents.
LOSS_P50=252_000; LOSS_P75=1_140_000; LOSS_P90=3_700_000
BAND_LO=50_000; BAND_HI=30_000_000

def _ch1(c):
    for k in (c, CHAIN_ALIASES.get(c)):
        if k and k in CHAIN_HAZARD_BLENDED: return CHAIN_HAZARD_BLENDED[k]
        if k and k in CHAIN_HAZARD: return CHAIN_HAZARD[k]
    return CHAIN_DEFAULT
def chain_hazard(chains):
    return max([_ch1(c) for c in (chains or [])] or [CHAIN_DEFAULT])
def category_hazard(cat):
    if cat in CATEGORY_HAZARD_BLENDED: return CATEGORY_HAZARD_BLENDED[cat]
    return CATEGORY_HAZARD.get(cat,CATEGORY_DEFAULT)

def hazard_profile(p):
    """0-25. Empirical over-representation of this protocol's segment among real victims."""
    ch=chain_hazard(p.get('_chains')); ca=category_hazard(p.get('_cat'))
    raw=ch*ca                       # ~0.3 .. ~50
    import math
    return round(min(25.0, 25.0*(math.log10(max(raw,0.3))+0.52)/(math.log10(50)+0.52)),2), ch, ca

NEGLECT_SIGNALS={
 'no_audit_listed':          (7,"no audit link listed by DefiLlama"),
 'single_audit_only':        (2,"a single audit listed, with no indication it covers the current deployment"),
 'dead_front_end':           (6,"front end is dead while contracts still hold value"),
 'deprecated_flag':          (4,"DefiLlama deprecated flag (ambiguous on its own)"),
 'dead_adapter_registry':    (7,"in DefiLlama's own deadAdapters registry while still reporting value"),
 'unverified_implementation':(7,"an implementation behind a proxy is unverified on the explorer"),
 'owner_is_eoa':             (6,"a privileged owner() resolves to an externally owned account, not a contract"),
 'owner_is_zero_with_value': (5,"owner() is the zero address while the contract still holds code and value"),
 'no_timelock_in_source':    (3,"no timelock construct found in the source that was read"),
 'prior_incident_hallmark':  (5,"DefiLlama hallmarks record a prior hack, exploit or drain on this protocol"),
 'is_window_victim':         (6,"exploited inside the six-month window and still listed"),
 'fork_of_window_victim':    (6,"forked from a protocol exploited inside the window"),
 'rebranded':                (2,"operated under previous names, so old contracts may still be live"),
 'version_sibling_legacy':   (4,"a version sibling of a newer deployment still holds value"),
 'sharp_outflow':            (4,"TVL fell sharply over the last week, the abandonment signature"),
 'sharp_inflow_unaudited':   (5,"TVL rose sharply over the last week with no audit listed: fresh money on unproven code"),
 'warning_banner':           (3,"DefiLlama displays a warning banner"),
 'misrepresented_tokens':    (3,"DefiLlama cannot reconcile this protocol's reported token holdings"),
 'repeat_victim':            (8,"already hacked more than once and still holding value: the strongest single "
                                "predictor in the data, since whatever let it happen twice is still there"),
 'prior_onchain_hack_live':  (5,"hacked by an on-chain defect before and still listed, per DefiLlama's own "
                                "hacks dataset"),
 'prior_technique_matches_family':(6,"the technique that hit this protocol before maps to the family being "
                                     "tested now, so the same class of defect may still be reachable"),
}

# DefiLlama hack techniques mapped onto this library's families.
TECHNIQUE_FAMILY={
 'Improper Access Control':{'AUTH-MISSING-ON-VALUE-MOVING-PATH','AUTH-ZERO-ADDRESS-ACCEPTED',
                            'AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY','AUTH-IDENTITY-SATISFIABLE-BY-ATTACKER-CONTRACT'},
 'Spot Price Manipulation':{'ORACLE-SPOT-THIN-LIQUIDITY','LIQUIDATION-ON-MANIPULABLE-VALUATION'},
 'Oracle Manipulation':{'ORACLE-SPOT-THIN-LIQUIDITY','ORACLE-STALE-OR-SILENT-FALLBACK',
                        'ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE'},
 'Oracle Misconfiguration':{'ORACLE-STALE-OR-SILENT-FALLBACK'},
 'Reentrancy':{'CALLBACK-STATE-LOCK-INCOMPLETE'},
 'Incorrect Share Accounting':{'ACC-NAV-SHAREPRICE-MANIPULABLE','ACC-ZERO-SUPPLY-INFLATION',
                               'ACC-DONATION-UNACCOUNTED-BALANCE'},
 'Donation Attack':{'ACC-DONATION-UNACCOUNTED-BALANCE'},
 'Infinite Mint':{'BRIDGE-MESSAGE-NOT-BOUND-TO-SOURCE','AUTH-MISSING-ON-VALUE-MOVING-PATH'},
 'Arbitrary External Call':{'CALLDATA-CALLER-CONTROLLED-TARGET'},
 'Token Approval Abuse':{'CALLDATA-CALLER-CONTROLLED-TARGET','CALLBACK-UNAUTHENTICATED-CALLER-USES-APPROVALS',
                         'APPROVALS-TO-UPGRADEABLE-SPENDER'},
 'Reward Logic Flaw':{'ACC-REWARD-INDEX-INIT-AND-ORDERING','ACC-CREDIT-NOT-RECEIVED'},
 'Arithmetic Error':{'ACC-SIGN-OR-BOUND-CHECK-MISSING','ACC-SPLIT-NONINVARIANT'},
 'Missing Input Validation':{'ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED','QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET'},
 'Forged Proof':{'PROOF-VERIFICATION-BYPASSED','BRIDGE-MESSAGE-NOT-BOUND-TO-SOURCE'},
 'Withdrawal Logic Flaw':{'ACC-SPLIT-NONINVARIANT','AUTH-PUBLIC-CLAIM-NO-ELIGIBILITY'},
 'Swap Logic Flaw':{'QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET','AMM-POOL-RATIO-SKEW-EXTRACTION'},
 'Signature Replay':{'SIG-REPLAY-CROSS-POSITION','SIG-DIGEST-AMBIGUOUS-OR-UNBOUND'},
 'Cross-Chain Message Spoofing':{'BRIDGE-MESSAGE-NOT-BOUND-TO-SOURCE'},
}

PRIOR_SIGNALS_ENABLED=True
def prior_hack_signals(slug, family_id=None, before_date=None):
    """Signals drawn from DefiLlama's own hacks dataset for this exact protocol.
    `before_date` restricts to hacks strictly earlier than that ISO date, which is what a
    leakage-free backtest needs: you cannot use an incident to predict itself."""
    if not PRIOR_SIGNALS_ENABLED: return []
    """Signals drawn from DefiLlama's own hacks dataset for this exact protocol."""
    out=[]
    hs=PRIOR_HACKS.get(slug) or []
    if before_date: hs=[h for h in hs if (h.get('date') or '9999') < before_date]
    n=REPEAT_VICTIMS.get(slug) if not before_date else len(hs)
    if n and n>1: out.append('repeat_victim')
    if hs: out.append('prior_onchain_hack_live')
    if family_id:
        for h in hs:
            if family_id in TECHNIQUE_FAMILY.get(h.get('technique') or '', set()):
                out.append('prior_technique_matches_family'); break
    return out

def neglect(p, probe=None, sweep=None, family_id=None, before_date=None):
    """0-25 plus the itemised reasons. Neglect is the attention deficit an attacker exploits."""
    hits=[]; conds=set(p.get('_conditions') or [])
    if not p.get('_audit_links'): hits.append('no_audit_listed')
    elif len(p['_audit_links'])==1: hits.append('single_audit_only')
    if p.get('_dead_url') and (p.get('_tvl') or 0)>0: hits.append('dead_front_end')
    if p.get('_deprecated'): hits.append('deprecated_flag')
    if 'DEAD_ADAPTER_WITH_RESIDUAL_TVL' in conds: hits.append('dead_adapter_registry')
    if 'HALLMARK_PRIOR_INCIDENT' in conds: hits.append('prior_incident_hallmark')
    if 'IS_WINDOW_VICTIM_STILL_LIVE' in conds: hits.append('is_window_victim')
    if 'FORK_OF_WINDOW_VICTIM' in conds: hits.append('fork_of_window_victim')
    if 'REBRANDED_DEPLOYMENT' in conds: hits.append('rebranded')
    if 'VERSION_SIBLING_LEGACY' in conds: hits.append('version_sibling_legacy')
    if 'WARNING_BANNER' in conds: hits.append('warning_banner')
    if 'MISREPRESENTED_TOKENS' in conds: hits.append('misrepresented_tokens')
    c7=p.get('change_7d')
    if isinstance(c7,(int,float)):
        if c7<=-35: hits.append('sharp_outflow')
        if c7>=60 and not p.get('_audit_links'): hits.append('sharp_inflow_unaudited')
    if probe:
        ap=probe.get('deployment',{}).get('addresses_probed',[])
        if any(a.get('owner_is_eoa') for a in ap): hits.append('owner_is_eoa')
        if any(a.get('owner_is_zero') and (a.get('code_size') or 0)>0 for a in ap): hits.append('owner_is_zero_with_value')
    if sweep:
        if any(c.get('status')=='IMPLEMENTATION_NOT_VERIFIED' for c in sweep.get('contracts',[])):
            hits.append('unverified_implementation')
        ind=sweep.get('indicators') or {}
        if ind and ind.get('timelock_present') is False: hits.append('no_timelock_in_source')
    hits += [h for h in prior_hack_signals(p.get('slug'), family_id, before_date) if h not in hits]
    score=sum(NEGLECT_SIGNALS[h][0] for h in hits)
    return round(min(25.0,score),2), [{"signal":h,"weight":NEGLECT_SIGNALS[h][0],
                                       "meaning":NEGLECT_SIGNALS[h][1]} for h in hits]

def attacker_economics(tvl):
    """0-10. Peaks where real losses actually landed: big enough to be worth an exploit,
    small enough that nobody is watching closely."""
    t=tvl or 0
    if t < BAND_LO:            return 0.0,"below the floor"
    if t <= LOSS_P50*4:        return 10.0,"squarely in the band where most in-window losses landed"
    if t <= LOSS_P90:          return 9.0,"within the band covering 90% of in-window losses"
    if t <= 10_000_000:        return 7.0,"above the typical loss band but still lightly watched"
    if t <= BAND_HI:           return 5.0,"upper end of the reviewable band"
    if t <= 100_000_000:       return 2.0,"above the operator's band; likely covered by dedicated audit retainers"
    return 0.5,"far above the operator's band; assume continuous professional coverage"

def band_status(tvl, explicit_danger):
    t=tvl or 0
    if t < BAND_LO:  return 'BELOW_FLOOR', "under the $50,000 floor"
    if t <= BAND_HI: return 'IN_BAND', "inside the $50,000-$30,000,000 reviewable band"
    return ('ABOVE_BAND_KEPT_EXPLICIT_DANGER' if explicit_danger else 'ABOVE_BAND_DROPPED'), \
           ("above the band but retained: explicit specific danger evidence" if explicit_danger
            else "above the band and dropped: no explicit danger, and protocols this size are assumed "
                 "to carry dedicated professional audit coverage")
