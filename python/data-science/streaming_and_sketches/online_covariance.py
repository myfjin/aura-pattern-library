"""
Online Covariance & Correlation via Welford's Method

Core idea: Update mean, variance, and covariance in a single pass via numerically-stable
incremental formulas. Matches batch computation to machine precision.

When to use: You have streaming data and need covariance/correlation, or want numerically
stable alternatives to naive summation.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import math
from typing import List, Tuple


class OnlineCovarianceEstimator:
    """Compute covariance/correlation online using Welford's method."""

    def __init__(self, n_vars: int = 2):
        self.n_vars = n_vars
        self.n = 0
        self.means = [0.0] * n_vars
        self.M2 = [[0.0] * n_vars for _ in range(n_vars)]  # Covariance matrix

    def process(self, point: List[float]) -> None:
        """Process a new multivariate data point."""
        self.n += 1

        # Update means and M2
        deltas = [x - m for x, m in zip(point, self.means)]

        for i in range(self.n_vars):
            self.means[i] += deltas[i] / self.n

        delta_primes = [x - m for x, m in zip(point, self.means)]

        for i in range(self.n_vars):
            for j in range(self.n_vars):
                self.M2[i][j] += deltas[i] * delta_primes[j]

    def get_covariance(self, unbiased: bool = True) -> List[List[float]]:
        """Return covariance matrix."""
        if self.n < 2:
            return self.M2

        divisor = self.n - 1 if unbiased else self.n
        return [[self.M2[i][j] / divisor for j in range(self.n_vars)] for i in range(self.n_vars)]

    def get_correlation(self) -> List[List[float]]:
        """Return correlation matrix (normalized covariance)."""
        cov = self.get_covariance()
        corr = [[0.0] * self.n_vars for _ in range(self.n_vars)]

        for i in range(self.n_vars):
            for j in range(self.n_vars):
                std_i = math.sqrt(cov[i][i]) if cov[i][i] > 0 else 1.0
                std_j = math.sqrt(cov[j][j]) if cov[j][j] > 0 else 1.0
                corr[i][j] = cov[i][j] / (std_i * std_j)

        return corr


def batch_covariance(data: List[List[float]]) -> List[List[float]]:
    """Compute covariance matrix batch-style (for comparison)."""
    n = len(data)
    n_vars = len(data[0])

    # Means
    means = [sum(row[i] for row in data) / n for i in range(n_vars)]

    # Covariance
    cov = [[0.0] * n_vars for _ in range(n_vars)]
    for row in data:
        for i in range(n_vars):
            for j in range(n_vars):
                cov[i][j] += (row[i] - means[i]) * (row[j] - means[j])

    # Normalize
    cov = [[c / (n - 1) for c in row] for row in cov]

    return cov


if __name__ == "__main__":
    random.seed(42)

    # Generate bivariate data: x ~ N(0, 1), y ~ N(0, 1), correlated
    data = []
    for _ in range(500):
        x = random.gauss(0, 1)
        y = 0.7 * x + random.gauss(0, 0.5)  # y correlated with x
        data.append([x, y])

    # Batch covariance (ground truth)
    batch_cov = batch_covariance(data)

    # Online covariance
    online_est = OnlineCovarianceEstimator(n_vars=2)
    for point in data:
        online_est.process(point)

    online_cov = online_est.get_covariance()
    online_corr = online_est.get_correlation()

    print(f"Batch covariance: {[[f'{c:.6f}' for c in row] for row in batch_cov]}")
    print(f"Online covariance: {[[f'{c:.6f}' for c in row] for row in online_cov]}")

    # Compute error
    max_error = 0.0
    for i in range(2):
        for j in range(2):
            error = abs(batch_cov[i][j] - online_cov[i][j])
            max_error = max(max_error, error)

    print(f"Max covariance error: {max_error:.2e}")
    print(f"Correlation: {online_corr[0][1]:.6f} (expected ~0.7 * std_x / std_y)")

    # Assertion: online should match batch to machine precision
    assert max_error < 1e-9, f"Covariance error too large: {max_error}"
    assert 0.5 < online_corr[0][1] < 1.0, f"Correlation should be in reasonable range: {online_corr[0][1]}"

    print("✓ Online Covariance: PASS")
