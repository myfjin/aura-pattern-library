"""
Weighted Reservoir Sampling — A-Res (Efraimidis-Spirakis) — sample k items proportional
to weight in one pass.

WHAT IT DOES: Gives each item a key u^(1/weight) with u ~ Uniform(0,1) and keeps the k
items with the largest keys in a min-heap. P(item in sample) grows with its weight.

WHEN TO USE: You need a weighted random sample from a stream where items have different
importance — survey sampling, weighted A/B test monitoring.

GUARANTEES: For k=1, P(item i is picked) = w_i / sum(w) (verified empirically). Selection
frequency is monotone in weight. One pass, O(k) memory.

NOT: Sampling with replacement. Does not support negative or zero weights (skipped).
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"