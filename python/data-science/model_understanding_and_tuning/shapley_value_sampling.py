"""
Shapley Value Sampling (Monte Carlo Approximation)

Core idea: Estimate each feature's marginal contribution via random coalition sampling.
For a simple additive model, sampled Shapley values should match analytic per-feature contributions.

When to use: You want fair feature attribution that respects coalition marginal values, without
computing all 2^n coalitions exactly.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import statistics
from typing import List, Tuple, Callable
from itertools import combinations


def additive_model(features: List[float]) -> float:
    """Simple additive model: sum of each feature weighted by its index + 1."""
    return sum(f * (i + 1) for i, f in enumerate(features))


def coalition_value(features: List[float], coalition_idx: List[int], baseline: List[float]) -> float:
    """
    Compute the value of a coalition.
    coalition_idx: indices of features in the coalition.
    baseline: feature values outside the coalition (replaced with 0).
    """
    result = [baseline[i] if i in coalition_idx else 0 for i in range(len(features))]
    return additive_model(result)


def shapley_value_sample(
    feature_idx: int,
    num_features: int,
    num_samples: int,
    feature_values: List[float]
) -> float:
    """
    Estimate Shapley value for feature_idx via Monte Carlo sampling.
    For each sample: randomly order features, compute marginal contribution.
    """
    marginal_contributions = []

    for _ in range(num_samples):
        # Random permutation
        perm = list(range(num_features))
        random.shuffle(perm)

        # Find position of feature_idx in permutation
        pos = perm.index(feature_idx)

        # Compute marginal contribution: v(S ∪ {i}) - v(S)
        # S = predecessors in random order
        coalition_without = perm[:pos]
        coalition_with = perm[:pos + 1]

        val_without = coalition_value(feature_values, coalition_without, feature_values)
        val_with = coalition_value(feature_values, coalition_with, feature_values)

        marginal = val_with - val_without
        marginal_contributions.append(marginal)

    return statistics.mean(marginal_contributions)


def analytic_shapley(feature_idx: int, feature_values: List[float]) -> float:
    """
    Analytic Shapley for additive model: each feature's contribution is simply weight * feature_value.
    For additive model f(x) = sum(w_i * x_i), Shapley value for feature i is w_i * x_i.
    """
    weight = feature_idx + 1  # Weight is index + 1
    return weight * feature_values[feature_idx]


if __name__ == "__main__":
    random.seed(42)

    num_features = 4
    feature_values = [2.0, 3.0, 1.5, 2.5]

    print("Shapley Value Estimation (Additive Model)")
    print("=" * 50)

    max_error = 0.0
    for feat_idx in range(num_features):
        # Sampled Shapley
        sampled = shapley_value_sample(feat_idx, num_features, 500, feature_values)

        # Analytic Shapley
        analytic = analytic_shapley(feat_idx, feature_values)

        error = abs(sampled - analytic)
        max_error = max(max_error, error)

        print(f"Feature {feat_idx}: Sampled {sampled:.4f}, Analytic {analytic:.4f}, Error {error:.4f}")

    # Assertion: sampled Shapley values match analytic within tolerance
    assert max_error < 0.5, f"Max error should be within tolerance: {max_error}"
    assert max_error < analytic_shapley(0, feature_values) * 0.3, "Error should be < 30% of max contribution"

    print("✓ Shapley Value Sampling: PASS")
