# event bus

**Language:** Python · **Sphere:** programming · **Category:** Architecture

## What it does

Event Bus with Typed Channels

A lightweight event bus implementation supporting typed channels, asynchronous
delivery, and type-safe message passing.

## Guarantee

When it runs, event bus guarantees sum(received['i']) == 100; received['s1'] == [f'Hello {i}' for i in range(5)]; received['s2'] == received['s1'] (proven by run).

**Checkable constraints:**

- `received['s1'] == [f'Hello {i}' for i in range(5)]`
- `received['s2'] == received['s1']`
- `received['i'] == [0, 10, 20, 30, 40]`
- `sum(received['i']) == 100`
- `received['d'] == [{'id': 0}, {'id': 1}, {'id': 2}]`
- `not any((isinstance(x, int) for x in received['s1']))`
- `received['s1'][-1] == 'after-unsub'`
- `'after-unsub' not in received['s2']`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
