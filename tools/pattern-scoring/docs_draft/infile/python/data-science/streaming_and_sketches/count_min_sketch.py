"""
Count-Min Sketch for Frequency Estimation — count frequencies in a massive stream
using almost no memory.

WHAT IT DOES: A probabilistic data structure: a 2D array of counters with multiple
hash functions. To increment an item, hash it with each function and increment the
corresponding counter. To query, take the minimum across all hash functions. The
estimate is guaranteed to be an upper bound (never under-counts), with error bounded
by epsilon * total.

WHEN TO USE: You have a massive data stream and need approximate frequency estimates
with formal error bounds. Classic use: finding heavy hitters in network traffic,
trending topics on Twitter, frequent items in a data stream.

GUARANTEES: Estimates never under-count (estimate >= true count). Error is bounded
by epsilon * total_stream_count + slack. Heavy hitters above threshold are detected.

NOT: A production sketch. Uses MD5 for hashing (slow). Does not implement the
"conservative update" variant for tighter estimates. The heavy hitter finder scans
all cells (O(width*depth)) rather than using a heap.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
