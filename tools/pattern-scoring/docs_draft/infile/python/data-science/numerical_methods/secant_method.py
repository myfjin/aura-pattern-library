"""
Secant Method — Newton's speed without derivatives.

WHAT IT DOES: Finite-difference slope from two prior points. Root of x³ − 2 = 0 at
∛2 ≈ 1.2599 within 1e-4. f(root) < 1e-8. Superlinear convergence (order ≈ 1.618).

WHEN TO USE: Root-finding when derivative is expensive or unavailable.

GUARANTEES: Root within 1e-4 of true. f(root) < 1e-8.

NOT: Guaranteed to converge. May fail if f(x0) ≈ f(x1) (near-zero denominator).
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"