# linreg modified gram schmidt

**Language:** JavaScript · **Sphere:** javascript · **Category:** Direct Solvers

**Signature:** `(X, y, lr, iters) → object`

## What it does

Linear regression via Modified Gram-Schmidt QR decomposition.

## Guarantee

When it runs, linreg modified gram schmidt guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node linreg_modified_gram_schmidt.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `modifiedGramSchmidtRegression(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` and `iters` are unused.
**Core:** Same structure as classical Gram-Schmidt but orthogonalises each new column against all previously processed columns immediately. This is numerically more stable than classical Gram-Schmidt. Back-substitution checks `Math.abs(R[i][i]) > 1e-12 ? s / R[i][i] : 0.0`.
**Assert:** Expected: `[1.9999999999999998, 3]`, bias `0.49999999999999994` at 1e-9.
**⚠️ Defect:** The back-substitution guard is the same partial check as QR. The docstring correctly distinguishes this from classical Gram-Schmidt but does not explain why modified Gram-Schmidt is preferred.

---
*△ AURA Pattern Library — © Reality Optimizer*
