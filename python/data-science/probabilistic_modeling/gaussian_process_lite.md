# gaussian process lite

**Language:** Python · **Sphere:** data-science · **Category:** Probabilistic Modeling

**Signature:** `(x1: float, x2: float, length_scale: float, sigma: float) → float`

## What it does

Gaussian process regression (lite): RBF kernel, small n, direct Cholesky solve.

Core idea: place Gaussian priors on function values; posterior mean interpolates
training data. "Lite" = RBF kernel only, direct dense solve (no sparse/inducing points).

When to use: small-data regression with uncertainty, interpolation, Bayesian optimization.

## Guarantee

When it runs, gaussian process lite guarantees abs(pred - true) < 0.5; len(means) == len(X_test); len(upper_bounds) == len(X_test) (proven by run).

**Checkable constraints:**

- `len(means) == len(X_test)`
- `len(upper_bounds) == len(X_test)`
- `abs(pred - true) < 0.5`
- `mean <= ub`
- `coverage >= 0.85`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
