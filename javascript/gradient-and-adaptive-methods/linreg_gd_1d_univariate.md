# linreg gd 1d univariate

**Language:** JavaScript · **Sphere:** javascript · **Category:** Gradient & Adaptive Methods

**Signature:** `(X, y, lr, iters) → object`

## What it does

Univariate linear regression via batch gradient descent

## Guarantee

When it runs, linreg gd 1d univariate guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node linreg_gd_1d_univariate.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `univariateGd(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array (n × nf). `y` is the target vector. `lr` is the learning rate. `iters` is the iteration count.
**Core:** Standard batch gradient descent: computes the prediction for every sample, accumulates the gradient over the full data set, averages, then updates weights and bias with a fixed step `lr`. This is the plain-vanilla GD that all optimiser variants in later batches are compared against.
**Assert:** Asserts 2 weights and a finite bias. Compares against expected values at 1e-9 relative tolerance.
**⚠️ Defect:** The fixture runs 200 iterations at `lr=0.05` and locks in whatever weights are reached — `[1.842, 2.871]` — which is short of the true `[2, 3]` by an error of 0.16. The algorithm has not converged; it has simply stopped. This under-convergence is the baseline every optimiser in batch 6 is compared against — an optimiser that converges faster will produce different weights at iteration 200 and FAIL this self-test, even though it is better. The name says "univariate" but the fixture uses `nf=2` (two features).

---
*△ AURA Pattern Library — © Reality Optimizer*
