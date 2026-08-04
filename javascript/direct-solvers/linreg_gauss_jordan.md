# linreg gauss jordan

**Language:** JavaScript · **Sphere:** javascript · **Category:** Direct Solvers

**Signature:** `(X, y, lr, iters) → object`

## What it does

Linear regression via Gauss-Jordan elimination to invert X^T X explicitly.

## Guarantee

When it runs, linreg gauss jordan guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node linreg_gauss_jordan.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `gaussJordanRegression(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` and `iters` are unused. ⚠️ `AtA` must be invertible — on a singular matrix the inverse is silently wrong.
**Core:** Forms `AtA`, augments with the identity matrix `[AtA | I]`, and reduces to `[I | inv(AtA)]` using Gauss-Jordan elimination with partial pivoting. Then computes `theta = inv(AtA) * Aty`.
**Assert:** Expected: `[2, 2.9999999999999996]`, bias `0.5000000000000001` at 1e-9.
**⚠️ Defect:** The pivot check `if (Math.abs(piv) < 1e-12) { continue; }` skips zero pivots but does not abort — the inverse will be wrong. This is the most expensive solver in the batch (explicitly inverts a 3×3 matrix) and the least numerically robust.

---
*△ AURA Pattern Library — © Reality Optimizer*
