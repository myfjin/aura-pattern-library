# CARD: log_rank_test  (batch 2 — compact format)
FILE: python/data-science/survival_and_reliability/log_rank_test.py
BASELINE (verified 2026-07-19): PASS (one word)
ENTRY: log_rank_test(times_g1, events_g1, times_g2, events_g2) · demo starts line 58

PASTE-ATTACKS — one at a time, just above the file's final print (~line 83);
run · read against the three-way rule · git checkout pristine -- <file> · next.
1. `    print(log_rank_test([1.0, 2.0], [1], [3.0], [1]))`
   times/events length mismatch — E007 class
2. `    print(log_rank_test([1.0], [5], [2.0], [1]))`
   event indicator 5 — events must be 0/1 (E007 label-domain)
3. `    print(log_rank_test([-1.0], [1], [2.0], [1]))`
   negative survival time — B5: time cannot be negative

FREE-PLAY: after the paste-attacks, 1-2 shots of YOUR OWN — your garbage, not mine.
Remember: attacks on initializers that later code overwrites never land (no-op) —
attack function calls or post-generation data.
