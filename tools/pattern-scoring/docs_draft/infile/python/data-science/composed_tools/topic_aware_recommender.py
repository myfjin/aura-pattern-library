"""
Topic-Aware Recommender — a 4-pattern workflow that recommends documents by topic,
not just word overlap.

WHAT IT DOES: (1) PMI-weighted term co-occurrence graph; (2) weighted label
propagation communities; (3) within-community PageRank for signature terms;
(4) recommend by topic-vector cosine. Flat term-overlap mixes topics when shared
vocabulary dominates; the pipeline stays within-topic.

WHEN TO USE: You need recommendations that respect topic structure, especially when
documents share a large common vocabulary across topics.

GUARANTEES: Each topic's core terms form one distinct community (3 topics → 3
communities). Topic-aware rate > 80% same-topic. Beats flat overlap by > 15%.

NOT: A general recommender. Requires a text corpus with distinct topic structure.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"