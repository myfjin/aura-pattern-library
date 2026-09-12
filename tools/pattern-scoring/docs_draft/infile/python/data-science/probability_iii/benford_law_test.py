"""
Benford's Law Test — test whether a dataset follows Benford's law via chi-square.

WHAT IT DOES: P(digit d) = log₁₀(1 + 1/d). Multiplicative data (powers of 2) fits
Benford; uniform data violates it. Chi-square statistic measures fit.

WHEN TO USE: Fraud detection, data integrity checks.

GUARANTEES: Multiplicative data has lower chi-square than uniform data. Leading digit
extraction handles values < 1 correctly.

NOT: A formal hypothesis test. Does not compute p-values or critical values.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"