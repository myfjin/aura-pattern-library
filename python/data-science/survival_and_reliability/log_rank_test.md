# log rank test

**Language:** Python · **Sphere:** data-science · **Category:** Survival & Reliability

**Signature:** `(times_g1: List[float], events_g1: List[int], times_g2: List[float], events_g2: List[int]) → Tuple[float, float]`

## What it does

Log-rank test: nonparametric test for equality of survival curves.

Compares two groups via observed vs expected events under null hypothesis
(no group difference). Core claim: two different groups detected; identical
groups not flagged as different.

## Guarantee

When it runs, log rank test guarantees p_diff < 0.1; p_same > 0.1 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `p_diff < 0.1`
- `p_same > 0.1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **hard** — positive, xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def log_rank_test(times_g1: List[float], events_g1: List[int], times_g2: List[float], events_g2: List[int]) -> Tuple[float, float]:`
**Valid input:** Each group's `times` and `events` are equal-length; `events[i]` ∈ {0,1}; at least some events occur in each group.
**Core:** Nonparametric log-rank test comparing two survival curves. At each unique event time it computes observed vs expected events in group 1 under the null of equal hazards, accumulating a z-statistic and approximate two-tailed p-value.
**Assert:** Two groups with clearly different exponential hazards produce a p-value < 0.10; two independent samples from the same exponential distribution produce a p-value > 0.10.
**⚠️ Defect:** The variance formula uses the standard hypergeometric variance but assumes `y1 + y2 − 1 > 0`; it skips time points with zero variance without clear reporting. No validation that the groups have any events or that time/event lists are equal length. The p-value is a normal approximation, which can be anticonservative for very small samples.

---
*△ AURA Pattern Library — © Reality Optimizer*
