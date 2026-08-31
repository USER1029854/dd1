#!/usr/bin/env python3
"""Classify each recorded victim by what its vault holds NOW versus around its incident.

Why this exists
---------------
"The incident is evidence, the un-hit sibling is the target." A drained victim's value
is gone -- a hot clock over an empty vault is not a candidate. But a victim that was
restarted, refunded or whitehat-restored is holding real money again on the same open
door, and the first hours after it resumes are the highest-sensitivity moment in the
whole model. Those two look identical in a current-TVL snapshot, so this pulls each
victim's TVL series and reads what actually happened.

Classification (all from the series, none assumed):
  DRAINED_OR_DEAD     holds less than the floor now -> EXCLUDED as a candidate, kept as evidence
  RESTORED            fell hard around the incident and has since recovered materially -> RESTORE WINDOW
  NEVER_MATERIALLY_HIT no large drop around the incident (partial loss, or loss small vs TVL)
  UNKNOWN_SERIES      series unavailable -> never promoted on a guess
"""
import json,os,sys,subprocess,time,datetime,collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import hazard as HZ
B=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')
FLOOR=50_000
CACHE=f'{B}/sources/defillama/protocol_tvl'

def series(slug):
    os.makedirs(CACHE,exist_ok=True)
    fp=f'{CACHE}/{slug}.json'
    if os.path.exists(fp) and os.path.getsize(fp)>50:
        try: return json.load(open(fp))
        except Exception: pass
    r=subprocess.run(["curl","-sS","-m","40",f"https://api.llama.fi/protocol/{slug}"],
                     capture_output=True,text=True)
    try: d=json.loads(r.stdout)
    except Exception: return None
    tv=d.get('tvl') or []
    out=[{"date":p.get("date"),"tvl":p.get("totalLiquidityUSD")} for p in tv
         if isinstance(p,dict) and p.get("date")]
    json.dump(out,open(fp,'w'))
    return out

def at(s,ts):
    """TVL nearest to a timestamp."""
    best=None
    for p in s:
        if p['tvl'] is None: continue
        if best is None or abs(p['date']-ts)<abs(best['date']-ts): best=p
    return best['tvl'] if best else None

def classify(slug,hacks,head_tvl):
    s=series(slug)
    if not s: return {"state":"UNKNOWN_SERIES","basis":"TVL series unavailable"}
    if (head_tvl or 0)<FLOOR:
        return {"state":"DRAINED_OR_DEAD","basis":"holds $%s now, below the $%s floor" %
                (f"{head_tvl or 0:,.0f}",f"{FLOOR:,}")}
    dates=[datetime.datetime.fromisoformat(h['date']).replace(tzinfo=datetime.timezone.utc).timestamp()
           for h in hacks if h.get('date')]
    if not dates: return {"state":"UNKNOWN_SERIES","basis":"no dated incident"}
    ts=max(dates)
    pre=at(s,ts-7*86400); post=at(s,ts+14*86400)
    if pre is None or post is None:
        return {"state":"UNKNOWN_SERIES","basis":"series does not cover the incident window"}
    drop=(pre-post)/pre if pre>0 else 0
    if drop>=0.6:
        rec=(head_tvl-post)/max(post,1)
        if head_tvl>=FLOOR and rec>=1.0:
            return {"state":"RESTORED","basis":
                    "fell %.0f%% around %s ($%s -> $%s) and has since recovered to $%s"
                    % (drop*100,datetime.datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d'),
                       f"{pre:,.0f}",f"{post:,.0f}",f"{head_tvl:,.0f}"),
                    "pre":pre,"post":post,"recovery_multiple":round(rec,2)}
        return {"state":"DRAINED_OR_DEAD","basis":
                "fell %.0f%% around the incident ($%s -> $%s) and holds $%s now"
                % (drop*100,f"{pre:,.0f}",f"{post:,.0f}",f"{head_tvl:,.0f}"),
                "pre":pre,"post":post}
    return {"state":"NEVER_MATERIALLY_HIT","basis":
            "no large drop around the incident ($%s -> $%s, %.0f%%); the loss was partial "
            "or small against TVL" % (f"{pre:,.0f}",f"{post:,.0f}",drop*100),
            "pre":pre,"post":post}

def main():
    limit=int(sys.argv[1]) if len(sys.argv)>1 else 10**9
    head=json.load(open(f'{B}/protocols/tvl_head.json'))
    outp=f'{B}/protocols/victim_state.json'
    done=json.load(open(outp)) if os.path.exists(outp) else {}
    todo=[s for s in HZ.PRIOR_HACKS if s not in done][:limit]
    print("classifying %d victims (done %d)" % (len(todo),len(done)),flush=True)
    for i,slug in enumerate(todo):
        done[slug]=classify(slug,HZ.PRIOR_HACKS[slug],head.get(slug,0))
        done[slug]['head_tvl']=head.get(slug,0)
        done[slug]['hacks']=len(HZ.PRIOR_HACKS[slug])
        if i%25==0:
            print("  [%d/%d] %s -> %s" % (i,len(todo),slug,done[slug]['state']),flush=True)
            json.dump(done,open(outp,'w'),indent=1)
    json.dump(done,open(outp,'w'),indent=1)
    c=collections.Counter(v['state'] for v in done.values())
    print(json.dumps({"victims":len(done),"by_state":dict(c),
      "restored_restore_window":[k for k,v in done.items() if v['state']=='RESTORED'][:20]},indent=2))

if __name__=='__main__': main()
