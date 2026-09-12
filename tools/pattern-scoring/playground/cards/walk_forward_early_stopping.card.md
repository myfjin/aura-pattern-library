# CARD: walk_forward_early_stopping  (batch 2 — compact format)
FILE: python/data-science/composed_tools/walk_forward_early_stopping.py
BASELINE (verified 2026-07-19): train MAE …/ forward MAE …/ PASS (3 lines)
ENTRY: fit_stump_to_residuals(X, r) · demo starts line 57

PASTE-ATTACKS — one at a time, just above the file's final print (~line 113);
run · read against the three-way rule · git checkout pristine -- <file> · next.
1. `    print(fit_stump_to_residuals([(1.0, 2.0)], []))`
   X/r length mismatch — E007 class
2. `    print(fit_stump_to_residuals([], []))`
   both empty — B8

FREE-PLAY: after the paste-attacks, 1-2 shots of YOUR OWN — your garbage, not mine.
Remember: attacks on initializers that later code overwrites never land (no-op) —
attack function calls or post-generation data.
