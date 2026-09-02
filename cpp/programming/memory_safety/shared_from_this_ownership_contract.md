# shared_from_this_ownership_contract

**Pattern:** shared_from_this_ownership_contract

**Why you would reach for this:** `enable_shared_from_this` lets an object hand out a `shared_ptr` to itself — but it works by holding a `weak_ptr` that only gets filled in when a `shared_ptr` first takes ownership. Call `shared_from_this()` on an object that no `shared_ptr` owns and it throws `bad_weak_ptr`. This pattern is the rule that `shared_from_this()` is only legal after a `shared_ptr` owns the object.

**Entry fn:** `auto self = sp->shared_from_this();` — called only after a `shared_ptr` owns the object.

**Valid input:** A `Node` (value `EXPECT = 4242`) that is owned by a `shared_ptr` before `shared_from_this()` is called. The precondition is about ownership, not about the object being alive.

**Core:** `shared_from_this()` works by holding a `weak_ptr` that is only filled in when a `shared_ptr` first takes ownership. The unsafe arm calls it on a plain stack local that no `shared_ptr` owns — the `weak_ptr` is empty, so it throws `bad_weak_ptr`, which goes uncaught and calls `std::terminate`. The safe arm creates the object with `make_shared` first, so the internal `weak_ptr` is filled and `shared_from_this()` returns a valid `shared_ptr`. Prior `shared_ptr` ownership is the mechanism — the precondition is about ownership, not about the object being alive.

**Assert:** The planted truth is that `shared_from_this()` returns the value `EXPECT = 4242` with `use_count 2`. Real SUCCESS line from the evidence file:
```
PASS: shared_from_this returned 4242 use_count 2 and the uncaught throw was caught as terminate called
```

**⚠️ Defect it prevents:** The disaster is calling `shared_from_this()` on a non-`shared_ptr`-owned object throwing `bad_weak_ptr`, which goes uncaught and calls `std::terminate`. Real FAILURE line from the evidence file:
```
terminate called: the runtime terminated the process
```

> **Portability note.** `terminate called ...` is libstdc++'s wording; libc++ (macOS, and any clang/libc++ build) prints `libc++abi: terminating due to ...` instead, so the named signature never appeared on half the toolchains. The pattern now installs a `std::set_terminate` handler that prints the signature itself and then aborts, so the same line is observed everywhere. The handler runs before the runtime's default message, which is therefore no longer emitted.
