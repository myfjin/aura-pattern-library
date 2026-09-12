# CARD: online_sgd_classifier  (batch 2 — compact format)
FILE: python/data-science/streaming_and_sketches/online_sgd_classifier.py
BASELINE (verified 2026-07-19): Online SGD loss …/ Batch …/ accuracy 99.00% (3+ lines)
ENTRY: logistic(z) · demo starts line 93

PASTE-ATTACKS — one at a time, just above the file's final print (~line 143);
run · read against the three-way rule · git checkout pristine -- <file> · next.
1. `    print(logistic(1e18))`
   huge z — B3 overflow: math.exp(-1e18) underflows fine but exp(+…) can OverflowError. Watch which way it breaks
2. `    print(logistic(float("nan")))`
   NaN in — NaN out silently? A probability that is NaN = INVALID if unflagged

FREE-PLAY: after the paste-attacks, 1-2 shots of YOUR OWN — your garbage, not mine.
Remember: attacks on initializers that later code overwrites never land (no-op) —
attack function calls or post-generation data.
