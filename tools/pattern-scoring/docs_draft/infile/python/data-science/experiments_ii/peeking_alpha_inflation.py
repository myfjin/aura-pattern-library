"""
Peeking Alpha Inflation — the silent p-value cheat.

WHAT IT DOES: You run an A/B test, peek at the p-value halfway through, see it's not
significant yet, so you keep collecting data and test again. This "peeking" inflates
your type-I error rate from the nominal 5% to 20-30% — you're much more likely to
declare a false positive. This pattern demonstrates the inflation by comparing fixed-n
testing (no peeking) against a peeking strategy under the null hypothesis.

WHEN TO USE: Any time you run experiments and are tempted to check results early.
The rule: if you peek, you must adjust your stopping rule (sequential testing, alpha
spending). This pattern shows you exactly how much damage peeking does.

GUARANTEES: Fixed-n type-I error < 12% (near nominal 5%). Peeking type-I error >
2× the fixed-n rate. The inflation is measurable over 2000 Monte Carlo replications.

NOT: A sequential testing solution. Only demonstrates the problem — does not implement
correct sequential methods (e.g. alpha spending, group sequential design).
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
