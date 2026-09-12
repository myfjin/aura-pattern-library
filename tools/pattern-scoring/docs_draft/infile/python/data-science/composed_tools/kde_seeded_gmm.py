"""
KDE-Seeded Gaussian Mixture — the nonparametric scout guides the parametric army.

WHAT IT DOES: KDE runs first as a scout: its density modes reveal how many components
exist and where, seeding EM's initial means. Random-initialized EM on unbalanced
mixtures routinely collapses components; the KDE-seeded start doesn't have to guess.

WHEN TO USE: Fitting mixtures without knowing k, or when random-init EM is unstable
on unbalanced components.

GUARANTEES: KDE scout finds exactly the right number of modes. Seeded EM recovers all
true means. Random init fails at least some trials. Seeded solution matches or beats
best random restart in log-likelihood.

NOT: A general-purpose clustering method. Only for 1D Gaussian mixtures.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"