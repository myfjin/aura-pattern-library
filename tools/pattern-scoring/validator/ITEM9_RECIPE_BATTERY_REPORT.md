# Open-loop item 9 — full recipe battery: COMPLETION REPORT

**Date:** 2026-07-27 · **Ruler:** frozen, verified 69/69 before and after (three runs, identical counts)

Item 9 had two lanes. **Lane B is finished. Lane A is finished for Go and R, NOT built for cpp/rust.**
Read the "What is NOT done" section — it is the honest half of this report.

---

## Lane B — probe pass over the 151 NaN/domain FLAG suspects ✅

The library-wide sweep produced `FLAG` for 325 of 380 python DS patterns, of which exactly **151**
carried `nan_output` / `silent_domain_acceptance`. That aggregate label hid two opposite
behaviours. `nan_domain_probe.py` re-fires only those fixtures and records the real input→output
pair for each.

| class | n | meaning |
|---|---:|---|
| **FABRICATED_CERTAINTY** | **23** | NaN in → finite confident output, no raise. Conclusive-kill class. |
| DOMAIN_SILENT | 18 | invalid domain value → finite output. Needs your ruling. |
| VISIBLE_POISON | 100 | NaN in → NaN out. Honest propagation — **benign**. |
| NO_OP_ATTACK | 3 | attacked param never changed the result — unreachable. |
| GUARDED | 7 | every attack raised. Good. |

**Two thirds of the 151 were never defects.** The actionable residue is 23 + 18, not 151.

### The root cause worth naming — the NaN comparison trap
15 of the 23 kills are one bug in one shape:
```python
return var * n / (n - 1) if var > 0 else 0.0            # NaN > 0        is False
return (mean - rf) / std_dev if std_dev > 1e-14 else 0.0 # NaN > 1e-14    is False
```
Every comparison against NaN is False, so the **defensive `else` fires and returns a confident
0.0**. The guard written to make the code safe is exactly what converts unreadable data into a
fabricated number. Equality has the same hole: `confusion_matrix` compares `y_true[i] == 1`, NaN
fails every branch, and the poisoned row is silently dropped — the cells sum to 5 for 6 inputs
while the matrix still looks complete.

Hand-verified sample: `naive_variance`, `sharpe_ratio`, `fixed_n_test`, `confusion_matrix` —
**4/4 real**. The other 19 are machine-classified, not hand-read.

Cards: `NAN_DOMAIN_EVIDENCE_CARDS.md` · data: `nan_domain_probe_report.json`

---

## Lane A — compiled-language attack lanes

`polyglot.py` deferred this explicitly: *"Deep attack-injection stays python-only until
compiled-language harness editing lands (v2)."*

### Go ✅ — `compiled_harness.py`
Copies the pattern into a temp module with its `main` renamed, emits a **second** file holding the
attack driver (Go forbids imports after declarations, so appending is illegal), then `go run`s it
with every call behind its own `recover()`.

**Coverage: 72 functions driven · 282 skipped** across 103 patterns. Skips are counted, not hidden:
they are maps/contexts/struct-pointers (unconstructible) and constructors with no numeric
parameter. Results: **3 FABRICATED_CERTAINTY**, 5 VISIBLE_POISON, 14 VALUE_PRESERVED,
11 NO_OP_ATTACK, 6 GUARDED, 64 NO_EVIDENCE.

The three, all hand-verified:
- **`crash_loop_detector.newCrashLoopDetector(windowSeconds=NaN)`** → window field becomes **0**
  (baseline 2 000 000 000 ns). A crash-loop detector with a zero window detects nothing. This is
  the exact `Duration`-vanishes class recipes.py recorded from GO batch 1.
- **`batch_controller.mk(throughput=NaN)`** → a struct field silently becomes 0.
- **`bloom_filter.calculateBitCount(capacity=1<<62)`** → **negative** bit count (−6653256548922161151):
  a genuine signed-integer overflow. Its `errorRate=NaN → 1` is weaker evidence: that function's
  baseline is already degenerate (returns −3), so read the overflow, not the NaN, as the finding.

### R ✅ built, but the corpus refuses it — `r_harness.py`
Adaptive (R is dynamically typed, so there are no annotations to read a domain from) and fires
R's own `NA` alongside `NaN`, per the `na_probe` prior of 1.0.

**The structural finding matters more than the numbers: only 10 of 60 R patterns define a
top-level function at all.** The other 50 are straight-line scripts with assertions — there is no
parameter to inject into, so an attack lane *cannot* reach them by construction. Final coverage
after the baseline-validity guard: **3 functions driven, 0 kills, 3 VISIBLE_POISON.**
R's assurance must keep coming from the ORACLE LAW plus mutation/reseed (`r_reseed_scan.py`),
not from parameter injection.

### cpp / rust ❌ NOT BUILT
No harness exists for either. The design is known and recorded so it is not re-derived:
- **cpp**: a driver `#define main auraOrigMain` / `#include "pattern.cpp"` / `#undef main`, then
  its own `main`. Needs a C++ signature parser (templates and overloads are the hard part).
- **rust**: textual rename of `fn main` + append a driver (Rust allows `use` after items, so
  appending is legal, unlike Go). Note `rustc -O` **wraps integer overflow silently** while debug
  builds panic — the harness must compile both ways or it will read release-mode wrapping as
  normal.

Do not read "battery over 1,409 patterns" as done. It is done for python (the 151) and Go, begun
and bounded for R, and untouched for cpp/rust.

---

## Five false-positive classes found and fixed DURING this pass
Every one of these would have demoted a correct pattern. They are the real product of the run.

1. **Shallow NaN scan** — the executor's `_has_nan_out` never recurses into dicts/sets/arrays, so
   `{nan: 0.0}` read as clean finite output. Visible poison misfiled as a silent kill.
2. **No attack-reachability guard** — attacks on unused parameters counted as kills. Adding the
   guard moved the count **45 → 23**.
3. **Inf treated as NaN** — `tricube_weight` documents "else 0", so `tricube_weight(inf) == 0.0`
   is its contract. Only NaN (which means *unknown*) is conclusive; Inf is reported separately.
4. **Nondeterministic baselines** — Go outputs differ run-to-run by timestamp, pointer address and
   event id. Raw string comparison produced two false OVERFLOW_WRAP kills on the first run;
   outputs are now normalised, and a faithfully-stored `1<<62` is VALUE_PRESERVED, not a wrap.
5. **Boolean predicates** — `approxEqual(NaN, b, tol) → false` is *mathematically correct*.
   Excluding `bool` returns dropped Go from 4 kills to 3.

Plus one guard shared by both new lanes: **baseline validity** — if the clean call already panics
or already returns NaN/NA, the function was never validly exercised and nothing measured against
it can be called a defect. That alone removed the R lane's only "kill".

---

## Verification
- Exam **69/69** run three times (before Lane B, after Lane B, after Lane A) — identical verdict
  counts `{PASS 49, FLAG 7, INVALID 13, SKIP 0}` every time. **The ruler did not move.**
- Full python sweep reproduced its prior counts exactly `{PASS 15, FLAG 325, INVALID 0, SKIP 40}`
  over 380 patterns — the 07-26 sweep non-determinism is genuinely gone.
- **Nothing was written into the library.** No pattern edited, demoted, quarantined or re-signed.
  These are evidence cards for your gate, in the spirit of the 191 description drafts.

## One tool defect noticed in passing
`sweep.py --exam` and the full sweep both write `sweep_report.json`, so running the exam
**silently clobbers** the full-sweep report. Worth separate filenames; it cost a re-run here.
