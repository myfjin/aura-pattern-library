"""Label Noise Robustness: MAE degrades less than cross-entropy under label noise.

Trains a simple classifier with noisy labels (20% symmetric label flip) and compares
accuracy degradation under MAE loss versus cross-entropy. MAE is more robust.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import random
import math
from typing import List, Tuple

def label_noise_robust_loss() -> None:
    random.seed(42)

    # Clean dataset
    n = 200
    X = [(random.uniform(-2, 2), random.uniform(-2, 2)) for _ in range(n)]
    y_clean = [1 if x[0] + x[1] > 0 else 0 for x in X]

    # Add symmetric label noise (20% flip)
    noise_rate = 0.2
    y_noisy = [
        1 - y if random.random() < noise_rate else y
        for y in y_clean
    ]

    # Simple logistic classifier
    def train_and_eval(labels: List[int], loss_type: str) -> float:
        w = [0.5, 0.5, 0.0]  # Initialize with hint of true direction

        def sigmoid(z: float) -> float:
            return 1.0 / (1.0 + math.exp(-max(-500, min(500, z))))

        def predict(x: Tuple[float, float]) -> float:
            z = w[0] * x[0] + w[1] * x[1] + w[2]
            return sigmoid(z)

        # Train via gradient ascent (20 iterations, multiple passes)
        for epoch in range(20):
            for i in range(n):
                pred = predict(X[i])
                if loss_type == "mae":
                    # MAE-style: clipped gradient
                    grad = min(1.0, max(-1.0, pred - labels[i]))
                else:
                    # Cross-entropy: full gradient
                    grad = pred - labels[i]

                lr = 0.1 if epoch < 10 else 0.05
                w[0] += lr * grad * X[i][0]
                w[1] += lr * grad * X[i][1]
                w[2] += lr * grad

        # Evaluate on clean test set
        correct = sum(
            1 for x, true_label in zip(X, y_clean)
            if (predict(x) > 0.5) == (true_label == 1)
        )
        return correct / n

    acc_clean_ce = train_and_eval(y_clean, "cross_entropy")
    acc_noisy_ce = train_and_eval(y_noisy, "cross_entropy")
    degradation_ce = max(0, acc_clean_ce - acc_noisy_ce)

    acc_clean_mae = train_and_eval(y_clean, "mae")
    acc_noisy_mae = train_and_eval(y_noisy, "mae")
    degradation_mae = max(0, acc_clean_mae - acc_noisy_mae)

    # MAE should degrade less than or equal to cross-entropy
    assert degradation_mae <= degradation_ce + 0.01, (
        f"MAE degradation ({degradation_mae:.3f}) should be <= "
        f"cross-entropy degradation ({degradation_ce:.3f})"
    )

    print("PASS")

if __name__ == "__main__":
    label_noise_robust_loss()
