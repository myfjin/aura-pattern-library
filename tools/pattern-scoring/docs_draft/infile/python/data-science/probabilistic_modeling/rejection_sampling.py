"""
Rejection Sampling — sample from complex density under an envelope.

WHAT IT DOES: Samples from proposal, accepts with probability p(x) / (M · q(x)). Empirical
moments match numeric-integration moments. All samples in proposal support.

WHEN TO USE: Non-standard distributions, Bayesian posterior sampling, missing primitives.

GUARANTEES: Empirical mean within 0.5 of integrated. Empirical variance within 0.5. All
samples in proposal support.

NOT: An efficient sampler for high dimensions. Acceptance rate drops exponentially with
dimension.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"