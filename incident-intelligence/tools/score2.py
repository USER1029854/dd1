#!/usr/bin/env python3
"""Phase H/13 v2: mandatory-precondition gate + MATCH / EVIDENCE_CONFIDENCE / PREVENTION,
now consuming the deployed-source static-indicator sweep and the condition layer."""
import json,sys,os,math,datetime,collections
sys.path.insert(0,'/home/user/dd1/incident-intelligence/tools')
from source_sweep import FAMILY_SIGNALS
from conditions import COND
B='/home/user/dd1/incident-intelligence'
W=json.load(open(f'{B}/protocols/deep_screen_worklist.json'))
AD=json.load(open(f'{B}/protocols/adapters_index.json'))
PR=json.load(open(f'{B}/protocols/onchain_probes.json'))
FAM={f['family_id']:f for f in json.load(open(f'{B}/families/families.json'))}
E={r['slug']:r for r in json.load(open(f'{B}/protocols/eligibility.json'))}
PRIOR=json.load(open(f'{B}/protocols/prior_art.json')) if os.path.exists(f'{B}/protocols/prior_art.json') else {}
WSTART=datetime.date(2026,2,22); WEND=datetime.date(2026,8,22)

# ---- self-calibrating precision control -------------------------------------------------
# An indicator that fires on a large share of the screened population is describing a common
# architecture, not a distinguishing prerequisite. Those are demoted to ordering-only so they
# cannot carry a pair to a high score on their own. The measured prevalence is published on
# every affected pair so the demotion is auditable rather than a hidden thumb on the scale.
PREVALENCE_DEMOTE=0.25
_pop=[v for v in PR.values() if (v.get('source_sweep') or {}).get('indicators')]
PREVALENCE={}
if _pop:
    _keys=set().union(*[set(v['source_sweep']['indicators']) for v in _pop])
    for k in _keys:
        PREVALENCE[k]=round(sum(1 for v in _pop if v['source_sweep']['indicators'].get(k))/len(_pop),4)
DEMOTED={k for k,v in PREVALENCE.items() if v>PREVALENCE_DEMOTE}
SWEPT_POPULATION=len(_pop)

# Families whose real exposure precondition is live third-party approvals, which this
# read-only pass did not enumerate. That precondition stays UNKNOWN, so these families
# cannot reach a full score from code shape alone.
APPROVAL_DEPENDENT={'CALLDATA-CALLER-CONTROLLED-TARGET',
                    'CALLBACK-UNAUTHENTICATED-CALLER-USES-APPROVALS',
                    'APPROVALS-TO-UPGRADEABLE-SPENDER'}
P,A,U,NA='PRESENT','ABSENT','UNKNOWN','NOT_APPLICABLE'
SANCTIONED={'tornado-cash','tornado-cash-classic','sinbad','blender'}
def d(s): return datetime.date(*map(int,s.split('-')))

def from_source(slug,fid):
    """code preconditions + guards derived from deployed verified source."""
    ss=PR.get(slug,{}).get('source_sweep',{})
    sig=(ss.get('family_signals') or {}).get(fid) or {}
    code={}; guards={}; notes=[]
    if not sig: return code,guards,notes,False
    pre_hits=[i for i,h in sig.items() if h['role']=='PRE' and h['match'] and i not in DEMOTED]
    if not pre_hits:
        names=[c.get('name') for c in ss.get('contracts',[]) if c.get('status')=='VERIFIED']
        notes.append("RELEVANCE GATE: the contract(s) actually read ("+(", ".join(str(n) for n in names) or "none")
                     +") show no distinguishing indicator for this family, so they are probably not the contracts "
                      "that implement it. Every source-derived signal is therefore UNKNOWN, including the absence "
                      "of a guard: not finding a staleness check in a data-provider contract says nothing about "
                      "the oracle.")
        return code,guards,notes,False
    ver=[c for c in ss.get('contracts',[]) if c.get('status')=='VERIFIED']
    unver=[c for c in ss.get('contracts',[]) if c.get('status')=='IMPLEMENTATION_NOT_VERIFIED']
    weak=[]
    for ind,h in sig.items():
        if h['role']=='PRE' and ind in DEMOTED:
            weak.append(f"{ind}={'yes' if h['observed'] else 'no'} (DEMOTED: fires on "
                        f"{PREVALENCE[ind]*100:.0f}% of the {SWEPT_POPULATION} contracts swept, so it "
                        f"describes a common architecture rather than a distinguishing prerequisite)")
            continue
        if h['role']=='PRE':
            # A prerequisite indicator that did not match is UNKNOWN, not ABSENT: a regex
            # missing a pattern is not proof the pattern is absent from the real code path.
            code[f"src::{ind}"]= P if h['match'] else U
        elif h['role']=='GUARD':
            guards[ind]= 'FOUND' if h['match'] else 'NOT_FOUND'
        else:
            weak.append(f"{ind}={'yes' if h['observed'] else 'no'}")
    if weak:
        notes.append("weak/ambiguous source indicators (ordering only, never scored): "+", ".join(weak))
    if ver:
        notes.append("deployed source read for "+", ".join(f"{c.get('name')}@{c['address'][:10]}…({c['chain']})" for c in ver[:2])
                     +"; indicators matched: "+", ".join(k for k,h in sig.items() if h['match']))
    if unver:
        notes.append(f"{len(unver)} implementation(s) behind a proxy are NOT verified on the explorer: "
                     "implementation identity unresolved, score capped at 60")
    return code,guards,notes,bool(ver)

def evaluate(slug,fid,pair):
    p=E.get(slug,{}); ad=AD.get(slug,{}); pr=PR.get(slug,{})
    dep=pr.get('deployment',{}); comp=pr.get('compound',{}); cur=pr.get('curator',{}); aav=pr.get('aave',{})
    dead=pr.get('dead_adapter',{}); ms=comp.get('market_source') or {}
    ap=dep.get('addresses_probed',[])
    code,guards,notes,have_src = from_source(slug,fid)
    state={}; lineage=float(pair.get('condition_lineage_bonus') or 0.0); reach=U

    conds=set(pair.get('conditions') or [])
    for cid in conds:
        _f,kind,w,desc=COND[cid]
        notes.append(f"condition {cid} ({kind}): {desc}")

    # ---- live-state preconditions, per family group ----
    tvl=p.get('_tvl') or 0
    live_code=[a for a in ap if (a.get('code_size') or 0)>0]
    if fid=='ACC-DONATION-UNACCOUNTED-BALANCE':
        if ms:
            if ms.get('has_internal_cash_counter'):
                code['rate_reads_raw_balance']=A
                guards['internal_cash_counter']='FOUND'
                notes.append("deployed implementation tracks cash in an internal counter: the donation mechanism is closed here")
            elif ms.get('has_getCashPrior_balanceOf') or ms.get('has_balanceOf_this_in_cash_path'):
                code['rate_reads_raw_balance']=P
            impls=ms.get('implementation_names') or ([ms.get('name')] if ms.get('name') else [])
            if impls: notes.append("market implementation(s) resolved: "+", ".join(str(x) for x in impls))
        code.setdefault('unprivileged_inbound_transfer_possible',P)
        lm=[m for m in comp.get('markets',[]) if (m.get('getCash') or 0)>0 or (m.get('totalSupply') or 0)>0]
        if lm:
            state['inflated_rate_consumed_by_value_decision']= P if any((m.get('totalBorrows') or 0)>0 for m in lm) else U
            state['third_party_claims_exposed']=P
            notes.append(f"{len(lm)} live market(s) read on-chain")
        else:
            state['live_value_exposed']= P if tvl>0 else A
        reach = P if state.get('third_party_claims_exposed')==P else U
    elif fid in ('UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY',):
        authoritative = bool(dead.get('deadFrom')) or 'DEAD_ADAPTER_WITH_RESIDUAL_TVL' in conds
        corrob = authoritative or (p.get('_deprecated') and p.get('_dead_url')) or (p.get('_dead_url') and tvl>0)
        if corrob: code['unmaintained_or_differing_code_path']=P
        elif p.get('_deprecated'):
            code['unmaintained_or_differing_code_path']=U
            notes.append("CAUTION: DefiLlama's `deprecated` flag is set but uncorroborated; it is also used when an "
                         "adapter is superseded or its TVL is counted elsewhere. Treated as UNKNOWN.")
        else: code['unmaintained_or_differing_code_path']=U
        code['prior_version_still_callable']= P if live_code else U
        state['still_holds_value_or_authority']= P if tvl>0 else A
        state['not_paused']= P if any(a.get('paused') is False for a in live_code) else U
        guards['paused_and_drained']= 'FOUND' if any(a.get('paused') for a in live_code) else ('NOT_FOUND' if live_code else U)
        guards.setdefault('approvals_revoked',U)
        if live_code: notes.append(f"{len(live_code)} address(es) still hold deployed code on-chain")
        reach = P if tvl>0 and live_code else U
    elif fid=='UPGRADE-INITIALIZER-REACHABLE-LIVE':
        px=[a for a in live_code if a.get('is_proxy')]
        code['upgradeable_architecture']= P if px else (A if live_code else U)
        zero_init=[a for a in px if not a.get('oz5_initializable_slot')]
        code.setdefault('initializer_flag_unset', P if zero_init else U)
        if zero_init: notes.append(f"{len(zero_init)}/{len(px)} live proxies read a zero ERC-7201 Initializable slot "
                                   "(inconclusive alone: older OZ versions store the flag elsewhere)")
        state['live_value_or_approvals']= P if tvl>0 else A
        guards.setdefault('upgrade_timelocked', 'FOUND' if any(a.get('erc1967_admin') for a in px) else U)
        eoa=[a for a in px if a.get('owner')]
        if eoa: notes.append(f"{len(eoa)} proxy/proxies expose a non-zero owner()")
        reach = P if px and tvl>0 else U
    elif fid in ('ORACLE-STALE-OR-SILENT-FALLBACK','ORACLE-SPOT-THIN-LIQUIDITY',
                 'ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE','LIQUIDATION-ON-MANIPULABLE-VALUATION'):
        orc=p.get('_oracles') or []; ot=p.get('_oracle_types') or []
        code.setdefault('value_decision_reads_configured_feed', P if p.get('_cat') in
            ('Lending','CDP','RWA Lending','Derivatives','Risk Curators','Basis Trading','Leveraged Farming') else U)
        code.setdefault('feed_selection_is_configuration', U)   # raised to PRESENT only if an oracle contract is resolved on-chain
        if 'Fallback' in ot or 'Secondary' in ot:
            code['fallback_selection_logic_exists']=P
            notes.append("protocol declares a Fallback/Secondary oracle: fallback selection logic exists by its own declaration")
        provs=[x for x in aav.get('providers',[]) if x.get('status')=='OK'] or \
              [{'priceOracle':a.get('priceOracle'),'addressesProvider':a['address'],'chain':a['chain']}
               for a in live_code if a.get('priceOracle')]
        if provs:
            code['feed_selection_is_configuration']=P
            state['oracle_contract_resolved_on_chain']=P
            notes.append("price oracle resolved on-chain: "+"; ".join(
                f"{str(x.get('addressesProvider'))[:10]}… -> {str(x.get('priceOracle'))[:12]}…" for x in provs[:3]))
        state['live_positions_exposed']= P if (tvl>0 and p.get('_cat') in
            ('Lending','CDP','RWA Lending','Derivatives','Basis Trading','Leveraged Farming','Risk Curators')) else (P if tvl>0 else A)
        # DefiLlama's oracle list is metadata: it cannot establish a code-level precondition or
        # prove the absence of a code-level guard. Recorded as a note, never scored.
        guards.setdefault('deviation_bound_vs_independent_source',U)
        if len(orc)<=1:
            notes.append("only one oracle (or none) is declared in DefiLlama metadata; this is a prioritisation "
                         "signal about disclosure, not evidence that no cross-source deviation bound exists in code")
        notes.append(f"declared oracles: {', '.join(orc) if orc else 'none declared'}"
                     + (f" (types: {', '.join(ot)})" if ot else ""))
        reach = P if tvl>0 else U
    elif fid=='ACC-NAV-SHAREPRICE-MANIPULABLE':
        n=cur.get('declared_vault_count',0); vr=cur.get('vault_reads',[])
        code.setdefault('multi_component_totalAssets', P if n>1 else U)
        ta=[a for a in live_code if a.get('totalAssets')]
        if ta:
            code['erc4626_style_totalAssets_live']=P
            notes.append(f"{len(ta)} live contract(s) answer totalAssets()")
        state['live_pooled_depositor_value']= P if (tvl>0) else A
        if vr: notes.append(f"{len(vr)} curated vault(s) read on-chain")
        reach = P if tvl>0 else U
    else:
        state['live_value_present']= P if tvl>0 else A
        if live_code: state['deployment_reachable_on_chain']=P
        if not code:
            code['_adapter_only']=P
            notes.append("GENERIC SCREEN: no family-specific deployed-code signal was evaluated for this pair; "
                         "evidence is adapter/metadata architecture only and the score is capped accordingly.")
        reach = P if (tvl>0 and live_code) else U
    return code,state,guards,lineage,reach,notes,have_src

def level(slug,fid,code,have_src):
    ad=AD.get(slug,{}); pr=PR.get(slug,{})
    if code.get('_adapter_only')==P:
        return 'L1_ADAPTER' if ad.get('status','').startswith('READ') else 'L0_METADATA'
    if have_src or (pr.get('compound',{}).get('market_source') or {}).get('implementation_reviewed'):
        return 'L4_GUARD_REVIEW'
    has_state=bool(pr.get('deployment',{}).get('addresses_probed') or pr.get('compound',{}).get('markets')
                   or pr.get('curator',{}).get('vault_reads') or pr.get('aave',{}).get('providers'))
    if has_state: return 'L3_STATE'
    if ad.get('status','').startswith('READ'): return 'L1_ADAPTER'
    return 'L0_METADATA'

PRIMARY_GUARDS={
 'ACC-DONATION-UNACCOUNTED-BALANCE':{'internal_cash_counter'},
 'UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY':{'paused_and_drained'},
 'ACC-ZERO-SUPPLY-INFLATION':{'virtual_shares_offset','dead_shares_minted'},
 'UPGRADE-INITIALIZER-REACHABLE-LIVE':{'initializer_modifier_present'},
 'SIG-VERIFIER-DEFEATABLE':{'uses_oz_ecdsa'},
 'ACC-SIGN-OR-BOUND-CHECK-MISSING':{'safecast_used'},
 'ORACLE-SPOT-THIN-LIQUIDITY':{'twap_present'},
 'ORACLE-STALE-OR-SILENT-FALLBACK':{'staleness_check'},
 'CALLBACK-STATE-LOCK-INCOMPLETE':{'nonreentrant_present'},
 'HOOK-ZERO-VALUE-TRANSFER-TRIGGERS-ACCRUAL':{'zero_amount_guard'},
}
def score(pair):
    slug,fid=pair['protocol_slug'],pair['family_id']
    if slug in SANCTIONED:
        return {"killed":True,"kill_reason":"SANCTIONS_DESIGNATED_NO_LAWFUL_ENGAGEMENT",
                "killed_conditions":["responsible-disclosure recipient"],"code":{},"state":{},"guards":{},
                "notes":["Withheld from candidate promotion: sanctions-designated, so an authorized defensive "
                         "engagement has no lawful disclosure recipient and no remediation path."]}
    code,state,guards,lineage,reach,notes,have_src=evaluate(slug,fid,pair)
    pa=PRIOR.get(f"{slug}|{fid}",{}); dg=pa.get('downgrade') or {}
    if dg.get('apply'):
        guards[dg.get('guard','documented_decisive_guard')]='FOUND'
        notes.append("prior-art research found a documented decisive guard: "+pa.get('basis','')[:280])
        if dg.get('disposition')=='KILLED':
            return {"killed":True,"kill_reason":"DECISIVE_GUARD_FOUND","guards_found":[dg.get('guard')],
                    "prior_art_status":pa.get('status'),"residual_hypothesis":dg.get('residual_hypothesis'),
                    "code":code,"state":state,"guards":guards,"notes":notes}
    if any(v==A for v in code.values()) or any(v==A for v in state.values()):
        return {"killed":True,"kill_reason":"MANDATORY_PRECONDITION_PROVEN_ABSENT",
                "killed_conditions":[k for k,v in {**code,**state}.items() if v==A],
                "code":code,"state":state,"guards":guards,"notes":notes}
    found=[k for k,v in guards.items() if v=='FOUND']
    prim=[k for k in found if k in PRIMARY_GUARDS.get(fid,set())]
    evaluated=[g for g in guards if guards[g]!=U]
    if prim:
        return {"killed":True,"kill_reason":"DECISIVE_GUARD_FOUND","guards_found":prim,
                "code":code,"state":state,"guards":guards,"notes":notes}
    if found and len(found)*2 > max(1,len(evaluated)):
        return {"killed":True,"kill_reason":"DECISIVE_GUARD_FOUND","guards_found":found,
                "code":code,"state":state,"guards":guards,"notes":notes}
    # Precondition coverage is measured against the family's FULL declared signature, not
    # against the subset this pass happened to evaluate. A precondition that was never
    # evaluated is UNKNOWN and scores zero, exactly like one evaluated and not found.
    declared=len(FAM[fid].get('mandatory_preconditions') or []) or 4
    confirmed=sum(1 for v in list(code.values())+list(state.values()) if v==P)
    evaluated=sum(1 for v in list(code.values())+list(state.values()) if v!=NA)
    denom=max(declared, evaluated)
    coverage=min(1.0, confirmed/denom) if denom else 0.0
    ms_=20.0 + 45.0*coverage + min(15.0,lineage) \
        + (10.0 if reach==P else 0.0) \
        + (10.0 if all(v!='FOUND' for v in guards.values()) and any(v=='NOT_FOUND' for v in guards.values()) else 0.0)
    lvl=level(slug,fid,code,have_src)
    caps={'L0_METADATA':20,'L1_ADAPTER':45}
    if lvl in caps: ms_=min(ms_,caps[lvl])
    ss=PR.get(slug,{}).get('source_sweep',{})
    unresolved=any(c.get('status')=='IMPLEMENTATION_NOT_VERIFIED' for c in ss.get('contracts',[]))
    impl_resolved = have_src or (PR.get(slug,{}).get('compound',{}).get('market_source') or {}).get('implementation_reviewed')
    if unresolved or not impl_resolved: ms_=min(ms_,60)
    ad=AD.get(slug,{}); pr=PR.get(slug,{})
    ec={"mapping_completeness": 100 if ad.get('status','').startswith('READ') and ad.get('hardcoded_address_count') else
                                (70 if ad.get('status','').startswith('READ') else 20),
        "deployment_parity_confidence": 92 if have_src else
                                (90 if (pr.get('compound',{}).get('market_source') or {}).get('implementation_reviewed') else
                                (55 if pr.get('deployment',{}).get('addresses_probed') else 15)),
        "live_state_completeness": 85 if (pr.get('compound',{}).get('markets') or pr.get('curator',{}).get('vault_reads')
                                          or pr.get('aave',{}).get('providers') or pr.get('deployment',{}).get('addresses_probed')) else 15,
        "source_corroboration": 90 if FAM[fid]['evidence_strength']=='HIGH' else 65,
        "guard_review_depth": 85 if have_src else (55 if any(v!=U for v in guards.values()) else 15)}
    EC=round(sum(ec.values())/len(ec),1)
    tvl=pair.get('tvl') or 0; exposure=tvl; auth=[]
    if pair.get('governance'): exposure*=1.15; auth.append('on-chain governance authority')
    if fid in ('CALLDATA-CALLER-CONTROLLED-TARGET','CALLBACK-UNAUTHENTICATED-CALLER-USES-APPROVALS',
               'APPROVALS-TO-UPGRADEABLE-SPENDER'):
        auth.append('live user approvals not enumerated: exposure is a floor, not a ceiling')
    if 'AUTHORITY_ADDRESSES_BEYOND_TVL' in set(pair.get('conditions') or []):
        exposure*=1.1; auth.append('treasury/staking/pool2 value sits outside the TVL figure')
    if fid=='ACC-NAV-SHAREPRICE-MANIPULABLE': auth.append('curator authority over third-party vaults')
    EXP=round(min(1.2, math.log10(max(exposure,1))/10),4)
    rec=d(FAM[fid]['most_recent_event']) if FAM[fid]['most_recent_event'] else WSTART
    FRF=round(0.70+0.30*max(0.0,min(1.0,(rec-WSTART).days/max(1,(WEND-WSTART).days))),4)
    urc=FAM[fid]['unique_root_cause_count']
    RECUR=round(1.0+0.05*min(max(urc-2,0),4),3)
    return {"killed":False,"MATCH_SCORE":round(ms_,1),"EVIDENCE_CONFIDENCE":EC,
            "evidence_confidence_components":ec,"PREVENTION_SCORE":round(ms_*(EC/100.0)*EXP*FRF*RECUR,3),
            "EXPOSURE_INDEX":EXP,"FAMILY_RECENCY_FACTOR":FRF,"RECURRENCE_MULTIPLIER":RECUR,
            "exposure_basis_usd":round(exposure,2),"authority_notes":auth,
            "evidence_level":lvl,"code":code,"state":state,"guards":guards,"notes":notes,
            "precondition_coverage":{"family_declares":declared,"confirmed_present":confirmed,
                                     "evaluated":evaluated,"coverage":round(coverage,3),
                                     "note":"unevaluated preconditions count as zero, like unconfirmed ones"},
            "indicator_prevalence":{k.replace('src::',''):PREVALENCE.get(k.replace('src::',''))
                                    for k in code if k.startswith('src::')},
            "demoted_indicators":sorted(DEMOTED & set(
                (PR.get(slug,{}).get('source_sweep',{}).get('family_signals') or {}).get(fid,{}).keys()))}

out=[{**w,**score(w)} for w in W]
with open(f'{B}/protocols/deep_screened.jsonl','w') as fh:
    for o in out: fh.write(json.dumps(o,ensure_ascii=False)+"\n")
live=[o for o in out if not o['killed']]
print(json.dumps({"pairs":len(out),"killed":len(out)-len(live),
 "killed_by_precondition":sum(1 for o in out if o.get('kill_reason')=='MANDATORY_PRECONDITION_PROVEN_ABSENT'),
 "killed_by_guard":sum(1 for o in out if o.get('kill_reason')=='DECISIVE_GUARD_FOUND'),
 "killed_sanctions":sum(1 for o in out if o.get('kill_reason')=='SANCTIONS_DESIGNATED_NO_LAWFUL_ENGAGEMENT'),
 "surviving":len(live),"by_level":dict(collections.Counter(o['evidence_level'] for o in live)),
 "top_match":[(o['protocol_slug'],o['family_id'],o['MATCH_SCORE'],o['EVIDENCE_CONFIDENCE'],o['evidence_level'])
              for o in sorted(live,key=lambda x:-x['MATCH_SCORE'])[:12]],
 "top_prevention":[(o['protocol_slug'],o['family_id'],o['PREVENTION_SCORE'],f"${o['tvl']:,.0f}")
              for o in sorted(live,key=lambda x:-x['PREVENTION_SCORE'])[:12]]},indent=2))
