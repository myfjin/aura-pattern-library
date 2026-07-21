"""
Bootstrap Model Comparison

Compares two models using paired bootstrap resampling on the same test set.
Computes the win rate: how often Model A is better than Model B across bootstrap samples.

Use this to determine whether observed performance difference is statistically significant,
or could be due to random variation in the test set.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import math
from typing import List, Tuple, Callable


def generate_test_data(n: int, seed: int) -> List[Tuple[float, float]]:
    """Generate synthetic test data: y = 2*x + noise."""
    random.seed(seed)
    data = []
    for _ in range(n):
        x = random.uniform(-5, 5)
        y = 2 * x + random.gauss(0, 1)
        data.append((x, y))
    return data


def model_a(x: float) -> float:
    """Good model: 2*x (true function)."""
    return 2 * x


def model_b(x: float) -> float:
    """Mediocre model: 1.8*x (biased)."""
    return 1.8 * x


def mean_absolute_error(
    y_true: List[float], y_pred: List[float]
) -> float:
    """Compute MAE."""
    return sum(abs(yt - yp) for yt, yp in zip(y_true, y_pred)) / len(y_true)




class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_bootstrap_model_comparison(n_bootstraps):
    v = []
    if isinstance(n_bootstraps, (int, float)) and n_bootstraps <= 0:
        v.append(f"AURA-E009: n_bootstraps must be > 0, got {n_bootstraps}")
    if v:
        raise AuraInputError(v)

def bootstrap_model_comparison(
    test_data: List[Tuple[float, float]],
    model1: Callable[[float], float],
    model2: Callable[[float], float],
    n_bootstraps: int = 100,
) -> Tuple[int, int, float]:
    """
    Compare two models using bootstrap resampling.
    Returns (wins_model1, wins_model2, win_rate_model1).
    """
    _aura_validate_bootstrap_model_comparison(n_bootstraps)
    wins1 = 0
    wins2 = 0

    for _ in range(n_bootstraps):
        # Resample test set with replacement
        boot_sample = [random.choice(test_data) for _ in range(len(test_data))]
        x_list = [x for x, y in boot_sample]
        y_list = [y for x, y in boot_sample]

        # Compute MAE for both models
        pred1 = [model1(x) for x in x_list]
        pred2 = [model2(x) for x in x_list]

        mae1 = mean_absolute_error(y_list, pred1)
        mae2 = mean_absolute_error(y_list, pred2)

        # Lower MAE is better
        if mae1 < mae2:
            wins1 += 1
        elif mae2 < mae1:
            wins2 += 1

    win_rate1 = wins1 / n_bootstraps if n_bootstraps > 0 else 0
    return wins1, wins2, win_rate1


def test_bootstrap_comparison() -> None:
    """
    Test bootstrap comparison:
    - Model A is better than Model B: A should win most bootstrap samples
    - Two identical models should have win rate ≈ 0.5
    """
    random.seed(42)

    # Test data
    test_data = generate_test_data(200, seed=42)

    # Model A vs Model B (A is better)
    wins_a, wins_b, win_rate_a = bootstrap_model_comparison(
        test_data, model_a, model_b, n_bootstraps=100
    )

    # Model A should win significantly more often
    assert win_rate_a > 0.7, f"Better model should win >70% of samples: {win_rate_a}"

    # Test identical models
    wins_same1, wins_same2, win_rate_same = bootstrap_model_comparison(
        test_data, model_a, model_a, n_bootstraps=100
    )

    # Identical models should have ~50/50 (ties count as ties)
    # But since they're identical, wins should be minimal
    assert wins_same1 + wins_same2 < 50, f"Identical models should have few wins: {wins_same1 + wins_same2}"

    print("bootstrap_model_comparison.py: PASS")


if __name__ == "__main__":
    test_bootstrap_comparison()
