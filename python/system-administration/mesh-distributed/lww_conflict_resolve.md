# lww conflict resolve

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 20 · Mesh / distributed coordination

**Signature:** `(key: str, value: str, timestamp: int) → ?`

## What it does

Last-Write-Wins (LWW) Conflict Resolution Pattern
When replicas diverge (partition), use Lamport clock to resolve.
Higher timestamp wins, lower is discarded.
Assert: both replicas converge to same value after merge.

## Guarantee

When it runs, lww conflict resolve guarantees store_a.data['x'].value == 20; store_a.data['x'].timestamp == 2; store_a.data['x'].value == 30 (proven by run).

**Checkable constraints:**

- `store_a.data['x'].value == 20`
- `store_a.data['x'].timestamp == 2`
- `ts_b > ts_a`
- `store_a.data['x'].value == 30`
- `store_a.data['x'].timestamp == ts_b`
- `store_a.data['x'].value == store_b.data['x'].value`
- `store.data['x'].value == 'value3'`
- `store.data['x'].value == 'value3'`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
