# linreg minres

**Language:** JavaScript · **Sphere:** javascript · **Category:** Iterative Solvers

**Signature:** `(X, y, lr, iters) → object`

## What it does

Linear regression via MINRES (minimum residual) / conjugate residual on the

## Guarantee

When it runs, linreg minres guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node linreg_minres.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `minresRegression(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` is unused. `iters` caps the number of MINRES iterations (at most 2m steps). ⚠️ The matrix must be symmetric.
**Core:** Conjugate residual method on `AtA * theta = Aty`. Maintains residual `r` and search direction `p`. At each step: `alpha = rT*Ar / (Ap)T*(Ap); theta += alpha * p; r -= alpha * Ap; beta = rT*Ar_new / rT*Ar_old; p = r + beta * p`. Caps iterations at `min(iters, 2*m)`.
**Assert:** Expected: `[2, 3]`, bias `0.5000000000000003` at 1e-9.
**⚠️ Defect:** MINRES requires the matrix to be symmetric (not necessarily positive definite). `AtA` is symmetric, so the precondition holds. But there is no check. The conjugate residual method is mathematically equivalent to CG on SPD matrices but uses a different convergence criterion (minimises residual norm rather than A-norm of error).

---
*△ AURA Pattern Library — © Reality Optimizer*
