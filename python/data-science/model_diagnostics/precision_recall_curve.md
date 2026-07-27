# precision recall curve

**Language:** Python · **Sphere:** data-science · **Category:** Model Diagnostics

**Signature:** `(n_positive: int, n_negative: int, noise: float, seed: int) → List[Tuple[float, int]]`

## Guarantee

When it runs, precision recall curve guarantees ap_strong > 0.8; ap_weak < 0.6; ap_strong > ap_weak (weak-grade: directional, proven by run).

**Checkable constraints:**

- `ap_strong > 0.8`
- `ap_weak < 0.6`
- `ap_strong > ap_weak`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `compute_pr_curve(scores, labels, n_points=100) → (thresholds, precisions, recalls)`, `average_precision(recalls, precisions) → float`
**Valid input:** `scores: List[float]` — predicted scores. `labels: List[int]` — 0 or 1.
**Core:** Compute precision-recall curve by varying decision threshold. Strong classifier (scores at 0.7 for positives, 0.3 for negatives, noise=0.1) should have high AP. Weak classifier (random scores) should have AP near base rate.
**Assert:** On 50 positives + 50 negatives: strong classifier AP > 0.8, weak classifier AP < 0.6, strong AP > weak AP.
**✔ Retrofitted:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E retrofit pass; the current signed code reflects the fix.

---
*△ AURA Pattern Library — © Reality Optimizer*
