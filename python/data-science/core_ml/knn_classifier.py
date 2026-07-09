"""
k-Nearest Neighbors Classifier (from scratch).

Core idea: To classify a new point, find the k nearest training samples using
Euclidean distance and predict the majority class among them. No training phase;
prediction is expensive but the model is simple and often effective.

When to use: Non-linear boundaries; small to medium datasets; quick prototypes.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import math
from typing import List, Tuple


def euclidean_distance(p1: List[float], p2: List[float]) -> float:
    """Compute Euclidean distance between two points."""
    return math.sqrt(sum((p1[i] - p2[i]) ** 2 for i in range(len(p1))))


def knn_predict(
    x_test: List[float],
    X_train: List[List[float]],
    y_train: List[int],
    k: int = 3
) -> int:
    """
    Predict the class of a single test point using kNN.

    Args:
        x_test: feature vector of test point
        X_train: list of training feature vectors
        y_train: list of training labels
        k: number of neighbors to consider

    Returns:
        predicted class label
    """
    # Compute distances to all training points
    distances = []
    for i in range(len(X_train)):
        dist = euclidean_distance(x_test, X_train[i])
        distances.append((dist, y_train[i]))

    # Sort by distance and take k nearest
    distances.sort()
    k_nearest = distances[:k]

    # Majority vote
    votes = {}
    for _, label in k_nearest:
        votes[label] = votes.get(label, 0) + 1

    return max(votes, key=votes.get)


def knn_predict_batch(
    X_test: List[List[float]],
    X_train: List[List[float]],
    y_train: List[int],
    k: int = 3
) -> List[int]:
    """
    Predict classes for multiple test points.

    Args:
        X_test: list of test feature vectors
        X_train: list of training feature vectors
        y_train: list of training labels
        k: number of neighbors

    Returns:
        list of predicted labels
    """
    return [knn_predict(X_test[i], X_train, y_train, k) for i in range(len(X_test))]


if __name__ == "__main__":
    random.seed(42)

    # Generate synthetic classification data (two classes)
    n_train = 50
    X_train = []
    y_train = []

    # Class 0: around (0, 0)
    for _ in range(n_train // 2):
        X_train.append([random.gauss(0, 1), random.gauss(0, 1)])
        y_train.append(0)

    # Class 1: around (5, 5)
    for _ in range(n_train // 2):
        X_train.append([random.gauss(5, 1), random.gauss(5, 1)])
        y_train.append(1)

    # Generate test data
    n_test = 20
    X_test = []
    y_test = []

    for _ in range(n_test // 2):
        X_test.append([random.gauss(0, 0.8), random.gauss(0, 0.8)])
        y_test.append(0)

    for _ in range(n_test // 2):
        X_test.append([random.gauss(5, 0.8), random.gauss(5, 0.8)])
        y_test.append(1)

    # Predict and check accuracy
    preds = knn_predict_batch(X_test, X_train, y_train, k=5)
    accuracy = sum(preds[i] == y_test[i] for i in range(n_test)) / n_test

    assert accuracy >= 0.8, f"Accuracy = {accuracy} is too low"

    print(f"KNN_CLASSIFIER PASS: accuracy = {accuracy:.3f}, k = 5")
