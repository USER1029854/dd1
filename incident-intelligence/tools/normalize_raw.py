#!/usr/bin/env python3
"""Phase A.2: merge all-category crawl + per-category crawls -> all_raw.jsonl"""
import json, glob, os, re, collections

SM  = "/home/user/dd1/incident-intelligence/sources/slowmist"
OUT = "/home/user/dd1/incident-intelligence/incidents"
WSTART, WEND = "2026-02-22", "2026-08-22"

rows = json.load(open(f"{SM}/parsed_rows_all.json"))

# category attribution: key = (date, normalized target)
def key(r): return (r["event_date"], re.sub(r'[^a-z0-9]', '', r["target"].lower()))
cats = collections.defaultdict(set)
for f in sorted(glob.glob(f"{SM}/parsed_rows_*.json")):
    tag = os.path.basename(f)[len("parsed_rows_"):-len(".json")]
    if tag == "all": continue
    for r in json.load(open(f)):
        cats[key(r)].add(tag)

def slug(t):
    s = re.sub(r'[^A-Za-z0-9]', '', t).upper()
    return (s[:3] or "UNK").ljust(3, "X")

seen, out = collections.Counter(), []
for r in rows:
    d = r["event_date"]
    if not re.match(r'^\d{4}-\d{2}-\d{2}$', d):
        d_status, d = "UNVERIFIED", d
    else:
        d_status = "VERIFIED"
    base = f"INC-{d}-{slug(r['target'])}"
    seen[base] += 1
    iid = base if seen[base] == 1 else f"{base}-{seen[base]}"
    c = sorted(cats.get(key(r), []))
    out.append({
        "incident_id": iid,
        "event_date": d,
        "target": r["target"],
        "slowmist_category": c,
        "slowmist_attack_method": r["slowmist_attack_method"],
        "reported_loss_usd": r["reported_loss_usd"],
        "reported_loss_raw": r["reported_loss_raw"],
        "description_raw": r["description_raw"],
        "slowmist_page_url": r["slowmist_page_url"],
        "slowmist_page_no": r["slowmist_page_no"],
        "reference_urls": r["reference_urls"],
        "date_status": d_status,
        "in_window": (WSTART <= d <= WEND),
        "initial_disposition": "REVIEW",
    })

with open(f"{OUT}/all_raw.jsonl","w") as fh:
    for o in out: fh.write(json.dumps(o, ensure_ascii=False)+"\n")

inw = [o for o in out if o["in_window"]]
print(json.dumps({
  "total_rows": len(out), "in_window": len(inw),
  "with_category": sum(1 for o in inw if o["slowmist_category"]),
  "without_category": sum(1 for o in inw if not o["slowmist_category"]),
  "with_refs": sum(1 for o in inw if o["reference_urls"]),
  "no_refs": sum(1 for o in inw if not o["reference_urls"]),
  "date_unverified": sum(1 for o in inw if o["date_status"]!="VERIFIED"),
  "loss_unparsed": sum(1 for o in inw if o["reported_loss_usd"] is None),
  "id_collisions": sum(1 for k,v in seen.items() if v>1),
}, indent=2))
