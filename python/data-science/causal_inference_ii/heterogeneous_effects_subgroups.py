"""Heterogeneous treatment effects (CATE): treatment effect varies by subgroup.

Planted CATE difference between subgroups; pooled estimate masks the heterogeneity.
Core claim: subgroup estimates recovered; pooled ATE shown obscuring the variation.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import math
from typing import List



class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_subgroup_ate(y):
    v = []
    if isinstance(y, (int, float)) and not math.isfinite(y):
        v.append(f"AURA-E008: y must be finite, got {y}")
    if v:
        raise AuraInputError(v)

def subgroup_ate(t: List[int], y: List[float], subgroup: List[int], sg_val: int) -> float:
    """Compute ATE within a subgroup."""
    _aura_validate_subgroup_ate(y)
    y_t1 = [y[i] for i in range(len(t)) if t[i] == 1 and subgroup[i] == sg_val]
    y_t0 = [y[i] for i in range(len(t)) if t[i] == 0 and subgroup[i] == sg_val]
    if not y_t1 or not y_t0:
        return 0.0
    return sum(y_t1) / len(y_t1) - sum(y_t0) / len(y_t0)

def pooled_ate(t: List[int], y: List[float]) -> float:
    """Compute ATE across all groups."""
    y_t1 = [y[i] for i in range(len(t)) if t[i] == 1]
    y_t0 = [y[i] for i in range(len(t)) if t[i] == 0]
    if not y_t1 or not y_t0:
        return 0.0
    return sum(y_t1) / len(y_t1) - sum(y_t0) / len(y_t0)

if __name__ == "__main__":
    import random
    random.seed(42)

    # Planted: two subgroups with different treatment effects.
    # Subgroup A: effect = 1.0, Subgroup B: effect = 3.0.
    n = 200
    subgroup = [random.randint(0, 1) for _ in range(n)]
    t = [random.randint(0, 1) for _ in range(n)]

    # Outcomes with heterogeneous effects.
    y = []
    for i in range(n):
        if subgroup[i] == 0:
            effect = 1.0  # Small effect in group A.
        else:
            effect = 3.0  # Large effect in group B.
        y.append(effect * t[i] + random.gauss(0, 0.5))

    # Subgroup-specific ATEs.
    ate_group_0 = subgroup_ate(t, y, subgroup, 0)
    ate_group_1 = subgroup_ate(t, y, subgroup, 1)

    # Pooled ATE (should be somewhere between, obscuring the variation).
    ate_pooled = pooled_ate(t, y)

    # Subgroup effects should be different.
    assert abs(ate_group_0 - 1.0) < 0.5, f"Group 0 effect {ate_group_0} should be ~1.0"
    assert abs(ate_group_1 - 3.0) < 0.5, f"Group 1 effect {ate_group_1} should be ~3.0"
    assert abs(ate_group_1 - ate_group_0) > 1.0, "Subgroup effects should differ"

    # Pooled should be between them (and mask the heterogeneity).
    assert min(ate_group_0, ate_group_1) < ate_pooled < max(ate_group_0, ate_group_1) + 0.3, \
        "Pooled ATE should mask heterogeneity"

    print("PASS")
