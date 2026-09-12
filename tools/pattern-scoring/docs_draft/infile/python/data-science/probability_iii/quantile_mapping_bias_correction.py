"""
Quantile Mapping Bias Correction — correct distributional bias by matching quantiles.

WHAT IT DOES: For each point in biased data, finds its quantile, then maps to the
reference value at the same quantile. Corrected median matches reference median
within 1.0 unit. Non-parametric — no distributional assumptions.

WHEN TO USE: Bias correction in climate models, sensor calibration.

GUARANTEES: Corrected median within 1.0 of reference median.

NOT: A parametric correction. Does not assume a specific distribution family.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"