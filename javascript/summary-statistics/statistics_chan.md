# statistics chan

**Language:** JavaScript · **Sphere:** javascript · **Category:** Summary Statistics

**Signature:** `(X, y, lr, iters) → object`

## What it does

Chan's parallel merge formula for one-pass mean and population variance.

## Guarantee

When it runs, statistics chan guarantees its self-test assertions hold on the harness fixture
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

- **Green-run:** ✓ passes (`node statistics_chan.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `chanVariance(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array where `X[i][0]` is the i-th data point. `y` is the target vector. `lr` and `iters` are unused.
**Core:** Recursively splits the data in half, computes `{n, mean, M2}` for each half, then merges pairs using Chan's formula: `delta = b.mean - a.mean; M2 = a.M2 + b.M2 + delta² * a.n * b.n / (a.n + b.n)`. This is the foundation for map-reduce and distributed variance computation.
**Assert:** Asserts `statsX` and `statsY` each have finite `mean` and `variance`, plus finite `correlation` and `covariance`. Compares all four against expected values at 1e-9 relative tolerance.
**⚠️ Defect:** The merge formula `delta * delta * a.n * b.n / n` can overflow for large `n` because `a.n * b.n` grows as O(n²). For the harness data (n=30) this is fine, but for data sets with millions of points the product would exceed `Number.MAX_SAFE_INTEGER` (2⁵³). The compensation is also unexercised — the harness data is well-conditioned, so the merge path produces the same result as a naive computation.

**Shared with every pattern in its family:**

- **`lr` and `iters` are silently ignored.** Every function takes `(X, y, lr, iters)` because that is the Forge Gate harness contract, but variance computation has no use for a learning rate or iteration count. `X` is used (mapped to `xs` via `X.map(row => row[0])`), and `y` is used as the target vector for the Y statistics. `lr` and `iters` are dead parameters.
- **The self-test does not exercise the instability any of these patterns exist to fix.** All 10 use the same harness data: 30 points in [-1, 1] with variance ~0.37 (xs) and ~2.0 (ys). These are small, well-conditioned values where even the naive `sumSq/n - mean²` formula produces the correct answer to 1e-9. A Kahan summation verified on this data proves nothing about Kahan summation — the compensation path is never tested against a case where it would matter. The self-test passes for reasons unrelated to each pattern's purpose.
- **`k=3` is not relevant here** (these are statistics, not clustering), but the harness contract still forces the `(X, y, lr, iters)` signature.

---
*△ AURA Pattern Library — © Reality Optimizer*
