# streaming kmeans

**Language:** Python · **Sphere:** data-science · **Category:** Streaming & Sketches

## What it does

Streaming k-means (Online Clustering)

Core idea: Update cluster centroids incrementally as data streams in, without storing
all points. On slowly-drifting data, centroids track the evolution.

When to use: You have a streaming data source and need real-time clustering that adapts
to slowly-changing data distributions.

## Guarantee

When it runs, streaming kmeans guarantees avg_dist < 2.0 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `avg_dist < 2.0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `class StreamingKMeans:`, `def __init__(self, k: int = 3):`, `def initialize(self, first_points: List[List[float]]) -> None:`, `def nearest_centroid(self, point: List[float]) -> int:`, `def process(self, point: List[float]) -> None:`, `def get_centroids(self) -> List[List[float]:`
**Valid input:** `k` is a positive integer; `point` is a numeric vector of consistent dimension.
**Core:** Online k-means variant. Initializes centroids from the first `k` points, then incrementally updates the nearest centroid toward each new point using a learning rate `1/(count + 1)`.
**Assert:** After processing a seeded, slowly-drifting 3-cluster stream, the final centroids are on average within 2 units of the expected drifting centers.
**⚠️ Defect:** Initialization from the first `k` points is fragile — if those points are outliers or all from one cluster, the algorithm never recovers. There is no forgetting factor, so early data can dominate later drift. `nearest_centroid` is not exposed as a required top-level entry point in the signature reference but is part of the public class API.

---
*△ AURA Pattern Library — © Reality Optimizer*
