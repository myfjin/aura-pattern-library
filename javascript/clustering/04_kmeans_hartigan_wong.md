# 04 kmeans hartigan wong

**Language:** JavaScript · **Sphere:** javascript · **Category:** Clustering

**Signature:** `(X, y, lr, iters) → object`

## What it does

Hartigan-Wong k-means.

## Guarantee

When it runs, 04 kmeans hartigan wong guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `NOT (!result || typeof result !== 'object')`
- `NOT (result.k !== 3)`
- `NOT (!Array.isArray(c) || c.length !== 2)`

## Verification evidence

- **Green-run:** ✓ passes (`node 04_kmeans_hartigan_wong.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `kmeansHartiganWong(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers. `y` and `lr` are unused. `iters` should be at least 10.
**Core:** Initialises with first-k points, then iteratively evaluates every point for a move to another cluster. A move is accepted only if it strictly reduces the total within-cluster sum of squares, accounting for the centroid shifts caused by the move. The gain formula is `left - (counts[s] / (counts[s] + 1)) * ds`. A final Lloyd pass guarantees the fixed-point condition.
**Assert:** Same shape and value checks as #1.
**⚠️ Defect:** The guard `if (counts[r] <= 1) continue;` prevents emptying a cluster, which is correct — but it also means a point that is the sole member of its cluster can never be moved, even if moving it would lower the total SSE. This is a known limitation of Hartigan-Wong and is handled correctly here (the guard is the standard approach), but it means the algorithm can get stuck in a local optimum that a different algorithm would escape. Additionally, `recomputeCentroids()` falls back to `centroids[c].slice()` when `counts[c] === 0` — the same never-recovers-from-empty defect as kmeans_lloyd: an empty cluster keeps its old centroid rather than being re-initialised.

**Shared with every pattern in its family:**

- **`y` and `lr` are silently ignored.** Every function takes `(X, y, lr, iters)` because that is the Forge Gate harness contract, but k-means has no use for a target vector or a learning rate. A caller who passes meaningful values gets no warning that they were discarded. The signature is honest about what the harness needs and dishonest about what the function consumes.
- **`k=3` is hardcoded.** Every pattern fixes the number of clusters at 3. This matches the harness test data (3 planted clusters, 20 points each) but means the pattern is not a general k-means implementation — it is a k-means-for-3-clusters implementation wearing a general name.
- **Iteration-capped convergence.** Every pattern uses `iters` as a hard iteration limit rather than a tolerance-based convergence check. The loop runs for up to `iters` passes and stops early only if no assignments change. This is correct for the harness (which supplies `iters=200` and the data converges in ~10–15 iterations) but means a caller who supplies too few iterations gets a non-converged result with no warning.

---
*△ AURA Pattern Library — © Reality Optimizer*
