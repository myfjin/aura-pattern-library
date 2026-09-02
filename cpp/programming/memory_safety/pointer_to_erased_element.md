# pointer_to_erased_element

**Pattern:** pointer_to_erased_element

**Why you would reach for this:** You kept a pointer to an element of a node-based container — a `std::list` or set — and then removed that element. Erasing a node deallocates it, so a pointer taken before the erase dangles. This pattern is the rule for re-querying the container after the erase instead of trusting a cached pointer to a removed element.

**Entry fn:** `std::accumulate(l.begin(), l.end(), 0L)` — re-querying the container after the erase.

**Valid input:** A `std::list<int>` holding 1..8, from which one element (the 4th, value 4) has been erased. The remaining elements must be re-read from the container after the erase, not through a pre-erase pointer.

**Core:** In a node-based container each element lives in its own heap-allocated node. The unsafe arm caches `&*it` for the 4th element, erases that element, and then dereferences the cached pointer — the node was deallocated by the erase, so the read hits freed memory. The safe arm performs the erase and then re-queries the container, summing the surviving elements. Re-querying after the erase is the mechanism — a pointer into a removed node is freed memory, not stale-but-readable.

**Assert:** The planted truth is that after erasing the 4th element the re-queried list sums to `EXPECT_AFTER = 32` and has size `EXPECT_SIZE = 7`. Real SUCCESS line from the evidence file:
```
PASS: re-queried list summed 32 size 7 and the erased-node pointer was caught as heap-use-after-free
```

**⚠️ Defect it prevents:** The disaster is the pointer reading the freed node's memory after the erase — a heap-use-after-free. Real FAILURE line from the evidence file:
```
==1422076==ERROR: AddressSanitizer: heap-use-after-free on address 0x5030000000e0 at pc 0x641e51e629a6 bp 0x7ffe5be755e0 sp 0x7ffe5be755d0
```
