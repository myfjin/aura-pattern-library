# hdr latency lite

**Language:** Rust · **Sphere:** rust · **Category:** metrics-scheduling

**Signature:** `(v: u64) → usize`

## What it does

hdr_latency_lite — HDR-style latency histogram; percentiles within a BOUNDED relative error.

Core idea: a High-Dynamic-Range histogram keeps `SUB` linear sub-buckets inside every
power-of-two octave, so it covers 1µs..1s cheaply while bounding the relative error of any
recorded value to ~1/SUB — the whole point of HDR (an order-of-magnitude bucketer cannot).
THE ONE LAW: record a Pareto-ish latency distribution, then assert the bucketed p50/p99 are
within a TIGHT relative error of the exact sorted percentiles — a coarse or off-by-one bucket
mapping would blow past the bound. When to use: SLO tail-latency tracking, p99 dashboards.

## Guarantee

When it runs, hdr latency lite guarantees assert_eq!(hist.count(), 10_000, "every sample must be recorded once") (proven by rustc-run).

**Checkable constraints:**

- `assert!(err < 0.12, "p{p} error {:.1}% exceeds 12% (exact={exact}µs, hdr={got}µs)", err * 100.0)`
- `assert!(p50 < p99, "p50 must be below p99")`
- `assert_eq!(hist.count(), 10_000, "every sample must be recorded once")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
