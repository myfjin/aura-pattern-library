"""
Pseudo-Relevance Feedback (PRF) for Query Expansion — expand a query with terms from
top-k retrieved docs.

WHAT IT DOES: Retrieves top-k docs with initial query, extracts most frequent terms
(excluding query terms), appends them to the query. Raw query "dog" misses "canine"
docs; expanded query finds them.

WHEN TO USE: Improving recall in search — finding relevant docs that use different
vocabulary.

GUARANTEES: Expanded query includes synonym terms. Previously missed docs are retrieved.

NOT: A relevance feedback method requiring user interaction. PRF assumes top-k docs
are relevant (pseudo-relevance).
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"