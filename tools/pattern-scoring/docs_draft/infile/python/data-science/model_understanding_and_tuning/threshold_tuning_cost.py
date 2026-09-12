"""
Threshold Tuning with Asymmetric Costs — find optimal decision threshold.

WHAT IT DOES: Grid search over thresholds with asymmetric costs (FN = 10× FP). Optimal
threshold < 0.5 when FN cost > FP cost. Cost reduction > 20%.

WHEN TO USE: Fraud detection, spam filtering where misclassification costs are unequal.

GUARANTEES: Optimal threshold < 0.5 (FN cost > FP). Optimal cost < default. Reduction > 20%.

NOT: A ROC curve analysis. Directly optimizes cost, not AUC.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"