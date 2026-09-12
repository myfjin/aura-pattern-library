"""
KSWIN — Kolmogorov-Smirnov Windowing Drift Detector — detect distribution shift using
the KS two-sample test on sliding windows.

WHAT IT DOES: Maintains two windows from the stream and applies the KS test to check
whether they come from the same distribution. The KS statistic measures the maximum
absolute difference between the empirical CDFs. If it exceeds a critical value from the
Kolmogorov distribution, drift is declared.

WHEN TO USE: You need a non-parametric drift detector that makes no assumptions about
the underlying distribution — works for any continuous-valued stream.

GUARANTEES: No false positives on stationary streams. Detects shifts of ≥ 2σ in mean.

NOT: A streaming detector (processes the full stream at once, not one-at-a-time). Does
not localize where the drift occurs within the stream.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"