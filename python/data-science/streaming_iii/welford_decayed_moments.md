# welford decayed moments

**Language:** Python · **Sphere:** data-science · **Category:** Streaming III

**Signature:** `(stream: list, decay: float) → Tuple[float, float]`

## What it does

Exponentially-decayed streaming mean/variance (Welford-style, decay-weighted).
Core idea: maintain a decay-weighted running mean and M2 so recent samples dominate. On a
stream whose level shifts, the decayed mean tracks the RECENT level while the plain global
mean lags halfway between old and new. The demo plants a clean level shift and asserts the
decayed mean recovers the post-shift level -- and beats the global mean at it.
When: track mean/variance on non-stationary streams (concept drift, regime change).

## Guarantee

When it runs, welford decayed moments guarantees abs(decayed_mean - recent_level) < 1.0; abs(decayed_mean - recent_level) < abs(global_mean - recent_level) - 3.0; decayed_var < 4.0 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `abs(decayed_mean - recent_level) < 1.0`
- `abs(decayed_mean - recent_level) < abs(global_mean - recent_level) - 3.0`
- `decayed_var < 4.0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
