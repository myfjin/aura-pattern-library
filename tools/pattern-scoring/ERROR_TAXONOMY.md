# Error Taxonomy — every way a pattern can fail, and what the verdict means

**Scope:** the frozen ruler v1.0.0 as it actually runs — `utility_score.py` + `evidence_runner.py`
(Python) and the four native oracles (`rust_oracle.py`, `cpp_oracle.py`, `r_oracle.py`,
`go_oracle.py`). Every trigger below is extracted from the code, not from memory.
**Companion docs:** `VALIDATION_MANUAL.md` (how to test), and 6E's gate-design classification
(`bu@.8:/home/bu/patterns-to-analyze/ERROR_CLASSIFICATION.md`, 2026-07-15) — the A/B/C code
system that this taxonomy's statuses implement. Cross-references to those codes are given as (≈A1) etc.

*(Note for the record: an earlier version of this document was reported "deployed" on 2026-07-16
but never landed on disk. This is the real one — verify with `ls -la` and read it.)*

---

## 1. The pipeline — a pattern stops at the first gate it fails

```
pattern file
  → STRUCTURAL   can the file be read and parsed at all?
  → SENSE        is it a real, testable pattern (not a wrapper/script/hollow shell)?
  → DESCRIPTION  does it declare what it does and its input domain?
  → EVIDENCE     success-run · adversary-run · abuse (fuzz) — real executions
  → VERDICT      VERIFIED / needs_validity / invalid / quarantine / senseless / flagged
```

## 2. The statuses (what the form's `status` column can say)

| Status | Meaning | U | Who acts |
|---|---|---|---|
| `VERIFIED` | Ran, self-checks held, abuse survived, evidence card clean | computed | nobody — done (subject to Illia's ≤5% sample) |
| `needs_validity` | Has a real shape but the success-run could not prove it standalone (e.g. needs a live DB) — **unproven, not rejected** | computed | Illia decides: give it a runnable example, or accept the limit |
| `invalid` | A real check failed: assert broke, or abuse produced a **silently wrong** answer (fake-robust) | 0.0 | fix the pattern or drop it (≈A3/A4) |
| `senseless` | Sense-filter rejection: trivial wrapper (sklearn/numpy re-export), script-shaped (no top-level function/class), or hollow asserts — nothing real to test | none | restructure or drop (≈A2-adjacent; hollow ≈C-warning escalated) |
| `quarantine_no_description` | No docstring contract — nothing to verify against | none | one rewrite attempt, then Illia (≈A1) |
| `quarantine_undefined_domain` | Description exists but declares no input domain — can't be fuzzed | none | declare the domain, re-run (≈ abuse "UNDEFINED") |
| `flagged` | The *machinery* hit a wall on this file (see §3 structural reasons) — verdict withheld, never guessed | none | fix the file/environment, re-run |

**Law:** a status is never a bare word — the form carries `failing_column` + evidence with it.
A verdict without evidence is not trusted, from a script or a model or a vibe.

## 3. The failure reasons (`failing_column` / flags), by layer

**Structural** (≈A2)
- `read_error` — file unreadable
- `syntax_error` / `parse_error` — does not parse; nothing downstream runs

**Sense-filter**
- `senseless: trivial wrapper …` — re-exports stdlib/sklearn work (kills sklearn-wrapper library rot)
- `senseless: no top-level function or class` — script-shaped; nothing to import and fuzz
- `hollow_assert: all assertions are tautologies` — every assert is `assert True` / `1==1`.
  **Not hollow:** `assert False, "message"` — that is a negative test, the strongest kind.
  (This distinction was the 07-16 sense-filter bug; the AST rule now flags a file only when
  *every* assertion is a tautology.)

**Evidence / abuse** (the fuzz layer — 6E's Category B is what these probes exercise)
- `abuse_silent_output` — fed garbage (letters-for-numbers, empty, None-literals, negatives,
  overflow), produced output **without erroring**; machine can't judge correct-vs-wrong → flagged
  for human eyes. The honest boundary.
- `abuse_wrong` — fed garbage, produced a **provably wrong** answer without erroring → `invalid`.
  This is fake-robust, the #1 failure the ruler exists to catch.
- `domain_undefined` — no declared input domain → `quarantine_undefined_domain`
- `evidence_runner_error` — the probe machinery itself failed; verdict withheld (`flagged`), never guessed

**The input-error classes** (Illia's requirement: "errors connected to incorrect number format
input or language based errors" — 6E's B-category, what the abuse probes exercise):

| Class | Bad input | Example |
|---|---|---|
| B1 type mismatch | letters where numbers belong | `"abc"` into a numeric arg |
| B2 shape mismatch | wrong dimensions/structure | 3×5 into a square-matrix arg |
| B3 numeric edge | zero/negative where positive assumed | division by 0, log of −1 |
| B4 null/NaN | `None`, `float('nan')`, missing values | NaN into a mean |
| B5 boundary | inf/overflow/underflow extremes | `1e18`, `-1`, `sys.maxsize` |
| B6 encoding/language | wrong-language or non-ASCII strings | `"сорок два"`, `"四十二"`, latin-1 bytes |
| B7 number format | locale formats where floats belong | `"3,14"`, `"1_000"`, `"1e"` |
| B8 empty | empty list/string/frame | `[]`, `""` |

**The three-way abuse rule (Illia's rule, verbatim in the mechanism):**
bad input → errors ✅ · bad input → handled per stated contract ✅ · bad input → no error +
silently wrong ❌ INVALID.

## 4. The native oracles (Rust · C++ · R · Go) — same frame, compiler as judge

Each oracle passed its own planted testbed (known-valid + known-fake cases) **before** touching
canonical patterns. The judge is the toolchain, never a model opinion.

| Oracle | Judge | `failing_column` values |
|---|---|---|
| `rust_oracle` | `rustc` (unsafe **forbidden**) + run | `compile_error` · `assert_failed` · `run_timeout` · `read_error` |
| `cpp_oracle` | `g++` **and** `clang++ -pedantic` + run | `compile_error_gcc` · `compile_error_clang` · `assert_failed` · `run_timeout` · `read_error` |
| `r_oracle` | `Rscript --vanilla` + `stopifnot` | `syntax_error` · `assert_failed` · `run_error` · `run_timeout` · `missing_dependency` (→ `needs_validity`, an env gap not a pattern fault) |
| `go_oracle` | `go run`, exit code | `compile_error` · `check_failed` · `run_timeout` · `read_error` |

Sense checks per language: a real self-test must exist (`stopifnot` in R, `assert`/exit-code
checks in Rust/C++/Go, `func main` + `os.Exit`/`panic` in Go) — else `senseless`.

## 5. How to read a rejection in the form

Open `output/UNIFIED_library_form_2026-07-16.csv`: the row gives `status` + `failing_column`;
the JSON form carries the full evidence card (claim · success-run · adversary-run · abuse ·
failing column). Reproduce any verdict:

```bash
# Python
python3 utility_score.py <file> --abuse          # single pattern, full card
# other languages
python3 <lang>_oracle.py <file>                  # single-file verdict as JSON
```

Deterministic by construction: same file + same ruler version → same verdict, byte-identical.
(Proven 2026-07-17: r_oracle re-run twice → identical to each other and to the frozen 07-16 form.)

## 6. What the machine refuses to decide (hand-offs to Illia)

- `abuse_silent_output` — output-without-error on garbage: correct-by-design or silently wrong?
- `needs_validity` — true-but-unprovable-standalone (external state like a DB)
- `quarantine_*` after one rewrite attempt
- The ≤5% deep audit of `VERIFIED` — does the code match what the description promises?
  The machine proves *it runs and holds*; only a human can prove *it means what it says*.
