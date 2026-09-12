# CARD: token_bucket_limiter  (batch 2 — compact format)
FILE: python/system-administration/resource-guards/token_bucket_limiter.py
BASELINE (verified 2026-07-19): SILENT: no output, exit 0 (check echo $?)
ENTRY: token_bucket_limiter(tokens_per_sec=10) · demo starts line 40

PASTE-ATTACKS — one at a time, just above the file's final print (~line end of main);
run · read against the three-way rule · git checkout pristine -- <file> · next.
1. `    print(token_bucket_limiter(0))`
   zero rate — bucket never refills: honest error or infinite-wait semantics? Contract decides
2. `    print(token_bucket_limiter(-10))`
   negative rate — B5: tokens per second cannot be negative

FREE-PLAY: after the paste-attacks, 1-2 shots of YOUR OWN — your garbage, not mine.
Remember: attacks on initializers that later code overwrites never land (no-op) —
attack function calls or post-generation data.
