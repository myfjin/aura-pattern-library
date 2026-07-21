"""
Gaussian Mixture Model (1D) via Expectation-Maximization (from scratch).

Core idea: Model data as a mixture of k Gaussian distributions. EM iteratively
infers cluster responsibilities (E-step) and updates Gaussian parameters (M-step).
Converges to a local maximum of the likelihood.

When to use: Soft clustering; probabilistic model of data; identifying mixture components.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import math
from typing import List, Tuple




class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_em_fit_1d(max_iterations, tolerance):
    v = []
    if isinstance(max_iterations, (int, float)) and max_iterations <= 0:
        v.append(f"AURA-E009: max_iterations must be > 0, got {max_iterations}")
    if isinstance(tolerance, (int, float)) and not math.isfinite(tolerance):
        v.append(f"AURA-E008: tolerance must be finite, got {tolerance}")
    if isinstance(tolerance, (int, float)) and tolerance <= 0:
        v.append(f"AURA-E009: tolerance must be > 0, got {tolerance}")
    if v:
        raise AuraInputError(v)

def _aura_validate_normal_pdf(x, var):
    v = []
    if isinstance(x, (int, float)) and not math.isfinite(x):
        v.append(f"AURA-E008: x must be finite, got {x}")
    if isinstance(var, (int, float)) and not math.isfinite(var):
        v.append(f"AURA-E008: var must be finite, got {var}")
    if isinstance(var, (int, float)) and var < 0:
        v.append(f"AURA-E-B5: var must be >= 0, got {var}")
    if v:
        raise AuraInputError(v)

def normal_pdf(x: float, mean: float, var: float) -> float:
    """Compute Gaussian PDF value at x."""
    _aura_validate_normal_pdf(x, var)
    if var <= 0:
        return 0.0
    return math.exp(-0.5 * ((x - mean) ** 2) / var) / math.sqrt(2 * math.pi * var)


def em_fit_1d(
    X: List[float],
    k: int,
    max_iterations: int = 100,
    tolerance: float = 1e-6
) -> Tuple[List[float], List[float], List[float]]:
    """
    Fit 1D Gaussian Mixture Model using EM.

    Args:
        X: list of scalar data points
        k: number of mixture components
        max_iterations: maximum EM iterations
        tolerance: convergence threshold for log-likelihood

    Returns:
        (means, variances, weights): parameters of k Gaussians and their mixture weights
    """
    _aura_validate_em_fit_1d(max_iterations, tolerance)
    n_samples = len(X)

    # Initialize: random means, equal variances, equal weights
    means = [X[random.randint(0, n_samples - 1)] for _ in range(k)]
    variances = [1.0] * k
    weights = [1.0 / k] * k

    prev_log_likelihood = -float('inf')

    for iteration in range(max_iterations):
        # E-step: compute responsibilities (soft assignments)
        responsibilities = []
        for i in range(n_samples):
            # Compute P(x_i | component j) * P(component j) for all j
            likelihoods = [weights[j] * normal_pdf(X[i], means[j], variances[j])
                          for j in range(k)]
            total = sum(likelihoods)

            if total > 0:
                resp = [likelihoods[j] / total for j in range(k)]
            else:
                resp = [1.0 / k] * k  # Uniform if all likelihoods are zero

            responsibilities.append(resp)

        # M-step: update parameters
        Nk = [sum(responsibilities[i][j] for i in range(n_samples)) for j in range(k)]

        new_weights = [Nk[j] / n_samples for j in range(k)]

        new_means = []
        for j in range(k):
            if Nk[j] > 0:
                mean_j = sum(responsibilities[i][j] * X[i] for i in range(n_samples)) / Nk[j]
            else:
                mean_j = means[j]
            new_means.append(mean_j)

        new_variances = []
        for j in range(k):
            if Nk[j] > 0:
                var_j = sum(responsibilities[i][j] * (X[i] - new_means[j]) ** 2
                           for i in range(n_samples)) / Nk[j]
            else:
                var_j = variances[j]
            new_variances.append(max(var_j, 1e-6))  # Avoid zero variance

        means = new_means
        variances = new_variances
        weights = new_weights

        # Compute log-likelihood for convergence check
        log_likelihood = 0.0
        for i in range(n_samples):
            likelihood = sum(weights[j] * normal_pdf(X[i], means[j], variances[j])
                            for j in range(k))
            if likelihood > 0:
                log_likelihood += math.log(likelihood)

        if abs(log_likelihood - prev_log_likelihood) < tolerance:
            break

        prev_log_likelihood = log_likelihood

    return means, variances, weights


def gmm_predict_responsibilities(
    X: List[float],
    means: List[float],
    variances: List[float],
    weights: List[float]
) -> List[List[float]]:
    """Compute soft assignments (responsibilities) for new data."""
    k = len(means)
    responsibilities = []

    for x in X:
        likelihoods = [weights[j] * normal_pdf(x, means[j], variances[j])
                      for j in range(k)]
        total = sum(likelihoods)

        if total > 0:
            resp = [likelihoods[j] / total for j in range(k)]
        else:
            resp = [1.0 / k] * k

        responsibilities.append(resp)

    return responsibilities


if __name__ == "__main__":
    random.seed(42)

    # Generate synthetic data: mixture of 2 Gaussians
    n_per_component = 25
    X = []

    # Component 0: mean = 0, var = 1
    for _ in range(n_per_component):
        X.append(random.gauss(0, 1))

    # Component 1: mean = 5, var = 1
    for _ in range(n_per_component):
        X.append(random.gauss(5, 1))

    # Fit GMM with k=2
    means, variances, weights = em_fit_1d(X, k=2, max_iterations=100)

    # Check: we should recover 2 well-separated means
    # (could be in either order)
    means_sorted = sorted(means)
    assert means_sorted[0] < 2.5, f"First mean {means_sorted[0]} should be close to 0"
    assert means_sorted[1] > 2.5, f"Second mean {means_sorted[1]} should be close to 5"
    assert abs(means_sorted[0]) < 1.5, f"First mean too far from 0"
    assert abs(means_sorted[1] - 5.0) < 1.5, f"Second mean too far from 5"

    # Verify all variances are positive
    assert all(v > 0 for v in variances), "Variances should be positive"

    # Verify weights sum to 1
    assert abs(sum(weights) - 1.0) < 1e-5, "Weights should sum to 1"

    print(f"GAUSSIAN_MIXTURE_EM PASS: means = {[f'{m:.2f}' for m in means_sorted]}, variances = {[f'{v:.2f}' for v in variances]}")
