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

def chain_hazard(chains):
    return max([CHAIN_HAZARD.get(c,CHAIN_DEFAULT) for c in (chains or [])] or [CHAIN_DEFAULT])
def category_hazard(cat):
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
}

def neglect(p, probe=None, sweep=None):
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
