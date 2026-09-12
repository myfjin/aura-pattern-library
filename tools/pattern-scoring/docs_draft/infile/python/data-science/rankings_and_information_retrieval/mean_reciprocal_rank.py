"""
Ranking Metrics Suite: MRR, Precision@K, Recall@K — evaluate ranking quality.

WHAT IT DOES: MRR = mean over queries of 1/(rank of first relevant). P@K = |relevant
∩ top-K| / K. R@K = |relevant ∩ top-K| / |relevant|. Each returns exact known values
on planted rankings. MRR falls monotonically as first relevant is demoted.

WHEN TO USE: Evaluating search and ranking systems.

GUARANTEES: RR = 1/rank of first relevant. P@K and R@K match hand-computed values.
MRR monotone in relevance position.

NOT: A graded-relevance metric. Use NDCG for graded relevance judgments.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"