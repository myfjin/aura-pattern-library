# proc stat cpu

**Language:** Rust · **Sphere:** rust · **Category:** filesystem-process

**Signature:** `(line: &str) → Option<Self>`

## What it does

proc_stat_cpu — parse two /proc/stat fixtures → CPU% delta; matches hand math.

Core idea: parse /proc/stat lines to extract CPU ticks (user, system, etc.), compute
the delta between two snapshots, and calculate the percentage. THE ONE LAW: plant
two known /proc/stat snapshots, parse both, compute CPU% from hand math, assert
the parser produces the same result.
When to use: system monitoring, CPU usage tracking, performance analysis.

## Guarantee

When it runs, proc stat cpu guarantees assert_eq!(snap1.user, 10); assert_eq!(snap1.system, 20); assert_eq!(snap1.idle, 100) (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(snap1.user, 10)`
- `assert_eq!(snap1.system, 20)`
- `assert_eq!(snap1.idle, 100)`
- `assert_eq!(snap1.iowait, 5)`
- `assert_eq!(snap1.total_ticks(), 135)`
- `assert_eq!(snap1.busy_ticks(), 30)`
- `assert_eq!(snap2.user, 50)`
- `assert_eq!(snap2.system, 70)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
