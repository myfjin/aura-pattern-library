"""
Block Maxima: Gumbel Distribution — fit Gumbel to extreme values for return-level
estimation.

WHAT IT DOES: Fits Gumbel(μ, σ) to block maxima via moment matching. Gumbel CDF:
F(x) = exp(−exp(−(x−μ)/σ)). Return level for T periods: x_T where F(x_T) = 1 − 1/T.

WHEN TO USE: Extreme value analysis — flood levels, max temperatures, worst-case
latency.

GUARANTEES: Fitted μ within 5, σ within 3 of true. CDF correct at median (F=0.5).
Return level within 2σ of true.

NOT: A GEV (Generalized Extreme Value) fit. Only fits the Gumbel (Type I) family.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"