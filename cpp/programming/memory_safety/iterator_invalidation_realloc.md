# iterator_invalidation_realloc

**Pattern:** iterator_invalidation_realloc

**Why you would reach for this:** You are walking a container while mutating it — appending to a `std::vector` inside a traversal, or doing any growth that may reallocate the buffer. An iterator you obtained before the growth points into the old, freed allocation. This pattern is the rule for re-acquiring elements by index after growth instead of holding an iterator across a reallocation.

**Entry fn:** `v[i]` — element access by index, re-acquired after all the `push_back` growth has happened.

**Valid input:** A `std::vector<int>` that has been fully grown (here, 100 initial elements plus 10000 appended) and whose first 100 elements you want to sum. The index access must happen after the growth, not before.

**Core:** A `std::vector`'s iterators are invalidated by any operation that reallocates the buffer. The unsafe arm captures `v.begin()` before pushing 10000 more elements; the growth reallocates, and dereferencing the stale iterator reads freed memory. The safe arm performs all the growth first and then re-acquires each element by index, which always resolves against the current live buffer. Re-acquiring by index after growth is the mechanism — indices survive reallocation, iterators do not.

**Assert:** The planted truth is that re-acquiring the first 100 elements by index sums to `EXPECT = 4950`. Real SUCCESS line from the evidence file:
```
PASS: index re-acquisition summed 4950 and the dangling iterator was caught as heap-use-after-free
```

**⚠️ Defect it prevents:** The disaster is an iterator held across a reallocation dereferencing freed memory — a heap-use-after-free. Real FAILURE line from the evidence file:
```
==1421939==ERROR: AddressSanitizer: heap-use-after-free on address 0x515000000080 at pc 0x5ad3966de9fc bp 0x7ffc6f1bf480 sp 0x7ffc6f1bf470
```
