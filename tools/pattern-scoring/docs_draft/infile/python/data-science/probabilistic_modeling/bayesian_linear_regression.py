"""
Bayesian Linear Regression — conjugate normal prior, closed-form posterior.

WHAT IT DOES: Prior N(μ₀, Σ₀); likelihood N(y | Xβ, σ²I); posterior is N(μ_post, Σ_post).
Posterior mean is between prior and OLS. Variance shrinks with data.

WHEN TO USE: Interpretable regression with uncertainty, small data, informative priors.

GUARANTEES: Weak prior posterior near OLS. Strong prior pulls toward prior mean. Posterior
variance shrinks from prior.

NOT: A general Bayesian regression. Assumes known noise variance σ².
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"