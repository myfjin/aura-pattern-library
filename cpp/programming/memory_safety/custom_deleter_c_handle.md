# custom_deleter_c_handle

**Pattern:** custom_deleter_c_handle

**Why you would reach for this:** C APIs hand back handles that need a specific release function. Wrapping one in a smart pointer only helps if the deleter actually calls it — a deleter that does nothing compiles, runs, and silently leaks every handle. This pattern is the rule that the custom deleter must call the C API's own release; the smart pointer guarantees when it runs, never what it does.

**Entry fn:** `std::unique_ptr<int, void(*)(int*)> p(h, deleter);` — a `unique_ptr` whose custom deleter calls `free`.

**Valid input:** A `malloc`'d block of 64 ints (`0..63`) wrapped in a `unique_ptr` with a custom deleter. The deleter must call the C API's own release function.

**Core:** The unsafe arm's deleter is a no-op — it compiles and runs but never calls `free`, so when the `unique_ptr` is reset the malloc'd block is abandoned and unreachable. The safe arm's deleter calls `free(q)`, so when the `unique_ptr` is destroyed the block is released. The smart pointer guarantees when the deleter runs, never what it does — the deleter must call the C API's own release.

**Assert:** The planted truth is that the deleter calls `free` and the block sums to `EXPECT_SUM = 2016`. Real SUCCESS line from the evidence file:
```
PASS: deleter called free summed 2016 and the no-op deleter leak was caught as detected memory leaks
```

**⚠️ Defect it prevents:** The disaster is the deleter not calling `free`, so the malloc'd block is abandoned and unreachable — a memory leak. Real FAILURE line from the evidence file:
```
==1434783==ERROR: LeakSanitizer: detected memory leaks
```
