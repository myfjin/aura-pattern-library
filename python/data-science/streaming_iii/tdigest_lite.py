"""
t-digest (merging variant) -- accurate tail quantiles in small space.
Core idea: merge sorted points into centroids under a q-dependent SIZE BOUND
limit(q) = 4*N*delta*q*(1-q). Near the tails (q->0 or 1) the bound shrinks to ~0, so tail
centroids stay tiny (near-exact), while mid-distribution centroids may grow large. This
tail-scaling is the DEFINING move of a t-digest -- it is why p99/p01 are far more accurate
than a fixed-width sketch would give.
When: estimate extreme quantiles (p99, p01, ...) from a large stream in bounded memory.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import math
import random
from typing import List, Tuple


def _build(sorted_vals: List[float], compression: float) -> List[Tuple[float, int]]:
    n = len(sorted_vals)
    delta = 1.0 / compression
    centroids: List[Tuple[float, int]] = []
    c_mean, c_count = sorted_vals[0], 1
    cum = 0
    for x in sorted_vals[1:]:
        q = (cum + (c_count + 1) / 2.0) / n
        limit = 4.0 * n * delta * q * (1.0 - q)        # tail-scaled size bound
        if c_count + 1 <= max(1.0, limit):
            c_mean = (c_mean * c_count + x) / (c_count + 1)
            c_count += 1
        else:
            centroids.append((c_mean, c_count))
            cum += c_count
            c_mean, c_count = x, 1
    centroids.append((c_mean, c_count))
    return centroids


def tdigest_quantile(centroids: List[Tuple[float, int]], q: float) -> float:
    total = sum(c for _, c in centroids)
    target = q * total
    cum = 0.0
    prev_center, prev_q = centroids[0][0], 0.0
    for mean, count in centroids:
        center = cum + count / 2.0                     # this centroid sits at this rank
        if center >= target:
            if center == prev_q:
                return mean
            frac = (target - prev_q) / (center - prev_q)
            return prev_center + frac * (mean - prev_center)
        prev_center, prev_q = mean, center
        cum += count
    return centroids[-1][0]




class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_tdigest_lite(compression):
    v = []
    if isinstance(compression, (int, float)) and not math.isfinite(compression):
        v.append(f"AURA-E008: compression must be finite, got {compression}")
    if v:
        raise AuraInputError(v)

def tdigest_lite(stream: List[float], compression: float = 200.0) -> Tuple[float, float]:
    """Return (p99, p01) estimates from a merging t-digest."""
    _aura_validate_tdigest_lite(compression)
    centroids = _build(sorted(stream), compression)
    return tdigest_quantile(centroids, 0.99), tdigest_quantile(centroids, 0.01)


if __name__ == "__main__":
    random.seed(42)  # deterministic: seed BEFORE any data generation
    stream = [random.gauss(50.0, 10.0) for _ in range(20000)]
    srt = sorted(stream)
    true_p99 = srt[int(0.99 * (len(srt) - 1))]
    true_p01 = srt[int(0.01 * (len(srt) - 1))]

    p99, p01 = tdigest_lite(stream, compression=200.0)
    e99, e01 = abs(p99 - true_p99), abs(p01 - true_p01)
    centroids = _build(srt, 200.0)
    print(f"p99 est={p99:.3f} true={true_p99:.3f} err={e99:.3f} | "
          f"p01 est={p01:.3f} true={true_p01:.3f} err={e01:.3f} | centroids={len(centroids)}")

    # RECOVERY ASSERT 1: tail quantiles within 1.0 (~0.1 sigma of a N(.,10)). This is a
    # REAL tail-accuracy claim -- 30x tighter than the old max(30, 0.5*range) hatch.
    assert e99 < 1.0 and e01 < 1.0, f"t-digest tail error too large: p99={e99:.3f}, p01={e01:.3f}"

    # RECOVERY ASSERT 2: the space win -- far fewer centroids than points, and the
    # tail-scaling kept the extreme centroids small (defining property).
    assert len(centroids) < 0.1 * len(stream), "t-digest failed to compress"
    assert centroids[-1][1] < centroids[len(centroids) // 2][1], \
        "tail centroids must be smaller than mid centroids (tail-scaling)"
    print("t-digest PASS")
