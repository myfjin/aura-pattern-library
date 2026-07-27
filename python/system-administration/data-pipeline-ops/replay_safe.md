# replay safe

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 19 · Data pipeline ops

**Signature:** `(records: List[dict], state_path: str) → ?`

## What it does

Replay-Safe Pattern
Guarantee that replaying operations produces identical output.
Assert: first run and replay produce same result, idempotency holds.
Key: operations must be commutative and state-independent within a batch.

## Guarantee

When it runs, replay safe guarantees state1['sum'] == 65; state1['count'] == 4; state1['max'] == 30 (proven by run).

**Checkable constraints:**

- `state1['sum'] == 65`
- `state1['count'] == 4`
- `state1['max'] == 30`
- `state1['min'] == 5`
- `state1 == state2`
- `state2['sum'] == 65`
- `state2['count'] == 4`
- `state2['max'] == 30`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def replay_safe_aggregate(records, state_path):`
**Valid input:** `records` is a list of dicts with `'id'` and `'value'`; `state_path` is a writable JSON path.
**Core:** Recomputes aggregate statistics (sum, count, max, min) from the full input set every call and overwrites the state file, making the aggregate commutative and replay-safe.
**Assert:** First run and replay with identical input produce identical aggregates; reordering the same records also produces identical aggregates.
**⚠️ Defect:** The function ignores any previously persisted state and recomputes from scratch, which is correct for commutativity but wastes work for incremental streams. It does not handle missing/None values or non-numeric inputs. The initial `state` dict loaded from disk is immediately discarded, so partial crash recovery of incremental state is impossible.

---
*△ AURA Pattern Library — © Reality Optimizer*
