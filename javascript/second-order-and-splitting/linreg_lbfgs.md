# linreg lbfgs

**Language:** JavaScript · **Sphere:** javascript · **Category:** Second-Order & Splitting

**Signature:** `(X, y, lr, iters) → object`

## What it does

Linear regression via L-BFGS (limited-memory BFGS).

## Guarantee

When it runs, linreg lbfgs guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node linreg_lbfgs.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `lbfgsRegression(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` is unused. `iters` controls the number of L-BFGS iterations.
**Core:** Same as BFGS but stores only the last 5 `(s, y)` pairs (`historyLimit = 5`). Uses the two-loop recursion to compute the search direction. The curvature condition is checked: `if (Math.abs(sy) > 1e-18)` before storing the pair.
**Assert:** Expected: `[2, 3]`, bias `0.5000000000000001` at 1e-9.
**⚠️ Defect:** Same curvature-condition issue as BFGS: the check `Math.abs(sy) > 1e-18` allows negative `s·y` through. The `historyLimit = 5` is hardcoded — for m=3 this is more than enough, but for high-dimensional problems the history size should be a parameter. The `lr` parameter is unused.

---
*△ AURA Pattern Library — © Reality Optimizer*
