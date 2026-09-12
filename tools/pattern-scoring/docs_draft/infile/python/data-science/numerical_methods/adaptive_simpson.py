"""
Adaptive Simpson's Rule — automatic step refinement via error estimation.

WHAT IT DOES: Compares Simpson on [a,b] with two estimates on [a,c] and [c,b]. Recursively
refines where error exceeds tolerance. O(h⁴) accuracy with fewer evals than fixed-step.

WHEN TO USE: Numerical integration where integrand varies in smoothness.

GUARANTEES: ∫₀^π sin(x) dx = 2 to within 1e-7. Depth limit 50 prevents infinite recursion.

NOT: A fixed-step method. Adaptive refinement may be slower for very smooth integrands.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"