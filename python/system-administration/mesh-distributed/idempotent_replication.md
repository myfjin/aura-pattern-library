# idempotent replication

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 20 · Mesh / distributed coordination

**Signature:** `(write_id: str, key: str, value: int) → ?`

## What it does

Idempotent Replication Pattern
Replicate writes across replicas.
Crash mid-replication, resume.
Assert: each write applied exactly once (no duplicates).

## Guarantee

When it runs, idempotent replication guarantees replica.data['x'] == 30; replica2.data['x'] == 30; primary.data == replica.data (proven by run).

**Checkable constraints:**

- `primary.data == replica.data`
- `replica.applied_writes == {'w1'}`
- `replica.data == {'x': 10}`
- `replica.applied_writes == {'w1'}`
- `replica.applied_writes == {'w1', 'w2'}`
- `replica.applied_writes == {'w1', 'w2', 'w3', 'w4'}`
- `replica.data == primary.data`
- `replica.data == {'x': 100}`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — chaos (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
