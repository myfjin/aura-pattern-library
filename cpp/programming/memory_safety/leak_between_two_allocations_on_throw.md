# leak_between_two_allocations_on_throw

**Pattern:** leak_between_two_allocations_on_throw

**Why you would reach for this:** Two raw `new`s in one function is a leak waiting for the second one to fail. If you allocate multiple resources in sequence before any RAII wrapper is applied, a throw in a later step abandons the earlier allocation. This pattern is the rule for giving each pointer to an RAII owner so cleanup is automatic on any exit path.

**Entry fn:** `auto up = std::make_unique<int[]>(EXPECT_N);` — an RAII owner that releases the allocation on any exit path.

**Valid input:** A block of 64 ints (`0..63`) allocated before a later step throws. The allocation must be held by an RAII owner so it is released when the throw propagates.

**Core:** The unsafe arm allocates a raw block and then throws before the `delete[]` is reached — the first allocation is abandoned when the second step fails. The safe arm holds the block in a `std::unique_ptr`; when the throw propagates, the owner is destroyed during unwinding and releases the block. Giving the pointer to an RAII owner is the mechanism — cleanup happens automatically on any exit path, including the throwing one.

**Assert:** The planted truth is that the `unique_ptr` holds the block through the throw and the sum is `EXPECT_SUM = 2016`. Real SUCCESS line from the evidence file:
```
PASS: unique_ptr held 2016 through throw and the raw-pointer leak was caught as detected memory leaks
```

**⚠️ Defect it prevents:** The disaster is the first allocation being abandoned when the second step throws — a memory leak. Real FAILURE line from the evidence file:
```
==1421978==ERROR: LeakSanitizer: detected memory leaks
```
