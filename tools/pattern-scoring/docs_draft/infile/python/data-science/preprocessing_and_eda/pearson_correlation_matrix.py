"""
Pearson Correlation Matrix — pairwise correlation between all numeric columns.

WHAT IT DOES: r = cov(x,y) / (σ_x · σ_y). Diagonal = 1. Symmetric. Perfectly correlated
variables have r = 1.0. Independent variables have near-zero correlation.

WHEN TO USE: EDA for relationships, feature selection, multicollinearity detection.

GUARANTEES: Diagonal = 1. Symmetric. Perfect correlation → r = 1.0. Independent → r near 0.

NOT: A robust correlation. Pearson is sensitive to outliers. Use Spearman for monotonic
nonlinear relationships.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"