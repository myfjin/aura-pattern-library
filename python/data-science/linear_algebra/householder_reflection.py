"""Householder reflection: zeros out components via hyperplane reflection.

Given vector x, finds reflection matrix H = I - 2·v·v^T that maps x to
[||x||, 0, 0, ...]. Used in QR, eigenvalue, and least-squares algorithms.
Core claim: reflection computed; planted vector mapped to scaled unit vector.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import math
from typing import Tuple

def householder_reflection(
    x: list
) -> Tuple[list, float]:
    """Compute Householder reflection H such that H·x = [±||x||, 0, ..., 0]^T.

    Returns: (v, beta) where H = I - 2·v·v^T / (v^T·v), v normalized.
    """
    n = len(x)
    norm_x = math.sqrt(sum(xi**2 for xi in x))

    if norm_x < 1e-14:
        return [0.0] * n, 0.0

    # Compute v = x - sign(x[0])·||x||·e1.
    v = x[:]
    if x[0] >= 0:
        v[0] -= norm_x
    else:
        v[0] += norm_x

    # Normalize v.
    norm_v = math.sqrt(sum(vi**2 for vi in v))
    if norm_v < 1e-14:
        return [0.0] * n, 0.0

    v_normalized = [vi / norm_v for vi in v]
    return v_normalized, 2.0



class AuraInputError(ValueError):
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_domain_apply_householder(beta):
    v = []
    if isinstance(beta, (int, float)) and not math.isfinite(beta):
        v.append(f"AURA-E008: beta must be finite, got {beta}")
    if v:
        raise AuraInputError(v)

def apply_householder(H_vector: list, beta: float, x: list) -> list:
    """Apply Householder reflection H = I - beta·v·v^T to vector x."""
    _aura_domain_apply_householder(beta)
    n = len(x)
    dot_product = sum(H_vector[i] * x[i] for i in range(n))
    return [x[i] - beta * dot_product * H_vector[i] for i in range(n)]

if __name__ == "__main__":
    import random
    random.seed(42)

    # Planted: vector [3, 4, 0] with norm 5.
    x = [3.0, 4.0, 0.0]
    v, beta = householder_reflection(x)

    # Apply reflection: H·x should be [5, 0, 0] (or [-5, 0, 0]).
    Hx = apply_householder(v, beta, x)

    # Check: first component is ±||x||, others are ~0.
    norm_x = 5.0
    assert abs(abs(Hx[0]) - norm_x) < 1e-10, f"First component: {Hx[0]} vs ±{norm_x}"
    assert abs(Hx[1]) < 1e-10, f"Second component: {Hx[1]}"
    assert abs(Hx[2]) < 1e-10, f"Third component: {Hx[2]}"

    print("PASS")
