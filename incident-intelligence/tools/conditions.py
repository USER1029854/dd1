# -*- coding: utf-8 -*-
"""Creative observable conditions derived from DefiLlama metadata, the adapter
registries and the incident corpus. Each condition names the families it feeds and
whether it is evidence of a prerequisite or only a prioritisation signal."""
import json,re,collections

# condition_id -> (families fed, kind, weight, human description)
#   kind: 'LINEAGE'   contributes to the lineage-similarity score component
#         'PRECOND'   an observable prerequisite signal (still capped at the L0/L1 ceiling)
#         'PRIORITY'  ordering only, never scored
COND = {
 "FORK_OF_WINDOW_VICTIM": (None,'LINEAGE',22,
   "Forked from a protocol that was exploited inside the six-month window: the fork inherits the "
   "upstream defect until the patch is proven present in ITS deployed bytecode."),
 "FORK_OF_KNOWN_VULNERABLE_UPSTREAM": (None,'LINEAGE',16,
   "Forked from an upstream whose defect class is publicly documented (Compound V2 donation/exchange-rate, "
   "Aave V2 oracle configuration, DN404/BT404 packed ownership, Balancer V1 governance-drainable pools)."),
 "IS_WINDOW_VICTIM_STILL_LIVE": (None,'PRECOND',18,
   "The protocol itself was exploited in-window and still reports live TVL. Section 14 keeps previously "
   "exploited protocols in scope when the affected deployment remains live, the pattern exists in another "
   "module, or the fix is absent from deployed bytecode."),
 "DEAD_ADAPTER_WITH_RESIDUAL_TVL": (["UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY","APPROVALS-TO-UPGRADEABLE-SPENDER",
                                     "ACC-REWARD-INDEX-INIT-AND-ORDERING"],'PRECOND',20,
   "Listed in DefiLlama's own registries/deadAdapters.json yet still reports value. This is the authoritative "
   "abandoned-deployment signal, unlike the ambiguous `deprecated` flag."),
 "HALLMARK_PRIOR_INCIDENT": (None,'PRIORITY',14,
   "DefiLlama hallmarks record a prior hack, exploit, attack, drain or breach on this protocol's own timeline."),
 "VERSION_SIBLING_LEGACY": (["UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY","ACC-MULTI-PATH-CREDIT-DRIFT",
                             "UPGRADE-INITIALIZER-REACHABLE-LIVE"],'PRECOND',15,
   "Shares a parent protocol with a higher-version sibling while still holding value: the classic "
   "sibling-deployment-retains-the-old-version shape."),
 "DECLARED_FALLBACK_ORACLE": (["ORACLE-STALE-OR-SILENT-FALLBACK","LIQUIDATION-ON-MANIPULABLE-VALUATION"],'PRECOND',14,
   "DefiLlama records a Fallback or Secondary oracle for this protocol, so fallback selection logic exists "
   "by the protocol's own declaration. That logic is exactly what mis-selected the feed in Solido Cash."),
 "SINGLE_PRIMARY_ORACLE_NO_CROSSCHECK": (["ORACLE-STALE-OR-SILENT-FALLBACK","ORACLE-SPOT-THIN-LIQUIDITY",
                                          "LIQUIDATION-ON-MANIPULABLE-VALUATION"],'PRIORITY',8,
   "Exactly one declared oracle and no declared secondary, so no cross-source deviation bound is declared."),
 "PRICING_SURFACE_UNDECLARED": (["ORACLE-STALE-OR-SILENT-FALLBACK","ORACLE-SPOT-THIN-LIQUIDITY"],'PRIORITY',9,
   "A lending, CDP, derivatives or curation archetype with no oracle declared at all: the pricing path is unmapped."),
 "RWA_PRICING_SURFACE": (["ORACLE-STALE-OR-SILENT-FALLBACK","ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE",
                          "SETTLEMENT-EPOCH-BOUNDARY-CREDIT"],'PRECOND',13,
   "Prices real-world assets (treasury bills, private credit, real estate, equities, commodities, money-market "
   "funds). Off-chain-valued collateral with periodic marks is the surface that failed in Solido Cash and "
   "Ploutos Money inside this window."),
 "MISREPRESENTED_TOKENS": (["ACC-NAV-SHAREPRICE-MANIPULABLE","ACC-DONATION-UNACCOUNTED-BALANCE",
                            "TOKEN-TRANSFER-OVERRIDE-BREAKS-CONSERVATION"],'PRIORITY',10,
   "DefiLlama flags this protocol's token accounting as misrepresented: its own indexer cannot reconcile the "
   "reported holdings, which is a direct accounting-integrity signal."),
 "WRONG_LIQUIDITY_FLAG": (["ORACLE-SPOT-THIN-LIQUIDITY","AMM-POOL-RATIO-SKEW-EXTRACTION"],'PRIORITY',10,
   "DefiLlama flags this protocol's liquidity figures as wrong, so depth-derived assumptions are unreliable."),
 "CO_CURATED_VAULTS": (["ACC-NAV-SHAREPRICE-MANIPULABLE","ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE"],'PRECOND',12,
   "Curates vaults jointly with another curator, so a valuation failure in a shared component has a blast "
   "radius spanning both curators' depositors."),
 "AUTHORITY_ADDRESSES_BEYOND_TVL": (["CALLDATA-CALLER-CONTROLLED-TARGET","APPROVALS-TO-UPGRADEABLE-SPENDER",
                                     "GOV-CHEAP-CONTROL-NO-TIMELOCK","AUTH-MISSING-ON-VALUE-MOVING-PATH"],'PRIORITY',8,
   "Declares treasury, staking or pool2 addresses that hold value outside the TVL figure, so TVL understates "
   "what an authority failure reaches."),
 "REBRANDED_DEPLOYMENT": (["UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY"],'PRIORITY',7,
   "Operated under previous names, so contracts deployed under the old identity may still be live and unwatched."),
 "DEAD_FRONTEND_FUNDED": (["UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY","AUTH-MISSING-ON-VALUE-MOVING-PATH"],'PRECOND',12,
   "Front end is dead while contracts still hold value: nobody is watching the deployment that still holds funds."),
 "WARNING_BANNER": (None,'PRIORITY',8,"DefiLlama displays a warning banner on this protocol."),
 "NO_AUDIT_MATERIAL_TVL": (None,'PRIORITY',6,
   "No audit link listed while holding material value. A prioritisation feature only - absence of an audit is "
   "never evidence of a defect."),
 "MULTICHAIN_VERSION_DRIFT": (["ACC-MULTI-PATH-CREDIT-DRIFT","UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY",
                               "BRIDGE-MESSAGE-NOT-BOUND-TO-SOURCE"],'PRIORITY',7,
   "Deployed across many chains, where per-chain deployments drift and the least-watched chain sets the risk."),
 "SHARED_GITHUB_LINEAGE": (None,'LINEAGE',10,
   "Shares a GitHub organisation with a protocol exploited in-window, so code may be shared."),
 "TAG_HOOK_AMM": (["CALLBACK-UNAUTHENTICATED-CALLER-USES-APPROVALS","CALLBACK-STATE-LOCK-INCOMPLETE",
                   "ACC-MULTI-PATH-CREDIT-DRIFT"],'PRECOND',14,
   "Hook-based AMM: payment and accounting run through callbacks, the architecture that failed in Ekubo."),
 "TAG_CLMM": (["SIG-REPLAY-CROSS-POSITION","QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET"],'PRECOND',11,
   "Concentrated-liquidity AMM with per-position NFTs managed on users' behalf: the Atomic Green shape, where "
   "one manager signature covered many positions."),
 "TAG_STABLESWAP": (["AMM-POOL-RATIO-SKEW-EXTRACTION","ORACLE-SPOT-THIN-LIQUIDITY"],'PRECOND',11,
   "StableSwap-style curve whose pricing at extreme imbalance is the Allbridge Core surface."),
 "TAG_VE33": (["ACC-REWARD-INDEX-INIT-AND-ORDERING","ACC-DUPLICATE-ID-ACCUMULATION",
               "INCENTIVE-PER-ADDRESS-NO-SYBIL-COST"],'PRECOND',10,
   "ve(3,3) gauge and bribe accounting: per-epoch reward indices and per-ID lock accounting, the ApeBond and "
   "NovaBox surfaces."),
 "TAG_ORDERBOOK": (["LIQUIDATION-ON-MANIPULABLE-VALUATION","SETTLEMENT-EPOCH-BOUNDARY-CREDIT"],'PRECOND',10,
   "On-chain order book with its own mark price: the Cascade shape, where the mark was moved by the party "
   "holding the opposing position."),
}

VULN_UPSTREAM = {"compound v2","compound","venus","aave v2","aave v1","dn404","bt404","flooring protocol",
                 "balancer v1","curve dex","uniswap v2","set protocol","cream finance","iron bank"}
RWA_TAGS = {"treasury bills","private credit","real estate","stocks & etfs","commodities",
            "money market funds","other fixed income"}
TAGMAP = {"hook-based amm":"TAG_HOOK_AMM","clmm":"TAG_CLMM","dlmm":"TAG_CLMM",
          "stableswap":"TAG_STABLESWAP","ve(3,3)":"TAG_VE33","order book":"TAG_ORDERBOOK"}
INCIDENT_KW = ("hack","exploit","attack","drain","breach","incident")
LENDING_LIKE = {"Lending","CDP","RWA Lending","Derivatives","Risk Curators","Basis Trading",
                "Onchain Capital Allocator","Leveraged Farming","Perps"}

def norm(s): return re.sub(r'[^a-z0-9]','',(s or '').lower())

def build(P, dead_map, victim_slugs, victim_families, curator_cfg):
    """Return slug -> {condition_id: {'evidence':..., 'families':[...]}}"""
    byid={str(r['id']):r for r in P}
    # version-sibling index
    fam=collections.defaultdict(list)
    for r in P:
        if r.get('parentProtocolSlug'): fam[r['parentProtocolSlug']].append(r)
    def vnum(nm):
        m=re.search(r'\bv(\d)\b',(nm or '').lower())
        return int(m.group(1)) if m else None
    # curator vault -> curators
    vault_owners=collections.defaultdict(set)
    for k,v in (curator_cfg or {}).items():
        a=v.get('addresses') or {}
        for vt in (a.get('morpho') or [])+(a.get('turtleclub') or [])+(a.get('vaults') or []):
            vault_owners[vt.lower()].add(k)
    victim_github={ (g or '').lower() for s in victim_slugs
                    for g in ((next((r for r in P if r['slug']==s),{}) or {}).get('github') or []) }
    out={}
    for r in P:
        s=r['slug']; c={}
        def add(cid,ev,fams=None):
            base=COND[cid][0]
            c[cid]={"evidence":ev,"families":fams if fams is not None else base}
        # fork lineage
        fids=[str(x) for x in (r.get('forkedFromIds') or [])]
        upnames=[byid[f]['name'] for f in fids if f in byid]
        upslugs=[byid[f]['slug'] for f in fids if f in byid]
        vhit=[u for u in upslugs if u in victim_slugs]
        if vhit:
            fams=sorted({f for u in vhit for f in victim_families.get(u,[])}) or None
            add("FORK_OF_WINDOW_VICTIM",f"forked from in-window victim(s): {', '.join(vhit)}",fams)
        vu=[u for u in upnames if norm(u) in {norm(x) for x in VULN_UPSTREAM}]
        if vu: add("FORK_OF_KNOWN_VULNERABLE_UPSTREAM",f"forked from {', '.join(vu)}",None)
        if s in victim_slugs and (r.get('tvl') or 0)>0:
            add("IS_WINDOW_VICTIM_STILL_LIVE",
                f"exploited in-window and still reporting ${r.get('tvl'):,.0f}",
                victim_families.get(s) or None)
        if s in dead_map and (r.get('tvl') or 0)>0:
            add("DEAD_ADAPTER_WITH_RESIDUAL_TVL",
                f"deadAdapters key `{dead_map[s]}` with ${r.get('tvl'):,.0f} still reported")
        hm=[h for h in (r.get('hallmarks') or []) if len(h)>1 and any(k in str(h[1]).lower() for k in INCIDENT_KW)]
        if hm: add("HALLMARK_PRIOR_INCIDENT","hallmarks: "+"; ".join(str(h[1])[:60] for h in hm[:3]))
        sib=fam.get(r.get('parentProtocolSlug') or '',[])
        if len(sib)>1:
            mine=vnum(r['name'])
            others=[vnum(x['name']) for x in sib if x['slug']!=s]
            if mine is not None and any(o is not None and o>mine for o in others):
                add("VERSION_SIBLING_LEGACY",
                    f"v{mine} alongside newer sibling(s) "+", ".join(x['name'] for x in sib if (vnum(x['name']) or -1)>mine)[:90])
        ob=r.get('oraclesBreakdown') or []
        types={o.get('type') for o in ob}
        if types & {"Fallback","Secondary"}:
            add("DECLARED_FALLBACK_ORACLE","declared: "+", ".join(f"{o.get('name')}({o.get('type')})" for o in ob))
        elif len(ob)==1 and r.get('category') in LENDING_LIKE:
            add("SINGLE_PRIMARY_ORACLE_NO_CROSSCHECK",f"single declared oracle: {ob[0].get('name')}")
        elif not ob and r.get('category') in LENDING_LIKE:
            add("PRICING_SURFACE_UNDECLARED",f"{r.get('category')} with no oracle declared")
        tags={str(t).lower() for t in (r.get('tags') or [])}
        if tags & RWA_TAGS or (r.get('category') or '').startswith('RWA'):
            add("RWA_PRICING_SURFACE","tags/category: "+", ".join(sorted(tags & RWA_TAGS) or [r.get('category')]))
        for t,cid in TAGMAP.items():
            if t in tags: add(cid,f"tag `{t}`")
        if r.get('misrepresentedTokens'): add("MISREPRESENTED_TOKENS","DefiLlama misrepresentedTokens flag")
        if r.get('wrongLiquidity'):       add("WRONG_LIQUIDITY_FLAG","DefiLlama wrongLiquidity flag")
        if r.get('warningBanners'):       add("WARNING_BANNER","DefiLlama warning banner present")
        if r.get('previousNames'):        add("REBRANDED_DEPLOYMENT","previous names: "+", ".join(r['previousNames'][:3]))
        if r.get('deadUrl') and (r.get('tvl') or 0)>=50_000:
            add("DEAD_FRONTEND_FUNDED",f"dead front end with ${r.get('tvl'):,.0f} still reported")
        if not r.get('audit_links') and (r.get('tvl') or 0)>=50_000:
            add("NO_AUDIT_MATERIAL_TVL",f"no audit link listed at ${r.get('tvl'):,.0f}")
        if len(r.get('chains') or [])>5:
            add("MULTICHAIN_VERSION_DRIFT",f"{len(r['chains'])} chains")
        if r.get('treasury') or r.get('staking') or r.get('pool2'):
            add("AUTHORITY_ADDRESSES_BEYOND_TVL","declares "+", ".join(
                k for k in ('treasury','staking','pool2') if r.get(k)))
        gh={(g or '').lower() for g in (r.get('github') or [])}
        if gh and (gh & victim_github) and s not in victim_slugs:
            add("SHARED_GITHUB_LINEAGE","shares GitHub org with an in-window victim: "+", ".join(sorted(gh & victim_github)))
        ck=norm(r['name'])
        shared=[vt for vt,owners in vault_owners.items() if len(owners)>1 and ck in {norm(o) for o in owners}]
        if shared: add("CO_CURATED_VAULTS",f"{len(shared)} vault(s) co-curated with another curator")
        if c: out[s]=c
    return out
