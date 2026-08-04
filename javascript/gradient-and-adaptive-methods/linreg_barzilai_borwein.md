# linreg barzilai borwein

**Language:** JavaScript · **Sphere:** javascript · **Category:** Gradient & Adaptive Methods

**Signature:** `(X, y, lr, iters) → object`

## What it does

Linear regression via the Barzilai-Borwein (BB) gradient method.

## Guarantee

When it runs, linreg barzilai borwein guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node linreg_barzilai_borwein.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `barzilaiBorweinRegression(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` is unused. `iters` controls the number of BB steps.
**Core:** Precomputes `AtA` and `Aty` (the normal equations), then uses the BB step size `alpha = sTs / sTy` where `s = theta_k - theta_{k-1}` and `y = grad_k - grad_{k-1}`. Clamped to [1e-6, 1.0]. Starts with a fixed 0.05 step for the first iteration.
**Assert:** Expected: `[2, 3]`, bias `0.5` at 1e-9 — **exact true weights**.
**⚠️ Defect:** Converges to the true weights to machine precision in roughly 25 iterations, where plain GD is still at 1.6e-1 error after 200. The docstring's finite-step claim does NOT hold for this implementation: the BB step is clamped to `alpha = Math.max(1e-6, Math.min(alpha, 1.0))`, and clamping destroys the finite-termination property that BB has on a quadratic in exact arithmetic. The exactness at iteration 200 is gradual convergence to float64 precision, not finite termination. The `lr` parameter is unused.

---
*△ AURA Pattern Library — © Reality Optimizer*
