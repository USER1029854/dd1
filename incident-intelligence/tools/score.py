#!/usr/bin/env python3
"""Phase H/13: mandatory-precondition gate, MATCH_SCORE, EVIDENCE_CONFIDENCE, PREVENTION_SCORE."""
import json,sys,math,re,datetime,collections
sys.path.insert(0,'/home/user/dd1/incident-intelligence/tools')
B='/home/user/dd1/incident-intelligence'
W=json.load(open(f'{B}/protocols/deep_screen_worklist.json'))
AD=json.load(open(f'{B}/protocols/adapters_index.json'))
PR=json.load(open(f'{B}/protocols/onchain_probes.json'))
FAM={f['family_id']:f for f in json.load(open(f'{B}/families/families.json'))}
E={r['slug']:r for r in json.load(open(f'{B}/protocols/eligibility.json'))}
import os
PRIOR=json.load(open(f'{B}/protocols/prior_art.json')) if os.path.exists(f'{B}/protocols/prior_art.json') else {}
WSTART=datetime.date(2026,2,22); WEND=datetime.date(2026,8,22)
P,A,U,NA='PRESENT','ABSENT','UNKNOWN','NOT_APPLICABLE'

def d(s): return datetime.date(*map(int,s.split('-')))

def evaluate(slug,fid,pair):
    """Return (code_preconds, state_preconds, guards, lineage, reachability, notes)."""
    p=E.get(slug,{}); ad=AD.get(slug,{}); pr=PR.get(slug,{})
    comp=pr.get('compound',{}); cur=pr.get('curator',{}); dep=pr.get('deployment',{})
    aav=pr.get('aave',{}); dead=pr.get('dead_adapter',{})
    ms=comp.get('market_source') or {}
    code,state,guards,notes={},{},{},[]
    lineage=0.0; reach=U

    def live_markets():
        return [m for m in comp.get('markets',[]) if (m.get('getCash') or 0)>0 or (m.get('totalSupply') or 0)>0]

    if fid=='ACC-DONATION-UNACCOUNTED-BALANCE':
        if ms.get('verified'):
            if ms.get('has_internal_cash_counter'):
                code['rate_reads_raw_balance']=A
                notes.append("deployed implementation tracks cash in an internal counter, so the exchange rate is not "
                             "a function of the raw token balance: the donation mechanism is closed here")
            elif ms.get('has_getCashPrior_balanceOf') or ms.get('has_balanceOf_this_in_cash_path'):
                code['rate_reads_raw_balance']=P
            else:
                code['rate_reads_raw_balance']=U
            guards['internal_cash_counter']= 'FOUND' if ms.get('has_internal_cash_counter') else 'NOT_FOUND'
            guards['exchange_rate_change_cap']= 'FOUND' if ms.get('has_exchange_rate_cap') else 'NOT_FOUND'
            impls=ms.get('implementation_names') or ([ms.get('name')] if ms.get('name') else [])
            notes.append(f"deployed market implementation(s) resolved and read: {', '.join(str(x) for x in impls)}"
                         + (" (followed from the delegator/beacon proxy)" if ms.get('implementation_reviewed') else "")
                         + f"; cash read from balanceOf(address(this))={'yes' if ms.get('has_getCashPrior_balanceOf') or ms.get('has_balanceOf_this_in_cash_path') else 'not matched'}"
                         + f"; internal cash counter={'present' if ms.get('has_internal_cash_counter') else 'absent'}"
                         + f"; exchange-rate change cap={'present' if ms.get('has_exchange_rate_cap') else 'absent'}")
            lm2=live_markets()
            if lm2:
                notes.append(f"{len(lm2)} live market(s) read across {len({m.get('chain') for m in lm2})} chain(s); "
                             "sample: "+"; ".join(f"{m['cToken'][:10]}… cash={m.get('getCash')} borrows={m.get('totalBorrows')}"
                                                  for m in lm2[:3]))
        else:
            code['rate_reads_raw_balance']=U; guards['internal_cash_counter']=U; guards['exchange_rate_change_cap']=U
            notes.append("market implementation source not retrieved: rate-derivation path unresolved")
        code['unprivileged_inbound_transfer_possible']=P   # ERC-20 underlying, no allowlist possible
        lm=live_markets()
        state['inflated_rate_consumed_by_value_decision']= P if any((m.get('totalBorrows') or 0)>0 for m in lm) else (U if lm else A)
        state['third_party_claims_exposed']= P if any((m.get('totalSupply') or 0)>0 and (m.get('getCash') or 0)>0 for m in lm) else A
        caps=[m.get('supplyCap') for m in lm]
        guards['supply_cap_binds_rate']= 'FOUND' if any(c for c in caps if c) else ('NOT_FOUND' if caps else U)
        if p.get('_forked_from'): lineage=15.0; notes.append("fork lineage: "+", ".join(p['_forked_from']))
        elif comp.get('registry_key'): lineage=11.0; notes.append("enumerated by DefiLlama registries/compound.js (Compound-fork lineage)")
        reach = P if state.get('third_party_claims_exposed')==P else U
        if 'isInsolvent' in (comp.get('registry_flags') or []):
            notes.append("registry flags this deployment isInsolvent (existing bad debt) - live-state amplifier")

    elif fid=='ACC-NAV-SHAREPRICE-MANIPULABLE':
        n=cur.get('declared_vault_count',0)
        code['multi_component_totalAssets']= P if n>1 else (U if n==1 else U)
        code['component_valuation_externally_influenceable']=U
        vr=cur.get('vault_reads',[])
        state['live_pooled_depositor_value']= P if any((v.get('totalAssets') or 0)>0 for v in vr) else (U if not vr else A)
        state['deposit_and_redeem_reachable']=U
        guards['per_block_share_price_cap']=U
        guards['component_valuation_deviation_bound']=U
        if cur.get('curator_owner_addresses'):
            lineage=12.0
            notes.append(f"curator controls {n} declared vaults via registries/curators.js; "
                         f"owner keys {', '.join(cur['curator_owner_addresses'][:2])}")
        reach=U
        if vr: notes.append("live vault reads: "+"; ".join(
            f"{v['vault'][:10]}… totalAssets={v['totalAssets']}" for v in vr[:3]))

    elif fid in ('UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY','UPGRADE-INITIALIZER-REACHABLE-LIVE'):
        ap=dep.get('addresses_probed',[])
        code['prior_version_still_callable']= P if ap else U
        if fid=='UPGRADE-INITIALIZER-REACHABLE-LIVE':
            pr_=[x for x in ap if x.get('is_proxy')]
            code['upgradeable_architecture']= P if pr_ else (A if ap else U)
            code['initializer_flag_unset']= U   # requires per-contract layout resolution
            guards['initializer_consumed']=U
            guards['upgrade_timelocked']= 'FOUND' if any(x.get('erc1967_admin') for x in pr_) else U
            state['live_value_or_approvals']= P if ap else U
            if pr_: notes.append(f"{len(pr_)}/{len(ap)} probed adapter addresses are ERC-1967 proxies; "
                                 f"implementations: "+", ".join(str(x.get('erc1967_implementation'))[:12] for x in pr_[:3]))
        else:
            authoritative_dead = bool(dead.get('deadFrom'))
            corroborated_dead   = authoritative_dead or (p.get('_deprecated') and p.get('_dead_url')) \
                                  or (p.get('_dead_url') and (p.get('_tvl') or 0)>0)
            if corroborated_dead:
                code['unmaintained_or_differing_code_path']=P
            elif p.get('_deprecated'):
                code['unmaintained_or_differing_code_path']=U
                notes.append("CAUTION: DefiLlama's `deprecated` flag is set but uncorroborated. That flag is also "
                             "used when an adapter is superseded or its TVL is counted elsewhere, so on its own it "
                             "does NOT establish an abandoned deployment. Treated as UNKNOWN (no positive score).")
            else:
                code['unmaintained_or_differing_code_path']=U
            if dead.get('deadFrom'):
                notes.append(f"listed in DefiLlama registries/deadAdapters.json, deadFrom={dead['deadFrom']}"
                             + (f"; hallmarks: {json.dumps(dead.get('hallmarks'))[:180]}" if dead.get('hallmarks') else ""))
            state['still_holds_value_or_authority']= P if (p.get('_tvl') or 0)>0 else A
            state['not_paused']= P if any(x.get('paused') is False for x in ap) else U
            guards['paused_and_drained']= 'FOUND' if any(x.get('paused') for x in ap) else ('NOT_FOUND' if ap else U)
            guards['approvals_revoked']=U
            if p.get('_deprecated'): notes.append("DefiLlama deprecated flag set with non-zero residual TVL")
            if p.get('_dead_url'): notes.append("front end dead; contracts still hold value")
            lineage=13.0 if dead.get('deadFrom') else (10.0 if p.get('_forked_from') else 0.0)
        reach = P if (p.get('_tvl') or 0)>0 else U

    elif fid in ('ORACLE-STALE-OR-SILENT-FALLBACK','ORACLE-SPOT-THIN-LIQUIDITY',
                 'ORACLE-VAULT-SHARE-RATE-AS-SPOT-PRICE','LIQUIDATION-ON-MANIPULABLE-VALUATION'):
        orc=p.get('_oracles') or []
        code['value_decision_reads_configured_feed']= P if (comp.get('markets') or cur.get('vault_reads') or p.get('_cat') in
             ('Lending','CDP','RWA Lending','Derivatives','Risk Curators')) else U
        code['feed_selection_is_configuration']= P if orc else U
        code['failure_path_returns_usable_number']=U
        state['live_positions_exposed']= P if any((m.get('totalBorrows') or 0)>0 for m in comp.get('markets',[])) else U
        state['single_or_undeclared_oracle']= P if len(orc)<=1 else A
        guards['staleness_check_reverts']=U
        guards['deviation_bound_vs_independent_source']= 'NOT_FOUND' if len(orc)<=1 else U
        guards['caps_sized_to_venue_depth']= 'FOUND' if any(m.get('supplyCap') for m in comp.get('markets',[])) else U
        provs=aav.get('providers',[])
        if provs:
            oa=[x for x in provs if x.get('priceOracle')]
            code['feed_selection_is_configuration']= P if oa else code['feed_selection_is_configuration']
            state['live_positions_exposed']= P if any((x.get('reserve_count') or 0)>0 for x in provs) else state['live_positions_exposed']
            notes.append("addresses-provider probe: "+"; ".join(
                f"{x['addressesProvider'][:10]}… priceOracle={str(x.get('priceOracle'))[:12]} "
                f"pool={str(x.get('pool'))[:12]} reserves={x.get('reserve_count')} owner={str(x.get('owner'))[:12]}"
                for x in provs[:3]))
            if any(x.get('owner') for x in provs):
                notes.append("addresses-provider owner is a live address: oracle re-registration is a configuration action, "
                             "so feed-to-asset binding depends on that role, not on code")
        notes.append(f"declared oracles: {', '.join(orc) if orc else 'none declared in DefiLlama metadata'}")
        if p.get('_forked_from'): lineage=9.0
        reach = P if state.get('live_positions_exposed')==P else U

    elif fid=='ACC-ZERO-SUPPLY-INFLATION':
        lm=comp.get('markets',[])
        dust=[m for m in lm if (m.get('totalSupply') or 0)==0 or (0<(m.get('totalSupply') or 0)<10**6)]
        code['share_formula_has_zero_branch']=U
        code['permissionless_market_or_vault_creation']= P if ad.get('uses_factory_or_registry') else U
        state['dust_or_zero_supply_markets_live']= P if dust else (A if lm else U)
        guards['virtual_shares_or_dead_shares']=U
        if dust: notes.append(f"{len(dust)}/{len(lm)} probed markets have zero or dust share supply "
                              "(the zero-supply branch is reachable on those)")
        reach = P if dust else U

    elif fid=='GOV-CHEAP-CONTROL-NO-TIMELOCK':
        code['governance_can_move_value_mint_or_upgrade']= P if p.get('_governance') else A
        code['decisive_voting_power_cheaper_than_controlled_value']=U
        state['no_timelock_or_timelock_shorter_than_response_window']=U
        state['live_value_or_approvals_reachable_by_governance']= P if (p.get('_tvl') or 0)>0 else A
        guards['timelock_plus_guardian_veto']=U
        guards['quorum_scaled_to_controlled_value']=U
        notes.append("Cost to acquire decisive voting power was NOT measured against controlled value, and timelock "
                     "parameters were NOT read on-chain. Both remain UNKNOWN and therefore score zero: this pair is "
                     "listed as an open question about governance economics, not as an assertion that control is cheap.")
        reach=U
        lineage=0.0

    else:  # generic families: metadata + adapter evidence only
        notes.append("GENERIC-FAMILY SCREEN: no family-specific precondition was verified for this pair. "
                     "Evidence is adapter-level architecture only, so the score is capped at the L1 adapter ceiling "
                     "and this pair is preliminary by construction.")
        code['_generic_family_adapter_only']=P
        code['family_architecture_signals_in_adapter']= P if (ad.get('status','').startswith('READ') and
            (ad.get('uses_factory_or_registry') or ad.get('hardcoded_address_count'))) else U
        state['live_value_present']= P if (p.get('_tvl') or 0)>0 else A
        guards['decisive_guard_reviewed']=U
        reach=U
        if ad.get('status','').startswith('READ'):
            notes.append(f"adapter `{ad.get('module')}` read: "
                         f"{ad.get('hardcoded_address_count',0)} hardcoded addresses, "
                         f"dynamic={ad.get('uses_factory_or_registry')}, external API={ad.get('uses_external_api')}")
    return code,state,guards,lineage,reach,notes

def level(slug,fid,code,state):
    ad=AD.get(slug,{}); pr=PR.get(slug,{})
    has_state=any(v==P for v in state.values()) and bool(pr)
    has_impl = bool((pr.get('compound',{}).get('market_source') or {}).get('verified')) or \
               any(x.get('erc1967_implementation') or x.get('code_size') for x in pr.get('deployment',{}).get('addresses_probed',[])) or \
               bool(pr.get('aave',{}).get('providers')) or bool(pr.get('curator',{}).get('vault_reads'))
    guard_reviewed = bool((pr.get('compound',{}).get('market_source') or {}).get('verified'))
    if guard_reviewed: return 'L4_GUARD_REVIEW'
    if has_state and has_impl: return 'L3_STATE'
    if has_impl: return 'L2_DEPLOYMENT'
    if ad.get('status','').startswith('READ'): return 'L1_ADAPTER'
    return 'L0_METADATA'

SANCTIONED={'tornado-cash','tornado-cash-classic','sinbad','blender'}
def score(pair):
    slug,fid=pair['protocol_slug'],pair['family_id']
    if slug in SANCTIONED:
        return {"killed":True,"kill_reason":"SANCTIONS_DESIGNATED_NO_LAWFUL_ENGAGEMENT",
                "killed_conditions":["responsible-disclosure recipient"],
                "code":{},"state":{},"guards":{},
                "notes":["Excluded from candidate promotion: the entity is sanctions-designated, so an authorized "
                         "defensive engagement has no lawful disclosure recipient and no remediation path. "
                         "A discovery-stage candidate presumes a party who can receive a disclosure and deploy a fix."]}
    code,state,guards,lineage,reach,notes=evaluate(slug,fid,pair)
    # Documented decisive guards found during prior-art research override the read-only screen.
    pa=PRIOR.get(f"{slug}|{fid}",{})
    dg=pa.get('downgrade') or {}
    if dg.get('apply'):
        guards[dg.get('guard','documented_decisive_guard')]='FOUND'
        notes.append("prior-art research found a documented decisive guard: "+pa.get('basis','')[:300])
        if dg.get('disposition')=='KILLED':
            return {"killed":True,"kill_reason":"DECISIVE_GUARD_FOUND",
                    "guards_found":[dg.get('guard')],"prior_art_status":pa.get('status'),
                    "residual_hypothesis":dg.get('residual_hypothesis'),
                    "code":code,"state":state,"guards":guards,"notes":notes}
    # --- mandatory-precondition gate ---
    if any(v==A for v in code.values()) or any(v==A for v in state.values()):
        killed=[k for k,v in {**code,**state}.items() if v==A]
        return {"killed":True,"kill_reason":"MANDATORY_PRECONDITION_PROVEN_ABSENT",
                "killed_conditions":killed,"code":code,"state":state,"guards":guards,"notes":notes}
    PRIMARY_GUARDS={
      'ACC-DONATION-UNACCOUNTED-BALANCE':{'internal_cash_counter'},
      'UPGRADE-OLD-DEPLOYMENT-LIVE-AUTHORITY':{'paused_and_drained'},
      'ACC-ZERO-SUPPLY-INFLATION':{'virtual_shares_or_dead_shares'},
      'UPGRADE-INITIALIZER-REACHABLE-LIVE':{'initializer_consumed'},
    }
    found=[k for k,v in guards.items() if v=='FOUND']
    prim=[k for k in found if k in PRIMARY_GUARDS.get(fid,set())]
    evaluated=[g for g in guards if guards[g]!=U]
    if prim:
        return {"killed":True,"kill_reason":"DECISIVE_GUARD_FOUND","guards_found":prim,
                "code":code,"state":state,"guards":guards,"notes":notes}
    if found and len(found)*2 > max(1,len(evaluated)):
        return {"killed":True,"kill_reason":"DECISIVE_GUARD_FOUND","guards_found":found,
                "code":code,"state":state,"guards":guards,"notes":notes}
    # --- MATCH_SCORE ---
    def frac(dd):
        rel=[v for v in dd.values() if v!=NA]
        return (sum(1 for v in rel if v==P)/len(rel)) if rel else 0.0
    ms  = 20.0                                   # archetype applicable (gate already passed)
    ms += 25.0*frac(code)                        # mandatory architectural/code prerequisites
    ms += 20.0*frac(state)                       # mandatory live-state/config prerequisites
    ms += min(15.0,lineage)                      # lineage similarity
    ms += 10.0 if reach==P else 0.0              # live unprivileged reachability plausible
    ms += 10.0 if all(v!='FOUND' for v in guards.values()) and any(v=='NOT_FOUND' for v in guards.values()) else 0.0
    lvl=level(slug,fid,code,state)
    if code.get('_generic_family_adapter_only')==P: lvl='L1_ADAPTER'
    caps={'L0_METADATA':20,'L1_ADAPTER':45}
    if lvl in caps: ms=min(ms,caps[lvl])
    impl_resolved = lvl in ('L3_STATE','L4_GUARD_REVIEW') or \
                    bool((PR.get(slug,{}).get('compound',{}).get('market_source') or {}).get('verified'))
    if not impl_resolved: ms=min(ms,60)
    # --- EVIDENCE_CONFIDENCE (published separately) ---
    ad=AD.get(slug,{}); pr=PR.get(slug,{})
    ec={
     "mapping_completeness": 100 if ad.get('status','').startswith('READ') and ad.get('hardcoded_address_count') else
                              (70 if ad.get('status','').startswith('READ') else 20),
     "deployment_parity_confidence": 90 if (pr.get('compound',{}).get('market_source') or {}).get('verified') else
                              (75 if pr.get('aave',{}).get('providers') else
                              (55 if pr.get('deployment',{}).get('addresses_probed') else 15)),
     "live_state_completeness": 85 if (pr.get('compound',{}).get('markets') or pr.get('curator',{}).get('vault_reads')
                                       or pr.get('aave',{}).get('providers')) else
                              (50 if pr.get('deployment',{}).get('addresses_probed') else 10),
     "source_corroboration": 90 if FAM[fid]['evidence_strength']=='HIGH' else 65,
     "guard_review_depth": 80 if any(v!=U for v in guards.values()) else 15,
    }
    EC=round(sum(ec.values())/len(ec),1)
    # --- PREVENTION_SCORE ---
    tvl=pair.get('tvl') or 0
    exposure=tvl
    auth=[]
    if pair.get('governance'): exposure*=1.15; auth.append('on-chain governance authority')
    if fid in ('CALLDATA-CALLER-CONTROLLED-TARGET','CALLBACK-UNAUTHENTICATED-CALLER-USES-APPROVALS',
               'APPROVALS-TO-UPGRADEABLE-SPENDER'):
        exposure=max(exposure,tvl)+0  # approvals not enumerated; recorded as unresolved exposure
        auth.append('live user approvals not enumerated (exposure understated)')
    if fid=='ACC-NAV-SHAREPRICE-MANIPULABLE': auth.append('curator authority over third-party vaults')
    EXP=round(min(1.2, math.log10(max(exposure,1))/10),4)
    rec=d(FAM[fid]['most_recent_event']) if FAM[fid]['most_recent_event'] else WSTART
    FRF=round(0.70+0.30*max(0.0,min(1.0,(rec-WSTART).days/max(1,(WEND-WSTART).days))),4)
    urc=FAM[fid]['unique_root_cause_count']
    RECUR=round(1.0+0.05*min(max(urc-2,0),4),3)
    PS=round(ms*(EC/100.0)*EXP*FRF*RECUR,3)
    return {"killed":False,"MATCH_SCORE":round(ms,1),"EVIDENCE_CONFIDENCE":EC,
            "evidence_confidence_components":ec,"PREVENTION_SCORE":PS,
            "EXPOSURE_INDEX":EXP,"FAMILY_RECENCY_FACTOR":FRF,"RECURRENCE_MULTIPLIER":RECUR,
            "exposure_basis_usd":round(exposure,2),"authority_notes":auth,
            "evidence_level":lvl,"code":code,"state":state,"guards":guards,"notes":notes}

out=[]
for w in W:
    s=score(w)
    out.append({**w,**s})

with open(f'{B}/protocols/deep_screened.jsonl','w') as fh:
    for o in out: fh.write(json.dumps(o,ensure_ascii=False)+"\n")
live=[o for o in out if not o['killed']]
print(json.dumps({"pairs":len(out),"killed":len(out)-len(live),
 "killed_by_precondition":sum(1 for o in out if o.get('kill_reason')=='MANDATORY_PRECONDITION_PROVEN_ABSENT'),
 "killed_by_guard":sum(1 for o in out if o.get('kill_reason')=='DECISIVE_GUARD_FOUND'),
 "surviving":len(live),
 "by_level":collections.Counter(o['evidence_level'] for o in live),
 "top_match":[(o['protocol_slug'],o['family_id'],o['MATCH_SCORE'],o['EVIDENCE_CONFIDENCE'],o['evidence_level'])
              for o in sorted(live,key=lambda x:-x['MATCH_SCORE'])[:12]],
 "top_prevention":[(o['protocol_slug'],o['family_id'],o['PREVENTION_SCORE'],f"${o['tvl']:,.0f}")
              for o in sorted(live,key=lambda x:-x['PREVENTION_SCORE'])[:12]]},indent=2))
