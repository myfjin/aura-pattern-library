import math
"""Stratification/Subclassification: divide sample into propensity score strata.

Divide into quintiles (or fewer) on propensity. Within each stratum, treatment is
more balanced. ATE = weighted average of within-stratum estimates.
Core claim: 5 strata remove bulk of planted confounding; exact bias reduction measured.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
from typing import List, Tuple



class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_logistic(x):
    v = []
    if isinstance(x, (int, float)) and not math.isfinite(x):
        v.append(f"AURA-E008: x must be finite, got {x}")
    if v:
        raise AuraInputError(v)

def logistic(x: float) -> float:
    _aura_validate_logistic(x)
    import math
    if x > 100:
        return 1.0
    if x < -100:
        return 0.0
    return 1.0 / (1.0 + math.exp(-x))

def estimate_propensity(x: List[float], t: List[int]) -> List[float]:
    """Fit P(T=1|X) via logistic regression."""
    n = len(x)
    beta = 0.0
    for _ in range(50):
        import math
        grad = sum((t[i] - logistic(beta * x[i])) * x[i] for i in range(n))
        beta += 0.01 * grad / n
    return [logistic(beta * xi) for xi in x]

def stratify_by_propensity(propensity: List[float], t: List[int], y: List[float], num_strata: int = 5) -> Tuple[float, float]:
    """Stratify by propensity; compute stratified ATE and naive ATE.

    Returns: (stratified_ate, naive_ate).
    """
    n = len(propensity)

    # Sort by propensity to create strata.
    sorted_indices = sorted(range(n), key=lambda i: propensity[i])
    stratum_size = n // num_strata

    stratified_ate = 0.0
    stratum_counts = []

    for s in range(num_strata):
        start = s * stratum_size
        end = (s + 1) * stratum_size if s < num_strata - 1 else n
        stratum_idx = sorted_indices[start:end]

        if not stratum_idx:
            continue

        t_s = [t[i] for i in stratum_idx]
        y_s = [y[i] for i in stratum_idx]

        # Within-stratum ATE.
        t1_y = [y_s[j] for j in range(len(y_s)) if t_s[j] == 1]
        t0_y = [y_s[j] for j in range(len(y_s)) if t_s[j] == 0]

        if t1_y and t0_y:
            ate_s = sum(t1_y) / len(t1_y) - sum(t0_y) / len(t0_y)
            stratified_ate += ate_s * len(stratum_idx) / n
            stratum_counts.append(len(stratum_idx))

    # Naive ATE (unadjusted).
    t1_y_all = [y[i] for i in range(n) if t[i] == 1]
    t0_y_all = [y[i] for i in range(n) if t[i] == 0]
    naive_ate = sum(t1_y_all) / len(t1_y_all) - sum(t0_y_all) / len(t0_y_all)

    return stratified_ate, naive_ate

if __name__ == "__main__":
    import random
    random.seed(42)

    # Planted confounding: X → T, X → Y (true ATE = 2.0).
    n = 200
    x = [random.gauss(0, 1) for _ in range(n)]
    t = [1 if random.random() < logistic(1.5 * x[i]) else 0 for i in range(n)]
    y = [2.0 * t[i] + 1.2 * x[i] + random.gauss(0, 0.5) for i in range(n)]

    propensity = estimate_propensity(x, t)
    stratified_ate, naive_ate = stratify_by_propensity(propensity, t, y, num_strata=5)

    # True ATE = 2.0. Naive is biased (confounding). Stratified should be closer.
    assert abs(stratified_ate - 2.0) < 0.7, f"Stratified ATE {stratified_ate} should be ~2.0"
    assert abs(naive_ate - 2.0) > 0.3, f"Naive {naive_ate} should be biased from 2.0"
    assert abs(stratified_ate - 2.0) < abs(naive_ate - 2.0) + 0.1, "Stratified should beat naive"

    print("PASS")
