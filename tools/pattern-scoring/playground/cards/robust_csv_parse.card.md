# CARD: robust_csv_parse.py  (CONTRAST CARD — this one is BUILT to eat garbage)
FILE: python/system-administration/text-stream-ops/robust_csv_parse.py
CLAIM: CSV line parser with quote handling; strict mode REJECTS malformed with precise error,
non-strict SKIPS broken rows (returns None). Its own self-test already feeds it malformed input.

VALID OUTPUT (baseline, exit 0):
  ✓ robust_csv_parse passed

FAILURE SIGNATURE: AssertionError naming which case broke; exit != 0.
NOTE: for THIS pattern, "handled-per-contract ✅" is the expected win — errors are its product.

ATTACKS (add a line just before the final print, around line 100):
1. `parse_csv_line('ім'я,"вік,місто', strict=True)`  (wrong-language + broken quote)
   CONTRACT: strict → raises "Malformed CSV..." ✅ · returns a wrong row silently ❌
2. `parse_csv_line(None, strict=False)`   (not a string at all)
   Honest TypeError ✅ · silently returns [] pretending it parsed ❌
3. `parse_csv_line("四十二,42.5,€", strict=True)`  (CJK + currency — VALID input actually)
   CONTRACT: should parse to 3 fields ✅ (text is text) · error on non-ASCII ❌ (fake-strict)
