"""
Gradient Descent with Momentum — stop oscillating and converge faster.

WHAT IT DOES: Vanilla gradient descent zigzags in narrow valleys — it takes tiny
steps in the steep direction and wastes iterations. Momentum accumulates velocity
across iterations: if the gradient keeps pointing the same direction, momentum
accelerates; if it reverses (oscillation), momentum smooths it out. On a 2D quadratic
bowl with one steep axis (100x steeper), momentum converges in fewer iterations than
vanilla GD.

WHEN TO USE: Convex optimization with non-isotropic (elongated) loss landscapes.
Standard in neural network training to accelerate convergence and reduce oscillation.

GUARANTEES: Both vanilla GD and momentum GD converge to function value < 1e-6.
Momentum GD converges in fewer iterations than vanilla GD. Both start from the same
initial point for fair comparison.

NOT: A general optimization library. Only demonstrates the concept on a simple 2D
quadratic. Does not implement Nesterov momentum, adaptive learning rates (Adam, RMSprop),
or line search. The momentum value (0.9) is fixed and may not be optimal for all problems.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
