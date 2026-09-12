"""
Successive Halving for Hyperparameter Optimization — allocate budget to promising configs.

WHAT IT DOES: Evaluates all configs, keeps top half, doubles budget. 16 → 8 → 4 → 2 → 1.
Finds config close to planted optimum (lr ≈ 0.01). Best loss < 2.0.

WHEN TO USE: Many candidates but limited evaluation budget.

GUARANTEES: Best loss < 2.0. Learning rate near planted optimum 0.01.

NOT: A Bayesian optimization method. Simple elimination without surrogate model.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"