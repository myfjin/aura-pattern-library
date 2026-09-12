"""
Covariance Matrix — compute sample covariance between all numeric columns.

WHAT IT DOES: cov(i,j) = Σ (x_i − mean_i)(x_j − mean_j) / (n−1). Symmetric matrix.
Diagonal = variance. Positive covariance for positively correlated variables.

WHEN TO USE: Understanding variance structure, multivariate analysis, PCA setup.

GUARANTEES: Symmetric. Diagonal positive and matches direct variance. Positive covariance
for positively correlated variables.

NOT: A correlation matrix. Covariance is scale-dependent. Use correlation for
scale-free association.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"