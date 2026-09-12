"""
Regression Discontinuity (RD).

Treatment is assigned by a cutoff rule on a running variable: T=1 if X >= cutoff.
There is a discontinuity in the outcome at the cutoff: E[Y | X=c+] - E[Y | X=c-] = ATE.
We plant a cutoff effect and smooth underlying relationship; RD recovers the effect.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
from typing import List, Tuple


def local_linear_fit(
    x_window: List[float], y_window: List[float]
) -> Tuple[float, float]:
    """
    Fit Y = a + b*X via least-squares on a small window.
    Returns (intercept, slope).
    """
    n = len(x_window)
    if n < 2:
        return 0.0, 0.0

    mean_x = sum(x_window) / n
    mean_y = sum(y_window) / n

    ss_xx = sum((x - mean_x) ** 2 for x in x_window)
    ss_xy = sum((x_window[i] - mean_x) * (y_window[i] - mean_y) for i in range(n))

    if ss_xx < 1e-6:
        return mean_y, 0.0

    b = ss_xy / ss_xx
    a = mean_y - b * mean_x

    return a, b


if __name__ == "__main__":
    random.seed(42)

    # Running variable X, uniformly distributed
    n = 300
    X = sorted([random.uniform(0, 10) for _ in range(n)])

    # Treatment cutoff at X=5
    cutoff = 5.0
    T = [1 if x >= cutoff else 0 for x in X]

    # Outcome: smooth underlying function + discontinuity at cutoff
    # Underlying: Y = 0.5 * X + noise
    # Discontinuity: +3.0 jump at X=cutoff for treated units
    true_rd_effect = 3.0
    Y = [
        0.5 * X[i] + true_rd_effect * T[i] + random.gauss(0, 0.3) for i in range(n)
    ]

    # RD estimate: fit local linear on window around cutoff
    bandwidth = 2.0
    left_indices = [
        i for i in range(n) if cutoff - bandwidth <= X[i] < cutoff
    ]
    right_indices = [
        i for i in range(n) if cutoff <= X[i] <= cutoff + bandwidth
    ]

    if len(left_indices) > 1 and len(right_indices) > 1:
        x_left = [X[i] for i in left_indices]
        y_left = [Y[i] for i in left_indices]
        x_right = [X[i] for i in right_indices]
        y_right = [Y[i] for i in right_indices]

        a_left, b_left = local_linear_fit(x_left, y_left)
        a_right, b_right = local_linear_fit(x_right, y_right)

        # RD estimate = difference in fitted values at cutoff
        y_left_at_cutoff = a_left + b_left * cutoff
        y_right_at_cutoff = a_right + b_right * cutoff
        rd_estimate = y_right_at_cutoff - y_left_at_cutoff

        bias = abs(rd_estimate - true_rd_effect)

        assert bias < 1.0, (
            f"RD estimate {rd_estimate:.2f} too far from true effect "
            f"{true_rd_effect:.2f} (bias={bias:.2f})"
        )
        assert len(left_indices) >= 20, f"Too few observations in left window"
        assert len(right_indices) >= 20, f"Too few observations in right window"

        print(
            f"True RD effect: {true_rd_effect:.2f} | RD estimate: {rd_estimate:.2f} | "
            f"Bias: {bias:.2f} | Left obs: {len(left_indices)} | Right obs: {len(right_indices)} | PASS"
        )
    else:
        raise AssertionError("Not enough observations in bandwidth window")
