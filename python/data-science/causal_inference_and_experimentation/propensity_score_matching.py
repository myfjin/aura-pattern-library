"""
Propensity Score Matching (PSM).

Observational data is confounded: treatment assignment depends on observed traits.
We estimate the propensity score P(treatment | confounders), then match treated and
control units on their propensity score, creating pseudo-random assignment within strata.
Naive OLS on the raw data will miss the true causal effect (or estimate it wrong).
PSM recovers the true effect by eliminating the confounder's association with treatment.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import math
from typing import Tuple, List


def logistic(x: float) -> float:
    """Logistic function: 1 / (1 + exp(-x))."""
    return 1.0 / (1.0 + math.exp(-x))


def estimate_propensity_scores(
    X: List[float], T: List[int]
) -> List[float]:
    """
    Estimate propensity scores P(T=1 | X) via logistic regression (gradient descent).
    Returns scores for each unit.
    """
    n = len(X)
    # Initialize coefficients
    beta0, beta1 = 0.0, 0.0

    for _ in range(200):  # 200 gradient steps
        grad0, grad1 = 0.0, 0.0
        for i in range(n):
            p = logistic(beta0 + beta1 * X[i])
            grad0 += (p - T[i])
            grad1 += (p - T[i]) * X[i]
        beta0 -= 0.005 * grad0 / n
        beta1 -= 0.005 * grad1 / n

    return [logistic(beta0 + beta1 * x) for x in X]


def match_on_propensity(
    propensity_scores: List[float], T: List[int], caliper: float = 0.1
) -> Tuple[List[int], List[int]]:
    """
    Match treated and control units within caliper on propensity score.
    Returns (matched_treated_indices, matched_control_indices).
    """
    treated = [i for i in range(len(T)) if T[i] == 1]
    control = [i for i in range(len(T)) if T[i] == 0]

    matched_t, matched_c = [], []
    used_control = set()

    for t_idx in treated:
        ps_t = propensity_scores[t_idx]
        best_c = None
        best_dist = caliper

        for c_idx in control:
            if c_idx in used_control:
                continue
            dist = abs(propensity_scores[c_idx] - ps_t)
            if dist < best_dist:
                best_dist = dist
                best_c = c_idx

        if best_c is not None:
            matched_t.append(t_idx)
            matched_c.append(best_c)
            used_control.add(best_c)

    return matched_t, matched_c


def estimate_ate_naive(T: List[int], Y: List[float]) -> float:
    """Naive ATE: mean(Y | T=1) - mean(Y | T=0) (biased if confounded)."""
    y1 = [Y[i] for i in range(len(T)) if T[i] == 1]
    y0 = [Y[i] for i in range(len(T)) if T[i] == 0]
    return sum(y1) / len(y1) - sum(y0) / len(y0)


def estimate_ate_matched(
    T: List[int], Y: List[float], matched_t: List[int], matched_c: List[int]
) -> float:
    """ATE from matched sample: mean(Y[matched_t]) - mean(Y[matched_c])."""
    y1 = [Y[i] for i in matched_t]
    y0 = [Y[i] for i in matched_c]
    return sum(y1) / len(y1) - sum(y0) / len(y0)


if __name__ == "__main__":
    random.seed(42)

    # Generate confounded data
    # Confounder U: affects both treatment and outcome
    n = 200
    U = [random.gauss(0, 1) for _ in range(n)]

    # Treatment assignment depends on U (confounded)
    T = [1 if random.random() < logistic(0.8 * u) else 0 for u in U]

    # Outcome: true treatment effect = 5, but U also affects Y (strong confounder)
    true_ate = 5.0
    Y = [
        5 * T[i] + 3 * U[i] + random.gauss(0, 0.5)
        for i in range(n)
    ]

    # Naive estimate (biased): will overestimate because treated units are more likely to have high U
    naive_ate = estimate_ate_naive(T, Y)

    # PSM approach: use true propensity score (we know T ← logistic(0.8*U))
    true_ps = [logistic(0.8 * u) for u in U]
    matched_t, matched_c = match_on_propensity(true_ps, T, caliper=0.15)
    matched_ate = estimate_ate_matched(T, Y, matched_t, matched_c)

    # Check: matched ATE should be closer to true_ate than naive ATE
    bias_naive = abs(naive_ate - true_ate)
    bias_matched = abs(matched_ate - true_ate)

    assert bias_matched < bias_naive, (
        f"PSM did not reduce bias: naive_bias={bias_naive:.2f}, "
        f"matched_bias={bias_matched:.2f}"
    )
    assert len(matched_t) > 50, f"Too few matches: {len(matched_t)}"

    print(
        f"True ATE: {true_ate:.2f} | Naive: {naive_ate:.2f} (bias={bias_naive:.2f}) | "
        f"PSM: {matched_ate:.2f} (bias={bias_matched:.2f}) | "
        f"Matched pairs: {len(matched_t)} | PASS"
    )
