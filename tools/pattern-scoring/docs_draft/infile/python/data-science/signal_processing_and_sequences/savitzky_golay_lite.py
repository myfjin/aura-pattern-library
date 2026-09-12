"""
Savitzky-Golay Filter — smooth your signal without destroying the peaks.

WHAT IT DOES: Moving averages blur sharp features. The Savitzky-Golay filter fits a
low-order polynomial (e.g. quadratic) to a rolling window — it smooths noise while
preserving peak heights and widths much better than a moving average. This pattern
demonstrates the difference: SG preserves a smooth Gaussian peak while the moving
average visibly clips it.

WHEN TO USE: You have a noisy signal with smooth, band-limited peaks that you want
to preserve. Common in spectroscopy, chromatography, and any domain where peak shape
carries information.

GUARANTEES: SG filtered peak error < 0.9 (preserves smooth peak to within ~11% of
height). MA filtered peak error > 1.1 (visibly clips the peak). SG error < 70% of
MA error (SG clearly beats MA).

NOT: A general signal processing library. Only implements quadratic polynomial fit
(not configurable order). Does not handle edge effects optimally. The peak-preservation
claim applies to smooth band-limited peaks, not single-sample spikes (which are
outliers, not signal).
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
