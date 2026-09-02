# throwing_copy_in_swap

**Pattern:** throwing_copy_in_swap

**Why you would reach for this:** A swap that can throw leaves both objects broken — it frees one side's buffer and throws halfway, leaving a dangling pointer, and the object you did not touch is the one that breaks. This pattern is the rule that swap must be `noexcept`: it should only exchange pointers, with no allocation and no copying.

**Entry fn:** `void good_swap(Buf& a, Buf& b) noexcept` — a pointer-only, `noexcept` swap.

**Valid input:** Two `Buf` objects, each holding 8 ints (1..8), to be swapped. The swap must only exchange pointers and lengths, with no operation that can throw.

**Core:** A correct swap only exchanges pointers — no allocation, no copying — so it cannot throw. The unsafe arm's `bad_swap` frees one side's buffer and then throws before completing the exchange, leaving that side's pointer dangling. The safe arm's `good_swap` is `noexcept` and only swaps the pointer and length members, so both objects remain valid. Pointer-only exchange is the mechanism — a swap that copies or allocates can throw and break both objects.

**Assert:** The planted truth is that the `noexcept` swap preserves the sum `EXPECT_SUM = 36` on both sides. Real SUCCESS line from the evidence file:
```
PASS: noexcept swap preserved sum 36 on both sides and the throwing swap was caught as heap-use-after-free
```

**⚠️ Defect it prevents:** The disaster is the swap freeing one side's buffer and throwing, leaving a dangling pointer — a heap-use-after-free. Real FAILURE line from the evidence file:
```
==1432266==ERROR: AddressSanitizer: heap-use-after-free on address 0x503000000070 at pc 0x5b75a0991d52 bp 0x7fff53f7f960 sp 0x7fff53f7f950
```
