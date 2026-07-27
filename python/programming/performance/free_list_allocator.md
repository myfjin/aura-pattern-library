# free list allocator

**Language:** Python · **Sphere:** programming · **Category:** Performance

## What it does

Best-fit free-list memory allocator over a fixed arena.

Models allocate/free with exact address arithmetic: allocations carve from a
sorted free list using best-fit, over-sized blocks are split, and freed blocks
are coalesced with adjacent free neighbours. Use it to reason about
fragmentation and allocation policy without a real allocator.
Guarantees (self-test oracle): exact addresses, best-fit picks the tightest
hole, a request larger than any single hole is refused even when total free
space would suffice (the fragmentation disaster), and freeing everything
coalesces back to one block of the original size.

## Guarantee

When it runs, free list allocator guarantees a.allocate(200) == 100; a.allocate(50) == 300; blocks == 2 and free_mem == 850 (proven by run).

**Checkable constraints:**

- `a.allocate(100) == 0`
- `a.allocate(200) == 100`
- `a.allocate(50) == 300`
- `a.free(100) is True`
- `blocks == 2 and free_mem == 850`
- `abs(frag - 200.0 / 850.0) < 1e-12`
- `addr == 100`
- `blocks == 2 and free_mem == 700`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
