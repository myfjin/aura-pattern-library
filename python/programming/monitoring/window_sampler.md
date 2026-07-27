# window sampler

**Language:** Python · **Sphere:** programming · **Category:** Monitoring

**Signature:** `() → None`

## What it does

Anomaly Detection Sampler Module

This module provides classes for detecting anomalies in time-series data using
statistical methods with adaptive baselines and windowed sampling.

## Guarantee

When it runs, window sampler guarantees sampler.is_full() and sampler.size() == 5; sum(sampler.get_values()) == 20; z == 3.0 (proven by run).

**Checkable constraints:**

- `sampler.get_values() == [2, 3, 4, 5, 6]`
- `sampler.is_full() and sampler.size() == 5`
- `sum(sampler.get_values()) == 20`
- `z == 3.0`
- `is_anom`
- `mean == 10.0`
- `std == 30.0`
- `not is_anom and z == 0.0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
