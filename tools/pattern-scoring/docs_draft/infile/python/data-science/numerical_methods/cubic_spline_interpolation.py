"""
Natural Cubic Spline — piecewise cubic interpolation with C² continuity.

WHAT IT DOES: Solves tridiagonal system for interior second derivatives. Natural boundary
(zero second derivative at endpoints). sin(x) with 5 knots interpolated to error < 0.05.

WHEN TO USE: Smooth interpolation needing continuous first and second derivatives.

GUARANTEES: Interpolation error < 0.05 on sin(x) with 5 knots. C² continuity.

NOT: An extrapolation method. No guarantees outside data range.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"