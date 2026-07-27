# histogram quantile

**Language:** Rust · **Sphere:** rust · **Category:** metrics-scheduling

**Signature:** `(q: f64) → f64`

## What it does

histogram_quantile — bucketed histogram; quantile within tolerance of exact.

Core idea: log-scale buckets hold sample counts; approximate quantile is computed
by scanning buckets. THE ONE LAW: plant a known distribution into the histogram,
compute the quantile from exact sorted data, then assert the bucketed quantile
is within a tolerance (relative error). A broken bucket boundary or skipped bucket
would produce a quantile outside tolerance.
When to use: latency histograms, percentile-based SLOs, scalable quantile estimation.

## Guarantee

When it runs, histogram quantile guarantees assert_eq!(hist.count(), 1000, "histogram count must match input sample count") (proven by rustc-run).

**Checkable constraints:**

- `assert!(error_p50 < 0.2, "p50 quantile error {:.2}% exceeds 20% tolerance (exact={}, hist={})", error_p50 * 100.0, exact_p50, hist_p50)`
- `assert!(error_p99 < 0.2, "p99 quantile error {:.2}% exceeds 20% tolerance (exact={}, hist={})", error_p99 * 100.0, exact_p99, hist_p99)`
- `assert_eq!(hist.count(), 1000, "histogram count must match input sample count")`
- `assert!(q1 <= q2, "quantiles must be monotonic in q")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
