# arena_reset_semantics

**Pattern:** arena_reset_semantics

**Why you would reach for this:** An arena is fast because it hands out slices of one big block and frees nothing individually. That makes `reset()` the most dangerous method: whether issued pointers survive depends on whether reset reuses or replaces the block. The contract must be written down because the type system says nothing. This pattern is the rule that every pointer an arena issued is invalidated by a reset that reallocates.

**Entry fn:** `void ArenaGen::reset(size_t c)` — a reset that reallocates and bumps a generation counter, plus a `Handle` that records the generation.

**Valid input:** An arena that hands out a 16-int slice (`1..16`) and is then reset with a new capacity. A holder must be able to detect that its slice pointer is stale.

**Core:** The unsafe arm's `reset` frees the old block and allocates a new one, so a previously issued slice pointer reads freed memory. The safe arm's `ArenaGen` bumps a generation counter on every reset, and a `Handle` records the generation at allocation time; after a reset the holder compares generations, detects the stale handle, and re-acquires a fresh slice. A generation counter is the mechanism — it lets a holder check whether its issued pointer is still valid after a reset that reallocates.

**Assert:** The planted truth is that the generation counter detects the stale handle after reset, summing to `EXPECT_SUM = 136` with `gen 1`. Real SUCCESS line from the evidence file:
```
PASS: generation counter detected stale handle after reset summing 136 gen 1 and the freed slice was caught as heap-use-after-free
```

**⚠️ Defect it prevents:** The disaster is the old slice pointer reading freed memory after reset reallocates — a heap-use-after-free. Real FAILURE line from the evidence file:
```
==1434675==ERROR: AddressSanitizer: heap-use-after-free on address 0x519000000080 at pc 0x592a40db681a bp 0x7ffd4f816540 sp 0x7ffd4f816530
```
