"""
Stacking Ensemble with Meta-Learner.

Stacking trains a meta-learner on predictions from base models trained
via out-of-fold cross-validation. The meta-learner learns to combine the
base models' strengths, often outperforming the base models individually.

Use when: combining diverse base models, high-dimensional feature space, complex patterns.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
from typing import List, Tuple

def fit_linear_model(X_base: List[List[float]], y: List[float]) -> Tuple[float, float]:
    """Fit simple linear meta-learner: y = b0 + b1*x1 + b2*x2."""
    n = len(X_base)
    if n == 0:
        return 0.0, [0.0, 0.0]

    # Simple linear fit (1D for demo)
    mean_x = sum(sum(x) for x in X_base) / (n * len(X_base[0])) if X_base[0] else 0
    mean_y = sum(y) / n

    # Fit to first base feature
    numerator = sum((X_base[i][0] - mean_x) * (y[i] - mean_y) for i in range(n))
    denominator = sum((X_base[i][0] - mean_x) ** 2 for i in range(n))

    b1 = numerator / denominator if denominator > 1e-10 else 0.0
    b0 = mean_y - b1 * mean_x

    return b0, [b1, 0.0]

def predict_linear(X: List[float], b0: float, coef: List[float]) -> float:
    """Predict with linear meta-learner."""
    return b0 + sum(X[i] * coef[i] for i in range(len(coef)))

class BaseModel1:
    """Simple threshold classifier on x[0]."""
    def __init__(self):
        self.threshold = None

    def fit(self, X: List[Tuple[float, float]], y: List[int]):
        values = sorted([X[i][0] for i in range(len(X))])
        self.threshold = values[len(values) // 2]

    def predict(self, X: List[Tuple[float, float]]) -> List[float]:
        return [1.0 if x[0] > self.threshold else 0.0 for x in X]

class BaseModel2:
    """Simple threshold classifier on x[1]."""
    def __init__(self):
        self.threshold = None

    def fit(self, X: List[Tuple[float, float]], y: List[int]):
        values = sorted([X[i][1] for i in range(len(X))])
        self.threshold = values[len(values) // 2]

    def predict(self, X: List[Tuple[float, float]]) -> List[float]:
        return [1.0 if x[1] > self.threshold else 0.0 for x in X]

def generate_base_predictions(X: List[Tuple[float, float]], y: List[int],
                              base_models: List, k_folds: int = 5) -> List[List[float]]:
    """Generate out-of-fold predictions for meta-learner training."""
    n = len(X)
    fold_size = n // k_folds
    meta_features = [[0.0] * len(base_models) for _ in range(n)]

    for fold in range(k_folds):
        # Split data
        val_start = fold * fold_size
        val_end = val_start + fold_size if fold < k_folds - 1 else n

        X_train = X[:val_start] + X[val_end:]
        y_train = y[:val_start] + y[val_end:]
        X_val = X[val_start:val_end]

        # Train base models on this fold
        for model_idx, model in enumerate(base_models):
            model.fit(X_train, y_train)
            preds = model.predict(X_val)
            for i, val_idx in enumerate(range(val_start, val_end)):
                meta_features[val_idx][model_idx] = preds[i]

    return meta_features

def fit_stacking(X: List[Tuple[float, float]], y: List[int],
                 base_models: List, k_folds: int = 5) -> Tuple[List, float, List[float]]:
    """Fit stacking ensemble with meta-learner."""
    # Generate out-of-fold predictions
    meta_X = generate_base_predictions(X, y, base_models, k_folds)

    # Train meta-learner on out-of-fold predictions
    b0, coef = fit_linear_model(meta_X, [float(label) for label in y])

    return base_models, b0, coef

def predict_stacking(X: List[Tuple[float, float]], base_models: List,
                     b0: float, coef: List[float]) -> List[int]:
    """Predict with stacking ensemble."""
    # Get base predictions
    base_preds = []
    for model in base_models:
        preds = model.predict(X)
        base_preds.append(preds)

    # Apply meta-learner
    predictions = []
    for i in range(len(X)):
        meta_input = [base_preds[j][i] for j in range(len(base_models))]
        meta_pred = predict_linear(meta_input, b0, coef)
        predictions.append(1 if meta_pred >= 0.5 else 0)

    return predictions

if __name__ == "__main__":
    random.seed(42)

    # Generate classification data
    n_per_class = 50
    X = []
    y = []

    for i in range(n_per_class):
        x1 = random.gauss(2, 2.5)
        x2 = random.gauss(2, 2.5)
        X.append((x1, x2))
        y.append(0)

    for i in range(n_per_class):
        x1 = random.gauss(8, 2.5)
        x2 = random.gauss(8, 2.5)
        X.append((x1, x2))
        y.append(1)

    # Split into train and test
    n_train = int(0.7 * len(X))
    X_train = X[:n_train]
    y_train = y[:n_train]
    X_test = X[n_train:]
    y_test = y[n_train:]

    # Initialize base models
    base_model1 = BaseModel1()
    base_model2 = BaseModel2()
    base_models = [base_model1, base_model2]

    # Fit base models on training data
    base_model1.fit(X_train, y_train)
    base_model2.fit(X_train, y_train)

    # Evaluate base models on test set
    base1_preds_test = base_model1.predict(X_test)
    base1_acc = sum(1 for i in range(len(y_test)) if (1 if base1_preds_test[i] >= 0.5 else 0) == y_test[i]) / len(y_test)

    base2_preds_test = base_model2.predict(X_test)
    base2_acc = sum(1 for i in range(len(y_test)) if (1 if base2_preds_test[i] >= 0.5 else 0) == y_test[i]) / len(y_test)

    # Fit stacking on training data
    _, b0, coef = fit_stacking(X_train, y_train, base_models, k_folds=5)

    # Predict with stacking on test set
    stack_preds = predict_stacking(X_test, base_models, b0, coef)
    stack_acc = sum(1 for i in range(len(y_test)) if stack_preds[i] == y_test[i]) / len(y_test)

    # Verify stacking beats average of base models
    avg_base_acc = (base1_acc + base2_acc) / 2
    assert stack_acc > avg_base_acc, f"Stacking {stack_acc:.3f} should beat avg base {avg_base_acc:.3f}"
    print(f"stacking_ensemble: base1_acc={base1_acc:.4f}, base2_acc={base2_acc:.4f}, stack_acc={stack_acc:.4f} PASS")
