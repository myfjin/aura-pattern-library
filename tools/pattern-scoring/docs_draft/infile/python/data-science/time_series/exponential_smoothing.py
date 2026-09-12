"""
Exponential Smoothing — smooth a time series and forecast short-term.

WHAT IT DOES: SES: smooth_t = α·y_t + (1−α)·smooth_{t-1}. Holt's adds trend:
level_t = α·y_t + (1−α)·(level_{t-1} + trend_{t-1}). SES forecasts flat; Holt's
forecasts with trend.

WHEN TO USE: Short-horizon forecasting when trend matters — demand planning,
inventory forecasting.

GUARANTEES: SES reduces variance (smoothed < raw). Holt's detects positive trend
(avg trend > 0). Holt forecast increases; SES forecast is flat.

NOT: A seasonal method. Does not implement Holt-Winters (triple exponential
smoothing with seasonality).
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"