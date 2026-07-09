"""
KL divergence, cross-entropy, and Jensen-Shannon divergence between discrete distributions.

Core idea: KL divergence D(p||q) = sum(p[i] * log(p[i]/q[i])) measures how q differs from p.
Cross-entropy H(p,q) = -sum(p[i] * log(q[i])) is the expected bits needed when using distribution q
to encode samples from p. Jensen-Shannon distance is symmetric: JS(p||q) = 0.5*D(p||q) + 0.5*D(q||p).

Use when: comparing probability distributions, measuring distribution divergence, evaluating
generative models (cross-entropy loss), constructing symmetric distance metrics for clustering.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
from typing import List


def kl_divergence(p: List[float], q: List[float]) -> float:
    """KL divergence D(p||q), assuming both are valid probability distributions (sum to ~1)."""
    assert len(p) == len(q), "Distributions must have the same support."
    result = 0.0
    for pi, qi in zip(p, q):
        if pi > 1e-10:  # Avoid log(0)
            result += pi * math.log(pi / qi)
    return result


def cross_entropy(p: List[float], q: List[float]) -> float:
    """Cross-entropy H(p,q) = -sum(p[i] * log(q[i]))."""
    assert len(p) == len(q), "Distributions must have the same support."
    result = 0.0
    for pi, qi in zip(p, q):
        if pi > 1e-10:
            result -= pi * math.log(qi)
    return result


def shannon_entropy(p: List[float]) -> float:
    """Shannon entropy H(p) = -sum(p[i] * log(p[i]))."""
    result = 0.0
    for pi in p:
        if pi > 1e-10:
            result -= pi * math.log(pi)
    return result


def jensen_shannon_distance(p: List[float], q: List[float]) -> float:
    """Jensen-Shannon distance: sqrt(0.5 * D(p||m) + 0.5 * D(q||m)) where m = (p+q)/2."""
    assert len(p) == len(q), "Distributions must have the same support."
    m = [(pi + qi) / 2.0 for pi, qi in zip(p, q)]
    js_div = 0.5 * kl_divergence(p, m) + 0.5 * kl_divergence(q, m)
    return math.sqrt(js_div)


if __name__ == "__main__":
    import random
    random.seed(42)

    # Test 1: KL(p||p) should be 0
    p = [0.5, 0.3, 0.2]
    kl_self = kl_divergence(p, p)
    assert abs(kl_self) < 1e-9, f"KL(p||p) should be 0, got {kl_self}"

    # Test 2: Cross-entropy relationship: H(p,q) = H(p) + D(p||q)
    q = [0.4, 0.4, 0.2]
    hp = shannon_entropy(p)
    hpq = cross_entropy(p, q)
    dpq = kl_divergence(p, q)
    assert abs(hpq - (hp + dpq)) < 1e-9, f"Cross-entropy identity failed: {hpq} vs {hp + dpq}"

    # Test 3: Jensen-Shannon is symmetric
    js_pq = jensen_shannon_distance(p, q)
    js_qp = jensen_shannon_distance(q, p)
    assert abs(js_pq - js_qp) < 1e-9, f"JS should be symmetric: {js_pq} vs {js_qp}"

    # Test 4: Jensen-Shannon is bounded [0, 1]
    r = [0.2, 0.5, 0.3]
    js_pr = jensen_shannon_distance(p, r)
    assert 0 <= js_pr <= 1, f"JS distance should be in [0, 1], got {js_pr}"

    # Test 5: Known example verification (hand-computed)
    # p = [0.5, 0.5], q = [0.7, 0.3]
    # D(p||q) = 0.5*log(0.5/0.7) + 0.5*log(0.5/0.3)
    #         = 0.5*log(5/7) + 0.5*log(5/3)
    p_simple = [0.5, 0.5]
    q_simple = [0.7, 0.3]
    expected_kl = 0.5 * math.log(0.5 / 0.7) + 0.5 * math.log(0.5 / 0.3)
    computed_kl = kl_divergence(p_simple, q_simple)
    assert abs(computed_kl - expected_kl) < 1e-9, f"Hand-computed KL mismatch: {computed_kl} vs {expected_kl}"

    print("KL divergence / cross-entropy / Jensen-Shannon: all assertions PASS")
