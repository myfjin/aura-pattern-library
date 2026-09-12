"""
Sliding Window Quantile — compute the exact quantile over the most recent N elements
in a stream.

WHAT IT DOES: Maintains a deque of the last window_size elements and sorts them to
compute the exact q-th quantile with linear interpolation for non-integer indices.

WHEN TO USE: You need exact quantiles over a fixed-size sliding window and the window
is small enough to sort — monitoring dashboards, real-time analytics.

GUARANTEES: Exact — matches batch quantile to floating-point precision. O(window_size)
memory.

NOT: An approximate sketch. Stores all window elements. O(window_size·log window_size)
per query. Not suitable for very large windows.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"