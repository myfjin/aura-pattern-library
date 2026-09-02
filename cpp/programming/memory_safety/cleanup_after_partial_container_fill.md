# cleanup_after_partial_container_fill

**Pattern:** cleanup_after_partial_container_fill

**Why you would reach for this:** You are filling a container with raw owning pointers in a loop that can throw halfway through. The elements already inserted are owned by nobody — `clear()` destroys the pointers, not the things they point to, so the inserted blocks are abandoned and unreachable. This pattern is the rule for using a container of `unique_ptr` so every successfully inserted element is released however the loop exits.

**Entry fn:** `std::vector<std::unique_ptr<int[]>> v;` — a container of owning handles instead of raw pointers.

**Valid input:** A loop that allocates 5 blocks of 16 ints (each `1..16`) and may throw at iteration 3. The container must own each block via `unique_ptr` so unwinding releases the already-inserted elements.

**Core:** A raw `int*` in a container owns nothing — `clear()` destroys the pointer value, not the pointee, so blocks inserted before a throw are leaked. The unsafe arm fills a `vector<int*>` and throws at iteration 3; the three already-inserted blocks are abandoned. The safe arm fills a `vector<std::unique_ptr<int[]>>`; when the loop throws, unwinding destroys the `unique_ptr` elements, each releasing its block. Owning handles in the container is the mechanism — every successfully inserted element is released on any exit path.

**Assert:** The planted truth is that the `unique_ptr` vector releases on throw and the success path sums the first block to `EXPECT_SUM = 136`. Real SUCCESS line from the evidence file:
```
PASS: unique_ptr vector released on throw and success summed 136, raw leak caught as detected memory leaks
```

**⚠️ Defect it prevents:** The disaster is the three already-inserted blocks being abandoned and unreachable when the fill throws — a memory leak. Real FAILURE line from the evidence file:
```
==1421739==ERROR: LeakSanitizer: detected memory leaks
```
