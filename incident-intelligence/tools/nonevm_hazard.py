#!/usr/bin/env python3
"""Measured hazard per chain, derived rather than assumed.

Why this file exists
--------------------
The first non-EVM cohort was sized by how many protocols each chain has. That is
not a risk measure, it is a popularity measure, and it produced a cohort that was
40% Solana. Measured against actual incidents Solana is the OPPOSITE of a priority:

    Solana      x0.63   22 incidents across 293 protocols above the floor
    Cosmos      x2.25    8 incidents across  30
    EOS         x7.02   15 incidents across  18

hazard = (incidents on chain / all incidents) / (protocols on chain / all protocols)

Above 1 means the chain is over-represented among actual victims relative to how
much of the universe it is. Chains below the support floor are reported as
UNMEASURED and are never promoted on a guess.

Source: DefiLlama's hacks dataset filtered to on-chain root causes (the same
exclusion set the run's inclusion gate uses), cross-checked against this run's own
in-window corpus.
"""
import json,collections,sys,os
B=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')
OFF={'Key Compromise','Frontend & Infrastructure','Social Engineering','Rugpull'}
ALIAS={'Binance Smart Chain':'BSC','BNB Chain':'BSC','BNB':'BSC','Binance':'BSC',
       'Gnosis Chain':'Gnosis','Near':'NEAR','Terra Classic':'Terra','Cosmos Hub':'Cosmos'}
MIN_PROTOCOLS=3      # below this the ratio is noise
MIN_INCIDENTS=2

def norm(c): return ALIAS.get(c,c)

def compute():
    H=json.load(open(f'{B}/sources/defillama/hacks.json'))
    U=json.load(open(f'{B}/protocols/defillama_universe.json'))
    onchain=[h for h in H if h.get('classification') not in OFF
             and h.get('targetType') not in ('CEX','Wallet')]
    inc=collections.Counter(); loss=collections.Counter()
    for h in onchain:
        cs={norm(c) for c in (h.get('chain') or h.get('chains') or []) or []}
        for c in cs:
            inc[c]+=1; loss[c]+=(h.get('amount') or 0)/max(len(cs),1)
    proto=collections.Counter()
    for u in U:
        if (u.get('_tvl') or 0)<50_000: continue
        for c in {norm(x) for x in (u.get('_chains') or [])}: proto[c]+=1
    TI=sum(inc.values()); TP=sum(proto.values())
    out={}
    for c in set(inc)|set(proto):
        n,p=inc.get(c,0),proto.get(c,0)
        if p<MIN_PROTOCOLS or n<MIN_INCIDENTS:
            out[c]={"status":"UNMEASURED","incidents":n,"protocols":p,
                    "note":"below the support floor; never promoted on a guess"}
            continue
        out[c]={"status":"MEASURED","incidents":n,"protocols":p,
                "hazard":round((n/TI)/(p/TP),3),"loss_usd":round(loss[c],2),
                "mean_loss_usd":round(loss[c]/n,2)}
    # Frequency and severity are different questions and answer differently. Bridges are
    # the clearest case: by frequency the Bridge category is UNDER-represented (x0.80,
    # 12 incidents across 108 protocols) yet it carries $1.22bn, the largest loss of any
    # category, at a mean of ~$102M per incident. For an operator working a $50k-$30M
    # band that severity is out of reach by construction -- the band filter removes those
    # protocols before scoring -- so the ranking uses FREQUENCY hazard and severity is
    # reported separately rather than folded in. Neither number is discarded.
    return {"totals":{"incidents":TI,"protocols":TP,"onchain_incidents":len(onchain)},
            "note_frequency_vs_severity":("hazard is a FREQUENCY ratio. mean_loss_usd is "
              "reported alongside it because the two disagree: bridges are rare victims "
              "with catastrophic losses, and a frequency ranking will correctly not "
              "prioritise them for an operator whose band caps at $30M."),
            "min_protocols":MIN_PROTOCOLS,"min_incidents":MIN_INCIDENTS,"chains":out}

def hazard_of(chains, table):
    """A protocol's hazard is the MAX over the chains it is deployed on, because the
    exposure is to the worst of them. Unmeasured chains contribute nothing rather
    than a default, so an unmeasured protocol is not silently treated as average."""
    vals=[table['chains'][norm(c)]['hazard'] for c in (chains or [])
          if table['chains'].get(norm(c),{}).get('status')=='MEASURED']
    return max(vals) if vals else None

if __name__=='__main__':
    t=compute()
    json.dump(t,open(f'{B}/protocols/chain_hazard_measured.json','w'),indent=1)
    m=[(v['hazard'],k,v) for k,v in t['chains'].items() if v['status']=='MEASURED']
    m.sort(reverse=True)
    print("%-20s %7s %7s %8s" % ("chain","hazard","hacks","protos"))
    for h,k,v in m: print("%-20s %7.2f %7d %8d" % (k,h,v['incidents'],v['protocols']))
    print("\nUNMEASURED (below support floor): %d chains"
          % sum(1 for v in t['chains'].values() if v['status']=='UNMEASURED'))
