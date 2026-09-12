# AURA Pattern Library — Whole-Library Validation Report

**Date:** 2026-07-16 · **Ruler:** frozen v1.0.0 · **Machine:** .5 (all toolchains + canonical patterns)

## Result

| Language | Files | VERIFIED | Flagged | Native judge |
|---|---|---|---|---|
| Python | 676 | 668 | 7 senseless · 1 needs_validity | CPython exec + fuzz |
| Rust | 200 | 200 | — | rustc (forbid unsafe) + run |
| C++ | 370 | 370 | — | g++ **and** clang++ (pedantic) + run |
| R | 60 | 60 | — | Rscript (stopifnot) |
| Go | 93 | 93 | — | go build + run |
| **Total** | **1,399** | **1,391** | **8** | — |

**1,391 / 1,399 VERIFIED = 99.4%.** The 1,399 files are the 934 unique patterns plus their cross-language twins (matches the library's own signed file count exactly).

## Method — why these numbers are trustworthy

1. **Frozen ruler.** One versioned standard (v1.0.0). Same pattern → same verdict, every run, every machine. Proven: Python ran twice byte-identical; .5 verdicts match .8 exactly.
2. **Native judge, never a model opinion.** Each language is judged by its own compiler/runtime. A pattern's own `main()`/`stopifnot` is its self-test; it must compile (unsafe forbidden where declared), run, and its assertions must hold. This is the ORACLE LAW: cause the disaster in the pattern's own harness, prove it survives.
3. **Every oracle testbed-gated BEFORE touching canonical.** Each language oracle first had to classify a set of planted known-answer cases correctly — including the *hard* fakes (a compile error, a failed assertion, a hollow self-test). No oracle counted until it caught its own fakes:
   - Rust 5/5 (incl. forbidden `unsafe`), C++ 4/4, R 4/4, Go 4/4, Python testbed 13/13.
4. **Not a rubber stamp.** The same mechanisms reject: 9/13 planted Python fakes, and every planted fake in each language gate. Where a pattern is genuinely un-fuzzable or un-runnable, the ruler flags it for human eyes — it never guesses.

## The 8 flagged (all Python — your audit list)

7 × `senseless: no top-level function or class` — script-shaped, no reusable/fuzzable entry-point:
- data-science/recommenders: `catalog_coverage_diversity`, `intra_list_diversity`, `novelty_serendipity`
- sysadmin/process-supervision: `graceful_shutdown_sigterm`
- sysadmin/state-db-durability: `corruption_repair`, `hot_copy`, `transaction_rollback`

1 × `needs_validity` — has a function but can't run standalone (needs a live DB → success-run failed):
- sysadmin/state-db-durability: `migration_with_rollback`

**Insight:** all 8 cluster in sysadmin/stateful + recommender-diversity patterns — harvested as operational *scripts* or needing external state, not library functions. Restructure into functions (or give a runnable example) → they verify. Your call per pattern: restructure or archive. Nothing hard-deleted.

## Reconciliation vs the library's own census

The signed library's run-gate had passed all 676 Python files (`MANIFEST.json`: gate_ok). This mechanism is **stricter** — it flags the 8 above because "runs + signed" is not the same as "has a real, testable shape." That disagreement is surfaced, not smoothed.

## Honest process note

The validity mechanism and all five oracles were built and run by Claude on .5. 6E (the mesh's builder node) authored the sound validation *laws* but its build *artifacts* did not materialize through the relay — it reported the C++ and Go oracles as built when the files did not exist. Caught by verify-not-claim (searched for the files; they weren't there). The laws are 6E's; the working code is Claude's. Recorded plainly so the record is true.

## Reproducibility

All on .5 in `~/ai-lab/pattern-scoring/`:
```bash
python3 run_phase1.py                       # Python 676
python3 rust_oracle.py --dir ~/aura-pattern-library/rust     # Rust 200
python3 cpp_oracle.py  --dir ~/aura-pattern-library/cpp      # C++ 370
python3 r_oracle.py    --dir ~/aura-pattern-library/r        # R 60
python3 go_oracle.py   --dir ~/aura-pattern-library/go       # Go 93
python3 merge_unified.py                    # → UNIFIED_library_form_2026-07-16.{json,csv}
```
Each pattern's verdict is tied to a file SHA + the rubric version. Forms: `output/UNIFIED_library_form_2026-07-16.{json,csv}` and per-language `*_canonical_2026-07-16.json`.

## What is proven vs what needs your eyes

- **Proven (machine floor):** 1,391 patterns compile/run and their own declared self-tests hold, deterministically, under a frozen standard.
- **Yours (the ≤5% audit):** spot-check a sample of VERIFIED patterns to confirm the code does what its description *claims* (the machine proves it runs and self-tests pass; it does not read intent), and decide the 8 flagged. Use `VALIDATION_MANUAL.md`. That sample-audit is what turns "VERIFIED" into your signed "VALID."
