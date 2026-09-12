"""
Random Oversampling and SMOTE-Lite — rebalance imbalanced datasets.

WHAT IT DOES: Random oversampling duplicates minority samples. SMOTE-lite interpolates
between minority neighbors. Majority class unchanged. Classes balanced after.

WHEN TO USE: Imbalanced classification, oversampling minority before training.

GUARANTEES: Classes balanced after. Majority size unchanged. SMOTE generates synthetic
samples.

NOT: A full SMOTE implementation. SMOTE-lite uses random minority pair, not k-NN neighbors.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"