"""
Bagging for Variance Reduction.

Bagging (bootstrap aggregating) trains many copies of an UNSTABLE base learner
on bootstrap resamples and averages them. The averaged predictor has markedly
lower variance across retrainings than a single base learner — that reduction,
measured at fixed test points over many independent training draws, is the
whole point of the method. (A stable learner like plain linear regression
barely benefits; instability is bagging's fuel.)

Use when: high-variance base learners (deep trees, stumps on small data),
prediction stability across retrainings matters.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import statistics
from typing import Callable, List, Tuple

Stump = Tuple[float, float, float]  # (threshold, left_mean, right_mean)


def true_fn(x: float) -> float:
    return 2.0 * x




class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_make_training_set(n):
    v = []
    if isinstance(n, (int, float)) and n <= 0:
        v.append(f"AURA-E009: n must be > 0, got {n}")
    if v:
        raise AuraInputError(v)

def make_training_set(n: int) -> Tuple[List[float], List[float]]:
    _aura_validate_make_training_set(n)
    X = [random.uniform(0.0, 10.0) for _ in range(n)]
    y = [true_fn(x) + random.gauss(0.0, 3.0) for x in X]
    return X, y


def fit_stump(X: List[float], y: List[float]) -> Stump:
    """Regression stump: best single split by SSE — deliberately UNSTABLE
    under resampling (small perturbations move the threshold a lot)."""
    order = sorted(range(len(X)), key=lambda i: X[i])
    xs = [X[i] for i in order]
    ys = [y[i] for i in order]
    n = len(xs)
    best = (float("inf"), xs[n // 2], 0.0, 0.0)
    prefix = [0.0]
    prefix_sq = [0.0]
    for v in ys:
        prefix.append(prefix[-1] + v)
        prefix_sq.append(prefix_sq[-1] + v * v)
    for k in range(1, n):  # split between k-1 and k
        nl, nr = k, n - k
        sl, sr = prefix[k], prefix[n] - prefix[k]
        ssl = prefix_sq[k] - sl * sl / nl
        ssr = (prefix_sq[n] - prefix_sq[k]) - sr * sr / nr
        sse = ssl + ssr
        if sse < best[0]:
            best = (sse, (xs[k - 1] + xs[k]) / 2.0, sl / nl, sr / nr)
    _, thr, lm, rm = best
    return thr, lm, rm


def predict_stump(x: float, s: Stump) -> float:
    thr, lm, rm = s
    return lm if x <= thr else rm


def fit_bagged(X: List[float], y: List[float], n_models: int = 25) -> List[Stump]:
    models = []
    n = len(X)
    for _ in range(n_models):
        idx = [random.randint(0, n - 1) for _ in range(n)]
        models.append(fit_stump([X[i] for i in idx], [y[i] for i in idx]))
    return models


def predict_bagged(x: float, models: List[Stump]) -> float:
    return sum(predict_stump(x, m) for m in models) / len(models)


if __name__ == "__main__":
    random.seed(42)

    # Bias–variance protocol: draw R INDEPENDENT training sets; each time fit
    # (a) one stump and (b) a bagged ensemble of 25 stumps; record predictions
    # at FIXED test points. Variance across the R retrainings, averaged over
    # the test points, is the quantity bagging reduces.
    R = 30
    test_points = [1.0, 3.0, 5.0, 7.0, 9.0]
    single_preds: List[List[float]] = [[] for _ in test_points]
    bagged_preds: List[List[float]] = [[] for _ in test_points]

    for _ in range(R):
        X, y = make_training_set(60)
        stump = fit_stump(X, y)
        ensemble = fit_bagged(X, y, n_models=25)
        for j, x0 in enumerate(test_points):
            single_preds[j].append(predict_stump(x0, stump))
            bagged_preds[j].append(predict_bagged(x0, ensemble))

    single_var = statistics.mean(statistics.variance(p) for p in single_preds)
    bagged_var = statistics.mean(statistics.variance(p) for p in bagged_preds)

    # The reduction must be SUBSTANTIAL, not merely directional.
    assert bagged_var < 0.5 * single_var, (
        f"bagging should cut retraining variance at least in half: "
        f"single {single_var:.3f} vs bagged {bagged_var:.3f}"
    )
    print(f"bagging_variance_reduction: retraining variance {single_var:.3f} -> "
          f"{bagged_var:.3f} ({bagged_var / single_var:.0%} of single) PASS")
