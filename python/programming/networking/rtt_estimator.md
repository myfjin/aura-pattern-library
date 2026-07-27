# rtt estimator

**Language:** Python · **Sphere:** programming · **Category:** Networking

**Signature:** `(base_rtt: float, jitter: float, count: int) → List[float]`

## What it does

Round-trip time estimator module with EWMA smoothing and timeout calculation.

## Guarantee

When it runs, rtt estimator guarantees abs(est.get_rtt_estimate() - 0.1) < 1e-12; abs(est.get_jitter() - 0.05) < 1e-12; abs(est.get_timeout() - 0.3) < 1e-12 (proven by run).

**Checkable constraints:**

- `est.get_rtt_estimate() is None and est.get_jitter() is None`
- `est.get_timeout() == 1.0`
- `abs(est.get_rtt_estimate() - 0.1) < 1e-12`
- `abs(est.get_jitter() - 0.05) < 1e-12`
- `abs(est.get_timeout() - 0.3) < 1e-12`
- `abs(est.get_rtt_estimate() - 0.15) < 1e-12`
- `abs(est.get_jitter() - 0.075) < 1e-12`
- `abs(est.get_timeout() - 0.45) < 1e-12`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
