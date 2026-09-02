# pointer_after_container_swap

**Pattern:** pointer_after_container_swap

**Why you would reach for this:** You are swapping a `std::vector` into a temporary or a scope-bound container, then reading through a pointer you captured before the swap. `swap` is O(1) because it exchanges buffers, not contents — so swapping with a short-lived container hands your buffer to something that is about to die. This pattern is the rule for re-acquiring the pointer from the new owner after the swap.

**Entry fn:** `int* p = b.data();` — re-acquiring the pointer from the new owner `b` after the swap.

**Valid input:** A `std::vector<int>` with 100 elements (all `7`) whose data you want to read after a swap. The new owner must outlive the read, and the pointer must be re-acquired from it after the swap.

**Core:** `swap` transfers buffer ownership between containers in constant time — it exchanges the internal buffers, not the contents. The unsafe arm captures `a.data()`, swaps `a` into a scope-bound `b`, and then reads through the stale pointer after `b` dies and frees the buffer. The safe arm lets `b` outlive the read and re-acquires the pointer from `b` after the swap, so it points at the live buffer. Re-acquiring from the new owner is the mechanism — the pointer follows the buffer, not the container variable.

**Assert:** The planted truth is that the re-acquired pointer from the new owner sums to `EXPECT_SUM = 700`. Real SUCCESS line from the evidence file:
```
PASS: re-acquired pointer from new owner summed 700 and the swap dangling was caught as heap-use-after-free
```

**⚠️ Defect it prevents:** The disaster is the pointer reading the freed buffer when the swap target dies — a heap-use-after-free. Real FAILURE line from the evidence file:
```
==1422057==ERROR: AddressSanitizer: heap-use-after-free on address 0x514000000040 at pc 0x652b15e8293a bp 0x7fff933c4f40 sp 0x7fff933c4f30
```
