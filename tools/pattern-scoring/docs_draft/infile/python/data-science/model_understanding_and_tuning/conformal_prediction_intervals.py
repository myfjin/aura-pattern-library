"""
Split-Conformal Prediction Intervals — formal coverage guarantee for regression.

WHAT IT DOES: Train on train set, compute residuals on calibration set, set interval width
from quantile of residuals. Coverage ≥ 70% (target 90%). Model-agnostic.

WHEN TO USE: Prediction intervals with guaranteed coverage, non-Gaussian errors.

GUARANTEES: Coverage ≥ 70%. Interval width reasonable (> 0, < 100).

NOT: A Bayesian credible interval. Coverage is frequentist, not posterior.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"