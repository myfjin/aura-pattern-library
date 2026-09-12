"""
Pólya Urn Reinforcement — rich-get-richer feedback with random Beta limit.

WHAT IT DOES: Start with a balls of A, b of B. Each draw: pick a ball, return it plus
one more of same color. Limiting proportion is RANDOM ~ Beta(a,b). Across many urns,
mean matches a/(a+b) and variance matches Beta variance. The urn SPREADS — it does not
concentrate at the mean.

WHEN TO USE: Understanding reinforcement processes — preferential attachment, word
frequency evolution.

GUARANTEES: Mean matches Beta mean a/(a+b) within 0.03. Variance matches Beta variance
within 0.005. Variance > 0.01 (spreads, not concentrates).

NOT: A deterministic limit. Each urn converges to a different random limit.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"