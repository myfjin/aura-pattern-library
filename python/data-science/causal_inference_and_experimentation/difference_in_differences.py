"""
Difference-in-Differences (DiD).

Two groups (treated and control) observed before and after treatment.
Parallel trends assumption: absent treatment, both groups would have the same trend.
DiD estimate = (Y_treated_post - Y_treated_pre) - (Y_control_post - Y_control_pre).
We plant parallel trends and a treatment effect; DiD recovers the effect.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
from typing import List, Tuple


def simulate_did_data(
    n_per_group: int, treatment_effect: float, time_effect: float
) -> Tuple[List[float], List[float], List[float], List[float]]:
    """
    Generate two groups with parallel trends, treatment applied to group 1 post-period.
    Returns: (pre_control, post_control, pre_treated, post_treated).
    """
    pre_control = [random.gauss(100, 10) for _ in range(n_per_group)]
    pre_treated = [random.gauss(100, 10) for _ in range(n_per_group)]

    # Post-period: both groups trend up by time_effect (parallel trends)
    # Treated group also gets treatment_effect
    post_control = [y + time_effect + random.gauss(0, 10) for y in pre_control]
    post_treated = [
        y + time_effect + treatment_effect + random.gauss(0, 10)
        for y in pre_treated
    ]

    return pre_control, post_control, pre_treated, post_treated


def mean(values: List[float]) -> float:
    """Mean of a list."""
    return sum(values) / len(values)


def estimate_did(
    pre_control: List[float],
    post_control: List[float],
    pre_treated: List[float],
    post_treated: List[float],
) -> float:
    """
    DiD estimator: (post_treated - pre_treated) - (post_control - pre_control).
    """
    treated_change = mean(post_treated) - mean(pre_treated)
    control_change = mean(post_control) - mean(pre_control)
    return treated_change - control_change


if __name__ == "__main__":
    random.seed(42)

    # Generate data with known treatment effect = 20 and time trend = 5
    treatment_effect = 20.0
    time_trend = 5.0

    pre_c, post_c, pre_t, post_t = simulate_did_data(100, treatment_effect, time_trend)

    # DiD estimate
    did_estimate = estimate_did(pre_c, post_c, pre_t, post_t)

    # Check: estimate should be close to true treatment effect
    bias = abs(did_estimate - treatment_effect)
    assert bias < 3.0, (
        f"DiD estimate {did_estimate:.2f} too far from true effect "
        f"{treatment_effect:.2f} (bias={bias:.2f})"
    )

    # Sanity checks
    assert estimate_did(pre_c, pre_c, pre_t, pre_t) < 1.0, "Pre-period DiD should be ~0"
    control_only_effect = estimate_did(pre_c, post_c, pre_c, post_c)
    assert abs(control_only_effect) < 2.0, "Same-group DiD should be ~0"

    print(
        f"True treatment effect: {treatment_effect:.2f} | DiD estimate: {did_estimate:.2f} | "
        f"Bias: {bias:.2f} | Pre-period DiD: {estimate_did(pre_c, pre_c, pre_t, pre_t):.2f} | PASS"
    )
