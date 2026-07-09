"""
Isolation Forest (Lite) Anomaly Detection from scratch.

Ensemble of random isolation trees: points requiring fewer splits to isolate are likely
anomalies (short average path length). Core idea: anomalies are isolated easily; normals
require many splits. Anomaly score = average path length across trees (lower = anomaly).

Use when: detecting outliers/anomalies without computing distances to all points.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import math
from typing import List, Tuple, Optional

class IsolationNode:
    """Node in isolation tree."""
    def __init__(self):
        self.split_feature = None
        self.split_value = None
        self.left = None
        self.right = None
        self.size = 0  # Number of points at this node

def build_isolation_tree(
    points: List[Tuple[float, ...]],
    indices: List[int],
    depth: int = 0,
    max_depth: int = 10,
) -> IsolationNode:
    """Build a single isolation tree recursively."""
    node = IsolationNode()
    node.size = len(indices)

    # Base case: single point or max depth
    if len(indices) <= 1 or depth >= max_depth:
        return node

    # Randomly select a feature and split value
    num_features = len(points[0])
    split_feature = random.randint(0, num_features - 1)

    # Find min/max values for this feature
    values = [points[i][split_feature] for i in indices]
    min_val = min(values)
    max_val = max(values)

    if min_val == max_val:
        return node  # Can't split

    split_value = random.uniform(min_val, max_val)
    node.split_feature = split_feature
    node.split_value = split_value

    # Partition indices
    left_indices = [i for i in indices if points[i][split_feature] < split_value]
    right_indices = [i for i in indices if points[i][split_feature] >= split_value]

    if len(left_indices) == 0 or len(right_indices) == 0:
        return node  # Bad split; return leaf

    # Recursively build children
    node.left = build_isolation_tree(points, left_indices, depth + 1, max_depth)
    node.right = build_isolation_tree(points, right_indices, depth + 1, max_depth)

    return node

def path_length(tree: IsolationNode, point: Tuple[float, ...], depth: int = 0) -> int:
    """Compute path length from root to leaf for a point."""
    if tree.split_feature is None or tree.left is None or tree.right is None:
        return depth

    if point[tree.split_feature] < tree.split_value:
        return path_length(tree.left, point, depth + 1)
    else:
        return path_length(tree.right, point, depth + 1)

def isolation_forest_anomaly_score(
    points: List[Tuple[float, ...]],
    num_trees: int = 50,
    seed: int = 42,
) -> List[float]:
    """
    Compute anomaly scores using isolation forest ensemble.

    Args:
        points: List of points
        num_trees: Number of trees to build
        seed: Random seed

    Returns:
        Anomaly scores (lower = more anomalous)
    """
    random.seed(seed)
    n_points = len(points)
    trees = []

    # Build ensemble of trees
    for _ in range(num_trees):
        # Random sample (with replacement)
        sample_size = min(256, n_points)
        sample_indices = [random.randint(0, n_points - 1) for _ in range(sample_size)]
        tree = build_isolation_tree(points, sample_indices)
        trees.append(tree)

    # Compute average path length for each point
    scores = []
    for point in points:
        path_lengths = [path_length(tree, point) for tree in trees]
        avg_path_length = sum(path_lengths) / len(path_lengths)
        scores.append(avg_path_length)

    return scores

if __name__ == "__main__":
    random.seed(42)

    # Generate normal points in a cluster
    normal = [
        (random.gauss(5.0, 0.5), random.gauss(5.0, 0.5))
        for _ in range(100)
    ]

    # Add outliers
    outliers = [
        (random.uniform(-5, 0), random.uniform(-5, 0))
        for _ in range(5)
    ]

    points = normal + outliers
    true_labels = [0] * 100 + [1] * 5

    # Compute anomaly scores
    scores = isolation_forest_anomaly_score(points, num_trees=30, seed=42)

    # Anomaly score should correlate with true labels (lower score = anomaly)
    # Check: outliers should have lower average path length than normals
    normal_scores = [scores[i] for i in range(100)]
    outlier_scores = [scores[i] for i in range(100, 105)]

    avg_normal = sum(normal_scores) / len(normal_scores)
    avg_outlier = sum(outlier_scores) / len(outlier_scores)

    assert avg_outlier < avg_normal, f"Outliers should have lower path length: {avg_outlier} vs {avg_normal}"
    assert avg_normal > 0, "Scores should be positive"

    print(f"isolation_tree_anomaly.py: normal_avg={avg_normal:.2f}, outlier_avg={avg_outlier:.2f} PASS")
