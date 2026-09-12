"""
Pairwise Ranking via Logistic Regression — learn item ordering from pairwise
comparisons.

WHAT IT DOES: For each pair (i,j), fits logistic regression on feature difference
(f_i − f_j) to predict which ranks higher. Recovers planted order with high Kendall
tau correlation.

WHEN TO USE: Learning to rank from pairwise preference data.

GUARANTEES: Kendall tau > 0.7 vs true order. Recovers exact or near-exact order.

NOT: A pointwise or listwise ranking method. Only uses pairwise comparisons.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"