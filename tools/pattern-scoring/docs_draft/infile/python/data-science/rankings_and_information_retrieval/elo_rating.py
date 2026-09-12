"""
Elo Rating System — maintain skill ratings via pairwise wins/losses.

WHAT IT DOES: Elo(new) = Elo(old) + K × (observed − expected). Expected = 1 / (1 +
10^((opponent_elo − my_elo)/400)). Stronger player's Elo converges higher after enough
matches. A 100-point advantage gives ~64% expected score.

WHEN TO USE: Rating players or items from pairwise comparisons — chess, gaming.

GUARANTEES: Stronger player (55% win rate) has higher Elo after 100 matches. Expected
score formula matches hand-computed values.

NOT: A Bayesian rating system. Does not model uncertainty in ratings (use Glicko for
that).
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"