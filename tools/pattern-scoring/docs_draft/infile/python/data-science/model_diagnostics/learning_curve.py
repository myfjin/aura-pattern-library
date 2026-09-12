"""
Learning Curve Analysis — how much data does your model need?

WHAT IT DOES: Plot error vs training set size. As you add more training data, training
error should increase (the model can't memorize everything) and validation error should
decrease (the model generalizes better). If both curves are high and flat, you have
high bias (model too simple). If training is low but validation is high, you have
high variance (model overfits).

WHEN TO USE: Diagnosing whether your model would benefit from more data. If the
validation curve is still decreasing at the largest training size, more data will help.
If it's flat, you need a better model, not more data.

GUARANTEES: Training error stays below 2.0. Validation error exceeds training error
at small sample sizes. Validation error decreases with more training data.

NOT: A general learning curve tool. Only demonstrates the concept with a simple linear
model on synthetic data. Does not handle classification, multiple models, or real data.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
