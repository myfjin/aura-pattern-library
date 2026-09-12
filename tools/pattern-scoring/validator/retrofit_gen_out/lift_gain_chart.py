import math
"""
Lift & Gain Chart

Computes cumulative gain (% of positives captured) and lift (gain / base rate) by decile.
Lift > 1 indicates the model is better than random.

Use this in marketing/targeting to quantify how much better a model ranks customers than random.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
from typing import List, Tuple




class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_generate_scored_labels(n_positive, n_negative):
    v = []
    if isinstance(n_positive, (int, float)) and n_positive <= 0:
        v.append(f"AURA-E009: n_positive must be > 0, got {n_positive}")
    if isinstance(n_negative, (int, float)) and n_negative <= 0:
        v.append(f"AURA-E009: n_negative must be > 0, got {n_negative}")
    if v:
        raise AuraInputError(v)

def _aura_validate_lift_gain_chart(n_deciles):
    v = []
    if isinstance(n_deciles, (int, float)) and n_deciles <= 0:
        v.append(f"AURA-E009: n_deciles must be > 0, got {n_deciles}")
    if v:
        raise AuraInputError(v)



class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_generate_scored_labels(signal_strength):
    v = []
    if isinstance(signal_strength, (int, float)) and not math.isfinite(signal_strength):
        v.append(f"AURA-E008: signal_strength must be finite, got {signal_strength}")
    if v:
        raise AuraInputError(v)

def generate_scored_labels(
    n_positive: int, n_negative: int, signal_strength: float, seed: int
) -> List[Tuple[float, int]]:
    """
    Generate predicted scores and true labels.
    Positive labels have higher scores proportional to signal_strength.
    """
    _aura_validate_generate_scored_labels(signal_strength)
    _aura_validate_generate_scored_labels(n_positive, n_negative)
    random.seed(seed)
    data = []

    # Positive class: scores centered higher
    for _ in range(n_positive):
        score = 0.5 + signal_strength * 0.3 + random.gauss(0, 0.15)
        score = max(0, min(1, score))
        data.append((score, 1))

    # Negative class: scores centered lower
    for _ in range(n_negative):
        score = 0.5 - signal_strength * 0.3 + random.gauss(0, 0.15)
        score = max(0, min(1, score))
        data.append((score, 0))

    return data


def lift_gain_chart(scores: List[float], labels: List[int], n_deciles: int = 10) -> Tuple[List[float], List[float], List[float]]:
    """
    Compute gain and lift by decile.
    Returns (decile_percentages, gains, lifts).
    """
    _aura_validate_lift_gain_chart(n_deciles)
    # Sort by score descending
    scored_labels = sorted(zip(scores, labels), key=lambda x: -x[0])
    labels_sorted = [l for s, l in scored_labels]

    n_total = len(labels_sorted)
    n_positive = sum(labels_sorted)
    base_rate = n_positive / n_total if n_total > 0 else 0

    decile_percentages = []
    gains = []
    lifts = []

    for decile in range(1, n_deciles + 1):
        # Top decile% of population
        n_in_decile = max(1, (decile * n_total) // n_deciles)
        n_pos_in_decile = sum(labels_sorted[:n_in_decile])

        # Cumulative gain: % of positives captured in top decile%
        gain = (n_pos_in_decile / n_positive) * 100 if n_positive > 0 else 0

        # Lift: actual positive rate in decile / base rate
        pos_rate_in_decile = n_pos_in_decile / n_in_decile if n_in_decile > 0 else 0
        lift = pos_rate_in_decile / base_rate if base_rate > 0 else 1.0

        decile_percentages.append(decile * 10)
        gains.append(gain)
        lifts.append(lift)

    return decile_percentages, gains, lifts


def test_lift_gain() -> None:
    """
    Test lift and gain: strong classifier should have high lift in top decile,
    random classifier should have lift ≈ 1 throughout.
    """
    random.seed(42)

    # Strong classifier (signal_strength = 0.8)
    data_strong = generate_scored_labels(100, 400, signal_strength=0.8, seed=42)
    scores_strong = [s for s, l in data_strong]
    labels_strong = [l for s, l in data_strong]

    deciles_strong, gains_strong, lifts_strong = lift_gain_chart(scores_strong, labels_strong)

    # Random classifier (signal_strength = 0)
    random.seed(42)
    data_random = generate_scored_labels(100, 400, signal_strength=0.0, seed=42)
    scores_random = [s for s, l in data_random]
    labels_random = [l for s, l in data_random]

    deciles_random, gains_random, lifts_random = lift_gain_chart(scores_random, labels_random)

    # Verify: strong classifier top decile lift should be >> 1
    assert lifts_strong[0] > 1.5, f"Strong classifier top decile lift should be high: {lifts_strong[0]}"

    # Random classifier lift should be close to 1
    avg_lift_random = sum(lifts_random) / len(lifts_random)
    assert 0.7 < avg_lift_random < 1.3, f"Random classifier average lift should be near 1: {avg_lift_random}"

    # Strong classifier should capture more positives at top decile
    assert gains_strong[0] > gains_random[0], f"Strong gain should exceed random: {gains_strong[0]} vs {gains_random[0]}"

    print("lift_gain_chart.py: PASS")


if __name__ == "__main__":
    test_lift_gain()
