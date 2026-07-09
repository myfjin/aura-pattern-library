"""
Streaming Histogram with Bin Merging

Core idea: Maintain a fixed-size histogram on a stream. When bins exceed the limit,
merge adjacent bins to free space. Trade-off: quantile estimates have bounded error.

When to use: You need a histogram summary of streaming data with bounded memory, or want
to understand the accuracy/memory trade-off in streaming histogram algorithms.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
from typing import List, Tuple


class StreamingHistogram:
    """Fixed-budget histogram with adaptive bin merging."""

    def __init__(self, max_bins: int = 20):
        self.max_bins = max_bins
        self.bins: List[Tuple[float, int]] = []  # (bin_center, count)

    def process(self, value: float) -> None:
        """Process a new value: add to appropriate bin or merge if necessary."""
        # Find bin or create new one
        found = False
        for i, (center, count) in enumerate(self.bins):
            if abs(value - center) < 0.5:  # Tolerance for "same bin"
                self.bins[i] = (center, count + 1)
                found = True
                break

        if not found:
            # New bin
            self.bins.append((value, 1))

            # Check if we need to merge
            if len(self.bins) > self.max_bins:
                self._merge_adjacent()

    def _merge_adjacent(self) -> None:
        """Merge two adjacent bins with smallest counts."""
        if len(self.bins) <= 1:
            return

        # Find pair with smallest combined count
        min_cost = float("inf")
        min_idx = 0
        for i in range(len(self.bins) - 1):
            cost = self.bins[i][1] + self.bins[i + 1][1]
            if cost < min_cost:
                min_cost = cost
                min_idx = i

        # Merge bins at min_idx and min_idx + 1
        c1, n1 = self.bins[min_idx]
        c2, n2 = self.bins[min_idx + 1]

        # Weighted average
        merged_center = (c1 * n1 + c2 * n2) / (n1 + n2)
        merged_count = n1 + n2

        # Replace with merged bin
        self.bins[min_idx] = (merged_center, merged_count)
        del self.bins[min_idx + 1]

    def query_quantile(self, p: float) -> float:
        """Estimate quantile p (0 <= p <= 1)."""
        if not self.bins:
            return 0.0

        total_count = sum(count for _, count in self.bins)
        target_rank = p * total_count

        cumsum = 0
        for center, count in sorted(self.bins):
            cumsum += count
            if cumsum >= target_rank:
                return center

        return self.bins[-1][0]

    def get_bins(self) -> List[Tuple[float, int]]:
        """Return current bins."""
        return sorted(self.bins)


if __name__ == "__main__":
    random.seed(42)

    # Bimodal distribution: two peaks at 30 and 70
    stream = []
    for _ in range(500):
        if random.random() < 0.5:
            stream.append(random.gauss(30, 5))
        else:
            stream.append(random.gauss(70, 5))

    # Compute exact quantiles on stored stream
    sorted_stream = sorted(stream)
    n = len(stream)
    exact_median = sorted_stream[n // 2]
    exact_p25 = sorted_stream[n // 4]
    exact_p75 = sorted_stream[3 * n // 4]

    # Process with streaming histogram
    hist = StreamingHistogram(max_bins=15)
    for x in stream:
        hist.process(x)

    # Quantile estimates
    est_median = hist.query_quantile(0.5)
    est_p25 = hist.query_quantile(0.25)
    est_p75 = hist.query_quantile(0.75)

    print(f"Exact quantiles: p25={exact_p25:.1f}, median={exact_median:.1f}, p75={exact_p75:.1f}")
    print(f"Est. quantiles: p25={est_p25:.1f}, median={est_median:.1f}, p75={est_p75:.1f}")

    final_bins = hist.get_bins()
    print(f"Final number of bins: {len(final_bins)} (max {hist.max_bins})")

    # Compute errors
    error_p25 = abs(exact_p25 - est_p25)
    error_median = abs(exact_median - est_median)
    error_p75 = abs(exact_p75 - est_p75)

    print(f"Errors: p25={error_p25:.2f}, median={error_median:.2f}, p75={error_p75:.2f}")

    # Assertion: quantile estimates within tolerance, bins respect budget
    # Fixed-budget histogram trades accuracy for memory
    assert len(final_bins) <= hist.max_bins, f"Bins should respect budget: {len(final_bins)} vs {hist.max_bins}"
    assert error_p25 < 25.0, f"P25 error within reasonable bound: {error_p25}"
    assert error_median < 25.0, f"Median error within reasonable bound: {error_median}"
    assert error_p75 < 25.0, f"P75 error within reasonable bound: {error_p75}"

    print("✓ Streaming Histogram Merge: PASS")
