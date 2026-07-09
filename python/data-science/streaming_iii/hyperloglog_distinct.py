"""
HyperLogLog cardinality estimation (Flajolet et al.).
Core idea: hash each element to 64 bits; the first p bits pick a register, the rank
(position of the leftmost 1) in the remaining bits updates that register with its max;
estimate distinct count from the harmonic mean of 2^register across m = 2^p registers.
When: count distinct elements on massive streams in fixed tiny memory (m registers).
Standard error is 1.04/sqrt(m); with p=12 (m=4096) that is ~1.6%.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import hashlib
import math
import random
from typing import List


def _hash64(x) -> int:
    # Deterministic across processes (no PYTHONHASHSEED salt, unlike builtin hash()).
    h = hashlib.blake2b(repr(x).encode(), digest_size=8).digest()
    return int.from_bytes(h, "big")


def hyperloglog_distinct(stream: List, p: int = 12) -> int:
    """
    Estimate the number of distinct elements via HyperLogLog.
    Args:
        stream: input sequence (with duplicates)
        p: log2 of the number of registers (m = 2**p)
    Returns:
        Estimated distinct count.
    """
    assert 4 <= p <= 16
    m = 1 << p
    registers = [0] * m
    suffix_bits = 64 - p

    for elem in stream:
        h = _hash64(elem)
        idx = h >> suffix_bits                      # first p bits -> register index
        w = h & ((1 << suffix_bits) - 1)            # remaining bits
        # rank = position of leftmost 1-bit (1-based) within suffix_bits
        rank = suffix_bits - w.bit_length() + 1 if w else suffix_bits + 1
        if rank > registers[idx]:
            registers[idx] = rank

    # Raw estimate: alpha_m * m^2 / sum(2^-reg)
    alpha = 0.7213 / (1 + 1.079 / m)
    inv_sum = sum(2.0 ** (-r) for r in registers)
    estimate = alpha * m * m / inv_sum

    # Small-range correction: linear counting when many registers are empty.
    zeros = registers.count(0)
    if estimate <= 2.5 * m and zeros > 0:
        estimate = m * math.log(m / zeros)

    return int(round(estimate))


if __name__ == "__main__":
    random.seed(42)  # deterministic: seed BEFORE any data generation
    # Plant a known cardinality: exactly 8000 distinct ids, each repeated ~a few times.
    distinct_ids = list(range(8000))
    stream = [random.choice(distinct_ids) for _ in range(40000)]
    true_distinct = len(set(stream))  # ~8000 (nearly all appear)

    est = hyperloglog_distinct(stream, p=12)
    rel_err = abs(est - true_distinct) / true_distinct
    print(f"HyperLogLog p=12: est={est}, true={true_distinct}, rel_err={rel_err:.4f}")

    # RECOVERY ASSERT: HLL recovers the planted cardinality within ~3x its own
    # standard error (1.04/sqrt(4096) = 1.63%). Bound 0.05 (~3 sigma) -- a real
    # accuracy claim. (Measured rel_err on this seed printed above.)
    assert rel_err < 0.05, f"HLL cardinality error {rel_err:.4f} exceeds 3-sigma bound"

    # And it must crush the trivial stream-length guess.
    naive_rel = abs(len(stream) - true_distinct) / true_distinct
    assert rel_err < naive_rel / 10, "HLL should beat the stream-length guess by 10x"
    print("HyperLogLog PASS")
