"""
Cross-Domain Query Expansion — expand a query with broker terms to surface
cross-domain documents instead of deeper monoculture.

WHAT IT DOES: Classic PRF expands with top-document terms (more of the same domain).
Broker expansion expands with the corpus's top broker terms (words on shortest paths
between topic clusters). A finance query expanded with broker terms surfaces bridge
documents between finance and biology.

WHEN TO USE: You need cross-domain discovery — finding documents that bridge fields.

GUARANTEES: Broker expansion picks actual broker terms. Classic PRF stays in its
monoculture (≤1 bridge doc in top-5). Broker expansion surfaces ≥2 bridge docs.

NOT: A general-purpose query expansion. Only useful when the corpus spans multiple
domains with bridge documents.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"