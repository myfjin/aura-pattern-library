"""
Feature hashing for dimensionality reduction of high-dimensional sparse features.

Hash trick maps unbounded categorical/text features to a fixed number of
dimensions via hashing. Trade-off: reduces memory/computation but introduces
collisions. Deterministic, works online, and maintains separability for
classification tasks.

Use: text/NLP feature extraction, streaming data, memory-constrained settings.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
import hashlib
from collections import defaultdict


def hash_feature(feature_name: str, n_dims: int) -> int:
    """
    Hash feature name to bin in [0, n_dims-1].
    Uses SHA-256 for good distribution.
    """
    h = hashlib.sha256(feature_name.encode()).digest()
    # Convert first 8 bytes to int, mod n_dims
    hash_int = int.from_bytes(h[:8], byteorder='big')
    return hash_int % n_dims


def hash_vectorize_text(texts: list[str], n_dims: int = 128) -> list[list[float]]:
    """
    Convert text documents to hash-trick feature vectors.
    Each word gets hashed to a dimension; count occurrences.
    Returns n_dims-dimensional vectors.
    """
    vectors = []
    for text in texts:
        words = text.lower().split()
        feature_vec = [0.0] * n_dims

        for word in words:
            dim = hash_feature(word, n_dims)
            feature_vec[dim] += 1.0

        vectors.append(feature_vec)

    return vectors


def dot_product(v1: list[float], v2: list[float]) -> float:
    """Compute dot product of two vectors."""
    return sum(a * b for a, b in zip(v1, v2))




class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_simple_linear_classifier(iterations):
    v = []
    if isinstance(iterations, (int, float)) and iterations <= 0:
        v.append(f"AURA-E009: iterations must be > 0, got {iterations}")
    if v:
        raise AuraInputError(v)

def simple_linear_classifier(X_train: list[list[float]], y_train: list[int],
                             X_test: list[list[float]],
                             iterations: int = 100) -> list[float]:
    """
    Train a simple linear classifier via stochastic gradient descent.
    Return soft predictions.
    """
    _aura_validate_simple_linear_classifier(iterations)
    n_features = len(X_train[0]) if X_train else 0
    weights = [0.0] * n_features

    for _ in range(iterations):
        for x, y in zip(X_train, y_train):
            # Logistic regression update
            z = dot_product(x, weights)
            pred = 1.0 / (1.0 + (2.718281828 ** min(100, -z)))
            error = pred - y
            lr = 0.01

            for i in range(n_features):
                weights[i] -= lr * error * x[i] / len(X_train)

    # Predict
    preds = []
    for x in X_test:
        z = dot_product(x, weights)
        pred = 1.0 / (1.0 + (2.718281828 ** min(100, -z)))
        preds.append(pred)

    return preds


def accuracy(y_true: list[int], y_pred: list[float]) -> float:
    """Binary accuracy."""
    correct = sum(1 for yt, yp in zip(y_true, y_pred) if (yp > 0.5) == (yt == 1))
    return correct / len(y_true) if y_true else 0


def collision_rate(texts: list[str], n_dims: int) -> float:
    """
    Estimate collision rate: fraction of feature hash collisions.
    Computed as 1 - (unique_dims / unique_words).
    """
    unique_words = set()
    for text in texts:
        unique_words.update(text.lower().split())

    dims_used = set()
    for word in unique_words:
        dim = hash_feature(word, n_dims)
        dims_used.add(dim)

    collision_rate_val = 1.0 - (len(dims_used) / len(unique_words)) if unique_words else 0
    return collision_rate_val


if __name__ == "__main__":
    import random
    random.seed(42)

    # Synthetic text classification: spam (negative) vs ham (positive)
    # Spam texts have "FREE", "WINNER", "CLICK"; ham texts have "meeting", "report"

    spam_texts = [
        "FREE MONEY WINNER CLICK HERE",
        "YOU WON CLAIM PRIZE NOW",
        "FREE FREE CLICK WINNER",
        "CLICK HERE FREE MONEY NOW",
        "PRIZE CLICK WINNER CLAIM",
    ]

    ham_texts = [
        "meeting tomorrow at office",
        "quarterly report attached",
        "team lunch next week",
        "project update status meeting",
        "report meeting schedule next",
    ]

    # Create balanced training set
    y_train = [0] * 5 + [1] * 5
    X_texts_train = spam_texts + ham_texts

    # Create test set (unseen combinations)
    spam_test = [
        "FREE WINNER CLICK MONEY",
        "CLICK PRIZE FREE NOW",
    ]
    ham_test = [
        "meeting report schedule",
        "office tomorrow project",
    ]

    y_test = [0] * 2 + [1] * 2
    X_texts_test = spam_test + ham_test

    # Test with different hash dimensions
    dimensions = [32, 64, 128]
    results = []

    print("Feature hashing classification performance")
    print()

    for n_dims in dimensions:
        # Vectorize
        X_train = hash_vectorize_text(X_texts_train, n_dims)
        X_test = hash_vectorize_text(X_texts_test, n_dims)

        # Train and evaluate
        preds = simple_linear_classifier(X_train, y_train, X_test, iterations=200)
        acc = accuracy(y_test, preds)

        # Compute collision rate
        all_texts = X_texts_train + X_texts_test
        collisions = collision_rate(all_texts, n_dims)

        results.append((n_dims, acc, collisions))

        print(f"Dimensions: {n_dims}")
        print(f"  Accuracy:       {acc:.4f}")
        print(f"  Collision rate: {collisions:.4f}")
        print()

    # Assertions: determinism, accuracy, collision rate
    # Recompute with same seed to verify determinism
    random.seed(42)
    X_train_repeat = hash_vectorize_text(X_texts_train, 64)
    preds_repeat = simple_linear_classifier(X_train_repeat, y_train,
                                            hash_vectorize_text(X_texts_test, 64),
                                            iterations=200)
    acc_repeat = accuracy(y_test, preds_repeat)

    # Determinism check
    assert abs(acc_repeat - results[1][1]) < 1e-6, "Determinism failed"

    # Classification should work (reasonably)
    assert results[1][1] > 0.5, f"Accuracy {results[1][1]} should beat chance"

    # Collision rate should increase with smaller dimensions
    assert results[0][2] > results[2][2], \
        f"32-dim collisions {results[0][2]} should > 128-dim {results[2][2]}"

    print("Feature hashing verification:")
    print(f"  Determinism: PASS")
    print(f"  Classification: PASS (accuracy {results[1][1]:.4f} > 0.5)")
    print(f"  Dimension-collision tradeoff: PASS")

    print("\nfeature_hashing_trick.py PASS")
