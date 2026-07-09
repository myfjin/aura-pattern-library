"""Mutual information for feature selection.

Core idea: compute entropy and mutual information between discrete features and
a label, then rank features by MI. Informative features have higher MI than noise.

When to use: for feature importance ranking in classification or regression,
especially with discrete/categorical data.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
import random
from typing import Dict, List, Tuple
from collections import Counter


def entropy(values: List[int]) -> float:
    """Compute Shannon entropy of a discrete distribution."""
    counts = Counter(values)
    total = len(values)
    return -sum((count / total) * math.log2(count / total) for count in counts.values() if count > 0)


def mutual_information(feature: List[int], label: List[int]) -> float:
    """
    Compute mutual information between feature and label.
    I(X;Y) = H(Y) - H(Y|X)
    """
    # H(Y)
    h_label = entropy(label)

    # H(Y|X) = sum_x P(X=x) * H(Y|X=x)
    feature_values = set(feature)
    h_label_given_feature = 0.0
    total = len(label)

    for fval in feature_values:
        # Labels where feature == fval
        subset_labels = [label[i] for i in range(len(feature)) if feature[i] == fval]
        if subset_labels:
            p_x = len(subset_labels) / total
            h_label_given_x = entropy(subset_labels)
            h_label_given_feature += p_x * h_label_given_x

    mi = h_label - h_label_given_feature
    return max(0.0, mi)  # Clamp to avoid numerical noise


if __name__ == "__main__":
    random.seed(42)

    n_samples = 200

    # Synthetic data: 4 features, 1 label
    # Feature 0 (informative): strongly correlated with label
    # Feature 1 (informative): weakly correlated with label
    # Feature 2 (noise): independent of label
    # Feature 3 (noise): independent of label

    label = [random.randint(0, 1) for _ in range(n_samples)]

    # Feature 0: highly informative (80% agreement with label)
    feature_0 = [label[i] if random.random() < 0.8 else 1 - label[i] for i in range(n_samples)]

    # Feature 1: weakly informative (60% agreement)
    feature_1 = [label[i] if random.random() < 0.6 else 1 - label[i] for i in range(n_samples)]

    # Feature 2,3: random noise (50% agreement, i.e., independent)
    feature_2 = [random.randint(0, 1) for _ in range(n_samples)]
    feature_3 = [random.randint(0, 1) for _ in range(n_samples)]

    # Compute MI for each feature
    mi_scores = {
        0: mutual_information(feature_0, label),
        1: mutual_information(feature_1, label),
        2: mutual_information(feature_2, label),
        3: mutual_information(feature_3, label),
    }

    # Rank by MI
    ranked = sorted(mi_scores.items(), key=lambda x: x[1], reverse=True)

    # Verify: informative features score higher than noise
    assert mi_scores[0] > mi_scores[2], \
        f"Feature 0 (informative, MI={mi_scores[0]:.4f}) should beat Feature 2 (noise, MI={mi_scores[2]:.4f})"
    assert mi_scores[1] > mi_scores[3], \
        f"Feature 1 (informative, MI={mi_scores[1]:.4f}) should beat Feature 3 (noise, MI={mi_scores[3]:.4f})"

    print(f"mutual_information_feature_selection.py: top_feature={ranked[0][0]}, mi={ranked[0][1]:.4f} PASS")
