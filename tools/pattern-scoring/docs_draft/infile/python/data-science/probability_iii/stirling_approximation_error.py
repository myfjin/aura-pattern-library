"""
Stirling's Approximation Error — approximate log(n!) without computing factorial.

WHAT IT DOES: log(n!) ≈ n·log(n) − n + 0.5·log(2πn). Relative error decreases as n
grows. At n=1000, error < 1%. Error at n=10 > n=100 > n=1000 (monotonic decrease).

WHEN TO USE: Computing log-factorials for large n — statistical mechanics, information
theory.

GUARANTEES: Error decreases monotonically with n. At n=1000, rel error < 1%.

NOT: An exact formula. The approximation is asymptotic — error grows for small n.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"