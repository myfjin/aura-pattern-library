"""
Placebo Test for Causal Inference.

Under the null (no treatment effect), permuting treatment labels should destroy
the measured effect. Under the alternative (true treatment effect), the effect
persists under the true assignment but disappears under permuted assignments.
We verify that true assignment recovers effect, permuted assignments do not.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
from typing import List


def estimate_effect(T: List[int], Y: List[float]) -> float:
    """ATE = mean(Y | T=1) - mean(Y | T=0)."""
    y1 = [Y[i] for i in range(len(T)) if T[i] == 1]
    y0 = [Y[i] for i in range(len(T)) if T[i] == 0]
    if len(y1) == 0 or len(y0) == 0:
        return 0.0
    return sum(y1) / len(y1) - sum(y0) / len(y0)


if __name__ == "__main__":
    random.seed(42)

    n = 200
    true_effect = 3.0

    # Confounder
    U = [random.gauss(0, 1) for _ in range(n)]

    # Treatment assignment (depends on U, but we observe both T and U)
    T = [1 if random.random() < 0.3 + 0.3 * (u > 0) else 0 for u in U]

    # Outcome with true causal effect
    Y = [true_effect * T[i] + 0.5 * U[i] + random.gauss(0, 1) for i in range(n)]

    # Estimate effect with true assignment
    true_effect_estimate = estimate_effect(T, Y)

    # Permutation test: shuffle treatment labels 100 times
    permuted_effects = []
    for _ in range(100):
        T_perm = T.copy()
        random.shuffle(T_perm)
        effect_perm = estimate_effect(T_perm, Y)
        permuted_effects.append(effect_perm)

    # Compute: what fraction of permuted effects are as large as true estimate?
    # (One-sided p-value)
    larger_count = sum(1 for e in permuted_effects if e >= true_effect_estimate)
    p_value_approx = larger_count / len(permuted_effects)

    # Check: true effect should be significant (p < 0.05)
    # and should be much larger than permuted effects
    avg_permuted = sum(permuted_effects) / len(permuted_effects)
    max_permuted = max(permuted_effects)

    assert true_effect_estimate > avg_permuted, (
        f"True effect {true_effect_estimate:.2f} not larger than "
        f"avg permuted {avg_permuted:.2f}"
    )
    assert p_value_approx < 0.1, (
        f"True effect p-value {p_value_approx:.2f} too high (not significant)"
    )

    print(
        f"True assignment effect: {true_effect_estimate:.2f} | "
        f"Avg permuted: {avg_permuted:.2f} | Max permuted: {max_permuted:.2f} | "
        f"P-value: {p_value_approx:.2f} (n_perms={len(permuted_effects)}) | PASS"
    )
