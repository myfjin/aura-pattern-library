# rw lock

**Language:** Python · **Sphere:** programming · **Category:** Performance

## What it does

Writer-preferring read-write lock with upgrade and downgrade.

Allows many concurrent readers or one exclusive writer, backed by a Condition;
pending writers block new readers to prevent writer starvation, a sole reader
may upgrade to a writer, and a writer may downgrade to a reader without fully
releasing. Use it to guard a resource read far more often than written. Guarantees
(self-test oracle): multiple readers hold the lock at the same instant, writers
are mutually exclusive (no lost increments under contention), no reader is ever
observed inside a write section, and upgrade is granted only to the sole reader.

## Guarantee

When it runs, rw lock guarantees barrier_ok[0] == 4; state['value'] == 1600; not state['overlap'] (proven by run).

**Checkable constraints:**

- `barrier_ok[0] == 4`
- `state['value'] == 1600`
- `not state['overlap']`
- `solo.upgrade() is True`
- `solo.upgrade() is False`
- `solo.upgrade() is True`
- `solo._readers == 1 and solo._writers == 0`
- `solo.upgrade() is True`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
