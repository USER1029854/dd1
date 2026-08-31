# -*- coding: utf-8 -*-
"""Feature definitions shared by the lift analysis and production scoring.

One copy only. An earlier revision kept a second copy inside feature_lift.py and
the two drifted, so the weights were fitted on a slightly different feature set
than production evaluated. Both now import from here.

A note on what may be measured retrospectively
----------------------------------------------
Features are only admitted to the LEARNED weights if their value cannot have been
caused by the incident being predicted:

  admitted   listedAt (immutable), audits, fork lineage, chain/category, tags,
             deployed-source shape, adapter registry state
  attenuated admin posture -- read today, and teams often harden after being hit,
             so a real effect is understated here, never overstated
  refused    market cap and TVL trajectory. Both are read today; for a victim they
             partly measure the hack's own outflow. They are carried as
             ORDERING-ONLY operational signals and never enter the fitted weights.
"""
import sys,datetime
sys.path.insert(0,'/home/user/dd1/incident-intelligence/tools')
import hazard as HZ

# Refused because their value today is partly caused by the incident being predicted.
ORDERING_ONLY={'tvl_falling_fast','tvl_rising_fast','mcap_below_tvl','mcap_absent'}

# Refused on measurement, not on principle. tools/ablation.py refits the whole model
# with each group held out and revalidates on 95 protocols hacked after the fitting
# window. Adding admin posture moved out-of-sample lift x2.19 -> x2.15, i.e. it made
# the prediction slightly worse, while exposure age moved it x2.19 -> x2.32. Over the
# full 2024+ window these signals measure ~1.0 (admin_terminal_eoa x0.98,
# admin_single_signature x0.96): single-key custody does NOT predict a code defect.
# That is the expected answer -- key compromise is an excluded root cause here -- and
# it is why custody is reported on its own in results/upgrade_authority_exposure.md
# instead of being folded into a likelihood score.
EXCLUDED_BY_ABLATION={'admin_terminal_eoa','admin_single_signature','admin_multisig',
                      'admin_timelocked','admin_no_delay_path'}
NOT_FITTED=ORDERING_ONLY|EXCLUDED_BY_ABLATION
NOW=datetime.datetime(2026,8,23,tzinfo=datetime.timezone.utc).timestamp()

def _age_years(p,asof=None):
    t=p.get('listedAt')
    if not isinstance(t,(int,float)) or t<=0: return None
    a=((asof or NOW)-t)/31557600.0
    return a if a>=0 else None

def feats(s,p,PR,asof=None,AD=None):
    """asof: evaluation instant (a victim's incident date, else now) -- used only
    for age, which is the one time-varying feature that is safe to measure.
    AD: admin posture index, optional."""
    pr=(PR or {}).get(s,{}); ap=pr.get('deployment',{}).get('addresses_probed',[])
    sw=pr.get('source_sweep',{}); c=set(p.get('_conditions') or [])
    tvl=p.get('_tvl') or 0
    age=_age_years(p,asof)
    ch7=p.get('change_7d'); mc=p.get('mcap')
    post=((AD or {}).get(s) or {}).get('posture')
    f={
     'no_audit_listed': not p.get('_audit_links'),
     'single_audit_only': len(p.get('_audit_links') or [])==1,
     'has_2plus_audits': len(p.get('_audit_links') or [])>=2,
     'dead_front_end': bool(p.get('_dead_url')),
     'deprecated_flag': bool(p.get('_deprecated')),
     'has_fork_lineage': bool(p.get('_forked_from')),
     'misrepresented_tokens': bool(p.get('_misrep')),
     'has_governance': bool(p.get('_governance')),
     'multichain_gt3': len(p.get('_chains') or [])>3,
     'single_chain': len(p.get('_chains') or [])==1,
     'rebranded': 'REBRANDED_DEPLOYMENT' in c,
     'version_sibling_legacy': 'VERSION_SIBLING_LEGACY' in c,
     'dead_adapter_registry': 'DEAD_ADAPTER_WITH_RESIDUAL_TVL' in c,
     'declared_fallback_oracle': 'DECLARED_FALLBACK_ORACLE' in c,
     'pricing_surface_undeclared': 'PRICING_SURFACE_UNDECLARED' in c,
     'rwa_pricing_surface': 'RWA_PRICING_SURFACE' in c,
     'authority_addrs_beyond_tvl': 'AUTHORITY_ADDRESSES_BEYOND_TVL' in c,
     'tag_clmm': 'TAG_CLMM' in c,
     'has_oracle_declared': bool(p.get('_oracles')),
     'owner_is_eoa': any(a.get('owner_is_eoa') for a in ap),
     'owner_is_contract': any(a.get('owner_is_contract') for a in ap),
     'is_proxy': any(a.get('is_proxy') for a in ap),
     'unverified_implementation': any(x.get('status')=='IMPLEMENTATION_NOT_VERIFIED' for x in sw.get('contracts',[])),
     'tvl_under_500k': tvl<500_000,
     'tvl_500k_5m': 500_000<=tvl<5_000_000,
     'tvl_over_5m': tvl>=5_000_000,
     'cat_hazard_ge2': HZ.category_hazard(p.get('_cat'))>=2.0,
     'chain_hazard_ge2': HZ.chain_hazard(p.get('_chains'))>=2.0,
     'on_ethereum': 'Ethereum' in (p.get('_chains') or []),
     'on_bsc': any(x in ('Binance','BSC') for x in (p.get('_chains') or [])),
     # --- added in v4: exposure age, measured at the evaluation instant ---
     'age_under_1y': age is not None and age<1.0,
     'age_1_3y': age is not None and 1.0<=age<3.0,
     'age_over_3y': age is not None and age>=3.0,
     'no_public_repo': not p.get('_github'),
     # --- added in v4: measured upgrade authority (attenuated, see docstring) ---
     'admin_terminal_eoa': post=='EOA_SINGLE_KEY',
     'admin_single_signature': post in ('EOA_SINGLE_KEY','SAFE_1_OF_N'),
     'admin_multisig': post=='SAFE_M_OF_N',
     'admin_timelocked': post in ('TIMELOCK','GOVERNOR'),
     'admin_no_delay_path': post in ('EOA_SINGLE_KEY','SAFE_1_OF_N','SAFE_M_OF_N','TIMELOCK_ZERO_DELAY'),
     # --- ORDERING ONLY: never fitted, see ORDERING_ONLY ---
     'tvl_falling_fast': isinstance(ch7,(int,float)) and ch7<=-20.0,
     'tvl_rising_fast': isinstance(ch7,(int,float)) and ch7>=20.0,
     'mcap_below_tvl': isinstance(mc,(int,float)) and mc>0 and tvl>0 and mc<tvl,
     'mcap_absent': not isinstance(mc,(int,float)) or not mc,
    }
    return f
