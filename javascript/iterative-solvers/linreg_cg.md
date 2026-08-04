# linreg cg

**Language:** JavaScript · **Sphere:** javascript · **Category:** Iterative Solvers

**Signature:** `(X, y, lr, iters) → object`

## What it does

Conjugate gradient on the normal equations for linear regression.

## Guarantee

When it runs, linreg cg guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node linreg_cg.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `conjugateGradientRegression(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` is unused. `iters` caps the number of CG iterations (at most m steps). ⚠️ `AtA` must be symmetric positive definite.
**Core:** Standard CG for `AtA * theta = Aty`. Maintains residual `r` and search direction `p`. At each step: `alpha = rTr / (pT * AtA * p); theta += alpha * p; r -= alpha * AtA * p; beta = rTr_new / rTr_old; p = r + beta * p`. Caps iterations at `min(iters, m)` (at most 3 steps for m=3). Has early-exit on residual norm < 1e-12.
**Assert:** Expected: `[2, 3]`, bias `0.49999999999999983` at 1e-9.
**⚠️ Defect:** CG requires `AtA` to be symmetric positive definite. The harness fixture's `AtA` is SPD (Gram matrix of full-rank data), so it converges in at most m=3 iterations. On a non-SPD system (rank-deficient data, or a non-Gram matrix), CG would silently return garbage — the residual norm may decrease while the solution is wrong. There is no SPD check. The early-exit on residual norm is correct but the max-iter cap of `min(iters, m)` means CG never runs more than 3 steps regardless of `iters`.

---
*△ AURA Pattern Library — © Reality Optimizer*
