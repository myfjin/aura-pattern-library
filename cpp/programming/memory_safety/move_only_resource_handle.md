# move_only_resource_handle

**Pattern:** move_only_resource_handle

**Why you would reach for this:** Writing your own move constructor is the moment you take responsibility for the moved-from object. Copying the pointer out of the source is only half a move — the source still holds it, so both destructors run and the resource is released twice. This pattern is the rule that a move must neuter the source.

**Entry fn:** `HandleGood(HandleGood&& o) noexcept : p(o.p) { o.p = nullptr; }` — a move constructor that nulls the source.

**Valid input:** A resource handle owning a 16-int block (`1..16`) that is moved into another handle. After the move the source must be nulled so it releases nothing.

**Core:** The unsafe arm's move constructor copies the pointer out of the source but does not null it — both `a` and `b` hold the same pointer, so both destructors `delete[]` the same block, a double-free. The safe arm's move constructor copies the pointer and sets the source's pointer to `nullptr`, and the destructor only frees if the pointer is non-null; after the move the source releases nothing. Neuter-the-source is the mechanism — after a move the moved-from object must be destructible and release nothing.

**Assert:** The planted truth is that the neutered move sums to `EXPECT_SUM = 136`, releases exactly once, and leaves the source nulled. Real SUCCESS line from the evidence file:
```
PASS: neutered move summed 136 released once and the non-neutered double-free was caught as attempting double-free
```

**⚠️ Defect it prevents:** The disaster is both destructors freeing the same block because the source was not neutered — a double-free. Real FAILURE line from the evidence file:
```
==1435161==ERROR: AddressSanitizer: attempting double-free on 0x506000000020 in thread T0:
```
