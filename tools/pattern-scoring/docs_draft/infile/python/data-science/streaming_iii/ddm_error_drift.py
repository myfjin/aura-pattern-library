"""
DDM — Drift Detection Method — detect when a classifier's error rate has significantly
worsened, online.

WHAT IT DOES: Tracks the running error rate p_i and its standard deviation s_i as each
prediction arrives. Keeps the minimum of (p_i + s_i) ever seen (the model's best
performance). Signals DRIFT at p_i + s_i ≥ p_min + 3·s_min — a statistical control
chart, not "later > earlier."

WHEN TO USE: You're running a classifier on a stream and need to know when its accuracy
has degraded enough to warrant retraining.

GUARANTEES: No false alarms on stationary error streams. Detects real error increases
within ~30 samples of the change point.

NOT: A warning-level detector (2-sigma). Only signals at the 3-sigma DRIFT level.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"