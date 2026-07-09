"""
Markov chain stationary distribution via power iteration.

Core idea: For a finite, ergodic Markov chain with transition matrix P, repeatedly multiply
a probability vector by P^T until it converges to π, the left eigenvector with eigenvalue 1.
The stationary distribution satisfies πP = π and is independent of the starting distribution.

Use when: computing long-run state probabilities, analyzing stochastic processes, checking
Markov chain convergence.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
from typing import List


def matrix_multiply(v: List[float], P: List[List[float]]) -> List[float]:
    """Multiply vector v by transition matrix P (left multiplication: v' = v * P)."""
    n = len(P)
    result = [0.0] * n
    for j in range(n):
        result[j] = sum(v[i] * P[i][j] for i in range(n))
    return result


def power_iteration_stationary(P: List[List[float]], max_iter: int = 1000, tol: float = 1e-9) -> List[float]:
    """
    Compute stationary distribution via power iteration.
    Starts from uniform distribution, multiplies by P repeatedly until convergence.
    """
    n = len(P)
    pi = [1.0 / n] * n  # Uniform start

    for iteration in range(max_iter):
        pi_new = matrix_multiply(pi, P)
        # Check convergence
        max_diff = max(abs(pi_new[i] - pi[i]) for i in range(n))
        if max_diff < tol:
            return pi_new
        pi = pi_new

    raise RuntimeError(f"Power iteration did not converge after {max_iter} iterations")


def verify_stationary(pi: List[float], P: List[List[float]], tol: float = 1e-9) -> bool:
    """Verify π*P ≈ π."""
    pi_P = matrix_multiply(pi, P)
    return all(abs(pi_P[i] - pi[i]) < tol for i in range(len(pi)))


if __name__ == "__main__":
    import random
    random.seed(42)

    # Test 1: 2-state Markov chain with known solution
    # P = [[0.7, 0.3], [0.4, 0.6]]
    # Stationary: π*P = π => π = [4/7, 3/7] analytically
    P_2state = [
        [0.7, 0.3],
        [0.4, 0.6]
    ]

    pi_computed = power_iteration_stationary(P_2state)
    pi_analytical = [4.0 / 7.0, 3.0 / 7.0]

    # Check convergence
    assert all(abs(pi_computed[i] - pi_analytical[i]) < 1e-6 for i in range(2)), (
        f"2-state chain: computed {pi_computed} vs analytical {pi_analytical}"
    )

    # Verify πP = π
    assert verify_stationary(pi_computed, P_2state), "π*P ≠ π for 2-state chain"

    # Test 2: 3-state symmetric chain (uniform stationary)
    P_3state = [
        [0.5, 0.25, 0.25],
        [0.25, 0.5, 0.25],
        [0.25, 0.25, 0.5]
    ]

    pi_3 = power_iteration_stationary(P_3state)
    pi_expected_3 = [1.0 / 3.0, 1.0 / 3.0, 1.0 / 3.0]

    assert all(abs(pi_3[i] - pi_expected_3[i]) < 1e-6 for i in range(3)), (
        f"3-state symmetric: computed {pi_3} vs expected uniform"
    )
    assert verify_stationary(pi_3, P_3state), "π*P ≠ π for 3-state chain"

    # Test 3: 4-state chain, arbitrary but ergodic
    P_4state = [
        [0.1, 0.4, 0.3, 0.2],
        [0.2, 0.1, 0.4, 0.3],
        [0.3, 0.2, 0.1, 0.4],
        [0.4, 0.3, 0.2, 0.1]
    ]

    pi_4 = power_iteration_stationary(P_4state)

    # Verify it's a valid probability distribution
    assert abs(sum(pi_4) - 1.0) < 1e-9, f"Stationary distribution should sum to 1, got {sum(pi_4)}"

    # Verify πP = π
    assert verify_stationary(pi_4, P_4state), "π*P ≠ π for 4-state chain"

    # Test 4: Different initial distributions converge to same π
    P_test = [
        [0.6, 0.4],
        [0.3, 0.7]
    ]

    # Start with deterministic distribution
    v1 = [1.0, 0.0]
    for _ in range(100):
        v1 = matrix_multiply(v1, P_test)

    # Start with different distribution
    v2 = [0.0, 1.0]
    for _ in range(100):
        v2 = matrix_multiply(v2, P_test)

    # Start with another
    v3 = [0.5, 0.5]
    for _ in range(100):
        v3 = matrix_multiply(v3, P_test)

    # All should converge to same π
    assert all(abs(v1[i] - v2[i]) < 1e-6 for i in range(2)), "Different starts should converge to same π"
    assert all(abs(v2[i] - v3[i]) < 1e-6 for i in range(2)), "Different starts should converge to same π"

    print("Markov chain stationary distribution (power iteration): all assertions PASS")
