"""
Hierarchical Agglomerative Clustering from scratch.

Bottom-up merging of clusters using distance linkage (single or complete). Produces a
dendrogram (tree structure) of nested partitions. Cut at height k to get k clusters.
Core idea: repeatedly merge two closest clusters until one remains.

Use when: you want a hierarchy of clusters or need to explore multiple granularities.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
from typing import List, Tuple, Set

def euclidean_distance(p1: Tuple[float, ...], p2: Tuple[float, ...]) -> float:
    """Compute Euclidean distance between two points."""
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

def cluster_distance(
    cluster_a: List[int],
    cluster_b: List[int],
    points: List[Tuple[float, ...]],
    linkage: str
) -> float:
    """
    Compute distance between two clusters using specified linkage.

    Args:
        cluster_a, cluster_b: Lists of point indices in each cluster
        points: Original points
        linkage: "single" (min) or "complete" (max)

    Returns:
        Distance between clusters
    """
    distances = [
        euclidean_distance(points[i], points[j])
        for i in cluster_a
        for j in cluster_b
    ]
    return min(distances) if linkage == "single" else max(distances)

def hierarchical_agglomerative(
    points: List[Tuple[float, ...]],
    linkage: str = "complete"
) -> Tuple[List[List[int]], List[Tuple[int, int, float]]]:
    """
    Hierarchical agglomerative clustering.

    Args:
        points: List of points (tuples of coordinates)
        linkage: "single" or "complete"

    Returns:
        (clusters at each merge step, list of (cluster_i, cluster_j, distance))
    """
    # Start with each point in its own cluster
    clusters = [[i] for i in range(len(points))]
    merge_history = []

    while len(clusters) > 1:
        # Find two closest clusters
        min_distance = float("inf")
        merge_i, merge_j = -1, -1

        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                dist = cluster_distance(clusters[i], clusters[j], points, linkage)
                if dist < min_distance:
                    min_distance = dist
                    merge_i, merge_j = i, j

        # Merge clusters[merge_j] into clusters[merge_i]
        merged = clusters[merge_i] + clusters[merge_j]
        merge_history.append((merge_i, merge_j, min_distance))

        # Remove merge_j (always remove higher index to avoid shifting)
        clusters[merge_i] = merged
        clusters.pop(merge_j)

    return clusters, merge_history

def cut_dendrogram(
    points: List[Tuple[float, ...]],
    k: int,
    linkage: str = "complete"
) -> List[int]:
    """
    Cut the dendrogram at a given number of clusters.

    Args:
        points: List of points
        k: Desired number of clusters
        linkage: "single" or "complete"

    Returns:
        Cluster labels for each point
    """
    clusters = [[i] for i in range(len(points))]

    while len(clusters) > k:
        min_distance = float("inf")
        merge_i, merge_j = -1, -1

        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                dist = cluster_distance(clusters[i], clusters[j], points, linkage)
                if dist < min_distance:
                    min_distance = dist
                    merge_i, merge_j = i, j

        clusters[merge_i] = clusters[merge_i] + clusters[merge_j]
        clusters.pop(merge_j)

    # Convert to labels
    labels = [-1] * len(points)
    for cluster_id, cluster in enumerate(clusters):
        for point_idx in cluster:
            labels[point_idx] = cluster_id

    return labels

if __name__ == "__main__":
    import random
    random.seed(42)

    # Plant three clusters
    cluster1 = [(random.gauss(0.0, 0.5), random.gauss(0.0, 0.5)) for _ in range(10)]
    cluster2 = [(random.gauss(5.0, 0.5), random.gauss(5.0, 0.5)) for _ in range(10)]
    cluster3 = [(random.gauss(10.0, 0.5), random.gauss(0.0, 0.5)) for _ in range(10)]

    points = cluster1 + cluster2 + cluster3
    labels = cut_dendrogram(points, k=3, linkage="complete")

    # Check: should find 3 clusters
    unique_labels = set(labels)
    assert len(unique_labels) == 3, f"Expected 3 clusters, got {len(unique_labels)}"
    assert all(l in range(3) for l in labels), "Invalid cluster labels"

    # Check each original cluster is mostly in one recovered cluster
    c1_labels = [labels[i] for i in range(10)]
    c2_labels = [labels[i] for i in range(10, 20)]
    c3_labels = [labels[i] for i in range(20, 30)]

    def most_common(lst):
        return max(set(lst), key=lst.count)

    assert len(set(c1_labels)) <= 2, "Cluster 1 too fragmented"
    assert len(set(c2_labels)) <= 2, "Cluster 2 too fragmented"
    assert len(set(c3_labels)) <= 2, "Cluster 3 too fragmented"

    print(f"hierarchical_agglomerative.py: 3 clusters recovered, cutoff works PASS")
