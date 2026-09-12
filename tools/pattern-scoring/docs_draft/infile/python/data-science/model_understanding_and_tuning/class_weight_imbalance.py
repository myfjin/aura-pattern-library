"""
Class Weights for Imbalanced Classification — upweight minority class to recover recall.

WHAT IT DOES: Weighted binary cross-entropy with inverse frequency weights. Unweighted
model misses all minority samples. Weighted recovers recall.

WHEN TO USE: Classification with severe class imbalance where minority class matters.

GUARANTEES: Weighted recall ≥ unweighted recall × 0.8. Weighted recall > 0.1.

NOT: A sampling method. Uses loss weighting, not data resampling.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"