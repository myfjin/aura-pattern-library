"""
Gaussian Copula — model dependence structure separately from marginals.

WHAT IT DOES: Samples from bivariate normal with correlation rho, transforms to
uniform via CDF. Spearman rank correlation of the uniform samples is close to the
true rho. Dependence structure preserved regardless of marginals.

WHEN TO USE: Modeling dependencies when marginal distributions are not normal.

GUARANTEES: Estimated rank correlation within 0.2 of true rho (n=500).

NOT: A non-Gaussian copula. Only implements the Gaussian (normal) copula.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"