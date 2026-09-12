"""
HMM Baum-Welch (EM) Training — learn emission and transition probabilities.

WHAT IT DOES: E-step computes forward-backward statistics (scaled to avoid underflow).
M-step re-estimates parameters. Likelihood increases monotonically. Perturbed init breaks
symmetry. Multiple restarts for best likelihood.

WHEN TO USE: Sequence tagging, time-series classification, learning from unlabeled sequences.

GUARANTEES: Stochastic matrices (rows sum to 1). Likelihood never decreases. Emission error
< 0.15, transition error < 0.20.

NOT: A fully general HMM. Discrete observations only. No support for continuous emissions.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"