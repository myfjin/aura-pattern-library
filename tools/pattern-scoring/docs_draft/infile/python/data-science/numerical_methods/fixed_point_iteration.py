"""
Fixed-Point Iteration — find x where g(x) = x.

WHAT IT DOES: Iterates x_{n+1} = g(x_n). Fixed point of cos(x) ≈ 0.7391 recovered.
|g(x) − x| < 1e-7. Linear convergence rate depends on |g'(x*)|.

WHEN TO USE: Solving equations rearranged into fixed-point form.

GUARANTEES: Fixed point within 0.001 of true. |g(x) − x| < 1e-7.

NOT: Guaranteed to converge. Requires |g'(x*)| < 1 (contraction mapping).
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"