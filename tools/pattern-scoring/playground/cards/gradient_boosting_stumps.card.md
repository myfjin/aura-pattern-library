# CARD: gradient_boosting_stumps  (batch 2 — compact format)
FILE: python/data-science/ensembles_and_robust_methods/gradient_boosting_stumps.py
BASELINE (verified 2026-07-19): gradient_boosting_stumps: single_stump_mse=0.3244, boosted_mse=0.0396 PASS
ENTRY: gini_split(y) / the boosting fit in demo · demo starts line 125

PASTE-ATTACKS — one at a time, just above the file's final print (~line 162);
run · read against the three-way rule · git checkout pristine -- <file> · next.
1. `    print(gini_split([]))`
   empty labels — B8
2. `    print(gini_split([float("nan"), 1.0]))`
   NaN label — E008 class: silent gini number = INVALID
3. FREE-PLAY: poison the demo's y after generation (like stacking) — does boosting train on NaN silently?

FREE-PLAY: after the paste-attacks, 1-2 shots of YOUR OWN — your garbage, not mine.
Remember: attacks on initializers that later code overwrites never land (no-op) —
attack function calls or post-generation data.
