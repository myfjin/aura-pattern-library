# overlapping_copy_requires_memmove

**Pattern:** overlapping_copy_requires_memmove

**Why you would reach for this:** `memcpy` is allowed to be fast precisely because it may assume the regions do not overlap — it can copy in any order, in any width. Shifting elements within one buffer is exactly the overlapping case, and it arises every time you insert or delete in the middle of an array. This pattern is the rule that any copy whose source and destination lie in the same buffer must use `memmove`.

**Entry fn:** `std::memmove(b + 2, b, 8);` — the overlap-safe copy.

**Valid input:** A 16-byte buffer whose contents are shifted within itself (source `b`, destination `b+2`, length 8). The copy must use `memmove`, not `memcpy`.

**Core:** `memcpy` may assume the source and destination do not overlap, so it can copy in any order and any width — on overlapping regions that is undefined. The unsafe arm calls `memcpy(b + 2, b, 8)` on overlapping regions, which the sanitizer flags as `memcpy-param-overlap`. The safe arm uses `std::memmove`, which is defined to handle overlap. Using `memmove` is the mechanism — any copy whose source and destination lie in the same buffer must use it.

**Assert:** The planted truth is that the `memmove` shift sums to `EXPECT_SUM_AFTER = 120` with `b[2]=1` and `b[3]=2`. Real SUCCESS line from the evidence file:
```
PASS: memmove summed 120 after overlap b[2]=1 b[3]=2 and the memcpy overlap was caught as memcpy-param-overlap
```

**⚠️ Defect it prevents:** The disaster is `memcpy` on overlapping regions being flagged by the sanitizer as `memcpy-param-overlap`. Real FAILURE line from the evidence file:
```
==1569237==ERROR: AddressSanitizer: memcpy-param-overlap: memory ranges [0x502000000012,0x50200000001a) and [0x502000000010, 0x502000000018) overlap
```
