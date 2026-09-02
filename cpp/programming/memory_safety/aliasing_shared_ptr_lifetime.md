# aliasing_shared_ptr_lifetime

**Pattern:** aliasing_shared_ptr_lifetime

**Why you would reach for this:** You often want to hand out a pointer to one member of a shared object. A raw `&sp->m` says nothing about the whole object's lifetime — the owner dies and takes the member with it. This pattern is the rule for the aliasing constructor `shared_ptr<M>(owner, &owner->m)`, which gives you a pointer to the member that keeps the whole owner alive.

**Entry fn:** `std::shared_ptr<Part> alias(w, &w->p);` — the aliasing constructor, sharing the owner's control block while pointing at a sub-object.

**Valid input:** A `shared_ptr<Whole>` owning a `Whole` whose `Part` member holds a 16-int buffer (`1..16`). The alias must keep the whole owner alive while pointing at the member.

**Core:** A raw `&sp->m` says nothing about the whole object's lifetime — when the owner dies, the member dies with it, and the raw pointer reads freed memory. The unsafe arm caches `&w->p` and reads it after the owner releases. The safe arm uses the aliasing constructor `shared_ptr<Part>(w, &w->p)`, which shares the owner's control block while pointing at the sub-object; even after the original `w` is reset, the alias keeps the whole owner alive. The aliasing constructor is the mechanism — the member pointer is valid exactly as long as the alias exists.

**Assert:** The planted truth is that the aliasing `shared_ptr` keeps the owner alive, summing to `EXPECT_SUM = 136` with `use_count 1`. Real SUCCESS line from the evidence file:
```
PASS: aliasing shared_ptr kept owner alive summing 136 use_count 1 and raw member dangling was caught as heap-use-after-free
```

**⚠️ Defect it prevents:** The disaster is the raw member pointer reading freed memory after the owner releases — a heap-use-after-free. Real FAILURE line from the evidence file:
```
==1434637==ERROR: AddressSanitizer: heap-use-after-free on address 0x503000000050 at pc 0x5fc667538812 bp 0x7ffc707e2cc0 sp 0x7ffc707e2cb0
```
