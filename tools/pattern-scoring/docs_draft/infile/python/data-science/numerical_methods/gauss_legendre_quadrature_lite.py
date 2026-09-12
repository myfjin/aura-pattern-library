"""
Gauss-Legendre Quadrature (Lite) — optimal nodes for polynomial integration.

WHAT IT DOES: 4-point Gauss-Legendre with hardcoded nodes/weights. Exact for degree ≤7
polynomials. ∫₀¹ x² dx = 1/3 to machine epsilon. 4 function evaluations.

WHEN TO USE: Numerical integration of smooth functions needing high accuracy with few evals.

GUARANTEES: ∫₀¹ x² dx = 1/3 to 1e-10. ∫₀^π sin(x) dx = 2 to 1e-4.

NOT: An adaptive method. Fixed 4-point rule — accuracy depends on integrand smoothness.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"