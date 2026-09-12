"""
Differencing for Stationarity — transform a non-stationary series into a stationary
one via first differencing.

WHAT IT DOES: d_t = y_t − y_{t-1}. Demonstrates that differencing reduces variance
drift (random walk) and mean drift (linear trend). Differenced random walk has mean
close to 0.

WHEN TO USE: Preprocessing step before fitting AR/ARIMA models — make the series
stationary first.

GUARANTEES: Differenced series is more stationary (variance ratio closer to 1).
Differencing reduces mean drift. Differenced series is shorter by 1.

NOT: A stationarity test. Does not implement the full ADF test — uses a simple
variance-ratio diagnostic.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"