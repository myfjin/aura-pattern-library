# double_release_on_error_path

**Pattern:** double_release_on_error_path

**Why you would reach for this:** You added cleanup to the error path and forgot the success path already had it. The two paths are correct in isolation and fatal together — this bug survives code review because each `delete` looks right where it stands. This pattern is the rule that ownership must have exactly one release point.

**Entry fn:** `auto up = std::make_unique<int[]>(EXPECT_N);` — a single owning handle with exactly one release point.

**Valid input:** A block of 16 ints (each `1..16`) allocated and released on both a throwing and a success path. Ownership must be held by a single owner that releases exactly once on each path.

**Core:** The unsafe arm frees the block in the catch block and then frees it again in the trailing normal-path code — both paths are individually correct, but together they double-free the same block. The safe arm holds the block in a `std::unique_ptr`; on the throwing path the owner releases during unwinding, and on the success path it releases at scope exit — exactly one release per path. A single owning handle is the mechanism: ownership has exactly one release point, so the two paths cannot both free the same memory.

**Assert:** The planted truth is that the single owner releases once and the success path sums to `EXPECT_SUM = 136`. Real SUCCESS line from the evidence file:
```
PASS: single owner released once and success summed 136, double-free caught as attempting double-free
```

**⚠️ Defect it prevents:** The disaster is both the catch and the trailing code freeing the same block — a double-free. Real FAILURE line from the evidence file:
```
==1421896==ERROR: AddressSanitizer: attempting double-free on 0x506000000020 in thread T0:
```
