"""
Perceptron Learning Algorithm (from scratch).

Core idea: A linear classifier for linearly separable data. The perceptron
iteratively updates weights on misclassified samples using the rule:
w ← w + y_i * x_i for each error. Converges in finite steps on separable data.

When to use: Binary classification on linearly separable data; fast training.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
from typing import List, Tuple


def perceptron_fit(
    X: List[List[float]],
    y: List[int],
    learning_rate: float = 1.0,
    max_iterations: int = 100
) -> Tuple[List[float], float]:
    """
    Fit a perceptron using the learning rule.

    Args:
        X: list of feature vectors
        y: list of binary labels (must be -1 or 1, or converted from 0/1)
        learning_rate: step size for weight updates (usually 1.0)
        max_iterations: maximum passes over data

    Returns:
        (weights, bias): fitted parameters
    """
    n_samples = len(X)
    n_features = len(X[0]) if X else 0

    # Convert labels to {-1, 1} if needed
    y_labels = [2 * label - 1 if label in (0, 1) else label for label in y]

    # Initialize weights and bias
    weights = [0.0] * n_features
    bias = 0.0

    for _ in range(max_iterations):
        num_errors = 0
        for i in range(n_samples):
            # Compute prediction
            z = bias + sum(weights[j] * X[i][j] for j in range(n_features))
            pred = 1 if z >= 0 else -1

            # Update on error
            if pred != y_labels[i]:
                error = y_labels[i] - pred
                weights = [weights[j] + learning_rate * error * X[i][j] / 2.0
                          for j in range(n_features)]
                bias = bias + learning_rate * error / 2.0
                num_errors += 1

        # Early stop if no errors
        if num_errors == 0:
            break

    return weights, bias


def perceptron_predict(
    X: List[List[float]],
    weights: List[float],
    bias: float
) -> List[int]:
    """
    Predict binary labels (0 or 1) for samples X.

    Args:
        X: list of feature vectors
        weights: fitted weights
        bias: fitted bias

    Returns:
        list of predicted labels (0 or 1)
    """
    predictions = []
    for i in range(len(X)):
        z = bias + sum(weights[j] * X[i][j] for j in range(len(weights)))
        pred = 1 if z >= 0 else 0
        predictions.append(pred)
    return predictions


if __name__ == "__main__":
    random.seed(42)

    # Generate linearly separable data
    n_samples = 40
    X = []
    y = []

    # Class 0: mostly below the line y = x
    for _ in range(n_samples // 2):
        x1 = random.uniform(-3, 3)
        x2 = x1 - random.uniform(0.5, 2.5)
        X.append([x1, x2])
        y.append(0)

    # Class 1: mostly above the line y = x
    for _ in range(n_samples // 2):
        x1 = random.uniform(-3, 3)
        x2 = x1 + random.uniform(0.5, 2.5)
        X.append([x1, x2])
        y.append(1)

    # Fit perceptron
    weights, bias = perceptron_fit(X, y, learning_rate=1.0, max_iterations=50)

    # Test accuracy
    preds = perceptron_predict(X, weights, bias)
    accuracy = sum(preds[i] == y[i] for i in range(n_samples)) / n_samples

    assert accuracy >= 0.9, f"Accuracy = {accuracy} is too low on linearly separable data"

    print(f"PERCEPTRON PASS: accuracy = {accuracy:.3f}, weights = {[f'{w:.2f}' for w in weights]}")
