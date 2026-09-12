"""
DTW Shape-Drift Monitor — catch "the day looks wrong" when every point statistic
looks fine.

WHAT IT DOES: DTW-matches each day against a reference profile and EWMA-smooths the
distances. Drift = smoothed distance crossing a calibrated MAD fence. Point monitors
(mean/variance z-scores) are blind to shape changes — the whole point.

WHEN TO USE: Monitoring periodic profiles (traffic, load, sales) where timing and
shape matter, not just level.

GUARANTEES: Point monitor flags zero shape-drift days (blind). Shape monitor catches
drift within 3 days of change. Zero false alarms on normal days.

NOT: An amplitude-change detector. Point monitors handle level shifts; this handles
shape shifts that preserve mean and variance.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"