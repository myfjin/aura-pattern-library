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
w("> **`NO_FINDING` was called `PASS` until Ver's honesty pass on 2026-08-30.** The word PASS")
w("> told a reader the pattern was good; the tool only ever measured the classes it can check,")
w("> and C1 (correctness), C3 (twin equivalence) and C11 (provenance) were never assessed for")
w("> any pattern. The disclosure was there per record, but a summary reader sees the headline")
w("> word, not the footnote. The word now matches the measurement.")
w("")
w("| verdict | count | meaning |")
w("|---|---:|---|")
MEAN = {"NO_FINDING": "no defect found among the classes this tool CAN check — NOT "
                      "'correct': C1/C3/C11 were never assessed",
        "FAIL": "a decidable check is RED",
        "FLAG": "needs judgement; evidence attached", "SKIP": "nothing applicable ran",
        "UNVERIFIABLE": "the tool could not measure it"}
for v in ("FAIL", "FLAG", "UNVERIFIABLE", "NO_FINDING", "SKIP"):
    if by_verdict.get(v):
        w(f"| **{v}** | {by_verdict[v]} | {MEAN[v]} |")
w("")
w("## By language")
w("")
w("| lane | " + " | ".join(("FAIL", "FLAG", "UNVERIFIABLE", "NO_FINDING", "SKIP")) + " | total |")
w("|---|" + "---:|" * 6)
for lane in sorted(by_lane):
    c = by_lane[lane]
    w(f"| {lane} | " + " | ".join(str(c.get(v, 0)) for v in
      ("FAIL", "FLAG", "UNVERIFIABLE", "NO_FINDING", "SKIP")) + f" | {sum(c.values())} |")
w("")
w("### ⚠️ Read the UNVERIFIABLE column before the NO_FINDING column")
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
# ---- the UNVERIFIABLE board. 6E: one undifferentiated bucket is useless for triage,
# because "no R analyser" and "this twin has no source" do not have the same remedy.
sub_counts = collections.Counter()
code_rows = collections.defaultdict(collections.Counter)     # (subclass, code) -> check ct
code_lanes = collections.defaultdict(collections.Counter)    # (subclass, code) -> lane ct
undisposed = 0
with_u = sum(1 for r in recs if r.get("unverifiable_checks"))
for r in recs:
    for u in (r.get("unverifiable_checks") or []):
        key = (u.get("subclass") or "UNCODED", u.get("reason_code") or "(none)")
        code_rows[key][u["name"]] += 1
        code_lanes[key][r["language"]] += 1
    for sc in (r.get("unverifiable_subclass") or []):
        sub_counts[sc] += 1
    if r["verdict"] == "UNVERIFIABLE" and r.get("disposition") is None:
        undisposed += 1

hidden = with_u - sum(1 for r in recs if r["verdict"] == "UNVERIFIABLE")
tax = header.get("unverifiable_taxonomy") or {}
if code_rows:
    w("---")
    w("")
    w("# The UNVERIFIABLE board — sorted by REMEDY")
    w("")
    w("UNVERIFIABLE is not one problem. Each subclass below names a different kind of work,")
    w("and that is the point of the split: the triage session can be run without reopening a")
    w("single pattern file.")
    w("")
    w(f"**{undisposed} records are UNVERIFIABLE and undispositioned.** The tool exits 2 while")
    w("that is true, unless `--acknowledge-unverifiable` is passed.")
    w("")
    if hidden:
        w(f"### ⚠️ …and {hidden} MORE records carry an unmeasured check without saying so")
        w("")
        w(f"{with_u} records have at least one `unverifiable` check, but only {undisposed} of")
        w(f"them carry UNVERIFIABLE as their verdict. The other **{hidden} report as FLAG**,")
        w("because FLAG outranks UNVERIFIABLE in the precedence — a record with a real finding")
        w("AND an unmeasured half shows the finding and hides the hole.")
        w("")
        w("That is correct precedence (the finding is the more urgent fact) but it makes the")
        w("verdict column understate how much was never measured. **Triage these from the")
        w("reason-code table below, not from the verdict column** — the table counts checks,")
        w("so it sees all of them.")
        w("")
    w("| subclass | records w/ ≥1 such check | what it means | remedy |")
    w("|---|---:|---|---|")
    for sc in sorted(sub_counts):
        meta = (tax.get("subclasses") or {}).get(sc, {})
        w(f"| **{sc} {meta.get('name','?')}** | {sub_counts[sc]} | "
          f"{'the tool is the gap' if sc=='U1' else 'the environment/data is the gap' if sc=='U2' else 'the FILE blocked measurement'} "
          f"| {meta.get('remedy','?')} |")
    w("")
    w("## By reason code")
    w("")
    w("| subclass | reason code | occurrences | checks affected | lanes |")
    w("|---|---|---:|---|---|")
    for key in sorted(code_rows, key=lambda k: (k[0], -sum(code_rows[k].values()))):
        sc, code = key
        n = sum(code_rows[key].values())
        chk = ", ".join(f"`{c}`×{m}" for c, m in code_rows[key].most_common(4))
        lns = ", ".join(f"{l}×{m}" for l, m in code_lanes[key].most_common())
        w(f"| {sc} | `{code}` | {n} | {chk} | {lns} |")
    w("")
    if tax.get("per_subclass_dispositions"):
        w("## Disposition vocabulary (closed set — no free text)")
        w("")
        w("| subclass | permitted dispositions |")
        w("|---|---|")
        for sc, ds in sorted(tax["per_subclass_dispositions"].items()):
            w(f"| {sc} | " + ", ".join(f"`{d}`" for d in ds) + " |")
        w("")
        w("`WAIVE` additionally REQUIRES a `disposition_ref` — who waived it and why. Without")
        w("that it is a silent NO_FINDING wearing a different name.")
        w("")
    cov = header.get("analyser_coverage") or {}
    if cov:
        w("## Analyser coverage — which check can run on which lane")
        w("")
        w("A future edit that adds a `pass`-returning fallback for a missing analyser would")
        w("empty the U1 bucket silently, and the exit-2 forcing function cannot see that")
        w("happen. This table is asserted cell by cell in the self-test, so such an edit")
        w("breaks a probe instead.")
        w("")
        lanes = sorted({l for v in cov.values() for l in v})
        w("| check | " + " | ".join(lanes) + " |")
        w("|---|" + "---|" * len(lanes))
        for c in sorted(cov):
            w(f"| `{c}` | " + " | ".join("yes" if l in cov[c] else "—" for l in lanes) + " |")
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
        _d = detail[:150].replace("|", "\\|")
        w(f"| `{path}` | {_d} |")
    if len(items) > len(shown):
        w(f"")
        w(f"*… and {len(items) - len(shown)} more — see `{src.name}`.*")
    w("")

out.write_text("\n".join(L) + "\n", encoding="utf-8")
print(f"{len(recs)} records -> {out}  ({len(L)} lines)")
