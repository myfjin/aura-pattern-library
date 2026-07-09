"""
AdaBoost Classification with Decision Stumps.

AdaBoost sequentially fits weak learners (decision stumps) by reweighting
training examples: samples misclassified by the current stump get higher
weight in the next round. The ensemble combines weak learners with weights
based on their accuracy.

Use when: iterative ensemble for classification, balancing examples hard to classify.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import math
from typing import List, Tuple

def fit_stump_binary(X: List[Tuple[float, float]], y: List[int],
                     sample_weights: List[float]) -> Tuple[int, float, int, int]:
    """Fit a decision stump with weighted samples. Returns (feature, threshold, left_label, right_label)."""
    if not X:
        return 0, 0.0, 0, 1

    best_feature = 0
    best_threshold = 0.0
    best_accuracy = -1.0
    best_left_label = 0
    best_right_label = 1

    # Try each feature
    for feat in range(len(X[0])):
        feature_vals = [(X[i][feat], i) for i in range(len(X))]
        feature_vals.sort()

        # Try each split
        for i in range(len(feature_vals) - 1):
            threshold = (feature_vals[i][0] + feature_vals[i+1][0]) / 2

            # Count weighted accuracy for both label assignments
            for left_label in [0, 1]:
                right_label = 1 - left_label
                correct_weight = 0.0

                for j in range(len(X)):
                    pred = left_label if X[j][feat] < threshold else right_label
                    if pred == y[j]:
                        correct_weight += sample_weights[j]

                accuracy = correct_weight / sum(sample_weights)

                if accuracy > best_accuracy:
                    best_accuracy = accuracy
                    best_feature = feat
                    best_threshold = threshold
                    best_left_label = left_label
                    best_right_label = right_label

    return best_feature, best_threshold, best_left_label, best_right_label

def predict_stump(x: Tuple[float, float], feature: int, threshold: float,
                  left_label: int, right_label: int) -> int:
    """Predict with a single stump."""
    return left_label if x[feature] < threshold else right_label

def adaboost(X: List[Tuple[float, float]], y: List[int], n_rounds: int = 10) -> List[Tuple]:
    """Fit AdaBoost ensemble. Returns list of (stump, alpha) tuples."""
    n = len(X)
    sample_weights = [1.0 / n] * n
    ensemble = []

    for round_num in range(n_rounds):
        # Fit stump with current weights
        feature, threshold, left_label, right_label = fit_stump_binary(X, y, sample_weights)
        stump = (feature, threshold, left_label, right_label)

        # Compute weighted error
        error = 0.0
        for i in range(n):
            pred = predict_stump(X[i], feature, threshold, left_label, right_label)
            if pred != y[i]:
                error += sample_weights[i]

        # Prevent division by zero and stop if error is too high
        error = max(error, 1e-10)
        error = min(error, 1.0 - 1e-10)

        # Compute weight of this stump (alpha)
        alpha = 0.5 * math.log((1.0 - error) / error)
        ensemble.append((stump, alpha))

        # Reweight samples: misclassified samples get higher weight
        total_weight = 0.0
        for i in range(n):
            pred = predict_stump(X[i], feature, threshold, left_label, right_label)
            if pred != y[i]:
                sample_weights[i] *= math.exp(alpha)
            total_weight += sample_weights[i]

        # Normalize weights
        sample_weights = [w / total_weight for w in sample_weights]

    return ensemble

def predict_ensemble(x: Tuple[float, float], ensemble: List[Tuple]) -> int:
    """Predict with AdaBoost ensemble using weighted voting."""
    weighted_sum = 0.0
    for (feature, threshold, left_label, right_label), alpha in ensemble:
        pred = 1 if (left_label if x[feature] < threshold else right_label) == 1 else -1
        weighted_sum += alpha * pred
    return 1 if weighted_sum >= 0 else 0

if __name__ == "__main__":
    random.seed(42)

    # Generate 2D synthetic classification data with overlap
    # Class 0 and 1 overlap significantly to prevent perfect separation
    n_per_class = 40
    X = []
    y = []

    for i in range(n_per_class):
        X.append((random.gauss(4, 2.5), random.gauss(4, 2.5)))
        y.append(0)

    for i in range(n_per_class):
        X.append((random.gauss(6, 2.5), random.gauss(6, 2.5)))
        y.append(1)

    # Single stump baseline
    weights = [1.0 / len(X)] * len(X)
    feature, threshold, left_label, right_label = fit_stump_binary(X, y, weights)
    single_stump_preds = [predict_stump(x, feature, threshold, left_label, right_label) for x in X]
    single_stump_acc = sum(1 for i in range(len(y)) if single_stump_preds[i] == y[i]) / len(y)

    # AdaBoost ensemble
    ensemble = adaboost(X, y, n_rounds=10)
    ada_preds = [predict_ensemble(x, ensemble) for x in X]
    ada_acc = sum(1 for i in range(len(y)) if ada_preds[i] == y[i]) / len(y)

    # Verify ensemble beats single stump
    assert ada_acc > single_stump_acc, f"AdaBoost {ada_acc:.3f} should beat single stump {single_stump_acc:.3f}"
    print(f"adaboost: single_stump_acc={single_stump_acc:.4f}, ensemble_acc={ada_acc:.4f} PASS")
