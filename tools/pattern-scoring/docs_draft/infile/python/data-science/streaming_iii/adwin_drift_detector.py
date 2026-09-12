"""
ADWIN0 Adaptive Windowing Drift Detector — detect distribution shift online with a
provable false-alarm guarantee.

WHAT IT DOES: Keeps a window of recent values. After each arrival, tries every split
of the window into older and newer parts. If |mean(old) − mean(new)| exceeds a
variance-aware Hoeffding bound, a real change is declared and the older part is dropped.
delta controls the false-positive rate.

WHEN TO USE: You need to detect distribution shift online — classifier error rate
monitoring, sensor drift detection, any stream where you need to know "did the process
change?" with a statistical guarantee.

GUARANTEES: False-alarm rate ≤ delta on stationary streams. Detection within one window
of a real shift. Values must be in [0,1] (e.g., classification errors).

NOT: A fixed-window detector. The window grows and shrinks adaptively. Uses stride
sampling (n//32) for efficiency rather than checking every split.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"