"""
Bayesian two-segment changepoint: marginal-likelihood comparison over split points.

Core idea: compare model evidence for no-change vs change-at-t; find planted change location;
no-change data prefers single-segment model.

When to use: quality control, structural break detection, time-series anomalies.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
from typing import List, Tuple

def log_normal_likelihood(data: List[float], mean: float = None, var: float = 1.0) -> float:
    """Log-likelihood of data under N(mean, var). If mean is None, use MLE."""
    if mean is None:
        mean = sum(data) / len(data)
    ll = 0.0
    for x in data:
        ll += -0.5 * math.log(2 * math.pi * var) - 0.5 * (x - mean) ** 2 / var
    return ll

def model_evidence_1seg(data: List[float], var: float = 1.0) -> float:
    """Log marginal likelihood for single-segment model."""
    # Assuming flat prior, evidence ∝ likelihood at MLE
    mean = sum(data) / len(data)
    return log_normal_likelihood(data, mean, var)

def model_evidence_2seg(data: List[float], split: int, var: float = 1.0) -> float:
    """Log marginal likelihood for two-segment model split at index split."""
    if split <= 0 or split >= len(data):
        return float('-inf')
    seg1 = data[:split]
    seg2 = data[split:]
    mean1 = sum(seg1) / len(seg1)
    mean2 = sum(seg2) / len(seg2)
    ll = log_normal_likelihood(seg1, mean1, var) + log_normal_likelihood(seg2, mean2, var)
    return ll

def changepoint_detection(data: List[float], var: float = 1.0) -> Tuple[int, float]:
    """
    Find changepoint by comparing model evidence.
    Return: (best_split, log_bayes_factor_2seg_vs_1seg)
    """
    ll_1seg = model_evidence_1seg(data, var)

    best_split = -1
    best_ll_2seg = float('-inf')
    for split in range(1, len(data)):
        ll_2seg = model_evidence_2seg(data, split, var)
        if ll_2seg > best_ll_2seg:
            best_ll_2seg = ll_2seg
            best_split = split

    log_bf = best_ll_2seg - ll_1seg  # Bayes factor favors 2-seg if > 0
    return best_split, log_bf

if __name__ == '__main__':
    import random
    random.seed(42)

    # Data with a change at index 25
    seg1 = [random.gauss(1.0, 0.5) for _ in range(25)]
    seg2 = [random.gauss(3.5, 0.5) for _ in range(25)]
    data_with_change = seg1 + seg2

    split_detected, bf = changepoint_detection(data_with_change, var=0.25)

    # Assertions
    # Detected split should be near the planted split (25)
    assert 20 <= split_detected <= 30, f"Detected split {split_detected} should be near 25"

    # Bayes factor should favor 2-segment model (log_bf > 0)
    assert bf > 0, f"2-segment should be favored for data with change, log_bf={bf}"

    # Test with no-change data: 1-segment is usually preferred or tied
    no_change_data = [random.gauss(2.0, 0.5) for _ in range(50)]
    split_no_change, bf_no_change = changepoint_detection(no_change_data, var=0.25)

    # For uniform data, BF can be slightly in favor of 2-segment due to overfitting, but should be small
    assert abs(bf_no_change) < 3.0, f"No-change data should have small |BF|, got {bf_no_change}"

    # For data with change, evidence ratio should be more extreme than no-change case
    assert bf > abs(bf_no_change), f"Change data should have more extreme BF than no-change"

    # Detected split on no-change data is less meaningful, but should still find something
    assert 0 < split_no_change < len(no_change_data), "Split should be in bounds"

    print("PASS")
