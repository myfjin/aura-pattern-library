"""
Decision Tree Classifier using ID3 Algorithm (from scratch).

Core idea: Recursively split data on the feature that gives the highest
information gain (reduction in entropy). Build tree top-down, stopping when
all samples are of one class or max depth is reached.

When to use: Non-linear boundaries; interpretable rules; categorical/continuous data.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import math
from typing import List, Tuple, Optional, Dict, Any


def entropy(class_counts: Dict[int, int]) -> float:
    """Compute Shannon entropy from class counts."""
    total = sum(class_counts.values())
    if total == 0:
        return 0.0
    ent = 0.0
    for count in class_counts.values():
        if count > 0:
            p = count / total
            ent -= p * math.log2(p)
    return ent


def information_gain(
    parent_entropy: float,
    child_entropies: List[Tuple[int, float]]
) -> float:
    """
    Compute information gain from a split.

    Args:
        parent_entropy: entropy of parent node
        child_entropies: list of (sample_count, entropy) for each child

    Returns:
        information gain
    """
    total = sum(count for count, _ in child_entropies)
    weighted_child_entropy = sum((count / total) * ent for count, ent in child_entropies)
    return parent_entropy - weighted_child_entropy


class TreeNode:
    """A node in the decision tree."""
    def __init__(self):
        self.feature: Optional[int] = None
        self.threshold: Optional[float] = None
        self.label: Optional[int] = None  # For leaf nodes
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None


def build_tree(
    X: List[List[float]],
    y: List[int],
    max_depth: int = 5,
    depth: int = 0
) -> TreeNode:
    """
    Build a decision tree using ID3 (information gain).

    Args:
        X: feature matrix
        y: labels
        max_depth: maximum tree depth
        depth: current depth (for recursion)

    Returns:
        root TreeNode
    """
    node = TreeNode()

    # Base cases: all same class or max depth
    class_counts = {}
    for label in y:
        class_counts[label] = class_counts.get(label, 0) + 1

    if len(class_counts) == 1 or depth >= max_depth or len(X) == 0:
        node.label = max(class_counts, key=class_counts.get)
        return node

    # Try to find best split
    parent_entropy = entropy(class_counts)
    n_features = len(X[0]) if X else 0
    best_gain = 0.0
    best_feature = None
    best_threshold = None

    for feature in range(n_features):
        # Try each unique value as threshold
        thresholds = sorted(set(X[i][feature] for i in range(len(X))))

        for i in range(len(thresholds) - 1):
            threshold = (thresholds[i] + thresholds[i + 1]) / 2.0

            # Split data
            left_indices = [j for j in range(len(X)) if X[j][feature] <= threshold]
            right_indices = [j for j in range(len(X)) if X[j][feature] > threshold]

            if len(left_indices) == 0 or len(right_indices) == 0:
                continue

            # Compute entropy of children
            left_counts = {}
            right_counts = {}

            for idx in left_indices:
                left_counts[y[idx]] = left_counts.get(y[idx], 0) + 1
            for idx in right_indices:
                right_counts[y[idx]] = right_counts.get(y[idx], 0) + 1

            left_entropy = entropy(left_counts)
            right_entropy = entropy(right_counts)

            gain = information_gain(parent_entropy, [
                (len(left_indices), left_entropy),
                (len(right_indices), right_entropy)
            ])

            if gain > best_gain:
                best_gain = gain
                best_feature = feature
                best_threshold = threshold

    # If no good split found, make leaf
    if best_feature is None:
        node.label = max(class_counts, key=class_counts.get)
        return node

    # Split and recurse
    left_indices = [j for j in range(len(X)) if X[j][best_feature] <= best_threshold]
    right_indices = [j for j in range(len(X)) if X[j][best_feature] > best_threshold]

    X_left = [X[i] for i in left_indices]
    y_left = [y[i] for i in left_indices]
    X_right = [X[i] for i in right_indices]
    y_right = [y[i] for i in right_indices]

    node.feature = best_feature
    node.threshold = best_threshold
    node.left = build_tree(X_left, y_left, max_depth, depth + 1)
    node.right = build_tree(X_right, y_right, max_depth, depth + 1)

    return node


def predict_tree(x: List[float], node: TreeNode) -> int:
    """Predict class for a single sample."""
    if node.label is not None:
        return node.label

    if x[node.feature] <= node.threshold:
        return predict_tree(x, node.left)
    else:
        return predict_tree(x, node.right)


if __name__ == "__main__":
    random.seed(42)

    # Generate synthetic classification data
    n_samples = 50
    X = []
    y = []

    # Class 0: x1 < 2.5
    for _ in range(n_samples // 2):
        x1 = random.uniform(0, 2.5)
        x2 = random.uniform(0, 5)
        X.append([x1, x2])
        y.append(0)

    # Class 1: x1 >= 2.5
    for _ in range(n_samples // 2):
        x1 = random.uniform(2.5, 5)
        x2 = random.uniform(0, 5)
        X.append([x1, x2])
        y.append(1)

    # Build tree
    tree = build_tree(X, y, max_depth=5)

    # Test on training data
    preds = [predict_tree(X[i], tree) for i in range(len(X))]
    accuracy = sum(preds[i] == y[i] for i in range(len(X))) / len(X)

    assert accuracy >= 0.95, f"Accuracy = {accuracy} is too low"

    print(f"DECISION_TREE_ID3 PASS: accuracy = {accuracy:.3f}")
