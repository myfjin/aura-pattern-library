# CARD: stacking_ensemble.py
FILE: python/data-science/ensembles_and_robust_methods/stacking_ensemble.py
CLAIM: stacked ensemble — two base learners + linear meta-model beats/equals bases on held-out data.

VALID OUTPUT (baseline, exit 0):
  stacking_ensemble: base1_acc=0.9667, base2_acc=1.0000, stack_acc=1.0000 PASS

FAILURE SIGNATURE: AssertionError or ValueError/TypeError traceback; exit != 0.

ATTACKS (demo starts line 118; find the data-building lines just after):
1. In the demo, make X and y different lengths (delete one y element / slice y[:-1]).
   CONTRACT: length mismatch must be rejected. Error ✅ · silent accuracy number ❌
2. Replace one y label with a string: `"один"`. Error ✅ · silent PASS ❌
3. Replace one X row value with float('nan'). Honest: error/NaN-guard ✅ ·
   confident accuracy with NaN inside ❌ (NaN poisons silently — classic fake-robust)
