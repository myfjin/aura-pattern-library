# linreg lsqr

**Language:** JavaScript · **Sphere:** javascript · **Category:** Iterative Solvers

**Signature:** `(X, y, lr, iters) → object`

## What it does

Linear regression via LSQR, the iterative least-squares solver based on

## Guarantee

When it runs, linreg lsqr guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node linreg_lsqr.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `lsqrRegression(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` is unused. `iters` caps the number of LSQR iterations (at most 4m steps).
**Core:** Implements the full LSQR algorithm: initialises `u = y / ||y||`, `v = A^T * u`, then iterates bidiagonalisation steps with Givens rotations to update the solution. Caps iterations at `min(iters, 4*m)` (at most 12 steps for m=3). Does not form `AtA` explicitly — works with `A` and `A^T` directly.
**Assert:** Expected: `[1.9999999999999998, 3]`, bias `0.4999999999999998` at 1e-9.
**⚠️ Defect:** LSQR works on any matrix (no SPD requirement) and minimises `||A*theta - y||` directly. This is the most numerically robust solver in the batch. The iteration cap of `4*m` is conservative — for m=3, LSQR converges in at most 3 steps on this data. The implementation is correct.

---
*△ AURA Pattern Library — © Reality Optimizer*
