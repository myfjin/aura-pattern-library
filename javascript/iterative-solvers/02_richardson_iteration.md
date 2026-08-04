# 02 richardson iteration

**Language:** JavaScript · **Sphere:** javascript · **Category:** Iterative Solvers

**Signature:** `(X, y, lr, iters) → object`

## What it does

Richardson iteration for linear regression.

## Guarantee

When it runs, 02 richardson iteration guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node 02_richardson_iteration.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `richardsonIterationRegression(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` is unused. `iters` controls the number of Richardson iterations. ⚠️ `AtA` must be SPD.
**Core:** Estimates the largest eigenvalue of `AtA` using 10 power iterations, then sets `omega = 1 / lambdaMax`. Each step: `theta += omega * (Aty - AtA * theta)`. This is the optimal stationary method for SPD matrices.
**Assert:** Expected: `[1.9999999999999996, 2.9999999999999996]`, bias `0.5` at 1e-9.
**⚠️ Defect:** The power iteration estimate of `lambdaMax` is a partial precondition check — it computes the spectral radius and uses it to set the step size. But the method still assumes `AtA` is SPD (Richardson diverges on non-SPD systems, same failure mode as Jacobi). The power iteration with only 10 steps may not have converged to the true `lambdaMax`, so the step size could be slightly off. The `lr` parameter is unused.

---
*△ AURA Pattern Library — © Reality Optimizer*
