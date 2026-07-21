"""
Binary Logistic Regression via Gradient Descent (from scratch).

Core idea: Model binary classification via sigmoid(z) = 1 / (1 + e^-z).
Given labeled data (X, y) where y ∈ {0, 1}, fit weights w and bias b
by minimizing binary cross-entropy loss via gradient descent.

When to use: Binary classification; interpretable probabilities; small to medium data.
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

def _aura_validate_sigmoid(z):
    v = []
    if isinstance(z, (int, float)) and not math.isfinite(z):
        v.append(f"AURA-E008: z must be finite, got {z}")
    if v:
        raise AuraInputError(v)

def sigmoid(z: float) -> float:
    """Compute sigmoid(z) = 1 / (1 + exp(-z))."""
    _aura_validate_sigmoid(z)
    if z > 100:  # Prevent overflow
        return 1.0
    if z < -100:
        return 0.0
    return 1.0 / (1.0 + math.exp(-z))


def logistic_regression_fit(
    X: List[List[float]],
    y: List[int],
    learning_rate: float = 0.01,
    iterations: int = 100
) -> Tuple[List[float], float]:
    """
    Fit a logistic regression model using gradient descent.

    Args:
        X: list of feature vectors
        y: list of binary labels (0 or 1)
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

    for _ in range(iterations):
        # Compute predictions (probabilities)
        predictions = []
        for i in range(n_samples):
            z = bias + sum(weights[j] * X[i][j] for j in range(n_features))
            predictions.append(sigmoid(z))

        # Compute gradients (binary cross-entropy)
        errors = [predictions[i] - y[i] for i in range(n_samples)]
        dw = [sum(errors[i] * X[i][j] for i in range(n_samples)) / n_samples
              for j in range(n_features)]
        db = sum(errors) / n_samples

        # Update parameters
        weights = [weights[j] - learning_rate * dw[j] for j in range(n_features)]
        bias = bias - learning_rate * db

    return weights, bias


def logistic_regression_predict(
    X: List[List[float]],
    weights: List[float],
    bias: float,
    threshold: float = 0.5
) -> List[int]:
    """
    Predict binary labels for samples X.

    Args:
        X: list of feature vectors
        weights: fitted weights
        bias: fitted bias
        threshold: probability threshold for class 1

    Returns:
        list of predicted labels (0 or 1)
    """
    predictions = []
    for i in range(len(X)):
        z = bias + sum(weights[j] * X[i][j] for j in range(len(weights)))
        prob = sigmoid(z)
        predictions.append(1 if prob >= threshold else 0)
    return predictions


if __name__ == "__main__":
    random.seed(42)

    # Generate synthetic binary classification data
    # Class 0: centered around (-2, -2), Class 1: centered around (2, 2)
    n_samples = 40
    X = []
    y = []

    for _ in range(n_samples // 2):
        X.append([random.gauss(-2, 1), random.gauss(-2, 1)])
        y.append(0)

    for _ in range(n_samples // 2):
        X.append([random.gauss(2, 1), random.gauss(2, 1)])
        y.append(1)

    # Fit model
    weights, bias = logistic_regression_fit(X, y, learning_rate=0.1, iterations=100)

    # Predict and check accuracy
    preds = logistic_regression_predict(X, weights, bias)
    accuracy = sum(preds[i] == y[i] for i in range(n_samples)) / n_samples

    assert accuracy >= 0.85, f"Accuracy = {accuracy} is too low"

    print(f"LOGISTIC_REGRESSION PASS: accuracy = {accuracy:.3f}, weights = {[f'{w:.2f}' for w in weights]}")
