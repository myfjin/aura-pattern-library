"""
Histogram Builder — equal-width bins with Sturges' rule bin count.

WHAT IT DOES: k = ceil(log₂(n)) + 1 bins via Sturges' rule. Counts sum to n. Edges ordered.
Bimodal data shows two peaks.

WHEN TO USE: EDA, visualizing distributions, detecting multimodality.

GUARANTEES: Counts sum to n. Edges monotonic. Bin count follows Sturges' rule.

NOT: An adaptive binning method. Sturges' rule works well for normal data but may
under-smooth multimodal distributions.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"