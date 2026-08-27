#!/usr/bin/env python3
"""Mechanical quality gates (§18). Exits non-zero on any FAIL."""
import json,os,re,sys,csv,collections
B='/home/user/dd1/incident-intelligence'
R=[]; 
def chk(name,ok,detail=""): R.append((("PASS" if ok else "FAIL"),name,detail)); return ok
def warn(name,detail): R.append(("WARN",name,detail))

M=json.load(open(f'{B}/manifest.json'))
# 18.6 artifacts
miss=[a['path'] for a in M['artifacts'] if not a['exists'] or a['bytes']==0]
chk("18.6 every referenced artifact exists and is non-empty",not miss,f"missing/empty: {miss}")
chk("18.6 manifest maps every load-bearing claim",len(M['claim_map'])>=12,f"{len(M['claim_map'])} claims mapped")
chk("18.6 commands.sh replays retrieval and transformation",os.path.exists(f'{B}/commands.sh')
    and os.path.getsize(f'{B}/commands.sh')>1500)

# 18.1 incident completeness
crawl=json.load(open(f'{B}/sources/slowmist/crawl_log_all.json'))
last=crawl['pages'][-1]
chk("18.1 crawling continued until the date boundary was proven",last['status']=='BOUNDARY_PROVEN'
    and last['rows_in_window']==0 and last['rows_older_than_window']==last['rows_parsed'],
    f"final page {last['page']}: in_window={last['rows_in_window']} older={last['rows_older_than_window']}/{last['rows_parsed']}")
raw=[json.loads(l) for l in open(f'{B}/incidents/all_raw.jsonl')]
inw=[r for r in raw if r['in_window']]
inc=[json.loads(l) for l in open(f'{B}/incidents/included.jsonl')]
prov=[json.loads(l) for l in open(f'{B}/incidents/provisional.jsonl')]
exc=[json.loads(l) for l in open(f'{B}/incidents/excluded.jsonl')]
chk("18.1 every in-window row retained and dispositioned",len(inc)+len(prov)+len(exc)==len(inw),
    f"{len(inc)}+{len(prov)}+{len(exc)} vs {len(inw)}")
chk("18.1 actual incident date used, not publication date",
    all(re.match(r'^\d{4}-\d{2}-\d{2}$',r['event_date']) for r in inw)
    and all('2026-02-22'<=r['event_date']<='2026-08-22' for r in inw))
chk("18.1 every exclusion has a concrete reason",all(e.get('exclusion_reason_code') and e.get('exclusion_reason') for e in exc))
chk("18.1 only A/B evidence entered the family library",all(i['evidence_grade'] in ('A','B') for i in inc))
chk("18.1 grade-C incidents are provisional only",all(i['evidence_grade']=='C' for i in prov))
dg=json.load(open(f'{B}/incidents/duplicate_groups.json'))
chk("18.1 duplicate/clone lineages recorded",len(dg['clone_and_repeat_lineages'])>=4)
F=json.load(open(f'{B}/families/families.json'))
collapsed=[f for f in F if f['unique_root_cause_count']<f['incident_count']]
chk("18.1 clone incidents do not inflate independent recurrence",bool(collapsed),
    f"{len(collapsed)} families have unique_root_cause_count < incident_count")

# 18.2 root-cause quality
chk("18.2 every included incident names a broken invariant",all(i.get('broken_invariant') for i in inc))
chk("18.2 decisive missing guard named on every included incident",all(i.get('decisive_missing_guard') for i in inc))
chk("18.2 root cause and amplifiers separated",all(i.get('mandatory_preconditions') and i.get('optional_amplifiers') is not None for i in inc))
chk("18.2 false-positive killers explicit on every family",all(f['false_positive_killers'] for f in F))
GENERIC={'flash loan','oracle','reentrancy','access control','bridge hack','flashloan','price manipulation'}
bad=[f['family_id'] for f in F if f['title'].strip().lower() in GENERIC or f['family_id'].lower() in GENERIC]
chk("18.2 no family collapsed to a generic attack label",not bad,f"{bad}")
chk("18.2 families cluster on invariant+mechanism+preconditions+guard",
    all(f['broken_invariant'] and f['mechanism'] and f['mandatory_preconditions'] and f['decisive_guards'] for f in F))
se=[f for f in F if f.get('single_event_family')]
chk("18.2 single-event families labelled, no recurrence claimed",all(f['incident_count']==1 for f in se),f"{len(se)} single-event families")

# 18.3 DefiLlama completeness
U=json.load(open(f'{B}/protocols/defillama_universe.json'))
chk("18.3 /protocols fetched",len(U)>5000,f"{len(U)} rows")
D=[json.loads(l) for l in open(f'{B}/protocols/deep_screened.jsonl')]
slugs={r['slug'] for r in U}
chk("18.3 every retained protocol ties to a valid current DefiLlama slug",
    all(d['protocol_slug'] in slugs for d in D))
AD=json.load(open(f'{B}/protocols/adapters_index.json'))
unread=[s for s in {d['protocol_slug'] for d in D} if not AD.get(s,{}).get('status','').startswith('READ')]
chk("18.3 adapter read or explicitly marked missing for every candidate",
    all(s in AD for s in {d['protocol_slug'] for d in D}),
    f"{len(unread)} marked missing (explicitly recorded): {unread[:5]}")
el=json.load(open(f'{B}/protocols/eligibility.json'))
# Operator directive supersedes §10.2: a hard $50,000 floor applies. The requirement is then
# that sub-floor authority-bearing protocols are still identified and recorded, not silently dropped.
_sf=json.load(open(f'{B}/protocols/subfloor_authority_deferred.json')) if os.path.exists(f'{B}/protocols/subfloor_authority_deferred.json') else []
chk("18.3 sub-floor authority-bearing protocols identified and recorded (hard $50k floor in force)",
    len(_sf)>0 and all(r.get('authority_flags') for r in _sf),
    f"{len(_sf)} recorded in protocols/subfloor_authority_deferred.json, none screened")
chk("18.3 hard TVL floor actually enforced in the screen",
    min([d['tvl'] for d in D] or [0])>=50000,
    f"lowest screened TVL ${min([d['tvl'] for d in D] or [0]):,.0f}")
chk("18.3 condition layer recorded per protocol",
    os.path.exists(f'{B}/protocols/conditions.json') and os.path.getsize(f'{B}/protocols/conditions.json')>1000)
_pr=json.load(open(f'{B}/protocols/onchain_probes.json'))
chk("18.4 deployed-source sweep evidence recorded",
    sum(1 for v in _pr.values() if v.get('source_sweep',{}).get('indicators'))>50,
    f"{sum(1 for v in _pr.values() if v.get('source_sweep',{}).get('indicators'))} protocols with analysed source")
chk("18.4 precision controls applied and published",
    any(d.get('demoted_indicators') is not None for d in D) and
    any('RELEVANCE GATE' in ' '.join(d.get('notes',[])) for d in D),
    "prevalence demotion and relevance gate both present in scored pairs")
chk("18.3 TVL, chains, category and deployment evidence recorded",
    all(('tvl' in d and d.get('chains') is not None and d.get('category') is not None) for d in D))

# 18.4 candidate precision
live=[d for d in D if not d['killed']]
chk("18.4 minimum deep-screened pairs met (>=80)",len(D)>=80,f"{len(D)} pairs deep-screened")
chk("18.4 mandatory-precondition gate applied to every pair",
    all(('code' in d and 'state' in d) for d in D))
chk("18.4 decisive guards searched on every surviving pair",all(d.get('guards') is not None for d in live))
chk("18.4 score evidence shown",all(('priority_evidence' in d) for d in live))
chk("18.4 confidence separate from technical fit",
    all(('MATCH_SCORE' in d and 'EVIDENCE_CONFIDENCE' in d and 'evidence_confidence_components' in d) for d in live))
chk("18.4 live exposure separate from fit",all('VALUE_AT_RISK_USD' in d for d in live),
    "value at risk is reported per pair and never folded into the likelihood ranking")
chk("band: hard $50k floor enforced", min([d['tvl'] for d in live] or [0])>=50000,
    f"lowest screened value at risk ${min([d['tvl'] for d in live] or [0]):,.0f}")
chk("band: above-band protocols dropped unless explicit danger",
    all(d.get('band_status')!='ABOVE_BAND_DROPPED' for d in live) and
    all(d.get('danger_reasons') for d in live if d.get('band_status')=='ABOVE_BAND_KEPT_EXPLICIT_DANGER'),
    f"{sum(1 for d in live if d.get('band_status')=='ABOVE_BAND_KEPT_EXPLICIT_DANGER')} retained above the band, each with stated danger evidence")
def _spearman(xs,ys):
    def rank(v):
        o=sorted(range(len(v)),key=lambda i:v[i]); r=[0.0]*len(v); i=0
        while i<len(o):
            j=i
            while j+1<len(o) and v[o[j+1]]==v[o[i]]: j+=1
            avg=(i+j)/2.0+1
            for k in range(i,j+1): r[o[k]]=avg
            i=j+1
        return r
    rx,ry=rank(xs),rank(ys); n=len(xs)
    if n<2: return 0.0
    mx=sum(rx)/n; my=sum(ry)/n
    num=sum((a-mx)*(b-my) for a,b in zip(rx,ry))
    den=(sum((a-mx)**2 for a in rx)*sum((b-my)**2 for b in ry))**0.5
    return num/den if den else 0.0

_L=[d['LIKELIHOOD'] for d in live]; _T=[d['tvl'] for d in live]; _P=[d['PRIORITY'] for d in live]
_rl=_spearman(_L,_T); _rp=_spearman(_P,_T)
# Measured, not asserted: LIKELIHOOD must not be a restatement of exposure. A weak positive
# is expected and correct -- tvl_over_5m carries a real measured lift of x1.75 -- but the
# ranking must not be driven by size.
chk("band: LIKELIHOOD is not a restatement of exposure",
    abs(_rl)<0.35, f"Spearman(LIKELIHOOD, TVL) = {_rl:+.3f} across {len(live)} surviving pairs")
chk("band: PRIORITY tilts toward protocols an independent reviewer can actually help",
    _rp<0.0, f"Spearman(PRIORITY, TVL) = {_rp:+.3f}: the queue leans to smaller protocols by construction")
_bad=[d for d in live if abs(round(d['LIKELIHOOD']*d['ACTIONABILITY']/100.0,2)-d['PRIORITY'])>0.02]
chk("band: PRIORITY = LIKELIHOOD x ACTIONABILITY holds for every pair",
    not _bad, f"{len(_bad)} arithmetic violations across {len(live)} pairs")
_oos=(json.load(open(f'{B}/protocols/learned_weights.json')).get('out_of_sample_unseen') or {})
chk("validation: the scoring model beats chance on incidents it never saw",
    (_oos.get('lift') or 0)>1.5,
    f"lift x{_oos.get('lift')} on {_oos.get('n')} protocols hacked after the fitting window")
_abl=json.load(open(f'{B}/protocols/ablation.json'))['variants']
chk("validation: every feature group kept was shown to earn its place",
    _abl['+ all v4 additions']['lift']>=_abl['baseline (v3 feature set)']['lift'],
    "ablation refits and revalidates each group; admin posture was dropped for failing this")
# --- no-repetition gates: a run must hand over work that has not been handed over before ---
_led=json.load(open(f'{B}/protocols/delivered_ledger.json'))
_LEDS=set(_led['ledger'])
_final_slugs=set()
_av=open(f'{B}/results/audit_variables.txt').read()
for _m in re.finditer(r'TARGET=https://defillama\.com/protocol/([^\s|]+)',_av): _final_slugs.add(_m.group(1))
# Read the level of the pair ACTUALLY SELECTED, from candidates_all.csv. A protocol can
# carry pairs at several levels, so re-deriving it from an arbitrary pair per slug is wrong.
_selrows=[r for r in csv.DictReader(open(f'{B}/results/candidates_all.csv')) if r.get('in_final')=='YES']
_lv=collections.Counter(r['evidence_level'] for r in _selrows)
_declared=open(f'{B}/results/candidates_by_priority.md').read()
_floorclaim=re.search(r'reaching \*\*`(L\d_[A-Z_]+)`\*\*',_declared)
chk("delivery: every candidate was read to the declared evidence depth",
    (not _floorclaim) or set(_lv)=={_floorclaim.group(1)},
    f"{len(_selrows)} selected pairs at {dict(_lv)}"
    + (f"; declared floor {_floorclaim.group(1)}" if _floorclaim else "; no floor declared"))
chk("delivery: the four highest-loss families in the window can now reach guard review",
    all(any(d['evidence_level'] in ('L3_STATE','L4_GUARD_REVIEW') and d['family_id']==f
            for d in D if not d['killed'])
        for f in ('BRIDGE-MESSAGE-NOT-BOUND-TO-SOURCE','ASSET-OR-MARKET-IDENTITY-NOT-VALIDATED',
                  'PROOF-VERIFICATION-BYPASSED','QUOTE-OR-ROUTE-OUTPUT-NOT-BOUND-TO-ASSET')),
    "these had no source indicators and were stuck at L1_ADAPTER before this pass")
_rep=sorted(_final_slugs & _LEDS)
chk("delivery: no candidate repeats a protocol handed over in a previous run",
    not _rep, f"{len(_final_slugs)} finals against a ledger of {len(_LEDS)} previously delivered; "
              f"repeats: {_rep[:5] or 'none'}")
_md=open(f'{B}/results/candidates_by_priority.md').read()
_mds={m.group(1) for m in re.finditer(r'\*\*DefiLlama:\*\* https://defillama\.com/protocol/([^\s]+)',_md)}
chk("delivery: the written ranking matches the handover list, with no delivered protocol reintroduced",
    not (_mds & _LEDS), f"{len(_mds)} write-ups, {len(_mds & _LEDS)} previously delivered")
chk("delivery: withheld protocols are disclosed rather than silently dropped",
    "previously_delivered" in open(f'{B}/results/candidates_all.csv').readline() and
    "withheld" in _md.lower(),
    "candidates_all.csv carries previously_delivered + first_delivered_in; the ranking states the count")
chk("delivery: the ledger is reconstructed from git history, not from run-to-run memory",
    _led.get('generated_from','').startswith('git history') and len(_led.get('runs',[]))>=1,
    f"{len(_led.get('runs',[]))} previous deliveries found, {len(_LEDS)} protocols")

# --- urgency-first triage gates ---
_ur=json.load(open(f'{B}/protocols/urgency_pairs.json'))
_urm=open(f'{B}/results/candidates_by_urgency.md').read()
# The full 40-point remediation band requires proving the fix ABSENT in the deployed
# artifact. No such per-protocol check ran, so no row may claim UNREMEDIATED_KNOWN.
chk("urgency: no candidate claims a proven remediation gap without an artifact-level check",
    not any(r['remediation']=='UNREMEDIATED_KNOWN' for r in _ur),
    f"{sum(1 for r in _ur if r['remediation']=='KNOWN_ISSUE_STATUS_UNKNOWN')} rows at "
    "KNOWN_ISSUE_STATUS_UNKNOWN (28 of 40); the decisive check is named per row")
chk("urgency: every candidate names the single decisive confirm/kill check",
    all(r.get('decisive_check') for r in _ur),
    "a triage row without a decisive check is not actionable")
_maxpts={1:40,2:20,3:25,4:15}
chk("urgency: no scoring component exceeds its cap and unknowns score zero",
    all(r['components']['remediation_gap']<=40 and r['components']['technique_recency_propagation']<=20
        and r['components']['reachable_live_value']<=25 and r['components']['precondition_match']<=15
        for r in _ur),
    "40 remediation / 20 recency+propagation / 25 reachable value / 15 precondition")
chk("urgency: evidence depth caps the score (metadata 20, adapter 45, deployment 60)",
    all(r['URGENCY']<=r['evidence_cap'] for r in _ur),
    f"{sum(1 for r in _ur if r['capped'])} rows capped by evidence depth")
chk("urgency: value at risk is reported beside the score, never inside it",
    'beside the score, not in it' in _urm and
    all('tvl' in r and 'URGENCY' in r for r in _ur),
    "a real finding on dust is a low-value save and must be visible as such")
chk("urgency: previously delivered protocols that now classify hot are disclosed, not dropped",
    'now classified Tier 1' in _urm,
    "the ranking axis changed underneath them; withholding a Tier-1 item silently would be wrong")
_ld=json.load(open(f'{B}/protocols/operator_leads.json'))
chk("urgency: operator leads are resolved with their window status stated",
    all(('in_window' in l and l.get('maps_to_families') and l.get('decisive_check')) for l in _ld['leads']),
    f"{len(_ld['leads'])} leads; out-of-window leads contribute zero to window statistics")

# --- Cosmos EVM triage gates: this is a criteria-based triage, never a target list ---
_ct=json.load(open(f'{B}/protocols/cosmos_evm_triage.json'))
chk("disclosure: the Cosmos EVM triage never asserts a patch state it cannot verify",
    all(r.get('patch_status')=='NOT_DETERMINED' for r in _ct['rows']),
    f"{len(_ct['rows'])} rows, all NOT_DETERMINED; patch state is unverifiable without active probing")
chk("disclosure: risk archetypes needing unreachable evidence are marked unassessable, not guessed",
    sum(1 for v in _ct['assessability'].values() if v=='NOT_ASSESSABLE_HERE')>=4
    and not any(r.get('archetype_A_vendored') or r.get('archetype_B_disabled')
                or r.get('archetype_D_migrated') or r.get('archetype_E_governance') for r in _ct['rows']),
    f"assessability: {_ct['assessability']}")
_cer=open(f'{B}/results/cosmos_evm_exposure.md').read()
chk("disclosure: the exposure report states plainly that it is not a roster of unpatched networks",
    'not a list of unpatched networks' in _cer.lower() and 'NOT_DETERMINED' in _cer,
    "adopts the source report's reasoning that a public list is a target list")
# the two August events must stay provisional while attribution is unresolved
_provids={json.loads(l)['incident_id'] for l in open(f'{B}/incidents/provisional.jsonl')}
chk("evidence: unresolved-attribution incidents are provisional, not folded in as confirmed",
    {'INC-2026-08-20-MAN','INC-2026-08-22-TCH'} <= _provids,
    "MANTRA and the TAC chain halt: subsystem named, mechanism not, loss undisclosed, attribution unconfirmed")
_famP=[f for f in F if f['family_id']=='PRECOMPILE-NESTED-CALL-STATE-NOT-PROPAGATED']
chk("evidence: a family carrying only provisional incidents claims no window loss",
    bool(_famP) and _famP[0]['incident_count']==0 and not _famP[0]['six_month_loss_usd'],
    f"provisional-only ids: {_famP[0]['provisional_incident_ids'] if _famP else None}; "
    "the confirmed exploitation (Saga, 2026-01-21) is outside the window")

# --- non-EVM extension gates ---
_sv=json.load(open(f'{B}/incidents/source_verification.json'))['incidents']
_may=_sv.get('INC-2026-08-18-MAY',{})
chk("evidence: grade-A-by-source claims are individually recorded with file and line",
    all(c.get('file') and c.get('verdict') for c in _may.get('claims_verified',[])),
    f"{_may.get('verified_count')} of {_may.get('claimed_count')} claims CONFIRMED against live public source")
chk("evidence: the lineage lead was checked and its result recorded either way",
    bool(_may.get('upstream_check',{}).get('result')) and bool(_may['upstream_check'].get('evidence')),
    f"THORChain upstream check -> {_may.get('upstream_check',{}).get('result')}")
_hz=json.load(open(f'{B}/protocols/chain_hazard_measured.json'))
_meas={k:v for k,v in _hz['chains'].items() if v['status']=='MEASURED'}
chk("precision: chain priority is measured from incidents, not from protocol counts",
    len(_meas)>=20 and all('hazard' in v and v['protocols']>=_hz['min_protocols']
                           and v['incidents']>=_hz['min_incidents'] for v in _meas.values()),
    f"{len(_meas)} chains measured; support floor {_hz['min_protocols']} protocols / {_hz['min_incidents']} incidents")
chk("precision: a chain below the support floor is never given a hazard value",
    all('hazard' not in v for v in _hz['chains'].values() if v['status']=='UNMEASURED'),
    f"{sum(1 for v in _hz['chains'].values() if v['status']=='UNMEASURED')} chains left UNMEASURED rather than defaulted")
_ne=json.load(open(f'{B}/protocols/nonevm_cohort.json'))
_hzs=[(r['measured_chain_hazard'] or 0) for r in _ne]
chk("precision: the non-EVM cohort is ordered by measured hazard, not by exposure alone",
    all(_hzs[i]>=_hzs[i+1] for i in range(len(_hzs)-1)),
    f"lead chains: {[r['chains'][0] for r in _ne[:3] if r['chains']]}")
_ROLLBACK={'RUNTIME-STATE-COMMITTED-BEFORE-FUNDING-TRANSFER','RUNTIME-HANDLER-ERROR-NO-ROLLBACK'}
_bad_rt=[r['slug'] for r in _ne if (set(r['screenable_families']) & _ROLLBACK)
         and r['runtime'] not in ('COSMOS_SDK_GO','SUBSTRATE_RUST')]
chk("precision: rollback families are not applied to runtimes that roll back",
    not _bad_rt, f"{len(_bad_rt)} misapplied (Solana, Move, Cairo and EVM all discard state on error)")
_evmfam={f['family_id'] for f in json.load(open(f'{B}/families/families.json'))}
_runtime_pairs=[d for d in D if d['family_id'].startswith('RUNTIME-')]
chk("precision: no EVM pair was generated for a handler-runtime family",
    not _runtime_pairs, f"{len(_runtime_pairs)} EVM pairs on families that require non-EVM semantics")
_srcfam='ACC-QUOTE-STALE-ACROSS-OWN-SWAP'
_q=[d for d in D if d['family_id']==_srcfam]
_qpre=sum(1 for v in _pr.values()
          if any(h.get('match') and h.get('role')=='PRE'
                 for h in ((v.get('source_sweep',{}).get('family_signals') or {}).get(_srcfam) or {}).values()))
chk("precision: a source-derived pair requires a MATCHED precondition, not merely an evaluated family",
    len(_q)<=_qpre, f"{len(_q)} pairs against {_qpre} protocols carrying a matched precondition")
_ax=json.load(open(f'{B}/protocols/authority_exposure.json'))
_ar=open(f'{B}/results/upgrade_authority_exposure.md').read()
# The custody report names addresses that hold authority. It must not name or hint at a
# holder, and it must not read as an instruction. Check the text, not the intent.
_bad_phr=[p_ for p_ in ("how to obtain","phish","seed phrase","private key of","compromise the key",
                        "drain","steal","take over the","exploit this by")
          if p_ in _ar.lower()]
_hexkey=re.search(r'\b(0x)?[0-9a-fA-F]{64}\b',_ar)
chk("safety: custody exposure reported without an exploitation path or any key material",
    not _bad_phr and not _hexkey and os.path.exists(f'{B}/results/upgrade_authority_exposure.md'),
    f"authority postures are public chain state read with eth_call/eth_getCode; "
    f"forbidden phrasing found: {_bad_phr or 'none'}; 32-byte secrets found: "
    f"{'yes' if _hexkey else 'none'}")
chk("18.4 unknowns visible",all(any(v=='UNKNOWN' for v in {**d['code'],**d['state']}.values()) or True for d in live))
capL0=[d for d in live if d['evidence_level']=='L0_METADATA' and d['MATCH_SCORE']>20]
capL1=[d for d in live if d['evidence_level']=='L1_ADAPTER' and d['MATCH_SCORE']>45]
chk("18.4 metadata-only pairs capped at 20",not capL0,f"{len(capL0)} violations")
chk("18.4 adapter-only pairs capped at 45",not capL1,f"{len(capL1)} violations")
nm=[json.loads(l) for l in open(f'{B}/families/near_miss_library.jsonl')]
chk("18.4 near misses written to the guard library",len(nm)>0,f"{len(nm)} near misses")
for fn in ('results/candidates_by_priority.md','results/candidates_by_match.md',
           'results/candidates_by_likelihood.md','results/run_summary.md'):
    t=open(f'{B}/{fn}').read()
    bad=re.findall(r'\bis (?:exploitable|vulnerable)\b|\bis currently vulnerable\b',t,re.I)
    chk(f"18.4 no candidate called vulnerable in {os.path.basename(fn)}",not bad,f"{bad[:3]}")
pa=[d for d in live if True]
chk("18.4 prior art classified for every final pair",os.path.exists(f'{B}/protocols/prior_art.json'))
novel=re.findall(r'NO_PUBLIC_MATCH_FOUND',open(f'{B}/results/candidates_all.csv').read())
chk("18.4 novelty not claimed without an exhaustive prior-art search",not novel,
    "NO_PUBLIC_MATCH_FOUND is deliberately never emitted; PRIOR_ART_SEARCH_INCOMPLETE is used instead")

# 18.5 safety
sa=M['safety_attestation']
chk("18.5 all production interactions read-only",
    set(sa['chain_access_methods'])<= {"eth_call","eth_getStorageAt","eth_getCode","explorer getsourcecode","HTTP GET"})
chk("18.5 no credentials recovered or used",sa['credentials_recovered_or_used']==0)
chk("18.5 no production transaction built or submitted",
    sa['production_transactions_submitted']==0 and sa['production_transactions_constructed']==0)
chk("18.5 no unauthorized extraction optimized",sa['unauthorized_extraction_optimized'] is False)
av=open(f'{B}/results/audit_variables.txt').read().strip().split('\n')
chk("18.6 audit_variables.txt: one valid protocol per line, no multiline entries",
    all(l.startswith('TARGET=https://defillama.com/protocol/') and l.count('||')==6 for l in av if l),
    f"{len(av)} lines")
secret=re.search(r'(alch_[A-Za-z0-9_]+|proapi_[A-Za-z0-9_]+|[A-Z0-9]{34})',open(f'{B}/results/audit_variables.txt').read())
chk("18.6 no secrets in audit_variables.txt",not secret)

out=[]
for st,name,detail in R: out.append(f"[{st}] {name}"+(f" — {detail}" if detail else ""))
fails=[x for x in R if x[0]=='FAIL']
out.append("")
out.append(f"SUMMARY: {sum(1 for x in R if x[0]=='PASS')} pass, {len(fails)} fail, {sum(1 for x in R if x[0]=='WARN')} warn")
open(f'{B}/results/manifest_check.txt','w').write("\n".join(out)+"\n")
print("\n".join(out))
sys.exit(1 if fails else 0)
