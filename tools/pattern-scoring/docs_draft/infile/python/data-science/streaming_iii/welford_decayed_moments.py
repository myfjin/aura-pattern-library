"""
Welford Decayed Streaming Moments — track mean and variance on non-stationary streams
where recent samples matter more than old ones.

WHAT IT DOES: Maintains a decay-weighted running mean and M2 (Welford-style). A sample
t steps in the past has weight decay^t. On a level shift, the decayed mean tracks the
new regime while the plain global mean lags between old and new.

WHEN TO USE: You need to track mean/variance on streams with concept drift or regime
changes — sensor monitoring, financial volatility tracking.

GUARANTEES: Decayed mean recovers the current level within 1.0 unit after a shift. Beats
the global mean by > 3 units. Decayed variance reflects the recent regime, not the pooled
cross-regime spread.

NOT: A batch estimator. The decay factor controls the effective window size (half-life
~ ln(2)/ln(1/decay) steps).
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"