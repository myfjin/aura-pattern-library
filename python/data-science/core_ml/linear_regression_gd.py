"""
Linear Regression via Batch Gradient Descent (from scratch).

Core idea: Given labeled training data (X, y), fit a linear model y = Xw + b
by iteratively updating weights w and bias b to minimize mean squared error.
Gradient descent computes ∂loss/∂w and ∂loss/∂b each iteration and moves opposite
the gradient to reduce loss.

When to use: Continuous target prediction; interpretable model; small to medium datasets.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import math
from typing import List, Tuple


def mean(values: List[float]) -> float:
    """Compute arithmetic mean."""
    return sum(values) / len(values) if values else 0.0


def variance(values: List[float]) -> float:
    """Compute sample variance."""
    if not values:
        return 0.0
    m = mean(values)
    return sum((v - m) ** 2 for v in values) / len(values)


def linear_regression_gd(
    X: List[List[float]],
    y: List[float],
    learning_rate: float = 0.01,
    iterations: int = 100
) -> Tuple[List[float], float]:
    """
    Fit a linear regression model using batch gradient descent.

    Args:
        X: list of feature vectors (each row is a sample)
        y: list of target values
        learning_rate: step size for gradient descent
        iterations: number of update steps

    Returns:
        (weights, bias): fitted parameters
    """
    n_samples = len(X)
    n_features = len(X[0]) if X else 0

    # Initialize weights and bias
    weights = [0.0] * n_features
    bias = 0.0

    loss_history = []

    for _ in range(iterations):
        # Compute predictions
        predictions = []
        for i in range(n_samples):
            pred = bias + sum(weights[j] * X[i][j] for j in range(n_features))
            predictions.append(pred)

        # Compute MSE loss
        errors = [predictions[i] - y[i] for i in range(n_samples)]
        mse = mean([e ** 2 for e in errors])
        loss_history.append(mse)

        # Compute gradients (batch)
        dw = [sum(errors[i] * X[i][j] for i in range(n_samples)) / n_samples
              for j in range(n_features)]
        db = sum(errors) / n_samples

        # Update parameters
        weights = [weights[j] - learning_rate * dw[j] for j in range(n_features)]
        bias = bias - learning_rate * db

    return weights, bias


if __name__ == "__main__":
    random.seed(42)

    # Generate synthetic regression data: y ≈ 2*x1 + 3*x2 + noise
    n_samples = 30
    X = [[random.uniform(-5, 5), random.uniform(-5, 5)] for _ in range(n_samples)]
    y = [2.0 * X[i][0] + 3.0 * X[i][1] + random.gauss(0, 0.5) for i in range(n_samples)]

    # Train model
    weights, bias = linear_regression_gd(X, y, learning_rate=0.01, iterations=200)

    # Test: compute R² on training data
    predictions = [bias + sum(weights[j] * X[i][j] for j in range(2))
                   for i in range(n_samples)]
    ss_res = sum((predictions[i] - y[i]) ** 2 for i in range(n_samples))
    ss_tot = sum((y[i] - mean(y)) ** 2 for i in range(n_samples))
    r2 = 1.0 - (ss_res / ss_tot) if ss_tot > 0 else 0.0

    assert r2 > 0.8, f"R² = {r2} is too low"
    assert abs(weights[0] - 2.0) < 0.5, f"w[0] = {weights[0]}, expected ~2.0"
    assert abs(weights[1] - 3.0) < 0.5, f"w[1] = {weights[1]}, expected ~3.0"

    print(f"LINEAR_REGRESSION_GD PASS: R² = {r2:.3f}, weights = {[f'{w:.2f}' for w in weights]}")
