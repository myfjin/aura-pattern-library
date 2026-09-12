"""
NDCG (Normalized Discounted Cumulative Gain) — evaluate ranking quality with graded
relevance.

WHAT IT DOES: DCG = Σ rel[i] / log₂(i+2). NDCG = DCG(predicted) / DCG(ideal). Perfect
ranking = NDCG 1.0. Degraded ranking scores much lower.

WHEN TO USE: Evaluating ranked lists where items have graded relevance.

GUARANTEES: Perfect NDCG = 1.0. Degraded NDCG < 0.5. Perfect >> degraded (> 2×).

NOT: A binary-relevance metric. Use MRR/Precision@K for binary judgments.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"