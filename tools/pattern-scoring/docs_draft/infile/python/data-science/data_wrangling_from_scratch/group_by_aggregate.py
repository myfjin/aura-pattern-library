"""
Group-By Aggregation (Multi-Key) — split your data into groups, then summarize each.

WHAT IT DOES: The SQL GROUP BY or pandas groupby() — implemented from scratch.
Group records by one or more keys (e.g. category + region), then aggregate a value
column (sum, mean, count, min, max). Verified against a brute-force nested-loop
computation on the same data.

WHEN TO USE: You need to understand how group-by aggregation works under the hood,
or you're in a constrained environment where pandas/SQL aren't available. Every
data analysis starts with group-by — this is the minimal honest version.

GUARANTEES: All five aggregation functions (sum, mean, count, min, max) produce
identical results to a brute-force nested-loop verifier. Multi-key grouping works
correctly (e.g. category + region). Single-key grouping also works.

NOT: A production group-by engine. No handling of null values, no multi-value
aggregation, no sorting of results. The brute-force verifier is O(n²) — for
teaching, not performance.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
