# linreg cholesky

**Language:** JavaScript · **Sphere:** javascript · **Category:** Direct Solvers

**Signature:** `(X, y, lr, iters) → object`

## What it does

Linear regression via Cholesky decomposition of A^T A.

## Guarantee

When it runs, linreg cholesky guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node linreg_cholesky.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `choleskyRegression(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` and `iters` are unused. ⚠️ `AtA` must be symmetric positive definite — on a non-SPD matrix this returns a finite wrong answer, not NaN.
**Core:** Computes `L` such that `AtA = L * L^T`. The diagonal check is `L[i][j] = s > 0 ? Math.sqrt(s) : 1e-8` — if the pivot is not positive, it substitutes `1e-8` instead of `sqrt(s)`. Forward and backward substitution use `L[i][i] !== 0 ? s / L[i][i] : 0.0`.
**Assert:** Expected: `[2, 3]`, bias `0.49999999999999994` at 1e-9.
**⚠️ Defect:** The check `s > 0 ? Math.sqrt(s) : 1e-8` is a partial singularity guard — it prevents `NaN` from `sqrt` of a negative number, but silently substitutes a small positive value instead of reporting that the matrix is not SPD. On a genuinely non-SPD matrix, this produces a finite wrong answer without warning — which is a MORE DANGEROUS failure mode than the `NaN` that `normal_eq` and `lu` produce. `NaN` is loud and a caller sees it immediately; `[76.05, -71.05]` looks like a result and will propagate silently into whatever uses it. The substitution `1e-8` is arbitrary and tuned to this fixture.

---
*△ AURA Pattern Library — © Reality Optimizer*
