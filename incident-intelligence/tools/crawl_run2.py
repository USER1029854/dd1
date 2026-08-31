#!/usr/bin/env python3
"""Run-2 crawler: re-crawl the SlowMist Hacked index to a proven date boundary.

Window is re-anchored on today (2026-08-29), so it reaches one week further
forward than the run-1 crawl and re-reads the older range for late-indexed rows.
Read-only HTTP GET against a public index. No chain interaction.
"""
import hashlib, html as htmllib, json, os, re, subprocess, sys, time

OUT   = "/home/user/dd1/incident-intelligence/sources/slowmist_run2"
WSTART, WEND = "2026-02-28", "2026-08-29"
MAXP  = int(sys.argv[1]) if len(sys.argv) > 1 else 40
CAT   = sys.argv[2] if len(sys.argv) > 2 else ""
TAG   = CAT if CAT else "all"
os.makedirs(OUT, exist_ok=True)

def fetch(url, dest):
    code = ""
    for attempt in range(4):
        r = subprocess.run(["curl","-sS","-m","90","-o",dest,"-w","%{http_code}",
                            "-H","User-Agent: Mozilla/5.0 (defensive-security-research; read-only)",
                            url], capture_output=True, text=True)
        code = (r.stdout or "").strip()[-3:]
        if code == "200" and os.path.exists(dest) and os.path.getsize(dest) > 2000:
            return code
        time.sleep(2 ** attempt)
    return code

ROW = re.compile(r'<li>\s*<span class="time">(.*?)</span>(.*?)</li>', re.S)
def txt(s):
    return htmllib.unescape(re.sub(r'<[^>]+>', '', s)).replace('\xa0',' ').strip()

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
        try:    loss = float(n) if n and n.count('.') <= 1 else None
        except ValueError: loss = None
        rows.append({"event_date": date, "target": txt(tgt.group(1)) if tgt else "",
            "slowmist_attack_method": txt(mth.group(1)) if mth else "",
            "reported_loss_usd": loss, "reported_loss_raw": raw_amt,
            "description_raw": txt(dsc.group(1)) if dsc else "",
            "slowmist_page_url": url, "slowmist_page_no": page_no, "reference_urls": refs})
    return rows

log, all_rows = [], []
for p in range(1, MAXP + 1):
    url  = f"https://hacked.slowmist.io/?c={CAT}&page={p}"
    dest = f"{OUT}/{TAG}_page_{p:03d}.html"
    code = fetch(url, dest)
    ts   = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    if code != "200":
        log.append({"page": p, "url": url, "http": code, "status": "FETCH_FAILED", "retrieved_utc": ts}); break
    raw  = open(dest, encoding="utf-8", errors="replace").read()
    rows = parse(raw, p, url)
    inw   = [r for r in rows if WSTART <= r["event_date"] <= WEND]
    older = [r for r in rows if r["event_date"] and r["event_date"] < WSTART]
    log.append({"page": p, "url": url, "http": code, "retrieved_utc": ts,
                "sha256": hashlib.sha256(raw.encode("utf-8","replace")).hexdigest(),
                "bytes": len(raw), "snapshot": os.path.basename(dest),
                "rows_parsed": len(rows), "rows_in_window": len(inw), "rows_older": len(older)})
    all_rows.extend(rows)
    print(f"page {p}: {len(rows)} rows, {len(inw)} in-window, {len(older)} older", flush=True)
    if rows and not inw and len(older) == len(rows):
        log.append({"boundary": "PROVEN", "page": p,
                    "rule": "full page with zero in-window rows and every row older than WSTART"})
        print("BOUNDARY PROVEN at page", p, flush=True); break
    if not rows:
        log.append({"boundary": "EMPTY_PAGE", "page": p}); print("empty page", p, flush=True); break
    time.sleep(1)

json.dump(log, open(f"{OUT}/crawl_log_{TAG}.json","w"), indent=1)
json.dump(all_rows, open(f"{OUT}/parsed_rows_{TAG}.json","w"), indent=1)
print(f"TOTAL rows={len(all_rows)} pages={len([l for l in log if 'page' in l and 'rows_parsed' in l])}")
