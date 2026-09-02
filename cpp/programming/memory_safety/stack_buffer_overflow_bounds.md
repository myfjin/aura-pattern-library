# stack_buffer_overflow_bounds

**Pattern:** stack_buffer_overflow_bounds

**Why you would reach for this:** A stack array's size is known to the compiler, which is why the classic overflow is written through a pointer passed to another function — where the size is gone and only the caller's promise remains. That promise is the bug. This pattern is the rule that a function which writes through a pointer must be given the buffer's length and must bound itself by it.

**Entry fn:** `int fill_safe(int* p, int n, int cap)` — a fill that takes the capacity and bounds itself by it.

**Valid input:** An 8-element stack buffer (`BUF_N = 8`) passed to a fill that is asked to write 12 elements. The fill must bound itself by the buffer's capacity.

**Core:** A stack array's size is known to the compiler, but a pointer passed to another function loses the array bound — only the caller's promise remains, and that promise is the bug. The unsafe arm passes an 8-element buffer to `fill(buf, 12)`, which writes 12 elements into it — a stack-buffer-overflow. The safe arm's `fill_safe` takes the capacity and bounds itself by it, writing only `min(n, cap)` elements. Passing the length and bounding by it is the mechanism — the buffer's size does not travel with the pointer.

**Assert:** The planted truth is that the bounded fill writes `BUF_N = 8` elements summing to `EXPECT_SUM = 36`. Real SUCCESS line from the evidence file:
```
PASS: bounded fill wrote 8 summed 36 and the stack overrun was caught as stack-buffer-overflow
```

**⚠️ Defect it prevents:** The disaster is writing 12 elements into an 8-element stack buffer being a stack-buffer-overflow. Real FAILURE line from the evidence file:
```
==1569612==ERROR: AddressSanitizer: stack-buffer-overflow on address 0x7fff06b56200 at pc 0x5a324ff08679 bp 0x7fff06b56180 sp 0x7fff06b56170
```
