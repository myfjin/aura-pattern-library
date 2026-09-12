"""
Partial Dependence Plot — marginal effect of a feature on predictions.

WHAT IT DOES: Averages predictions as one feature varies, holding others at data values.
Informative feature shows monotone curve. Noise feature is flat.

WHEN TO USE: Understanding marginal feature effects, model interpretation.

GUARANTEES: Informative feature monotone increasing. Noise feature flat (var < 0.5).

NOT: A causal interpretation tool. Assumes feature independence (may show extrapolation).
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"