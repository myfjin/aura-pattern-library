"""
Winsorization and Clipping — cap extreme values at percentile thresholds or hard bounds.

WHAT IT DOES: Winsorization caps at percentile limits (e.g., 5th/95th). Clipping enforces
hard bounds [min, max]. Count unchanged. Range much tighter after winsorization.

WHEN TO USE: Outlier mitigation, handling measurement errors, robust preprocessing.

GUARANTEES: Count unchanged. Extreme values capped. Range < 70% of original after
winsorization. Clipping enforces hard bounds.

NOT: A robust alternative to winsorization. Does not use MAD or other robust scale estimates.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"