"""
k-Nearest Neighbors Classifier — the laziest classifier that still works.

WHAT IT DOES: To classify a new point, find the k nearest training samples by
Euclidean distance and predict the majority class among them. No training phase —
the model IS the data. Prediction is expensive (O(n) per point) but the model is
simple, non-linear, and often surprisingly effective.

WHEN TO USE: Non-linear decision boundaries, small to medium datasets, quick
prototypes. KNN is the first thing to try when you have no idea what your data
looks like — if KNN works, there's signal; if it doesn't, the features probably
need work.

GUARANTEES: On two well-separated Gaussian clusters (centers 5 units apart, σ=1),
k=5 achieves >80% test accuracy. The majority vote is deterministic for a given
training set.

NOT: A production KNN. No distance weighting, no feature scaling, no efficient
index (brute-force O(n) per prediction). Assumes all features are on the same
scale — if one feature dominates, accuracy drops.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
