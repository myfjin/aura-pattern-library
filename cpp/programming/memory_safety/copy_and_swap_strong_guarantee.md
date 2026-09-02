# copy_and_swap_strong_guarantee

**Pattern:** copy_and_swap_strong_guarantee

**Why you would reach for this:** You are writing `operator=` for a class that manages memory, and the copy step can throw. The strong guarantee says a failed assignment leaves the target unchanged — but a naive "free then rebuild" order cannot offer it: if the rebuild throws, the target is left holding a freed pointer, and the next read is a use-after-free. This pattern is the rule for copy-and-swap, which gives the strong guarantee by construction.

**Entry fn:** `SafeBuffer& operator=(SafeBuffer other)` — copy-and-swap assignment, taking the copy by value.

**Valid input:** A `SafeBuffer` holding 8 ints (1..8) being assigned from another buffer whose copy is made to throw. The target must remain valid and unchanged when the copy throws.

**Core:** Copy-and-swap puts all work that can throw on a temporary: the parameter is a copy built from `other`, and the only mutation is a `noexcept` swap of the buffers. The unsafe arm's naive `operator=` frees the target's data first, then rebuilds — if the rebuild throws, `data` still holds the freed pointer and the next read is a use-after-free. Copy-and-swap is the mechanism: the copy is built before any mutation, so a throwing copy leaves the target untouched.

**Assert:** The planted truth is that after a throwing assignment the copy-and-swap target still sums to `EXPECT_SUM = 36` and has size `EXPECT_N = 8`. Real SUCCESS line from the evidence file:
```
PASS: copy-and-swap preserved sum 36 size 8 through throw and the freed read was caught as heap-use-after-free
```

**⚠️ Defect it prevents:** The disaster is the target's data pointer being freed, the rebuild throwing, and the freed pointer being read — a heap-use-after-free. Real FAILURE line from the evidence file:
```
==1421767==ERROR: AddressSanitizer: heap-use-after-free on address 0x503000000040 at pc 0x5d836260fab2 bp 0x7ffdec57ac50 sp 0x7ffdec57ac40
```
