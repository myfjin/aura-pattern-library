"""
Misra-Gries Heavy Hitters — find all items that appear more than n/k times in a stream
using only k−1 counters.

WHAT IT DOES: Keeps at most k−1 counters. On each new item: increment its counter if it
exists, open a new counter if there's room, otherwise decrement ALL counters (dropping
any that hit zero). Every item with true frequency > n/k survives.

WHEN TO USE: You need to find heavy hitters in one pass with O(k) space — the simplest
and most elegant heavy-hitter algorithm.

GUARANTEES: Zero false negatives for items with true frequency > n/k. For every surviving
counter, true − n/k ≤ counter ≤ true. O(k) space.

NOT: A streaming sketch. Processes the full stream in one pass. Does not return exact
counts — counters undercount by at most n/k.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"