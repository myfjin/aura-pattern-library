# lockfile pid guard

**Language:** Rust · **Sphere:** rust · **Category:** filesystem-process

**Signature:** `(_pid: u32) → bool`

## What it does

lockfile_pid_guard — pidfile stale-lock detection LOGIC on fixtures; stale reclaimed, live respected.

Core idea: a pidfile guards mutual exclusion. Acquisition must RECLAIM a lock that is stale
(too old) or whose owner PID is dead, but RESPECT a lock that is young AND whose owner is
alive. THE ONE LAW: drive the guard against a planted liveness fixture (which PIDs are alive)
and planted ages, asserting each of the four cases resolves correctly — a guard that ignored
staleness OR liveness would mis-handle one. When to use: daemon guarding, mutual exclusion.
(Liveness is a planted set here, standing in for the real `/proc/<pid>` check, which lives in
an uncalled `apply()` per the SAFETY law — no real process is inspected in the gated demo.)

## Guarantee

When it runs, lockfile pid guard guarantees assert!(acquire(None, stale_after, &live).is_ok(), "free lock must be acquirable") (none-grade: proven by rustc-run).

**Checkable constraints:**

- `assert!(acquire(None, stale_after, &live).is_ok(), "free lock must be acquirable")`
- `assert!(r.is_err(), "a young, live lock must be respected")`
- `assert!(r.unwrap_err().contains("42"), "error should name the holding pid")`
- `assert!(acquire(Some(&dead_owner), stale_after, &live).is_ok(), "dead owner → reclaim")`
- `assert!(acquire(Some(&stale), stale_after, &live).is_ok(), "stale lock → reclaim even if owner alive")`
- `assert!(acquire(Some(&boundary), stale_after, &live).is_err(), "age == threshold is not yet stale; live owner respected")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** none (no checkable constraint)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
