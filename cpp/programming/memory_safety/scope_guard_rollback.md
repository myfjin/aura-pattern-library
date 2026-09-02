# scope_guard_rollback

**Pattern:** scope_guard_rollback

**Why you would reach for this:** You acquired something, and the commit step three lines later can throw. A manual `delete` at the end does not run on the throwing path, so the resource leaks. This pattern is the rule for a scope guard that makes the rollback automatic — it releases on any exit path unless explicitly dismissed.

**Entry fn:** `ScopeGuard guard(res);` — a guard that releases the resource at scope exit unless `dismiss()` is called.

**Valid input:** A block of 64 ints (`0..63`) acquired before a commit step that may throw. The guard must release it on the throwing path and be dismissed on the success path.

**Core:** The unsafe arm allocates a raw block and then throws before the trailing `delete[]` is reached — the manual cleanup never runs on the throwing path. The safe arm wraps the block in a `ScopeGuard` whose destructor releases it unless dismissed; on the throwing path the guard is still active and releases at scope exit, while on the success path `dismiss()` keeps the resource alive. A scope guard is the mechanism — it releases on any exit path unless explicitly dismissed.

**Assert:** The planted truth is that the guard releases on throw and is dismissed on success, with the success path summing to `EXPECT_SUM = 2016`. Real SUCCESS line from the evidence file:
```
PASS: scope guard released on throw and dismissed on success summing 2016, leak caught as detected memory leaks
```

**⚠️ Defect it prevents:** The disaster is the manual `delete` never being reached because the throw bypasses it — a memory leak. Real FAILURE line from the evidence file:
```
==1431446==ERROR: LeakSanitizer: detected memory leaks
```
