"""
Three-Way Stratified Split — train/val/test preserving class proportions.

WHAT IT DOES: Groups by class, splits each class proportionally, combines. Proportions
preserved within 5%. All classes in all splits. No overlap.

WHEN TO USE: Classification datasets, ensuring class proportions preserved in all splits.

GUARANTEES: Proportions within 5% of full. All classes in all splits. No overlap.

NOT: A time-series split. Assumes i.i.d. samples. Does not handle temporal ordering.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"