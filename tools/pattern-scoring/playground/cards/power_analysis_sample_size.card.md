# CARD: power_analysis_sample_size.py
FILE: python/data-science/statistical_modeling/power_analysis_sample_size.py
CLAIM: computes sample size n for two-proportion test hitting target power; verifies achieved power >= target.

VALID OUTPUT (baseline, exit 0):
  power_analysis_sample_size.py: n_computed=185, achieved_power=0.963, target=0.8 PASS

FAILURE SIGNATURE (what a legit catch looks like): AssertionError with the message text
from line 113 ("Achieved power ... below target ...") or a ValueError/TypeError traceback; exit != 0.

ATTACKS (edit, run, reset):
1. line 104: `p1, p2 = 0.3, 0.5` → `p1, p2 = 1.5, 0.5`   (probability > 1 — impossible)
   CONTRACT: p1 must be in [0,1]. Error ✅ · silent n_computed number ❌
2. line 104: → `p1, p2 = 0.3, "0,5"`   (locale decimal-comma string — your B-class)
   Error (TypeError) ✅ · silent output ❌
3. line 105: `alpha = 0.05` → `alpha = -0.05`   (negative significance)
   Error ✅ · silent PASS ❌
4. line 104: → `p1, p2 = 0.5, 0.5`   (no effect at all — n should explode or reject)
   Honest behaviors: explicit error/huge-n warning ✅ · a small confident n ❌
