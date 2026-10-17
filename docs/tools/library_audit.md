# `library_audit.py` — the second layer of library verification

Where [`library_verify.py`](library_verify.md) proves the library **is what it claims to be** (signed, watermarked, catalogued), `library_audit.py` tries to prove that **individual patterns are worth something** — mechanically, where possible, or flagged with evidence where not.

6E named the gap on 2026-08-30 as twelve classes. This tool implements the mechanically decidable ones and FLAGS the rest with evidence attached.

---

## Why it is a separate file

`library_verify.py`'s `census_mismatches` check **graduated** on 2026-08-30 after eight red-team rounds with 4Q (round 8: zero findings) plus Ver's honesty pass. Adding twelve new check classes into that file would **restart its graduation clock**. The graduated gate stays graduated; this layer is red-teamed on its own.

That is the shape to inherit: a graduation does not get reopened to add work — the new work goes in a new file.

---

## The law of this file

> **A CHECK THAT COULD NOT RUN MUST NEVER REPORT `pass`.**

Every check returns one of:

| Verdict | Meaning |
|---|---|
| `pass` | measured, and it is fine |
| `fail` | measured AND wrong (deterministic defect) |
| `flag` | measured something suspicious; evidence attached, judgement needed |
| `unverifiable` | could not measure (no implementation for this language, hang, missing tool) |
| `skip` | genuinely not applicable, or not requested; `detail` says which |

A language with no implementation for a check gets `unverifiable`, **never `pass`**. That is the vacuous-fixture trap: a check that cannot fail scores as a pass no matter how broken it is.

A per-record field named `NO_FINDING` (not `PASS`) was Ver's honesty-pass correction on 2026-08-30 — "PASS" told a reader *"this pattern is good"* when the tool only ever measured the classes it could check (C1 / C3 / C11 were never assessed for any pattern). The clean verdict is `NO_FINDING`, not `PASS`.

---

## Dependencies

- Python ≥ 3.10
- **[folder-nature](https://github.com/myfjin/folder-nature)** (transitively via `library_verify`)
- Toolchains under `--gate`: `python3`, `Rscript`, `node`, `g++`, `go`, `rustc`

---

## CLI

```
library_audit.py [--out PATH] [--gate] [--repeat N] [--timeout S]
                 [--limit N] [--waivers PATH] [--acknowledge-unverifiable]
                 [--root PATH] [--self-test]
```

| Flag | Default | Effect |
|---|---|---|
| `--out` | `AUDIT-RESULTS.jsonl` | output JSONL path |
| `--gate` | off | also run the checks that need to execute code |
| `--repeat` | `1` | repeat each run N times (determinism probe) |
| `--timeout` | per-check | override the per-check timeout |
| `--limit` | all | audit only the first N patterns (useful for quick tests) |
| `--waivers` | none | path to a waivers file (pre-approved flags) |
| `--acknowledge-unverifiable` | off | admit the `unverifiable` set without halting |
| `--root` | `.` | library root (if run from elsewhere) |
| `--self-test` | off | run the probe suite that proves each check can both pass and fail |

---

## Output

JSONL. **Line 1 is the run header.** Every subsequent line is one pattern record. Record design is 6E's, from `REPORT-6E-VALIDATOR-DESIGN.md` §3.

Example header fields: `tool_version`, `run_started_utc`, `root_sha`, `pattern_count`, `check_classes`, `verdicts_declared`, `toolchain_versions`.

Example pattern record fields: `path`, `pattern_id`, `lang`, per-check verdict + reason-code + detail, aggregate `verdict`, `evidence` (truncation-marker if clipped).

Clip discipline: **every data-derived string reaches the output through `cell()`** (6E's funnel). 6E round 13 found 11 slots emitting raw; 4Q round 12 found 2 more; the page-level probe now asserts the grammar rather than trusting the funnel's own docstring.

---

## The 12 check classes (6E's taxonomy)

Mechanically decidable (`pass` / `fail` / `flag` / `unverifiable` / `skip`):

| C# | What it checks |
|---|---|
| C1 | asserts are non-vacuous (not deleted by `-DNDEBUG` or equivalent) |
| C2 | determinism markers present where expected |
| C3 | third-party deps declared (not imported stealth) |
| C4 | duplicate-map: no copy-paste of another pattern's body |
| C5 | hollow: no `pass` / `TODO` / stub-looking body |
| C6 | import discipline per language (importlib.import_module paths; computed names left alone) |
| C7 | hardcoded absolute paths |
| C8 | dangerous primitives (eval, exec, shell=True) require stated justification |
| C9 | view coverage: declared view matches derived view (code / code+strings) |
| C10 | undeclared-check-consumes-strip detection |
| C11 | fail-open on malformed input (returns `unverifiable`, not pass) |
| C12 | NEGATIVE ARM proofs (wellformed file still produces its normal verdict) |

---

## `--self-test` — what it proves

Not a smoke test. A **vacuous-check prevention proof**:

- `C6-py` import_module probes across stdlib / third-party / aliased / local-def / unrelated-module.
- DF filter arms: **positive** (`20/20` correctly linked when applied) and **negative** (`0/20` not falsely linked when removed).
- `VIEW_COVERAGE` declaration-vs-derivation parity for every subclass.
- `R26` two-strip length invariant on known test files.
- `R27` fail-open proofs: malformed file ⇒ `unverifiable`, wellformed file ⇒ real verdict.
- `R28` same for hollow, abs_paths, assert_nonvacuous, deps.

**578 probes, 0 failures** is the known-good state. A single failure means a check regressed to being able to false-pass. Any `--self-test` failure is RED, no exceptions.

---

## When to run it

- **Weekly scheduled**, on `master`, `--gate` enabled. The result lands as `AUDIT-RESULTS-YYYY-MM-DD.jsonl`; the triage view via [`audit_report.py`](audit_report.md).
- **Before shipping a release.**
- **After adding new check classes** — run `--self-test` to prove the new class can both pass and fail; add a NEGATIVE ARM probe for it.
- **When flagging a pattern as suspect** — use `--limit 1 --root <path>` for a focused re-measure.

---

## Related

- [`library_verify.md`](library_verify.md) — the graduated gate this one deliberately does not merge into.
- [`audit_report.md`](audit_report.md) — the triage renderer for this tool's JSONL.
- [`polyglot.md`](polyglot.md) — the Layer-2 multi-language health runner.
- [`.claude/skills/library-operations/SKILL.md`](https://github.com) — the operator-side skill.
