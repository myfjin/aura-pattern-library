"""
2-Layer MLP trained by hand-derived backpropagation on XOR.

Core idea: Manually implement the forward pass (linear -> sigmoid), backward pass
(chain rule through sigmoid), and weight updates. Learn to solve XOR by driving
loss to near zero.

When to use: Understanding backpropagation mechanics, debugging autodiff systems,
verifying network training fundamentals.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
import random
from typing import List, Tuple


def sigmoid(x: float) -> float:
    if x < -500:
        return 0.0
    if x > 500:
        return 1.0
    return 1.0 / (1.0 + math.exp(-x))


def sigmoid_derivative(s: float) -> float:
    """Derivative of sigmoid w.r.t its input, given the output s."""
    return s * (1 - s)


class SimpleMLPBackprop:
    def __init__(self, hidden_dim: int = 4, lr: float = 1.0):
        self.hidden_dim = hidden_dim
        self.lr = lr

        # Layer 1: 2 -> hidden_dim
        self.w1: List[List[float]] = [
            [random.gauss(0, 0.5) for _ in range(2)]
            for _ in range(hidden_dim)
        ]
        self.b1: List[float] = [0.0] * hidden_dim

        # Layer 2: hidden_dim -> 1
        self.w2: List[float] = [random.gauss(0, 0.5) for _ in range(hidden_dim)]
        self.b2: float = 0.0

    def forward(self, x: List[float]) -> Tuple[float, List[float]]:
        """Forward pass. Returns (output, hidden_activations)."""
        # Hidden layer
        z1 = [self.b1[i] + sum(self.w1[i][j] * x[j] for j in range(2))
              for i in range(self.hidden_dim)]
        h = [sigmoid(z) for z in z1]

        # Output layer
        z2 = self.b2 + sum(self.w2[i] * h[i] for i in range(self.hidden_dim))
        y = sigmoid(z2)

        return y, h

    def backward(self, x: List[float], y_true: float, y_pred: float, h: List[float]):
        """Backward pass via chain rule."""
        # Output layer gradients
        dy = y_pred - y_true  # dL/dz2
        dw2 = [dy * h[i] for i in range(self.hidden_dim)]
        db2 = dy

        # Hidden layer gradients (chain rule)
        dh = [dy * self.w2[i] * sigmoid_derivative(h[i]) for i in range(self.hidden_dim)]

        dw1 = [[dh[i] * x[j] for j in range(2)] for i in range(self.hidden_dim)]
        db1 = dh

        # Update weights
        for i in range(self.hidden_dim):
            for j in range(2):
                self.w1[i][j] -= self.lr * dw1[i][j]
            self.b1[i] -= self.lr * db1[i]

        for i in range(self.hidden_dim):
            self.w2[i] -= self.lr * dw2[i]
        self.b2 -= self.lr * db2

    def train(self, data: List[Tuple[List[float], float]], epochs: int) -> float:
        """Train on data, return final loss."""
        for _ in range(epochs):
            total_loss = 0.0
            for x, y_true in data:
                y_pred, h = self.forward(x)
                loss = (y_pred - y_true) ** 2 / 2.0
                total_loss += loss
                self.backward(x, y_true, y_pred, h)

        return total_loss / len(data) if data else 0.0


if __name__ == "__main__":
    random.seed(42)

    # XOR dataset
    xor_data = [
        ([0.0, 0.0], 0.0),
        ([0.0, 1.0], 1.0),
        ([1.0, 0.0], 1.0),
        ([1.0, 1.0], 0.0),
    ]

    # Train
    net = SimpleMLPBackprop(hidden_dim=4, lr=1.0)
    final_loss = net.train(xor_data, epochs=500)

    # Evaluate
    print(f"Final loss: {final_loss:.6f}")
    for x, y_true in xor_data:
        y_pred, _ = net.forward(x)
        print(f"  Input {x} -> {y_pred:.4f} (target {y_true})")

    # Check XOR learned
    assert final_loss < 0.01, f"Loss {final_loss} not converged"
    for x, y_true in xor_data:
        y_pred, _ = net.forward(x)
        error = abs(y_pred - y_true)
        assert error < 0.2, f"Prediction error {error} for {x}"

    print("PASS")
