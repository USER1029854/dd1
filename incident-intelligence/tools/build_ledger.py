#!/usr/bin/env python3
"""Cumulative ledger of every protocol already delivered as a final candidate.

A candidate list is work to be done, not a leaderboard. Handing back a protocol that
was already delivered in an earlier run gives the operator nothing new to work on, so
each run must exclude what previous runs already handed over. This reconstructs that
history from the repository itself -- the delivered lists are in git -- rather than
relying on anything kept in memory between runs.

Two extraction paths, because the output format changed across runs:
  results/candidates_all.csv     rows with in_final == YES   (later runs)
  results/candidates_by_*.md     the "**DefiLlama:** .../protocol/<slug>" lines that
                                 head each full write-up  (earlier runs, and a
                                 cross-check on the later ones)
"""
import json,csv,io,re,subprocess,sys,collections
B='/home/user/dd1/incident-intelligence'
REPO='/home/user/dd1'
# The write-up header changed between runs ("DefiLlama:" vs "DefiLlama URL:"), and the
# file set changed too (candidates_by_prevention.md existed early). Match the protocol
# URL wherever it heads a write-up, and enumerate the result files rather than naming them.
SLUG=re.compile(r'\*\*DefiLlama(?:\s+URL)?:\*\*\s+https://defillama\.com/protocol/([^\s)]+)')
TARGET=re.compile(r'TARGET=https://defillama\.com/protocol/([^\s|]+)')

def git(args):
    r=subprocess.run(["git"]+args,capture_output=True,text=True,cwd=REPO)
    return r.stdout if r.returncode==0 else ""

def commits():
    out=[]
    for line in git(["log","--format=%h\t%ct\t%s","--reverse"]).strip().split("\n"):
        if not line.strip(): continue
        h,ts,subj=line.split("\t",2); out.append((h,int(ts),subj))
    return out

def delivered_in(commit):
    """slug -> set(family_id) delivered as a FINAL at this commit."""
    got=collections.defaultdict(set)
    csv_txt=git(["show",f"{commit}:incident-intelligence/results/candidates_all.csv"])
    if csv_txt:
        try:
            for r in csv.DictReader(io.StringIO(csv_txt)):
                if r.get('in_final')=='YES':
                    got[r['protocol_slug']].add(r.get('family_id') or '')
        except Exception: pass
    listing=git(["ls-tree","-r","--name-only",commit]).split("\n")
    for path in listing:
        if not path.startswith("incident-intelligence/results/"): continue
        base=path.rsplit("/",1)[-1]
        if not (base.startswith("candidates_by_") and base.endswith(".md")): continue
        md=git(["show",f"{commit}:{path}"])
        for m in SLUG.finditer(md): got[m.group(1)].add('')
    # audit_variables.txt is the definitive handover list: one line per final candidate.
    av=git(["show",f"{commit}:incident-intelligence/results/audit_variables.txt"])
    for m in TARGET.finditer(av or ""): got[m.group(1)].add('')
    return {k:sorted(v-{''}) or [] for k,v in got.items()}

def main():
    head=git(["rev-parse","--short","HEAD"]).strip()
    # HEAD is a COMMITTED run, which means its candidates were already handed over.
    # An earlier revision excluded it on the theory that HEAD was "the run being produced
    # now" -- but the run being produced now is uncommitted and cannot be in git at all.
    # That mistake let 5 protocols from the previous delivery be served a second time
    # (smardex-amm, kyberswap-elastic, moneyfi, varen, elk). Every commit in history
    # counts as delivered; --exclude-head is kept only for inspecting the ledger as it
    # stood before the last delivery.
    exclude_head='--exclude-head' in sys.argv
    led={}
    runs=[]
    for h,ts,subj in commits():
        if exclude_head and h==head:      # the run being produced now is not yet delivered
            continue
        d=delivered_in(h)
        if not d: continue
        runs.append({"commit":h,"subject":subj,"protocols":len(d)})
        for slug,fams in d.items():
            e=led.setdefault(slug,{"first_delivered_in":h,"first_subject":subj,
                                   "runs":[],"families":[]})
            e["runs"].append(h)
            e["families"]=sorted(set(e["families"])|set(fams))
    out={"generated_from":"git history of results/candidates_*",
         "head_at_generation":head,
         "head_excluded":exclude_head,
         "runs":runs,
         "protocols_delivered":len(led),
         "ledger":led}
    json.dump(out,open(f'{B}/protocols/delivered_ledger.json','w'),indent=1)
    print(json.dumps({"runs_found":len(runs),"protocols_ever_delivered":len(led),
      "per_run":[{"commit":r["commit"],"protocols":r["protocols"],"subject":r["subject"][:60]} for r in runs]},
      indent=2))

if __name__=='__main__': main()
