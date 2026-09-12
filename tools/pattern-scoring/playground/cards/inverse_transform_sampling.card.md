# CARD: inverse_transform_sampling  (batch 2 — compact format)
FILE: python/data-science/information_theory_and_probability/inverse_transform_sampling.py
BASELINE (verified 2026-07-19): …all assertions PASS (one line)
ENTRY: exponential_inverse_cdf(u, rate) · demo starts line 73

PASTE-ATTACKS — one at a time, just above the file's final print (~line 144);
run · read against the three-way rule · git checkout pristine -- <file> · next.
1. `    print(exponential_inverse_cdf(1.5, 2.0))`
   u=1.5 outside [0,1) — E003 class (probability domain)
2. `    print(exponential_inverse_cdf(0.5, -2.0))`
   negative rate — E001 class
3. `    print(exponential_inverse_cdf(1.0, 2.0))`
   u exactly 1.0 — log(0) boundary: honest error or inf?

FREE-PLAY: after the paste-attacks, 1-2 shots of YOUR OWN — your garbage, not mine.
Remember: attacks on initializers that later code overwrites never land (no-op) —
attack function calls or post-generation data.
