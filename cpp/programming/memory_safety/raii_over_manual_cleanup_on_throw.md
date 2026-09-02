# raii_over_manual_cleanup_on_throw

**Pattern:** raii_over_manual_cleanup_on_throw

**Why you would reach for this:** The manual `delete` at the bottom of a function is correct exactly once — on the path where nothing throws. If you acquire a resource and then call code that may throw before the delete, the pointer is abandoned on the throwing path and becomes unreachable. This pattern is the rule for moving the release to a place the language guarantees will run.

**Entry fn:** `auto up = std::make_unique<int[]>(EXPECT_N);` — an RAII owner whose destructor runs on every exit path including unwinding.

**Valid input:** A block of 64 ints (`0..63`) allocated before a step that throws. The allocation must be held by an RAII owner so it is released when the throw propagates.

**Core:** The unsafe arm allocates a raw block and then throws before the trailing `delete[]` is reached — the manual cleanup never runs on the throwing path. The safe arm holds the block in a `std::unique_ptr`; when the throw propagates, the owner is destroyed during unwinding and releases the block. RAII is the mechanism — a destructor runs on every exit path, including unwinding, so the release is guaranteed.

**Assert:** The planted truth is that the `unique_ptr` releases on throw and the success path sums to `EXPECT_SUM = 2016`. Real SUCCESS line from the evidence file:
```
PASS: unique_ptr released on throw and success summed 2016, manual leak caught as detected memory leaks
```

**⚠️ Defect it prevents:** The disaster is the pointer being abandoned on the throwing path and becoming unreachable — a memory leak. Real FAILURE line from the evidence file:
```
==1431368==ERROR: LeakSanitizer: detected memory leaks
```
