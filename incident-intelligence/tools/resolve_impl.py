#!/usr/bin/env python3
"""Follow delegator/beacon proxies to the deployed implementation and review the
cash/exchange-rate path there. This is what separates L2 from L4 evidence."""
import json,sys,re,time
sys.path.insert(0,'/home/user/dd1/incident-intelligence/tools')
import chain as C
B='/home/user/dd1/incident-intelligence'
PR=json.load(open(f'{B}/protocols/onchain_probes.json'))
Z="0x"+"0"*40
def impl_of(ch,addr):
    for sel in ("implementation",):
        r=C.dec_addr(C.call(ch,addr,C.SEL[sel]) or "")
        if r and r!=Z: return r,"implementation()"
    s=C.storage(ch,addr,C.SLOT_1967_IMPL)
    if s and s!="0x"+"0"*64:
        a=C.dec_addr(s)
        if a and a!=Z: return a,"erc1967 slot"
    b=C.storage(ch,addr,C.SLOT_1967_BEACON)
    if b and b!="0x"+"0"*64:
        be=C.dec_addr(b)
        r=C.dec_addr(C.call(ch,be,C.SEL["implementation"]) or "")
        if r and r!=Z: return r,f"beacon {be}"
    return None,None

def review(src):
    return {
     "has_getCashPrior_balanceOf":bool(re.search(r'getCashPrior[\s\S]{0,800}?balanceOf\s*\(\s*address\s*\(\s*this',src)),
     "has_balanceOf_this_in_cash_path":bool(re.search(r'balanceOf\s*\(\s*address\s*\(\s*this\s*\)\s*\)',src)),
     "has_exchangeRateStoredInternal":bool(re.search(r'exchangeRateStoredInternal',src)),
     "cash_plus_borrows_minus_reserves":bool(re.search(r'totalCash\s*\+\s*totalBorrows|getCashPrior\(\)[\s\S]{0,200}totalBorrows',src)),
     "has_internal_cash_counter":bool(re.search(r'\binternalCash\b|\btotalCash\s*[-+]=',src)),
     "has_exchange_rate_cap":bool(re.search(r'maxExchangeRate|rateCap|exchangeRateDelta|MAX_RATE|maxRate',src,re.I)),
     "mentions_supply_cap":bool(re.search(r'supplyCap',src)),
     "has_sweep_or_skim_of_unaccounted":bool(re.search(r'function\s+sweep|function\s+skim|_sweepToken',src)),
     "source_chars":len(src)}

n=0
for slug,v in PR.items():
    c=v.get('compound') or {}
    if not c.get('markets'): continue
    out=[]
    for m in c['markets'][:4]:
        ch,a=m['chain'],m['cToken']
        ia,how=impl_of(ch,a)
        rec={"cToken":a,"chain":ch,"implementation":ia,"resolved_via":how}
        if ia:
            s=C.source(ch,ia)
            if s and s.get('verified'):
                rec["implementation_name"]=s['ContractName']; rec["guard_review"]=review(s['source'] or "")
            elif s:
                rec["implementation_name"]=s.get('ContractName'); rec["guard_review"]="IMPLEMENTATION_NOT_VERIFIED"
        out.append(rec); time.sleep(0.2); n+=1
    c['implementation_review']=out
    gr=[r.get('guard_review') for r in out if isinstance(r.get('guard_review'),dict)]
    if gr:
        c['market_source']={**(c.get('market_source') or {}),
          "implementation_reviewed":True,
          "has_getCashPrior_balanceOf":any(g['has_getCashPrior_balanceOf'] for g in gr),
          "has_balanceOf_this_in_cash_path":any(g['has_balanceOf_this_in_cash_path'] for g in gr),
          "has_internal_cash_counter":all(g['has_internal_cash_counter'] for g in gr),
          "has_exchange_rate_cap":all(g['has_exchange_rate_cap'] for g in gr),
          "mentions_supply_cap":any(g['mentions_supply_cap'] for g in gr),
          "implementation_names":sorted({r.get('implementation_name') for r in out if r.get('implementation_name')})}
    print(slug,"->",[(r['cToken'][:10],r.get('implementation_name'),
        (r['guard_review'] if isinstance(r['guard_review'],str) else
         {k:v2 for k,v2 in r['guard_review'].items() if v2 is True}) if r.get('guard_review') else None) for r in out],flush=True)
json.dump(PR,open(f'{B}/protocols/onchain_probes.json','w'),indent=1)
print("implementation hops:",n)
