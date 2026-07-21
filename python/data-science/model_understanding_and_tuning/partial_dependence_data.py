import math
"""
Partial Dependence Plot (PD) — Data Generation

Core idea: For each feature, marginalize over other features and plot the average model
prediction as that feature varies. Linear features show monotone curves; noise features show flat.

When to use: You want to understand the marginal effect of a feature on predictions, holding
other features constant in aggregate.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
from typing import List, Tuple


def train_linear_model(X: List[List[float]], y: List[float]) -> Tuple[float, List[float]]:
    """Fit linear model y = intercept + w1*x1 + w2*x2 via least squares."""
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
    return intercept, [w1, w2]




class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_predict(intercept):
    v = []
    if isinstance(intercept, (int, float)) and intercept <= 0:
        v.append(f"AURA-E009: intercept must be > 0, got {intercept}")
    if v:
        raise AuraInputError(v)

def predict(x1: float, x2: float, intercept: float, weights: List[float]) -> float:
    """Predict using linear model."""
    _aura_validate_predict(intercept)
    return intercept + weights[0] * x1 + weights[1] * x2


def partial_dependence(
    X: List[List[float]],
    intercept: float,
    weights: List[float],
    feat_idx: int,
    x_range: List[float]
) -> List[float]:
    """
    Compute partial dependence for feature feat_idx over x_range.
    Average prediction as feature varies, holding other features at their data values.
    """
    pd_values = []
    for x_val in x_range:
        predictions = []
        for row in X:
            x1 = x_val if feat_idx == 0 else row[0]
            x2 = x_val if feat_idx == 1 else row[1]
            pred = predict(x1, x2, intercept, weights)
            predictions.append(pred)
        pd_values.append(sum(predictions) / len(predictions))
    return pd_values


def is_monotone_increasing(values: List[float], tolerance: float = 0.1) -> bool:
    """Check if values are approximately monotone increasing."""
    for i in range(1, len(values)):
        if values[i] < values[i - 1] - tolerance:
            return False
    return True


def is_flat(values: List[float], tolerance: float = 0.5) -> bool:
    """Check if values are approximately flat (low variance relative to range)."""
    if not values:
        return False
    var = sum((v - sum(values) / len(values)) ** 2 for v in values) / len(values)
    return var < tolerance


if __name__ == "__main__":
    random.seed(42)

    # Generate synthetic data: y = 10 + 2*x1 + 0.1*x2_noise
    train_X = []
    train_y = []
    for _ in range(100):
        x1 = random.uniform(0, 5)
        x2 = random.uniform(0, 5)
        y = 10 + 2 * x1 + 0.1 * x2 + random.gauss(0, 0.3)
        train_X.append([x1, x2])
        train_y.append(y)

    # Train model
    intercept, weights = train_linear_model(train_X, train_y)

    # Partial dependence: feature 1 (linear) and feature 2 (noise)
    x_range = [i * 0.5 for i in range(11)]

    pd_f1 = partial_dependence(train_X, intercept, weights, 0, x_range)
    pd_f2 = partial_dependence(train_X, intercept, weights, 1, x_range)

    print(f"PD Feature 1: {[f'{v:.2f}' for v in pd_f1]}")
    print(f"PD Feature 2: {[f'{v:.2f}' for v in pd_f2]}")

    # Assertion: feature 1 shows monotone curve; feature 2 is flat
    assert is_monotone_increasing(pd_f1), f"Feature 1 should be monotone: {pd_f1}"
    assert is_flat(pd_f2), f"Feature 2 should be flat: {pd_f2}"

    print("✓ Partial Dependence Plot: PASS")
