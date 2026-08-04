# linreg jacobi

**Language:** JavaScript · **Sphere:** javascript · **Category:** Iterative Solvers

**Signature:** `(X, y, lr, iters) → object`

## What it does

Jacobi iteration on the normal equations for linear regression.

## Guarantee

When it runs, linreg jacobi guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node linreg_jacobi.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `jacobiRegression(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` is unused. `iters` controls the number of Jacobi passes. ⚠️ `AtA` must be diagonally dominant — centre your features before using this, or use Gauss-Seidel.
**Core:** Precomputes `AtA` and `Aty`. Each pass computes all new coordinates from the previous iterate: `thetaNew[i] = (Aty[i] - Σ_{j≠i} AtA[i][j] * theta[j]) / AtA[i][i]`. All coordinates are updated simultaneously (the new values are stored in a separate array).
**Assert:** Expected: `[2, 3]`, bias `0.5` at 1e-9 — exact true weights.
**⚠️ Defect:** Jacobi converges only when `AtA` is diagonally dominant. The harness fixture is centred on [-1,1], which happens to produce a dominant `AtA`; the pattern converges to `[2, 3]` there. On uncentred features — the ordinary case — it diverges: measured at ~1e51 to 1e57 on four separate inputs including a well-conditioned one, returning finite garbage with no error and no warning. There is no dominance check. Centre your features before using this, or use Gauss-Seidel, which converged on all four of the same inputs. The convergence is iteration-capped with no tolerance-based early exit.

---
*△ AURA Pattern Library — © Reality Optimizer*
