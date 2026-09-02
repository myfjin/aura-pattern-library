# small_buffer_boundary

**Pattern:** small_buffer_boundary

**Why you would reach for this:** Small-buffer optimisation keeps a few elements inside the object and spills to the heap only when it must. A pointer into such a container is valid or dangling depending on a size change that crosses the boundary in either direction, moving the data. This pattern is the rule that a pointer obtained from an SBO container is invalidated by any size change that crosses the inline/heap boundary.

**Entry fn:** `int* fresh = c.p;` — re-reading `data()` after every resize that crosses the boundary.

**Valid input:** An SBO container holding 16 ints (`1..16`) that is shrunk to 4, crossing from heap back to inline. The pointer must be re-read after the shrink.

**Core:** An SBO container keeps a few elements inline and spills to the heap only when it must; a size change that crosses the boundary in either direction moves the data. The unsafe arm caches a pointer into the heap block, then shrinks to 4 — the shrink copies the data back to inline and frees the heap block, so the cached pointer reads freed memory. The safe arm re-reads `c.p` after the shrink, so it points at the inline buffer. Re-reading `data()` after every resize is the mechanism — a pointer into an SBO container is invalidated by any size change that crosses the boundary.

**Assert:** The planted truth is that re-reading after shrink sums to `EXPECT_SUM_BIG = 136` big and `EXPECT_SUM_SMALL = 10` small, with the container back inline. Real SUCCESS line from the evidence file:
```
PASS: re-read after shrink summed 136 big 10 small inline and the old heap pointer was caught as heap-use-after-free
```

**⚠️ Defect it prevents:** The disaster is the old heap pointer reading freed memory after shrink copies data back to inline — a heap-use-after-free. Real FAILURE line from the evidence file:
```
==1435589==ERROR: AddressSanitizer: heap-use-after-free on address 0x506000000020 at pc 0x5bd51b93c8a3 bp 0x7fff29bc7760 sp 0x7fff29bc7750
```
