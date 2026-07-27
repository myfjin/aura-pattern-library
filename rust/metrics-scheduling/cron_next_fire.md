# cron next fire

**Language:** Rust · **Sphere:** rust · **Category:** metrics-scheduling

**Signature:** `(from_minute: u32, from_hour: u32) → (u32, u32)`

## What it does

cron_next_fire — parse simple cron expression; compute next fire time.

Core idea: parse "*/5 * * * *" (every 5 minutes) or similar, then compute the next
fire time from a given time. THE ONE LAW: plant a known current time and cron expr,
hand-compute the expected next fire, then assert the cron engine produces exactly that.
A missed fire or off-by-one interval would fail.
When to use: job scheduling, recurring task execution, cron-like systems.

## Guarantee

When it runs, cron next fire guarantees assert_eq!(next, (10, 5), "from 10:00, next fire should be 10:05"); assert_eq!(next, (10, 5), "from 10:04, next fire should be 10:05"); assert_eq!(next, (10, 10), "from 10:05, next fire should be 10:10") (weak-grade: proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(next, (10, 5), "from 10:00, next fire should be 10:05")`
- `assert_eq!(next, (10, 5), "from 10:04, next fire should be 10:05")`
- `assert_eq!(next, (10, 10), "from 10:05, next fire should be 10:10")`
- `assert_eq!(next, (0, 0), "from 23:59, next fire should wrap to 00:00")`
- `assert_eq!(next, (9, 0), "from 08:00, next fire should be 09:00")`
- `assert_eq!(next, (9, 30), "from 09:05, next fire should be 09:30")`
- `assert_eq!(next, (15, 0), "from 09:30, next fire should be 15:00")`
- `assert!(next_total > current_total, "next fire must be strictly after current")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
