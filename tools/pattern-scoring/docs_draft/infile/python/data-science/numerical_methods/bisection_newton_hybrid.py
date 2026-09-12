"""
Hybrid Bisection-Newton Root-Finding — bisection's guarantee + Newton's speed.

WHAT IT DOES: Uses Newton when step stays in bracket and is small; reverts to bisection
otherwise. Root of x² − x − 6 = 0 found at x ≈ 3.0 to within 1e-6.

WHEN TO USE: Root-finding wanting Newton's speed with bisection's robustness.

GUARANTEES: Root within 1e-6 of true. f(root) < 1e-8. Falls back to bisection on drift.

NOT: A pure Newton method. Requires f(a)·f(b) < 0 (sign change bracket).
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"