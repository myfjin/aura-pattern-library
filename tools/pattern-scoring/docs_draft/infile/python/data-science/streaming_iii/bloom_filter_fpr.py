"""
Bloom Filter with Measured False-Positive Rate — test membership with bounded FPR and
zero false negatives.

WHAT IT DOES: Hashes each inserted item to k positions in a bit array and sets those
bits. To query, check if all k positions are set. If any is unset, the item is definitely
not in the set. If all are set, the item is probably in the set. Measures the empirical
false-positive rate against the theoretical bound (1 − e^(−k·n/m))^k.

WHEN TO USE: You need to check membership in a large set but can tolerate a small
false-positive rate — cache filtering, spell-check dictionaries, network dedup.

GUARANTEES: Zero false negatives. Measured FPR ≤ theoretical FPR + 5% slack.

NOT: A production-grade filter. Uses MD5 for hashing (slow). Does not support deletion.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"