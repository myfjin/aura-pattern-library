"""
Empirical Bayes Shrinkage (James-Stein) — shrink group means toward grand mean.

WHAT IT DOES: Positive-part James-Stein (K−3 rule). Shrunken means closer to grand mean
than raw. Beats raw means in aggregate SE over replications (Stein's paradox measured).
Homogeneous data shrinks harder.

WHEN TO USE: Meta-analysis, small-group inference, estimation of many parameters.

GUARANTEES: Shrunken closer to grand mean. Shrinkage wins >55% of datasets. Homogeneous
data shrinks harder.

NOT: A full hierarchical Bayesian model. Uses empirical Bayes (hyperparameter estimated
from data).
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"