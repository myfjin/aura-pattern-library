# kmeans lloyd

**Language:** R · **Sphere:** R · **Category:** Multivariate & Applied Modeling

## What it does

K-Means via Lloyd's Algorithm
Implements Lloyd's algorithm by hand; verifies within-cluster SS matches kmeans()
Use when: unsupervised clustering and need deterministic, repeatable results

## Guarantee

When it runs, kmeans lloyd guarantees all.equal(wss_manual, km$tot.withinss, tolerance = 1e-04) (proven by run).

**Checkable constraints:**

- `all.equal(wss_manual, km$tot.withinss, tolerance = 1e-04)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** No params; 3 Gaussian blobs (n=25 each, 2-D), k=3, 20 iterations fixed.
**Core:** Lloyd's k-means: random init from data points, assign each point to nearest center (Euclidean via `dist`), recompute centers as cluster means, iterate to convergence (`max|Δcenter|<1e-8`). Cross-checks total within-cluster SS against base `kmeans()` seeded with the same centers.
**Assert:** `all.equal(wss_manual, kmeans()$tot.withinss, tol=1e-4)`.
**⚠️ Defect:** Distances via `as.matrix(dist(rbind(X, centers)))` builds a full (n+k)² matrix each iteration then slices it — quadratic waste vs. a direct point-to-center loop. Empty-cluster case returns the old center (no re-seeding), which can stall convergence on degenerate data. Correctness depends on the well-separated planted blobs.

---
*△ AURA Pattern Library — © Reality Optimizer*
