#!/usr/bin/env python3
"""Phase A crawler: SlowMist Hacked index -> raw snapshots + parsed rows.

Read-only HTTP GET against a public incident index. No chain interaction.
"""
import hashlib, html as htmllib, json, os, re, subprocess, sys, time

OUT   = "/home/user/dd1/incident-intelligence/sources/slowmist"
WSTART, WEND = "2026-02-22", "2026-08-22"
MAXP  = int(sys.argv[1]) if len(sys.argv) > 1 else 30
CAT   = sys.argv[2] if len(sys.argv) > 2 else ""     # "" = All
TAG   = CAT if CAT else "all"

os.makedirs(OUT, exist_ok=True)

def fetch(url, dest):
    for attempt in range(4):
        r = subprocess.run(["curl","-sS","-m","60","-o",dest,"-w","%{http_code}",
                            "-H","User-Agent: Mozilla/5.0 (defensive-security-research; read-only)",
                            url], capture_output=True, text=True)
        code = (r.stdout or "").strip()[-3:]
        if code == "200" and os.path.getsize(dest) > 2000:
            return code
        time.sleep(2 ** attempt)
    return code

# <li> ... </li> row extraction
ROW = re.compile(r'<li>\s*<span class="time">(.*?)</span>(.*?)</li>', re.S)
def txt(s):
    s = re.sub(r'<[^>]+>', '', s)
    return htmllib.unescape(s).replace('\xa0',' ').strip()

def parse(page_html, page_no, url):
    rows = []
    body = page_html.split('<div class="case-content">',1)[-1]
    for m in ROW.finditer(body):
        date, rest = m.group(1).strip(), m.group(2)
        tgt = re.search(r'<h3><em>Hacked target:\s*</em>(.*?)</h3>', rest, re.S)
        dsc = re.search(r'<em>Description of the event:\s*</em>(.*?)</p>', rest, re.S)
        amt = re.search(r'<em>Amount of loss:\s*</em>(.*?)</span>', rest, re.S)
        mth = re.search(r'<em>Attack method:\s*</em>(.*?)</span>', rest, re.S)
        refs = re.findall(r'<p class="link-reference"><a href="([^"]+)"', rest)
        raw_amt = txt(amt.group(1)) if amt else ""
        n = re.sub(r'[^0-9.]', '', raw_amt)
        try:
            loss = float(n) if n and n.count('.') <= 1 else None
        except ValueError:
            loss = None
        rows.append({
            "event_date": date,
            "target": txt(tgt.group(1)) if tgt else "",
            "slowmist_attack_method": txt(mth.group(1)) if mth else "",
            "reported_loss_usd": loss,
            "reported_loss_raw": raw_amt,
            "description_raw": txt(dsc.group(1)) if dsc else "",
            "slowmist_page_url": url,
            "slowmist_page_no": page_no,
            "reference_urls": refs,
        })
    return rows

log, all_rows = [], []
in_window_seen_any = False
for p in range(1, MAXP + 1):
    url  = f"https://hacked.slowmist.io/?c={CAT}&page={p}"
    dest = f"{OUT}/{TAG}_page_{p:03d}.html"
    code = fetch(url, dest)
    ts   = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    if code != "200":
        log.append({"page": p, "url": url, "http": code, "status": "FETCH_FAILED",
                    "retrieved_utc": ts}); break
    raw  = open(dest, encoding="utf-8", errors="replace").read()
    sha  = hashlib.sha256(raw.encode("utf-8", "replace")).hexdigest()
    rows = parse(raw, p, url)
    dates = sorted(r["event_date"] for r in rows if re.match(r'\d{4}-\d{2}-\d{2}', r["event_date"]))
    inw  = [r for r in rows if WSTART <= r["event_date"] <= WEND]
    older= [r for r in rows if r["event_date"] < WSTART]
    log.append({"page": p, "url": url, "http": code, "retrieved_utc": ts, "sha256": sha,
                "bytes": len(raw), "snapshot": os.path.basename(dest),
                "rows_parsed": len(rows), "rows_in_window": len(inw),
                "rows_older_than_window": len(older),
                "first_date": dates[0] if dates else None,
                "last_date": dates[-1] if dates else None, "status": "OK"})
    all_rows += rows
    if inw: in_window_seen_any = True
    if not rows:
        log[-1]["status"] = "EMPTY_PAGE_STOP"; break
    # Boundary proof: this whole page is older than the window AND we already saw the window.
    if in_window_seen_any and len(inw) == 0 and len(older) == len(rows):
        log[-1]["status"] = "BOUNDARY_PROVEN"; break
    time.sleep(0.6)

json.dump({"tag": TAG, "category_filter": CAT, "window_start": WSTART, "window_end": WEND,
           "pages": log, "total_rows": len(all_rows)},
          open(f"{OUT}/crawl_log_{TAG}.json","w"), indent=2)
json.dump(all_rows, open(f"{OUT}/parsed_rows_{TAG}.json","w"), indent=2)
print(json.dumps({"tag":TAG,"pages":len(log),"rows":len(all_rows),
                  "last_status":log[-1]["status"] if log else None,
                  "oldest":min((r['event_date'] for r in all_rows), default=None)}, indent=2))
