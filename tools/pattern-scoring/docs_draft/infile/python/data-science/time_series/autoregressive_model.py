"""
Autoregressive (AR) Model — predict the future from the past.

WHAT IT DOES: An AR(p) model says: the next value is a linear combination of the p
previous values, plus noise. y_t = c + phi_1*y_{t-1} + ... + phi_p*y_{t-p} + noise.
Fit by solving the normal equations directly (no external libraries). Produces
one-step-ahead forecasts and beats the naive mean forecast.

WHEN TO USE: Univariate time series prediction when past values predict the future.
AR models are the foundation of all time series modeling — ARIMA, SARIMA, and
state-space models all build on this idea.

GUARANTEES: AR(1) recovers the planted phi coefficient within [0.5, 0.9] (true
value 0.7). AR forecasts beat the naive mean forecast in mean absolute error. AR(2)
also fits successfully.

NOT: A general ARIMA implementation. Only supports p=1 and p=2 (explicit normal
equations for each). No model selection (AIC/BIC), no diagnostics, no forecasting
beyond one step ahead. The normal equations are solved directly — no QR or SVD for
numerical stability.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
