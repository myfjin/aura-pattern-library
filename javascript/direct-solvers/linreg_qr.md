# linreg qr

**Language:** JavaScript · **Sphere:** javascript · **Category:** Direct Solvers

**Signature:** `(X, y, lr, iters) → object`

## What it does

Linear regression via QR decomposition (Gram-Schmidt). lr and iters are

## Guarantee

When it runs, linreg qr guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node linreg_qr.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `qrRegression(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` and `iters` are unused.
**Core:** Decomposes `A = [1 | X]` into `Q` (n×m) and `R` (m×m) using classical Gram-Schmidt. Solves `R * theta = Q^T * y` via back-substitution. The back-substitution checks `Math.abs(R[i][i]) > 1e-12 ? s / R[i][i] : 0.0`.
**Assert:** Expected: `[1.9999999999999998, 3]`, bias `0.49999999999999994` at 1e-9.
**⚠️ Defect:** Classical Gram-Schmidt is numerically unstable — it loses orthogonality when columns are nearly dependent. Modified Gram-Schmidt (batch 4) is preferred. The back-substitution guard `Math.abs(R[i][i]) > 1e-12` is a partial singularity check, but returns 0 instead of reporting the problem. The docstring does not mention the instability of classical Gram-Schmidt.

---
*△ AURA Pattern Library — © Reality Optimizer*
