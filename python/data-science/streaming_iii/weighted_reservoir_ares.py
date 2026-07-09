"""
Weighted reservoir sampling -- Efraimidis-Spirakis A-Res.
Core idea: give each item a key u**(1/weight) with u ~ Uniform(0,1); keep the k items
with the largest keys in a min-heap. The resulting sample is a weighted sample without
replacement: P(item in sample) grows with its weight.
When: sample k items proportional to weight in one pass over a weighted stream.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import random
import heapq
from typing import List, Tuple


def weighted_reservoir_ares(stream: List[Tuple], k: int) -> List:
    """
    Weighted reservoir sample of k items (values) via A-Res keys u**(1/w).
    Args:
        stream: list of (value, weight) with weight > 0
        k: sample size
    Returns:
        List of sampled values.
    """
    assert k > 0
    heap: List[Tuple[float, int, object]] = []  # (key, tiebreak, value) min-heap
    for i, (value, weight) in enumerate(stream):
        if weight <= 0:
            continue
        key = random.random() ** (1.0 / weight)
        if len(heap) < k:
            heapq.heappush(heap, (key, i, value))
        elif key > heap[0][0]:
            heapq.heapreplace(heap, (key, i, value))
    return [v for _, _, v in heap]


if __name__ == "__main__":
    random.seed(42)  # deterministic: seed BEFORE any data generation
    # The DEFINING property: for k=1, A-Res picks item i with probability w_i / sum(w).
    # Verify empirically over many trials against the exact weighted distribution.
    weights = [1.0, 2.0, 3.0, 4.0, 5.0]           # total 15
    items = list(range(len(weights)))
    total_w = sum(weights)
    exact_p = [w / total_w for w in weights]

    trials = 40000
    counts = [0] * len(weights)
    for _ in range(trials):
        picked = weighted_reservoir_ares(list(zip(items, weights)), k=1)[0]
        counts[picked] += 1
    emp_p = [c / trials for c in counts]
    max_dev = max(abs(e - t) for e, t in zip(emp_p, exact_p))
    print(f"empirical p={[f'{p:.3f}' for p in emp_p]}  exact={[f'{p:.3f}' for p in exact_p]}")
    print(f"max deviation = {max_dev:.4f}")

    # RECOVERY ASSERT 1: empirical inclusion frequencies match w_i/sum(w) (the weighted
    # law). Bound 0.015 ~ 3*sqrt(p(1-p)/trials) for the heaviest cell. This FAILS for
    # uniform (unweighted) sampling -- it pins the *weighted* property, not "a sample
    # was returned".
    assert max_dev < 0.015, f"A-Res does not match the weighted distribution: {max_dev:.4f}"

    # RECOVERY ASSERT 2: monotone -- heavier items are picked strictly more often.
    assert counts == sorted(counts), f"selection frequency not monotone in weight: {counts}"
    print("Weighted reservoir (A-Res) PASS")
