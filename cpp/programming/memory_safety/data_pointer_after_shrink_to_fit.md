# data_pointer_after_shrink_to_fit

**Pattern:** data_pointer_after_shrink_to_fit

**Why you would reach for this:** You cached a `v.data()` pointer, then ran a clear-and-shrink cycle on the container, and you need to know whether that pointer is still valid. `clear()` alone keeps the buffer, so a stale pointer can seem to work for a long time — right up until `shrink_to_fit()` actually releases the allocation. This pattern is the rule for taking an owning copy before any allocation-trimming operation.

**Entry fn:** `std::vector<int> owned = v;` — an owning copy taken before `clear()` and `shrink_to_fit()`.

**Valid input:** A `std::vector<int>` with 100 elements (all `7`) whose data you want to keep after the container is cleared and trimmed. The copy must be made while the vector still holds its buffer.

**Core:** `clear()` does not release storage — it only destroys elements, so a stale `data()` pointer often still reads valid memory. `shrink_to_fit()` is different: it releases the excess allocation, invalidating every pointer previously obtained from `data()`. The unsafe arm caches `v.data()`, clears, shrinks, and then reads through the stale pointer into freed memory. The safe arm copies the vector into an owning `owned` before clearing, so the data lives in a separate buffer that survives the trim. The mechanism is taking ownership before the operation that frees the original buffer.

**Assert:** The planted truth is that the owning copy sums to `EXPECT_SUM = 700` and the trimmed vector's capacity is exactly `0`. Real SUCCESS line from the evidence file:
```
PASS: owning copy summed 700 capacity 0 and the shrink_to_fit dangling was caught as heap-use-after-free
```

**⚠️ Defect it prevents:** The disaster is the cached pointer reading the freed buffer after `shrink_to_fit()` — a heap-use-after-free. Real FAILURE line from the evidence file:
```
==1421833==ERROR: AddressSanitizer: heap-use-after-free on address 0x514000000040 at pc 0x5efead7eb93f bp 0x7ffddda23470 sp 0x7ffddda23460
```
