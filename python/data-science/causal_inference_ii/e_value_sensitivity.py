"""E-value sensitivity analysis: how strong must an unmeasured confounder be to explain away an effect?

E-value = (RR + sqrt(RR*(RR-1))) / 1 for RR > 1. A strong effect (RR=3) needs implausibly
large confounder to explain away; weak effect (RR=1.1) can be explained by modest confounder.
Core claim: strong vs weak effects quantified; numbers demonstrate implausibility thresholds.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import math
from typing import Tuple

def risk_ratio_from_counts(t1_y1: int, t1_y0: int, t0_y1: int, t0_y0: int) -> float:
    """Compute risk ratio: P(Y=1|T=1) / P(Y=1|T=0)."""
    p_y1_t1 = t1_y1 / (t1_y1 + t1_y0) if (t1_y1 + t1_y0) > 0 else 0.0
    p_y1_t0 = t0_y1 / (t0_y1 + t0_y0) if (t0_y1 + t0_y0) > 0 else 0.0
    if p_y1_t0 == 0:
        return float('inf')
    return p_y1_t1 / p_y1_t0

def e_value(rr: float) -> float:
    """Compute E-value for a risk ratio."""
    if rr <= 1.0:
        return 1.0
    return (rr + math.sqrt(rr * (rr - 1))) / 1.0

def build_2x2_table(treatment: list, outcome: list) -> Tuple[int, int, int, int]:
    """Tabulate a 2x2 contingency table from binary treatment/outcome.

    Returns: (T=1,Y=1), (T=1,Y=0), (T=0,Y=1), (T=0,Y=0).
    """
    t1_y1 = t1_y0 = t0_y1 = t0_y0 = 0
    for i in range(len(treatment)):
        if treatment[i] == 1:
            if outcome[i] == 1:
                t1_y1 += 1
            else:
                t1_y0 += 1
        else:
            if outcome[i] == 1:
                t0_y1 += 1
            else:
                t0_y0 += 1
    return t1_y1, t1_y0, t0_y1, t0_y0

if __name__ == "__main__":
    import random
    random.seed(42)

    # STRONG effect: RR = 3.0
    n_strong = 200
    t_strong = [random.randint(0, 1) for _ in range(n_strong)]
    # Y depends strongly on T.
    y_strong = [1 if (t_strong[i] == 1 and random.random() < 0.6) or
                     (t_strong[i] == 0 and random.random() < 0.2) else 0
                for i in range(n_strong)]

    t1_y1_s, t1_y0_s, t0_y1_s, t0_y0_s = build_2x2_table(t_strong, y_strong)
    rr_strong = risk_ratio_from_counts(t1_y1_s, t1_y0_s, t0_y1_s, t0_y0_s)
    e_strong = e_value(rr_strong)

    # WEAK effect: RR = 1.1
    n_weak = 300
    t_weak = [random.randint(0, 1) for _ in range(n_weak)]
    y_weak = [1 if random.random() < (0.30 if t_weak[i] == 1 else 0.27) else 0
              for i in range(n_weak)]

    t1_y1_w, t1_y0_w, t0_y1_w, t0_y0_w = build_2x2_table(t_weak, y_weak)
    rr_weak = risk_ratio_from_counts(t1_y1_w, t1_y0_w, t0_y1_w, t0_y0_w)
    e_weak = e_value(rr_weak)

    # Strong effect needs large E-value (confounder must be implausibly strong).
    # Weak effect can be explained away by modest confounder.
    assert rr_strong > 2.0, f"Strong effect RR {rr_strong} should be > 2.0"
    assert rr_weak < 1.5, f"Weak effect RR {rr_weak} should be modest"
    assert e_strong > e_weak * 1.5, f"Strong E-value {e_strong} should be higher than weak {e_weak}"
    assert e_strong > 1.5, f"E-values should be > 1 (at least risk ratio)"

    print("PASS")
