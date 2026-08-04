# linreg levenberg marquardt

**Language:** JavaScript · **Sphere:** javascript · **Category:** Second-Order & Splitting

**Signature:** `(X, y, lr, iters) → object`

## What it does

Linear regression via Levenberg-Marquardt (damped Gauss-Newton).

## Guarantee

When it runs, linreg levenberg marquardt guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node linreg_levenberg_marquardt.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `levenbergMarquardtRegression(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` is unused. `iters` controls the number of LM iterations.
**Core:** Solves `(AtA + lambda*I) * delta = -g` at each step. The damping `lambda` is ADAPTIVE: starts at `0.01`, decreases by factor 0.1 on an accepted step, increases by factor 10 on a rejected step. This is the correct LM adaptation rule. The loss is evaluated before and after each step to decide acceptance.
**Assert:** Expected: `[1.9999996522361867, 2.9999996635283104]`, bias `0.5000000381945622` at 1e-9.
**⚠️ Defect:** The damping adaptation is correctly implemented — this is genuine Levenberg-Marquardt, not fixed-damped Gauss-Newton. However, the initial `lambda = 0.01` and the factors 0.1/10.0 are hardcoded. For this well-conditioned problem, the first step is always accepted and `lambda` drops to 1e-7 after a few iterations, making the method equivalent to Gauss-Newton. The `lr` parameter is unused.

---
*△ AURA Pattern Library — © Reality Optimizer*
