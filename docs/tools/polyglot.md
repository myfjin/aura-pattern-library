# `polyglot.py` — multi-language health runner

Language-agnostic self-test runner for the whole library (6 languages). For `cpp` / `rust` / `go` / `r` / `javascript` / `python`, it **compiles and runs each pattern's own self-test** — the ORACLE LAW: cause the disaster, prove survival — and reports a single health card per pattern.

**Baseline HEALTH across all languages.** Deep attack-injection is python-only (see `executor.py`) until compiled-language harness editing lands (v2). Together: whole-library health + python deep-triage.

Location: [`tools/pattern-scoring/validator/polyglot.py`](../../tools/pattern-scoring/validator/polyglot.py)

---

## What question does it answer?

> *"Does this pattern's own self-test still hold on this machine, in this language, right now?"*

It is the only Layer-2 tool that reaches every language. Everything else (`executor`, `chaos_scan`, deep attack recipes) is python-only.

---

## The universal verdict (per pattern)

| Signal | Meaning |
|---|---|
| `BASELINE-OK` | compiles (if needed) AND runs clean (exit 0): its self-test holds |
| `COMPILE-FAIL` | does not compile (compiled langs only) |
| `RUNTIME-FAIL` | compiles but self-test fails / crashes / nonzero exit |
| `TIMEOUT` | hung |

Every card is a dict: `{"file": "<relpath>", "health": "<signal>", "detail": "<last 160 chars of relevant output>"}`.

**A missing toolchain is a `RUNTIME-FAIL` with the error visible in `detail`** (e.g. `[Errno 2] No such file or directory: 'Rscript'`). It never silently passes.

---

## Dependencies

- **Python ≥ 3.10** (for polyglot itself)
- **Toolchains for whatever languages you want measured:**
  - `python3` — python patterns
  - `Rscript` — R patterns
  - `node` — javascript patterns
  - `g++` (`-std=c++17`) — cpp patterns
  - `go` (any recent) — go patterns
  - `rustc` (`--edition 2021`) — rust patterns
- No folder-nature required. Pure stdlib + subprocess.

A missing toolchain surfaces in the pattern cards for that language, not as a silent skip. Install what you need before interpreting a sweep.

---

## API

Primary entry point: `polyglot.selftest(relpath)`. Call it per pattern:

```python
import sys
sys.path.insert(0, "tools/pattern-scoring/validator")
from polyglot import selftest

card = selftest("python/programming/sorting/01_insertion_sort.py")
# -> {"file": "...", "health": "BASELINE-OK", "detail": "..."}
```

Timeouts per language:
- python / javascript / R: 30s
- cpp / rust: 45s compile + 30s run
- go: 60s (go toolchain is heavier)

A hang beyond timeout returns `TIMEOUT` with exit code 124 captured in detail.

---

## Helper: `all_patterns(lang=None)`

Walks the library tree and yields every pattern's relpath, optionally filtered by language key (`"python" | "cpp" | "rust" | "go" | "r" | "javascript"`). Combined with `selftest()` this is the whole-library sweep.

---

## Example: six-language smoke

```python
from polyglot import selftest

samples = [
    "python/programming/monitoring/time_series_db.py",
    "cpp/data-science/probabilistic_modeling_bayes_ii/gamma_poisson_conjugate.cpp",
    "javascript/gradient-and-adaptive-methods/linreg_steepest_descent_exact.js",
    "go/system-administration/sysadmin/advisory_lock_timeout.go",
    "rust/parsing-protocols/query_string_parser.rs",
    "r/multivariate_and_applied_modeling/km_survival_lite.R",
]
for p in samples:
    r = selftest(p)
    print(f"{r['health']:14s}  {p}  {r.get('detail','')[:60]}")
```

Measured output (2026-10-17 on a Linux box without `Rscript`):

```
BASELINE-OK     python/programming/monitoring/time_series_db.py            in 20 exact, 10 buckets @245
BASELINE-OK     cpp/.../gamma_poisson_conjugate.cpp                         PASS
BASELINE-OK     javascript/.../linreg_steepest_descent_exact.js
BASELINE-OK     go/system-administration/.../advisory_lock_timeout.go       meout: holder held 0.5s
BASELINE-OK     rust/parsing-protocols/query_string_parser.rs               query_string_parser: PASS
RUNTIME-FAIL    r/.../km_survival_lite.R                                    [Errno 2] No such file: 'Rscript'
```

The last line is the point: polyglot refused to pass a language whose toolchain was missing, even though the pattern itself is fine. That is the honesty surface.

---

## Why it is a separate tool

`library_verify.py --gate` ALSO compiles and runs every file, but as part of the Layer-1 gate check. Polyglot is useful **as a standalone library-wide health probe** when:

- You are debugging a toolchain issue and want the per-pattern cards, not a single RED verdict.
- You are preparing a release and want to measure health across all languages before deciding what ships.
- You are red-teaming a new pattern and want its card next to the known-good baselines.
- You are grading the toolchain itself (new compiler version, new OS) and want to see which patterns flinch.

The output format (a dict per pattern) is easier to post-process than `library_verify.py`'s human-friendly table.

---

## Known limits

- **Not an attack lane.** `BASELINE-OK` means the self-test holds, not that the pattern survives adversarial input. For deep attack probes, see `executor.py` (python-only) and `chaos_scan.py`.
- **Serial.** No parallelism; a whole-library sweep is minutes to hours depending on the box.
- **Depends on your toolchain versions.** A pattern that passes on g++ 11 may FAIL on g++ 7 for legitimate language-standard reasons. Pin your toolchain if comparing runs.
- **Does not re-sign.** It is pure read; it never writes to the signed tree.

---

## Related

- [`library_verify.md`](library_verify.md) — Layer-1 gate; `--gate` is the integrated version of this check.
- [`library_audit.md`](library_audit.md) — second-layer, 12 check classes; broader than polyglot's one-signal health.
- [`harvest_gate.md`](harvest_gate.md) — Phase A proposer that uses polyglot indirectly through the harvest flow.
