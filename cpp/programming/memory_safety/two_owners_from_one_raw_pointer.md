# two_owners_from_one_raw_pointer

**Pattern:** two_owners_from_one_raw_pointer

**Why you would reach for this:** `shared_ptr` counts references to a control block, not to an address. Constructing two `shared_ptr`s from the same raw pointer creates two independent control blocks, each convinced it is the only owner, each with a count of one — and both free it. This pattern is the rule that ownership is established once, at the point of allocation.

**Entry fn:** `std::shared_ptr<int[]> b = a;` — sharing the same control block by copy, not by re-wrapping the raw pointer.

**Valid input:** A 16-int block (`1..16`) owned by a `shared_ptr`. A second `shared_ptr` must be created by copying the first, so both share one control block.

**Core:** `shared_ptr` counts references to a control block, not to an address. The unsafe arm constructs two `shared_ptr`s from the same raw pointer, creating two independent control blocks each with a count of one; when both are destroyed, each frees the same block — a double-free. The safe arm creates the second `shared_ptr` by copying the first, so both share one control block with a count of two. Ownership established once is the mechanism — a raw pointer already given to a `shared_ptr` must never be given to another.

**Assert:** The planted truth is that the shared control block sums to `EXPECT_SUM = 136` with `use_count 2` then `1`. Real SUCCESS line from the evidence file:
```
PASS: shared control block summed 136 use_count 2 then 1 and the double-ownership was caught as attempting double-free
```

**⚠️ Defect it prevents:** The disaster is both `shared_ptr`s freeing the same block when their counts hit zero — a double-free. Real FAILURE line from the evidence file:
```
==1435669==ERROR: AddressSanitizer: attempting double-free on 0x506000000020 in thread T0:
```
