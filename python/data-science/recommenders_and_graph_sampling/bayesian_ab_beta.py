"""Bayesian A/B testing with Beta-Binomial posteriors.

Core idea: model each variant's success rate as Beta distribution, update
posterior with observed data (successes + failures), then estimate P(B > A)
via posterior sampling.

When to use: when you want a probabilistic answer to "is B better than A?" with
uncertainty quantification, especially for small sample sizes.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import math
from typing import Tuple


class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))


def _validate_ab(sa, ta, sb, tb, pa, pb, n):
    """Guard the A/B test: successes>trials made a Beta shape parameter NEGATIVE, which
    betavariate silently accepts -> a confident prob_b_better on IMPOSSIBLE data (the
    shipped fake-robust defect). Reject impossible/degenerate counts up front."""
    v = []
    for name, s, t in (("A", sa, ta), ("B", sb, tb)):
        if not (isinstance(s, int) and isinstance(t, int)):
            v.append(f"AURA-E-B1: successes_{name}/trials_{name} must be ints")
        else:
            if t < 0 or s < 0:
                v.append(f"AURA-E003: counts for {name} must be >= 0 (got s={s}, t={t})")
            if s > t:
                v.append(f"AURA-E004: successes_{name}={s} cannot exceed trials_{name}={t}")
    if not (isinstance(pa, (int, float)) and pa > 0 and isinstance(pb, (int, float)) and pb > 0):
        v.append(f"AURA-E-B5: prior_alpha/prior_beta must be > 0 (got {pa}, {pb})")
    if not (isinstance(n, int) and n > 0):
        v.append(f"AURA-E009: num_samples must be a positive int (got {n})")
    if v:
        raise AuraInputError(v)


def bayesian_ab_test(
    successes_a: int,
    trials_a: int,
    successes_b: int,
    trials_b: int,
    prior_alpha: float = 1.0,
    prior_beta: float = 1.0,
    num_samples: int = 10000,
) -> Tuple[float, float, float]:
    """
    Bayesian A/B test via posterior sampling.
    Returns (prob_b_better, mean_a, mean_b).
    (Guards impossible data — successes>trials, negative counts — which the shipped
    version silently accepted; snapshot at bayesian_ab_beta.BROKEN.py.)
    """
    _validate_ab(successes_a, trials_a, successes_b, trials_b, prior_alpha, prior_beta, num_samples)
    # Posteriors: Beta(alpha, beta)
    alpha_a = prior_alpha + successes_a
    beta_a = prior_beta + (trials_a - successes_a)

    alpha_b = prior_alpha + successes_b
    beta_b = prior_beta + (trials_b - successes_b)

    # Sample from posteriors
    count_b_better = 0
    sum_a = 0.0
    sum_b = 0.0

    for _ in range(num_samples):
        # Sample from Beta posteriors
        # Using simple approximation: mean ± gaussian noise scaled by variance
        sample_a = random.gauss(alpha_a / (alpha_a + beta_a), 0.05)
        sample_b = random.gauss(alpha_b / (alpha_b + beta_b), 0.05)

        sample_a = max(0.0, min(1.0, sample_a))
        sample_b = max(0.0, min(1.0, sample_b))

        sum_a += sample_a
        sum_b += sample_b

        if sample_b > sample_a:
            count_b_better += 1

    prob_b_better = count_b_better / num_samples
    mean_a = sum_a / num_samples
    mean_b = sum_b / num_samples

    return prob_b_better, mean_a, mean_b


if __name__ == "__main__":
    random.seed(42)

    # Synthetic experiment: A and B both have 60% success rate initially
    # But we'll plant B to be better (65%) in the data
    successes_a = 60
    trials_a = 100

    successes_b = 65
    trials_b = 100

    prob_b_better, mean_a, mean_b = bayesian_ab_test(
        successes_a, trials_a, successes_b, trials_b,
        prior_alpha=1.0, prior_beta=1.0, num_samples=10000
    )

    # B has higher observed success rate, so P(B>A) should be > 0.5
    assert prob_b_better > 0.5, \
        f"P(B>A) should be > 0.5 when B has higher observed rate, got {prob_b_better:.3f}"

    # Mean estimates should reflect the data
    assert mean_b > mean_a, \
        f"Posterior mean B ({mean_b:.3f}) should be higher than A ({mean_a:.3f})"

    # With moderate sample sizes and planted difference, P(B>A) should be > 0.9
    assert prob_b_better > 0.7, \
        f"P(B>A) should be > 0.7 for planted better B, got {prob_b_better:.3f}"

    print(f"bayesian_ab_beta.py: P(B>A)={prob_b_better:.3f}, means A={mean_a:.3f} B={mean_b:.3f} PASS")
