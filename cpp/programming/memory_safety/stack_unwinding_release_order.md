# stack_unwinding_release_order

**Pattern:** stack_unwinding_release_order

**Why you would reach for this:** Later objects may hold references into earlier ones, so manual cleanup in the wrong order frees something still in use. If two resources exist where the second aliases the first's buffer, releasing the first first frees memory the second is still pointing into. This pattern is the rule that resources must be released in reverse order of acquisition — which RAII gets right by construction.

**Entry fn:** `auto a = std::make_unique<ResourceA>();` — RAII ownership so destructors run in reverse construction order.

**Valid input:** A `ResourceA` owning a 16-int buffer (`1..16`) and a `ResourceB` that aliases that buffer. The buffer must be read before teardown, and the owner must be released after the alias goes out of scope.

**Core:** Destructors run in reverse construction order for a reason: later objects may hold references into earlier ones. The unsafe arm manually frees `a.buf` first while `b.alias` still points into it, then reads through the dangling alias. The safe arm uses RAII — `b` goes out of scope before `a`, so the alias is dropped before the buffer is freed. Reverse-order release is the mechanism; RAII gets it right by construction.

**Assert:** The planted truth is that the RAII reverse-order release sums to `EXPECT_SUM = 136` with release order `b,a`. Real SUCCESS line from the evidence file:
```
PASS: RAII reverse-order release summed 136 order b,a and the wrong-order free was caught as heap-use-after-free
```

**⚠️ Defect it prevents:** The disaster is the first resource being freed while the second still aliases its buffer — a heap-use-after-free. Real FAILURE line from the evidence file:
```
==1432247==ERROR: AddressSanitizer: heap-use-after-free on address 0x506000000020 at pc 0x60ae61e0a8ab bp 0x7ffd718f9360 sp 0x7ffd718f9350
```
