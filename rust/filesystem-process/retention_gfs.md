# retention gfs

**Language:** Rust · **Sphere:** rust · **Category:** filesystem-process

**Signature:** `(dates: &[u32]) → Vec<u32>`

## What it does

retention_gfs — grandfather-father-son retention over a synthetic date set; keeps exactly.

Core idea: keep the most recent snapshot in each period bucket (daily within 7 days, weekly
within 4 weeks, monthly within 12 months); everything else is pruned. THE ONE LAW: apply GFS
retention, then assert the kept set equals — EXACTLY — an independently computed expected set
(newest-per-bucket-within-window), not merely a loose count. A drop or duplicate would diverge.
When to use: backup rotation, snapshot retention, tiered archival.

## Guarantee

When it runs, retention gfs guarantees assert_eq!(retained, expected, "GFS kept set must match the independent expected set exactly"); assert_eq!(gfs_retain(&weekly), expected_gfs(&weekly), "sparse set must also match exactly") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(retained, expected, "GFS kept set must match the independent expected set exactly")`
- `assert!(retained.contains(&d), "recent day {d} must be retained by the daily rule")`
- `assert!(retained.len() < 40 && retained.len() > 15, "365→{} is the expected reduction", retained.len())`
- `assert!(w[1] > w[0], "retained dates must be strictly increasing (no dups)")`
- `assert!(retained.iter().all(|&d| d < 365), "every retained date is a real snapshot")`
- `assert_eq!(gfs_retain(&weekly), expected_gfs(&weekly), "sparse set must also match exactly")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
