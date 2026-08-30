#!/usr/bin/env python3
"""Turn AUDIT-RESULTS.jsonl into a triage document a human can act on.

The JSONL is the record; this is the readout. It groups by CHECK (what is wrong) and by
OWNER (who decides), because that is how the work gets divided -- 1,500 records sorted by
path is not triage, it is a list.
"""
import collections
import json
import sys
from pathlib import Path

src = Path(sys.argv[1] if len(sys.argv) > 1 else "AUDIT-RESULTS.jsonl")
out = Path(sys.argv[2] if len(sys.argv) > 2 else "AUDIT-REPORT.md")

lines = [l for l in src.read_text(encoding="utf-8").splitlines() if l.strip()]
header = json.loads(lines[0])["run"]
recs = [json.loads(l) for l in lines[1:]]

by_verdict = collections.Counter(r["verdict"] for r in recs)
by_lane = collections.defaultdict(collections.Counter)
check_status = collections.defaultdict(collections.Counter)
issues = collections.defaultdict(list)          # (check, status) -> [(path, detail)]
for r in recs:
    by_lane[r["language"]][r["verdict"]] += 1
    for c in r["checks"]:
        check_status[c["name"]][c["status"]] += 1
        if c["status"] in ("fail", "flag", "unverifiable"):
            issues[(c["name"], c["status"])].append((r["path"], c["detail"]))

L = []
w = L.append
w("# AURA Pattern Library — full audit")
w("")
w(f"**{header['total_patterns']} patterns** · run {header['run_date']} on `{header['host']}` "
  f"· {header.get('elapsed_s','?')}s")
w(f"· `library_verify.py` md5 `{header['library_verify_md5']}`")
w("")
w("## Verdicts")
w("")
w("| verdict | count | meaning |")
w("|---|---:|---|")
MEAN = {"PASS": "every decidable check green", "FAIL": "a decidable check is RED",
        "FLAG": "needs judgement; evidence attached", "SKIP": "nothing applicable ran",
        "UNVERIFIABLE": "the tool could not measure it"}
for v in ("FAIL", "FLAG", "UNVERIFIABLE", "PASS", "SKIP"):
    if by_verdict.get(v):
        w(f"| **{v}** | {by_verdict[v]} | {MEAN[v]} |")
w("")
w("## By language")
w("")
w("| lane | " + " | ".join(("FAIL", "FLAG", "UNVERIFIABLE", "PASS", "SKIP")) + " | total |")
w("|---|" + "---:|" * 6)
for lane in sorted(by_lane):
    c = by_lane[lane]
    w(f"| {lane} | " + " | ".join(str(c.get(v, 0)) for v in
      ("FAIL", "FLAG", "UNVERIFIABLE", "PASS", "SKIP")) + f" | {sum(c.values())} |")
w("")
w("### ⚠️ Read the UNVERIFIABLE column before the PASS column")
w("")
w("Most checks are AST-based and implemented for python only. A non-python lane scoring few")
w("FLAGs is not evidence that it is clean — it is evidence that fewer checks could run on it.")
w("The per-check table below shows exactly which.")
w("")
w("## Per check")
w("")
w("| check | pass | fail | flag | unverifiable | skip |")
w("|---|---:|---:|---:|---:|---:|")
for n in sorted(check_status):
    c = check_status[n]
    w(f"| `{n}` | " + " | ".join(str(c.get(s, 0)) for s in
      ("pass", "fail", "flag", "unverifiable", "skip")) + " |")
w("")
if header.get("census_mismatches"):
    w("## ⛔ Census")
    w("")
    for m in header["census_mismatches"]:
        w(f"- {m}")
    w("")
w("## Judgement-only classes (stated once, not flagged per pattern)")
w("")
for k, v in (header.get("judgement_only_classes") or {}).items():
    w(f"- **{k}** — {v}")
w("")
w("## Not requested this run")
w("")
for c in header.get("checks_not_requested") or ["(none)"]:
    w(f"- `{c}`")
w("")
w("Toolchains: " + ", ".join(f"{k}={'yes' if v else '**MISSING**'}"
                             for k, v in header["toolchains_present"].items()))
w("")
w("---")
w("")
w("# The triage queue")
w("")
w("Ordered FAIL first, then FLAG, then UNVERIFIABLE. Every entry carries its evidence, so")
w("triage does not need to re-read the file.")
w("")
order = {"fail": 0, "flag": 1, "unverifiable": 2}
for (name, status) in sorted(issues, key=lambda k: (order[k[1]], -len(issues[k]))):
    items = issues[(name, status)]
    w(f"## `{name}` — {status.upper()} × {len(items)}")
    w("")
    det = collections.Counter(d for _, d in items)
    if len(det) <= 8:
        w("Reasons:")
        w("")
        for d, n in det.most_common():
            w(f"- ({n}×) {d}")
        w("")
    shown = items if len(items) <= 40 else items[:40]
    w("| pattern | evidence |")
    w("|---|---|")
    for path, detail in shown:
        w(f"| `{path}` | {detail[:150].replace('|', '\\|')} |")
    if len(items) > len(shown):
        w(f"")
        w(f"*… and {len(items) - len(shown)} more — see `{src.name}`.*")
    w("")

out.write_text("\n".join(L) + "\n", encoding="utf-8")
print(f"{len(recs)} records -> {out}  ({len(L)} lines)")
