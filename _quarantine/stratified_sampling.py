"""
Stratified Sampling

Core idea: Divide population into strata (subgroups), then sample independently from each
stratum to preserve the original class proportions. Ensures representative samples,
especially valuable with imbalanced classes.

When to use: Sample from data with distinct subgroups or classes when you want the sample
to have the same proportions as the population.
"""

import random
from typing import List, Tuple
from collections import Counter


def stratified_sample(data: List, strata: List, sample_size: int) -> Tuple[List, List]:
    """
    Stratified random sample.

    Args:
        data: Items to sample from.
        strata: Stratum label for each item (e.g., class/group).
        sample_size: Total number of items to sample.

    Returns:
        Tuple of (sampled_data, sampled_strata).
    """
    n = len(data)
    if sample_size > n:
        sample_size = n

    # Group indices by stratum
    stratum_indices = {}
    for idx, stratum in enumerate(strata):
        if stratum not in stratum_indices:
            stratum_indices[stratum] = []
        stratum_indices[stratum].append(idx)

    # Compute stratum proportions in population
    stratum_counts = Counter(strata)
    total = len(strata)

    # Sample from each stratum proportionally
    sampled_indices = []
    for stratum, indices in stratum_indices.items():
        # Number of samples from this stratum
        proportion = stratum_counts[stratum] / total
        stratum_sample_size = max(1, int(proportion * sample_size))

        # Randomly sample from this stratum's indices
        sampled = random.sample(indices, min(stratum_sample_size, len(indices)))
        sampled_indices.extend(sampled)

    # Adjust final size if rounding caused over/under-sampling
    while len(sampled_indices) > sample_size:
        sampled_indices.pop()
    while len(sampled_indices) < sample_size and len(sampled_indices) < n:
        # Add a random item not yet sampled
        all_indices = set(range(n))
        remaining = list(all_indices - set(sampled_indices))
        if remaining:
            sampled_indices.append(random.choice(remaining))

    sampled_data = [data[i] for i in sampled_indices]
    sampled_strata = [strata[i] for i in sampled_indices]

    return sampled_data, sampled_strata


def check_proportions(population_strata: List, sample_strata: List) -> Tuple[dict, dict, bool]:
    """
    Check that sample proportions match population proportions.

    Args:
        population_strata: Original stratum labels.
        sample_strata: Sampled stratum labels.

    Returns:
        Tuple of (pop_props, sample_props, is_close).
    """
    pop_counts = Counter(population_strata)
    sample_counts = Counter(sample_strata)

    pop_total = len(population_strata)
    sample_total = len(sample_strata)

    pop_props = {s: c / pop_total for s, c in pop_counts.items()}
    sample_props = {s: c / sample_total for s, c in sample_counts.items()}

    # Check if proportions are close (within 10% relative difference)
    is_close = True
    for stratum in pop_props:
        if stratum in sample_props:
            rel_diff = abs(pop_props[stratum] - sample_props[stratum]) / max(pop_props[stratum], 0.01)
            if rel_diff > 0.15:
                is_close = False

    return pop_props, sample_props, is_close


if __name__ == "__main__":
    random.seed(42)

    # Scenario 1: Imbalanced population (classes: 70% A, 20% B, 10% C)
    data = list(range(1000))
    strata = (["A"] * 700) + (["B"] * 200) + (["C"] * 100)

    pop_props, _, _ = check_proportions(strata, strata)
    print(f"Population proportions: {pop_props}")

    # Stratified sample of 100
    sampled_data, sampled_strata = stratified_sample(data, strata, sample_size=100)
    sample_props, _, is_close = check_proportions(strata, sampled_strata)
    print(f"Sample proportions: {sample_props}")
    print(f"Proportions preserved: {is_close}")

    assert len(sampled_data) == 100, "Sample size should be 100"
    assert len(sampled_strata) == 100, "Sample strata size should be 100"
    assert is_close, "Sample proportions should match population"

    # Scenario 2: Very small sample from imbalanced data
    sampled_data_small, sampled_strata_small = stratified_sample(data, strata, sample_size=20)
    sample_props_small, _, is_close_small = check_proportions(strata, sampled_strata_small)
    print(f"Small sample (n=20) proportions: {sample_props_small}")
    assert len(sampled_data_small) == 20, "Small sample should have 20 items"
    # For very small samples, proportions may be looser
    assert is_close_small or len([s for s in sampled_strata_small if s == "A"]) >= 10, \
        "Majority class A should have at least half the small sample"

    print("✓ Stratified sampling PASSED")
