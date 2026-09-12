"""
KD-Tree Accelerated k-NN — the search engine meets the classifier.

WHAT IT DOES: Builds a kd-tree from training points. Queries use best-first descent
with pruning: a subtree is skipped when its splitting plane is farther than the current
k-th best distance. Identical predictions to brute force, fraction of the distance
computations.

WHEN TO USE: kNN on low-dimensional data where query volume makes brute force expensive.

GUARANTEES: Identical predictions to brute force (100% agreement). Distance computations
cut by >60%. O(log n) average query time.

NOT: Suitable for high-dimensional data (curse of dimensionality degrades kd-tree to
brute force).
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"