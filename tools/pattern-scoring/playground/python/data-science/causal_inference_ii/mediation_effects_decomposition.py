"""Mediation analysis: decompose a total effect into direct + indirect via a mediator.

Linear model X→M→Y. Total = direct (X→Y holding M) + indirect (X→M→Y). Product method:
indirect = β(X→M) × β(M→Y | X). The M→Y coefficient MUST be the partial (multiple-
regression) coefficient adjusting for X — using the X-coefficient here instead silently
SWAPS direct and indirect.
Core claim: planted linear system recovered — total≈7, direct≈1, indirect≈6.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
from typing import Tuple

def fit_simple_slope(x_vals, y_vals) -> float:
    n = len(x_vals)
    xm = sum(x_vals) / n
    ym = sum(y_vals) / n
    num = sum((x_vals[i] - xm) * (y_vals[i] - ym) for i in range(n))
    den = sum((x_vals[i] - xm)**2 for i in range(n))
    return num / den if abs(den) > 1e-12 else 0.0

def mediation_analysis(x, m, y) -> Tuple[float, float, float]:
    """Return (total, direct, indirect) for X→M→Y.

    total    = slope of Y on X (unadjusted)
    direct   = X coefficient in Y ~ X + M   (b1)
    indirect = β(X→M) × [M coefficient in Y ~ X + M]   (b2, adjusted for X)
    """
    n = len(x)
    total = fit_simple_slope(x, y)
    x_to_m = fit_simple_slope(x, m)

    xm = sum(x) / n
    mm = sum(m) / n
    ym = sum(y) / n
    sxx = sum((x[i] - xm)**2 for i in range(n))
    smm = sum((m[i] - mm)**2 for i in range(n))
    sxm = sum((x[i] - xm) * (m[i] - mm) for i in range(n))
    sxy = sum((x[i] - xm) * (y[i] - ym) for i in range(n))
    smy = sum((m[i] - mm) * (y[i] - ym) for i in range(n))
    den = sxx * smm - sxm**2
    if abs(den) < 1e-12:
        return total, total, 0.0

    b1 = (smm * sxy - sxm * smy) / den   # X coefficient  → direct effect
    b2 = (sxx * smy - sxm * sxy) / den   # M coefficient  → M→Y adjusting for X
    direct = b1
    indirect = x_to_m * b2
    return total, direct, indirect

if __name__ == "__main__":
    import random
    random.seed(42)

    # Planted: X→M (2.0), M→Y (3.0), X→Y direct (1.0). Total = 1 + 2*3 = 7.
    # M carries its own noise so X and M aren't collinear enough to swamp the partial fit.
    n = 300
    x = [random.gauss(0, 1) for _ in range(n)]
    m = [2.0 * x[i] + random.gauss(0, 1.0) for i in range(n)]
    y = [1.0 * x[i] + 3.0 * m[i] + random.gauss(0, 0.5) for i in range(n)]

    total, direct, indirect = mediation_analysis(x, m, y)

    # Defining property: recover the PLANTED decomposition (not just the identity).
    # Measured (seed 42): total≈7.08, direct≈1.09, indirect≈5.99.
    assert abs(total - 7.0) < 0.5, f"total {total} should recover 7.0"
    assert abs(direct - 1.0) < 0.5, f"direct {direct} should recover 1.0"
    assert abs(indirect - 6.0) < 0.7, f"indirect {indirect} should recover 6.0"
    assert abs((direct + indirect) - total) < 1e-6, "total = direct + indirect"

    print("PASS")
