"""
Mutual-Information Matrix — the dependence heatmap Pearson cannot draw.

WHAT IT DOES: Computes a feature-by-feature matrix with normalized mutual information
(binned, equal-frequency), side by side with |Pearson|. y = x² lights up where the
classic heatmap shows nothing.

WHEN TO USE: First-look EDA on features whose relationships may be nonlinear.

GUARANTEES: Both metrics see the linear pair (Pearson > 0.7, MI > 0.25). Pearson is
blind to y = x² (< 0.15). Normalized MI lights up the nonlinear pair (> 3× noise
level, > 0.2). Matrix is symmetric.

NOT: A causal discovery tool. MI measures dependence, not direction.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"