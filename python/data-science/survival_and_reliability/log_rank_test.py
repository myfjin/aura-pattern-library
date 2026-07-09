"""Log-rank test: nonparametric test for equality of survival curves.

Compares two groups via observed vs expected events under null hypothesis
(no group difference). Core claim: two different groups detected; identical
groups not flagged as different.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import math
from typing import List, Tuple

def log_rank_test(
    times_g1: List[float],
    events_g1: List[int],
    times_g2: List[float],
    events_g2: List[int]
) -> Tuple[float, float]:
    """Compute log-rank test statistic and p-value.

    Returns: (test_statistic, p_value).
    """
    times = sorted(set(times_g1 + times_g2))

    o1 = 0  # Observed events in group 1.
    e1 = 0.0  # Expected events in group 1 under H0.
    var = 0.0  # Variance of e1.

    for t in times:
        # At each event time, compute contribution to test statistic.
        y1 = sum(1 for i in range(len(times_g1)) if times_g1[i] >= t)
        y2 = sum(1 for i in range(len(times_g2)) if times_g2[i] >= t)
        d1 = sum(1 for i in range(len(times_g1)) if times_g1[i] == t and events_g1[i] == 1)
        d2 = sum(1 for i in range(len(times_g2)) if times_g2[i] == t and events_g2[i] == 1)
        d = d1 + d2

        if d == 0:
            continue

        o1 += d1
        e1_contrib = d * y1 / (y1 + y2)
        e1 += e1_contrib

        denom = (y1 + y2)**2 * (y1 + y2 - 1)
        if denom > 1e-14:
            var_contrib = d * y1 * y2 * (y1 + y2 - d) / denom
            var += var_contrib

    if var < 1e-14:
        return 0.0, 1.0

    z = (o1 - e1) / math.sqrt(var)
    # Two-tailed p-value (approximation via normal).
    p_value = 2 * (1 - 0.5 * (1 + math.erf(abs(z) / math.sqrt(2))))

    return z, p_value

if __name__ == "__main__":
    import random
    random.seed(42)

    # Planted: group 1 has better survival (true difference).
    times_g1 = [random.expovariate(0.5) for _ in range(30)]
    events_g1 = [1] * 30

    times_g2 = [random.expovariate(1.0) for _ in range(30)]
    events_g2 = [1] * 30

    z_diff, p_diff = log_rank_test(times_g1, events_g1, times_g2, events_g2)

    # Planted null: TWO INDEPENDENT samples drawn from the SAME distribution. (Feeding
    # the same array twice would force z=0 by construction — a vacuous null. Independent
    # draws make the "fail to reject" a real statistical outcome, not an identity.)
    times_same1 = [random.expovariate(0.7) for _ in range(40)]
    times_same2 = [random.expovariate(0.7) for _ in range(40)]
    z_same, p_same = log_rank_test(times_same1, [1] * 40, times_same2, [1] * 40)

    # Different groups: reject equality (low p). Same distribution: fail to reject (high p).
    # Measured (seed 42): p_diff≈0.036, p_same≈0.83.
    assert p_diff < 0.10, f"p-value for different groups too high: {p_diff}"
    assert p_same > 0.10, f"p-value for same-distribution groups too low (false reject): {p_same}"

    print("PASS")
