# `audit_report.py` — JSONL → triage markdown

Takes the output of [`library_audit.py`](library_audit.md) (`AUDIT-RESULTS.jsonl`) and renders it as a document a human can act on. The JSONL is the record; this is the readout.

**It is not another check.** It performs no measurement, invents no verdicts, adds no evidence. It groups and formats what the audit already wrote.

---

## What question does it answer?

> *"1,500 records sorted by path is not triage, it is a list. Who should look at what, and in what order?"*

The audit emits one JSONL line per pattern record. On a healthy library most lines are clean; the interesting ones are a tiny fraction. `audit_report.py` groups them so the right eye lands on the right bucket:

- **by CHECK** — what is wrong (C1 vacuous asserts? C8 dangerous primitives? etc.)
- **by OWNER** — who decides (the per-sphere owner on record)

That is how the work gets divided. One triage document → N smaller work items.

---

## Dependencies

- Python ≥ 3.10
- Imports `clip_evidence` from `library_audit` (shared truncation discipline)
- No folder-nature required
- No toolchains required

---

## CLI

```
audit_report.py <input-jsonl>
```

Positional arg: path to the JSONL file written by `library_audit.py`.

Writes `AUDIT-REPORT.md` next to the input, replacing any previous version.

Exit 0 on success. Non-zero on a parse error in the JSONL (which is itself a bug worth catching — the audit emitted something malformed).

---

## What it reads

A JSONL where **line 1 is the run header** and every subsequent line is one pattern record. From the audit's own documentation:

- header: `tool_version`, `run_started_utc`, `root_sha`, `pattern_count`, `check_classes`, `verdicts_declared`, `toolchain_versions`
- record: `path`, `pattern_id`, `lang`, per-check verdict + reason-code + detail, aggregate `verdict`, `evidence` (truncation-marker if clipped)

---

## What it emits

A markdown document (`AUDIT-REPORT.md`) with:

1. **Run header** — audit version, start time, root SHA, pattern count, toolchain versions, the declared verdict set.
2. **By-CHECK sections** — one section per check class (C1 … C12). Only non-empty verdicts appear.
3. **By-OWNER sections** — one section per owner, listing their flagged / failed records.
4. **Analyser coverage table** — per language, which checks have an implementation vs which do not (so a reader knows what `unverifiable` columns actually mean).
5. **Taxonomy and judgement-class rows** — the subclass → remedy → disposition triples pulled from the audit records.

Example invocation + output:

```
$ python3 audit_report.py AUDIT-RESULTS.jsonl
1 records -> AUDIT-REPORT.md  (231 lines)
```

---

## The `cell()` funnel

Every data-derived string in the output reaches the page through `cell()` — the shared truncation + formatting helper.

**Comment that used to be there, and the lesson:** the old docstring said *"every data-derived string reaches the page through here"* and it was false — 6E's round-13 red-team found **eleven** slots emitting raw (lane names, reason codes, triage path, disposition rows, analyser coverage). An overclaiming comment is the reason the author stopped looking. Each of those now calls `cell()`, and the page-level probe asserts the grammar rather than trusting the docstring.

4Q's round 12 then inventoried all 14 text-to-page paths and found two more unclipped — the tool-defects table (a raw `repr()` of a list of dicts, 260+ chars in one cell) and the census mismatches. Patching those two by hand would have left the taxonomy and judgement-class rows exposed. So the fix is **the funnel**, not four patches: a non-string value is FORMATTED through `cell()` rather than `repr()`'d, and everything is clipped with the marker.

This is a shape worth inheriting outside this tool: *when a convention is enforced by a comment, the comment is wrong*. Enforce by call-site or by test.

---

## When to run it

- **Immediately after each `library_audit.py` run.** The JSONL is the primary artifact; the report is the human view.
- **In CI, as part of the weekly audit.** Attach `AUDIT-REPORT.md` to the audit run so reviewers see the triage, not the raw.
- **Any time you want to re-render** — the JSONL is append-only truth; the report is derived and safe to overwrite.

---

## Known limits

- **Does not re-audit.** If the JSONL is stale (patterns added since), the report will be stale too. Re-run `library_audit.py` first.
- **No HTML / no PDF.** Markdown only. Convert with pandoc if you need another format.
- **Depends on the record schema from the audit.** If the audit output changes format, the renderer may silently produce an incomplete section. The audit's `--self-test` catches schema regressions; this renderer trusts that.

---

## Related

- [`library_audit.md`](library_audit.md) — the source of the JSONL this tool renders.
- [`library_verify.md`](library_verify.md) — the layer-1 gate; audit sits on top of it.
