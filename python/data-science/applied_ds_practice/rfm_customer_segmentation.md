# rfm customer segmentation

**Language:** Python · **Sphere:** data-science · **Category:** Applied DS Practice

**Signature:** `(transactions: list[dict]) → dict[int, dict]`

## What it does

RFM customer segmentation: Recency, Frequency, Monetary.

Segment customers based on:
  - Recency: days since last purchase
  - Frequency: number of purchases
  - Monetary: total spend
RFM scores divide each metric into quartiles, then combine into segments
(e.g., "whale" = high on all three, "churned" = low on all).

Use: customer value analysis, retention targeting, marketing segmentation.

## Guarantee

When it runs, rfm customer segmentation guarantees avg_whale_freq > avg_churned_freq (weak-grade: directional, proven by run).

**Checkable constraints:**

- `len(segments['whale']) > 10`
- `len(segments['churned']) > 10`
- `avg_whale_freq > avg_churned_freq`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def compute_rfm_metrics(transactions: list[dict]) -> dict[int, dict]:`, `def quartile_score(values: list[float], recency_flag: bool = False) -> dict[float, int]:`, `def segment_from_rfm(r: int, f: int, m: int) -> str:`
**Valid input:** `transactions` are dicts with `user_id`, `purchase_date` (numeric), `amount`. At least one transaction.
**Core:** RFM segmentation: recency (days since last purchase), frequency (count), monetary (total spend). Each metric is mapped to quartile scores 1–4, with recency inverted so lower recency scores higher. Combined R, F, M scores produce segments such as "whale", "churned", "at_risk".
**Assert:** On planted archetypes (whales: frequent/recent/high spend; churned: old/low/low), the whale segment contains more than 10 customers, the churned segment contains more than 10, and whale average frequency exceeds churned average frequency.
**⚠️ Defect:** `quartile_score` builds quartile boundaries from `sorted(set(values))` — it removes duplicates before computing quartiles, so the boundaries reflect unique-value ranks rather than true count quartiles. A value repeated many times can be assigned to different score buckets across runs or relative to its actual percentile. The function also has no guard for empty input and uses arbitrary 1/2/3/4 cutoffs in `segment_from_rfm` that are not validated against business semantics.

---
*△ AURA Pattern Library — © Reality Optimizer*
