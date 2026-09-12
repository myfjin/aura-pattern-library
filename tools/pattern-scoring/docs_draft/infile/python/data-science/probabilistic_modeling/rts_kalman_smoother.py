"""
RTS Kalman Smoother — forward-backward pass for optimal smoothing.

WHAT IT DOES: Forward Kalman filter, then RTS backward pass corrects trajectory using all
future observations. Smoothed RMSE < filtered RMSE < raw RMSE. Covariances positive and
decrease after backward pass.

WHEN TO USE: Trajectory estimation, state inference after all data arrives (offline).

GUARANTEES: Smoothed < filtered < raw RMSE. Covariances positive. Smoothed cov ≤ filtered cov.

NOT: An online filter. Requires all data for the backward pass. 1D constant-velocity model.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"