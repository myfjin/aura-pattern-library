# orphan detect

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 15 · Process/system introspection

**Signature:** `(process_lines: str) → ?`

## What it does

orphan_detect: Identify orphaned processes (parent pid doesn't exist).
THE ONE LAW: Parse tree, identify orphans by ppid not in known pids, return exact list.

## Guarantee

When it runs, orphan detect guarantees orphans == [100, 101]; broken_orphans == [100]; broken_orphans != orphans (weak-grade: directional, proven by run).

**Checkable constraints:**

- `orphans == [100, 101]`
- `broken_orphans == [100]`
- `broken_orphans != orphans`
- `len(orphans) == 2`
- `100 in orphans`
- `101 in orphans`
- `clean_orphans == []`
- `multi == [100, 101, 102]`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
