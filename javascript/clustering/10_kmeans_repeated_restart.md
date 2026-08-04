# 10 kmeans repeated restart

**Language:** JavaScript · **Sphere:** javascript · **Category:** Clustering

**Signature:** `(X, y, lr, iters) → object`

## What it does

Repeated-restart k-means.

## Guarantee

When it runs, 10 kmeans repeated restart guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `result.k === 3`
- `Array.isArray(result.centroids) && result.centroids.length === 3`
- `Array.isArray(c) && c.length === 2`
- `Array.isArray(result.assignments) && result.assignments.length === 60`
- `approxEqual(result.centroids, expectedCentroids, 1e-9)`
- `approxEqual(result.assignments, expectedAssignments, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node 10_kmeans_repeated_restart.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `kmeansRepeatedRestart(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers. `y` and `lr` are unused. `iters` should be at least 10.
**Core:** Runs 6 independent Lloyd restarts with k-means++ seeding. Each restart uses a different PRNG seed (`20240807 + r * 12345`). Keeps the result with the lowest within-cluster sum of squares. Each restart re-initialises the PRNG state, so the sequence of random choices is different for each restart.
**Assert:** Same shape and value checks as #1, with centroids in k-means++ order.
**⚠️ Defect:** The number of restarts is hardcoded at 6. This is enough for the harness data (3 well-separated clusters, 20 points each) where k-means++ almost always finds the global optimum in one try. On harder data (overlapping clusters, high dimensions), 6 restarts may not be enough to escape local optima. The PRNG state reset `rngState = (20240807 + seedOffset * 12345) >>> 0` is deterministic — every run produces the same 6 restarts in the same order, so the "repeated" restarts are actually fixed.

**Shared with every pattern in its family:**

- **`y` and `lr` are silently ignored.** Every function takes `(X, y, lr, iters)` because that is the Forge Gate harness contract, but k-means has no use for a target vector or a learning rate. A caller who passes meaningful values gets no warning that they were discarded.
- **`k=3` is hardcoded.** Every pattern fixes the number of clusters at 3. This matches the harness test data but means the pattern is not a general k-means implementation.
- **Iteration-capped convergence.** Every pattern uses `iters` as a hard iteration limit rather than a tolerance-based convergence check. The loop runs for up to `iters` passes and stops early only if no assignments change.
- **Empty-cluster fallback preserves old centroid.** Every pattern that recomputes centroids uses the pattern `if (counts[c] > 0) { ... }` without re-initialising empty clusters — the old centroid stays in place, and an empty cluster stays empty forever.

---
*△ AURA Pattern Library — © Reality Optimizer*
