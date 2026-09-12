"""
Frugal Streaming Median (Frugal-1) — estimate the median of a stream using a single
integer of state.

WHAT IT DOES: Keeps one estimate m. For each element, with a coin flip gated by the
target quantile q=0.5, steps m up by 1 if the element is above m, down by 1 if below.
At the true quantile, up-pressure and down-pressure balance, so m random-walks to the
median. Starts from 0 (far from the answer) to prove convergence.

WHEN TO USE: You need a quantile estimate on an unbounded stream with O(1) memory —
embedded systems, sensor networks.

GUARANTEES: Converges to within O(step) of the true median. O(1) memory — one float.

NOT: A precise median. The estimate oscillates within a random-walk band. Not suitable
for small streams (< 1000 samples).
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"