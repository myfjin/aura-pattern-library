"""
Permutation Feature Importance

Core idea: Shuffle each feature independently on held-out data and measure the drop in model
performance. Features whose shuffling hurts performance are important; noise features don't affect
predictions when shuffled.

When to use: You've trained a model and want to rank features by their predictive contribution,
agnostic to the model's internal structure.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import statistics
from typing import List, Tuple, Callable


def train_simple_model(X: List[List[float]], y: List[float]) -> Tuple[float, float, float]:
    """Fit a linear predictor via simple least-squares. Returns (intercept, weight_f1, weight_f2)."""
    n = len(X)
    x1_vals = [x[0] for x in X]
    x2_vals = [x[1] for x in X]

    x1_mean = sum(x1_vals) / n
    x2_mean = sum(x2_vals) / n
    y_mean = sum(y) / n

    cov_x1_y = sum((x1_vals[i] - x1_mean) * (y[i] - y_mean) for i in range(n)) / n
    cov_x2_y = sum((x2_vals[i] - x2_mean) * (y[i] - y_mean) for i in range(n)) / n
    var_x1 = sum((x - x1_mean) ** 2 for x in x1_vals) / n
    var_x2 = sum((x - x2_mean) ** 2 for x in x2_vals) / n

    w1 = cov_x1_y / var_x1 if var_x1 > 0 else 0
    w2 = cov_x2_y / var_x2 if var_x2 > 0 else 0

    intercept = y_mean - w1 * x1_mean - w2 * x2_mean
    return intercept, w1, w2


def predict(X: List[List[float]], coeffs: Tuple[float, float, float]) -> List[float]:
    """Predict using linear model."""
    intercept, w1, w2 = coeffs
    return [intercept + w1 * x[0] + w2 * x[1] for x in X]


def mse(y_true: List[float], y_pred: List[float]) -> float:
    """Compute mean squared error."""
    return sum((y_t - y_p) ** 2 for y_t, y_p in zip(y_true, y_pred)) / len(y_true)


def permutation_importance(
    X_test: List[List[float]], y_test: List[float], coeffs: Tuple[float, float, float]
) -> Tuple[float, float]:
    """
    Compute permutation importance for each feature.
    Returns (importance_f1, importance_f2).
    """
    # Baseline: model performance on original data
    y_pred_orig = predict(X_test, coeffs)
    baseline_mse = mse(y_test, y_pred_orig)

    importances = []

    # For each feature, shuffle and measure performance drop
    for feat_idx in range(2):
        X_shuffled = [row[:] for row in X_test]  # Deep copy
        shuffled_vals = [row[feat_idx] for row in X_shuffled]
        random.shuffle(shuffled_vals)
        for i, val in enumerate(shuffled_vals):
            X_shuffled[i][feat_idx] = val

        y_pred_shuffled = predict(X_shuffled, coeffs)
        shuffled_mse = mse(y_test, y_pred_shuffled)

        importance = shuffled_mse - baseline_mse  # Higher = more important
        importances.append(importance)

    return tuple(importances)


if __name__ == "__main__":
    random.seed(42)

    # Generate synthetic data: y = 5 + 3*x1 + 0.1*noise_x2
    # x1 is informative, x2 is noise
    train_X = []
    train_y = []
    for _ in range(100):
        x1 = random.uniform(-2, 2)
        x2 = random.uniform(-2, 2)  # Noise feature, not used in true model
        y = 5 + 3 * x1 + random.gauss(0, 0.5)
        train_X.append([x1, x2])
        train_y.append(y)

    # Fit model
    coeffs = train_simple_model(train_X, train_y)

    # Test on held-out data
    test_X = []
    test_y = []
    for _ in range(50):
        x1 = random.uniform(-2, 2)
        x2 = random.uniform(-2, 2)
        y = 5 + 3 * x1 + random.gauss(0, 0.5)
        test_X.append([x1, x2])
        test_y.append(y)

    # Compute permutation importance
    imp_f1, imp_f2 = permutation_importance(test_X, test_y, coeffs)

    print(f"Feature 1 importance: {imp_f1:.4f}, Feature 2 importance: {imp_f2:.4f}")

    # Assertion: informative feature's importance exceeds noise feature's
    assert imp_f1 > imp_f2, f"Informative feature should have higher importance: {imp_f1} vs {imp_f2}"
    assert imp_f1 > 0.5, f"Informative feature should have substantial importance: {imp_f1}"

    print("✓ Permutation Feature Importance: PASS")
