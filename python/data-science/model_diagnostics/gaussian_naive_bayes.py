"""
Gaussian Naive Bayes Classifier

Implements a Gaussian Naive Bayes classifier for continuous features.
Assumes each feature is independently distributed as Gaussian given the class label.

Use this for fast, interpretable classification on continuous data,
especially when feature independence is a reasonable assumption.
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

def _aura_validate_gaussian_probability(x, mean, std):
    v = []
    if isinstance(x, (int, float)) and not math.isfinite(x):
        v.append(f"AURA-E008: x must be finite, got {x}")
    if isinstance(mean, (int, float)) and not math.isfinite(mean):
        v.append(f"AURA-E008: mean must be finite, got {mean}")
    if isinstance(mean, (int, float)) and mean <= 0:
        v.append(f"AURA-E009: mean must be > 0, got {mean}")
    if isinstance(std, (int, float)) and not math.isfinite(std):
        v.append(f"AURA-E008: std must be finite, got {std}")
    if isinstance(std, (int, float)) and std < 0:
        v.append(f"AURA-E-B5: std must be >= 0, got {std}")
    if v:
        raise AuraInputError(v)

def _aura_validate_generate_gaussian_data(n_per_class):
    v = []
    if isinstance(n_per_class, (int, float)) and n_per_class <= 0:
        v.append(f"AURA-E009: n_per_class must be > 0, got {n_per_class}")
    if v:
        raise AuraInputError(v)

def generate_gaussian_data(
    n_per_class: int, seed: int
) -> Tuple[List[Tuple[float, float]], List[int]]:
    """
    Generate 2D Gaussian data for two classes.
    Class 0: mean=[0, 0], Class 1: mean=[3, 3].
    """
    _aura_validate_generate_gaussian_data(n_per_class)
    random.seed(seed)
    X = []
    y = []

    # Class 0
    for _ in range(n_per_class):
        x1 = random.gauss(0, 1)
        x2 = random.gauss(0, 1)
        X.append((x1, x2))
        y.append(0)

    # Class 1
    for _ in range(n_per_class):
        x1 = random.gauss(3, 1)
        x2 = random.gauss(3, 1)
        X.append((x1, x2))
        y.append(1)

    return X, y


def fit_gaussian_naive_bayes(
    X: List[Tuple[float, float]], y: List[int]
) -> Tuple[List[float], List[List[float]], List[List[float]], List[float]]:
    """
    Fit Gaussian Naive Bayes model.
    Returns (class_priors, means_per_class, stds_per_class, class_list).
    """
    classes = list(set(y))
    class_priors = []
    means_per_class = []
    stds_per_class = []

    n_samples = len(y)
    n_features = len(X[0]) if X else 0

    for cls in classes:
        # Count samples in this class
        indices = [i for i, label in enumerate(y) if label == cls]
        n_cls = len(indices)
        prior = n_cls / n_samples

        class_priors.append(prior)

        # Compute mean and std for each feature
        means = []
        stds = []
        for feat_idx in range(n_features):
            feat_values = [X[i][feat_idx] for i in indices]
            mean = sum(feat_values) / len(feat_values)
            variance = sum((v - mean) ** 2 for v in feat_values) / max(1, len(feat_values) - 1)
            std = math.sqrt(variance)

            means.append(mean)
            stds.append(std if std > 0 else 1e-6)

        means_per_class.append(means)
        stds_per_class.append(stds)

    return class_priors, means_per_class, stds_per_class, classes


def gaussian_probability(x: float, mean: float, std: float) -> float:
    """Compute Gaussian PDF at x."""
    _aura_validate_gaussian_probability(x, mean, std)
    if std == 0:
        return 0
    exponent = -((x - mean) ** 2) / (2 * std * std)
    return math.exp(exponent) / (math.sqrt(2 * math.pi) * std)


def predict_gaussian_naive_bayes(
    x_sample: Tuple[float, float],
    class_priors: List[float],
    means_per_class: List[List[float]],
    stds_per_class: List[List[float]],
    classes: List[int],
) -> int:
    """Predict class for a single sample."""
    posteriors = []

    for cls_idx, cls in enumerate(classes):
        prior = class_priors[cls_idx]
        means = means_per_class[cls_idx]
        stds = stds_per_class[cls_idx]

        posterior = prior
        for feat_idx, feat_val in enumerate(x_sample):
            posterior *= gaussian_probability(feat_val, means[feat_idx], stds[feat_idx])

        posteriors.append(posterior)

    return classes[posteriors.index(max(posteriors))]


def test_gaussian_naive_bayes() -> None:
    """Test GNB on well-separated 2D Gaussian data."""
    random.seed(42)

    # Generate training data
    X_train, y_train = generate_gaussian_data(100, seed=42)

    # Fit model
    class_priors, means_per_class, stds_per_class, classes = fit_gaussian_naive_bayes(X_train, y_train)

    # Generate test data
    X_test, y_test = generate_gaussian_data(100, seed=123)

    # Predict
    predictions = [
        predict_gaussian_naive_bayes(x, class_priors, means_per_class, stds_per_class, classes)
        for x in X_test
    ]

    # Compute accuracy
    correct = sum(1 for pred, true in zip(predictions, y_test) if pred == true)
    accuracy = correct / len(y_test)

    # For well-separated Gaussians, accuracy should be high
    assert accuracy >= 0.9, f"GNB accuracy should be >= 0.9: {accuracy}"

    print("gaussian_naive_bayes.py: PASS")


if __name__ == "__main__":
    test_gaussian_naive_bayes()
