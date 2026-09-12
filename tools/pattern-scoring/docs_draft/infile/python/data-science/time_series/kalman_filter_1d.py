"""
1D Kalman Filter — recursively estimate the state of a 1D system from noisy
observations.

WHAT IT DOES: Balances prediction (prior) and observation (likelihood) using
Gaussian uncertainties. Kalman gain weights the innovation. Filtered MSE is lower
than raw observation MSE. Gains converge as the filter learns to trust its estimate.

WHEN TO USE: Smoothing GPS readings, sensor data, or tracking slow-moving targets.

GUARANTEES: Filtered MSE < raw MSE. Kalman gains in (0, 1) and converge. Filtered
mean within 0.5 of true value.

NOT: A multi-dimensional Kalman filter. Only handles 1D constant-value or
constant-velocity models.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"