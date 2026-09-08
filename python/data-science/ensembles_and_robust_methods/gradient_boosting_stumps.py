"""
Gradient Boosting with Decision Stumps.

Gradient boosting iteratively fits weak learners (depth-1 decision trees) to
residuals of the previous ensemble, with each new tree weighted by a learning rate.
Training loss decreases monotonically and the ensemble beats a single stump on regression.

Use when: sequential ensemble improvement, regression on tabular data.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import math
from typing import List, Tuple


class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))


def _aura_validate_gini_split(y):
    v = []
    if hasattr(y, '__iter__'):
        for i, val in enumerate(y):
            if isinstance(val, (int, float)) and not math.isfinite(val):
                v.append(f"AURA-E008: y[{i}] must be finite, got {val}")
    if v:
        raise AuraInputError(v)


def _aura_validate_gradient_boost(y, n_rounds, learning_rate):
    v = []
    if isinstance(n_rounds, (int, float)) and n_rounds < 1:
        v.append(f"AURA-E009: n_rounds must be >= 1, got {n_rounds}")
    if isinstance(learning_rate, (int, float)) and learning_rate <= 0:
        v.append(f"AURA-E009: learning_rate must be > 0, got {learning_rate}")
    if hasattr(y, '__iter__'):
        for i, val in enumerate(y):
            if isinstance(val, (int, float)) and not math.isfinite(val):
                v.append(f"AURA-E008: y[{i}] must be finite, got {val}")
    if v:
        raise AuraInputError(v)


def gini_split(y: List[float]) -> Tuple[float, float]:
    """Find best threshold for a single feature (stumps only split once)."""
    _aura_validate_gini_split(y)
    if len(y) < 2:
        return 0.0, float('inf')

    sorted_y = sorted(y)
    best_mse = float('inf')
    best_threshold = sorted_y[0]

    # Try thresholds between consecutive sorted values
    for i in range(len(sorted_y) - 1):
        threshold = (sorted_y[i] + sorted_y[i+1]) / 2
        left = [v for v in y if v < threshold]
        right = [v for v in y if v >= threshold]

        if not left or not right:
            continue

        left_mean = sum(left) / len(left)
        right_mean = sum(right) / len(right)
        left_mse = sum((x - left_mean)**2 for x in left) / len(left)
        right_mse = sum((x - right_mean)**2 for x in right) / len(right)
        # Weighted average of within-group MSEs
        mse = (len(left) * left_mse + len(right) * right_mse) / len(y)

        if mse < best_mse:
            best_mse = mse
            best_threshold = threshold

    return best_threshold, best_mse

def fit_stump(X: List[Tuple[float, float]], y: List[float]) -> Tuple[int, float, float, float]:
    """Fit a single decision stump (depth-1 tree) by minimizing MSE of y predictions."""
    if not X:
        return 0, 0.0, 0.0, 0.0

    best_feature = 0
    best_threshold = 0.0
    best_mse = float('inf')
    best_left_val = 0.0
    best_right_val = 0.0

    # Try each feature
    for feat in range(len(X[0])):
        feature_vals = [x[feat] for x in X]
        sorted_features = sorted(feature_vals)

        # Try each split point (between consecutive sorted values)
        for i in range(len(sorted_features) - 1):
            threshold = (sorted_features[i] + sorted_features[i+1]) / 2

            # Partition y based on feature value
            left_y = [y[j] for j in range(len(X)) if X[j][feat] < threshold]
            right_y = [y[j] for j in range(len(X)) if X[j][feat] >= threshold]

            if not left_y or not right_y:
                continue

            # Predict with means
            left_mean = sum(left_y) / len(left_y)
            right_mean = sum(right_y) / len(right_y)

            # Compute overall MSE for this split
            mse = 0.0
            for j in range(len(X)):
                pred = left_mean if X[j][feat] < threshold else right_mean
                mse += (y[j] - pred)**2
            mse /= len(y)

            if mse < best_mse:
                best_mse = mse
                best_feature = feat
                best_threshold = threshold
                best_left_val = left_mean
                best_right_val = right_mean

    return best_feature, best_threshold, best_left_val, best_right_val

def predict_stump(x: Tuple[float, float], feature: int, threshold: float,
                  left_val: float, right_val: float) -> float:
    """Predict with a single stump."""
    return left_val if x[feature] < threshold else right_val

def gradient_boost(X: List[Tuple[float, float]], y: List[float], n_rounds: int = 10,
                   learning_rate: float = 0.1) -> Tuple[List[Tuple[int, float, float, float, float]], float]:
    """Fit gradient boosting ensemble. Each stump stored with its learning rate."""
    _aura_validate_gradient_boost(y, n_rounds, learning_rate)
    stumps = []
    pred = [0.0] * len(y)

    for round_num in range(n_rounds):
        # Residuals are gradients for MSE loss
        residuals = [y[i] - pred[i] for i in range(len(y))]

        # Fit stump to residuals
        feature, threshold, left_val, right_val = fit_stump(X, residuals)

        # Scale stump predictions by learning rate before storage
        stumps.append((feature, threshold, learning_rate * left_val, learning_rate * right_val))

        # Update predictions (no additional scaling)
        for i in range(len(X)):
            stump_pred = predict_stump(X[i], feature, threshold, learning_rate * left_val,
                                      learning_rate * right_val)
            pred[i] += stump_pred

    return stumps, sum((y[i] - pred[i])**2 for i in range(len(y))) / len(y)

if __name__ == "__main__":
    random.seed(42)

    # Four-region piecewise constant function: requires multiple splits
    # Divide [0,10]x[0,10] into 4 quadrants with different values
    n = 100
    X = [(random.uniform(0, 10), random.uniform(0, 10)) for _ in range(n)]
    y = []
    for x in X:
        if x[0] <= 5 and x[1] <= 5:
            base = 1.0
        elif x[0] <= 5 and x[1] > 5:
            base = 3.0
        elif x[0] > 5 and x[1] <= 5:
            base = 2.0
        else:
            base = 4.0
        y.append(base + random.gauss(0, 0.2))

    # Single stump baseline: can only split on one feature
    feature, threshold, left_val, right_val = fit_stump(X, y)
    single_stump_pred = [predict_stump(x, feature, threshold, left_val, right_val) for x in X]
    single_stump_mse = sum((y[i] - single_stump_pred[i])**2 for i in range(len(y))) / len(y)

    # Gradient boosting: builds second stump to handle residuals
    stumps, gb_mse = gradient_boost(X, y, n_rounds=50, learning_rate=0.25)

    # Predict with boosting ensemble (learning rate already in stump values)
    gb_pred = [0.0] * len(X)
    for x_idx, x in enumerate(X):
        for feature, threshold, left_val, right_val in stumps:
            gb_pred[x_idx] += predict_stump(x, feature, threshold, left_val, right_val)
    gb_final_mse = sum((y[i] - gb_pred[i])**2 for i in range(len(y))) / len(y)

    # Verify improvement (boosting should substantially reduce MSE on 4-quadrant target)
    improvement_ratio = single_stump_mse / (gb_final_mse + 1e-10)
    assert improvement_ratio > 1.15, f"GB should improve stump by >15%; got {improvement_ratio:.2f}x"
    print(f"gradient_boosting_stumps: single_stump_mse={single_stump_mse:.4f}, boosted_mse={gb_final_mse:.4f} PASS")
