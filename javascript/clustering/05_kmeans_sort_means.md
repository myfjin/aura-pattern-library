# 05 kmeans sort means

**Language:** JavaScript · **Sphere:** javascript · **Category:** Clustering

**Signature:** `(X, y, lr, iters) → object`

## What it does

Sort-means k-means.

## Guarantee

When it runs, 05 kmeans sort means guarantees its self-test assertions hold on the harness fixture
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

- **Green-run:** ✓ passes (`node 05_kmeans_sort_means.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `kmeansSortMeans(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers. `y` and `lr` are unused. `iters` should be at least 10.
**Core:** Computes a projection direction each iteration (the vector from centroid 0 to centroid 1, normalised). Projects all centroids onto this direction and sorts by the projection. For each point, scans centroids in sorted order. The prune condition `if (gap * gap >= bestD) break;` uses the sort-means rule: once the projected gap exceeds the best distance, no further centroid can be closer.
**Assert:** Same shape and value checks as #1.
**⚠️ Defect:** The projection direction `centroids[1] - centroids[0]` changes every iteration as centroids move. This means the sort order changes every iteration, which is correct — but it also means the direction can collapse to zero if centroids 0 and 1 converge to the same point. The code handles this with `if (dirNorm > 0) { ... } else { direction[0] = 1; }`, falling back to the first axis. This is a reasonable fallback but means the prune is disabled (no meaningful direction) when two centroids coincide.

**Shared with every pattern in its family:**

- **`y` and `lr` are silently ignored.** Every function takes `(X, y, lr, iters)` because that is the Forge Gate harness contract, but k-means has no use for a target vector or a learning rate. A caller who passes meaningful values gets no warning that they were discarded.
- **`k=3` is hardcoded.** Every pattern fixes the number of clusters at 3. This matches the harness test data but means the pattern is not a general k-means implementation.
- **Iteration-capped convergence.** Every pattern uses `iters` as a hard iteration limit rather than a tolerance-based convergence check. The loop runs for up to `iters` passes and stops early only if no assignments change.
- **Empty-cluster fallback preserves old centroid.** Every pattern that recomputes centroids uses the pattern `if (counts[c] > 0) { ... }` without re-initialising empty clusters — the old centroid stays in place, and an empty cluster stays empty forever.

---
*△ AURA Pattern Library — © Reality Optimizer*
