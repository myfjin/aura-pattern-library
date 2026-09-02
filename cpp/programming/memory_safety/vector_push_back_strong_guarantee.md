# vector_push_back_strong_guarantee

**Pattern:** vector_push_back_strong_guarantee

**Why you would reach for this:** `push_back` promises the strong guarantee — if it throws, the vector is exactly as it was. A hand-rolled container that frees the old buffer before the new one is safely filled breaks that promise: a failed growth leaves the storage pointer dangling. This pattern is the rule for doing the throwing work first, then swapping.

**Entry fn:** `void GoodVector::push(int val)` — allocate the new buffer first, fill it, and only then free the old one.

**Valid input:** A hand-rolled vector holding 4 ints (1..4) that attempts a growth which throws. The old buffer must survive the failed growth so the container is unchanged.

**Core:** The unsafe arm frees the old buffer before allocating the new one, then throws during the simulated allocation step — the storage pointer is left dangling and the next read is a use-after-free. The safe arm allocates the new buffer and copies the elements first, and only frees the old buffer after the new one is ready; if the allocation throws, the old buffer is untouched. Allocate-first-then-swap is the mechanism — the old buffer survives any failure, preserving the strong guarantee.

**Assert:** The planted truth is that after a failed growth the container still sums to `EXPECT_SUM = 10` and has size 4. Real SUCCESS line from the evidence file:
```
PASS: allocate-first preserved sum 10 size 4 and the dangling storage was caught as heap-use-after-free
```

**⚠️ Defect it prevents:** The disaster is the container's storage pointer being freed and dangling after a failed growth — a heap-use-after-free. Real FAILURE line from the evidence file:
```
==1432454==ERROR: AddressSanitizer: heap-use-after-free on address 0x502000000010 at pc 0x5c05eece4871 bp 0x7ffc6a4b6f40 sp 0x7ffc6a4b6f30
```
