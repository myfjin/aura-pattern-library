# span_over_resized_container

**Pattern:** span_over_resized_container

**Why you would reach for this:** You formed a span over a vector and then pushed more elements past its capacity. A span is a borrow — just a pointer plus a length — so it does not track container reallocation; growing the container moves the buffer and leaves the span pointing at the old one. This pattern is the rule for re-forming the span after growth.

**Entry fn:** `IntSpan s2(v.data(), 100);` — re-forming the span from the current buffer after growth.

**Valid input:** A `std::vector<int>` with 100 elements (all `7`) that has been fully grown (10000 more pushed) and whose first 100 elements you want to read. The span must be re-formed from the live buffer after the growth.

**Core:** `std::span` is a non-owning view — a pointer plus a length — with no connection back to the container it was formed over. The unsafe arm forms a span over the vector, then pushes 10000 elements; the growth reallocates, and the span still points at the freed old buffer. The safe arm performs all the growth first and then re-forms the span from `v.data()`, so it views the live buffer. Re-forming the span after growth is the mechanism — a span does not follow the container's reallocations.

**Assert:** The planted truth is that the re-formed span sums to `EXPECT_SUM = 700` over the first 100 elements. Real SUCCESS line from the evidence file:
```
PASS: re-formed span summed 700 and the dangling span was caught as heap-use-after-free
```

**⚠️ Defect it prevents:** The disaster is the span reading the freed old buffer after the container reallocates — a heap-use-after-free. Real FAILURE line from the evidence file:
```
==1422252==ERROR: AddressSanitizer: heap-use-after-free on address 0x514000000040 at pc 0x5c7061350ae7 bp 0x7ffc2aa1bc10 sp 0x7ffc2aa1bc00
```

> **Portability note.** `std::span` is C++20 and the library compiles C++17, so this file uses `IntSpan` — the minimal equivalent non-owning pointer+length view. The mechanism, the disaster and the rule are identical; `std::span` tracks container reallocation exactly as poorly. The unsafe arm also reports the move itself, so the disaster is witnessed with no sanitizer present:
```
heap-use-after-free: captured 0x514000000040 but the buffer moved to 0x52f000000400 - the capture is freed
```
