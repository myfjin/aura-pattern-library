import math
"""
Exponential histogram / DGIM count of 1s in a sliding window (Datar-Gionis-Indyk-Motwani).
Core idea: to count the 1-bits among the last N arrivals in O((1/eps) log N) space, keep
buckets each holding a power-of-2 count and the timestamp of its most recent 1. Allow at
most k/2+1 buckets of each size (k = ceil(1/eps)); when exceeded, merge the two oldest of
that size into one double-size bucket. Expire buckets that fall out of the window. Estimate
= (sum of bucket sizes) - (half the oldest in-window bucket). Relative error <= 1/k = eps.
When: count events in a sliding window under strict memory with a provable error bound.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import random
from typing import List




class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_dgim_count(window):
    v = []
    if isinstance(window, (int, float)) and window <= 0:
        v.append(f"AURA-E009: window must be > 0, got {window}")
    if v:
        raise AuraInputError(v)

def dgim_count(stream: List[int], window: int, eps: float = 0.1) -> int:
    """
    Estimate the number of 1s among the last `window` bits via DGIM.
    Args:
        stream: sequence of 0/1
        window: sliding-window size N
        eps: target relative error (buckets-per-size = ceil(1/eps))
    """
    _aura_validate_dgim_count(window)
    assert 0 < eps < 1
    k = int(1.0 / eps + 0.999999)
    cap = k // 2 + 1
    # each bucket: [size (power of 2), timestamp of newest 1]
    buckets: List[List[int]] = []
    for t, bit in enumerate(stream):
        # expire buckets whose newest 1 is outside the window
        buckets = [b for b in buckets if b[1] > t - window]
        if bit == 1:
            buckets.insert(0, [1, t])          # newest bucket at front
            # merge from smallest size upward when a size overflows its cap
            size = 1
            while True:
                idxs = [i for i, b in enumerate(buckets) if b[0] == size]
                if len(idxs) <= cap:
                    break
                # merge the two OLDEST of this size (largest timestamps are newest,
                # so oldest = smallest timestamps = last in list order)
                i2, i1 = idxs[-1], idxs[-2]     # i2 oldest, i1 next
                merged_ts = max(buckets[i1][1], buckets[i2][1])
                buckets[i1] = [size * 2, merged_ts]
                del buckets[i2]
                size *= 2
    if not buckets:
        return 0
    est = sum(b[0] for b in buckets) - buckets[-1][0] // 2
    return est


if __name__ == "__main__":
    random.seed(42)  # deterministic: seed BEFORE any data generation
    N = 1000
    eps = 0.1
    stream = [1 if random.random() < 0.3 else 0 for _ in range(5000)]
    est = dgim_count(stream, window=N, eps=eps)
    true = sum(stream[-N:])                     # exact count of 1s in the last N
    rel = abs(est - true) / true
    print(f"DGIM windowed count: est={est}, true={true}, rel_err={rel:.4f} (eps={eps})")

    # RECOVERY ASSERT: DGIM's guarantee -- relative error <= eps. Bound eps + a hair for
    # integer rounding. This is the ALGORITHM'S bound, not a loose catch-all (old code
    # allowed 0.2 to mask a truncated decayed-sum that was never DGIM at all).
    assert rel <= eps + 1e-9, f"DGIM exceeded its eps guarantee: {rel:.4f} > {eps}"

    # And the space win: O((1/eps) log N) buckets, far below N.
    # (recompute bucket count for the assertion)
    def _bucket_count(s, w, e):
        k = int(1 / e + 0.999999); cap = k // 2 + 1; bks = []
        for t, bit in enumerate(s):
            bks = [b for b in bks if b[1] > t - w]
            if bit == 1:
                bks.insert(0, [1, t]); size = 1
                while True:
                    idxs = [i for i, b in enumerate(bks) if b[0] == size]
                    if len(idxs) <= cap: break
                    i2, i1 = idxs[-1], idxs[-2]
                    bks[i1] = [size * 2, max(bks[i1][1], bks[i2][1])]; del bks[i2]; size *= 2
        return len(bks)
    assert _bucket_count(stream, N, eps) < N // 10, "DGIM failed to compress"
    print("Exponential histogram (DGIM) PASS")
