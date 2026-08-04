# linreg steepest descent exact

**Language:** JavaScript · **Sphere:** javascript · **Category:** Gradient & Adaptive Methods

**Signature:** `(X, y, lr, iters) → object`

## What it does

Linear regression via steepest descent with EXACT line search.

## Guarantee

When it runs, linreg steepest descent exact guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node linreg_steepest_descent_exact.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `steepestDescentExactRegression(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` is unused. `iters` controls the number of gradient steps.
**Core:** Precomputes `AtA` and `Aty`, then at each step computes the exact minimiser along the negative gradient: `alpha = gTg / (gT * AtA * g)`. This is the closed-form optimal step for a quadratic objective. The `lr` parameter is unused.
**Assert:** Expected: `[1.9999999999999523, 2.999999999999978]`, bias `0.5000000000000197` at 1e-9.
**⚠️ Defect:** The exact line search is correctly implemented. The expected weights are very close to the true values but not exact (unlike BB which hits them exactly). This is because steepest descent with exact line search on a quadratic converges geometrically but not in a finite number of steps.

---
*△ AURA Pattern Library — © Reality Optimizer*
