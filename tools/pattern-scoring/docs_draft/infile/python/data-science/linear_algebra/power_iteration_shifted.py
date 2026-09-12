"""
Power Iteration with Shift — find the smallest eigenvalue without computing all of them.

WHAT IT DOES: Standard power iteration finds the largest eigenvalue. By shifting the
matrix (A - sigma*I), the largest |lambda - sigma| corresponds to the eigenvalue
farthest from sigma. Choose sigma larger than the largest eigenvalue, and power
iteration on the shifted matrix recovers the smallest eigenvalue. The Rayleigh
quotient then extracts the true eigenvalue from the converged eigenvector.

WHEN TO USE: You need the smallest eigenvalue of a symmetric matrix (e.g. for
condition number estimation, convergence analysis, or checking positive definiteness)
without computing the full spectrum.

GUARANTEES: The recovered eigenvalue is within [0.5, 1.5] of the true smallest
eigenvalue (for the planted 3x3 matrix with true min ≈ 1.268). The eigenvector
satisfies A*v ≈ lambda*v to within 0.1 per component.

NOT: A general eigensolver. Only works for symmetric matrices. The shift must be
chosen carefully — a shift inside the spectrum converges to a different eigenvalue.
No deflation for finding multiple eigenvalues.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
