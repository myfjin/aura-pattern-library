"""
Gaussian Process Regression (Lite) — RBF kernel, small n, direct Cholesky solve.

WHAT IT DOES: Places Gaussian priors on function values. Posterior mean interpolates
training data. CI coverage ≥ 85% on held-out points. RBF kernel only, direct dense solve.

WHEN TO USE: Small-data regression with uncertainty, interpolation, Bayesian optimization.

GUARANTEES: Training points interpolated (error < 0.5). CI coverage ≥ 85%. CI bounds valid.

NOT: A scalable GP. Uses dense Cholesky solve — O(n³). No sparse or inducing-point methods.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"