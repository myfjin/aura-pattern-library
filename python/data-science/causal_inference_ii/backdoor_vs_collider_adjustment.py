"""Backdoor vs Collider adjustment: adjusting backdoor removes confounding bias;
adjusting a collider CREATES bias (collider bias, Berkson's paradox).

DAG: X ← U → Y (backdoor open; adjust U to close it).
DAG: X → V ← Y (collider; adjusting V opens a spurious path).
Core claim: backdoor adjustment recovers effect; collider adjustment makes bias WORSE.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import math
from typing import List, Tuple

def fit_regression(x: List[float], y: List[float]) -> Tuple[float, float]:
    """Fit y = a + b*x; return (a, b)."""
    n = len(x)
    if n == 0:
        return 0.0, 0.0
    x_mean = sum(x) / n
    y_mean = sum(y) / n
    num = sum((x[i] - x_mean) * (y[i] - y_mean) for i in range(n))
    denom = sum((x[i] - x_mean)**2 for i in range(n))
    if abs(denom) < 1e-10:
        return y_mean, 0.0
    b = num / denom
    a = y_mean - b * x_mean
    return a, b

if __name__ == "__main__":
    import random
    random.seed(42)

    n = 200
    true_effect = 2.0

    # BACKDOOR case: U confounds X → Y. Adjusting U closes the backdoor and recovers true effect.
    u = [random.gauss(0, 1) for _ in range(n)]
    x_backdoor = [1.0 * u[i] + random.gauss(0, 1) for i in range(n)]
    y_backdoor = [true_effect * x_backdoor[i] + 1.5 * u[i] + random.gauss(0, 0.5) for i in range(n)]

    # Unadjusted: biased due to confounding.
    _, unadjusted_backdoor = fit_regression(x_backdoor, y_backdoor)

    # Adjusted for U: should recover true effect (backdoor closed).
    # Fit y = a + b*x + c*u; extract b.
    x_mean = sum(x_backdoor) / n
    u_mean = sum(u) / n
    y_mean = sum(y_backdoor) / n

    sxx = sum((x_backdoor[i] - x_mean)**2 for i in range(n))
    suu = sum((u[i] - u_mean)**2 for i in range(n))
    sxu = sum((x_backdoor[i] - x_mean) * (u[i] - u_mean) for i in range(n))
    sxy = sum((x_backdoor[i] - x_mean) * (y_backdoor[i] - y_mean) for i in range(n))
    suy = sum((u[i] - u_mean) * (y_backdoor[i] - y_mean) for i in range(n))

    denom = sxx * suu - sxu**2
    if abs(denom) > 1e-10:
        # X coefficient (b1) in y = b1*x + b2*u:  (Suu*Sxy - Sxu*Suy) / (Sxx*Suu - Sxu^2).
        adjusted_backdoor = (suu * sxy - sxu * suy) / denom
    else:
        adjusted_backdoor = 0.0

    # COLLIDER case: X → V ← Y. Adjusting V creates spurious association.
    x_collider = [random.gauss(0, 1) for _ in range(n)]
    y_collider = [random.gauss(0, 1) for _ in range(n)]  # Y independent of X
    v = [1.0 * x_collider[i] + 1.0 * y_collider[i] + random.gauss(0, 0.5) for i in range(n)]

    # Unadjusted: should show no association (X and Y independent).
    _, unadjusted_collider = fit_regression(x_collider, y_collider)

    # Adjusted for V: opens spurious path, creates fake association.
    x_mean_c = sum(x_collider) / n
    v_mean = sum(v) / n
    y_mean_c = sum(y_collider) / n

    sxx_c = sum((x_collider[i] - x_mean_c)**2 for i in range(n))
    svv = sum((v[i] - v_mean)**2 for i in range(n))
    sxv = sum((x_collider[i] - x_mean_c) * (v[i] - v_mean) for i in range(n))
    sxy_c = sum((x_collider[i] - x_mean_c) * (y_collider[i] - y_mean_c) for i in range(n))
    svy = sum((v[i] - v_mean) * (y_collider[i] - y_mean_c) for i in range(n))

    denom_c = sxx_c * svv - sxv**2
    if abs(denom_c) > 1e-10:
        # X coefficient in y = b*x + d*v (same corrected form as the backdoor case).
        adjusted_collider = (svv * sxy_c - sxv * svy) / denom_c
    else:
        adjusted_collider = 0.0

    # Backdoor: unadjusted is biased (confounding); ADJUSTED must RECOVER the true effect.
    assert abs(unadjusted_backdoor - true_effect) > 0.3, \
        f"Backdoor unadjusted {unadjusted_backdoor} should be biased from true {true_effect}"
    assert abs(adjusted_backdoor - true_effect) < 0.3, \
        f"Backdoor ADJUSTED {adjusted_backdoor} should recover true effect {true_effect} (measured ≈1.98)"

    # Collider: adjust should make bias WORSE (create spurious association).
    assert abs(adjusted_collider) > abs(unadjusted_collider) * 1.5, \
        f"Collider adjustment should worsen: unadj {abs(unadjusted_collider)}, adj {abs(adjusted_collider)}"

    print("PASS")
