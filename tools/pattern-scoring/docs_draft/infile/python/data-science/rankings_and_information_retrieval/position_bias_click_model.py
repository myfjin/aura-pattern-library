"""
Position Bias in Click Models and Inverse Propensity Weighting — correct for position
bias in click data.

WHAT IT DOES: Simulates clicks with position bias (position 1 gets more clicks).
Naive click-count ranking is distorted. IPW corrects by dividing each click count by
the position bias factor, recovering the true relevance order.

WHEN TO USE: Analyzing click data from search logs where position bias distorts raw
counts.

GUARANTEES: Naive ranking does NOT rank the most relevant doc first (distorted by
position). IPW recovers true order (A first).

NOT: A full click model. Does not model examination probability separately from
relevance.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"