"""
Broker-Term Extraction — find the words that sit between topic clusters using
betweenness centrality on a co-occurrence graph.

WHAT IT DOES: Builds a co-occurrence graph from adjacent-pair windows (not all-pairs,
which would bypass the broker). Computes betweenness centrality via Brandes' algorithm.
Broker words dominate betweenness but are mid-to-low in frequency — invisible to
frequency-based methods.

WHEN TO USE: You need the vocabulary that bridges domains — cross-domain search,
knowledge graph construction.

GUARANTEES: The broker word tops betweenness with a clear margin (> 2× runner-up).
The broker is NOT findable by frequency (rank ≥ 5).

NOT: A hub-finder. TextRank finds high-degree words within topics; this finds
between-topic bridges.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"