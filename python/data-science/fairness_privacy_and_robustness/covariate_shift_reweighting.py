"""Covariate Shift Reweighting: correct train/test distribution mismatch.

Plants a covariate shift between train and test sets, estimates importance weights
from density ratio, and shows that reweighting corrects the bias while unweighted
model remains biased.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import random
import math
from typing import List, Tuple

def covariate_shift_reweighting() -> None:
    random.seed(42)

    # Train set: features from N(0, 1)
    n_train = 200
    X_train = [random.gauss(0, 1) for _ in range(n_train)]
    # True model: y = 2*x + noise
    y_train = [2 * x + random.gauss(0, 0.5) for x in X_train]

    # Test set: covariate shift — features from N(2, 1) (shifted right)
    n_test = 200
    X_test = [random.gauss(2, 1) for _ in range(n_test)]
    y_test = [2 * x + random.gauss(0, 0.5) for x in X_test]

    # Train unweighted model (linear regression)
    def linear_regression(X: List[float], y: List[float], weights: List[float] = None) -> Tuple[float, float]:
        n = len(X)
        if weights is None:
            weights = [1.0] * n

        sum_w = sum(weights)
        sum_wx = sum(w * x for w, x in zip(weights, X))
        sum_wy = sum(w * y_val for w, y_val in zip(weights, y))
        sum_wxx = sum(w * x * x for w, x in zip(weights, X))
        sum_wxy = sum(w * x * y_val for w, x, y_val in zip(weights, X, y))

        denom = sum_w * sum_wxx - sum_wx * sum_wx
        if abs(denom) < 1e-10:
            return 0, 0

        slope = (sum_w * sum_wxy - sum_wx * sum_wy) / denom
        intercept = (sum_wy - slope * sum_wx) / sum_w
        return slope, intercept

    slope_unweighted, intercept_unweighted = linear_regression(X_train, y_train)

    # Estimate importance weights via density ratio
    # p_test(x) / p_train(x): test is N(2,1), train is N(0,1)
    # For Gaussians: ratio = exp(-(x-2)^2/2 + x^2/2) = exp(2x - 2)
    importance_weights = [math.exp(2 * x - 2) for x in X_train]

    slope_weighted, intercept_weighted = linear_regression(X_train, y_train, importance_weights)

    # Evaluate MSE on test set
    def mse(X: List[float], y: List[float], slope: float, intercept: float) -> float:
        pred = [slope * x + intercept for x in X]
        return sum((p - true_y) ** 2 for p, true_y in zip(pred, y)) / len(X)

    mse_unweighted = mse(X_test, y_test, slope_unweighted, intercept_unweighted)
    mse_weighted = mse(X_test, y_test, slope_weighted, intercept_weighted)

    # Weighted should perform better (lower MSE)
    assert mse_weighted < mse_unweighted, (
        f"Weighted MSE ({mse_weighted:.3f}) should be < "
        f"unweighted MSE ({mse_unweighted:.3f})"
    )

    print("PASS")

if __name__ == "__main__":
    covariate_shift_reweighting()
