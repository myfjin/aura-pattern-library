"""
CUPED (Controlled-experiment Using Pre-Experiment Data).

In A/B tests, Y_post = metric post-treatment, Y_pre = metric pre-treatment.
CUPED adjusted metric = Y_post - theta * Y_pre, where theta = Cov(Y_pre, Y_post) / Var(Y_pre).
This removes covariate-driven noise, reducing the variance of the treatment effect estimate.
We measure actual variance reduction from CUPED vs naive difference.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import math
from typing import List


def mean(values: List[float]) -> float:
    """Mean of a list."""
    return sum(values) / len(values)


def variance(values: List[float]) -> float:
    """Sample variance."""
    n = len(values)
    m = mean(values)
    return sum((v - m) ** 2 for v in values) / (n - 1)


def covariance(x: List[float], y: List[float]) -> float:
    """Sample covariance."""
    n = len(x)
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    return sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n)) / (n - 1)


if __name__ == "__main__":
    random.seed(42)

    n = 500
    true_effect = 0.5

    # Pre-period metric (baseline) for all units
    Y_pre = [random.gauss(100, 15) for _ in range(n)]

    # Split into control and treatment
    control_idx = list(range(n // 2))
    treatment_idx = list(range(n // 2, n))

    # Post-period: treatment group gets true_effect boost
    # Both groups' post-metrics are highly correlated with their pre-metrics (noise reduction)
    Y_post = [
        Y_pre[i] + true_effect + random.gauss(0, 5)
        if i in treatment_idx
        else Y_pre[i] + random.gauss(0, 5)
        for i in range(n)
    ]

    # Naive estimate: mean difference post-period
    y_post_treatment = [Y_post[i] for i in treatment_idx]
    y_post_control = [Y_post[i] for i in control_idx]
    naive_effect = mean(y_post_treatment) - mean(y_post_control)
    naive_variance = variance(y_post_treatment) + variance(y_post_control)

    # CUPED adjustment: estimate theta on control group (or pre-treatment data)
    y_pre_treatment = [Y_pre[i] for i in treatment_idx]
    y_pre_control = [Y_pre[i] for i in control_idx]

    # theta = Cov(pre, post) / Var(pre), estimated on control group
    theta = covariance(y_pre_control, y_post_control) / (
        variance(y_pre_control) + 1e-6
    )

    # Adjusted metrics: apply same theta to both groups
    adjusted_post_t = [y_post_treatment[i] - theta * y_pre_treatment[i]
                       for i in range(len(y_pre_treatment))]
    adjusted_post_c = [y_post_control[i] - theta * y_pre_control[i]
                       for i in range(len(y_pre_control))]

    cuped_effect = mean(adjusted_post_t) - mean(adjusted_post_c)
    cuped_variance = variance(adjusted_post_t) + variance(adjusted_post_c)

    # Check: CUPED variance should be smaller than naive variance
    variance_reduction = (naive_variance - cuped_variance) / naive_variance

    assert variance_reduction > 0.1, (
        f"CUPED variance reduction too small: {variance_reduction:.2%}"
    )
    assert abs(cuped_effect - true_effect) < abs(naive_effect - true_effect), (
        f"CUPED estimate {cuped_effect:.3f} not closer to true "
        f"{true_effect:.3f} than naive {naive_effect:.3f}"
    )

    print(
        f"True effect: {true_effect:.2f} | Naive: {naive_effect:.2f} (var={naive_variance:.2f}) | "
        f"CUPED: {cuped_effect:.2f} (var={cuped_variance:.2f}) | "
        f"Variance reduction: {variance_reduction:.1%} | PASS"
    )
