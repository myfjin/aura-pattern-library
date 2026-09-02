# self_assignment_safety

**Pattern:** self_assignment_safety

**Why you would reach for this:** `x = x` looks impossible until an alias makes it happen — two references to the same object, or a container holding a reference to itself. A naive copy-assignment that frees its own data before copying from `other` reads freed memory when `other` is the same object. This pattern is the rule for making copy-assignment self-assignment-safe by construction.

**Entry fn:** `SafeBuffer& operator=(SafeBuffer other)` — copy-and-swap assignment, taking the copy by value.

**Valid input:** A `SafeBuffer` holding 8 ints (1..8) that is assigned to itself. The copy must be built before the old data is destroyed, so even `x = x` is a no-op.

**Core:** Copy-and-swap makes self-assignment safe by construction: the parameter is a copy built from `other` before any of the current object's data is touched, and the swap then exchanges buffers. The unsafe arm's hand-written `operator=` captures the source pointer, deletes its own data, and then copies from the captured pointer — on self-assignment that pointer is into the block it just freed. Copy-and-swap is the mechanism: the copy is made first, so the source is never read after the destination's data is destroyed.

**Assert:** The planted truth is that after `x = x` the copy-and-swap buffer still sums to `EXPECT = 36` and has size `EXPECT_SIZE = 8`. Real SUCCESS line from the evidence file:
```
PASS: copy-and-swap preserved sum 36 size 8 and the self-assignment freed read was caught as heap-use-after-free
```

**⚠️ Defect it prevents:** The disaster is a hand-written `operator=` that deletes its data then copies from `other`, reading freed memory when `other` is the same object — a heap-use-after-free. Real FAILURE line from the evidence file:
```
==1422185==ERROR: AddressSanitizer: heap-use-after-free on address 0x503000000040 at pc 0x764050c3a397 bp 0x7ffc15436670 sp 0x7ffc15435e18
```
