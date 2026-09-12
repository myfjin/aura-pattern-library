# CARD: dirichlet_stick_breaking  (batch 2 — compact format)
FILE: python/data-science/bayesian_iii_modeling_and_selection/dirichlet_stick_breaking.py
BASELINE (verified 2026-07-19): PASS
ENTRY: stick_breaking_process(alpha, num_breaks) · demo starts line 37

PASTE-ATTACKS — one at a time, just above the file's final print (~line 62);
run · read against the three-way rule · git checkout pristine -- <file> · next.
1. `    print(stick_breaking_process(-1.0, 5))`
   negative concentration alpha — Beta(1,-1) is meaningless (bayesian-kill class)
2. `    print(stick_breaking_process(1.0, 0))`
   zero breaks — B8. Empty result OK if contract says so · fabricated weights = INVALID

FREE-PLAY: after the paste-attacks, 1-2 shots of YOUR OWN — your garbage, not mine.
Remember: attacks on initializers that later code overwrites never land (no-op) —
attack function calls or post-generation data.
