# linreg backtracking

**Language:** JavaScript · **Sphere:** javascript · **Category:** Gradient & Adaptive Methods

**Signature:** `(X, y, lr, iters) → object`

## What it does

Gradient descent with backtracking line search (Armijo condition) for

## Guarantee

When it runs, linreg backtracking guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node linreg_backtracking.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `backtrackingLineSearchGd(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` is the initial step size for the line search. `iters` controls the number of iterations.
**Core:** At each iteration, computes the gradient and tries step sizes `lr, lr*rho, lr*rho², ...` (rho=0.5) until the Armijo condition `loss(new) <= loss(current) - c * step * ||grad||²` is satisfied. Falls back to a 1e-6 fixed step if no trial succeeds.
**Assert:** Expected: `[1.842168533693048, 2.8712117069626166]`, bias `0.5186281751329075` at 1e-9 — **identical to plain GD**.
**⚠️ Defect:** The expected weights are bit-for-bit identical to plain batch GD (batch1). This means the Armijo condition accepts the full `lr=0.05` step at every iteration — the backtracking never actually backtracks. The adaptive line search is completely unexercised. The fallback path (1e-6 step when no trial succeeds) is also never triggered. This is the same defect class as the statistics batch: a pattern named for an adaptive mechanism that is never tested against a case where it would matter.

---
*△ AURA Pattern Library — © Reality Optimizer*
