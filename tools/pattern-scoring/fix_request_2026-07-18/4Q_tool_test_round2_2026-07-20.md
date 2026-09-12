# 4Q — validation tool round-2 adversarial test report
**2026-07-20**

## Baseline

Fixed tool v1.1 reproduces 4/4 exam verdicts and now flags `power_analysis_sample_size.py` as `FLAG` (mechanical coverage removed, coverage derived). I attacked the fixed tool on three fronts asked by Fable.

## Attack (a) — spoofing a positive oracle (numeric/semantic/invariant)

### Numeric oracle spoof

**Attempt:** Probe sets `oracle_match=True` (claims the numeric oracle matched) for a pattern that returns `42.0` with no actual comparison.
**Tool behavior:**
- `classify_signal` returns `confident_output_unproven` / `NEEDS_ORACLE` (because output is finite and no kill signal fired).
- `derive_coverage` sees `probe_result.get("oracle_match") is not None` and sets `numeric: True`.
- `verdict_from_signals` sees `unproven` + positive numeric oracle → `PASS`.

**Result:** LIE achieved. A probe can still spoof numeric coverage by claiming `oracle_match=True`.

**Mechanism failure:** `derive_coverage` treats any non-None `oracle_match` as evidence of a numeric oracle, without verifying the oracle actually ran and compared something. A probe could set `oracle_match=True` without a ground-truth comparison.

**Suggested fix:** `derive_coverage` should require both `probe_result.get("oracle_match") is not None` AND the presence of an `oracle` fixture or a `truth` value in the probe result. Or better: the numeric oracle should be a separate layer that always returns `oracle_match ∈ {True, False}` with a `compared` flag.

### Semantic oracle spoof

**Attempt:** Probe wants to claim semantic coverage without any semantic signal.
**Tool behavior:** With no `nan_absorbed_silently`, no `invariant_broken`, no `output_identical_to_clean`, `derive_coverage` correctly sets `semantic: False`. Verdict = `FLAG`.

**Result:** Spoof blocked.

**But:** `validate.py` still appends semantic KILL signals from probe booleans:
```python
if r.get("confident_impossible") or r.get("nan_absorbed_silently"):
    signals.append(("silent_wrong_on_invalid", "KILL_signal"))
```
A probe author can set these booleans arbitrarily and thereby both produce a KILL verdict and claim semantic coverage. This is a semantic-spoof backdoor.

**Suggested fix:** Remove probe-boolean short-circuits. The oracle should decide `silent_wrong_on_invalid` from raw outputs (e.g., NaN poison run vs clean run, output still finite and plausible → KILL; domain violation + finite output → KILL).

### Invariant oracle spoof

**Attempt:** Probe sets `invariant_checked=True` with no actual invariant signal.
**Tool behavior:** `derive_coverage` sets `invariant: True` solely from `invariant_checked`. Verdict = `PASS`.

**Result:** LIE achieved. `invariant_checked` is still probe-trusted.

**Suggested fix:** `derive_coverage` should set `invariant: True` only if an invariant was actually checked and the result was either `invariant_broken: False` or the invariant held. A boolean flag from the probe is not enough; need the invariant definition + result.

## Attack (b) — hole in derived-coverage logic

**Finding:** `derive_coverage` is a step forward, but it still trusts the probe for:
- `oracle_match` (non-None = numeric oracle ran)
- `invariant_checked` (boolean = invariant oracle ran)
- the semantic-signal booleans injected in `validate.py`

A determined probe author can still manufacture positive coverage in two of the three channels (numeric, invariant) and manufacture a KILL signal from a semantic boolean.

**The deeper hole:** there is no independent auditor of the probe. The tool trusts probe metadata even though `mechanical` was demoted. The coverage derivation moved from "probe claims all" to "probe claims specific oracles"; it did not add verification that those oracles actually executed and produced the claimed result.

**Suggested fix:** Introduce a `ProbeAudit` layer. A probe's raw result must include the actual oracle object/fixture/invariant that was checked. `derive_coverage` then checks whether that object exists and whether the comparison was meaningful (e.g., numeric oracle has a non-trivial ground-truth function).

## Attack (c) — recipes.py not wired to drive probes

**Finding:** `validate.py` uses `probes.PROBES.get(relpath)()` directly. `recipes.fire_all()` is never called to generate fixtures. The exam is graded against hand-tuned probes.

**Consequence:** A hand-tuned probe can pass the exam while the recipe library would have found additional defects.

**Example:** For `power_analysis_sample_size.py` arg spec `[p1, p2, alpha, power]`, `recipes.fire_all()` generates:
- R1/R2 domain under/over for every numeric param (8 fixtures)
- R3 degenerate-equal on `p1 == p2` (E002)
- R6 wrong-type (None/string) for every param
- R12 mutation probe

The current hand probe only tests `p1=1.5`. It does NOT test:
- `p1 == p2 = 0.5` (R3) → would raise `ZeroDivisionError` (accidental catch, already known)
- `alpha = -0.05` (R1) → in the demo raises, in the entry function returns a number silently
- `power = 0.0` (R1 domain-under) → unknown behavior

A recipe-driven engine would surface more behavior than the hand probe. The current exam score is therefore partly a score of probe quality, not recipe completeness.

**Suggested fix:** v1.5 must wire `recipes.fire_all()` to a generic executor that takes the manifest arg_spec, builds fixtures, calls the entry function, and lets the oracle classify. Hand probes should become regression tests, not the primary grading mechanism.

## Attack (d) — concurrency detection hole

**Finding:** `_scan_concurrency` uses a regex:
```python
r"\b(Atomic\w*|compare_exchange|thread::spawn|Mutex|RwLock|threading\.|multiprocessing\.|goroutine|go func|sync\.)\b"
```
- It correctly flags `atomic_spinlock.rs`.
- It does NOT flag `std::thread::spawn` (with namespace prefix) or `std::sync::Mutex`.
- It could false-positive on Python docstrings mentioning `threading`.

**Result:** A rust pattern using fully-qualified names or a Python docstring-only mention could bypass or trigger the cap incorrectly. This is minor for v1 because the only concurrency pattern is detected, but it is a robustness gap.

## Attack (e) — harness_ok still probe-trusted

**Attempt:** Probe sets `harness_ok=True` for a pattern whose harness cannot actually report success/failure.
**Tool behavior:** With no positive oracle, verdict is `FLAG` anyway (no false-PASS). But if the probe also spoofs numeric/invariant coverage, harness_ok=True removes the harness gate and a PASS can result.

**Combined spoof:** `oracle_match=True` + `harness_ok=True` + finite output = `PASS`.

**Suggested fix:** `harness_ok` should be derived by checking whether the pattern's demo/harness produces observable success/failure output. Default should be `False` (cap at FLAG) unless proven otherwise.

## Summary of fixed vs still-broken

| Spoof path | v1.0 | v1.1 | Still exploitable? |
|---|---|---|---|
| mechanical coverage | yes | no | no |
| numeric oracle via `oracle_match=True` | yes | yes | yes |
| invariant via `invariant_checked=True` | yes | yes | yes |
| semantic KILL via probe booleans | yes | partially | yes (validate.py extra hook) |
| harness_ok | yes | yes | yes |
| recipes not wired | yes | yes | yes (honest v1.5 gap) |
| concurrency regex | n/a | mostly | minor |

## Proposals for v1.5

1. **Audit numeric oracle claims.** Require `oracle_match` to be accompanied by the actual ground-truth fixture/value used. `derive_coverage` checks `probe_result.get("oracle") is not None`.
2. **Audit invariant claims.** Require the invariant definition and the check result. Remove `invariant_checked` as a probe-trusted boolean.
3. **Remove probe semantic booleans.** Let the oracle derive `silent_wrong_on_invalid` from raw outputs (domain recipe + finite output + no raise = KILL).
4. **Default harness_ok=False.** Derive harness trustworthiness from observable success/failure reporting, not probe assertion.
5. **Wire recipes.py to a generic executor.** Hand probes become regression fixtures; the exam is graded on the recipe library.
6. **Strengthen concurrency regex.** Include `std::thread`, `std::sync`, `pthreads`, `tokio`, `rayon`, and require at least one real primitive (not docstring).
