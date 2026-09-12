"""
Missing Value Imputation — replace None/NaN with mean/median/mode + missing indicators.

WHAT IT DOES: Fills missing values with chosen statistic. Returns imputed data + binary
missing indicator. No None values remain. Imputed values match strategy.

WHEN TO USE: Handling incomplete datasets, preserving row count, understanding missingness.

GUARANTEES: No None remains. Indicators correct (1 where missing). Imputed values match
strategy (mean/median/mode of non-missing).

NOT: A model-based imputation. Does not use regression or MICE for multivariate imputation.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"