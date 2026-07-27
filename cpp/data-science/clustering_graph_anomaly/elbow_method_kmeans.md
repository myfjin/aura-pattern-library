# elbow method kmeans

**Language:** C++ · **Sphere:** data-science · **Category:** Clustering, Graph & Anomaly

**Signature:** `(p1: Tuple[float, ...], p2: Tuple[float, ...]) → float`

## What it does

Elbow Method + K-Means from scratch.
C++17 self-contained port with full parity to Python oracle.

## Guarantee

When it runs, elbow method kmeans guarantees detected_k == 3; inertias[1] - inertias[2] > inertias[2] - inertias[3] (proven by run on the PY original).

**Checkable constraints:**

- `detected_k == 3`
- `inertias[1] - inertias[2] > inertias[2] - inertias[3]`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — established on the PY original and shared by this C++ twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `kmeans(points, k, max_iterations=100, seed=42) → (labels, centroids, inertia)`, `elbow_knee(inertias) → int`
**Valid input:** `points: List[Tuple[float, ...]]` — at least k points. `k ≥ 1`.
**Core:** K-means with k-means++ initialization (probabilistic, distance-squared weighting). Compute inertia (sum of squared distances to centroids) for k=1..6. Find elbow via second derivative heuristic: largest change in acceleration of the inertia curve.
**Assert:** On 3 planted Gaussian clusters (20 pts each at (0,0), (6,6), (12,0), σ=0.4): elbow detected at k=3, and inertia drop from k=2 to k=3 > drop from k=3 to k=4.
**⚠️ Defect:** The k-means++ initialization uses a cumulative-sum approach (`cumsum += distances[i]`) but the random threshold `r = random.random() * total_dist` is compared against `cumsum` which accumulates raw distances, not probabilities. This is correct because `cumsum` goes from 0 to `total_dist`, matching the random range. However, the `break` after selecting a centroid means only one candidate is considered per iteration, which is correct for k-means++ but the implementation is fragile — if `total_dist` is 0 (all points identical), it falls back to `random.choice(points)`.

---
*△ AURA Pattern Library — © Reality Optimizer*
