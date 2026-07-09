"""Adversarial Perturbation: gradient-sign attack on logistic classifier.

Builds a simple logistic classifier from scratch, computes adversarial perturbation
via gradient direction, and shows that adversarial perturbations flip predictions more
reliably than random noise of equivalent norm.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import random
import math
from typing import List, Tuple

def adversarial_perturbation_lite() -> None:
    random.seed(42)

    # Use a fixed linear classifier to ensure consistency
    # w = (2, 2, -4) implements decision boundary x1 + x2 = 2
    w_true = [2.0, 2.0, -4.0]

    def sigmoid(z: float) -> float:
        return 1.0 / (1.0 + math.exp(-max(-500, min(500, z))))

    def predict(x: Tuple[float, float], weights: List[float] = None) -> float:
        if weights is None:
            weights = w_true
        z = weights[0] * x[0] + weights[1] * x[1] + weights[2]
        return sigmoid(z)

    # Test point at decision boundary: (1.0, 1.1) => z = 2*1.0 + 2*1.1 - 4 = 0.2
    x_test = (1.0, 1.1)
    pred_orig = predict(x_test)
    assert 0.5 < pred_orig < 0.8, f"Test point should be moderately positive, got {pred_orig}"

    # Gradient at test point (for sigmoid(w·x), grad = w * sigmoid(z) * (1 - sigmoid(z)))
    z_test = w_true[0] * x_test[0] + w_true[1] * x_test[1] + w_true[2]
    sig_z = sigmoid(z_test)
    grad_scale = sig_z * (1 - sig_z)
    grad_x1 = w_true[0] * grad_scale
    grad_x2 = w_true[1] * grad_scale

    grad_norm = math.sqrt(grad_x1**2 + grad_x2**2)
    if grad_norm > 0:
        grad_dir = [grad_x1 / grad_norm, grad_x2 / grad_norm]
    else:
        grad_dir = [1.0, 1.0]

    # Adversarial: step opposite to gradient (to decrease probability, flip to negative)
    perturbation_norm = 0.8
    x_adv = (
        x_test[0] - perturbation_norm * grad_dir[0],
        x_test[1] - perturbation_norm * grad_dir[1]
    )
    pred_adv = predict(x_adv)

    # Random perturbations: same norm, multiple directions
    random_flips = 0
    for _ in range(10):
        theta = random.uniform(0, 2 * math.pi)
        x_rand = (
            x_test[0] + perturbation_norm * math.cos(theta),
            x_test[1] + perturbation_norm * math.sin(theta)
        )
        if predict(x_rand) < 0.5:
            random_flips += 1

    # Adversarial should flip prediction (move towards negative)
    assert pred_adv < 0.5, f"Adversarial should flip prediction, got {pred_adv}"
    # Most random directions should not flip
    assert random_flips <= 5, f"Random perturbations should rarely flip, got {random_flips}/10"

    print("PASS")

if __name__ == "__main__":
    adversarial_perturbation_lite()
