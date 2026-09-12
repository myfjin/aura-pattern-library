"""
Richardson Extrapolation — boost convergence order via linear combination.

WHAT IT DOES: (2^p·F(h/2) − F(h))/(2^p − 1) cancels leading error term C·h^p. Raises
O(h²) midpoint rule to O(h⁴). Error after < 1e-10. Factor is 2^p, not p.

WHEN TO USE: Improving accuracy without changing the underlying method.

GUARANTEES: Error after < error before. Error after < 1e-10 for cubic integrand.

NOT: A standalone integration method. Requires a base method with known error order.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"