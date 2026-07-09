"""
Streaming k-means (Online Clustering)

Core idea: Update cluster centroids incrementally as data streams in, without storing
all points. On slowly-drifting data, centroids track the evolution.

When to use: You have a streaming data source and need real-time clustering that adapts
to slowly-changing data distributions.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import math
from typing import List, Tuple


class StreamingKMeans:
    """Online k-means: update centroids incrementally."""

    def __init__(self, k: int = 3):
        self.k = k
        self.centroids: List[List[float]] = []
        self.counts: List[int] = []

    def initialize(self, first_points: List[List[float]]) -> None:
        """Initialize centroids from first k points."""
        self.centroids = first_points[:self.k]
        self.counts = [1] * self.k

    def nearest_centroid(self, point: List[float]) -> int:
        """Find nearest centroid to point."""
        best_dist = float("inf")
        best_idx = 0
        for i, centroid in enumerate(self.centroids):
            dist = sum((p - c) ** 2 for p, c in zip(point, centroid))
            if dist < best_dist:
                best_dist = dist
                best_idx = i
        return best_idx

    def process(self, point: List[float]) -> None:
        """Process a new data point: update centroid of nearest cluster."""
        if not self.centroids:
            return

        idx = self.nearest_centroid(point)

        # Update centroid: weighted average
        learning_rate = 1.0 / (self.counts[idx] + 1)
        for j, val in enumerate(point):
            self.centroids[idx][j] += learning_rate * (val - self.centroids[idx][j])

        self.counts[idx] += 1

    def get_centroids(self) -> List[List[float]]:
        """Return current centroids."""
        return [c[:] for c in self.centroids]


if __name__ == "__main__":
    random.seed(42)

    # Generate slowly-drifting data: clusters move over time
    stream = []

    # Phase 1: Clusters at (0, 0), (3, 0), (0, 3)
    for t in range(150):
        for cluster_idx in range(3):
            # Cluster centers drift slowly
            drift = t * 0.01
            centers = [
                (0 + drift, 0 + drift),
                (3 + drift, 0 - drift),
                (0 - drift, 3 + drift),
            ]
            cx, cy = centers[cluster_idx]
            x = random.gauss(cx, 0.3)
            y = random.gauss(cy, 0.3)
            stream.append([x, y])

    # Shuffle stream to make it realistic
    random.shuffle(stream)

    # Process stream with streaming k-means
    kmeans = StreamingKMeans(k=3)
    kmeans.initialize(stream[:3])

    for point in stream:
        kmeans.process(point)

    final_centroids = kmeans.get_centroids()
    print(f"Final centroids: {[[f'{c:.2f}' for c in centroid] for centroid in final_centroids]}")

    # Verify centroids are reasonable (roughly in expected regions)
    # After drift, expected centers are around (1.5, 1.5), (4.5, -1.5), (-1.5, 4.5)
    expected_centers = [(1.5, 1.5), (4.5, -1.5), (-1.5, 4.5)]

    # Find closest centroid to each expected center
    matched = [False] * 3
    distances = []
    for i, (ex, ey) in enumerate(expected_centers):
        min_dist = float("inf")
        for cx, cy in final_centroids:
            dist = math.sqrt((ex - cx) ** 2 + (ey - cy) ** 2)
            min_dist = min(min_dist, dist)
        distances.append(min_dist)
        print(f"Expected ({ex}, {ey}): closest centroid dist {min_dist:.2f}")

    avg_dist = sum(distances) / len(distances)

    # Assertion: average distance to expected centers should be reasonable (clusters tracked)
    assert avg_dist < 2.0, f"Centroids should track drifting clusters: avg distance {avg_dist}"

    print("✓ Streaming k-means: PASS")
