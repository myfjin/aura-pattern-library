# reference_to_temporary_in_loop

**Pattern:** reference_to_temporary_in_loop

**Why you would reach for this:** You wrote `const T& r = make().get();` and assumed the reference keeps the temporary alive. It does not — lifetime extension applies to the temporary itself, not to something reached through it, so the temporary is destroyed at the end of the full expression and `r` dangles. This pattern is the rule for holding the object by value instead of binding a reference to a member of a temporary.

**Entry fn:** `Box owned = make();` — holding the returned object by value so it lives until the end of scope.

**Valid input:** A `Box` returned from `make()` whose `std::string` member (80 chars of `'y'`) you want to read. The object must be held by value, not reached through a reference bound to a temporary.

**Core:** A `const&` bound to a member of a temporary does not extend the temporary's lifetime — lifetime extension applies to the temporary object itself, not to something reached through it. The unsafe arm binds `const std::string& r = make().get()`; the temporary `Box` is destroyed at the end of the full expression, leaving `r` pointing at freed memory. The safe arm holds the whole `Box` by value, so the object and its member live until the end of scope. Holding the object by value is the mechanism — a reference into a destroyed temporary is freed memory.

**Assert:** The planted truth is that the value-held copy sums to `EXPECT_SUM = 9680` over the 80 chars. Real SUCCESS line from the evidence file:
```
PASS: value-held copy summed 9680 and the dangling temporary reference was caught as heap-use-after-free
```

**⚠️ Defect it prevents:** The disaster is the reference reading the destroyed temporary's memory — a heap-use-after-free. Real FAILURE line from the evidence file:
```
==1422140==ERROR: AddressSanitizer: heap-use-after-free on address 0x508000000020 at pc 0x56f86d9c6ae7 bp 0x7ffe46222510 sp 0x7ffe46222500
```
This pattern is built at `-O0` and reports `heap-use-after-free`; at `-O1` or higher the same bug surfaces as `stack-use-after-scope`, because the compiler keeps the pointer in a register and the dangling stack slot faults before the heap read is reached.

> **Signature note.** AddressSanitizer's own report alternates with optimisation level: `heap-use-after-free` at `-O0`, `stack-use-after-scope` at `-O1+`, because the temporary's storage is promoted. Same bug either way. The pattern's portable ledger reports `heap-use-after-free` at every level and that is what the parent matches on, so the named signature in this doc is stable across builds.
