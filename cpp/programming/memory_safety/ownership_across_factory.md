# ownership_across_factory

**Pattern:** ownership_across_factory

**Why you would reach for this:** A factory that returns a raw `T*` has no way to say whether the caller must delete it — the answer lives in a comment, and every early return in the caller is a chance to lose it. This pattern is the rule that a factory's return type is its ownership contract, and returning `unique_ptr<T>` moves that answer out of the documentation and into the type.

**Entry fn:** `std::unique_ptr<Res> make_owned()` — a factory returning `unique_ptr`, which enforces release on every path.

**Valid input:** A factory that allocates a `Res` (owning a 16-int buffer, `1..16`) and a caller that takes an early return. The factory must return an owning handle so the resource is released on every path.

**Core:** A factory returning a raw `T*` relies on every caller path to remember to delete — the unsafe arm's `do_leak` helper takes an early return and abandons the raw pointer, which becomes unreachable. The safe arm's factory returns `unique_ptr<Res>`; even with an early return, the `unique_ptr` releases on scope exit. The return type is the mechanism — `unique_ptr` enforces release on every path, moving the ownership answer out of comments and into the type.

**Assert:** The planted truth is that the `unique_ptr` factory sums to `EXPECT_SUM = 136` and destroys exactly 1 object. Real SUCCESS line from the evidence file:
```
PASS: unique_ptr factory summed 136 destroyed 1 and the raw-pointer leak was caught as detected memory leaks
```

**⚠️ Defect it prevents:** The disaster is the caller taking an early return and the raw pointer being abandoned — a memory leak. Real FAILURE line from the evidence file:
```
==1435181==ERROR: LeakSanitizer: detected memory leaks
```
