"""
Windowed Distinct Count — count the exact number of distinct elements in the most recent
N items of a stream.

WHAT IT DOES: Maintains a deque of the last window_size elements and computes
len(set(window)) at query time. Simple, exact, O(window_size) memory.

WHEN TO USE: You need exact distinct counts over a fixed-size sliding window — real-time
dashboards, monitoring unique users in the last hour.

GUARANTEES: Exact — matches batch distinct count. O(window_size) memory.

NOT: An approximate sketch. Stores all window elements. O(window_size) per query. Not
suitable for very large windows or high-cardinality streams.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"