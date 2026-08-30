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

# one source of truth for truncation marking (6E renderer pass)
from library_audit import clip_evidence


def cell(value, limit=200):
    """⛔ EVERY data-derived string reaches the page through here.

    4Q round 12 inventoried all 14 text-to-page paths and found two more unclipped after I
    had fixed the two 6E named — the tool-defects table (a raw Python `repr()` of a list of
    dicts, 260+ chars in one table cell) and the census mismatches. Patching those two would
    have left the same class open in the taxonomy and judgement-class rows, which are also
    header-derived. So this is the funnel, not four more patches: a value that is not a
    string is FORMATTED rather than repr'd, and everything is clipped with the marker.
    """
    if isinstance(value, (list, tuple)):
        parts = []
        for v in value:
            if isinstance(v, dict):
                parts.append(" ".join(f"{k}={v[k]!s}" for k in sorted(v)))
            else:
                parts.append(str(v))
        value = " · ".join(parts) if parts else "(none)"
    elif not isinstance(value, str):
        value = str(value)
    return clip_evidence(value.replace("|", "\\|").replace("\n", " "), limit)

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
# ⛔ 6E design review 3: an unowned record is a defect in the TOOL (a dropped reason code or
# a missing routing rule), not a triage item. It goes FIRST and it cannot be scrolled past.
_has_routing = any("needs_tool_fix" in r for r in recs)
_defects = [r for r in recs if r.get("needs_tool_fix")]
if not _has_routing:
    # ⛔ A record that never carried the field is not a record with the field set to False.
    # Printing "0 tool defects" for a pre-routing run would be absence of evidence read as
    # evidence of absence -- on the exact claim this section exists to make loud.
    w("## ⚠️ This run PREDATES the routing model")
    w("")
    w("No record in this JSONL carries `needs_tool_fix`, so the number of unowned records is")
    w("**UNKNOWN, not zero**, and the lane table below would be zeros for the same reason.")
    w("Re-run the audit with the current tool before quoting anything about routing.")
    w("")
elif _defects:
    w("## ⛔ TOOL DEFECTS — read before anything else")
    w("")
    w(f"**{len(_defects)} record(s) carry a check that NO ROUTING RULE CLAIMED.** That is a")
    w("defect in the audit tool, not work for a human reviewer: a human cannot fix a dropped")
    w("reason code or a missing routing rule. Every number below this line is suspect until")
    w("these are fixed and the run is repeated.")
    w("")
    w("| pattern | unclaimed checks |")
    w("|---|---|")
    for r in _defects[:40]:
        w(f"| `{r['path']}` | {cell(r.get('unclaimed_checks') or [])} |")
    if len(_defects) > 40:
        w(f"| … | {len(_defects) - 40} more |")
    w("")
else:
    w("> **0 tool defects.** Every non-clean check on every record was claimed by a named")
    w("> routing rule — no record fell through to an unowned lane. A run with any unowned")
    w("> record exits 3 and no flag suppresses it.")
    w("")

w("## Who the work belongs to")
w("")
w("Ver's finding 5, and 6E's design review 3: `needs_judgement` used to mean three different")
w("asks of three different people. It is three fields now, and a tool defect is never")
w("counted as human work.")
w("")
w("| lane | what is asked | records |")
w("|---|---|---|")
for _f, _what in () if not _has_routing else (
                 ("needs_review", "read the pattern — a check FAILED or was FLAGGED"),
                  ("needs_pathology_triage", "decide: defect, or documented edge case? (U3)"),
                  ("needs_implementation", "build the analyser / provide the input (U1, U2)"),
                 ("needs_tool_fix", "⛔ fix THIS TOOL — nobody claimed the check")):
    w(f"| `{_f}` | {_what} | {sum(1 for r in recs if r.get(_f))} |")
w("")
if any("unverified" in r for r in recs):
    # ⛔ 6E conformance 3: this said "every check ran" for every record with
    # `unverified: 0/n`. `unverified` counts UNMEASURED checks only — a SKIPPED check is
    # not unverifiable — and all 676 such records also carried 3 skipped checks, so the
    # sentence was false for every one of them. The counts are now derived so the prose
    # cannot overstate: a record only reaches the first bucket if NOTHING was left out.
    # ⛔ 4Q round 11 O1: NO DEFAULT on either .get() here, on purpose. A record that never
    # carried the field must fall into NEITHER bucket -- adding `, 0` to make the two lines
    # look consistent would count a pre-routing record as "every check ran", which is
    # exactly the defect 6E found in round 10. Consistency here would be a regression.
    _none_run = sum(1 for r in recs
                    if r.get("checks_unmeasured") == 0 and r.get("checks_skipped") == 0)
    _skipped_only = sum(1 for r in recs
                        if r.get("checks_unmeasured") == 0
                        and (r.get("checks_skipped") or 0) > 0)
    w("Stated as how much could NOT be measured, never as how much passed. `unverified: 1/8`")
    w("cannot be misread as a pass; `measured: 7/8` can.")
    w("")
    w(f"- **{_none_run} of {len(recs)}** records had EVERY check run — nothing unverifiable,")
    w("  nothing skipped.")
    w(f"- **{_skipped_only}** more have nothing unverifiable but at least one check SKIPPED.")
    w("  A skipped check is not an unverifiable one, and it is not a measured one either —")
    w("  reading `unverified: 0/n` as \"fully checked\" is the mistake this line exists to")
    w("  prevent.")
    w(f"- the remaining **{len(recs) - _none_run - _skipped_only}** carry a non-zero")
    w("  `unverified` figure beside the verdict. The verdict is about the pattern, the")
    w("  coverage is about the tool, and they are orthogonal.")
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
        w(f"- {cell(m, 300)}")
    w("")
w("## Judgement-only classes (stated once, not flagged per pattern)")
w("")
for k, v in (header.get("judgement_only_classes") or {}).items():
    w(f"- **{cell(k, 80)}** — {cell(v, 400)}")
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

# ⛔ 4Q round 11 F1 and 6E renderer #3, found independently: the prose below used
# `undisposed` where it meant "records carrying the UNVERIFIABLE verdict". They are equal
# on a fresh run and diverge the moment a triage session sets a disposition -- and this
# report exists to BE that triage session, so the divergence is the normal case, not the
# edge case. The two counts are named apart now so the wrong one cannot be reached for.
unv_verdict = sum(1 for r in recs if r["verdict"] == "UNVERIFIABLE")
hidden = with_u - unv_verdict
# 6E renderer #4: `hidden` is "has an unverifiable check but a higher-severity verdict",
# and FAIL outranks UNVERIFIABLE too. Derived rather than asserted, because a --gate run
# (which is how the shipped sweep is produced) can put a gate=fail beside deps=unverifiable.
hidden_by_verdict = collections.Counter(
    r["verdict"] for r in recs if r.get("unverifiable_checks")
    and r["verdict"] != "UNVERIFIABLE")
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
    w(f"**{unv_verdict} records carry the UNVERIFIABLE verdict**, of which "
      f"**{undisposed} are still undispositioned.**")
    w("")
    w("⛔ The tool exits 2 while ANY record carries the UNVERIFIABLE verdict, unless")
    w("`--acknowledge-unverifiable` is passed. It does not read `disposition` at all —")
    w("dispositioning every record does NOT clear the exit code, and an earlier draft of this")
    w("sentence implied it did (6E, renderer pass).")
    w("")
    if hidden:
        w(f"### ⚠️ …and {hidden} MORE records carry an unmeasured check without saying so")
        w("")
        w(f"{with_u} records have at least one `unverifiable` check, but only {unv_verdict} of")
        w(f"them carry UNVERIFIABLE as their verdict. The other **{hidden}** report as "
          + ", ".join(f"**{v}** ({n})" for v, n in sorted(hidden_by_verdict.items()))
          + ",")
        w("because both FAIL and FLAG outrank UNVERIFIABLE in the precedence — a record with a")
        w("real finding AND an unmeasured half shows the finding and hides the hole.")
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
        w(f"| **{cell(sc, 20)} {cell(meta.get('name','?'), 60)}** | {sub_counts[sc]} | "
          f"{'the tool is the gap' if sc=='U1' else 'the environment/data is the gap' if sc=='U2' else 'the FILE blocked measurement'} "
          f"| {cell(meta.get('remedy','?'), 200)} |")
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
w("Ordered FAIL first, then FLAG, then UNVERIFIABLE. Long details are cut with an explicit")
w("truncation marker; the record's `checks` array in the JSONL always holds the full text.")
w("Every entry carries its evidence, so")
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
            # The "Reasons" list is the SECOND place a detail reaches the page, and it was
            # emitting the raw string uncut. Found by the renderer's own new fixture, not by
            # either agent -- 6E named the triage-queue cut, and fixing only that would have
            # left a 400-char reason dumped verbatim two sections above it.
            w(f"- ({n}×) {clip_evidence(d, 150)}")
        w("")
    shown = items if len(items) <= 40 else items[:40]
    w("| pattern | evidence |")
    w("|---|---|")
    for path, detail in shown:
        # ⛔ 6E renderer pass: this was a hard 150-char cut with NO marker, while the tool's
        # own clip_evidence marks its truncations -- Ver's finding 7, live in the renderer,
        # silently cutting the two hand-verified known_finding explanations on this sweep.
        # The tool's function is imported rather than copied so the two cannot drift.
        _d = clip_evidence(detail, 150).replace("|", "\\|")
        w(f"| `{path}` | {_d} |")
    if len(items) > len(shown):
        w(f"")
        w(f"*… and {len(items) - len(shown)} more — see `{src.name}`.*")
    w("")

out.write_text("\n".join(L) + "\n", encoding="utf-8")
print(f"{len(recs)} records -> {out}  ({len(L)} lines)")
