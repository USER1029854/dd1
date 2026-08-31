# -*- coding: utf-8 -*-
"""Static indicators for the handler-runtime families, with their decisive guards.

These are deliberately WINDOWED rather than single-line regexes. "A setter exists"
and "a transfer exists" are both true of nearly every keeper file ever written; the
defect is a setter that commits BEFORE a transfer that can fail, in the same
function. So each indicator names an anchor pattern, a follower pattern, and how
many lines may separate them.

Every indicator carries a role, exactly as the EVM sweep does:
  PRE    a mandatory precondition of the family
  GUARD  a decisive guard whose presence FALSIFIES the pair
  WEAK   supporting shape only; never sufficient on its own
"""
import re

def _c(p): return re.compile(p)

IND = {
# ---------------- RUNTIME-STATE-COMMITTED-BEFORE-FUNDING-TRANSFER ----------------
"GO-SET-BEFORE-SEND": dict(
  role="PRE", lang={".go"}, family="RUNTIME-STATE-COMMITTED-BEFORE-FUNDING-TRANSFER",
  anchor=_c(r'\.Set[A-Z]\w*\(\s*ctx\s*,'),
  follow=_c(r'\.Send(?:Coins|FromModuleToModule|CoinsFromModuleToAccount|CoinsFromAccountToModule)\w*\('),
  window=30,
  note="a keeper setter commits state, then a module transfer that can fail runs after it in the same function"),
"GO-CACHECONTEXT": dict(
  role="GUARD", lang={".go"}, family="RUNTIME-STATE-COMMITTED-BEFORE-FUNDING-TRANSFER",
  anchor=_c(r'CacheContext\(\)'), follow=None, window=0,
  note="cosmos CacheContext(): writes are staged and only committed by write() on success"),
"RS-TRANSACTIONAL": dict(
  role="GUARD", lang={".rs"}, family="RUNTIME-STATE-COMMITTED-BEFORE-FUNDING-TRANSFER",
  anchor=_c(r'#\[transactional\]|with_transaction\(|storage_layer::'), follow=None, window=0,
  note="substrate #[transactional] / with_transaction: dispatchable writes unwind on error"),
"RS-MUT-BEFORE-TRANSFER": dict(
  role="PRE", lang={".rs"}, family="RUNTIME-STATE-COMMITTED-BEFORE-FUNDING-TRANSFER",
  anchor=_c(r'<\w+<T>>::(?:insert|mutate|put)\(|\w+::<T>::(?:insert|mutate|put)\('),
  follow=_c(r'(?:T::Currency::transfer|transfer_from|::transfer\()'),
  window=25,
  note="a storage write precedes a currency transfer that can fail, in one dispatchable"),

# ---------------- RUNTIME-HANDLER-ERROR-NO-ROLLBACK ----------------
"GO-LOG-THEN-CONTINUE": dict(
  role="PRE", lang={".go"}, family="RUNTIME-HANDLER-ERROR-NO-ROLLBACK",
  anchor=_c(r'Logger\(\)\.Error\('), follow=_c(r'^\s*continue\s*$'), window=8,
  note="a handler error is logged and the dispatcher continues in the same context"),
"GO-SETDONE-ON-ERROR": dict(
  role="PRE", lang={".go"}, family="RUNTIME-HANDLER-ERROR-NO-ROLLBACK",
  anchor=_c(r'if\s+err\s*!=\s*nil\s*\{'), follow=_c(r'\.SetDone\(\)|MarkProcessed\(|SetCompleted\('),
  window=10,
  note="the error branch marks the item done, so it is never reprocessed"),
"GO-DISPATCH-RETURNS-ERR": dict(
  role="GUARD", lang={".go"}, family="RUNTIME-HANDLER-ERROR-NO-ROLLBACK",
  anchor=_c(r'if\s+err\s*!=\s*nil\s*\{'), follow=_c(r'^\s*return\s+(?:nil,\s*)?err\b'), window=4,
  note="the dispatcher propagates the error so the runtime aborts the transaction"),

# ---------------- RUNTIME-BATCHED-MESSAGE-SHARED-KEY-CLOBBER ----------------
"GO-TXID-KEYED-WRITE-IN-LOOP": dict(
  role="PRE", lang={".go"}, family="RUNTIME-BATCHED-MESSAGE-SHARED-KEY-CLOBBER",
  anchor=_c(r'for\s+(?:_|\w+)\s*,\s*\w+\s*:?=\s*range\s+\w*(?:[Mm]sgs|[Mm]essages|[Ii]tems|[Cc]oins)'),
  follow=_c(r'New\w*Voter\(\s*\w+\.(?:Tx\.)?ID|\.Set[A-Z]\w*\(\s*ctx\s*,\s*\w*(?:[Vv]oter|[Rr]ecord)'),
  window=40,
  note="per-message loop constructs and stores a record keyed on the shared transaction id"),
"GO-FETCH-THEN-APPEND": dict(
  role="GUARD", lang={".go"}, family="RUNTIME-BATCHED-MESSAGE-SHARED-KEY-CLOBBER",
  anchor=_c(r'\.Get[A-Z]\w*(?:Voter|Record)\w*\(\s*ctx\s*,'),
  follow=_c(r'\.Add\(|append\(|\.Txs\s*=\s*append'), window=12,
  note="the existing record is fetched and appended to rather than reconstructed"),
"RS-PDA-WRITE-IN-LOOP": dict(
  role="PRE", lang={".rs"}, family="RUNTIME-BATCHED-MESSAGE-SHARED-KEY-CLOBBER",
  anchor=_c(r'for\s+\w+\s+in\s+\w*(?:instructions|ixs|msgs|accounts)\b'),
  follow=_c(r'(?:try_borrow_mut_data|\.serialize\(|\*\*?\w+\s*=\s)'), window=30,
  note="a per-instruction loop writes an account whose key does not vary with the instruction"),
"MOVE-SHARED-OBJECT-WRITE-IN-LOOP": dict(
  role="PRE", lang={".move"}, family="RUNTIME-BATCHED-MESSAGE-SHARED-KEY-CLOBBER",
  anchor=_c(r'while\s*\(|vector::(?:borrow|length)\('),
  follow=_c(r'\*\s*\w+\s*=\s|table::(?:add|remove|borrow_mut)\('), window=25,
  note="a loop overwrites an entry in a shared table rather than keying per element"),

# ---------------- RECONCILIATION-STRIDE-SKIPS-TRUE-VALUE ----------------
"GO-NONUNIT-STRIDE-SCAN": dict(
  role="PRE", lang={".go"}, family="RECONCILIATION-STRIDE-SKIPS-TRUE-VALUE",
  anchor=_c(r'for\s+\w+\s*:?=\s*\w+\s*;\s*\w+\s*<=?\s*[\w\.\(\)]+\s*;\s*\w+\s*\+=\s*(?!1\s*\{)\w+'),
  follow=None, window=0,
  note="a scan loop steps by a variable stride rather than by one, so a value between steps is missed"),
"RS-STEP-BY": dict(
  role="PRE", lang={".rs"}, family="RECONCILIATION-STRIDE-SKIPS-TRUE-VALUE",
  anchor=_c(r'\.step_by\(\s*(?!1\s*\))'), follow=None, window=0,
  note="an iterator strides by more than one while searching"),
"STRIDE-MISS-TRIGGERS-PENALTY": dict(
  role="WEAK", lang={".go",".rs",".move",".cairo"}, family="RECONCILIATION-STRIDE-SKIPS-TRUE-VALUE",
  anchor=_c(r'(?:not\s*found|notFound|missing|NotFound)'),
  follow=_c(r'(?:[Ss]lash|[Ss]ubsidi|[Cc]ompensat|[Mm]int\(|[Rr]eimburse)'), window=20,
  note="a not-found branch reaches a penalising or compensating path rather than a retry"),
"INDEXED-LOOKUP": dict(
  role="GUARD", lang={".go",".rs",".move",".cairo"}, family="RECONCILIATION-STRIDE-SKIPS-TRUE-VALUE",
  anchor=_c(r'\.Get[A-Z]\w*\(\s*ctx\s*,\s*\w*(?:[Hh]ash|ID|[Kk]ey)\b|\.get\(&?\w*(?:hash|id|key)\b'),
  follow=None, window=0,
  note="records are looked up by identifier against an index, not by walking a counter"),
}

VIEW_ONLY=re.compile(r'(?:^|/)(?:test|tests|mock|mocks|example|examples|docs?|simulation|fuzz|bench)(?:/|_|\.)',re.I)

def scan(path, text, langs_allowed, families_allowed):
    """Return [{indicator, family, role, line, evidence}] for one file."""
    if VIEW_ONLY.search(path): return []
    ext='.'+path.rsplit('.',1)[-1] if '.' in path else ''
    lines=text.split('\n')
    out=[]
    for name,d in IND.items():
        if ext not in d['lang'] or ext not in langs_allowed: continue
        if d['family'] not in families_allowed: continue
        for i,l in enumerate(lines):
            if not d['anchor'].search(l): continue
            if d['follow'] is None:
                out.append({"indicator":name,"family":d['family'],"role":d['role'],
                            "file":path,"line":i+1,"evidence":l.strip()[:200],"note":d['note']})
                break
            hit=None
            for j in range(i+1,min(i+1+d['window'],len(lines))):
                if d['follow'].search(lines[j]): hit=j; break
            if hit is not None:
                out.append({"indicator":name,"family":d['family'],"role":d['role'],
                            "file":path,"line":i+1,"evidence":(lines[i].strip()[:120]+"  ...  "+lines[hit].strip()[:120]),
                            "follow_line":hit+1,"note":d['note']})
                break
    return out
