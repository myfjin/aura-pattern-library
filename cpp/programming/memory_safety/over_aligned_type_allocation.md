# over_aligned_type_allocation

**Pattern:** over_aligned_type_allocation

**Why you would reach for this:** A type with `alignas(64)` — a SIMD vector, a cache-line-padded counter — has an alignment requirement that plain `malloc` does not know about. `malloc` promises only `max_align_t`, and hand-computed offsets into a raw block promise nothing at all. The hardware may or may not fault; the standard says the access is undefined either way. This pattern is the rule that over-aligned types must be allocated through something that knows their alignment.

**Entry fn:** `Wide* w = new Wide();` — C++17 aligned new, which honours `alignas(64)`.

**Valid input:** An over-aligned type `Wide` (8 doubles, `alignas(64)`) to be allocated and written. The allocation must honour the 64-byte alignment requirement.

**Core:** A type with `alignas(64)` has an alignment requirement that plain `malloc` does not know about — `malloc` promises only `max_align_t`, and a hand-computed `+8` offset into a raw block guarantees the requirement is missed. The unsafe arm allocates `sizeof(Wide)+8` and constructs at `raw+8`, so the store to `w->v[0]` is misaligned and UBSan reports it. The safe arm uses C++17 aligned new, which honours `alignas(64)`. Allocating through something that knows the alignment is the mechanism — over-aligned types must not go through `malloc` with a manual offset.

**Assert:** The planted truth is that aligned new sums to `EXPECT_SUM = 36.0` and the pointer is aligned to 64. Real SUCCESS line from the evidence file:
```
PASS: aligned new summed 36.000000 aligned to 64 and the misaligned offset was caught as misaligned address
```

**⚠️ Defect it prevents:** The disaster is the `+8` offset guaranteeing the 64-byte requirement is missed, and UBSan reporting a misaligned store. Real FAILURE line from the evidence file (a UBSan line, not an AddressSanitizer one):
```
patterns_cpp_native/over_aligned_type_allocation.cpp:37: runtime error: store to misaligned address 0x507000000108 for type 'struct Wide', which requires 64 byte alignment
```
