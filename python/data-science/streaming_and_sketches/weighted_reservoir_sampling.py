"""
Weighted Reservoir Sampling (A-Res Algorithm)

Core idea: Sample k items from a weighted stream such that inclusion probability is
proportional to item weight. A-Res: use u^(1/w) as sort key.

When to use: You have a stream of weighted items and need a representative sample
where rare (high-weight) items are more likely to appear.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import math
from typing import List, Tuple


class WeightedReservoirSampler:
    """A-Res: weighted reservoir sampling with probability ∝ weight."""

    def __init__(self, k: int = 5):
        self.k = k
        self.reservoir = []  # List of (key, item, weight) tuples

    def process(self, item: str, weight: float) -> None:
        """Process weighted item from stream."""
        if weight <= 0:
            return

        # Generate key: u^(1/w) where u ~ Uniform(0, 1)
        u = random.random()
        key = u ** (1.0 / weight)

        if len(self.reservoir) < self.k:
            self.reservoir.append((key, item, weight))
        else:
            # Keep only top-k items by key
            if key > self.reservoir[0][0]:  # Assume heap-like structure
                self.reservoir[0] = (key, item, weight)

        # Maintain sorted order
        self.reservoir.sort()

    def get_sample(self) -> List[Tuple[str, float]]:
        """Return sampled items with weights."""
        return [(item, weight) for _, item, weight in self.reservoir]

    def get_inclusion_freq(self, item: str, total_samples: int) -> float:
        """After multiple runs, compute empirical inclusion frequency."""
        return sum(1 for _, i, _ in self.reservoir if i == item) / total_samples


if __name__ == "__main__":
    random.seed(42)

    # Items with weights: high weight items should be sampled more
    weighted_items = [
        ("rare1", 10.0),
        ("rare2", 8.0),
        ("common1", 1.0),
        ("common2", 0.5),
        ("common3", 0.5),
    ]

    # Simulate multiple runs to check inclusion frequency
    num_runs = 100
    sample_size = 3
    item_counts = {item: 0 for item, _ in weighted_items}

    for run in range(num_runs):
        sampler = WeightedReservoirSampler(k=sample_size)

        # Process each item's stream (repeated based on weight)
        # Simulate stream by processing each item count times
        items_in_stream = []
        for item, weight in weighted_items:
            # Represent weighted item by adding it proportionally
            items_in_stream.extend([(item, weight) for _ in range(max(1, int(weight)))])

        random.shuffle(items_in_stream)

        for item, weight in items_in_stream:
            sampler.process(item, weight)

        sample = sampler.get_sample()
        for item, _ in sample:
            item_counts[item] += 1

    print(f"Inclusion counts over {num_runs} runs (sample size {sample_size}):")
    for item, weight in weighted_items:
        freq = item_counts[item] / num_runs
        print(f"  {item} (weight {weight}): {freq:.2%}")

    # Assertion: high-weight items should have higher inclusion frequency
    rare_freq = (item_counts["rare1"] + item_counts["rare2"]) / num_runs / 2
    common_freq = (item_counts["common1"] + item_counts["common2"] + item_counts["common3"]) / num_runs / 3

    assert rare_freq > common_freq, f"Rare (high-weight) should be sampled more: {rare_freq} vs {common_freq}"
    assert rare_freq > 0.3, f"Rare items should have substantial inclusion: {rare_freq}"

    print("✓ Weighted Reservoir Sampling: PASS")
