"""Frontdoor criterion: identify a causal effect when the backdoor is unblockable.

DAG: U → X → M → Y and U → Y (hidden confounder U on X and Y; the backdoor through U
cannot be closed because U is unobserved). The frontdoor path X→M→Y still identifies the
effect:  effect = β(X→M) × β(M→Y adjusting for X). The M→Y coefficient MUST adjust for X
(conditioning on X blocks the M↔Y backdoor through U) — the unadjusted M→Y slope leaves
the confounding in.
Core claim: frontdoor recovers the true causal effect; the naive X→Y slope is biased by U.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
from typing import List, Tuple

def simple_slope(x: List[float], y: List[float]) -> float:
    n = len(x)
    xm = sum(x) / n
    ym = sum(y) / n
    num = sum((x[i] - xm) * (y[i] - ym) for i in range(n))
    den = sum((x[i] - xm)**2 for i in range(n))
    return num / den if abs(den) > 1e-12 else 0.0

def partial_slope_m(x: List[float], m: List[float], y: List[float]) -> float:
    """M coefficient in the regression Y ~ X + M  (M→Y adjusting for X)."""
    n = len(x)
    xm = sum(x) / n
    mm = sum(m) / n
    ym = sum(y) / n
    smm = sum((m[i] - mm)**2 for i in range(n))
    sxx = sum((x[i] - xm)**2 for i in range(n))
    smx = sum((m[i] - mm) * (x[i] - xm) for i in range(n))
    smy = sum((m[i] - mm) * (y[i] - ym) for i in range(n))
    sxy = sum((x[i] - xm) * (y[i] - ym) for i in range(n))
    den = smm * sxx - smx**2
    return (sxx * smy - smx * sxy) / den if abs(den) > 1e-12 else 0.0

def frontdoor_lite(x, m, y) -> Tuple[float, float]:
    """Return (frontdoor_effect, naive_direct_slope)."""
    beta_xm = simple_slope(x, m)
    beta_my_adj = partial_slope_m(x, m, y)   # adjusted for X — the key fix
    frontdoor = beta_xm * beta_my_adj
    naive = simple_slope(x, y)               # confounded by U
    return frontdoor, naive

if __name__ == "__main__":
    import random
    random.seed(42)

    n = 150
    true_x_to_m, true_m_to_y = 2.0, 1.5
    true_effect = true_x_to_m * true_m_to_y   # 3.0

    u = [random.gauss(0, 1) for _ in range(n)]              # hidden confounder
    x = [0.8 * u[i] + random.gauss(0, 0.5) for i in range(n)]
    m = [true_x_to_m * x[i] + random.gauss(0, 0.5) for i in range(n)]
    y = [true_m_to_y * m[i] + 0.6 * u[i] + random.gauss(0, 0.5) for i in range(n)]

    frontdoor, naive = frontdoor_lite(x, m, y)

    # Defining property: frontdoor recovers ~3.0; naive X→Y slope is biased by U; frontdoor wins.
    # Measured (seed 42): frontdoor≈3.12, naive≈3.53.
    assert abs(frontdoor - true_effect) < 0.6, f"Frontdoor {frontdoor} should recover {true_effect}"
    assert abs(naive - true_effect) > 0.3, f"Naive {naive} should be biased from {true_effect}"
    assert abs(frontdoor - true_effect) < abs(naive - true_effect), "Frontdoor should beat naive"

    print("PASS")
