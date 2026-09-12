"""
Rolling OLS Update — a running balance instead of a recount.

WHAT IT DOES: Maintains the window's covariance incrementally (Welford-style add/
remove) and reads the OLS slope off it. Identical coefficients to naive refit,
O(1) per step instead of O(window).

WHEN TO USE: You need time-varying regression coefficients on a high-frequency stream
where O(window) per step is too expensive.

GUARANTEES: Rolling equals naive refit to machine precision (max dev < 1e-8). Tracks
planted slope changes. Rolling does < 10% of refit's work.

NOT: A multivariate regression. Only handles simple (x, y) pairs. Does not compute
standard errors or confidence intervals.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"