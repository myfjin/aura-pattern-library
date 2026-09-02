# two_phase_init_failure_path

**Pattern:** two_phase_init_failure_path

**Why you would reach for this:** Two-phase init (constructor then `init()`) means an object can exist in a failed state. The dangerous version allocates, rolls back, and leaves the pointer looking valid — so a caller that ignores the failure return reads through a dangling pointer. This pattern is the rule that a failed `init()` must clear the pointer and record the failure, and callers must check the return value before any accessor.

**Entry fn:** `bool TwoPhaseSafe::init(bool succeed)` — an init that clears the pointer and records failure, plus a `sum()` accessor that refuses when `!ok`.

**Valid input:** A two-phase object whose `init(false)` must leave it refusing use, and whose `init(true)` must succeed with a 16-int buffer (`1..16`). The accessor must return a sentinel when the object is not `ok`.

**Core:** The unsafe arm's `init(false)` allocates, frees the buffer, but leaves `buf` pointing at the freed block and `n` looking valid — the caller ignores the failure return and reads through the dangling pointer. The safe arm's `init` clears `buf` to `nullptr`, zeroes `n`, and sets `ok = false` on failure, and the `sum()` accessor refuses when `!ok`. Clearing the pointer and recording the failure is the mechanism — a failed init must leave the object refusing use, and callers must check the return before any accessor.

**Assert:** The planted truth is that the safe accessor refuses after failed init and the success path sums to `EXPECT_SUM = 136`. Real SUCCESS line from the evidence file:
```
PASS: safe accessor refused after failed init and success summed 136, dangling was caught as heap-use-after-free
```

**⚠️ Defect it prevents:** The disaster is the caller ignoring the failure return and reading through the dangling pointer — a heap-use-after-free. Real FAILURE line from the evidence file:
```
==1432304==ERROR: AddressSanitizer: heap-use-after-free on address 0x506000000020 at pc 0x62c3380da7a8 bp 0x7fffebc1e2a0 sp 0x7fffebc1e290
```
