#!/usr/bin/env python3
"""Upgrade / privileged-authority posture, measured read-only on chain.

Why this layer exists
---------------------
The family model answers "could this code be made to misbehave". It says nothing
about the other question a defender has to answer: *if this protocol's authority
key is lost, how much has to go wrong before user funds move?* That is not a code
bug and it is deliberately NOT scored as one -- an off-chain key compromise is an
excluded root cause under the run's inclusion gate (Sec.6). It is an IMPACT
AMPLIFIER, and it is the single most reportable, most fixable thing a small
independent reviewer can hand a team: "$3.1M sits behind an upgradeable proxy
whose terminal authority is one externally-owned account".

Everything here is public state read with eth_call / eth_getCode. Nothing
identifies a key holder, and nothing here is an attack instruction.

Method
------
For every address already probed, take its ERC-1967 admin slot and its owner().
Walk the authority chain up to MAXHOP hops (a proxy's admin is usually an
OZ ProxyAdmin whose own owner() is the real authority; that in turn is often a
Safe or a timelock), then classify the TERMINAL authority:

  EOA_SINGLE_KEY      code size 0 -- one private key
  SAFE_1_OF_N         Safe, threshold 1 -- one signature, so one key in practice
  SAFE_M_OF_N         Safe, threshold >= 2
  TIMELOCK_ZERO_DELAY timelock whose delay is 0 -- no warning window
  TIMELOCK            timelock with a real delay (seconds recorded)
  GOVERNOR            on-chain governor (votingDelay present)
  UNKNOWN_CONTRACT    a contract we could not fingerprint
  NONE_FOUND          no authority slot or owner exposed

A protocol's posture is the WEAKEST terminal authority over its addresses,
because the weakest one is what a defender has to plan around.
"""
import json,os,sys,time,collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import chain_batch as CB
from keccak import selector as SEL

B='/home/user/dd1/incident-intelligence'
MAXHOP=3
S={n:SEL(n) for n in ("getThreshold()","getOwners()","getMinDelay()","delay()",
                      "admin()","owner()","votingDelay()","GRACE_PERIOD()","token()")}
ZERO='0x'+'0'*40

def _addr(h):
    if not isinstance(h,str) or len(h)<66: return None
    a='0x'+h[-40:]
    return None if a.lower()==ZERO else a
def _uint(h):
    if not isinstance(h,str) or not h.startswith('0x') or len(h)<3: return None
    try: v=int(h,16)
    except Exception: return None
    return v if v < (1<<128) else None
def _arrlen(h):
    """length of a returned dynamic address[] (offset word, then length word)."""
    if not isinstance(h,str) or len(h)<131: return None
    try: n=int(h[66:130],16)
    except Exception: return None
    return n if 0<n<256 else None

RANK={'EOA_SINGLE_KEY':0,'SAFE_1_OF_N':1,'TIMELOCK_ZERO_DELAY':2,'UNKNOWN_CONTRACT':3,
      'SAFE_M_OF_N':4,'TIMELOCK':5,'GOVERNOR':6,'NONE_FOUND':7}

def classify(codesize,res):
    """res: dict selector-name -> raw hex result for one candidate authority."""
    if codesize==0: return {'posture':'EOA_SINGLE_KEY','next':None}
    thr=_uint(res.get('getThreshold()')); own=_arrlen(res.get('getOwners()'))
    if thr is not None and own:
        return {'posture':('SAFE_1_OF_N' if thr<=1 else 'SAFE_M_OF_N'),
                'threshold':thr,'signers':own,'next':None}
    d=_uint(res.get('getMinDelay()'))
    if d is None:
        dd=_uint(res.get('delay()'))
        # Compound Timelock also exposes GRACE_PERIOD(); require it so a random
        # delay() getter on an unrelated contract is not read as a timelock.
        if dd is not None and _uint(res.get('GRACE_PERIOD()')) is not None: d=dd
    if d is not None:
        return {'posture':('TIMELOCK_ZERO_DELAY' if d==0 else 'TIMELOCK'),
                'delay_seconds':d,'next':_addr(res.get('admin()'))}
    if _uint(res.get('votingDelay()')) is not None:
        return {'posture':'GOVERNOR','next':None}
    nxt=_addr(res.get('owner()')) or _addr(res.get('admin()'))
    return {'posture':'UNKNOWN_CONTRACT','next':nxt}

def audit(chain, seeds):
    """seeds: list of authority addresses. Returns {addr: chain-of-hops}."""
    out={}; frontier=[a for a in dict.fromkeys(seeds) if a and a.lower()!=ZERO]
    seen=set(); chains={a:[] for a in frontier}; owner_of={a:a for a in frontier}
    hop=0
    while frontier and hop<MAXHOP:
        frontier=[a for a in frontier if a.lower() not in seen]
        for a in frontier: seen.add(a.lower())
        if not frontier: break
        sizes=CB.calls(chain,[('code',a) for a in frontier])
        spec=[]; names=list(S)
        for a in frontier: spec += [('call',a,S[n]) for n in names]
        raw=CB.calls(chain,spec)
        nxts=[]
        for i,a in enumerate(frontier):
            res={n:raw[i*len(names)+j] for j,n in enumerate(names)}
            cs=sizes[i] if isinstance(sizes[i],int) else None
            c=classify(cs,res); c['address']=a; c['code_size']=cs; c['hop']=hop
            root=owner_of.get(a,a); chains.setdefault(root,[]).append(c)
            n=c.pop('next',None)
            if n and n.lower() not in seen:
                owner_of[n]=root; nxts.append(n)
        frontier=nxts; hop+=1
    for root,ch in chains.items():
        if ch: out[root]=ch
    return out

def terminal(ch):
    """last hop that is not a pass-through, else the last hop."""
    real=[c for c in ch if c['posture']!='UNKNOWN_CONTRACT'] or ch
    return real[-1]

def main():
    limit=int(sys.argv[1]) if len(sys.argv)>1 else 10**9
    force='--force' in sys.argv
    PR=json.load(open(f'{B}/protocols/onchain_probes.json'))
    outp=f'{B}/protocols/admin_posture.json'
    done=json.load(open(outp)) if (os.path.exists(outp) and not force) else {}
    todo=[]
    for slug,v in PR.items():
        if slug in done: continue
        d=v.get('deployment',{})
        if d.get('status')!='PROBED': continue
        seeds=collections.defaultdict(list)
        for a in d.get('addresses_probed') or []:
            ch=a.get('chain')
            for key in ('erc1967_admin','owner'):
                x=a.get(key)
                if isinstance(x,str) and x.startswith('0x') and x.lower()!=ZERO:
                    seeds[ch].append(x)
        if seeds: todo.append((slug,dict(seeds)))
    todo=todo[:limit]
    print(f"admin posture over {len(todo)} protocols (already done {len(done)})",flush=True)
    t0=time.time()
    for i,(slug,seeds) in enumerate(todo):
        rec={'authorities':{},'posture':None}
        for ch,addrs in seeds.items():
            try: res=audit(ch,addrs[:12])
            except Exception as e: res={}
            for root,chain_ in res.items(): rec['authorities'][root]={'chain':ch,'hops':chain_}
        post=[terminal(v['hops'])for v in rec['authorities'].values() if v['hops']]
        if post:
            worst=min(post,key=lambda c:RANK.get(c['posture'],9))
            rec['posture']=worst['posture']; rec['posture_detail']=worst
        else:
            rec['posture']='NONE_FOUND'
        rec['n_authorities']=len(rec['authorities'])
        done[slug]=rec
        if i%40==0:
            el=time.time()-t0
            print(f"  [{i}/{len(todo)}] {slug} -> {rec['posture']} ({el:.0f}s, {el/max(1,i):.2f}s/p)",flush=True)
            json.dump(done,open(outp,'w'))
    json.dump(done,open(outp,'w'))
    c=collections.Counter(v['posture'] for v in done.values())
    print(json.dumps({"protocols":len(done),"by_posture":dict(c)},indent=2))

if __name__=='__main__': main()
