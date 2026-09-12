"""
t-Digest (Merging Variant) — accurate tail quantiles (p99, p01) in bounded memory.

WHAT IT DOES: Merges sorted points into centroids under a q-dependent size bound:
limit(q) = 4·N·δ·q·(1−q). Near the tails the bound shrinks to ~0, so tail centroids
stay tiny (near-exact) while mid-distribution centroids may grow large.

WHEN TO USE: You need accurate tail quantiles from a large stream — latency monitoring,
SLA tracking, any "how bad are the worst cases?" question.

GUARANTEES: Tail quantiles within ~0.1σ of true. Compresses 20,000 points into ~200
centroids. Tail centroids are smaller than mid centroids (tail-scaling property).

NOT: A streaming algorithm. Requires sorting the full stream. Does not support
incremental updates.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"