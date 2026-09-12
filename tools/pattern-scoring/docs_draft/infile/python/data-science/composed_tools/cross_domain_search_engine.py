"""
Cross-Domain Search Engine — a 4-pattern workflow that retrieves cross-domain bridge
documents a plain BM25 search leaves buried.

WHAT IT DOES: (1) Stem vocabulary; (2) extract broker terms from co-occurrence graph;
(3) expand query with broker terms; (4) BM25-rank. A domain-A query surfaces bridge
documents that plain BM25 misses.

WHEN TO USE: You need a search engine that finds documents connecting fields.

GUARANTEES: Stage 2 recovers actual broker terms. Plain BM25 stays in-domain (≤1
bridge doc in top-6). Pipeline surfaces ≥3 bridge docs in top-6.

NOT: A general search engine. Only useful for cross-domain retrieval in multi-topic
corpora.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"