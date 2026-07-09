"""
Cross-validation data leakage from preprocessing before splitting.

Feature selection fit on the FULL dataset before train-test split leaks
information from test into train, inflating CV scores. Correct approach:
fit feature selection inside each fold on training data only.

Use: detecting CV score inflation, validating proper cross-validation pipelines.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import math


def univariate_correlation(X: list[list[float]], y: list[int]) -> list[float]:
    """
    Compute correlation between each feature and the target.
    Used for univariate feature selection.
    """
    n_features = len(X[0]) if X else 0
    correlations = []

    for j in range(n_features):
        x_j = [row[j] for row in X]
        mean_x = sum(x_j) / len(x_j) if x_j else 0
        mean_y = sum(y) / len(y) if y else 0

        cov = sum((x_j[i] - mean_x) * (y[i] - mean_y) for i in range(len(x_j))) / len(x_j)
        var_x = sum((xi - mean_x) ** 2 for xi in x_j) / len(x_j)
        var_y = sum((yi - mean_y) ** 2 for yi in y) / len(y)

        denom = math.sqrt(max(var_x * var_y, 1e-10))
        corr = cov / denom if denom > 0 else 0
        correlations.append(abs(corr))

    return correlations


def select_top_features(X: list[list[float]], y: list[int], k: int) -> list[int]:
    """
    Select top-k features by univariate correlation with target.
    LEAKY version: fits on all available data (before split).
    """
    correlations = univariate_correlation(X, y)
    feature_importance = [(j, correlations[j]) for j in range(len(correlations))]
    feature_importance.sort(key=lambda x: -x[1])
    return [j for j, _ in feature_importance[:k]]


def knn_classify(X_train: list[list[float]], y_train: list[int],
                 X_test: list[list[float]], k: int = 3) -> list[int]:
    """
    Simple k-NN classifier for speed in demo.
    Returns class predictions.
    """
    preds = []
    for x_test in X_test:
        distances = []
        for i, x_train in enumerate(X_train):
            dist = sum((xt - xtr) ** 2 for xt, xtr in zip(x_test, x_train)) ** 0.5
            distances.append((dist, y_train[i]))

        distances.sort()
        nearest_labels = [label for _, label in distances[:k]]
        pred = 1 if sum(nearest_labels) > k / 2 else 0
        preds.append(pred)

    return preds


def accuracy(y_true: list[int], y_pred: list[int]) -> float:
    """Accuracy."""
    correct = sum(1 for yt, yp in zip(y_true, y_pred) if yt == yp)
    return correct / len(y_true) if y_true else 0


if __name__ == "__main__":
    random.seed(42)

    # Generate data: 100 noise features + 5 weak true features (low signal)
    n_samples = 200
    n_noise = 100
    n_true = 5
    n_features = n_noise + n_true

    # Weak signal: y depends weakly on first 5 features
    X = []
    y = []
    for _ in range(n_samples):
        true_part = [random.gauss(0, 0.3) for _ in range(n_true)]
        noise_part = [random.gauss(0, 1) for _ in range(n_noise)]
        x = true_part + noise_part
        X.append(x)

        # y is mostly random but slightly correlated with first few features
        label = random.random() < 0.5
        if any(xi > 0.5 for xi in true_part):
            label = random.random() < 0.6  # Slightly higher prob if true_part large
        y.append(1 if label else 0)

    # Split into train/test manually (4-fold CV simulation)
    fold_size = n_samples // 4
    fold_accs_leaky = []
    fold_accs_correct = []

    for fold_idx in range(4):
        test_idx_start = fold_idx * fold_size
        test_idx_end = (fold_idx + 1) * fold_size

        X_test = X[test_idx_start:test_idx_end]
        y_test = y[test_idx_start:test_idx_end]
        X_train = X[:test_idx_start] + X[test_idx_end:]
        y_train = y[:test_idx_start] + y[test_idx_end:]

        # === LEAKY: select features on FULL dataset (includes test info) ===
        selected_features_leaky = select_top_features(X, y, k=10)
        X_train_leaky = [[x[j] for j in selected_features_leaky] for x in X_train]
        X_test_leaky = [[x[j] for j in selected_features_leaky] for x in X_test]

        preds_leaky = knn_classify(X_train_leaky, y_train, X_test_leaky, k=5)
        acc_leaky = accuracy(y_test, preds_leaky)
        fold_accs_leaky.append(acc_leaky)

        # === CORRECT: select features on TRAIN only ===
        selected_features_correct = select_top_features(X_train, y_train, k=10)
        X_train_correct = [[x[j] for j in selected_features_correct] for x in X_train]
        X_test_correct = [[x[j] for j in selected_features_correct] for x in X_test]

        preds_correct = knn_classify(X_train_correct, y_train, X_test_correct, k=5)
        acc_correct = accuracy(y_test, preds_correct)
        fold_accs_correct.append(acc_correct)

    mean_leaky = sum(fold_accs_leaky) / len(fold_accs_leaky)
    mean_correct = sum(fold_accs_correct) / len(fold_accs_correct)

    print(f"Leaky CV (select on full data):   {mean_leaky:.4f}")
    print(f"Correct CV (select on train):     {mean_correct:.4f}")
    print(f"Leakage inflation:                {mean_leaky - mean_correct:+.4f}")

    # Assert leakage is detectable
    assert mean_leaky > mean_correct, \
        f"Leaky {mean_leaky} should be > correct {mean_correct}"
    assert mean_leaky - mean_correct > 0.05, \
        f"Inflation {mean_leaky - mean_correct} too small to detect"

    print("\ncross_validation_leakage.py PASS")
