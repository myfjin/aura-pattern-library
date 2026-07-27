# confusion matrix metrics

**Language:** Python · **Sphere:** data-science · **Category:** Statistics & Testing

**Signature:** `(y_true: List[int], y_pred: List[int]) → Tuple[int, int, int, int]`

## Guarantee

When it runs, confusion matrix metrics guarantees tp == 3 and fp == 0 and (tn == 3) and (fn == 0); tp == 2 and fp == 2 and (tn == 1) and (fn == 1); prec == 1.0 and rec == 1.0 and (f1 == 1.0) (proven by run).

**Checkable constraints:**

- `tp == 3 and fp == 0 and (tn == 3) and (fn == 0)`
- `prec == 1.0 and rec == 1.0 and (f1 == 1.0)`
- `tp == 2 and fp == 2 and (tn == 1) and (fn == 1)`
- `0 < prec < 1`
- `0 < rec < 1`
- `0 < f1 < 1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def confusion_matrix(y_true: List[int], y_pred: List[int]) -> Tuple[int, int, int, int]:`, `def precision(tp: int, fp: int) -> float:`, `def recall(tp: int, fn: int) -> float:`, `def f1_score(precision_val: float, recall_val: float) -> float:`, `def accuracy(tp: int, tn: int, total: int) -> float:`
**Valid input:** `y_true` and `y_pred` are equal-length lists of binary labels (0 or 1); metric denominators are handled with zero-guard returns.
**Core:** Computes TP, FP, TN, FN for binary classification, then precision, recall, F1, and accuracy from those counts.
**Assert:** Perfect predictions yield (3, 0, 3, 0) and all metrics equal 1.0; a planted imperfect case yields the expected confusion counts and intermediate metric values between 0 and 1.
**✔ Retrofitted:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E retrofit pass; the current signed code reflects the fix.

---
*△ AURA Pattern Library — © Reality Optimizer*
