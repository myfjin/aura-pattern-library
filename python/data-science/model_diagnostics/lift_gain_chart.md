# lift gain chart

**Language:** Python · **Sphere:** data-science · **Category:** Model Diagnostics

**Signature:** `(scores: List[float], labels: List[int], n_deciles: int) → Tuple[List[float], List[float], List[float]]`

## What it does

Lift & Gain Chart

Computes cumulative gain (% of positives captured) and lift (gain / base rate) by decile.
Lift > 1 indicates the model is better than random.

Use this in marketing/targeting to quantify how much better a model ranks customers than random.

## Guarantee

When it runs, lift gain chart guarantees lifts_strong[0] > 1.5; 0.7 < avg_lift_random < 1.3; gains_strong[0] > gains_random[0] (weak-grade: directional, proven by run).

**Checkable constraints:**

- `lifts_strong[0] > 1.5`
- `0.7 < avg_lift_random < 1.3`
- `gains_strong[0] > gains_random[0]`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `lift_gain_chart(scores, labels, n_deciles=10) → (decile_percentages, gains, lifts)`
**Valid input:** `scores: List[float]` — predicted scores. `labels: List[int]` — 0 or 1. `n_deciles ≥ 1`.
**Core:** Compute cumulative gain (% of positives captured) and lift (positive rate / base rate) by decile. Sort by score descending. Strong classifier (signal_strength=0.8) should have high lift in top decile. Random classifier (signal_strength=0) should have lift ≈ 1 throughout.
**Assert:** On 100 positives + 400 negatives: strong classifier top decile lift > 1.5, random classifier average lift within [0.7, 1.3], strong gain > random gain at top decile.
**✔ Retrofitted:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E retrofit pass; the current signed code reflects the fix.

---
*△ AURA Pattern Library — © Reality Optimizer*
