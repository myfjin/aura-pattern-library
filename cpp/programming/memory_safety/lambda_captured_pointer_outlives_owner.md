# lambda_captured_pointer_outlives_owner

**Pattern:** lambda_captured_pointer_outlives_owner

**Why you would reach for this:** You are storing a callback in a `std::function` that will outlive the scope that created it, and the lambda captured a local pointer. A raw pointer capture is a promise the creating scope cannot keep once the local is freed. This pattern is the rule for capturing an owning handle — a `shared_ptr` or a by-value copy — so the captured data lives as long as the callback.

**Entry fn:** `f = [sp]{ return *sp; };` — capturing a `std::shared_ptr<int>` by value inside the lambda.

**Valid input:** A heap-allocated `int` (here `EXPECT = 4242`) that the callback must still be able to read after the creating scope exits. The owning handle must be captured by value so the lambda holds its own reference.

**Core:** A lambda stored in a `std::function` outlives the scope that created it. If it captured a raw pointer, that pointer dangles the moment the local is freed — the unsafe arm captures `int* p`, deletes it, and then calls the stored function, which dereferences freed memory. The safe arm captures a `std::shared_ptr<int>` by value; the lambda's copy keeps the control block alive, so the pointee survives the scope exit. Capturing an owning handle by value is the mechanism — it extends the lifetime to match the callback's.

**Assert:** The planted truth is that calling the stored function after the creating scope exits returns `EXPECT = 4242`. Real SUCCESS line from the evidence file:
```
PASS: shared_ptr capture returned 4242 and the dangling lambda pointer was caught as heap-use-after-free
```

**⚠️ Defect it prevents:** The disaster is the lambda dereferencing a pointer whose owner was freed — a heap-use-after-free. Real FAILURE line from the evidence file:
```
==1421958==ERROR: AddressSanitizer: heap-use-after-free on address 0x502000000010 at pc 0x6113b2aa17c2 bp 0x7ffe002e1930 sp 0x7ffe002e1920
```
