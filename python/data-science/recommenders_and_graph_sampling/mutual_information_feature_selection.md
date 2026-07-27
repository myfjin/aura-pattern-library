# mutual information feature selection

**Language:** Python · **Sphere:** data-science · **Category:** Recommenders & Graph Sampling

**Signature:** `(values: List[int]) → float`

## What it does

Mutual information for feature selection.

Core idea: compute entropy and mutual information between discrete features and
a label, then rank features by MI. Informative features have higher MI than noise.

When to use: for feature importance ranking in classification or regression,
especially with discrete/categorical data.

## Guarantee

When it runs, mutual information feature selection guarantees mi_scores[0] > mi_scores[2]; mi_scores[1] > mi_scores[3] (weak-grade: directional, proven by run).

**Checkable constraints:**

- `mi_scores[0] > mi_scores[2]`
- `mi_scores[1] > mi_scores[3]`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def entropy(values: List[int]) -> float:`, `def mutual_information(feature: List[int], label: List[int]) -> float:`
**Valid input:** `feature` and `label` are equal-length lists of discrete integer class labels; at least one feature value and one label value.
**Core:** Ranks discrete features by mutual information with the target label. Computes `I(X;Y) = H(Y) - H(Y|X)` using frequency-based entropy; informative features score higher than noise.
**Assert:** A feature with 80% agreement with the label has higher MI than a random-noise feature; a feature with 60% agreement beats an independent noise feature.
**⚠️ Defect:** Only handles discrete integer features; continuous features must be binned externally. No smoothing is applied, so feature values that appear only once contribute zero conditional entropy and can inflate MI. No length-check between `feature` and `label`; silent truncation could occur if the caller passes mismatched lists.

---
*△ AURA Pattern Library — © Reality Optimizer*
