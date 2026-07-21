"""
Pairwise Ranking via Logistic Regression.

Learn item ordering from pairwise comparisons: for each pair (i,j),
fit logistic regression on feature difference (f_i - f_j) to predict which ranks higher.
Verify on planted item order: learned model should recover the order
with high Kendall tau correlation vs truth.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
from typing import List, Tuple




class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_sigmoid(x):
    v = []
    if isinstance(x, (int, float)) and not math.isfinite(x):
        v.append(f"AURA-E008: x must be finite, got {x}")
    if v:
        raise AuraInputError(v)

def sigmoid(x: float) -> float:
    """Sigmoid: 1 / (1 + exp(-x))."""
    _aura_validate_sigmoid(x)
    return 1.0 / (1.0 + math.exp(-x))


def fit_logistic_pairwise(
    items: List[str],
    features: List[float],
    true_order: List[str],
) -> Tuple[float, float]:
    """
    Fit logistic regression on pairwise differences.
    For each pair (i,j) where true_order[i] < true_order[j], we have
    a training example: feature_diff = features[i] - features[j], label = 1 (i ranks higher).
    Returns (learned_weight, learned_bias) for score = weight * feature_diff + bias.
    """
    item_to_idx = {item: idx for idx, item in enumerate(items)}
    true_ranks = {item: rank for rank, item in enumerate(true_order)}

    # Generate pairwise examples
    examples = []
    for i, item_i in enumerate(items):
        for j, item_j in enumerate(items):
            if i != j:
                # Label: 1 if item_i ranks higher than item_j in true order
                label = 1 if true_ranks[item_i] < true_ranks[item_j] else 0
                feat_diff = features[i] - features[j]
                examples.append((feat_diff, label))

    # Fit via gradient descent
    weight, bias = 0.0, 0.0
    for epoch in range(50):
        grad_w, grad_b = 0.0, 0.0
        for feat_diff, label in examples:
            pred = sigmoid(weight * feat_diff + bias)
            error = pred - label
            grad_w += error * feat_diff
            grad_b += error
        weight -= 0.01 * grad_w / len(examples)
        bias -= 0.01 * grad_b / len(examples)

    return weight, bias


def kendall_tau(ranking1: List[str], ranking2: List[str]) -> float:
    """
    Kendall tau: correlation between two rankings.
    Number of concordant pairs / total pairs.
    """
    n = len(ranking1)
    rank1 = {item: i for i, item in enumerate(ranking1)}
    rank2 = {item: i for i, item in enumerate(ranking2)}

    concordant = 0
    for i in range(n):
        for j in range(i + 1, n):
            item_i, item_j = ranking1[i], ranking1[j]
            order1 = rank1[item_i] < rank1[item_j]
            order2 = rank2[item_i] < rank2[item_j]
            if order1 == order2:
                concordant += 1

    total_pairs = n * (n - 1) / 2
    return 2 * concordant / total_pairs - 1  # Normalized to [-1, 1]


if __name__ == "__main__":
    # Plant true item order and features that correlate with rank
    items = ["A", "B", "C", "D", "E"]
    true_order = ["A", "B", "C", "D", "E"]

    # Features: A > B > C > D > E (with noise)
    features = [5.0, 4.2, 3.1, 2.0, 1.0]

    # Fit logistic model
    weight, bias = fit_logistic_pairwise(items, features, true_order)

    # Predict ranking via learned model
    scores = [weight * feat + bias for feat in features]
    predicted_order = sorted(items, key=lambda item: scores[items.index(item)], reverse=True)

    # Compute Kendall tau vs true order
    tau = kendall_tau(true_order, predicted_order)

    assert tau > 0.7, (
        f"Kendall tau {tau:.2f} should be > 0.7 for a learnable ranking"
    )
    assert predicted_order == true_order or tau > 0.5, (
        f"Predicted order {predicted_order} should match or correlate with "
        f"true {true_order} (tau={tau:.2f})"
    )

    print(
        f"True order: {true_order} | Predicted: {predicted_order} | "
        f"Weight={weight:.2f} | Bias={bias:.2f} | Kendall tau={tau:.2f} | PASS"
    )
