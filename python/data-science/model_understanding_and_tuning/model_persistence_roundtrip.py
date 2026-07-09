"""
Model Persistence Roundtrip (Save and Reload)

Core idea: Train a model, serialize it to JSON, reload it, and verify predictions are
identical (bit-for-bit for floats, or within machine epsilon).

When to use: You need to confirm that model serialization/deserialization preserves all
parameters and produces deterministic predictions on new data.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import json
import random
from typing import List, Tuple, Dict, Any


class SimpleLinearModel:
    """A minimal linear regression model: y = intercept + sum(weights[i] * x[i])."""

    def __init__(self, intercept: float = 0.0, weights: List[float] = None):
        self.intercept = intercept
        self.weights = weights or []

    def predict(self, X: List[List[float]]) -> List[float]:
        """Predict on batch of samples."""
        predictions = []
        for x in X:
            pred = self.intercept + sum(w * val for w, val in zip(self.weights, x))
            predictions.append(pred)
        return predictions

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to dictionary."""
        return {
            "intercept": self.intercept,
            "weights": self.weights,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "SimpleLinearModel":
        """Deserialize from dictionary."""
        return cls(intercept=data["intercept"], weights=data["weights"])


def fit_linear_model(X: List[List[float]], y: List[float]) -> SimpleLinearModel:
    """Fit linear model via least squares."""
    n = len(X)
    num_features = len(X[0])

    # Compute means
    x_means = [sum(X[i][j] for i in range(n)) / n for j in range(num_features)]
    y_mean = sum(y) / n

    # Compute correlations and variances
    weights = []
    for j in range(num_features):
        cov_xy = sum((X[i][j] - x_means[j]) * (y[i] - y_mean) for i in range(n)) / n
        var_x = sum((X[i][j] - x_means[j]) ** 2 for i in range(n)) / n
        w = cov_xy / var_x if var_x > 0 else 0.0
        weights.append(w)

    intercept = y_mean - sum(w * xm for w, xm in zip(weights, x_means))

    return SimpleLinearModel(intercept=intercept, weights=weights)


if __name__ == "__main__":
    random.seed(42)

    # Generate synthetic data
    X_train = []
    y_train = []
    for _ in range(100):
        x1 = random.uniform(-2, 2)
        x2 = random.uniform(-2, 2)
        x3 = random.uniform(-2, 2)
        y = 10 + 2 * x1 - 1.5 * x2 + 0.5 * x3 + random.gauss(0, 0.1)
        X_train.append([x1, x2, x3])
        y_train.append(y)

    # Train model
    model = fit_linear_model(X_train, y_train)
    print(f"Trained model: intercept={model.intercept:.6f}, weights={[f'{w:.6f}' for w in model.weights]}")

    # Generate test data
    X_test = []
    for _ in range(20):
        x = [random.uniform(-2, 2) for _ in range(3)]
        X_test.append(x)

    # Original predictions
    preds_original = model.predict(X_test)

    # Serialize to JSON
    model_dict = model.to_dict()
    json_str = json.dumps(model_dict)
    print(f"Serialized: {json_str[:50]}...")

    # Deserialize from JSON
    model_dict_loaded = json.loads(json_str)
    model_loaded = SimpleLinearModel.from_dict(model_dict_loaded)

    # Predictions after roundtrip
    preds_loaded = model_loaded.predict(X_test)

    # Compare predictions
    max_diff = max(abs(p1 - p2) for p1, p2 in zip(preds_original, preds_loaded))
    print(f"Max prediction difference after roundtrip: {max_diff:.2e}")

    # Assertion: predictions should be identical (within machine epsilon)
    for p1, p2 in zip(preds_original, preds_loaded):
        assert abs(p1 - p2) < 1e-10, f"Prediction mismatch: {p1} vs {p2}"

    assert model.intercept == model_loaded.intercept, "Intercept mismatch"
    assert model.weights == model_loaded.weights, "Weights mismatch"

    print("✓ Model Persistence Roundtrip: PASS")
