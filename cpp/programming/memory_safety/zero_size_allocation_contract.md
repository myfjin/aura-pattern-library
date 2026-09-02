# zero_size_allocation_contract

**Pattern:** zero_size_allocation_contract

**Why you would reach for this:** `new T[0]` and `malloc(0)` succeed. They return a real, non-null, unique pointer that you must still release — and that you must never dereference. Every "did the allocation work?" check passes, so an empty input flows straight through into a loop that writes one element. This pattern is the rule that a zero-length allocation is valid and must be freed, but has no elements.

**Entry fn:** the zero-length loop `for (int i = 0; i < n0; ++i)` — which must run 0 times on a zero-length allocation.

**Valid input:** An array allocated from an external size that may be zero. A zero-length allocation must be freed but never dereferenced; a non-null result answers "did it allocate", never "is there anything there".

**Core:** `new T[0]` and `malloc(0)` succeed, returning a real, non-null, unique pointer that must be released but never dereferenced. The unsafe arm allocates `new int[0]` and writes `a[0] = 1` — no elements exist, so the write is a heap-buffer-overflow. The safe arm allocates zero-length, verifies it is non-null, runs a loop that iterates 0 times, and frees it; then it handles the non-empty case separately. Treating a non-null zero-length result as "no elements" is the mechanism — a non-null result answers "did it allocate", never "is there anything there".

**Assert:** The planted truth is that the zero-length loop runs 0 times and the non-empty case sums to `EXPECT_SUM = 136`. Real SUCCESS line from the evidence file:
```
PASS: zero-length looped 0 times non-empty summed 136 and the zero-alloc write was caught as heap-buffer-overflow
```

**⚠️ Defect it prevents:** The disaster is writing to `a[0]` on a zero-length allocation being a heap-buffer-overflow. Real FAILURE line from the evidence file:
```
==1570463==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x502000000010 at pc 0x5be6229b5641 bp 0x7ffe8048cf20 sp 0x7ffe8048cf10
```
