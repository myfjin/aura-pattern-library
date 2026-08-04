# 10 kmeans bisecting

**Language:** JavaScript · **Sphere:** javascript · **Category:** Clustering

**Signature:** `(X, y, lr, iters) → object`

## What it does

Bisecting k-means.

## Guarantee

When it runs, 10 kmeans bisecting guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `NOT (!result || typeof result !== 'object')`
- `NOT (result.k !== 3)`
- `NOT (!Array.isArray(c) || c.length !== 2)`

## Verification evidence

- **Green-run:** ✓ passes (`node 10_kmeans_bisecting.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `kmeansBisecting(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers. `y` and `lr` are unused. `iters` should be at least 10.
**Core:** Starts with one cluster containing all points. Repeatedly finds the cluster with the largest within-cluster sum of squares and splits it using 2-means (farthest-point seeding within the subset, then Lloyd-2). Stops when k=3 clusters exist. A final full-data Lloyd pass guarantees the fixed-point condition. If a 2-means split produces an empty child, falls back to splitting the parent's indices by halves.
**Assert:** Same shape and value checks as #1.
**⚠️ Defect:** The 2-means split uses farthest-point seeding within the subset, which is deterministic (no PRNG). But the farthest-point heuristic picks the two most distant points in the subset, which may both belong to the same true cluster if the subset is already well-separated. The degenerate-split guard (split-by-halves when one child is empty) is a blunt fix — it produces a split that is not centroid-based at all, just an index-range partition. The final Lloyd pass can recover from a bad split, but the bisecting hierarchy may have already committed to a suboptimal partition tree.

**Shared with every pattern in its family:**

- **`y` and `lr` are silently ignored.** Every function takes `(X, y, lr, iters)` because that is the Forge Gate harness contract, but k-means has no use for a target vector or a learning rate. A caller who passes meaningful values gets no warning that they were discarded. The signature is honest about what the harness needs and dishonest about what the function consumes.
- **`k=3` is hardcoded.** Every pattern fixes the number of clusters at 3. This matches the harness test data (3 planted clusters, 20 points each) but means the pattern is not a general k-means implementation — it is a k-means-for-3-clusters implementation wearing a general name.
- **Iteration-capped convergence.** Every pattern uses `iters` as a hard iteration limit rather than a tolerance-based convergence check. The loop runs for up to `iters` passes and stops early only if no assignments change. This is correct for the harness (which supplies `iters=200` and the data converges in ~10–15 iterations) but means a caller who supplies too few iterations gets a non-converged result with no warning.

---
*△ AURA Pattern Library — © Reality Optimizer*
