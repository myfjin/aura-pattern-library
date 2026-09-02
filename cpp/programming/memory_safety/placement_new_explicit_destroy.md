# placement_new_explicit_destroy

**Pattern:** placement_new_explicit_destroy

**Why you would reach for this:** Placement new constructs an object in storage you already own, and it does not own that storage — so nothing will ever call the destructor for you. If the object owns anything (a buffer, a handle), forgetting the explicit `p->~T()` loses it silently. This pattern is the rule that every placement new is paired with exactly one explicit destructor call, run before the underlying storage is released.

**Entry fn:** `o->~Owner();` — the explicit destructor call, run before `free(st)`.

**Valid input:** An `Owner` (owning a 16-int buffer, `1..16`) constructed via placement new into `malloc`'d storage. The destructor must be called explicitly before the storage is freed.

**Core:** Placement new constructs an object in storage you already own and does not own that storage, so no destructor runs automatically. The unsafe arm constructs an `Owner` into `malloc`'d storage and frees the storage without calling `~Owner` — the owned array is orphaned and unreachable. The safe arm calls `o->~Owner()` explicitly before `free(st)`, releasing the owned buffer. The explicit destructor call is the mechanism — every placement new must be paired with exactly one explicit destroy before the storage is released.

**Assert:** The planted truth is that the explicit destroy sums to `EXPECT_SUM = 136` and destroys exactly 1 object. Real SUCCESS line from the evidence file:
```
PASS: explicit destroy summed 136 destroyed 1 and the orphaned placement was caught as detected memory leaks
```

**⚠️ Defect it prevents:** The disaster is the owned array being orphaned when the storage is freed without destroying the object — a memory leak. Real FAILURE line from the evidence file:
```
==1441015==ERROR: LeakSanitizer: detected memory leaks
```
