"""
Shannon entropy estimation from samples: naive plug-in vs Miller-Madow bias correction.

Core idea: Naive plug-in uses empirical frequencies as probabilities; Miller-Madow correction
adds a bias term (-1/(2*N) * number_of_symbols) to reduce bias on small samples. The correction
pulls the estimate closer to the true entropy when N is small.

Use when: estimating entropy from limited data, correcting bias in frequency-based statistics,
comparing sample-based estimates to ground truth.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
import random
from typing import List
from collections import Counter


def true_entropy(probabilities: List[float]) -> float:
    """True Shannon entropy of a known distribution."""
    result = 0.0
    for p in probabilities:
        if p > 1e-10:
            result -= p * math.log2(p)
    return result


def naive_plugin_entropy(samples: List[int]) -> float:
    """Plug-in entropy: use empirical frequencies as probabilities."""
    n = len(samples)
    counts = Counter(samples)
    result = 0.0
    for count in counts.values():
        p = count / n
        if p > 1e-10:
            result -= p * math.log2(p)
    return result


def miller_madow_entropy(samples: List[int]) -> float:
    """Miller-Madow bias-corrected entropy estimate."""
    n = len(samples)
    counts = Counter(samples)
    k = len(counts)  # Number of observed symbols

    # Naive entropy
    naive = naive_plugin_entropy(samples)

    # Miller-Madow bias correction
    correction = (k - 1) / (2 * n * math.log(2))

    return naive + correction


if __name__ == "__main__":
    random.seed(42)

    # Ground truth: uniform distribution over 4 symbols
    # H(uniform 4) = log2(4) = 2.0 bits
    true_probs = [0.25, 0.25, 0.25, 0.25]
    true_h = true_entropy(true_probs)
    assert abs(true_h - 2.0) < 1e-9, f"True entropy of uniform(4) should be 2.0, got {true_h}"

    # Test on SMALL samples (N=20): Miller-Madow should be closer to ground truth
    samples_small = random.choices([0, 1, 2, 3], weights=true_probs, k=20)

    naive_small = naive_plugin_entropy(samples_small)
    mm_small = miller_madow_entropy(samples_small)

    # On small samples, bias is significant; MM should reduce it
    naive_error = abs(naive_small - true_h)
    mm_error = abs(mm_small - true_h)

    assert mm_error < naive_error, (
        f"Miller-Madow should reduce error on small samples. "
        f"Naive error: {naive_error:.4f}, MM error: {mm_error:.4f}"
    )

    # Test on LARGE samples (N=10000): both should be close, MM adds tiny correction
    samples_large = random.choices([0, 1, 2, 3], weights=true_probs, k=10000)

    naive_large = naive_plugin_entropy(samples_large)
    mm_large = miller_madow_entropy(samples_large)

    # On large samples, both are close to true, MM correction is small
    assert abs(naive_large - true_h) < 0.1, f"Naive should converge to true entropy"
    assert abs(mm_large - true_h) < 0.1, f"MM should converge to true entropy"

    # MM correction is always positive (adds small amount)
    assert mm_large > naive_large, "Miller-Madow correction should increase estimate"

    print("Entropy estimators (naive plug-in vs Miller-Madow): all assertions PASS")
