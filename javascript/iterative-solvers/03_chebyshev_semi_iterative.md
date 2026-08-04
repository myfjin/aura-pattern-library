# 03 chebyshev semi iterative

**Language:** JavaScript · **Sphere:** javascript · **Category:** Iterative Solvers

**Signature:** `(X, y, lr, iters) → object`

## What it does

Chebyshev semi-iterative method for linear regression.

## Guarantee

When it runs, 03 chebyshev semi iterative guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node 03_chebyshev_semi_iterative.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `chebyshevSemiIterativeRegression(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` is unused. `iters` controls the number of Chebyshev iterations.
**Core:** Computes the exact eigenvalues of the 3x3 `AtA` by solving the characteristic polynomial `λ³ - trace λ² + S λ - det = 0` via the depressed cubic formula. Falls back to power iteration if the discriminant is negative. Uses the eigenvalue bounds to set the optimal Chebyshev acceleration parameters. This is the most sophisticated solver in the batch.
**Assert:** Expected: `[2.0000000000000004, 3.0000000000000004]`, bias `0.49999999999999994` at 1e-9.
**⚠️ Defect:** The eigenvalue computation is exact for the 3x3 case (the characteristic polynomial is solved analytically). This is the only solver in the batch that genuinely checks its precondition — it computes the spectrum of `AtA` and uses it to tune the acceleration. However, the fallback to power iteration (when the discriminant is negative) may produce inaccurate bounds. The Gershgorin bound is also computed as a safety check. This is the most thorough precondition handling in the batch.

---
*△ AURA Pattern Library — © Reality Optimizer*
