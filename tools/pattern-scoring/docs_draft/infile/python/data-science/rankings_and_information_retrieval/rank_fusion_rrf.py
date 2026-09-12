"""
Reciprocal Rank Fusion (RRF) — combine multiple rankers via RRF scoring.

WHAT IT DOES: RRF score = Σ 1/(k + rank_i) across all rankings. Fused ranking beats
both individual rankers in NDCG. Robust to individual ranker weaknesses.

WHEN TO USE: Combining results from multiple search systems or ranking methods.

GUARANTEES: Fused NDCG beats both individual rankers. Fused beats average individual
score.

NOT: A weighted fusion method. All rankers have equal weight in RRF.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"