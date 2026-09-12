"""
Grid Search vs Random Search — random search efficiency with many hyperparams.

WHAT IT DOES: Grid: 3 values × 3 params = 27 evals. Random: 20 samples. Random finds
comparable quality with fewer evals when only some params matter.

WHEN TO USE: Many hyperparams but limited evaluation budget.

GUARANTEES: Random score within 0.05 of grid. Random uses fewer evals.

NOT: A Bayesian optimization method. Random search is still uninformed.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"