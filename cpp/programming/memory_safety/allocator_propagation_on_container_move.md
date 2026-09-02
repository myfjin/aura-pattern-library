# allocator_propagation_on_container_move

**Pattern:** allocator_propagation_on_container_move

**Why you would reach for this:** A container with a stateful allocator cannot simply steal another's buffer on move-assignment: the buffer belongs to the source's arena, and the destination's arena has no way to free it. The `propagate_on_container_move_assignment` trait decides — steal the pointer, or copy the elements into your own memory. Get it wrong and the destination outlives the arena that owns its bytes. This pattern is the rule that when allocators do not propagate and do not compare equal, a move must copy.

**Entry fn:** `void Vec::move_safe(Vec& src)` — copies the elements into the destination's own arena when the arenas differ.

**Valid input:** A `Vec` of 4 ints (`1..4`) in one arena being moved into a `Vec` backed by a different arena. The destination must copy the elements into its own arena, not adopt the source's pointer.

**Core:** A buffer belongs to the arena that allocated it, and a different arena has no way to free it. The unsafe arm's `steal` adopts the source's pointer and keeps the source's arena reference; when the source arena is destroyed, the destination's buffer dangles. The safe arm's `move_safe` checks whether the arenas are equal — if they differ, it copies the elements into the destination's own arena. Copying when allocators differ is the mechanism — the destination must not outlive the arena that owns its bytes.

**Assert:** The planted truth is that the allocator-aware move copies into the destination arena, summing to `EXPECT_SUM = 10`. Real SUCCESS line from the evidence file:
```
PASS: allocator-aware move copied into destination arena summing 10 and the stolen buffer was caught as heap-use-after-free
```

**⚠️ Defect it prevents:** The disaster is the destination adopting the source's buffer, the source arena being destroyed, and the destination reading freed memory — a heap-use-after-free. Real FAILURE line from the evidence file:
```
==1434656==ERROR: AddressSanitizer: heap-use-after-free on address 0x521000000100 at pc 0x61cd4c8a992f bp 0x7ffc47c57670 sp 0x7ffc47c57660
```
