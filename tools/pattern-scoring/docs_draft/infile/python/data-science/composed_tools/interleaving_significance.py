"""
Interleaving Significance — the duel names a winner; the bootstrap says if it's real.

WHAT IT DOES: Collects interleaving's per-query paired preference and feeds it to the
paired bootstrap: a confidence interval on the mean preference. A genuine ranker edge
gives a CI that excludes zero; two equal rankers give a CI that straddles zero.

WHEN TO USE: You need to compare two ranking systems with statistical confidence,
especially when the better system wins fewer queries but by larger margins.

GUARANTEES: Real edge → CI excludes zero. Null case → CI straddles zero (no false
positive). Raw win-count can mislead (under half).

NOT: A split A/B test. Interleaving is more sensitive but needs the bootstrap for
calibrated confidence.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"