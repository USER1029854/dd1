#!/usr/bin/env python3
"""Assert a candidate slug is NOT in the exclusion set (all prior pushes)."""
import json, sys, re
excl=set(json.load(open('results/discoveries/_exclusion_set.json')))
def norm(s): return re.sub(r'[^a-z0-9]+','-',s.lower()).strip('-')
for q in sys.argv[1:]:
    n=norm(q)
    hit = n in excl or any(n in e or e in n for e in excl if len(e)>4)
    print(f"{'DUPLICATE' if hit else 'NEW      '}  {q}  ({n})")
