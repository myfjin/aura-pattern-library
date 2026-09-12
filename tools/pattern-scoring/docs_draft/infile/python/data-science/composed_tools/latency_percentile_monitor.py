"""
Latency Percentile Monitor — p99 tracking in five floats per quantile.

WHAT IT DOES: Welds the P² five-marker streaming quantile estimator into a per-service
aggregator. Tracks p50 and p99 in O(1) memory. A tail-only regression (5% of requests
slow 10×) is invisible at p50 but loud at p99.

WHEN TO USE: Service latency monitoring where the tail IS the product.

GUARANTEES: Streaming p99 tracks exact p99 within 15% relative error. Tail regression
invisible at p50 (<25% shift) but >2× at p99. O(1) memory — five markers per quantile.

NOT: A batch quantile estimator. The P² estimator needs warm-up (~5 samples) before
producing reliable estimates.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"