"""
Platt Scaling for Probability Calibration

Core idea: When a classifier outputs uncalibrated scores (overconfident), fit a logistic
function (Platt scaling) on a hold-out set to map scores to true probabilities.

When to use: You've trained a classifier and want to recalibrate its confidence scores to
match true conditional probabilities, improving Brier score and reliability diagrams.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import math
from typing import List, Tuple




class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_logistic(z):
    v = []
    if isinstance(z, (int, float)) and not math.isfinite(z):
        v.append(f"AURA-E008: z must be finite, got {z}")
    if v:
        raise AuraInputError(v)

def logistic(z: float) -> float:
    """Sigmoid function."""
    _aura_validate_logistic(z)
    return 1.0 / (1.0 + math.exp(-z))


def fit_platt_scaling(scores: List[float], labels: List[float], max_iter: int = 100) -> Tuple[float, float]:
    """
    Fit logistic recalibration: p = 1 / (1 + exp(-(a*score + b))).
    Simple coordinate ascent on log-likelihood.
    """
    a, b = 0.0, 0.0

    for iteration in range(max_iter):
        # Gradient steps
        grad_a = 0.0
        grad_b = 0.0

        for score, label in zip(scores, labels):
            z = a * score + b
            p = logistic(z)
            error = p - label
            grad_a += error * score
            grad_b += error

        # Update
        step_size = 0.01
        a -= step_size * grad_a / len(scores)
        b -= step_size * grad_b / len(scores)

    return a, b


def brier_score(y_true: List[float], y_pred: List[float]) -> float:
    """Brier score: mean squared error between predicted probabilities and binary labels."""
    return sum((y - yhat) ** 2 for y, yhat in zip(y_true, y_pred)) / len(y_true)


def calibration_error(y_true: List[float], y_pred: List[float], n_bins: int = 5) -> float:
    """Expected Calibration Error (ECE): average absolute difference between predicted and observed frequency per bin."""
    bins = [[] for _ in range(n_bins)]
    for y, yhat in zip(y_true, y_pred):
        bin_idx = min(int(yhat * n_bins), n_bins - 1)
        bins[bin_idx].append(y)

    errors = []
    for bin_preds in bins:
        if len(bin_preds) > 0:
            avg_pred = sum(bin_preds) / len(bin_preds)
            avg_true = sum(bin_preds) / len(bin_preds)
            errors.append(abs(avg_pred - avg_true))

    return sum(errors) / len(errors) if errors else 0.0


if __name__ == "__main__":
    random.seed(42)

    # Generate overconfident classifier scores and labels
    # Scores are extreme (near 0 or 1) but labels are uniform → poorly calibrated
    cal_scores = []
    cal_labels = []
    for _ in range(200):
        # Scores are extreme
        score = 0.95 if random.random() < 0.5 else 0.05
        # But labels are nearly uniform (roughly 50/50)
        label = 1 if random.random() < 0.4 else 0

        cal_scores.append(score)
        cal_labels.append(label)

    # Compute baseline (uncalibrated) Brier score
    baseline_brier = brier_score(cal_labels, cal_scores)

    # Fit Platt scaling
    a, b = fit_platt_scaling(cal_scores, cal_labels)

    # Calibrated predictions
    calibrated_preds = [logistic(a * s + b) for s in cal_scores]
    calibrated_brier = brier_score(cal_labels, calibrated_preds)

    print(f"Baseline Brier: {baseline_brier:.4f}")
    print(f"Calibrated Brier: {calibrated_brier:.4f}")
    print(f"Improvement: {(baseline_brier - calibrated_brier) / baseline_brier * 100:.1f}%")

    # Assertion: calibration should improve Brier score
    assert baseline_brier > calibrated_brier, f"Calibration should reduce Brier: {baseline_brier} vs {calibrated_brier}"
    assert calibrated_brier < 0.25, f"Calibrated Brier should be reasonable: {calibrated_brier}"

    print("✓ Platt Scaling Calibration: PASS")
