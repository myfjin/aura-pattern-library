"""
HyperLogLog Cardinality Estimation — count distinct elements in a massive stream
using fixed tiny memory (~4KB for p=12).

WHAT IT DOES: Hashes each element to 64 bits. The first p bits pick one of m = 2^p
registers. The remaining bits' rank (position of the leftmost 1) updates that register
to its maximum. Estimates distinct count from the harmonic mean of 2^rank across all
registers. Uses linear counting correction for small cardinalities.

WHEN TO USE: You need to count unique visitors, distinct IPs, unique search queries on
a high-volume stream where storing all IDs is impossible.

GUARANTEES: Standard error ≈ 1.04/√m. With p=12 (4096 registers), rel error < 5%
(3-sigma). Beats the naive stream-length guess by 10x.

NOT: A precise count. Returns an estimate with known error bounds. Does not support
deletions or set operations (union/intersection).
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"