"""
Sliding Window Regression — track a time-varying regression coefficient on streaming
data via windowed OLS.

WHAT IT DOES: Maintains a sliding window of (x, y) pairs and recomputes the OLS slope
over the most recent window. When the underlying relationship changes, the windowed
estimate tracks the new regime.

WHEN TO USE: You need to detect and track non-stationary relationships — time-varying
beta in finance, sensor calibration drift.

GUARANTEES: Windowed estimate reflects the current regime within one window length.
O(window_size) per step.

NOT: An incremental update. Recomputes OLS from scratch per window. Not suitable for
very large windows or high-frequency streams.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"