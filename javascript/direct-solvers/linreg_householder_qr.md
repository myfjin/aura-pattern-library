# linreg householder qr

**Language:** JavaScript · **Sphere:** javascript · **Category:** Direct Solvers

**Signature:** `(X, y, lr, iters) → object`

## What it does

Linear regression via Householder QR reflection.

## Guarantee

When it runs, linreg householder qr guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node linreg_householder_qr.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `householderQrRegression(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` and `iters` are unused.
**Core:** Applies Householder reflections to reduce `A` to upper triangular form while transforming `y`. Back-substitutes using the upper-triangular `R`. This is the most numerically stable QR implementation in the batch.
**Assert:** Expected: `[2.000000000000003, 2.9999999999999996]`, bias `0.5000000000000008` at 1e-9.
**⚠️ Defect:** The back-substitution checks `Math.abs(A[i][i]) > 1e-12 ? s / A[i][i] : 0.0` — same partial guard as the other QR methods. The Householder reflection itself handles near-zero norms correctly (`if (norm < 1e-14) { continue; }`).

---
*△ AURA Pattern Library — © Reality Optimizer*
