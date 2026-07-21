"""
Expectation-Maximization (EM) Algorithm: Two-Coin Problem.

Estimates two coin biases from mixed flip sessions without labels.
The classic EM example: data is ambiguous (which coin produced each session?).
Use when data is incomplete or missing labels for mixture components.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import math
from typing import List, Tuple


def e_step(
    sessions: List[List[int]],  # 1=heads, 0=tails
    p_a: float,
    p_b: float,
    p_coin_a: float,
) -> Tuple[List[float], List[float]]:
    """
    E-step: compute posterior probability of coin A for each session.

    Args:
        sessions: list of flip sequences
        p_a, p_b: estimated biases
        p_coin_a: prior probability of coin A

    Returns:
        (posterior_a, posterior_b) for each session
    """
    posteriors_a = []
    posteriors_b = []

    for flips in sessions:
        # Likelihood of flips under coin A
        heads_a = sum(flips)
        tails_a = len(flips) - heads_a
        lik_a = (p_a ** heads_a) * ((1.0 - p_a) ** tails_a)

        # Likelihood under coin B
        lik_b = (p_b ** heads_a) * ((1.0 - p_b) ** tails_a)

        # Posterior (using equal prior for simplicity)
        post_a = lik_a / (lik_a + lik_b) if (lik_a + lik_b) > 0 else 0.5
        post_b = 1.0 - post_a

        posteriors_a.append(post_a)
        posteriors_b.append(post_b)

    return posteriors_a, posteriors_b


def m_step(
    sessions: List[List[int]],
    posteriors_a: List[float],
    posteriors_b: List[float],
) -> Tuple[float, float]:
    """
    M-step: update coin biases.

    Args:
        sessions: list of flip sequences
        posteriors_a, posteriors_b: posterior responsibilities

    Returns:
        (updated_p_a, updated_p_b)
    """
    sum_heads_a = 0.0
    sum_tails_a = 0.0
    sum_heads_b = 0.0
    sum_tails_b = 0.0

    for flips, post_a, post_b in zip(sessions, posteriors_a, posteriors_b):
        heads = sum(flips)
        tails = len(flips) - heads

        sum_heads_a += post_a * heads
        sum_tails_a += post_a * tails
        sum_heads_b += post_b * heads
        sum_tails_b += post_b * tails

    # Update biases
    p_a_new = sum_heads_a / (sum_heads_a + sum_tails_a) if (sum_heads_a + sum_tails_a) > 0 else 0.5
    p_b_new = sum_heads_b / (sum_heads_b + sum_tails_b) if (sum_heads_b + sum_tails_b) > 0 else 0.5

    return p_a_new, p_b_new




class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_em_two_coins(n_iter):
    v = []
    if isinstance(n_iter, (int, float)) and n_iter <= 0:
        v.append(f"AURA-E009: n_iter must be > 0, got {n_iter}")
    if v:
        raise AuraInputError(v)

def em_two_coins(
    sessions: List[List[int]],
    p_a_init: float = 0.6,
    p_b_init: float = 0.4,
    n_iter: int = 50,
) -> Tuple[float, float]:
    """
    Run EM to estimate coin biases.

    Args:
        sessions: list of flip sequences (1=heads, 0=tails)
        p_a_init, p_b_init: initial estimates
        n_iter: number of EM iterations

    Returns:
        (estimated_p_a, estimated_p_b)
    """
    _aura_validate_em_two_coins(n_iter)
    p_a = p_a_init
    p_b = p_b_init

    for _ in range(n_iter):
        # E-step
        post_a, post_b = e_step(sessions, p_a, p_b, 0.5)

        # M-step
        p_a, p_b = m_step(sessions, post_a, post_b)

    return p_a, p_b


if __name__ == "__main__":
    random.seed(42)

    # Plant true biases
    true_p_a = 0.8
    true_p_b = 0.3

    # Generate sessions: randomly choose which coin, with 50% prior for each
    n_sessions = 100
    flips_per_session = 30
    sessions = []

    for i in range(n_sessions):
        if random.random() < 0.5:
            # Use coin A
            flips = [1 if random.random() < true_p_a else 0 for _ in range(flips_per_session)]
        else:
            # Use coin B
            flips = [1 if random.random() < true_p_b else 0 for _ in range(flips_per_session)]
        sessions.append(flips)

    # Run EM with better initialization
    overall_heads = sum(sum(flips) for flips in sessions)
    overall_rate = overall_heads / (n_sessions * flips_per_session)
    p_a_init = overall_rate + 0.2
    p_b_init = overall_rate - 0.2
    p_a_init = min(0.99, max(0.01, p_a_init))
    p_b_init = min(0.99, max(0.01, p_b_init))

    estimated_p_a, estimated_p_b = em_two_coins(sessions, p_a_init=p_a_init, p_b_init=p_b_init, n_iter=100)

    # Verify recovery
    # Might recover (p_a, p_b) or (p_b, p_a) due to label switching
    pair_1_error = abs(estimated_p_a - true_p_a) + abs(estimated_p_b - true_p_b)
    pair_2_error = abs(estimated_p_a - true_p_b) + abs(estimated_p_b - true_p_a)

    min_error = min(pair_1_error, pair_2_error)
    assert min_error < 0.3, f"Recovery error {min_error} too large"

    print(f"em_two_coins.py: true=(p_a={true_p_a}, p_b={true_p_b}), estimated=(p_a={estimated_p_a:.3f}, p_b={estimated_p_b:.3f}), min_error={min_error:.3f} PASS")
