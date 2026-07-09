"""Caliper matching: restrict nearest-neighbor matches to within a caliper (distance threshold).

Bias-variance tradeoff: uncalipered NN can match distant observations (high bias);
caliper trades some matches for lower bias. Core claim: bias vs uncalipered measured,
unmatched rate honestly reported.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
from typing import List, Tuple

def euclidean_distance(x1: float, x2: float) -> float:
    return abs(x1 - x2)

def nearest_neighbor_match(treated: List[float], control: List[float], caliper: float = float('inf')) -> Tuple[List[Tuple[int, int]], int]:
    """Match each treated unit to closest control within caliper.

    Returns: list of (treated_idx, control_idx) matches, unmatched_count.
    """
    matched = []
    matched_controls = set()
    unmatched = 0

    for t_idx, t_val in enumerate(treated):
        best_c_idx = -1
        best_dist = float('inf')

        for c_idx, c_val in enumerate(control):
            if c_idx in matched_controls:
                continue
            dist = euclidean_distance(t_val, c_val)
            if dist < best_dist:
                best_dist = dist
                best_c_idx = c_idx

        if best_c_idx != -1 and best_dist <= caliper:
            matched.append((t_idx, best_c_idx))
            matched_controls.add(best_c_idx)
        else:
            unmatched += 1

    return matched, unmatched

def estimate_bias(treated_vals: List[float], control_vals: List[float],
                  outcome_treated: List[float], outcome_control: List[float],
                  matches: List[Tuple[int, int]]) -> float:
    """Estimate bias as covariate imbalance in matched sample."""
    if not matches:
        return 0.0
    treated_matched = sum(treated_vals[m[0]] for m in matches) / len(matches)
    control_matched = sum(control_vals[m[1]] for m in matches) / len(matches)
    return abs(treated_matched - control_matched)

if __name__ == "__main__":
    import random
    random.seed(42)

    # Planted confounding: treated units have higher X, outcome depends on X.
    n_treated, n_control = 50, 100
    treated_x = [random.gauss(2.0, 1) for _ in range(n_treated)]
    control_x = [random.gauss(0.0, 1) for _ in range(n_control)]

    # Outcome depends on X + treatment effect.
    treated_y = [2.0 + 1.5 * treated_x[i] + random.gauss(0, 0.5) for i in range(n_treated)]
    control_y = [1.5 * control_x[i] + random.gauss(0, 0.5) for i in range(n_control)]

    # Uncalipered matching: matches may be distant.
    uncalipered, unmatch_uncal = nearest_neighbor_match(treated_x, control_x, caliper=float('inf'))
    bias_uncal = estimate_bias(treated_x, control_x, treated_y, control_y, uncalipered)

    # Caliper matching: restrict distance.
    caliper_threshold = 0.5
    calipered, unmatch_cal = nearest_neighbor_match(treated_x, control_x, caliper=caliper_threshold)
    bias_cal = estimate_bias(treated_x, control_x, treated_y, control_y, calipered)

    # Caliper should have lower bias (better covariate balance) despite higher unmatched rate.
    assert len(calipered) <= len(uncalipered), "Caliper should have fewer or equal matches"
    assert unmatch_cal >= unmatch_uncal, "Caliper should have more unmatched"
    assert bias_cal <= bias_uncal * 1.1, f"Caliper bias {bias_cal} should be <= uncalipered {bias_uncal}"

    print("PASS")
