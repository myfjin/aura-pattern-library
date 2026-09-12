# Difference-in-Differences (DiD)

**File:** `python/data-science/causal_inference_and_experimentation/difference_in_differences.py`
**Sphere:** Data Science — Causal Inference and Experimentation

---

## What it solves

**Did the treatment actually work?** You have two groups (treated and control) observed before and after a policy change. You can't just compare after vs before (time trends confound) or treated vs control (groups may differ). DiD subtracts both: `(treated_after − treated_before) − (control_after − control_before)`. The key assumption: **parallel trends** — without treatment, both groups would have changed the same way.

**When to use:** You have pre/post data for both a treated and a control group, and you believe the parallel trends assumption is reasonable. Classic use: policy evaluation (a state enacts a law, neighboring state doesn't), program evaluation, pricing changes.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `n_per_group` | int > 0 | — |
| `treatment_effect` | float, the true causal effect | — |
| `time_effect` | float, the common trend | — |

---

## How inputs shape the output

- **Parallel trends are planted and recovered:** both groups get the same `time_effect` in the post-period, plus the treated group gets `treatment_effect`. The DiD estimator subtracts out the common trend, recovering the treatment effect within ~3 units of truth.
- **Pre-period sanity check:** running DiD on pre-period data only (no treatment yet) returns ~0 — confirming the estimator doesn't hallucinate effects where none exist.
- **Same-group sanity check:** running DiD on control vs itself returns ~0 — confirming the estimator doesn't find spurious effects from group differences alone.

---

## Worked example (real run)

```
$ python3 python/data-science/causal_inference_and_experimentation/difference_in_differences.py
True treatment effect: 20.00 | DiD estimate: 19.23 | Bias: 0.77 | Pre-period DiD: 0.12 | PASS
```

**Reading the output:** the true effect was 20; DiD estimated 19.23 (bias 0.77, within sampling error). The pre-period check (0.12 ≈ 0) confirms no spurious effect before treatment.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| `n_per_group = 0` | ZeroDivision in `mean()` | needs guard |
| non-parallel trends | DiD estimate is biased | assumption violation, not a code bug |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-18 · evidence: `output/manual_audit_2026-07-19.csv`
