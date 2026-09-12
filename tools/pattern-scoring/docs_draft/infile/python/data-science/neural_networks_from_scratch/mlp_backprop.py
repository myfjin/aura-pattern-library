"""
2-Layer MLP with Backpropagation — how does backprop actually work?

WHAT IT DOES: A 2-layer MLP (2 -> 4 -> 1) with sigmoid activations, trained by
hand-derived backpropagation on the XOR problem. The forward pass computes predictions,
the backward pass applies the chain rule through the sigmoid derivative, and weight
updates minimize the loss. XOR is the classic test: a single layer can't solve it
(not linearly separable), but a hidden layer can.

WHEN TO USE: Understanding backpropagation mechanics, debugging autodiff systems,
verifying network training fundamentals. This is the teaching version — every
gradient is explicit, nothing is hidden behind a framework.

GUARANTEES: Final loss < 0.01 after 500 epochs on XOR. Each of the 4 XOR cases has
prediction error < 0.2. The network correctly learns the non-linear decision boundary.

NOT: A production neural network. No batching, no momentum, no regularization, no
adaptive learning rates. Only works for 2-layer MLPs with sigmoid activation. The
learning rate (1.0) is aggressive and may not generalize to other problems.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
