"""
Online Stochastic Gradient Descent Classifier

Core idea: Train a logistic regressor in a single pass over a stream via SGD, updating
weights with each sample. Should converge close to batch solution on separable data.

When to use: Data is too large to fit in memory, or you need to update models continuously
as new data arrives (online learning).
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import math
from typing import List, Tuple


def logistic(z: float) -> float:
    """Sigmoid function."""
    return 1.0 / (1.0 + math.exp(-max(-100, min(100, z))))


def online_sgd_classifier(
    stream: List[Tuple[List[float], float]],
    learning_rate: float = 0.01,
    epochs: int = 1
) -> Tuple[List[float], float]:
    """
    Train logistic classifier via online SGD.
    Returns (weights, final_loss).
    """
    num_features = len(stream[0][0])
    weights = [0.0] * num_features
    bias = 0.0

    for epoch in range(epochs):
        for x, y in stream:
            # Forward pass
            z = bias + sum(w * xi for w, xi in zip(weights, x))
            pred = logistic(z)

            # Gradient
            error = pred - y
            for i in range(num_features):
                weights[i] -= learning_rate * error * x[i]
            bias -= learning_rate * error

    # Compute final loss
    total_loss = 0.0
    for x, y in stream:
        z = bias + sum(w * xi for w, xi in zip(weights, x))
        pred = logistic(z)
        loss = -y * math.log(pred + 1e-7) - (1 - y) * math.log(1 - pred + 1e-7)
        total_loss += loss

    return weights, total_loss / len(stream)


def batch_sgd_classifier(
    X: List[List[float]],
    y: List[float],
    learning_rate: float = 0.01,
    epochs: int = 10
) -> Tuple[List[float], float]:
    """
    Batch SGD (for comparison): train on full dataset multiple times.
    """
    num_features = len(X[0])
    weights = [0.0] * num_features
    bias = 0.0

    for epoch in range(epochs):
        for x, label in zip(X, y):
            z = bias + sum(w * xi for w, xi in zip(weights, x))
            pred = logistic(z)
            error = pred - label
            for i in range(num_features):
                weights[i] -= learning_rate * error * x[i]
            bias -= learning_rate * error

    # Compute loss
    total_loss = 0.0
    for x, label in zip(X, y):
        z = bias + sum(w * xi for w, xi in zip(weights, x))
        pred = logistic(z)
        loss = -label * math.log(pred + 1e-7) - (1 - label) * math.log(1 - pred + 1e-7)
        total_loss += loss

    return weights, total_loss / len(X)


if __name__ == "__main__":
    random.seed(42)

    # Generate separable data
    stream = []
    for _ in range(200):
        label = random.choice([0, 1])
        if label == 0:
            # Negative class: around (-1, -1)
            x = [random.gauss(-1, 0.5), random.gauss(-1, 0.5)]
        else:
            # Positive class: around (1, 1)
            x = [random.gauss(1, 0.5), random.gauss(1, 0.5)]
        stream.append((x, label))

    # Prepare for batch (convert stream to X, y)
    X_batch = [x for x, _ in stream]
    y_batch = [y for _, y in stream]

    # Online SGD (single pass)
    online_weights, online_loss = online_sgd_classifier(stream, learning_rate=0.05, epochs=1)

    # Batch SGD (multiple epochs)
    batch_weights, batch_loss = batch_sgd_classifier(X_batch, y_batch, learning_rate=0.05, epochs=5)

    print(f"Online SGD loss (1 epoch): {online_loss:.4f}")
    print(f"Batch SGD loss (5 epochs): {batch_loss:.4f}")

    # Compute accuracy on stream
    online_correct = 0
    batch_correct = 0
    for x, y in stream:
        online_pred = 1 if logistic(sum(w * xi for w, xi in zip(online_weights, x))) > 0.5 else 0
        batch_pred = 1 if logistic(sum(w * xi for w, xi in zip(batch_weights, x))) > 0.5 else 0

        if online_pred == y:
            online_correct += 1
        if batch_pred == y:
            batch_correct += 1

    online_acc = online_correct / len(stream)
    batch_acc = batch_correct / len(stream)

    print(f"Online accuracy: {online_acc:.2%}")
    print(f"Batch accuracy: {batch_acc:.2%}")

    # Assertion: online should reach reasonable accuracy on separable data
    assert online_acc > 0.7, f"Online should achieve >70% on separable data: {online_acc:.2%}"
    assert online_loss < batch_loss * 3, f"Online loss should be within 3x of batch: {online_loss} vs {batch_loss}"

    print("✓ Online SGD Classifier: PASS")
