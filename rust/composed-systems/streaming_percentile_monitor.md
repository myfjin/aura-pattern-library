# streaming percentile monitor

**Language:** Rust · **Sphere:** rust · **Category:** composed-systems

**Signature:** `(p: usize) → Option<usize>`

## What it does

composes: parse-metric-samples + bounded-histogram-sketch + alert-on-threshold-cross

## Guarantee

When it runs, streaming percentile monitor guarantees assert_eq!(alerts.len(), 1, "Should have exactly 1 alert") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(alerts.len(), 1, "Should have exactly 1 alert")`
- `assert!(alerts[0].contains("P95"), "Alert should be for P95")`
- `assert!(histogram.percentile(50).is_some(), "Percentile computed")`
- `assert!(histogram.buckets.len() > 0, "Histogram has data")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
