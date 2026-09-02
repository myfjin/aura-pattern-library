# c_str_pointer_after_string_mutation

**Pattern:** c_str_pointer_after_string_mutation

**Why you would reach for this:** You are passing a `std::string`'s `c_str()` pointer into a C API, and somewhere in between the string gets mutated — appended to, resized, or otherwise grown. The pointer you cached is only valid until the next mutation, so you need a rule for when it is safe to keep using it. This pattern is the discipline of re-acquiring the pointer after every modification instead of trusting a stale one.

**Entry fn:** `const char* std::string::c_str() const` — re-acquired *after* the mutation, not before.

**Valid input:** A `std::string` that has already undergone its mutation (here, `s.append(100000, 'y')`), so the returned pointer points at the current, live buffer. The string must be heap-allocated (length ≥ 64) for the failure to be a real heap-use-after-free rather than a silent read of a small-buffer-optimized inline array.

**Core:** `c_str()` returns a pointer into the string's current internal buffer. Any mutation that grows the string may reallocate, freeing the old buffer and leaving the previously returned pointer dangling. The safe arm performs the mutation first and only then calls `c_str()`, guaranteeing the pointer refers to the live allocation. The unsafe arm captures `c_str()` before appending, so its pointer points at the freed old block. Re-acquiring after mutation is the whole mechanism — the pointer is a borrow, not a stable handle.

**Assert:** The planted truth is that the re-acquired pointer sums to `EXPECT_SUM = 9600` over the first 80 chars. Real SUCCESS line from the evidence file:
```
PASS: re-acquired c_str summed 9600 and the dangling c_str pointer was caught as heap-use-after-free
```

**⚠️ Defect it prevents:** The disaster is reading the freed old buffer after reallocation — a heap-use-after-free. Real FAILURE line from the evidence file:
```
==1421719==ERROR: AddressSanitizer: heap-use-after-free on address 0x508000000020 at pc 0x62e7aec2a83c bp 0x7ffc6e332960 sp 0x7ffc6e332950
```
