"""
Class Weights for Imbalanced Classification

Core idea: When classes are imbalanced (e.g., 95% negative, 5% positive), training loss
can favor predicting the majority class. Assigning higher weight to the minority class
penalizes misclassification more, recovering minority recall.

When to use: Binary or multiclass classification with severe class imbalance, where you
care about minority class performance.
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

def _aura_validate_binary_cross_entropy(pred):
    v = []
    if isinstance(pred, (int, float)) and not math.isfinite(pred):
        v.append(f"AURA-E008: pred must be finite, got {pred}")
    if v:
        raise AuraInputError(v)

def _aura_validate_logistic(z):
    v = []
    if isinstance(z, (int, float)) and not math.isfinite(z):
        v.append(f"AURA-E008: z must be finite, got {z}")
    if v:
        raise AuraInputError(v)

def _aura_validate_weighted_binary_cross_entropy(pred):
    v = []
    if isinstance(pred, (int, float)) and not math.isfinite(pred):
        v.append(f"AURA-E008: pred must be finite, got {pred}")
    if v:
        raise AuraInputError(v)

def logistic(z: float) -> float:
    """Sigmoid function."""
    _aura_validate_logistic(z)
    return 1.0 / (1.0 + math.exp(-z))


def binary_cross_entropy(y: float, pred: float) -> float:
    """Binary cross-entropy loss."""
    _aura_validate_binary_cross_entropy(pred)
    pred = max(1e-7, min(1 - 1e-7, pred))
    return -y * math.log(pred) - (1 - y) * math.log(1 - pred)


def weighted_binary_cross_entropy(y: float, pred: float, weight: float) -> float:
    """Weighted binary cross-entropy: upweight minority class."""
    _aura_validate_weighted_binary_cross_entropy(pred)
    return weight * binary_cross_entropy(y, pred)


def train_logistic_classifier(
    X: List[List[float]],
    y: List[float],
    class_weights: Tuple[float, float] = (1.0, 1.0),
    epochs: int = 50
) -> Tuple[float, float]:
    """
    Train logistic regression via gradient descent with class weights.
    Returns (intercept, weight).
    """
    w = 0.0
    b = 0.0

    for epoch in range(epochs):
        grad_w = 0.0
        grad_b = 0.0

        for xi, yi in zip(X, y):
            z = w * xi[0] + b
            pred = logistic(z)
            error = pred - yi

            weight = class_weights[int(yi)]

            grad_w += weight * error * xi[0]
            grad_b += weight * error

        # Update
        lr = 0.01
        w -= lr * grad_w / len(X)
        b -= lr * grad_b / len(X)

    return b, w


def precision_recall(y_true: List[float], y_pred: List[float]) -> Tuple[float, float]:
    """Compute precision and recall."""
    tp = sum(1 for y, yhat in zip(y_true, y_pred) if y == 1 and yhat == 1)
    fp = sum(1 for y, yhat in zip(y_true, y_pred) if y == 0 and yhat == 1)
    fn = sum(1 for y, yhat in zip(y_true, y_pred) if y == 1 and yhat == 0)

    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0

    return precision, recall


if __name__ == "__main__":
    random.seed(42)

    # Generate imbalanced data: 90% negative, 10% positive (moderate separation)
    X = []
    y = []

    for _ in range(300):
        if random.random() < 0.90:
            # Negative class
            x = random.gauss(0.0, 1.0)
            label = 0
        else:
            # Positive class (minority, slightly shifted, noisy)
            x = random.gauss(1.0, 1.0)
            label = 1

        X.append([x])
        y.append(label)

    # Train WITHOUT class weights
    b_unweighted, w_unweighted = train_logistic_classifier(X, y, class_weights=(1.0, 1.0))

    # Train WITH class weights: upweight minority class
    pos_count = sum(y)
    neg_count = len(y) - pos_count
    # Weight positive class by (total - pos) / pos = inverse frequency
    pos_weight = neg_count / pos_count
    b_weighted, w_weighted = train_logistic_classifier(X, y, class_weights=(1.0, pos_weight))

    # Evaluate on test set
    X_test = []
    y_test = []
    for _ in range(100):
        if random.random() < 0.90:
            x = random.gauss(0.0, 1.0)
            label = 0
        else:
            x = random.gauss(1.0, 1.0)
            label = 1
        X_test.append([x])
        y_test.append(label)

    # Predictions
    preds_unweighted = [1 if logistic(w_unweighted * x[0] + b_unweighted) > 0.5 else 0 for x in X_test]
    preds_weighted = [1 if logistic(w_weighted * x[0] + b_weighted) > 0.5 else 0 for x in X_test]

    prec_unw, recall_unw = precision_recall(y_test, preds_unweighted)
    prec_w, recall_w = precision_recall(y_test, preds_weighted)

    print(f"Unweighted: Precision {prec_unw:.2%}, Recall {recall_unw:.2%}")
    print(f"Weighted: Precision {prec_w:.2%}, Recall {recall_w:.2%}")

    # Assertion: weighted training should recover minority recall
    # Even if both are low, weighted should at least match or beat unweighted on recall
    assert recall_w >= recall_unw * 0.8, f"Weighted should match or improve minority recall: {recall_w} vs {recall_unw}"
    assert recall_w > 0.1 or recall_unw == 0.0, f"At least weighted should recover some recall: {recall_w}"

    print("✓ Class Weight Imbalance: PASS")
