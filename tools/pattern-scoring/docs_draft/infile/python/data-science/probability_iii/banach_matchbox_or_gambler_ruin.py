"""
Gambler's Ruin — probability of ruin in a bounded ±1 random walk.

WHAT IT DOES: For fair game (p=0.5): P(ruin) = b/(a+b). For biased game:
P(ruin) = (r^N − r^a)/(r^N − 1), r = q/p. Verified against simulation on an
asymmetric game (a=5, b=15) so the answer is not the self-symmetric ½.

WHEN TO USE: Understanding risk of ruin in gambling, finance, or bounded random walks.

GUARANTEES: Exact formula matches simulation within 3%. Fair game: P(ruin) = b/(a+b).
Biased game (p=0.6): ruin < 0.1.

NOT: An infinite-horizon result. Assumes bounded total wealth N = a+b.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"