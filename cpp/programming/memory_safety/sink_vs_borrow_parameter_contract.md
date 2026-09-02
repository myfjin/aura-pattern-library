# sink_vs_borrow_parameter_contract

**Pattern:** sink_vs_borrow_parameter_contract

**Why you would reach for this:** A function taking `unique_ptr` by value is a sink — it consumes the object. One taking a raw pointer or reference is a borrower. Calling a sink while holding a borrowed pointer means the sink destroys what you are still pointing at. This pattern is the rule that the parameter type IS the ownership contract — read it before you call.

**Entry fn:** `long borrow(const int* p, size_t n)` — a borrower that reads without taking ownership.

**Valid input:** A `unique_ptr<int[]>` owning 16 ints (`1..16`) whose data you want to read. The call must be a borrow (raw pointer), not a sink, so the owner survives.

**Core:** A function taking `unique_ptr` by value is a sink — it consumes and destroys the object at the end. The unsafe arm keeps a raw `borrowed` pointer to the owner's data, then passes the owner to a sink; the sink destroys the object, and the borrowed pointer reads freed memory. The safe arm calls a borrower that takes a raw pointer and does not take ownership, so the owner stays alive. The parameter type is the mechanism — it is the ownership contract, and reading it before the call prevents the sink from destroying what you still hold.

**Assert:** The planted truth is that the borrow preserves the owner, summing to `EXPECT_SUM = 136` both through the borrow and afterward. Real SUCCESS line from the evidence file:
```
PASS: borrow preserved owner summing 136 and the sink dangling was caught as heap-use-after-free
```

**⚠️ Defect it prevents:** The disaster is the sink destroying the object while a borrowed pointer still points at it — a heap-use-after-free. Real FAILURE line from the evidence file:
```
==1432209==ERROR: AddressSanitizer: heap-use-after-free on address 0x506000000020 at pc 0x59d628244a5f bp 0x7fff1f9a72c0 sp 0x7fff1f9a72b0
```
