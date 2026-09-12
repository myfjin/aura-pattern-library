"""
Autocorrelation Function (ACF) — measure how a time series correlates with its own
past.

WHAT IT DOES: ACF(k) = cov(y_t, y_{t-k}) / var(y_t). Includes significance bounds
(±2/√n) to identify significant lags. For AR(1) with φ=0.6, ACF decays as 0.6^k.

WHEN TO USE: First-look analysis of any time series — does it have memory? Is it
seasonal?

GUARANTEES: ACF at lag 0 is always 1.0. AR(1) ACF decays exponentially. White noise
has few significant lags (< 5 at α=0.05).

NOT: A partial ACF (PACF). Does not distinguish direct from indirect correlation.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"