# linreg rls

**Language:** JavaScript · **Sphere:** javascript · **Category:** Second-Order & Splitting

**Signature:** `(X, y, lr, iters) → object`

## What it does

Linear regression via Recursive Least Squares (RLS).

## Guarantee

When it runs, linreg rls guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node linreg_rls.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `recursiveLeastSquares(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` and `iters` are unused (RLS runs exactly one pass).
**Core:** Processes samples online in fixed order. Maintains the inverse covariance matrix `P` (initialised to `1e3 * I`) and updates it with the Woodbury identity at each step. The `passes` variable is hardcoded to 1 — `iters` is accepted for signature compatibility but ignored. Symmetry of `P` is enforced after each update to prevent numerical drift.
**Assert:** Expected: `[2.002775511761308, 2.9990771325016308]`, bias `0.500566636753753` at 1e-9.
**⚠️ Defect:** The `passes = 1` hardcoding means the algorithm runs exactly one pass over the data regardless of `iters`. For a noise-free linear model this is sufficient, but for noisy data or ill-conditioned problems, multiple passes would be needed. The initial `P = 1e3 * I` is a tuning parameter — too large causes numerical drift (the docstring notes this), too small biases the solution toward zero. The expected weights are the least accurate in this batch (off by ~0.003), because one pass of RLS with `P0 = 1e3` does not fully converge.

---
*△ AURA Pattern Library — © Reality Optimizer*
