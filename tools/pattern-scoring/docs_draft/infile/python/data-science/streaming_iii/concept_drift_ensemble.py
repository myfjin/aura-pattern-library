"""
Concept-Drift Ensemble vs. Frozen Single Learner — prove that a drift-aware ensemble
adapts to a changing concept while a frozen learner gets stuck on the old one.

WHAT IT DOES: On a stream whose label distribution flips at the midpoint, the ensemble
spawns a fresh learner per window and weights each by its recent accuracy. The frozen
learner predicts the pre-drift majority forever. The gap between them on post-drift data
is the measure that matters.

WHEN TO USE: You need to demonstrate why adaptive models matter in streaming classification.

GUARANTEES: Ensemble recovers to the new concept (accuracy > 0.75). Frozen learner
collapses (< 0.30). The gap exceeds 0.40.

NOT: A production ensemble. Uses simple majority-vote learners, not weighted classifiers.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"