"""
Greenwald-Khanna ε-Approximate Quantile Summary — estimate any quantile of a stream
with bounded error using far less memory than storing all values.

WHAT IT DOES: Maintains a sorted list of (value, g, delta) tuples where g is a lower
bound on rank and delta is the maximum error. When the summary grows too large, it
compresses by selectively dropping entries while preserving the ε-error guarantee.

WHEN TO USE: You need approximate quantiles (median, quartiles, percentiles) on a large
stream where storing all values is impractical — latency monitoring, sensor data.

GUARANTEES: Estimated quantile within 2·ε·n of the true quantile (in rank space).

NOT: A production-grade GK implementation. Uses a simplified compression strategy
(every-other) rather than the full GK merge algorithm.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"