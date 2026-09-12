# CARD: savitzky_golay_lite  (batch 2 — compact format)
FILE: python/data-science/signal_processing_and_sequences/savitzky_golay_lite.py
BASELINE (verified 2026-07-19): True peak: 9.25 | SG filtered peak: 9.22 … PASS (one line)
ENTRY: fit_polynomial_window(window, poly_order) · demo starts line 117

PASTE-ATTACKS — one at a time, just above the file's final print (~line 156);
run · read against the three-way rule · git checkout pristine -- <file> · next.
1. `    print(fit_polynomial_window([1.0, 2.0, 3.0], 5))`
   poly_order 5 > window size 3 — underdetermined fit (B5). Silent coefficients = INVALID
2. `    print(fit_polynomial_window([], 2))`
   empty window — B8
3. `    print(fit_polynomial_window([1.0, float("inf"), 3.0], 2))`
   infinity in signal — B4 cousin of NaN

FREE-PLAY: after the paste-attacks, 1-2 shots of YOUR OWN — your garbage, not mine.
Remember: attacks on initializers that later code overwrites never land (no-op) —
attack function calls or post-generation data.
