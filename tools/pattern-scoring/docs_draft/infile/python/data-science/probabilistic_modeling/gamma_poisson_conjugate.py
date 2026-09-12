"""
Gamma-Poisson Conjugate Prior — Gamma prior on Poisson rate, closed-form posterior.

WHAT IT DOES: Prior Gamma(α, β); Poisson counts; posterior Gamma(α + Σcount, β + n).
Posterior mean between prior and empirical. Variance shrinks. Sequential ≡ batch.

WHEN TO USE: Rate estimation, count data modeling, reliability/failure analysis.

GUARANTEES: Posterior matches closed form. Mean between prior and empirical. Variance
shrinks. Sequential matches batch.

NOT: A general Bayesian model. Only for Poisson likelihood with Gamma prior.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"