"""
DBSCAN Clustering from scratch.

Density-based spatial clustering of applications with noise. Groups points that are
close together (within eps distance) and have at least min_pts neighbors. Handles noise
as outliers. Core idea: grow regions from dense points, merging overlapping regions.

Use when: clusters have irregular shapes, density varies, or you need to identify noise.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
import random
from typing import List, Tuple, Set

def euclidean_distance(p1: Tuple[float, ...], p2: Tuple[float, ...]) -> float:
    """Compute Euclidean distance between two points."""
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

def region_query(points: List[Tuple[float, ...]], p: int, eps: float) -> Set[int]:
    """Find all neighbors of point p within eps distance."""
    neighbors = set()
    for i, point in enumerate(points):
        if euclidean_distance(points[p], point) <= eps:
            neighbors.add(i)
    return neighbors

def dbscan(points: List[Tuple[float, ...]], eps: float, min_pts: int) -> List[int]:
    """
    DBSCAN clustering algorithm.

    Args:
        points: List of points (tuples of coordinates)
        eps: Maximum distance for neighbors
        min_pts: Minimum number of points in a neighborhood to form a dense region

    Returns:
        List of cluster labels (-1 for noise)
    """
    labels = [-1] * len(points)  # -1 = noise, 0+ = cluster id
    cluster_id = 0

    for i in range(len(points)):
        if labels[i] != -1:  # Already processed
            continue

        neighbors = region_query(points, i, eps)

        if len(neighbors) < min_pts:
            # Not a core point; stays as noise for now
            continue

        # Start a new cluster
        cluster_id += 1
        expand_cluster(points, labels, i, cluster_id, eps, min_pts)

    return labels

def expand_cluster(
    points: List[Tuple[float, ...]],
    labels: List[int],
    p: int,
    cluster_id: int,
    eps: float,
    min_pts: int
) -> None:
    """Expand cluster from a core point using BFS-like traversal."""
    seeds = region_query(points, p, eps)
    labels[p] = cluster_id

    while seeds:
        current = seeds.pop()
        if labels[current] == -1:  # Noise point
            labels[current] = cluster_id
        elif labels[current] != -1:  # Already in a cluster
            continue

        neighbors = region_query(points, current, eps)
        if len(neighbors) >= min_pts:
            # current is a core point; add its neighbors
            seeds.update(neighbors - {current})

if __name__ == "__main__":
    random.seed(42)

    # Plant two dense clusters + noise
    cluster1 = [(random.gauss(2.0, 0.3), random.gauss(2.0, 0.3)) for _ in range(20)]
    cluster2 = [(random.gauss(8.0, 0.3), random.gauss(8.0, 0.3)) for _ in range(20)]
    noise = [(random.uniform(0, 10), random.uniform(0, 10)) for _ in range(5)]

    points = cluster1 + cluster2 + noise
    labels = dbscan(points, eps=1.0, min_pts=5)

    # Check: should find 2 clusters, ~5 noise points
    unique_labels = set(labels)
    num_clusters = len(unique_labels) - (1 if -1 in unique_labels else 0)
    num_noise = sum(1 for l in labels if l == -1)

    assert num_clusters == 2, f"Expected 2 clusters, got {num_clusters}"
    assert num_noise >= 3, f"Expected at least 3 noise points, got {num_noise}"
    assert all(l >= -1 for l in labels), "Invalid cluster labels"

    print(f"dbscan_clustering.py: {num_clusters} clusters, {num_noise} noise points PASS")
