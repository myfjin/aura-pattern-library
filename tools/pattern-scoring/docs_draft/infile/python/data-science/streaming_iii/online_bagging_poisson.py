"""
Online Bagging via Poisson(1) Weighting — bag an ensemble over a stream in one pass
with bounded memory.

WHAT IT DOES: Draws k ~ Poisson(1) per arriving point per model and updates that model
with weight k — no stored dataset, one pass. Oza's theorem: the online ensemble converges
to the batch-bagging ensemble.

WHEN TO USE: You need to train an ensemble on a stream where you can't store the data
and need the same guarantees as batch bagging.

GUARANTEES: Online bagging reproduces batch bagging (≥ 99% prediction agreement). The
ensemble is genuinely diverse (≥ 3 distinct stumps) and denoises a single stump by > 3%.

NOT: A general-purpose ensemble. Uses decision stumps as base learners. Requires
pre-specified split thresholds.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"