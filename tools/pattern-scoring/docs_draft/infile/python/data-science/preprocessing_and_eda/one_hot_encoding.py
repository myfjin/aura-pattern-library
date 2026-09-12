"""
One-Hot Encoding — convert categorical features into binary indicators.

WHAT IT DOES: Each category → binary column. Exactly one 1 per row. Round-trip matches
original. Unknown categories: 'error' raises, 'ignore' gives all zeros.

WHEN TO USE: Preprocessing categorical columns before model training.

GUARANTEES: Exactly one 1 per row. Round-trip matches original. Unknown handling correct.

NOT: A label encoder. Does not handle ordinal categories or high-cardinality features
(use target encoding for those).
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"