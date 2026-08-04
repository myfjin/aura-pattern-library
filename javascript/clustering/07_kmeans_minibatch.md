# 07 kmeans minibatch

**Language:** JavaScript · **Sphere:** javascript · **Category:** Clustering

**Signature:** `(X, y, lr, iters) → object`

## What it does

Mini-batch k-means.

## Guarantee

When it runs, 07 kmeans minibatch guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `NOT (!result || typeof result !== 'object')`
- `NOT (result.k !== 3)`
- `NOT (!Array.isArray(c) || c.length !== 2)`

## Verification evidence

- **Green-run:** ✓ passes (`node 07_kmeans_minibatch.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `kmeansMinibatch(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers. `y` and `lr` are unused. `iters` should be at least 10 (the mini-batch phase uses `max(1, floor(iters/2))` mini-batch passes, then up to `iters` full Lloyd iterations).
**Core:** Seeds with k-means++ using a local PRNG (seed `20240802`). Runs mini-batch passes on batches of size `max(1, floor(n/3))` with a deterministic Fisher-Yates shuffle. Each mini-batch point updates its nearest centroid with learning rate `1/counts[c]` (SGD-style). Finishes with full-dataset Lloyd iterations to reach a fixed point.
**Assert:** Same shape and value checks as #1, with centroids in k-means++ order (different from first-k order).
**⚠️ Defect:** The mini-batch phase uses `1/counts[c]` as the learning rate, which is the standard "count-based" decay for online k-means. But the counts are never reset between mini-batch passes, so later mini-batch updates have vanishingly small learning rates — a centroid that has seen 50 points in earlier mini-batches will barely move when a new point is assigned to it. This is a known trade-off (count-based decay stabilises but slows adaptation) but means the mini-batch phase contributes little after the first few passes. The final Lloyd pass is what actually produces the result.

**Shared with every pattern in its family:**

- **`y` and `lr` are silently ignored.** Every function takes `(X, y, lr, iters)` because that is the Forge Gate harness contract, but k-means has no use for a target vector or a learning rate. A caller who passes meaningful values gets no warning that they were discarded. The signature is honest about what the harness needs and dishonest about what the function consumes.
- **`k=3` is hardcoded.** Every pattern fixes the number of clusters at 3. This matches the harness test data (3 planted clusters, 20 points each) but means the pattern is not a general k-means implementation — it is a k-means-for-3-clusters implementation wearing a general name.
- **Iteration-capped convergence.** Every pattern uses `iters` as a hard iteration limit rather than a tolerance-based convergence check. The loop runs for up to `iters` passes and stops early only if no assignments change. This is correct for the harness (which supplies `iters=200` and the data converges in ~10–15 iterations) but means a caller who supplies too few iterations gets a non-converged result with no warning.

---
*△ AURA Pattern Library — © Reality Optimizer*
