"""
Community Local Authority — find who matters inside each community, not just in the
global ranking.

WHAT IT DOES: Detects communities via label propagation, then ranks WITHIN each
induced subgraph via PageRank. The village mayor is invisible globally (rank ≥ 5)
but crowned locally.

WHEN TO USE: You need the important nodes in each community, especially when
communities are of very different sizes.

GUARANTEES: Two communities found. Village core stays intact. Village mayor invisible
globally (rank ≥ 5) but crowned locally. Empire hub still wins its own community.

NOT: A global ranking method. The composition recovers local authority that global
PageRank buries.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"