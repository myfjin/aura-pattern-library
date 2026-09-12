"""
TF-IDF Vectorizer — turn text into numbers that capture what matters.

WHAT IT DOES: TF-IDF weights each word by how often it appears in a document (TF)
divided by how many documents contain it (IDF). Common words like "the" get low
weight; rare, distinctive words get high weight. This is the standard baseline for
document ranking, similarity search, and text classification.

WHEN TO USE: Ranking documents by relevance to a query, finding similar documents,
or preparing text for ML classifiers where term importance matters. TF-IDF is the
first thing to try before moving to neural embeddings.

GUARANTEES: Common words have lower IDF than rare words. Documents with shared
distinctive terms have higher cosine similarity. Query ranking correctly identifies
relevant documents.

NOT: A production NLP pipeline. Uses simple regex tokenization (no stemming, no
stop-word removal, no n-grams). Does not handle out-of-vocabulary words. The dense
vector representation is memory-inefficient for large vocabularies.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
