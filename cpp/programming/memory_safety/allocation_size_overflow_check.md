# allocation_size_overflow_check

**Pattern:** allocation_size_overflow_check

**Why you would reach for this:** `count * sizeof(T)` is unsigned arithmetic — it does not overflow, it wraps. A count from a file, header, or network packet can turn a request for gigabytes into a request for four bytes, and `malloc` will happily succeed. This pattern is the rule that the multiplication must be checked before the allocation.

**Entry fn:** the overflow check `n > (UINT_MAX / ELEM)` — a refusal before multiplying.

**Valid input:** An allocation size computed from an external count (`N_BIG = 1<<30` elements of 4 bytes) that wraps to zero. The oversized request must be refused before the multiplication.

**Core:** `count * sizeof(T)` is unsigned arithmetic, so it wraps rather than overflows — a huge external count can wrap to a tiny byte count and `malloc` succeeds on the small result. The unsafe arm multiplies `N_BIG * 4`, which wraps to 0, and `malloc(0)` succeeds; writing `p[0..7]` into the zero-byte allocation is a heap-buffer-overflow. The safe arm checks `n > (UINT_MAX / ELEM)` before multiplying and refuses the oversized request. Checking before the multiplication is the mechanism — `count > SIZE_MAX / sizeof(T)` is a refusal, not a rounding.

**Assert:** The planted truth is that the overflow check refuses the big request and the normal request sums to `EXPECT_SUM = 136` with `bytes 64`. Real SUCCESS line from the evidence file:
```
PASS: overflow check refused big request and normal summed 136 bytes 64 and the wrap was caught as heap-buffer-overflow
```

**⚠️ Defect it prevents:** The disaster is `malloc(0)` succeeding and writing `p[0..7]` being a heap-buffer-overflow. Real FAILURE line from the evidence file:
```
==1568631==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x502000000010 at pc 0x580ed4c3d692 bp 0x7ffe57b219f0 sp 0x7ffe57b219e0
```
