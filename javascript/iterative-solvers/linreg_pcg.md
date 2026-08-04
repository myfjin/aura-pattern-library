# linreg pcg

**Language:** JavaScript · **Sphere:** javascript · **Category:** Iterative Solvers

**Signature:** `(X, y, lr, iters) → object`

## What it does

Linear regression via preconditioned conjugate gradient on the normal

## Guarantee

When it runs, linreg pcg guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node linreg_pcg.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `preconditionedCgRegression(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` is unused. `iters` caps the number of PCG iterations (at most m steps). ⚠️ `AtA` must be symmetric positive definite.
**Core:** Same as CG but applies a Jacobi (diagonal) preconditioner: `M^{-1} = 1 / diag(AtA)`. The preconditioner is applied by scaling the residual: `z = M^{-1} * r`. The search direction is `p = z + beta * p_old`.
**Assert:** Expected: `[2.0000000000000004, 3]`, bias `0.4999999999999999` at 1e-9.
**⚠️ Defect:** The Jacobi preconditioner is computed (`Minv[i] = Math.abs(AtA[i][i]) > 1e-12 ? 1.0 / AtA[i][i] : 1.0`) and applied on every iteration. It provides no iteration-count benefit here: CG on a 3x3 SPD system converges in at most 3 steps regardless of preconditioning, so the speed-up the preconditioner exists to deliver cannot show on this fixture. PCG still requires `AtA` to be SPD, which is not checked — on a non-SPD system it would silently return garbage, same as CG. The diagonal guard prevents a divide-by-zero, not a non-SPD system.

---
*△ AURA Pattern Library — © Reality Optimizer*
