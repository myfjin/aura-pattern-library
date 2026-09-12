# CARD: bayes_factor_normal_means  (batch 2 — compact format)
FILE: python/data-science/bayesian_iii_approximate_inference/bayes_factor_normal_means.py
BASELINE (verified 2026-07-19): PASS (silent-style: one word)
ENTRY: bayes_factor_normal(data, prior_var_h1) · demo starts line 33

PASTE-ATTACKS — one at a time, just above the file's final print (~line 53);
run · read against the three-way rule · git checkout pristine -- <file> · next.
1. `    print(bayes_factor_normal([], 1.0))`
   empty data — B8. Error/explicit reject = OK · confident BF number = INVALID
2. `    print(bayes_factor_normal([float("nan"), 1.0, 2.0], 1.0))`
   NaN in data — B4 (today's E008 class). Watch for a silent confident Bayes factor
3. `    print(bayes_factor_normal([1.0, 2.0, 3.0], -1.0))`
   negative prior VARIANCE — impossible (E004 class)

FREE-PLAY: after the paste-attacks, 1-2 shots of YOUR OWN — your garbage, not mine.
Remember: attacks on initializers that later code overwrites never land (no-op) —
attack function calls or post-generation data.
