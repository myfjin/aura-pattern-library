# roc auc from scratch

**Language:** Python · **Sphere:** data-science · **Category:** Statistics & Testing

**Signature:** `(y_true: List[int], y_scores: List[float]) → List[Tuple[float, float]]`

## What it does

ROC Curve and AUC Computation

Core idea: For binary classification with probabilistic predictions, compute TPR (recall)
and FPR at various thresholds to build the ROC curve. AUC is the area under this curve,
computed via the Mann-Whitney U statistic (equivalent to the probability that a random
positive scores higher than a random negative).

When to use: Evaluate classifier quality across all decision thresholds, especially for
imbalanced data where AUC is more informative than accuracy.

## Guarantee

When it runs, roc auc from scratch guarantees abs(auc_perfect_rank - 1.0) < 0.01; abs(auc_perfect_trap - 1.0) < 0.01; 0.4 < auc_weak_rank < 1.0 (proven by run).

**Checkable constraints:**

- `abs(auc_perfect_rank - 1.0) < 0.01`
- `abs(auc_perfect_trap - 1.0) < 0.01`
- `0.4 < auc_weak_rank < 1.0`
- `0.4 < auc_weak_trap < 1.0`
- `0.75 <= auc_strong_rank <= 1.0`
- `0.75 <= auc_strong_trap <= 1.0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def roc_curve_points(y_true: List[int], y_scores: List[float]) -> List[Tuple[float, float]]:`, `def auc_from_ranks(y_true: List[int], y_scores: List[float]) -> float:`, `def auc_trapezoid(roc_points: List[Tuple[float, float]]) -> float:`
**Valid input:** `y_true` and `y_scores` are equal-length lists; `y_true` is binary.
**Core:** Computes ROC curve points (FPR, TPR) by sorting scores descending, then computes AUC either via the Mann-Whitney U rank statistic or the trapezoid rule over the ROC points.
**Assert:** Perfectly separable scores yield AUC ≈ 1 by both methods; weak and strong signal cases produce moderate/high AUC within expected ranges.
**⚠️ Defect:** `auc_from_ranks` uses a double loop, so it is O(n²) and impractical for large datasets. `roc_curve_points` does not include explicit threshold values in its output, and the degenerate cases (no positives or no negatives) return hardcoded `(0,0),(1,1)` or 0.5 without warning.

---
*△ AURA Pattern Library — © Reality Optimizer*
