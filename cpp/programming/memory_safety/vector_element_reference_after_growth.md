# vector_element_reference_after_growth

**Pattern:** vector_element_reference_after_growth

**Why you would reach for this:** You held a reference to an element of a `std::vector` and then grew the container — a `push_back` or a reserve change that reallocates. A reference or pointer to an element dies on reallocation; only an index survives. This pattern is the rule for re-reading by index after growth instead of holding a reference across it.

**Entry fn:** `int val = v[0];` — re-reading the element by index after the growth.

**Valid input:** A `std::vector<int>` that has been fully grown (10000 elements pushed after the first) and whose first element (value 42) you want to read. The index access must happen after the growth, not before.

**Core:** A `std::vector`'s element references and pointers are invalidated by any operation that reallocates the buffer. The unsafe arm binds `int& r = v[0]`, then pushes 10000 elements; the growth reallocates, and `r` points into the freed old buffer. The safe arm performs all the growth first and then re-reads `v[0]` by index, which always resolves against the current live buffer. Re-reading by index after growth is the mechanism — indices survive reallocation, references and pointers do not.

**Assert:** The planted truth is that re-reading `v[0]` by index after growth yields `EXPECT = 42`. Real SUCCESS line from the evidence file:
```
PASS: index survived growth yielding 42 and the dangling reference was caught as heap-use-after-free
```

**⚠️ Defect it prevents:** The disaster is the reference pointing into the old buffer, which was freed on reallocation — a heap-use-after-free. Real FAILURE line from the evidence file:
```
==1423091==ERROR: AddressSanitizer: heap-use-after-free on address 0x502000000010 at pc 0x573c72c9d924 bp 0x7ffcadc060e0 sp 0x7ffcadc060d0
```
