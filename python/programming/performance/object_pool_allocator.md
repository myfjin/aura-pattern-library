# object pool allocator

**Language:** Python · **Sphere:** programming · **Category:** Performance

## What it does

Thread-safe object pool for reusing expensive-to-create resources.

Manages a bounded pool of objects built by a factory and checked by a
validator: it prefills to min_size, hands out live objects (creating up to
max_size on demand), validates on acquire and return, reaps idle/invalid
objects, and blocks acquirers until one frees when the cap is reached. Use it
for connections or other costly handles. Guarantees (self-test oracle):
prefill count is exact, stock is reused without new creation, a request past
max_size times out, invalidation shrinks the pool, and idle objects past the
timeout are discarded and rebuilt fresh.

## Guarantee

When it runs, object pool allocator guarantees made['n'] == 2; pool.size() == 2 and pool.available() == 2; made['n'] == 2 (proven by run).

**Checkable constraints:**

- `made['n'] == 2`
- `pool.size() == 2 and pool.available() == 2`
- `id(po2.obj) in prefilled`
- `made['n'] == 2`
- `made['n'] == 4 and pool.size() == 4`
- `again.obj is freed.obj`
- `pool.size() == 3`
- `made['n'] == before`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
