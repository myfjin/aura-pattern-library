# linreg kaczmarz

**Language:** JavaScript · **Sphere:** javascript · **Category:** Iterative Solvers

**Signature:** `(X, y, lr, iters) → object`

## What it does

Linear regression via cyclic Kaczmarz row-action projection.

## Guarantee

When it runs, linreg kaczmarz guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node linreg_kaczmarz.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `kaczmarzRegression(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` is unused. `iters` controls the number of row projections.
**Core:** Cycles through rows of `A = [1 | X]` in order. For each row: computes the prediction error, then projects `theta` onto the hyperplane `A[i] * theta = y[i]` by adding `(y[i] - pred) / ||A[i]||² * A[i]`. Uses the original data matrix `A`, not the normal equations.
**Assert:** Expected: `[2, 3]`, bias `0.5` at 1e-9 — exact true weights.
**⚠️ Defect:** Kaczmarz converges for any consistent linear system (no precondition needed), which is correct. But the cyclic order means convergence speed depends on row ordering — a pathological ordering can require exponentially many passes. The docstring correctly notes that the system is consistent (y is generated exactly from the true coefficients). No precondition check needed.

---
*△ AURA Pattern Library — © Reality Optimizer*
