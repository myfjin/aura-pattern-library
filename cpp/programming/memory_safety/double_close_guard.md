# double_close_guard

**Pattern:** double_close_guard

**Why you would reach for this:** An explicit `close()` plus a destructor that also closes is two releases for one acquisition. Each looks correct on its own; together they are fatal. This pattern is the rule that a handle must record that it has been released, so the destructor is a no-op after an explicit close — release must be idempotent.

**Entry fn:** `void HandleGood::close()` — frees the handle and nulls it, so the destructor becomes a no-op.

**Valid input:** A handle owning a 16-int block (`1..16`) that is explicitly closed and then destroyed. The handle must record the release so the destructor does not free the same block again.

**Core:** The unsafe arm's `close()` frees the block but does not null the pointer, so the destructor frees the same block again — a double-free. The safe arm's `close()` frees the block and sets the pointer to `nullptr`, and the destructor only frees if the pointer is non-null; after an explicit close the destructor is a no-op. Recording the release is the mechanism — release must be idempotent, so the destructor does not double-free after an explicit close.

**Assert:** The planted truth is that the idempotent close sums to `EXPECT_SUM = 136` and releases exactly once. Real SUCCESS line from the evidence file:
```
PASS: idempotent close summed 136 released once and the double-free was caught as attempting double-free
```

**⚠️ Defect it prevents:** The disaster is both `close()` and the destructor freeing the same block — a double-free. Real FAILURE line from the evidence file:
```
==1431091==ERROR: AddressSanitizer: attempting double-free on 0x506000000020 in thread T0:
```
