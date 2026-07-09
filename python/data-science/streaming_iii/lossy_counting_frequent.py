"""
Lossy Counting for frequent items (Manku & Motwani, 2002).
Core idea: divide the stream into buckets of width w = ceil(1/eps). Store each item as
(freq, delta) where delta is the max possible undercount at insertion (current_bucket-1).
At every bucket boundary, delete any item whose freq+delta <= current_bucket. Output items
with freq >= (s-eps)*N. This guarantees ZERO false negatives for true frequency >= s*N,
and no reported item has true frequency < (s-eps)*N.
When: find frequent items in one pass with a provable error/space tradeoff (eps < s).
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import random
from typing import Dict, Set, Tuple


def lossy_counting_frequent(stream: list, support: float, eps: float = None) -> Tuple[Set, Dict]:
    """
    Lossy Counting. Returns (estimated_frequent_set, freq_estimates).
    Args:
        stream: input sequence
        support: frequency threshold s in (0,1)
        eps: error parameter (must be < support); defaults to support/10
    """
    assert 0 < support < 1
    if eps is None:
        eps = support / 10.0
    assert 0 < eps < support

    N = 0
    w = int(1.0 / eps + 0.999999)          # bucket width = ceil(1/eps)
    entries: Dict = {}                      # item -> [freq, delta]

    for item in stream:
        N += 1
        b_current = (N + w - 1) // w        # current bucket id, ceil(N/w)
        if item in entries:
            entries[item][0] += 1
        else:
            entries[item] = [1, b_current - 1]
        # prune at bucket boundary
        if N % w == 0:
            for it in [k for k, (f, d) in entries.items() if f + d <= b_current]:
                del entries[it]

    # Output items with freq >= (s - eps) * N; report their (undercounted) freq.
    cutoff = (support - eps) * N
    estimated = {it for it, (f, d) in entries.items() if f >= cutoff}
    freq_estimates = {it: f for it, (f, d) in entries.items()}
    return estimated, freq_estimates


if __name__ == "__main__":
    random.seed(42)  # deterministic: seed BEFORE any data generation
    # Plant a skewed stream: A,B are heavy (~30%,~20%), C,D,E rare noise.
    heavy = ['A'] * 3000 + ['B'] * 2000
    noise = [random.choice(['C', 'D', 'E', 'F', 'G', 'H']) for _ in range(5000)]
    stream = heavy + noise
    random.shuffle(stream)
    N = len(stream)

    from collections import Counter
    truth = Counter(stream)
    support = 0.10
    true_frequent = {it for it, c in truth.items() if c >= support * N}  # {A, B}

    est, freqs = lossy_counting_frequent(stream, support=support, eps=support / 10)

    # RECOVERY ASSERT 1: the defining guarantee -- ZERO false negatives.
    false_neg = true_frequent - est
    assert not false_neg, f"Lossy Counting dropped a frequent item: {false_neg}"

    # RECOVERY ASSERT 2: the count guarantee -- reported freq undercounts true by at
    # most eps*N (never over, at most eps*N under).
    eps = support / 10
    for it in est:
        true_c = truth[it]
        assert true_c - eps * N <= freqs[it] <= true_c, \
            f"count guarantee violated for {it}: est {freqs[it]}, true {true_c}"

    # RECOVERY ASSERT 3: no item with true freq < (s-eps)*N is reported (bounded FPs).
    for it in est:
        assert truth[it] >= (support - eps) * N, f"spurious frequent item {it}"

    print(f"Lossy Counting: frequent={sorted(est)}, true={sorted(true_frequent)}")
    print("Lossy Counting PASS")
