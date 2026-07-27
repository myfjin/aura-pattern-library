# job scheduler

**Language:** Python · **Sphere:** programming · **Category:** Performance

## What it does

A simple job scheduler with cron-like expressions.
Supports minute, hour, day of month, month, and day of week fields.

## Guarantee

When it runs, job scheduler guarantees got == expected; p._parse_field('*/15', 0, 59) == [0, 15, 30, 45]; p._parse_field('1-5', 0, 6) == [1, 2, 3, 4, 5] (proven by run).

**Checkable constraints:**

- `p._parse_field('*/15', 0, 59) == [0, 15, 30, 45]`
- `p._parse_field('1-5', 0, 6) == [1, 2, 3, 4, 5]`
- `p._parse_field('jan,jul', 1, 12) == [1, 7]`
- `p._parse_field('fri', 0, 6) == [5]`
- `got == expected`
- `{j.name for j in due} == {'t', 'boom'}`
- `ran == [1]`
- `not job.is_running and (not boom.is_running)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
