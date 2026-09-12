"""
Cross-Validation Data Leakage — the silent score inflator.

WHAT IT DOES: You split data into train/test, but you did feature selection on the
FULL dataset before splitting. That means the test set secretly helped choose the
features — so your cross-validation score looks better than it should. This pattern
demonstrates the leak: feature selection on all data inflates CV accuracy by ~0.05-0.10
compared to the honest approach (fit feature selection inside each fold on training
data only).

WHEN TO USE: Any time you do preprocessing (feature selection, scaling, imputation)
before cross-validation. The rule is simple: anything that looks at the data must be
inside the CV loop, not outside.

GUARANTEES: Leaky CV accuracy > correct CV accuracy. The inflation gap exceeds 0.05
(measurable and detectable). The effect is reproducible across 4-fold CV with 100
noise features and 5 true features.

NOT: A general cross-validation tool. Only demonstrates the specific leak from
preprocessing-before-split. Other leak sources (data-dependent parameter tuning,
leaky feature engineering) are not covered.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
