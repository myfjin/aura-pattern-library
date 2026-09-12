"""
Quantile Binning — equal-frequency vs equal-width binning.

WHAT IT DOES: Quantile binning: roughly equal counts per bin even on skewed data.
Equal-width: imbalanced on skew. All bins used.

WHEN TO USE: Discretizing continuous features, handling skewed distributions.

GUARANTEES: Quantile bins roughly equal (15-35 per bin for 100 pts, 4 bins). Equal-width
imbalanced on skew (first half > 1.5× second). All bins used.

NOT: An adaptive binning method. Does not optimize bin boundaries for predictive power.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"