"""
BM25 Ranking (Okapi BM25) — rank documents by relevance with saturation and length
normalization.

WHAT IT DOES: BM25 = Σ IDF · (tf · (k1+1)) / (tf + k1 · (1 − b + b · len/avg_len)).
Ranks shorter relevant doc higher than a longer doc with the same query terms. Naive
TF is confused by length.

WHEN TO USE: Document retrieval where document lengths vary.

GUARANTEES: BM25 ranks shorter relevant doc above longer one with same terms.
Irrelevant doc (no query terms) ranks last.

NOT: A learned ranking model. Uses fixed k1 and b parameters. Does not learn from
user feedback.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"