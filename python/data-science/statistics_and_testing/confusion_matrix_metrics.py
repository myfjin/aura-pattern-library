"""
Confusion Matrix and Classification Metrics

Core idea: Build a confusion matrix (TP, FP, TN, FN) from binary predictions and true labels.
Compute precision (TP/(TP+FP)), recall (TP/(TP+FN)), F1 (harmonic mean), and accuracy.

When to use: Evaluate binary classification models, especially with imbalanced classes where
accuracy alone is misleading.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Tuple


def confusion_matrix(y_true: List[int], y_pred: List[int]) -> Tuple[int, int, int, int]:
    """
    Compute confusion matrix elements for binary classification.

    Args:
        y_true: True binary labels (0 or 1).
        y_pred: Predicted binary labels (0 or 1).

    Returns:
        Tuple of (TP, FP, TN, FN).
    """
    tp = sum(1 for i in range(len(y_true)) if y_true[i] == 1 and y_pred[i] == 1)
    fp = sum(1 for i in range(len(y_true)) if y_true[i] == 0 and y_pred[i] == 1)
    tn = sum(1 for i in range(len(y_true)) if y_true[i] == 0 and y_pred[i] == 0)
    fn = sum(1 for i in range(len(y_true)) if y_true[i] == 1 and y_pred[i] == 0)
    return tp, fp, tn, fn


def precision(tp: int, fp: int) -> float:
    """Precision: TP / (TP + FP)."""
    denom = tp + fp
    return tp / denom if denom > 0 else 0.0


def recall(tp: int, fn: int) -> float:
    """Recall (Sensitivity): TP / (TP + FN)."""
    denom = tp + fn
    return tp / denom if denom > 0 else 0.0


def f1_score(precision_val: float, recall_val: float) -> float:
    """F1 score: 2 * (precision * recall) / (precision + recall)."""
    denom = precision_val + recall_val
    return 2 * (precision_val * recall_val) / denom if denom > 0 else 0.0


def accuracy(tp: int, tn: int, total: int) -> float:
    """Accuracy: (TP + TN) / total."""
    return (tp + tn) / total if total > 0 else 0.0


if __name__ == "__main__":
    # Scenario 1: Perfect predictions
    y_true_perfect = [1, 1, 0, 0, 1, 0]
    y_pred_perfect = [1, 1, 0, 0, 1, 0]
    tp, fp, tn, fn = confusion_matrix(y_true_perfect, y_pred_perfect)
    print(f"Perfect case: TP={tp}, FP={fp}, TN={tn}, FN={fn}")
    assert tp == 3 and fp == 0 and tn == 3 and fn == 0, "Perfect predictions should have no errors"

    prec = precision(tp, fp)
    rec = recall(tp, fn)
    f1 = f1_score(prec, rec)
    acc = accuracy(tp, tn, len(y_true_perfect))
    print(f"Perfect metrics: precision={prec:.3f}, recall={rec:.3f}, F1={f1:.3f}, accuracy={acc:.3f}")
    assert prec == 1.0 and rec == 1.0 and f1 == 1.0, "Perfect predictions should have perfect metrics"

    # Scenario 2: Imperfect predictions (2 false positives, 1 false negative)
    y_true_imperfect = [1, 1, 0, 0, 1, 0]
    y_pred_imperfect = [1, 0, 1, 0, 1, 1]  # 1 FN, 2 FP
    tp, fp, tn, fn = confusion_matrix(y_true_imperfect, y_pred_imperfect)
    print(f"Imperfect case: TP={tp}, FP={fp}, TN={tn}, FN={fn}")
    assert tp == 2 and fp == 2 and tn == 1 and fn == 1, "Confusion matrix mismatch"

    prec = precision(tp, fp)
    rec = recall(tp, fn)
    f1 = f1_score(prec, rec)
    acc = accuracy(tp, tn, len(y_true_imperfect))
    print(f"Imperfect metrics: precision={prec:.3f}, recall={rec:.3f}, F1={f1:.3f}, accuracy={acc:.3f}")
    assert 0 < prec < 1, "Precision should be between 0 and 1"
    assert 0 < rec < 1, "Recall should be between 0 and 1"
    assert 0 < f1 < 1, "F1 should be between 0 and 1"

    print("✓ Confusion matrix metrics PASSED")
