"""
Birthday Paradox — exact vs simulated collision probability.

WHAT IT DOES: P(≥2 same birthday in n people) ≈ 1 − n!/(365^n · (365−n)!). For n=23,
P ≈ 50%. Exact formula matches simulation within 10%.

WHEN TO USE: Understanding collision probability — hash collisions, random sampling.

GUARANTEES: n=23 gives P ≈ 50%. Exact matches simulation. For n > days, P = 1.0.

NOT: An approximation. Uses exact formula, not the exponential approximation.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"