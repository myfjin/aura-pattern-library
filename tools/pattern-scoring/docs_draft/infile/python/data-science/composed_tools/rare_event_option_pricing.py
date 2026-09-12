"""
Rare-Event Option Pricing — importance sampling where naive Monte Carlo goes blind.

WHAT IT DOES: Shifts the sampling drift toward the payoff region (deep OTM strike)
and re-weights by the likelihood ratio. Verified against the Black-Scholes closed
form. A thousand tilted paths beat a million blind ones.

WHEN TO USE: Pricing deep out-of-the-money options or any rare-event expectation
where naive MC has near-zero hit rate.

GUARANTEES: Naive MC is visibly blind (rel err > 3× IS error). IS lands within 10%
of BS truth. Estimator SE < 10% of truth.

NOT: A general MC variance reduction. The theta shift must be correctly targeted at
the payoff region.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"