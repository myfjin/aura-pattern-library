"""
Calibration Curve & Brier Score

Evaluates classifier calibration by binning predicted probabilities and comparing
observed frequency vs predicted probability. Also computes Brier score (MSE of predictions).

Use this to detect overconfident models (predicted prob >> observed freq) or underconfident models.
A well-calibrated classifier has observed ≈ predicted across bins.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import math
from typing import List, Tuple


def generate_well_calibrated_data(n: int, seed: int) -> Tuple[List[float], List[int]]:
    """
    Generate synthetic data where predicted probabilities match true frequencies.
    P(y=1) is proportional to the score.
    """
    random.seed(seed)
    scores = []
    labels = []

    for _ in range(n):
        # Score between 0 and 1
        score = random.uniform(0, 1)
        # True label is 1 with probability = score (well-calibrated by design)
        label = 1 if random.random() < score else 0
        scores.append(score)
        labels.append(label)

    return scores, labels


def generate_overconfident_data(n: int, seed: int) -> Tuple[List[float], List[int]]:
    """Generate overconfident predictions (predicted prob >> observed freq)."""
    random.seed(seed)
    scores = []
    labels = []

    for _ in range(n):
        # Score heavily skewed toward extremes
        raw = random.random()
        if raw < 0.3:
            score = random.uniform(0, 0.2)
        elif raw < 0.7:
            score = random.uniform(0.4, 0.6)
        else:
            score = random.uniform(0.8, 1.0)

        # But actual labels are much more uniform
        label = 1 if random.random() < 0.5 else 0
        scores.append(score)
        labels.append(label)

    return scores, labels


def calibration_curve(
    scores: List[float], labels: List[int], n_bins: int = 5
) -> Tuple[List[float], List[float], List[float]]:
    """
    Compute calibration curve: bin scores, compute observed and predicted frequencies.
    Returns (bin_centers, predicted_probs, observed_freqs).
    """
    bins = []
    for i in range(n_bins):
        bins.append((i / n_bins, (i + 1) / n_bins))

    bin_centers = []
    predicted_probs = []
    observed_freqs = []

    for lo, hi in bins:
        indices = [i for i, s in enumerate(scores) if lo <= s < hi or (i == len(scores) - 1 and s == 1.0)]
        if len(indices) == 0:
            continue

        bin_centers.append((lo + hi) / 2)
        avg_score = sum(scores[i] for i in indices) / len(indices)
        predicted_probs.append(avg_score)

        avg_label = sum(labels[i] for i in indices) / len(indices)
        observed_freqs.append(avg_label)

    return bin_centers, predicted_probs, observed_freqs


def brier_score(scores: List[float], labels: List[int]) -> float:
    """Brier score: MSE between predicted probabilities and actual labels."""
    return sum((s - l) ** 2 for s, l in zip(scores, labels)) / len(scores)


def calibration_error(
    predicted_probs: List[float], observed_freqs: List[float]
) -> float:
    """Expected Calibration Error (ECE): mean |predicted - observed| across bins."""
    if len(predicted_probs) == 0:
        return 0.0
    return sum(abs(p - o) for p, o in zip(predicted_probs, observed_freqs)) / len(predicted_probs)


def test_calibration() -> None:
    """Test calibration: well-calibrated model should have low ECE, overconfident should be high."""
    random.seed(42)

    # Well-calibrated model
    scores_good, labels_good = generate_well_calibrated_data(500, seed=42)
    _, pred_good, obs_good = calibration_curve(scores_good, labels_good, n_bins=5)
    ece_good = calibration_error(pred_good, obs_good)
    brier_good = brier_score(scores_good, labels_good)

    # Overconfident model
    scores_bad, labels_bad = generate_overconfident_data(500, seed=42)
    _, pred_bad, obs_bad = calibration_curve(scores_bad, labels_bad, n_bins=5)
    ece_bad = calibration_error(pred_bad, obs_bad)
    brier_bad = brier_score(scores_bad, labels_bad)

    # Verify: well-calibrated should have lower ECE and lower Brier
    assert ece_good < ece_bad, f"Well-calibrated ECE should be lower: {ece_good} vs {ece_bad}"
    assert brier_good < brier_bad, f"Well-calibrated Brier should be lower: {brier_good} vs {brier_bad}"

    print("calibration_curve.py: PASS")


if __name__ == "__main__":
    test_calibration()
