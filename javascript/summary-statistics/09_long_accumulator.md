# 09 long accumulator

**Language:** JavaScript · **Sphere:** javascript · **Category:** Summary Statistics

**Signature:** `(X, y, lr, iters) → object`

## What it does

Long-accumulator style exact summation (bucketed by exponent).

## Guarantee

When it runs, 09 long accumulator guarantees its self-test assertions hold on the harness fixture
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

- **Green-run:** ✓ passes (`node 09_long_accumulator.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `longAccumulator(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array where `X[i][0]` is the i-th data point. `y` is the target vector. `lr` and `iters` are unused.
**Core:** Splits each addend into bins indexed by exponent (`Math.floor(Math.log2(Math.abs(x)))`). After all values are binned, sums bins from smallest exponent to largest using Kahan compensation. The carry logic attempts to handle overflow: if adding a value to a bin changes its exponent, the overflow amount is carried to a higher bin.
**Assert:** Same shape and value checks as #1.
**⚠️ Defect:** The function is named `longAccumulator` and the file `09_long_accumulator.js`, but it implements exponent-bucketed float summation, not a wide fixed-point accumulator. A true long/Kulisch accumulator uses a fixed array of bins with exact representation (each bin holds a fixed-point value with enough bits to represent the full range). This implementation uses a `Map` and stores each bin as a single double — so a bin can still overflow. The name promises exactness the implementation does not provide. The carry logic `bins.set(exp, s - Math.sign(s) * Math.pow(2, newExp))` assumes the overflow amount is exactly a power of two, which is only true if the original value was at a power-of-two boundary. The compensation is unexercised — the harness data is well-conditioned.

**Shared with every pattern in its family:**

- **`lr` and `iters` are silently ignored.** Every function takes `(X, y, lr, iters)` because that is the Forge Gate harness contract. `X` is used (mapped to `xs` via `X.map(row => row[0])`), and `y` is used as the target vector. `lr` and `iters` are dead parameters.
- **All 10 use the same well-conditioned harness data as batch 3:** 30 points in [-1, 1], variance ~0.37 (xs) and ~2.0 (ys). A naive `xs.reduce((a,b) => a + b, 0)` would produce the same result to 1e-9 for every pattern. The compensation logic in every pattern is unexercised — none of these self-tests would fail if the body were replaced with a simple loop.

---
*△ AURA Pattern Library — © Reality Optimizer*
