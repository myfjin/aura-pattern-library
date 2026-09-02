# unique_ptr_array_vs_scalar_delete

**Pattern:** unique_ptr_array_vs_scalar_delete

**Why you would reach for this:** `unique_ptr<T>` calls `delete`, and `unique_ptr<T[]>` calls `delete[]`. Handing an array allocation to the scalar form is a mismatch the compiler will not catch and the sanitizer will. This pattern is the rule that the deleter must match the allocation form — and `make_unique<T[]>(n)` picks it for you.

**Entry fn:** `auto p = std::make_unique<int[]>(EXPECT_N);` — the array form, whose deleter matches the `new[]` allocation.

**Valid input:** An array of 16 ints (`1..16`) allocated with `new[]`. The owning handle must be the array form so destruction uses `delete[]`.

**Core:** `unique_ptr<T>` uses a scalar deleter (`delete`) and `unique_ptr<T[]>` uses an array deleter (`delete[]`). The unsafe arm writes `std::unique_ptr<int>(new int[EXPECT_N])` — a scalar `unique_ptr` holding an array allocation — so destruction calls `delete` on a `new[]` block, a mismatch. The safe arm uses `make_unique<int[]>(EXPECT_N)`, whose deleter matches the allocation form. Matching the deleter to the allocation is the mechanism; `make_unique<T[]>` picks the correct form for you.

**Assert:** The planted truth is that the `make_unique` array sums to `EXPECT_SUM = 136`. Real SUCCESS line from the evidence file:
```
PASS: make_unique array summed 136 and the scalar-delete mismatch was caught as alloc-dealloc-mismatch
```

**⚠️ Defect it prevents:** The disaster is the scalar deleter freeing the array incorrectly — an alloc-dealloc mismatch. Real FAILURE line from the evidence file:
```
==1432324==ERROR: AddressSanitizer: alloc-dealloc-mismatch (operator new [] vs operator delete) on 0x506000000020
```
