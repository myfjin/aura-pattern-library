"""
Inclusion-Exclusion: Derangements — count permutations with no fixed points.

WHAT IT DOES: !n = n! · Σ (−1)^k / k! ≈ n! / e. For n=10, !10/10! ≈ 0.368 = 1/e.
Simulation matches exact proportion within 5%.

WHEN TO USE: Secret santa, password resets, any "nothing stays in place" problem.

GUARANTEES: !n/n! → 1/e as n → ∞. Simulation matches exact within 5%.

NOT: A general inclusion-exclusion demo. Only covers derangements (no fixed points).
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"