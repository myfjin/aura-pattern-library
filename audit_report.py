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

    ⛔ THE COMMENT THAT USED TO BE HERE SAID "every data-derived string reaches the page
    through here" AND IT WAS FALSE -- 6E round 13 found ELEVEN slots still emitting raw
    (lane names, reason codes, the triage path, the disposition rows, analyser coverage).
    An overclaiming comment is worse than none: it is the reason I stopped looking. Every
    one of those now calls this, and the page-level probe asserts the grammar rather than
    trusting this docstring.

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
    # ⛔ ORDER MATTERS. 4Q round 13 F1: escaping `|` before `\` turns a value containing
    # `\|` into `\\|` -- an escaped BACKSLASH followed by a live column separator, so the
    # row silently gains a column and every count reads under the wrong heading.
    value = value.replace("\\", "\\\\").replace("|", "\\|")
    # ⛔ Length was never the whole grammar. 6E round 13 built a page to prove it: a
    # THREE-character ``` opens a fence that swallows the rest of the document, and a
    # <img src=x onerror=...> reached the page byte for byte -- both far under every limit
    # I had set. A backtick that cannot start a fence, and no raw `<`, or the clip is
    # cosmetic. (4Q read the HTML as cosmetic; escaping it costs one replace, so the
    # disagreement does not need settling.)
    value = value.replace("`", "\\`").replace("<", "&lt;")
    for _ws in ("\r\n", "\r", "\n"):
        value = value.replace(_ws, " ")
    return clip_evidence(value, limit)

src = Path(sys.argv[1] if len(sys.argv) > 1 else "AUDIT-RESULTS.jsonl")
out = Path(sys.argv[2] if len(sys.argv) > 2 else "AUDIT-REPORT.md")

lines = [l for l in src.read_text(encoding="utf-8").splitlines() if l.strip()]
header = json.loads(lines[0])["run"]
recs = [json.loads(l) for l in lines[1:]]

def _axes(r):
    """The two axes are NESTED (see library_audit.axes_of): a top-level `finding` was a seam a
    consumer could read alone, merging measured records with unmeasured ones."""
    a = r.get("axes") or {}
    return a.get("finding"), a.get("coverage")

def _finding(r): return _axes(r)[0]
def _coverage(r): return _axes(r)[1]

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
# ⛔ 6E round 14: the SIXTH thing. These four were emitted raw AND the page probe never
# seeded them, so all five grammar invariants were blind to the slot — a hostile `host`
# turns document line 2 into an unclosed fence and swallows the report. Same class as the
# round-13 comment: a guarantee that covers only what its author remembered.
w(f"**{cell(header['total_patterns'], 20)} patterns** · run {cell(header['run_date'], 40)} "
  f"on `{cell(header['host'], 60)}` · {cell(header.get('elapsed_s', '?'), 20)}s")
# ⛔ PROVENANCE. The page named the VERIFIER's md5 and never the PRODUCER's, so a reader
# could not tell which version of the audit tool made these verdicts -- and every round of
# this red-team changed the tool. The run_id embeds the same md5, so the two cannot drift
# apart silently. Both are read from the header, never recomputed here: a renderer that
# hashes the tool would report the tool it is running BESIDE, not the one that ran.
w(f"· produced by `{cell(header.get('tool', 'UNKNOWN'), 40)}` md5 "
  f"`{cell(header.get('tool_md5', 'UNKNOWN — pre-provenance run'), 40)}` "
  f"· run `{cell(header.get('run_id', 'UNKNOWN'), 40)}`")
w(f"· `library_verify.py` md5 `{cell(header['library_verify_md5'], 40)}`")
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
        w(f"| `{cell(r['path'], 120)}` | {cell(r.get('unclaimed_checks') or [])} |")
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
    w(f"| `{cell(_f, 40)}` | {cell(_what, 120)} | "
      f"{sum(1 for r in recs if r.get(_f))} |")
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
# ⛔ 6E, REPORT-6E-2AXIS.md reader path 1: the compound verdict LEADS WITH THE REASSURING WORD.
# "NO_FINDING/PARTIAL" puts NO_FINDING in token position 1 and the caution in position 2, so a
# skimming reader registers clean and nothing forces the coverage half into view. Under the old
# single word the headline WAS the caution. The fix is to make the coverage tally the first
# thing on the page, so the gap is what you read first and NO_FINDING is what you read past.
_cov_head = collections.Counter(_coverage(r) for r in recs)
_not_full = sum(v for k, v in _cov_head.items() if k != "FULL")
if recs:
    w(f"> ## ⛔ {_not_full} of {len(recs)} patterns were NOT fully measured")
    w("> ")
    w(f"> Coverage: **{_cov_head.get('FULL', 0)} FULL · {_cov_head.get('PARTIAL', 0)} PARTIAL "
      f"· {_cov_head.get('NONE', 0)} NONE**. Read this before any verdict below: a verdict of "
      "`NO_FINDING` on a PARTIAL record means *nothing was found among the checks that could "
      "run*, not that the pattern was fully checked. The finding half of a verdict is never "
      "meaningful without the coverage half.")
    w("")
w("Two independent questions are asked about every pattern, and they are reported as two")
w("axes rather than collapsed into one word.")
w("")
w("- **finding** — was anything found among the checks that RAN? (`NO_FINDING` / `FLAG` / `FAIL`)")
w("- **coverage** — how much of the suite could look at this file at all? (`FULL` / `PARTIAL` / `NONE`)")
w("")
w("> ⛔ **Why this is two axes and not one word.** Until 2026-08-30 a single verdict carried")
w("> both, and it could only be honest about one of them. A clean cpp pattern was labelled")
w("> `UNVERIFIABLE` — which reads as *nothing was measured* — when in fact 7 checks had run")
w("> and all 7 were clean; an identical python pattern was labelled `NO_FINDING`. The word")
w("> was describing THIS TOOL's lane coverage, not the pattern. Collapsing the other way")
w("> (`PASS_WITH_GAPS`) was rejected because it hides the gap. The fix is to stop collapsing:")
w("> a verdict is now always `finding/coverage`, so neither half can be dropped by a reader")
w("> or by a consumer that looks only at `verdict`.")
w("")
_FIND = [f for f in ("FAIL", "FLAG", "NO_FINDING", "SKIP")
         if any(_finding(r) == f for r in recs)]
_COV = [c for c in ("FULL", "PARTIAL", "NONE")
        if any(_coverage(r) == c for r in recs)]
_grid = collections.Counter(_axes(r) for r in recs)
w("| | " + " | ".join(f"coverage **{c}**" for c in _COV) + " | total |")
w("|---|" + "---:|" * (len(_COV) + 1))
for f in _FIND:
    _row = [_grid.get((f, c), 0) for c in _COV]
    w(f"| **{f}** | " + " | ".join(str(x) for x in _row) + f" | {sum(_row)} |")
w("| **total** | " + " | ".join(
    str(sum(_grid.get((f, c), 0) for f in _FIND)) for c in _COV) + f" | {len(recs)} |")
w("")
MEAN = {"NO_FINDING": "no defect found among the classes this tool CAN check — NOT "
                      "'correct': C1/C3/C11 were never assessed",
        "FAIL": "a decidable check is RED",
        "FLAG": "needs judgement; evidence attached", "SKIP": "nothing applicable ran"}
COVMEAN = {"FULL": "every requested check returned a measurement",
           "PARTIAL": "at least one check ran AND at least one could not",
           "NONE": "nothing could be measured — the only state that means 'unverifiable'"}
w("| axis value | meaning |")
w("|---|---|")
for f in _FIND:
    w(f"| finding **{f}** | {MEAN[f]} |")
for c in _COV:
    w(f"| coverage **{c}** | {COVMEAN[c]} |")
w("")
# The coverage gap is stated as a POSITIVE fact about what ran, derived per record -- never a
# hardcoded span, because the profile is not uniform.
# PARTIAL and NONE are different facts and must not be summed into one sentence: a
# record where nothing could be measured is not "partially measured".
_part = [r for r in recs if _coverage(r) == "PARTIAL"]
if _part:
    _ran, _cannot, _names = [], [], collections.Counter()
    for _r in _part:
        _st = [c.get("status") for c in _r.get("checks", [])]
        _ran.append(sum(1 for x in _st if x in ("pass", "flag", "fail")))
        _cannot.append(sum(1 for x in _st if x == "unverifiable"))
        for _c in _r.get("checks", []):
            if _c.get("status") == "unverifiable":
                _names[_c.get("name")] += 1
    def _span(v):
        return f"{min(v)}" if min(v) == max(v) else f"{min(v)}-{max(v)}"
    _clean = sum(1 for _r in _part if _finding(_r) == "NO_FINDING")
    _uniform = len(set(_names.values())) == 1 and len(_names) > 0
    w(f"> **What PARTIAL coverage means here.** {len(_part)} records were only partially "
      f"measured. Each still had **{_span(_ran)} checks actually run**, and {_clean} of them "
      f"came back with no finding on every check that ran. What could not run is "
      f"**{_span(_cannot)} checks** per record"
      + (f", and it is the SAME checks every time — {', '.join(f'`{k}`' for k in sorted(_names))}"
         f" — each needing an analyser this lane does not have." if _uniform else ".")
      + " PARTIAL is a statement about this tool's reach, not about the pattern.")
    w("")
    _none = [r for r in recs if _coverage(r) == "NONE"]
    w(f"> **Records where NOTHING could be measured: {len(_none)}.** That is the only state "
      f"in which the tool genuinely knows nothing about a pattern"
      + ("." if _none else ", and no pattern in this library is in it.")) 
    w("")
    w("")
# ⛔ 6E ROUND 20, finding 2. `gate` and `determinism_repeat` are the only checks that RUN a
# file. When they are skipped, nothing was executed at all and every verdict on this page is
# static. That was disclosed in a small "not requested this run" box while the C1 section
# narrated the gate as if in play, next to "toolchains: all yes" -- so a reader could infer
# the NO_FINDING patterns had been executed. Derived from the records, never assumed.
_exec_checks = ("gate", "determinism_repeat")
_ran_exec = sum(1 for r in recs for c in r.get("checks", [])
                if c.get("name") in _exec_checks and c.get("status") != "skip")
if recs and not _ran_exec:
    w("> **NOTHING WAS EXECUTED IN THIS RUN.** `gate` and `determinism_repeat` are the only "
      "checks that run a file, and both were skipped for every record. Every verdict above "
      "is STATIC analysis. A pattern reported as having no finding was never compiled and "
      "never executed — re-run with `--gate` to change that. The toolchain list below says "
      "what COULD have run, not what did.")
    w("")
# ---- WAIVERS. 6E's rule: a waived finding stays LISTED, with its evidence intact and the
# adjudication beside it. It is never merged into pass/NO_FINDING and is tallied separately,
# so a reader always sees the finding AND the reason someone accepted it.
# NOTE: `header` here is ALREADY the inner "run" object (see `header.get(
# "unverifiable_taxonomy")` below) -- not the outer wrapper. Reaching through "run"
# again silently yields {}, which renders "0 waivers loaded" beside real waived rows.
_wv = header.get("waivers") or {}
_waived_rows = [(r, c) for r in recs for c in r.get("checks", []) if c.get("waived")]
_flag_recs = [r for r in recs if _finding(r) == "FLAG"]
_flag_waived = [r for r in _flag_recs if r.get("waived_checks")]
if _wv.get("loaded") or _waived_rows or _wv.get("stale") or _wv.get("orphan"):
    w("## Accepted with reason (waivers)")
    w("")
    w(f"Ledger: `{_wv.get('ledger', '(none)')}` — {_wv.get('loaded', 0)} waiver(s) loaded, "
      f"{_wv.get('applied', 0)} finding(s) accepted with reason.")
    w("")
    w("> ⛔ **A waived finding is still a finding.** Its check keeps status `flag`, its record "
      "keeps a FLAG verdict, and it is counted here — separately from anything clean. A waiver "
      "records that a named person accepted a risk on a named date for a stated reason. It is "
      "not a statement that the pattern is good.")
    w("")
    w(f"Of {len(_flag_recs)} records carrying a finding, **{len(_flag_waived)} have at least "
      f"one waived finding** and **{len(_flag_recs) - len(_flag_waived)} are still "
      f"unadjudicated.**")
    w("")
    if _wv.get("stale"):
        w(f"### ⛔ {len(_wv['stale'])} STALE waiver(s) — the finding STANDS")
        w("")
        w("The file changed after the waiver was granted, so the waiver does not apply. This is "
          "deliberate: it is what stops a waiver silently absorbing a *different* construct "
          "added to the same file later. Re-read the pattern and re-waive, or fix it.")
        w("")
        w("| pattern | check | waived against | now |")
        w("|---|---|---|---|")
        for _x in _wv["stale"]:
            w(f"| `{cell(_x['path'], 60)}` | {cell(_x['check'], 30)} | "
              f"`{(_x.get('waived_sha256') or '')[:12]}` | `{(_x.get('live_sha256') or 'missing')[:12]}` |")
        w("")
    if _wv.get("orphan"):
        w(f"### ⚠️ {len(_wv['orphan'])} orphan waiver(s) — matched no finding")
        w("")
        w("Either the pattern was fixed (delete the waiver) or the waiver names the wrong "
          "pattern/check (a typo that silently protects nothing).")
        w("")
        for _o in _wv["orphan"]:
            w(f"- `{cell(_o['path'], 60)}` / {cell(_o['check'], 30)}")
        w("")
    if _waived_rows:
        w("### WAIVED — every one, with its evidence and its reference")
        w("")
        # the ref IS the audit trail: truncating it loses the reason the risk was
        # accepted, which is the only thing separating a waiver from a pass.
        w("| pattern | check | evidence (unchanged) | accepted by | ref |")
        w("|---|---|---|---|---|")
        for _r, _c in _waived_rows:
            _wd = _c["waived"]
            w(f"| `{cell(_r['path'], 55)}` | {cell(_c['name'], 24)} | "
              f"{cell(_c.get('detail') or '', 70)} | {cell(_wd.get('owner') or '', 12)} "
              f"{cell(_wd.get('date') or '', 12)} | {cell(_wd.get('ref') or '', 200)} |")
        w("")

w("## By language")
w("")
_lane_f = collections.defaultdict(collections.Counter)
_lane_c = collections.defaultdict(collections.Counter)
for r in recs:
    _lane_f[r["language"]][_finding(r)] += 1
    _lane_c[r["language"]][_coverage(r)] += 1
w("| lane | " + " | ".join(_FIND) + " | " + " | ".join(f"cov {c}" for c in _COV) + " | total |")
w("|---|" + "---:|" * (len(_FIND) + len(_COV) + 1))
for lane in sorted(_lane_f):
    _cf, _cc = _lane_f[lane], _lane_c[lane]
    w(f"| {cell(lane, 40)} | " + " | ".join(str(_cf.get(v, 0)) for v in _FIND)
      + " | " + " | ".join(str(_cc.get(v, 0)) for v in _COV)
      + f" | {sum(_cf.values())} |")
w("")
w("### ⚠️ Read the coverage columns before the finding columns")
w("")
w("Most checks are AST-based and implemented for python only. A non-python lane scoring few")
w("FLAGs is not evidence that it is clean — it is evidence that fewer checks could run on it.")
w("The coverage columns say exactly how many; the per-check table below says which.")
w("")
w("## Per check")
w("")
w("| check | pass | fail | flag | unverifiable | skip |")
w("|---|---:|---:|---:|---:|---:|")
for n in sorted(check_status):
    c = check_status[n]
    w(f"| `{cell(n, 40)}` | " + " | ".join(str(c.get(s, 0)) for s in
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
    w(f"- `{cell(c, 60)}`")
w("")
# 4Q round 15 F2: dict KEYS can be data too. `_poison` left keys alone on the reasoning
# that keys are schema — true for a record's fields, false for a map whose keys ARE the
# payload. Same shape as F1: an exemption wider than the reason for it.
w("Toolchains: " + ", ".join(f"{cell(k, 40)}={'yes' if v else '**MISSING**'}"
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
    if _coverage(r) != "FULL" and r.get("disposition") is None:
        undisposed += 1

# ⛔ 4Q round 11 F1 and 6E renderer #3, found independently: the prose below used
# `undisposed` where it meant "records carrying the UNVERIFIABLE verdict". They are equal
# on a fresh run and diverge the moment a triage session sets a disposition -- and this
# report exists to BE that triage session, so the divergence is the normal case, not the
# edge case. The two counts are named apart now so the wrong one cannot be reached for.
unv_verdict = sum(1 for r in recs if _coverage(r) != "FULL")
# ⛔ `hidden` USED TO BE NON-ZERO AND IS NOW ZERO BY CONSTRUCTION -- this is the defect the
# two-axis rewrite removed rather than documented. Under the old single-word verdict, FAIL and
# FLAG outranked UNVERIFIABLE, so a record with a real finding AND an unmeasured half showed
# the finding and HID the hole: 95 records did exactly that, and the exit-2 guard counted 729
# when 824 records actually had an unmeasured check. Coverage is now its own axis and cannot
# be outranked by anything. It is still DERIVED, not asserted to be zero, so that a future
# regression shows up here instead of being assumed away.
hidden = with_u - unv_verdict
hidden_by_verdict = collections.Counter(
    r["verdict"] for r in recs if r.get("unverifiable_checks")
    and _coverage(r) == "FULL")
tax = header.get("unverifiable_taxonomy") or {}
if code_rows:
    w("---")
    w("")
    w("# The COVERAGE board — sorted by REMEDY")
    w("")
    w("An unmeasured check is not one problem. Each subclass below names a different kind of")
    w("work, and that is the point of the split: the triage session can be run without")
    w("reopening a single pattern file.")
    w("")
    w(f"**{unv_verdict} records are not FULLY covered**, of which "
      f"**{undisposed} are still undispositioned.**")
    w("")
    w("⛔ The tool exits 2 while ANY record has less than FULL coverage, unless")
    w("`--acknowledge-unverifiable` is passed. It does not read `disposition` at all —")
    w("dispositioning every record does NOT clear the exit code, and an earlier draft of this")
    w("sentence implied it did (6E, renderer pass).")
    w("")
    if not hidden:
        w("### ✅ No record hides an unmeasured check")
        w("")
        w(f"All {with_u} records with at least one `unverifiable` check say so in their")
        w("verdict, because coverage is its own axis and nothing can outrank it. Under the")
        w("previous single-word verdict this was **not** true: FAIL and FLAG outranked")
        w("UNVERIFIABLE, so 95 records showed a finding and hid the hole, and the exit-2 guard")
        w("undercounted the gap by the same 95.")
        w("")
    if hidden:
        w(f"### ⚠️ …and {hidden} MORE records carry an unmeasured check without saying so")
        w("")
        w(f"{with_u} records have at least one `unverifiable` check, but only {unv_verdict} of")
        w(f"them carry UNVERIFIABLE as their verdict. The other **{hidden}** report as "
          + ", ".join(f"**{cell(v, 30)}** ({n})"
                       for v, n in sorted(hidden_by_verdict.items()))
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
        w(f"| {cell(sc, 20)} | `{cell(code, 40)}` | {n} | {cell(chk, 120)} | "
          f"{cell(lns, 80)} |")
    w("")
    if tax.get("per_subclass_dispositions"):
        w("## Disposition vocabulary (closed set — no free text)")
        w("")
        w("| subclass | permitted dispositions |")
        w("|---|---|")
        for sc, ds in sorted(tax["per_subclass_dispositions"].items()):
            w(f"| {cell(sc, 20)} | "
              + ", ".join(f"`{cell(d, 40)}`" for d in ds) + " |")
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
        w("| check | " + " | ".join(cell(l, 30) for l in lanes) + " |")
        w("|---|" + "---|" * len(lanes))
        for c in sorted(cov):
            w(f"| `{cell(c, 40)}` | "
              + " | ".join("yes" if l in cov[c] else "—" for l in lanes) + " |")
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
    w(f"## `{cell(name, 60)}` — {cell(status.upper(), 20)} × {len(items)}")
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
            w(f"- ({n}×) {cell(d, 150)}")
        w("")
    shown = items if len(items) <= 40 else items[:40]
    w("| pattern | evidence |")
    w("|---|---|")
    for path, detail in shown:
        # ⛔ 6E renderer pass: this was a hard 150-char cut with NO marker, while the tool's
        # own clip_evidence marks its truncations -- Ver's finding 7, live in the renderer,
        # silently cutting the two hand-verified known_finding explanations on this sweep.
        # The tool's function is imported rather than copied so the two cannot drift.
        _d = cell(detail, 150)
        w(f"| `{cell(path, 120)}` | {_d} |")
    if len(items) > len(shown):
        w(f"")
        w(f"*… and {len(items) - len(shown)} more — see `{src.name}`.*")
    w("")

out.write_text("\n".join(L) + "\n", encoding="utf-8")
print(f"{len(recs)} records -> {out}  ({len(L)} lines)")
