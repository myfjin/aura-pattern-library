"""
CUSUM Change-Point Detection — detect step changes in the mean of a time series.

WHAT IT DOES: CUSUM_t = max(0, CUSUM_{t-1} + (y_t − target) − k). When CUSUM exceeds
threshold h, a change is signaled and the CUSUM resets. Stays low before the change,
rises after.

WHEN TO USE: Monitoring industrial processes, sensor data, or any stream where you
need to detect a mean shift quickly.

GUARANTEES: Detects a 5σ shift within ~10 samples of the change point. CUSUM rises
after the shift. Resets after detection for multiple change points.

NOT: A gradual-drift detector. CUSUM is designed for step changes, not slow drifts.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"