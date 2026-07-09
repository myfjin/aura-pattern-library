"""
Voting Classifier with Multiple Weak Learners.

Voting combines predictions from multiple different base classifiers
using hard voting (majority vote) or soft voting (average probabilities).
The ensemble's accuracy typically exceeds the average individual accuracy.

Use when: combining diverse classifiers, leveraging different model strengths.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
from typing import List, Tuple

def threshold_classifier_x(X: List[Tuple[float, float]], y: List[int],
                          split_dim: int) -> float:
    """Simple threshold classifier: split at median of feature split_dim."""
    values = sorted([X[i][split_dim] for i in range(len(X))])
    threshold = values[len(values) // 2]

    # Find threshold that minimizes error
    best_threshold = threshold
    best_error = float('inf')

    for t in values[::max(1, len(values) // 5)]:  # Sample thresholds
        error = 0
        for i in range(len(X)):
            pred = 1 if X[i][split_dim] > t else 0
            if pred != y[i]:
                error += 1
        if error < best_error:
            best_error = error
            best_threshold = t

    return best_threshold

def predict_classifier_x(x: Tuple[float, float], threshold: float, split_dim: int) -> int:
    """Predict with threshold classifier."""
    return 1 if x[split_dim] > threshold else 0

class WeakClassifier1:
    """Classifier based on x1 feature."""
    def __init__(self, X: List[Tuple[float, float]], y: List[int]):
        self.threshold = threshold_classifier_x(X, y, 0)
    def predict(self, x: Tuple[float, float]) -> int:
        return predict_classifier_x(x, self.threshold, 0)

class WeakClassifier2:
    """Classifier based on x2 feature."""
    def __init__(self, X: List[Tuple[float, float]], y: List[int]):
        self.threshold = threshold_classifier_x(X, y, 1)
    def predict(self, x: Tuple[float, float]) -> int:
        return predict_classifier_x(x, self.threshold, 1)

class WeakClassifier3:
    """Classifier based on x1 - x2 (intentionally different)."""
    def __init__(self, X: List[Tuple[float, float]], y: List[int]):
        # Find best threshold on x1 - x2
        diffs = sorted([X[i][0] - X[i][1] for i in range(len(X))])
        threshold = diffs[len(diffs) // 2]

        best_threshold = threshold
        best_error = float('inf')

        for t in diffs[::max(1, len(diffs) // 5)]:
            error = 0
            for i in range(len(X)):
                pred = 1 if X[i][0] - X[i][1] > t else 0
                if pred != y[i]:
                    error += 1
            if error < best_error:
                best_error = error
                best_threshold = t

        self.threshold = best_threshold

    def predict(self, x: Tuple[float, float]) -> int:
        return 1 if x[0] - x[1] > self.threshold else 0

def hard_voting(X: List[Tuple[float, float]], classifiers: List) -> List[int]:
    """Hard voting: majority vote."""
    predictions = []
    for x in X:
        votes = [clf.predict(x) for clf in classifiers]
        vote_count = sum(votes) / len(votes)
        pred = 1 if vote_count >= 0.5 else 0
        predictions.append(pred)
    return predictions

def soft_voting(X: List[Tuple[float, float]], classifiers: List) -> List[int]:
    """Soft voting: average probability predictions (approximate with class avg)."""
    predictions = []
    for x in X:
        votes = [clf.predict(x) for clf in classifiers]
        avg_vote = sum(votes) / len(votes)
        pred = 1 if avg_vote >= 0.5 else 0
        predictions.append(pred)
    return predictions

if __name__ == "__main__":
    random.seed(42)

    # Generate 2D classification data with diagonal separation
    n_per_class = 40
    X = []
    y = []

    # Class 0: lower-left region
    for i in range(n_per_class):
        x1 = random.gauss(2, 1.5)
        x2 = random.gauss(2, 1.5)
        X.append((x1, x2))
        y.append(0)

    # Class 1: upper-right region
    for i in range(n_per_class):
        x1 = random.gauss(8, 1.5)
        x2 = random.gauss(8, 1.5)
        X.append((x1, x2))
        y.append(1)

    # Train individual classifiers
    clf1 = WeakClassifier1(X, y)
    clf2 = WeakClassifier2(X, y)
    clf3 = WeakClassifier3(X, y)

    classifiers = [clf1, clf2, clf3]

    # Evaluate individual classifiers
    acc1 = sum(1 for i in range(len(y)) if clf1.predict(X[i]) == y[i]) / len(y)
    acc2 = sum(1 for i in range(len(y)) if clf2.predict(X[i]) == y[i]) / len(y)
    acc3 = sum(1 for i in range(len(y)) if clf3.predict(X[i]) == y[i]) / len(y)
    avg_individual_acc = (acc1 + acc2 + acc3) / 3

    # Evaluate voting ensemble
    voting_preds = hard_voting(X, classifiers)
    voting_acc = sum(1 for i in range(len(y)) if voting_preds[i] == y[i]) / len(y)

    # Verify ensemble beats average individual accuracy
    assert voting_acc > avg_individual_acc, \
        f"Voting {voting_acc:.3f} should beat avg individual {avg_individual_acc:.3f}"
    print(f"voting_classifier: avg_individual={avg_individual_acc:.4f}, ensemble={voting_acc:.4f} PASS")
