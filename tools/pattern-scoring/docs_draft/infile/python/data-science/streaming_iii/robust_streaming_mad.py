"""
Robust Anomaly Detection via Median/MAD — flag outliers using a robust z-score that
isn't corrupted by the outliers themselves.

WHAT IT DOES: Centers on the median and scales by MAD (median absolute deviation × 1.4826
for normal consistency). Flags points with |x−med| / (1.4826·MAD) > k. Median and MAD have
a 50% breakdown point — gross outliers don't corrupt the threshold.

WHEN TO USE: Online outlier flagging with low false-positive rate under heavy contamination
— sensor fault detection, network anomaly detection.

GUARANTEES: Catches all gross outliers (~30σ) with zero false positives at k=3.5 on clean
normal data. 50% breakdown point.

NOT: A streaming algorithm. Processes the full stream at once. Assumes the inlier
distribution is roughly symmetric.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"