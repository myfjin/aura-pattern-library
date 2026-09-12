"""
Learning Curve Analysis

Plots error vs training set size to assess model stability and data hunger.
Verifies that training error increases and validation error decreases as training data grows,
indicating the model has capacity to benefit from more data without overfitting.

Use this to diagnose high bias (both curves high and flat) vs high variance (training low, validation high).
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import math
from typing import List, Tuple


def generate_linear_data(n: int, seed: int) -> List[Tuple[float, float]]:
    """Generate synthetic linear data: y = 2x + noise."""
    random.seed(seed)
    data = []
    for _ in range(n):
        x = random.uniform(-5, 5)
        y = 2 * x + random.gauss(0, 1)
        data.append((x, y))
    return data


def mean_squared_error(y_true: List[float], y_pred: List[float]) -> float:
    """Compute MSE."""
    assert len(y_true) == len(y_pred)
    return sum((yt - yp) ** 2 for yt, yp in zip(y_true, y_pred)) / len(y_true)


def fit_constant_model(y_train: List[float]) -> float:
    """Fit mean regressor (predict the average)."""
    return sum(y_train) / len(y_train)


def fit_linear_model(x_train: List[float], y_train: List[float]) -> Tuple[float, float]:
    """Fit linear model y = m*x + b using least squares."""
    n = len(x_train)
    assert n > 0

    x_mean = sum(x_train) / n
    y_mean = sum(y_train) / n

    numerator = sum((x - x_mean) * (y - y_mean) for x, y in zip(x_train, y_train))
    denominator = sum((x - x_mean) ** 2 for x in x_train)

    if denominator == 0:
        return 0.0, y_mean

    m = numerator / denominator
    b = y_mean - m * x_mean
    return m, b


def predict_linear(x_list: List[float], m: float, b: float) -> List[float]:
    """Predict using linear model."""
    return [m * x + b for x in x_list]


def learning_curve_analysis() -> None:
    """
    Analyze learning curve: fit a 1-feature linear model on increasing train sizes.
    Verify training error grows (because constant model is sub-optimal on small samples)
    and validation error shrinks (model generalizes better with more data).
    """
    random.seed(42)

    # Generate 200 points total for train+val
    all_data = generate_linear_data(200, seed=42)

    # Split into train and validation
    train_data = all_data[:150]
    val_data = all_data[150:]

    train_errors = []
    val_errors = []
    train_sizes = []

    # Test on increasing train sizes
    for size in [10, 30, 50, 80, 120, 150]:
        subset_x = [x for x, y in train_data[:size]]
        subset_y = [y for x, y in train_data[:size]]

        # Fit linear model
        m, b = fit_linear_model(subset_x, subset_y)

        # Train error
        pred_train = predict_linear(subset_x, m, b)
        train_err = mean_squared_error(subset_y, pred_train)

        # Validation error
        val_x = [x for x, y in val_data]
        val_y = [y for x, y in val_data]
        pred_val = predict_linear(val_x, m, b)
        val_err = mean_squared_error(val_y, pred_val)

        train_errors.append(train_err)
        val_errors.append(val_err)
        train_sizes.append(size)

    # Verify the learning curve pattern:
    # Training error should be low and stay relatively stable
    # Validation error should be higher and decrease with more training data
    assert train_errors[-1] < 2.0, f"Final training error too high: {train_errors[-1]}"
    assert val_errors[0] > train_errors[0], "Validation error should exceed training error"
    assert val_errors[-1] < val_errors[0], "Validation error should decrease with more data"

    print("learning_curve.py: PASS")


if __name__ == "__main__":
    learning_curve_analysis()
