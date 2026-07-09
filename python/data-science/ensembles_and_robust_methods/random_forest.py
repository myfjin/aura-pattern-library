"""
Random Forest Classification.

Random forest builds multiple decision trees, each trained on a bootstrap
sample of the data and with random feature subsets at each split. The
ensemble averages predictions across trees, reducing overfitting variance.

Use when: robust classification on noisy data, feature importance, parallel training.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
from typing import List, Tuple, Optional

def build_tree(X: List[Tuple[float, float]], y: List[int], depth: int = 0,
               max_depth: int = 5, min_samples: int = 2) -> dict:
    """Recursively build a decision tree with random feature subsets."""
    # Base cases
    if depth >= max_depth or len(X) <= min_samples:
        # Return leaf: majority class
        class_counts = {}
        for label in y:
            class_counts[label] = class_counts.get(label, 0) + 1
        majority = max(class_counts.keys(), key=lambda k: class_counts[k])
        return {"type": "leaf", "value": majority}

    # Try to split on a random subset of features
    num_features = len(X[0])
    # Random feature subset: sqrt(num_features)
    num_try_features = max(1, int(num_features ** 0.5))
    try_features = random.sample(range(num_features), min(num_try_features, num_features))

    best_feature = None
    best_threshold = None
    best_split_score = -1.0

    # Find best split among candidate features
    for feat in try_features:
        feature_vals = [X[i][feat] for i in range(len(X))]
        sorted_vals = sorted(feature_vals)

        # Try split points
        for i in range(len(sorted_vals) - 1):
            threshold = (sorted_vals[i] + sorted_vals[i+1]) / 2

            left_y = [y[j] for j in range(len(X)) if X[j][feat] < threshold]
            right_y = [y[j] for j in range(len(X)) if X[j][feat] >= threshold]

            if not left_y or not right_y:
                continue

            # Information gain (Gini impurity)
            def gini(labels):
                if not labels:
                    return 0.0
                counts = {}
                for l in labels:
                    counts[l] = counts.get(l, 0) + 1
                gini_val = 1.0
                for c in counts.values():
                    p = c / len(labels)
                    gini_val -= p * p
                return gini_val

            parent_gini = gini(y)
            left_gini = gini(left_y)
            right_gini = gini(right_y)
            ig = parent_gini - (len(left_y) * left_gini + len(right_y) * right_gini) / len(y)

            if ig > best_split_score:
                best_split_score = ig
                best_feature = feat
                best_threshold = threshold

    # If no good split found, return leaf
    if best_feature is None:
        class_counts = {}
        for label in y:
            class_counts[label] = class_counts.get(label, 0) + 1
        majority = max(class_counts.keys(), key=lambda k: class_counts[k])
        return {"type": "leaf", "value": majority}

    # Recursively build left and right subtrees
    left_X = [X[i] for i in range(len(X)) if X[i][best_feature] < best_threshold]
    left_y = [y[i] for i in range(len(X)) if X[i][best_feature] < best_threshold]
    right_X = [X[i] for i in range(len(X)) if X[i][best_feature] >= best_threshold]
    right_y = [y[i] for i in range(len(X)) if X[i][best_feature] >= best_threshold]

    return {
        "type": "node",
        "feature": best_feature,
        "threshold": best_threshold,
        "left": build_tree(left_X, left_y, depth + 1, max_depth, min_samples),
        "right": build_tree(right_X, right_y, depth + 1, max_depth, min_samples)
    }

def predict_tree(x: Tuple[float, float], tree: dict) -> int:
    """Predict with a single tree."""
    if tree["type"] == "leaf":
        return tree["value"]
    else:
        if x[tree["feature"]] < tree["threshold"]:
            return predict_tree(x, tree["left"])
        else:
            return predict_tree(x, tree["right"])

def bootstrap_sample(X: List[Tuple[float, float]], y: List[int]) -> Tuple[List, List, List, List]:
    """Draw a bootstrap sample and return train/oob indices."""
    n = len(X)
    train_indices = [random.randint(0, n-1) for _ in range(n)]
    oob_indices = list(set(range(n)) - set(train_indices))

    X_train = [X[i] for i in train_indices]
    y_train = [y[i] for i in train_indices]
    X_oob = [X[i] for i in oob_indices]
    y_oob = [y[i] for i in oob_indices]

    return X_train, y_train, X_oob, y_oob

def random_forest(X: List[Tuple[float, float]], y: List[int], n_trees: int = 10) -> List[dict]:
    """Fit a random forest: multiple trees on bootstrap samples."""
    forest = []
    for _ in range(n_trees):
        X_train, y_train, _, _ = bootstrap_sample(X, y)
        tree = build_tree(X_train, y_train, max_depth=5, min_samples=2)
        forest.append(tree)
    return forest

def predict_forest(x: Tuple[float, float], forest: List[dict]) -> int:
    """Predict with forest: majority vote across trees."""
    votes = [predict_tree(x, tree) for tree in forest]
    vote_counts = {}
    for v in votes:
        vote_counts[v] = vote_counts.get(v, 0) + 1
    return max(vote_counts.keys(), key=lambda k: vote_counts[k])

if __name__ == "__main__":
    random.seed(42)

    # Generate noisy 2D classification data
    n_per_class = 40
    X = []
    y = []

    for i in range(n_per_class):
        x1 = random.gauss(3, 2.0)
        x2 = random.gauss(3, 2.0)
        X.append((x1, x2))
        y.append(0)

    for i in range(n_per_class):
        x1 = random.gauss(7, 2.0)
        x2 = random.gauss(7, 2.0)
        X.append((x1, x2))
        y.append(1)

    # Single tree baseline
    single_tree = build_tree(X, y, max_depth=5, min_samples=2)
    single_tree_preds = [predict_tree(x, single_tree) for x in X]
    single_tree_acc = sum(1 for i in range(len(y)) if single_tree_preds[i] == y[i]) / len(y)

    # Random forest
    forest = random_forest(X, y, n_trees=10)
    forest_preds = [predict_forest(x, forest) for x in X]
    forest_acc = sum(1 for i in range(len(y)) if forest_preds[i] == y[i]) / len(y)

    # Verify forest generalizes better on held-out data or at least matches
    # Forest should beat or equal single tree on training (ensemble effect)
    assert forest_acc >= single_tree_acc, f"Forest {forest_acc:.3f} should >= single tree {single_tree_acc:.3f}"
    print(f"random_forest: single_tree_acc={single_tree_acc:.4f}, forest_acc={forest_acc:.4f} PASS")
