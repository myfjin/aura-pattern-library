"""
Synthetic Control Method (Lite).

A treated unit's outcome is compared to a weighted average of control units.
Weights are chosen to match the treated unit's pre-intervention trends.
Post-intervention, any gap between treated and synthetic control is the treatment effect.
We plant pre-period trends and a treatment shock; SC recovers the gap.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
from typing import List, Tuple


def fit_weights(
    pre_treated: List[float], pre_controls: List[List[float]]
) -> List[float]:
    """
    Fit weights for control units to match pre-period trend of treated unit.
    Weights sum to 1. Use simple L2 minimization (gradient descent).
    """
    n_controls = len(pre_controls)
    n_periods = len(pre_treated)

    # Initialize equal weights
    weights = [1.0 / n_controls] * n_controls

    # Gradient descent to minimize SSE
    for _ in range(100):
        # Compute synthetic control
        synthetic = [
            sum(weights[j] * pre_controls[j][t] for j in range(n_controls))
            for t in range(n_periods)
        ]

        # Gradient
        grads = [0.0] * n_controls
        for j in range(n_controls):
            for t in range(n_periods):
                grads[j] += 2 * (synthetic[t] - pre_treated[t]) * pre_controls[j][t]

        # Update (with constraint to keep positive and sum to 1)
        step_size = 0.01
        for j in range(n_controls):
            weights[j] -= step_size * grads[j]

        # Normalize to sum to 1 and clip to non-negative
        total = sum(max(0, w) for w in weights)
        if total > 0:
            weights = [max(0, w) / total for w in weights]

    return weights


if __name__ == "__main__":
    random.seed(42)

    # Pre-intervention: 10 periods
    # Treated unit and 5 control units, all trending together
    n_periods_pre = 10
    n_controls = 5

    # Shared trend component
    trend = [t * 2.0 for t in range(n_periods_pre)]

    # Pre-period data for all units
    pre_treated = [trend[t] + random.gauss(0, 1) for t in range(n_periods_pre)]
    pre_controls = [
        [trend[t] + random.gauss(0, 1) for t in range(n_periods_pre)]
        for _ in range(n_controls)
    ]

    # Fit weights on pre-period
    weights = fit_weights(pre_treated, pre_controls)

    # Post-intervention: 10 periods
    # Treated unit gets a shock; controls continue the trend
    n_periods_post = 10
    treatment_shock = 5.0

    post_treated = [
        trend[n_periods_pre - 1] + (n_periods_pre + t) * 2.0 + treatment_shock
        + random.gauss(0, 1)
        for t in range(n_periods_post)
    ]
    post_controls = [
        [
            trend[n_periods_pre - 1] + (n_periods_pre + t) * 2.0 + random.gauss(0, 1)
            for t in range(n_periods_post)
        ]
        for _ in range(n_controls)
    ]

    # Synthetic control in post-period
    synthetic_post = [
        sum(weights[j] * post_controls[j][t] for j in range(n_controls))
        for t in range(n_periods_post)
    ]

    # SC estimate of treatment effect = mean gap in post-period
    gaps = [post_treated[t] - synthetic_post[t] for t in range(n_periods_post)]
    sc_effect = sum(gaps) / len(gaps)

    # Check: SC effect should be close to treatment shock
    bias = abs(sc_effect - treatment_shock)

    assert bias < 2.0, (
        f"SC estimate {sc_effect:.2f} too far from true shock "
        f"{treatment_shock:.2f} (bias={bias:.2f})"
    )
    assert all(w >= 0 for w in weights), "Weights should be non-negative"
    assert abs(sum(weights) - 1.0) < 0.01, "Weights should sum to 1"

    print(
        f"True shock: {treatment_shock:.2f} | SC estimate: {sc_effect:.2f} | "
        f"Bias: {bias:.2f} | Weights: {[f'{w:.2f}' for w in weights]} | PASS"
    )
