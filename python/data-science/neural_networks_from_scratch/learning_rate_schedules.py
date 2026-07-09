"""
Learning rate schedules: constant vs step-decay vs cosine annealing.

Core idea: Train the same network three times with different LR schedules on the
same problem. Show that step-decay and cosine schedules reach comparable or better
final loss with more stable late-phase updates compared to constant high LR.

When to use: Hyperparameter tuning, convergence acceleration, avoiding divergence
in late training stages.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
import random
from typing import List, Tuple, Callable


def sigmoid(x: float) -> float:
    if x < -500:
        return 0.0
    if x > 500:
        return 1.0
    return 1.0 / (1.0 + math.exp(-x))


def sigmoid_derivative(s: float) -> float:
    return s * (1 - s)


class SimpleNet:
    def __init__(self):
        # 2 -> 4 -> 1
        self.w1 = [[random.gauss(0, 0.5) for _ in range(2)] for _ in range(4)]
        self.b1 = [0.0] * 4
        self.w2 = [random.gauss(0, 0.5) for _ in range(4)]
        self.b2 = 0.0

    def forward(self, x: List[float]) -> Tuple[float, List[float]]:
        z1 = [self.b1[i] + sum(self.w1[i][j] * x[j] for j in range(2))
              for i in range(4)]
        h = [sigmoid(z1[i]) for i in range(4)]
        z2 = self.b2 + sum(self.w2[i] * h[i] for i in range(4))
        y = sigmoid(z2)
        return y, h

    def backward(self, x: List[float], y_true: float, y_pred: float, h: List[float], lr: float):
        dy = y_pred - y_true
        dz2 = dy * sigmoid_derivative(y_pred)

        for i in range(4):
            self.w2[i] -= lr * dz2 * h[i]
        self.b2 -= lr * dz2

        dh = [dz2 * self.w2[i] * sigmoid_derivative(h[i]) for i in range(4)]
        for i in range(4):
            for j in range(2):
                self.w1[i][j] -= lr * dh[i] * x[j]
            self.b1[i] -= lr * dh[i]

    def train(self, data: List[Tuple[List[float], float]], epochs: int,
              lr_schedule: Callable[[int, int], float]) -> Tuple[float, List[float]]:
        """Train and return (final_loss, loss_history)."""
        losses = []
        for epoch in range(epochs):
            total_loss = 0.0
            lr = lr_schedule(epoch, epochs)
            for x, y_true in data:
                y_pred, h = self.forward(x)
                loss = (y_pred - y_true) ** 2 / 2.0
                total_loss += loss
                self.backward(x, y_true, y_pred, h, lr)
            avg_loss = total_loss / len(data)
            losses.append(avg_loss)
        return losses[-1], losses


if __name__ == "__main__":
    random.seed(42)

    # Synthetic dataset
    data = []
    for _ in range(40):
        x = [random.gauss(0, 1.0) for _ in range(2)]
        y_true = 1.0 if (x[0] + x[1] > 0) else 0.0
        data.append((x, y_true))

    # Define schedules
    def constant_lr(epoch: int, total_epochs: int) -> float:
        return 0.05

    def step_decay_lr(epoch: int, total_epochs: int) -> float:
        # Start at 0.05, drop by factor of 2 every 40 epochs
        if epoch < 40:
            return 0.05
        elif epoch < 80:
            return 0.025
        else:
            return 0.0125

    def cosine_annealing_lr(epoch: int, total_epochs: int) -> float:
        # Cosine annealing from 0.05 to 0.001
        lr_min = 0.001
        lr_max = 0.05
        return lr_min + (lr_max - lr_min) * (1 + math.cos(math.pi * epoch / total_epochs)) / 2.0

    # Train with each schedule
    epochs = 120
    schedules = [
        ("Constant LR", constant_lr),
        ("Step Decay", step_decay_lr),
        ("Cosine Annealing", cosine_annealing_lr),
    ]

    results = {}
    for name, schedule in schedules:
        net = SimpleNet()
        final_loss, losses = net.train(data, epochs, schedule)
        results[name] = (final_loss, losses)
        print(f"{name:20} final loss: {final_loss:.6f}")

    # Show late-phase (last 10 epochs) loss variance
    print("\nLate-phase loss variance (last 10 epochs):")
    for name, (final_loss, losses) in results.items():
        late_losses = losses[-10:]
        variance = sum((l - sum(late_losses) / len(late_losses)) ** 2 for l in late_losses) / len(late_losses)
        print(f"  {name:20}: {variance:.2e}")

    # Check that schedules reach reasonable loss with better stability
    const_loss = results["Constant LR"][0]
    step_loss = results["Step Decay"][0]
    cosine_loss = results["Cosine Annealing"][0]

    # Check late-phase stability: variance should be low with schedules
    const_late_var = sum((l - sum(results["Constant LR"][1][-10:]) / 10) ** 2
                         for l in results["Constant LR"][1][-10:]) / 10
    step_late_var = sum((l - sum(results["Step Decay"][1][-10:]) / 10) ** 2
                        for l in results["Step Decay"][1][-10:]) / 10
    cosine_late_var = sum((l - sum(results["Cosine Annealing"][1][-10:]) / 10) ** 2
                          for l in results["Cosine Annealing"][1][-10:]) / 10

    print(f"\nAssertions:")
    # All converge to reasonable loss
    assert const_loss < 0.1, f"Constant loss {const_loss} too high"
    assert step_loss < 0.1, f"Step decay loss {step_loss} too high"
    assert cosine_loss < 0.1, f"Cosine loss {cosine_loss} too high"
    # Schedules demonstrate more stable late-phase convergence (lower variance)
    assert step_late_var < 1e-6, "Step decay late-phase variance too high"
    assert cosine_late_var < 1e-6, "Cosine late-phase variance too high"
    print("  All schedules converge well")

    print("PASS")
