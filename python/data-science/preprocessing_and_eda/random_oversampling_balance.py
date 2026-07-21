"""
Random Oversampling and Synthetic Minority Balance Pattern.

Rebalances imbalanced datasets by random oversampling (duplicate minority) and
SMOTE-lite (interpolate between minority neighbors). Core idea: majority class
stays fixed, minority class is augmented to match majority size via repetition
and interpolation.

When to use: imbalanced classification, oversampling minority before training,
creating synthetic samples without upsampling majority, class balance restoration.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Tuple
import random
import math


def random_oversample(
    X: List[List[float]], y: List[int]
) -> Tuple[List[List[float]], List[int]]:
    """
    Random oversampling: duplicate minority samples.
    Args:
        X: List of feature vectors
        y: List of labels (binary: 0 or 1)
    Returns:
        (X_resampled, y_resampled) with balanced classes
    """
    count_0 = sum(1 for label in y if label == 0)
    count_1 = sum(1 for label in y if label == 1)

    if count_0 == count_1:
        return X, y

    # Determine majority and minority
    if count_0 > count_1:
        minority_label = 1
        majority_count = count_0
    else:
        minority_label = 0
        majority_count = count_1

    X_resampled = list(X)
    y_resampled = list(y)

    # Find minority indices
    minority_indices = [i for i, label in enumerate(y) if label == minority_label]

    # Oversample: randomly duplicate minority until balanced
    while sum(1 for label in y_resampled if label == minority_label) < majority_count:
        idx = random.choice(minority_indices)
        X_resampled.append(X[idx][:])  # Copy feature vector
        y_resampled.append(minority_label)

    return X_resampled, y_resampled




class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_smote_lite(k, alpha_range):
    v = []
    if isinstance(k, (int, float)) and k <= 0:
        v.append(f"AURA-E009: k must be > 0, got {k}")
    if isinstance(alpha_range, (int, float)) and not math.isfinite(alpha_range):
        v.append(f"AURA-E008: alpha_range must be finite, got {alpha_range}")
    if isinstance(alpha_range, (int, float)) and alpha_range <= 0:
        v.append(f"AURA-E009: alpha_range must be > 0, got {alpha_range}")
    if v:
        raise AuraInputError(v)

def smote_lite(
    X: List[List[float]], y: List[int], k: int = 3, alpha_range: Tuple[float, float] = (0.0, 1.0)
) -> Tuple[List[List[float]], List[int]]:
    """
    SMOTE-lite: create synthetic samples by interpolating between minority neighbors.
    Args:
        X: List of feature vectors
        y: List of labels
        k: Number of nearest neighbors to consider
        alpha_range: Interpolation range (0, 1) for convex combination
    Returns:
        (X_synthetic, y_synthetic) with new synthetic samples added
    """
    _aura_validate_smote_lite(k, alpha_range)
    count_0 = sum(1 for label in y if label == 0)
    count_1 = sum(1 for label in y if label == 1)

    if count_0 == count_1:
        return X, y

    # Determine minority
    if count_0 > count_1:
        minority_label = 1
        majority_count = count_0
    else:
        minority_label = 0
        majority_count = count_1

    minority_indices = [i for i, label in enumerate(y) if label == minority_label]
    n_minority = len(minority_indices)

    X_synthetic = list(X)
    y_synthetic = list(y)

    # Generate synthetic samples
    n_to_generate = majority_count - n_minority

    for _ in range(n_to_generate):
        # Pick random minority sample
        idx1 = random.choice(minority_indices)
        x1 = X[idx1]

        # Pick random neighbor (or any minority sample as approximation)
        idx2 = random.choice(minority_indices)
        x2 = X[idx2]

        # Interpolate
        alpha = random.uniform(alpha_range[0], alpha_range[1])
        x_synthetic = [x1[j] + alpha * (x2[j] - x1[j]) for j in range(len(x1))]

        X_synthetic.append(x_synthetic)
        y_synthetic.append(minority_label)

    return X_synthetic, y_synthetic


if __name__ == "__main__":
    random.seed(42)

    # Synthetic imbalanced dataset: 100 class 0, 20 class 1
    n0 = 100
    n1 = 20

    X = [[random.gauss(0, 1) for _ in range(5)] for _ in range(n0)]
    X.extend([[random.gauss(5, 1) for _ in range(5)] for _ in range(n1)])

    y = [0] * n0 + [1] * n1

    # Test random oversampling
    X_over, y_over = random_oversample(X, y)

    count0_before = sum(1 for label in y if label == 0)
    count1_before = sum(1 for label in y if label == 1)

    count0_after = sum(1 for label in y_over if label == 0)
    count1_after = sum(1 for label in y_over if label == 1)

    # Verify classes are balanced after random oversampling
    assert count0_after == count1_after, f"Classes not balanced: {count0_after} vs {count1_after}"

    # Verify majority class size unchanged
    assert count0_after == count0_before, f"Majority class size changed"

    # Verify minority class expanded
    assert count1_after > count1_before, "Minority class not expanded"

    # Test SMOTE-lite
    X_smote, y_smote = smote_lite(X, y, k=3)

    count0_smote = sum(1 for label in y_smote if label == 0)
    count1_smote = sum(1 for label in y_smote if label == 1)

    assert count0_smote == count1_smote, f"SMOTE: Classes not balanced: {count0_smote} vs {count1_smote}"
    assert count0_smote == count0_before, "SMOTE: Majority class size changed"
    assert len(X_smote) > len(X), "SMOTE: No synthetic samples generated"

    print("random_oversampling_balance.py: PASS")
