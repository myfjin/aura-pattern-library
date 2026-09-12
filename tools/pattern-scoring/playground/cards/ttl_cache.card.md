# CARD: ttl_cache  (batch 2 — compact format)
FILE: python/system-administration/secrets-credentials/ttl_cache.py
BASELINE (verified 2026-07-19): ttl_cache PASS
ENTRY: ttl_cache(ttl_seconds=100, clock=None) · demo starts line 54

PASTE-ATTACKS — one at a time, just above the file's final print (~line 101);
run · read against the three-way rule · git checkout pristine -- <file> · next.
1. `    print(ttl_cache(-5))`
   negative TTL — B5: does it mean already-expired (defensible if declared) or silent weirdness?
2. `    print(ttl_cache(0))`
   zero TTL — boundary: instant expiry or divide-by-zero somewhere?

FREE-PLAY: after the paste-attacks, 1-2 shots of YOUR OWN — your garbage, not mine.
Remember: attacks on initializers that later code overwrites never land (no-op) —
attack function calls or post-generation data.
