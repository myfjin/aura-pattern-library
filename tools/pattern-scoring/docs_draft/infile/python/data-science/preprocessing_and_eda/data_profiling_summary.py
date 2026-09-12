"""
Data Profiling Summary — per-column profile of mixed datasets.

WHAT IT DOES: Type inference, missing count, cardinality, min/max/mean for numeric, top
values for categorical. One-pass summary without external libraries.

WHEN TO USE: EDA, data quality checks, understanding dataset structure before modeling.

GUARANTEES: Numeric columns get min/max/mean. Categorical get top values. Missing counts
accurate.

NOT: A full data quality report. Does not detect outliers, skewness, or distribution shape.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"