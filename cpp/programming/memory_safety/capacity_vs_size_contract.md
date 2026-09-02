# capacity_vs_size_contract

**Pattern:** capacity_vs_size_contract

**Why you would reach for this:** `reserve()` buys memory; it does not create elements. The gap between `size()` and `capacity()` is raw storage the container has not constructed anything in, and `data()[i]` for `i >= size()` is reading it. The mistake is natural — you reserved 100, so 100 feels available — and it survives testing because the memory is usually there. This pattern is the rule that every read and write must be bounded by `size()`.

**Entry fn:** `for (size_t i = 0; i < v.size(); ++i) sum += v.data()[i];` — a loop bounded by `size()`, not `capacity()`.

**Valid input:** A `std::vector<int>` with 16 elements (`1..16`) and capacity at least 16. Reads must be bounded by `size()`, and an out-of-bounds index must be refused.

**Core:** `size()` is how many elements exist; `capacity()` is only how many fit before the next reallocation. The unsafe arm reads `v.data()[EXPECT_N]` — one past the last element, inside capacity but outside size — which is a heap-buffer-overflow even though the memory is within the allocated capacity. The safe arm bounds every read by `v.size()` and refuses the out-of-bounds index. Bounding by `size()` is the mechanism — capacity is not a license to read; only `size()` counts as existing elements.

**Assert:** The planted truth is that the size-bounded loop sums to `EXPECT_SUM = 136` and the bounds check refuses index `EXPECT_N`. Real SUCCESS line from the evidence file:
```
PASS: size-bounded loop summed 136 and the one-past-end read was caught as heap-buffer-overflow
```

**⚠️ Defect it prevents:** The disaster is reading one past the last element — a heap-buffer-overflow even though the memory is within the allocated capacity. Real FAILURE line from the evidence file:
```
==1434720==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x506000000060 at pc 0x618f8cf5a8a6 bp 0x7ffda4d60b50 sp 0x7ffda4d60b40
```
