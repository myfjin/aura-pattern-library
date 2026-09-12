"""
Platt Scaling for Probability Calibration — recalibrate classifier scores.

WHAT IT DOES: Fits logistic function p = 1/(1 + exp(−(a·score + b))) on hold-out set.
Reduces Brier score. Calibrated Brier < baseline.

WHEN TO USE: Recalibrating overconfident classifier scores to true probabilities.

GUARANTEES: Calibrated Brier < baseline. Calibrated Brier < 0.25.

NOT: A multiclass calibration method. Binary only. Use temperature scaling for multiclass.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"