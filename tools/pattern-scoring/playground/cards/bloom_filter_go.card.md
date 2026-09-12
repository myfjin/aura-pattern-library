# CARD: bloom_filter (GO batch 1 — compact format)
FILE: go/programming/data_structures/bloom_filter.go
BASELINE (verified 2026-07-21): bloom_filter ... resize clears — PASS
ENTRY: NewBloomFilter(capacity, errorRate) · Add/Contains/FalsePositiveRate/Resize · demo line 124
RUN: `cd playground/go && go run programming/data_structures/bloom_filter.go`
PASTES: compile-verified in scratch 2026-07-21 — every attack runs and lands as predicted.
RESET: `git checkout pristine-full -- programming/data_structures/bloom_filter.go`
CLAIM UNDER TEST: "never false-negative; FPR within ~3x target; resize clears"

PASTE-ATTACKS — one at a time, just above the final Printf (line 238).
At that point `bf` has been Resize(2000)'d — 1000 items added, then CLEARED.
1. ```go
	fmt.Println("post-resize itemCount:", bf.itemCount, "analytic FPR:", bf.FalsePositiveRate())
   ```
   ttl_cache's size()-lie KIN — Resize (line 114) rebuilds the bit array but never
   resets itemCount. My prediction: itemCount=1000 and a nonzero "false-positive rate"
   reported for a filter that is EMPTY. The analytic self-report lies about state —
   same class as the size() docstring-lie you STRONG-FLAGGED in python.
2. ```go
	dup := NewBloomFilter(100, 0.01)
	dup.Add("same"); dup.Add("same"); dup.Add("same")
	fmt.Println("3x same item -> itemCount:", dup.itemCount, "fpr:", dup.FalsePositiveRate())
   ```
   duplicate accounting — Add counts every call (line 94), not distinct items. itemCount=3
   for one real element → analytic FPR overestimates. Flag-grade: does the FPR formula's
   n mean insertions or distinct members? Undeclared.
3. ```go
	tiny := NewBloomFilter(1, 0.99)
	tiny.Add("a")
	fmt.Println("cap=1 rate=0.99 -> bits:", tiny.bitCount, "hashes:", tiny.hashCount,
		"contains b:", tiny.Contains("b"))
   ```
   E009 degenerate-param — capacity 1, errorRate 0.99 both pass the guards; bitCount
   collapses to 1-2 bits. My prediction: Contains("b") true almost surely — a filter
   that answers yes to everything, constructed without complaint. Boundary vs guard hole.

NOTE (honest): the two guards that EXIST are real — shrinking Resize and invalid
construction genuinely panic (self-test proves both). The attack surface is what the
guards don't cover: state accounting.

FREE-PLAY: your garbage after mine. Skip giant-capacity constructions (1e9+ allocates
GBs — resource bomb, not a finding).
