# hierarchical shrinkage 2level

**Language:** Python · **Sphere:** data-science · **Category:** Bayesian III — Approximate Inference

**Signature:** `(groups: List[List[float]]) → List[float]`

## What it does

Hierarchical shrinkage (James-Stein): partial-pooling beats no-pooling on MSE.

When group means are estimated from noisy, small samples, shrinking them toward the grand
mean reduces total error — the James-Stein effect. The positive-part JS estimator dominates
the no-pooling (per-group MLE) estimator whenever there are ≥3 groups and sampling noise is
non-trivial. Core claim: partial-pooling MSE-to-truth is strictly LOWER than no-pooling.

## Guarantee

When it runs, hierarchical shrinkage 2level guarantees mse_js < mse_no_pool; mse_js < 0.6 * mse_no_pool (weak-grade: directional, proven by run).

**Checkable constraints:**

- `mse_js < mse_no_pool`
- `mse_js < 0.6 * mse_no_pool`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
