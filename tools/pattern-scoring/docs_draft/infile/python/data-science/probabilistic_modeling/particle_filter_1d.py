"""
Particle Filter (SMC) — track a noisy 1D random walk target.

WHAT IT DOES: Maintains weighted particles. Predict, weight by observation likelihood,
resample when ESS < n/2. Particle-mean RMSE beats raw observations. ESS monitors degeneracy.

WHEN TO USE: Nonlinear filtering, state tracking, online Bayesian inference.

GUARANTEES: Particle RMSE < observation RMSE. ESS in (0, n_particles]. Average ESS reasonable.

NOT: A general-purpose particle filter. 1D only. Uses Gaussian dynamics and observation models.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"