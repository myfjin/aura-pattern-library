"""
Bayesian Two-Segment Changepoint — compare model evidence for no-change vs change-at-t.

WHAT IT DOES: Compares log-likelihood of single-segment vs two-segment model split at each
point. Bayes factor favors 2-segment when a real change exists. Detected split near planted
change.

WHEN TO USE: Quality control, structural break detection, time-series anomalies.

GUARANTEES: Detected split within 5 of true. BF > 0 for change data. |BF| < 3 for no-change.

NOT: A full Bayesian changepoint model. Assumes known noise variance.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"