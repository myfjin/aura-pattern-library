"""Fixed-effects estimator (within): removes time-invariant entity effects.

Panel data: y_it = α_i + β·x_it + ε_it. Within-estimator demeansdata per
entity, eliminating α_i. Core claim: pooled OLS biased, within unbiased.
Planted panel with entity effects.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
from typing import List, Tuple

def pooled_ols(y: List[float], x: List[float]) -> float:
    """Naive pooled OLS regression: y ~ x."""
    n = len(y)
    mean_x = sum(x) / n
    mean_y = sum(y) / n

    cov = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n)) / n
    var_x = sum((x[i] - mean_x)**2 for i in range(n)) / n

    return cov / var_x if var_x > 1e-14 else 0.0

def within_estimator(y: List[List[float]], x: List[List[float]]) -> float:
    """Within (fixed-effects) estimator: demean within each entity.

    y[i][t] = y-values for entity i at times t.
    x[i][t] = x-values for entity i at times t.
    """
    num_entities = len(y)
    y_demeaned = []
    x_demeaned = []

    for i in range(num_entities):
        mean_y_i = sum(y[i]) / len(y[i])
        mean_x_i = sum(x[i]) / len(x[i])

        for t in range(len(y[i])):
            y_demeaned.append(y[i][t] - mean_y_i)
            x_demeaned.append(x[i][t] - mean_x_i)

    return pooled_ols(y_demeaned, x_demeaned)

if __name__ == "__main__":
    import random
    random.seed(42)

    # Planted: panel with 15 entities, 6 periods. y_it = α_i + 0.5·x_it + ε.
    # CRUCIAL: x_it is CORRELATED with the entity effect (x_it = 0.6·α_i + noise).
    # That correlation — not the size of α — is what biases pooled OLS (omitted-variable
    # bias). The within estimator demeans α_i away and recovers the truth. (An x drawn
    # independent of α would leave pooled UNbiased and the demo would prove nothing.)
    num_entities = 15
    num_periods = 6

    alpha = [random.gauss(0, 3) for _ in range(num_entities)]
    beta_true = 0.5

    y_flat = []
    x_flat = []
    y_panel = []
    x_panel = []

    for i in range(num_entities):
        y_i = []
        x_i = []
        for t in range(num_periods):
            x_it = 0.6 * alpha[i] + random.gauss(0, 1)  # regressor correlated with entity effect
            y_it = alpha[i] + beta_true * x_it + random.gauss(0, 0.5)

            y_flat.append(y_it)
            x_flat.append(x_it)
            y_i.append(y_it)
            x_i.append(x_it)

        y_panel.append(y_i)
        x_panel.append(x_i)

    beta_pooled = pooled_ols(y_flat, x_flat)
    beta_within = within_estimator(y_panel, x_panel)

    # Defining property: within recovers β≈0.5; pooled is badly biased UPWARD by the
    # omitted, x-correlated entity effect. Measured (seed 42): within≈0.53, pooled≈1.47.
    assert abs(beta_within - beta_true) < 0.3, \
        f"Within estimator {beta_within} should recover {beta_true}"
    assert beta_pooled > beta_true + 0.5, \
        f"Pooled estimator {beta_pooled} should be biased well above {beta_true}"
    assert abs(beta_within - beta_true) < abs(beta_pooled - beta_true), \
        f"Within ({beta_within}) should beat pooled ({beta_pooled}) on bias"

    print("PASS")
