"""
Lossy Counting for Frequent Items — find all items that appear more than s·N times in
a stream, in one pass, with bounded memory.

WHAT IT DOES: Divides the stream into buckets of width w = ceil(1/ε). Stores each item
as (freq, delta) where delta is the max possible undercount at insertion. Prunes items
with freq+delta ≤ current_bucket at bucket boundaries. Outputs items with freq ≥ (s−ε)·N.

WHEN TO USE: You need to find frequent items in one pass with a provable error/space
tradeoff — network traffic analysis, trending topics.

GUARANTEES: Zero false negatives for true frequency ≥ s·N. No reported item has true
frequency < (s−ε)·N. Reported frequencies undercount true by at most ε·N.

NOT: A streaming sketch. Processes the full stream in one pass but stores all candidate
items until pruning. eps must be < support.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"