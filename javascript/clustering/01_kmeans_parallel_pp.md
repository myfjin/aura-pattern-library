# 01 kmeans parallel pp

**Language:** JavaScript · **Sphere:** javascript · **Category:** Clustering

**Signature:** `(X, y, lr, iters) → object`

## What it does

k-means|| (scalable k-means++).

## Guarantee

When it runs, 01 kmeans parallel pp guarantees its self-test assertions hold on the harness fixture
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

- **Green-run:** ✓ passes (`node 01_kmeans_parallel_pp.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `kmeansParallelPp(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers. `y` and `lr` are unused. `iters` should be at least 10.
**Core:** Picks one initial point, then oversamples candidates over 5 rounds: each point is selected with probability proportional to its squared distance from the nearest existing candidate. If more than k×4 candidates survive, thins them by farthest-point subsampling. Re-clusters the weighted candidates with Lloyd, then runs a final full-data Lloyd pass.
**Assert:** Asserts `k === 3`, 3 centroids each of length 2, 60 assignments. Compares centroids and assignments against expected values at 1e-9 relative tolerance.
**⚠️ Defect:** The re-clustering phase computes candidate weights by calling `nearest(X[j], candidates) === i` for every point and every candidate — this is O(n × candidates) per Lloyd iteration, which defeats the purpose of oversampling. For the harness data (n=60, candidates ~12) this is negligible, but on large data the overhead would exceed the benefit of the k-means|| seeding.

**Shared with every pattern in its family:**

- **`y` and `lr` are silently ignored.** Every function takes `(X, y, lr, iters)` because that is the Forge Gate harness contract, but k-means has no use for a target vector or a learning rate. A caller who passes meaningful values gets no warning that they were discarded.
- **`k=3` is hardcoded.** Every pattern fixes the number of clusters at 3. This matches the harness test data but means the pattern is not a general k-means implementation.
- **Iteration-capped convergence.** Every pattern uses `iters` as a hard iteration limit rather than a tolerance-based convergence check. The loop runs for up to `iters` passes and stops early only if no assignments change.
- **Empty-cluster fallback preserves old centroid.** Every pattern that recomputes centroids uses the pattern `if (counts[c] > 0) { ... }` without re-initialising empty clusters — the old centroid stays in place, and an empty cluster stays empty forever.

---
*△ AURA Pattern Library — © Reality Optimizer*
