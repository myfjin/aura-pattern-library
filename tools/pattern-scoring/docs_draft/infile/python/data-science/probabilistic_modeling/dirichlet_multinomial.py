"""
Dirichlet-Multinomial Conjugate — conjugate posterior over category probabilities.

WHAT IT DOES: Dirichlet prior Dir(α); multinomial counts; posterior Dir(α + counts). MAP
estimate = (α_i + count_i − 1) / (sum(α) + sum(counts) − K). Sequential ≡ batch.

WHEN TO USE: Topic modeling, urn problems, belief updating on discrete distributions.

GUARANTEES: Posterior sums to 1. Weak prior matches empirical. Strong prior skews posterior.

NOT: A full Bayesian analysis. Only provides MAP estimate, not full posterior samples.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"