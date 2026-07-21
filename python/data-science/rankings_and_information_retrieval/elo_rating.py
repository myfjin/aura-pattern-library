"""
Elo Rating System.

Maintain skill ratings via pairwise wins/losses.
Elo(new) = Elo(old) + K * (observed - expected).
Expected score = 1 / (1 + 10^((opponent_elo - my_elo)/400)).
We plant a stronger player and verify their Elo converges higher; hand-verify
the expected-score formula against observed win rate.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
from typing import Dict, Tuple




class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_expected_score(elo1, elo2):
    v = []
    if isinstance(elo1, (int, float)) and not math.isfinite(elo1):
        v.append(f"AURA-E008: elo1 must be finite, got {elo1}")
    if isinstance(elo2, (int, float)) and not math.isfinite(elo2):
        v.append(f"AURA-E008: elo2 must be finite, got {elo2}")
    if v:
        raise AuraInputError(v)

def _aura_validate_update_elo(opponent_elo, k):
    v = []
    if isinstance(opponent_elo, (int, float)) and not math.isfinite(opponent_elo):
        v.append(f"AURA-E008: opponent_elo must be finite, got {opponent_elo}")
    if isinstance(opponent_elo, (int, float)) and opponent_elo <= 0:
        v.append(f"AURA-E009: opponent_elo must be > 0, got {opponent_elo}")
    if isinstance(k, (int, float)) and k <= 0:
        v.append(f"AURA-E009: k must be > 0, got {k}")
    if v:
        raise AuraInputError(v)

def expected_score(elo1: float, elo2: float) -> float:
    """Expected score for player1 vs player2."""
    _aura_validate_expected_score(elo1, elo2)
    return 1.0 / (1.0 + 10.0 ** ((elo2 - elo1) / 400.0))


def update_elo(elo: float, opponent_elo: float, observed_score: float, k: float = 32.0) -> float:
    """Update Elo: new_elo = elo + k * (observed - expected)."""
    _aura_validate_update_elo(opponent_elo, k)
    expected = expected_score(elo, opponent_elo)
    return elo + k * (observed_score - expected)


if __name__ == "__main__":
    import random

    random.seed(42)

    # Simulate matches between two players
    # Player A: true skill 55% win rate (slightly better)
    # Player B: true skill 45% win rate
    true_win_rate_a = 0.55

    # Initialize both at 1600 Elo
    elo_a, elo_b = 1600.0, 1600.0
    k = 32.0

    num_matches = 100

    for _ in range(num_matches):
        # Determine winner based on true skill (55% for A)
        a_wins = random.random() < true_win_rate_a

        # Update Elo
        if a_wins:
            elo_a = update_elo(elo_a, elo_b, 1.0, k)
            elo_b = update_elo(elo_b, elo_a, 0.0, k)
        else:
            elo_a = update_elo(elo_a, elo_b, 0.0, k)
            elo_b = update_elo(elo_b, elo_a, 1.0, k)

    # After 100 matches with true 55-45 split, A should have higher Elo
    assert elo_a > elo_b, (
        f"After 100 matches with 55% win rate for A, A's Elo {elo_a:.1f} "
        f"should be > B's {elo_b:.1f}"
    )

    # Hand-verify expected score formula:
    # If A has Elo 1700 and B has Elo 1600:
    # Expected for A = 1 / (1 + 10^((1600-1700)/400)) = 1 / (1 + 10^(-0.25)) = 1 / (1 + 0.562) = 0.64
    test_elo_a = 1700.0
    test_elo_b = 1600.0
    expected_a = expected_score(test_elo_a, test_elo_b)
    expected_a_manual = 1.0 / (1.0 + 10.0 ** (-0.25))

    assert abs(expected_a - expected_a_manual) < 0.001, (
        f"Expected score mismatch: {expected_a:.4f} vs {expected_a_manual:.4f}"
    )
    assert abs(expected_a - 0.64) < 0.01, (
        f"Expected score for 100-Elo advantage should be ~0.64, got {expected_a:.2f}"
    )

    elo_diff = elo_a - elo_b

    print(
        f"After {num_matches} matches (true 55-45 split): "
        f"Elo A={elo_a:.1f} | Elo B={elo_b:.1f} | Diff={elo_diff:.1f} | "
        f"Expected(1700 vs 1600)={expected_a:.2f} | PASS"
    )
