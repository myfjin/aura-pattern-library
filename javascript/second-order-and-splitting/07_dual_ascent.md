# 07 dual ascent

**Language:** JavaScript · **Sphere:** javascript · **Category:** Second-Order & Splitting

**Signature:** `(X, y, lr, iters) → object`

## What it does

Dual ascent for linear regression.

## Guarantee

When it runs, 07 dual ascent guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node 07_dual_ascent.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `dualAscentRegression(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` is unused. `iters` controls the number of dual ascent iterations.
**Core:** Estimates the largest eigenvalue of `A*A^T` using 8 power iterations, then sets `alpha = 1 / lambdaMax`. Maintains dual variables `nu` (one per sample). Each iteration: computes primal `theta = A^T * nu`, then updates `nu -= alpha * (A*theta - y)`. The step size is computed from the spectral bound.
**Assert:** Expected: `[2, 3]`, bias `0.5` at 1e-9.
**⚠️ Defect:** The power iteration with only 8 steps may not have converged to the true `lambdaMax`, so the step size could be slightly off. The `lr` parameter is unused. Dual ascent converges for any convex problem with a strictly convex dual, which holds here. The spectral estimate is a partial precondition check.

---
*△ AURA Pattern Library — © Reality Optimizer*
