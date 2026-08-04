# 07 fixed point

**Language:** JavaScript · **Sphere:** javascript · **Category:** Summary Statistics

**Signature:** `(X, y, lr, iters) → object`

## What it does

Scaled fixed-point / integer accumulation statistics.

## Guarantee

When it runs, 07 fixed point guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `result.statsX && typeof result.statsX === 'object' && isFinite(result.statsX.mean) && isFinite(result.statsX.variance)`
- `result.statsY && typeof result.statsY === 'object' && isFinite(result.statsY.mean) && isFinite(result.statsY.variance)`
- `typeof result.correlation === 'number' && isFinite(result.correlation)`
- `typeof result.covariance === 'number' && isFinite(result.covariance)`
- `approxEqual(result.statsX, expectedStatsX, 1e-9)`
- `approxEqual(result.statsY, expectedStatsY, 1e-9)`
- `approxEqual(result.correlation, expectedCorrelation, 1e-9)`
- `approxEqual(result.covariance, expectedCovariance, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node 07_fixed_point.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `fixedPointSum(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array where `X[i][0]` is the i-th data point. `y` is the target vector. `lr` and `iters` are unused.
**Core:** Computes a scale factor from the data range: `scale = Math.pow(2, 52) / Math.max(Math.abs(min), Math.abs(max))`, clamped to 1e15. Shifts each value by an offset, scales it, rounds to integer, and accumulates in integer arithmetic. The result is divided back by the scale. This converts floating-point summation into integer-like accumulation, avoiding round-off in the sum.
**Assert:** Same shape and value checks as #1.
**⚠️ Defect:** The scale computation has a dead branch: `span ? (Math.pow(2, 52) / ...) : 1` — the `: 1` is never reached because `span` is always truthy when `span !== 0`, and `span === 0` is handled by the earlier `span === 0 ? 1 :` check. The variance formula `fixedSumSq` is complex and error-prone: it expands `Σ(d - offset)²` into three terms that can themselves cancel. The compensation is unexercised — the harness data is well-conditioned.

**Shared with every pattern in its family:**

- **`lr` and `iters` are silently ignored.** Every function takes `(X, y, lr, iters)` because that is the Forge Gate harness contract. `X` is used (mapped to `xs` via `X.map(row => row[0])`), and `y` is used as the target vector. `lr` and `iters` are dead parameters.
- **All 10 use the same well-conditioned harness data as batch 3:** 30 points in [-1, 1], variance ~0.37 (xs) and ~2.0 (ys). A naive `xs.reduce((a,b) => a + b, 0)` would produce the same result to 1e-9 for every pattern. The compensation logic in every pattern is unexercised — none of these self-tests would fail if the body were replaced with a simple loop.

---
*△ AURA Pattern Library — © Reality Optimizer*
