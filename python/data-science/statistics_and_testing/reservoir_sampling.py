"""
Reservoir Sampling (Algorithm R)

Core idea: Sample k items uniformly from a stream of unknown length without storing the
entire stream. Maintain a "reservoir" of k items; for each new item i (i >= k), include
it with probability k/i, replacing a random reservoir item if accepted.

When to use: Sample from data streams, huge files, or situations where you can't load all
data into memory at once.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
from typing import List, TypeVar

T = TypeVar("T")


def reservoir_sample(stream, k: int) -> List:
    """
    Reservoir sampling using Algorithm R.

    Args:
        stream: An iterable of items (e.g., file lines, generator).
        k: Number of items to sample.

    Returns:
        List of up to k sampled items, uniformly distributed from the stream.
    """
    reservoir = []

    for i, item in enumerate(stream):
        if i < k:
            # Fill reservoir for first k items
            reservoir.append(item)
        else:
            # For item i (i >= k), include with probability k/(i+1)
            j = random.randint(0, i)
            if j < k:
                # Replace random item in reservoir
                reservoir[j] = item

    return reservoir


def verify_uniformity(samples_per_run: List[List], item_count: int) -> bool:
    """
    Verify that reservoir samples are roughly uniformly distributed.
    For each item, count how often it appears across all runs.
    With k samples per run and n items, expected frequency is roughly (k * runs) / n.

    Args:
        samples_per_run: List of sample lists from multiple runs.
        item_count: Total number of distinct items in the stream.

    Returns:
        True if distribution looks approximately uniform.
    """
    counts = {}
    total_samples = 0

    for samples in samples_per_run:
        total_samples += len(samples)
        for item in samples:
            counts[item] = counts.get(item, 0) + 1

    # Expected count per item
    expected = total_samples / item_count

    # Check that most items have counts close to expected (within a factor of 2)
    close_counts = sum(1 for count in counts.values() if 0.5 * expected <= count <= 2 * expected)

    return close_counts >= len(counts) * 0.7  # At least 70% of items close to expected


if __name__ == "__main__":
    random.seed(42)

    # Scenario 1: Simple case - sample 5 from a stream of 20
    def simple_stream():
        for i in range(20):
            yield i

    sample_1 = reservoir_sample(simple_stream(), k=5)
    print(f"Sample 5 from [0..19]: {sorted(sample_1)}")
    assert len(sample_1) == 5, "Should have 5 samples"
    assert all(0 <= x < 20 for x in sample_1), "All samples should be in range"
    assert len(set(sample_1)) == 5, "All samples should be unique"

    # Scenario 2: Multiple runs to verify uniformity
    k = 10
    n = 100
    num_runs = 50

    samples_per_run = []
    for _ in range(num_runs):
        def stream():
            for i in range(n):
                yield i

        sample = reservoir_sample(stream(), k=k)
        samples_per_run.append(sample)

    # Check distribution
    is_uniform = verify_uniformity(samples_per_run, n)
    print(f"{num_runs} runs: sample 10 from 100, uniformity check: {is_uniform}")
    assert is_uniform, "Samples should be approximately uniformly distributed"

    # Scenario 3: Stream smaller than k
    def tiny_stream():
        for i in range(3):
            yield i

    sample_tiny = reservoir_sample(tiny_stream(), k=10)
    print(f"Sample 10 from [0..2]: {sorted(sample_tiny)}")
    assert len(sample_tiny) == 3, "Cannot sample more than available"
    assert sample_tiny == [0, 1, 2], "Should get all items when stream < k"

    print("✓ Reservoir sampling PASSED")
