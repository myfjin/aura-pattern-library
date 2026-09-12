"""
Exponential Histogram / DGIM Windowed Count — count 1-bits in the last N arrivals
using O((1/ε)·log N) space instead of O(N).

WHAT IT DOES: Keeps buckets holding power-of-2 counts with timestamps. When a size
overflows its cap (k/2+1 where k = ceil(1/ε)), the two oldest buckets merge into one
double-size bucket. Old buckets outside the window expire. Estimate = sum of bucket
sizes − half the oldest in-window bucket.

WHEN TO USE: You need to count events in a sliding window but can't afford O(N) memory
— network traffic monitoring, sensor event counting.

GUARANTEES: Relative error ≤ ε. Uses O((1/ε)·log N) buckets, far below N.

NOT: A general counter. Only counts 1-bits in a binary stream. Does not support
decrements or deletions.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"