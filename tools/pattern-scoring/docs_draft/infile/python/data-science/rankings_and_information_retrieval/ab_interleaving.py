"""
Team-Draft Interleaving for A/B Testing Rankers — compare two rankers by interleaving
their results in a single ranking.

WHAT IT DOES: Alternately picks the next unchosen document from A or B. Simulates user
clicks on the interleaved ranking. The ranker whose document the user clicked on wins
that "team." Stronger ranker wins more clicks.

WHEN TO USE: You need to compare two ranking systems with a more sensitive test than
splitting traffic.

GUARANTEES: Stronger ranker A wins more than B. A's win ratio > 0.5.

NOT: A significance test. Does not provide confidence intervals — use with paired
bootstrap for statistical inference.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"