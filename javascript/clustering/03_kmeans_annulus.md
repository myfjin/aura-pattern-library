# 03 kmeans annulus

**Language:** JavaScript · **Sphere:** javascript · **Category:** Clustering

**Signature:** `(X, y, lr, iters) → object`

## What it does

Annulus k-means.

## Guarantee

When it runs, 03 kmeans annulus guarantees its self-test assertions hold on the harness fixture
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

- **Green-run:** ✓ passes (`node 03_kmeans_annulus.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `kmeansAnnulus(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers. `y` and `lr` are unused. `iters` should be at least 10.
**Core:** Sorts centroids by their Euclidean norm each iteration. For each point, computes the point's norm and scans centroids in sorted order. The prune condition `if (Math.abs(xNorm - sorted[p].n) >= Math.sqrt(bestD)) break;` uses the annulus rule: by the triangle inequality, `||x - c|| >= | ||x|| - ||c|| |`, so if the norm gap already exceeds the best distance found, no further centroid can be closer.
**Assert:** Same shape and value checks as #1.
**⚠️ Defect:** The annulus prune only scans in one direction (forward from the first centroid in sorted order). For k=3 this is fine — the nearest centroid is always found within 1–2 comparisons. But the prune does not check both directions from the current best centroid, so on data with more centroids it would miss the true nearest if it lies on the opposite side of the sorted order. The prune is also computed against `Math.sqrt(bestD)` (Euclidean distance) while the comparison is against `Math.abs(xNorm - sorted[p].n)` (also Euclidean), which is consistent — but the initial `bestD` is a squared distance, so the first prune check uses `Math.sqrt(dist2(x, centroids[0]))` which is correct.

**Shared with every pattern in its family:**

- **`y` and `lr` are silently ignored.** Every function takes `(X, y, lr, iters)` because that is the Forge Gate harness contract, but k-means has no use for a target vector or a learning rate. A caller who passes meaningful values gets no warning that they were discarded.
- **`k=3` is hardcoded.** Every pattern fixes the number of clusters at 3. This matches the harness test data but means the pattern is not a general k-means implementation.
- **Iteration-capped convergence.** Every pattern uses `iters` as a hard iteration limit rather than a tolerance-based convergence check. The loop runs for up to `iters` passes and stops early only if no assignments change.
- **Empty-cluster fallback preserves old centroid.** Every pattern that recomputes centroids uses the pattern `if (counts[c] > 0) { ... }` without re-initialising empty clusters — the old centroid stays in place, and an empty cluster stays empty forever.

---
*△ AURA Pattern Library — © Reality Optimizer*
