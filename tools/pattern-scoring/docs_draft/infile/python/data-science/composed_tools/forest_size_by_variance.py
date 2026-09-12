"""
Forest Size by Variance — stop hiring trees when the crew is steady enough.

WHAT IT DOES: Runs bias-variance decomposition's bootstrap estimator across forest
sizes. Bias stays flat while ensemble variance falls as ~1/n. The data-driven size
is the diminishing-returns knee: the smallest forest capturing ≥80% of achievable
variance reduction.

WHEN TO USE: You need to choose a random forest size with evidence, not a default.

GUARANTEES: Variance falls ≥3× from 1 to 32 trees. Bias stays ~flat. The knee is
an interior size (4-16), not an extreme.

NOT: A universal rule. The knee depends on the problem's signal-to-noise ratio.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"