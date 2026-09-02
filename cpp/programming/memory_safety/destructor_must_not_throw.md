# destructor_must_not_throw

**Pattern:** destructor_must_not_throw

**Why you would reach for this:** During stack unwinding an exception is already in flight, and a second one leaving a destructor gives the runtime no choice but `std::terminate`. This is why destructors are implicitly `noexcept`. This pattern is the rule for a destructor that must not let an exception escape — it must swallow-and-log or handle internally.

**Entry fn:** `~Good()` — a destructor that catches and swallows any exception it triggers internally.

**Valid input:** A destructor that runs during stack unwinding (here, three `Good` objects destroyed while a primary exception propagates). The destructor must not let an exception escape; it must handle the throw internally.

**Core:** When an exception is already propagating, a second exception leaving a destructor during unwinding calls `std::terminate` — the runtime cannot handle two exceptions in flight. The unsafe arm's `Bad` destructor is `noexcept(false)` and throws; during unwinding it aborts the process. The safe arm's `Good` destructor wraps its throwing code in a try/catch and swallows it internally, so unwinding completes normally. Swallowing-and-handling internally is the mechanism — a destructor must never let an exception escape.

**Assert:** The planted truth is that all three `Good` destructors run during unwinding, each swallowing internally, for `EXPECT_RELEASES = 3`. Real SUCCESS line from the evidence file:
```
PASS: 3 destructors swallowed internally and the throwing destructor was caught as terminate called
```

**⚠️ Defect it prevents:** The disaster is the child aborting with `std::terminate` during stack unwinding. Real FAILURE line from the evidence file:
```
terminate called: the runtime terminated the process
```

> **Portability note.** `terminate called ...` is libstdc++'s wording; libc++ (macOS, and any clang/libc++ build) prints `libc++abi: terminating due to ...` instead, so the named signature never appeared on half the toolchains. The pattern now installs a `std::set_terminate` handler that prints the signature itself and then aborts, so the same line is observed everywhere. The handler runs before the runtime's default message, which is therefore no longer emitted.
