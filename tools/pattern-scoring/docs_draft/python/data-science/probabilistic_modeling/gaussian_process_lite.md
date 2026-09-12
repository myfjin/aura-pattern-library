# Gaussian Process Regression (Lite)

**File:** `python/data-science/probabilistic_modeling/gaussian_process_lite.py`
**Sphere:** Data Science — Probabilistic Modeling

---

## What it solves

**Gaussian process regression with RBF kernel, small n, direct Cholesky solve.** Places Gaussian priors on function values; posterior mean interpolates training data. "Lite" = RBF kernel only, direct dense solve (no sparse/inducing points).

**When to use:** Small-data regression with uncertainty, interpolation, Bayesian optimization.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `X_train`, `y_train` | List[float], training points | |
| `X_test` | List[float], test points | |
| `noise` | float > 0, observation noise | |
| `length_scale` | float > 0, RBF kernel width | |

---

## How inputs shape the output

- **Training points are interpolated** (prediction within 0.5 of true).
- **CI coverage ≥ 85%** on held-out points — the defining claim.
- **CI bounds are above the mean** — valid uncertainty.

---

## Worked example (real run)

```
$ python3 python/data-science/probabilistic_modeling/gaussian_process_lite.py
held-out CI coverage: 92% (12/13)
PASS
```

**Reading the output:** on a noisy sine function with 6 training points, the GP interpolates training data and achieves 92% CI coverage on 13 held-out points.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| duplicate training points | K matrix near-singular | regularization via noise |
| very few points | wide CI | high uncertainty |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20