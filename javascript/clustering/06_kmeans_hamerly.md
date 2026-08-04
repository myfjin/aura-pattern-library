# 06 kmeans hamerly

**Language:** JavaScript · **Sphere:** javascript · **Category:** Clustering

**Signature:** `(X, y, lr, iters) → object`

## What it does

Hamerly's bound-accelerated k-means.

## Guarantee

When it runs, 06 kmeans hamerly guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `NOT (!result || typeof result !== 'object')`
- `NOT (result.k !== 3)`
- `NOT (!Array.isArray(c) || c.length !== 2)`

## Verification evidence

- **Green-run:** ✓ passes (`node 06_kmeans_hamerly.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `kmeansHamerly(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers. `y` and `lr` are unused. `iters` should be at least 10.
**Core:** Simpler than Elkan: each point keeps one upper bound (to its assigned centroid) and one lower bound (to the nearest *other* centroid). A single `maxMove` value (the furthest any centroid moved) is used to update all lower bounds, which is a coarser but cheaper approximation than Elkan's per-centroid move tracking.
**Assert:** Same shape and value checks as #1.
**⚠️ Defect:** The lower bound update `lower[i] = Math.max(0, lower[i] - maxMove)` is a conservative approximation — it assumes every centroid moved as far as the furthest-moving one. This is correct (the bound remains valid) but means Hamerly prunes less aggressively than Elkan on data where centroid movements vary widely. The empty-cluster fallback preserves the old centroid, same as #1.

**Shared with every pattern in its family:**

- **`y` and `lr` are silently ignored.** Every function takes `(X, y, lr, iters)` because that is the Forge Gate harness contract, but k-means has no use for a target vector or a learning rate. A caller who passes meaningful values gets no warning that they were discarded. The signature is honest about what the harness needs and dishonest about what the function consumes.
- **`k=3` is hardcoded.** Every pattern fixes the number of clusters at 3. This matches the harness test data (3 planted clusters, 20 points each) but means the pattern is not a general k-means implementation — it is a k-means-for-3-clusters implementation wearing a general name.
- **Iteration-capped convergence.** Every pattern uses `iters` as a hard iteration limit rather than a tolerance-based convergence check. The loop runs for up to `iters` passes and stops early only if no assignments change. This is correct for the harness (which supplies `iters=200` and the data converges in ~10–15 iterations) but means a caller who supplies too few iterations gets a non-converged result with no warning.

---
*△ AURA Pattern Library — © Reality Optimizer*
