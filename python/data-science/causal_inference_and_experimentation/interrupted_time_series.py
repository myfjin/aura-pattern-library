"""
Interrupted Time Series (ITS) Segmented Regression.

Time series with a pre-intervention trend; at a cutoff, intervention introduces
a level change and/or slope change. Segmented regression detects both.
Y = β0 + β1*t + β2*intervention + β3*t*intervention + noise.
β2 = level change, β3 = slope change. We plant and recover both.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Tuple


def fit_segmented_regression(
    times: List[int], Y: List[float], cutoff: int
) -> Tuple[float, float, float, float]:
    """
    Fit Y = β0 + β1*t + β2*intervention + β3*t_post.
    intervention = 1 if t >= cutoff, else 0.
    t_post = max(0, t - cutoff).
    Returns (β0, β1, β2, β3) via least-squares.
    """
    n = len(Y)
    intervention = [1 if t >= cutoff else 0 for t in times]
    t_post = [max(0, t - cutoff) for t in times]

    # Build design matrix [1, t, intervention, t_post]
    X = [[1, times[i], intervention[i], t_post[i]] for i in range(n)]

    # Normal equations: X^T X β = X^T y
    xtx = [[0.0] * 4 for _ in range(4)]
    xty = [0.0] * 4

    for i in range(n):
        for j in range(4):
            for k in range(4):
                xtx[j][k] += X[i][j] * X[i][k]
            xty[j] += X[i][j] * Y[i]

    # Solve via Gaussian elimination
    for col in range(4):
        # Pivot
        max_row = col
        for row in range(col + 1, 4):
            if abs(xtx[row][col]) > abs(xtx[max_row][col]):
                max_row = row
        xtx[col], xtx[max_row] = xtx[max_row], xtx[col]
        xty[col], xty[max_row] = xty[max_row], xty[col]

        # Eliminate
        for row in range(col + 1, 4):
            if abs(xtx[col][col]) < 1e-10:
                continue
            factor = xtx[row][col] / xtx[col][col]
            for j in range(col, 4):
                xtx[row][j] -= factor * xtx[col][j]
            xty[row] -= factor * xty[col]

    # Back-substitution
    beta = [0.0] * 4
    for i in range(3, -1, -1):
        if abs(xtx[i][i]) < 1e-10:
            continue
        beta[i] = xty[i]
        for j in range(i + 1, 4):
            beta[i] -= xtx[i][j] * beta[j]
        beta[i] /= xtx[i][i]

    return tuple(beta)


if __name__ == "__main__":
    import random

    random.seed(42)

    n = 100
    times = list(range(n))
    cutoff = 50

    # True parameters
    true_beta0 = 50.0
    true_beta1 = 0.5  # baseline trend
    true_level_change = 10.0  # jump at cutoff
    true_slope_change = 0.3  # increased trend post-cutoff

    # Generate data
    Y = []
    for t in times:
        intervention = 1 if t >= cutoff else 0
        t_post = max(0, t - cutoff)
        y = (
            true_beta0
            + true_beta1 * t
            + true_level_change * intervention
            + true_slope_change * t_post
            + random.gauss(0, 2)
        )
        Y.append(y)

    # Estimate via segmented regression
    beta0, beta1, level_change, slope_change = fit_segmented_regression(
        times, Y, cutoff
    )

    # Check: estimates should be close to true parameters
    assert abs(level_change - true_level_change) < 2.0, (
        f"Level change {level_change:.2f} far from true "
        f"{true_level_change:.2f}"
    )
    assert abs(slope_change - true_slope_change) < 0.5, (
        f"Slope change {slope_change:.2f} far from true {true_slope_change:.2f}"
    )

    print(
        f"Level change: true={true_level_change:.2f} | est={level_change:.2f} | "
        f"Slope change: true={true_slope_change:.2f} | est={slope_change:.2f} | PASS"
    )
