"""Post-stratification variance reduction: stratify AFTER observing data, using prognostic covariate.

On a prognostic covariate (correlated with outcome but NOT treated), stratifying reduces
ATE estimator variance. Core claim: post-stratifying on prognostic covariate cuts variance
by measured fraction vs simple difference-in-means.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
from typing import List, Tuple

def simple_ate(t: List[int], y: List[float]) -> Tuple[float, float]:
    """Compute ATE and its variance (naive estimate)."""
    y_t1 = [y[i] for i in range(len(t)) if t[i] == 1]
    y_t0 = [y[i] for i in range(len(t)) if t[i] == 0]

    ate = sum(y_t1) / len(y_t1) - sum(y_t0) / len(y_t0) if y_t1 and y_t0 else 0.0

    # Variance of ATE.
    var_t1 = sum((yi - sum(y_t1)/len(y_t1))**2 for yi in y_t1) / (len(y_t1) - 1) if len(y_t1) > 1 else 0.0
    var_t0 = sum((yi - sum(y_t0)/len(y_t0))**2 for yi in y_t0) / (len(y_t0) - 1) if len(y_t0) > 1 else 0.0
    var_ate = var_t1 / len(y_t1) + var_t0 / len(y_t0)

    return ate, var_ate

def post_stratified_ate(t: List[int], y: List[float], x: List[float]) -> Tuple[float, float]:
    """Post-stratify on x and compute weighted ATE and variance."""
    # Stratify on median.
    median_x = sorted(x)[len(x) // 2]
    strata = [0 if xi <= median_x else 1 for xi in x]

    total_n = len(t)
    ate_total = 0.0
    var_total = 0.0

    for s in [0, 1]:
        # Within-stratum ATE.
        indices_s = [i for i in range(len(t)) if strata[i] == s]
        t_s = [t[i] for i in indices_s]
        y_s = [y[i] for i in indices_s]

        y_t1 = [y_s[j] for j in range(len(y_s)) if t_s[j] == 1]
        y_t0 = [y_s[j] for j in range(len(y_s)) if t_s[j] == 0]

        if y_t1 and y_t0:
            ate_s = sum(y_t1) / len(y_t1) - sum(y_t0) / len(y_t0)
            weight_s = len(indices_s) / total_n
            ate_total += ate_s * weight_s

            # Stratum variance.
            var_t1 = sum((yi - sum(y_t1)/len(y_t1))**2 for yi in y_t1) / (len(y_t1) - 1) if len(y_t1) > 1 else 0.0
            var_t0 = sum((yi - sum(y_t0)/len(y_t0))**2 for yi in y_t0) / (len(y_t0) - 1) if len(y_t0) > 1 else 0.0
            var_s = (var_t1 / len(y_t1) + var_t0 / len(y_t0)) * (weight_s ** 2)
            var_total += var_s

    return ate_total, var_total

if __name__ == "__main__":
    import random
    random.seed(42)

    # Planted: outcome depends on prognostic covariate x.
    # x is NOT treated (prognostic, not effect-modifying).
    n = 200
    x = [random.gauss(0, 1) for _ in range(n)]
    t = [random.randint(0, 1) for _ in range(n)]

    # Outcome: depends on x (prognostic) and t (causal).
    true_effect = 2.0
    y = [true_effect * t[i] + 1.5 * x[i] + random.gauss(0, 0.3) for i in range(n)]

    # Simple ATE.
    ate_simple, var_simple = simple_ate(t, y)

    # Post-stratified ATE.
    ate_post, var_post = post_stratified_ate(t, y, x)

    # Both should estimate the same ATE (approximately).
    assert abs(ate_simple - ate_post) < 0.3, \
        f"Post-strat ATE {ate_post} should match simple {ate_simple}"

    # Post-stratified variance should be lower (variance reduction).
    assert var_post < var_simple, \
        f"Post-strat variance {var_post} should be < simple {var_simple}"

    # Variance reduction should be substantial (x is prognostic).
    reduction = (var_simple - var_post) / var_simple
    assert reduction > 0.15, f"Variance reduction {reduction} should be >15%"

    print("PASS")
