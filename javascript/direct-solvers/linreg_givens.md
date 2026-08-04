# linreg givens

**Language:** JavaScript · **Sphere:** javascript · **Category:** Direct Solvers

**Signature:** `(X, y, lr, iters) → object`

## What it does

Linear regression via Givens-rotation QR decomposition.

## Guarantee

When it runs, linreg givens guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node linreg_givens.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `givensQrRegression(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` and `iters` are unused.
**Core:** Applies Givens rotations to zero sub-diagonal entries of `A` column by column, simultaneously transforming `y`. Back-substitutes using the upper-triangular `R`.
**Assert:** Expected: `[2.0000000000000004, 2.9999999999999996]`, bias `0.4999999999999998` at 1e-9.
**⚠️ Defect:** No guard against zero diagonal in back-substitution: `s / R[i][i]` will produce Inf/NaN on a singular matrix. The Givens rotation itself handles zero entries correctly (the `if (r < 1e-14) continue;` guard skips rotations on zero elements), but the back-substitution is unguarded.

---
*△ AURA Pattern Library — © Reality Optimizer*
