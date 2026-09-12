"""
Romberg Integration — Richardson extrapolation on trapezoid rule.

WHAT IT DOES: Generates table of refined trapezoid estimates, extrapolates to O(h⁴).
∫₀^π sin(x) dx = 2 to within 1e-6 with n=5 rows. Uses 4^j extrapolation factor.

WHEN TO USE: High-accuracy numerical integration with automatic order improvement.

GUARANTEES: ∫₀^π sin(x) dx = 2 within 1e-6 with n=5.

NOT: An adaptive method. Uses fixed refinement pattern regardless of integrand behavior.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"