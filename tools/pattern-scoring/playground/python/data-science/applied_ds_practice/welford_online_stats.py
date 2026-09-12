"""
Welford's online algorithm for running mean and variance.

Welford's algorithm computes running mean and variance in a single pass with
O(1) memory and perfect numerical stability. It avoids the naive sum-of-squares
formula which catastrophically cancels when data has a large offset.

Use: streaming metrics, online parameter updates, memory-constrained environments.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
import random
from dataclasses import dataclass


@dataclass
class WelfordStats:
    """Accumulator for running mean and variance using Welford's algorithm."""
    count: int = 0
    mean: float = 0.0
    m2: float = 0.0  # Sum of squared differences from running mean

    def update(self, x: float) -> None:
        """Incorporate a new value into the running statistics."""
        self.count += 1
        delta = x - self.mean
        self.mean += delta / self.count
        delta2 = x - self.mean
        self.m2 += delta * delta2

    def variance(self) -> float:
        """Return sample variance (unbiased, requires count >= 2)."""
        if self.count < 2:
            return 0.0
        return self.m2 / (self.count - 1)

    def std_dev(self) -> float:
        """Return sample standard deviation."""
        return math.sqrt(self.variance())


def naive_variance(values: list[float]) -> float:
    """Naive sum-of-squares formula: E[X²] - E[X]² (numerically unstable)."""
    if len(values) < 2:
        return 0.0
    mean = sum(values) / len(values)
    sum_sq = sum(x**2 for x in values)
    n = len(values)
    # This can go negative or lose precision when values are large/offset
    var = (sum_sq / n) - (mean ** 2)
    return var * n / (n - 1) if var > 0 else 0.0


def batch_variance(values: list[float]) -> float:
    """Batch variance using sum of squared deviations (reference truth)."""
    if len(values) < 2:
        return 0.0
    mean = sum(values) / len(values)
    sum_sq_dev = sum((x - mean) ** 2 for x in values)
    return sum_sq_dev / (len(values) - 1)


if __name__ == "__main__":
    random.seed(42)

    # Test 1: Welford matches batch on normal data
    print("Test 1: Normal data (small offset)")
    normal_data = [random.gauss(0, 1) for _ in range(1000)]

    welford = WelfordStats()
    for x in normal_data:
        welford.update(x)

    batch_var = batch_variance(normal_data)
    welford_var = welford.variance()
    assert abs(welford_var - batch_var) < 1e-10, \
        f"Welford {welford_var} != batch {batch_var}"
    print(f"  Welford variance: {welford_var:.10f}")
    print(f"  Batch variance:   {batch_var:.10f}")
    print(f"  Match: ✓")

    # Test 2: Demonstrate naive formula failure with offset data
    print("\nTest 2: Large offset (1e10) — naive fails, Welford holds")
    offset = 1e10
    offset_data = [offset + random.gauss(0, 1) for _ in range(1000)]

    naive_var = naive_variance(offset_data)
    batch_var = batch_variance(offset_data)

    welford = WelfordStats()
    for x in offset_data:
        welford.update(x)
    welford_var = welford.variance()

    print(f"  Naive variance:   {naive_var:.2f} (wrong: lost precision/canceled)")
    print(f"  Batch variance:   {batch_var:.10f}")
    print(f"  Welford variance: {welford_var:.10f}")

    # The critical assertion: Welford and batch agree; naive diverges
    assert abs(welford_var - batch_var) < 1e-6, \
        f"Welford {welford_var} != batch {batch_var}"
    assert abs(naive_var - batch_var) > 1.0, \
        f"Naive should fail but got {naive_var} vs batch {batch_var}"
    print(f"  Welford agrees with batch ✓")
    print(f"  Naive diverges from batch ✓")

    print("\nwelford_online_stats.py PASS")
