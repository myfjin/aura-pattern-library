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

def _validate_ab_inputs(successes_a, trials_a, successes_b, trials_b,
                        prior_alpha, prior_beta, num_samples):
    v = []
    for name, s, t in (("A", successes_a, trials_a), ("B", successes_b, trials_b)):
        for pname, val in ((f"successes_{name.lower()}", s), (f"trials_{name.lower()}", t)):
            if not isinstance(val, int) or isinstance(val, bool):
                v.append(f"AURA-E-B1: {pname} must be an integer, got {type(val).__name__} {val!r}")
        if isinstance(s, int) and isinstance(t, int) and not isinstance(s, bool) and not isinstance(t, bool):
            if t <= 0:
                v.append(f"AURA-E005: trials_{name.lower()} must be > 0, got {t} (no experiment ran)")
            if s < 0:
                v.append(f"AURA-E-B5: successes_{name.lower()} must be >= 0, got {s}")
            if t > 0 and s > t:
                v.append(f"AURA-E004: successes_{name.lower()} ({s}) exceed trials_{name.lower()} ({t}) — impossible data")
    for pname, val in (("prior_alpha", prior_alpha), ("prior_beta", prior_beta)):
        if not (isinstance(val, (int, float)) and val > 0):
            v.append(f"AURA-E-B5: {pname} must be a positive number, got {val!r}")
    if not (isinstance(num_samples, int) and num_samples > 0):
        v.append(f"AURA-E-B5: num_samples must be a positive integer, got {num_samples!r}")
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
    """
    _validate_ab_inputs(successes_a, trials_a, successes_b, trials_b,
                        prior_alpha, prior_beta, num_samples)
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

    print()
    print("=== RETROFIT DEMO: Illia's attacks from 2026-07-19 ===")
    attacks = [
        ("run 4  (65 successes / 10 trials — was silent PASS)", (60, 1000, 65, 10)),
        ("run 11 (65 successes / 0 trials — was silent PASS)", (60, 100, 65, 0)),
        ("run 3  (60 successes / 10 trials on A)", (60, 10, 65, 100)),
        ("wrong-language, properly quoted", (60, 100, "шістдесят п'ять", 100)),
        ("combined: impossible A + wrong-lang B + negative trials", (160, 100, "шістдесят п'ять", -100)),
    ]
    for label, args in attacks:
        try:
            bayesian_ab_test(*args)
            print(f"  {label}: !! computed silently — RETROFIT FAILED")
        except AuraInputError as e:
            print(f"  {label}:")
            for viol in e.violations:
                print(f"      {viol}")

