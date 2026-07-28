"""
Train/Test Split and K-Fold Cross-Validation

Core idea: Split data into train/test subsets for model evaluation. Extend to k-fold CV
where data is divided into k folds; iterate k times, using each fold as test and the rest
for training, then average results.

When to use: Evaluate model performance with limited data, avoid overfitting estimates,
and get stable generalization metrics.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
from typing import List, Tuple




class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_train_test_split(test_size):
    v = []
    if isinstance(test_size, (int, float)) and test_size <= 0:
        v.append(f"AURA-E009: test_size must be > 0, got {test_size}")
    if v:
        raise AuraInputError(v)

def train_test_split(data: List, labels: List, test_size: float = 0.2) -> Tuple[List, List, List, List]:
    """
    Split data into train and test sets.

    Args:
        data: Feature samples.
        labels: Corresponding labels.
        test_size: Fraction to reserve for test (0 < test_size < 1).

    Returns:
        Tuple of (X_train, X_test, y_train, y_test).
    """
    _aura_validate_train_test_split(test_size)
    n = len(data)
    test_count = int(n * test_size)
    indices = list(range(n))
    random.shuffle(indices)

    test_indices = indices[:test_count]
    train_indices = indices[test_count:]

    X_train = [data[i] for i in train_indices]
    X_test = [data[i] for i in test_indices]
    y_train = [labels[i] for i in train_indices]
    y_test = [labels[i] for i in test_indices]

    return X_train, X_test, y_train, y_test


def kfold_split(data: List, labels: List, k: int = 5) -> List[Tuple[List, List, List, List]]:
    """
    Generate k-fold cross-validation splits.

    Args:
        data: Feature samples.
        labels: Corresponding labels.
        k: Number of folds.

    Returns:
        List of k tuples, each (X_train, X_test, y_train, y_test) for one fold.
    """
    n = len(data)
    fold_size = n // k
    indices = list(range(n))
    random.shuffle(indices)

    folds = []
    for fold_idx in range(k):
        test_start = fold_idx * fold_size
        test_end = test_start + fold_size
        if fold_idx == k - 1:
            # Last fold gets any remainder
            test_end = n

        test_indices = set(indices[test_start:test_end])
        train_indices = [i for i in indices if i not in test_indices]

        X_train = [data[i] for i in train_indices]
        X_test = [data[i] for i in test_indices]
        y_train = [labels[i] for i in train_indices]
        y_test = [labels[i] for i in test_indices]

        folds.append((X_train, X_test, y_train, y_test))

    return folds


def simple_mean_predictor(X_train: List, y_train: List) -> float:
    """Train a trivial model: predict the mean of y_train."""
    return sum(y_train) / len(y_train) if y_train else 0.0


def mean_squared_error(y_true: List, y_pred: List) -> float:
    """Compute mean squared error."""
    if len(y_true) == 0:
        return 0.0
    return sum((y_true[i] - y_pred[i]) ** 2 for i in range(len(y_true))) / len(y_true)


if __name__ == "__main__":
    random.seed(42)

    # Generate synthetic regression data: y ≈ 2*x + noise
    X = [i / 10.0 for i in range(100)]
    y = [2 * x + random.gauss(0, 1) for x in X]

    # Test train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    assert len(X_train) + len(X_test) == len(X), "Split must partition all data"
    assert len(X_test) == int(len(X) * 0.2), "Test size should match"
    print(f"Train/test split: train={len(X_train)}, test={len(X_test)}")

    # Train and evaluate simple predictor on train/test
    pred_value = simple_mean_predictor(X_train, y_train)
    y_test_pred = [pred_value] * len(y_test)
    mse_test = mean_squared_error(y_test, y_test_pred)
    print(f"Train/test MSE: {mse_test:.3f}")

    # Test k-fold cross-validation
    folds = kfold_split(X, y, k=5)
    assert len(folds) == 5, "Should have 5 folds"

    mse_scores = []
    for fold_idx, (X_tr, X_te, y_tr, y_te) in enumerate(folds):
        pred_val = simple_mean_predictor(X_tr, y_tr)
        y_te_pred = [pred_val] * len(y_te)
        mse = mean_squared_error(y_te, y_te_pred)
        mse_scores.append(mse)

    avg_mse = sum(mse_scores) / len(mse_scores)
    print(f"5-Fold CV MSE (avg): {avg_mse:.3f}, scores: {[f'{m:.3f}' for m in mse_scores]}")

    # Assertions
    assert all(len(X_tr) + len(X_te) == len(X) for X_tr, X_te, _, _ in folds), "Each fold must partition data"
    assert 0 < avg_mse < 100, "MSE should be positive and reasonable"

    print("✓ Train/test split and k-fold CV PASSED")
