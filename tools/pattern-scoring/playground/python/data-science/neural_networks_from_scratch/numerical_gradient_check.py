"""
Verify analytic backprop gradients against finite-difference numerical gradients.

Core idea: Compute gradients both ways (backprop and numerical finite-difference)
on the same tiny network. Compare element-wise; if max relative error < 1e-4,
backprop is correct. Essential debugging pattern for any hand-rolled network.

When to use: Verifying custom backprop implementations, debugging gradient bugs,
validating autodiff before scaling up.
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
    return s * (1 - s)


class TinyNetwork:
    def __init__(self):
        # Very small network: 2 inputs -> 2 hidden -> 1 output
        self.w1 = [[0.5, -0.3], [0.2, 0.4]]  # 2x2
        self.b1 = [0.1, -0.1]
        self.w2 = [0.6, -0.5]  # 1x2
        self.b2 = 0.2

    def forward(self, x: List[float]) -> Tuple[float, List[float], List[float]]:
        """Forward pass. Returns (output, z1, h) for backprop."""
        z1 = [self.b1[0] + self.w1[0][0] * x[0] + self.w1[0][1] * x[1],
              self.b1[1] + self.w1[1][0] * x[0] + self.w1[1][1] * x[1]]
        h = [sigmoid(z1[0]), sigmoid(z1[1])]

        z2 = self.b2 + self.w2[0] * h[0] + self.w2[1] * h[1]
        y = sigmoid(z2)

        return y, z1, h

    def loss(self, x: List[float], y_true: float) -> float:
        """MSE loss."""
        y_pred, _, _ = self.forward(x)
        return (y_pred - y_true) ** 2 / 2.0

    def analytic_gradients(self, x: List[float], y_true: float) -> Tuple[List[List[float]], List[float], List[float], float]:
        """Compute gradients via backprop."""
        y_pred, z1, h = self.forward(x)

        # Output layer: dL/dy = (y_pred - y_true) [MSE derivative]
        # Then dL/dz2 = dL/dy * dy/dz2 = (y_pred - y_true) * sigmoid'(y_pred)
        dL_dy = y_pred - y_true
        dL_dz2 = dL_dy * sigmoid_derivative(y_pred)

        # Output layer weights w.r.t. loss
        dw2 = [dL_dz2 * h[0], dL_dz2 * h[1]]
        db2 = dL_dz2

        # Hidden layer gradients w.r.t. z1, via chain rule through sigmoid
        dL_dz1 = [
            dL_dz2 * self.w2[0] * sigmoid_derivative(h[0]),
            dL_dz2 * self.w2[1] * sigmoid_derivative(h[1])
        ]

        # First layer weights: dL/dw1[i][j] = dL/dz1[i] * dz1[i]/dw1[i][j]
        dw1 = [[dL_dz1[0] * x[0], dL_dz1[0] * x[1]],
               [dL_dz1[1] * x[0], dL_dz1[1] * x[1]]]
        db1 = dL_dz1

        return dw1, db1, dw2, db2

    def numerical_gradient(self, x: List[float], y_true: float, param_name: str, param_indices: Tuple[int, ...], eps: float = 1e-5) -> float:
        """Compute numerical gradient via finite differences."""
        # Save original value
        if param_name == "w1":
            original = self.w1[param_indices[0]][param_indices[1]]
        elif param_name == "b1":
            original = self.b1[param_indices[0]]
        elif param_name == "w2":
            original = self.w2[param_indices[0]]
        else:  # b2
            original = self.b2

        # f(x + eps)
        if param_name == "w1":
            self.w1[param_indices[0]][param_indices[1]] = original + eps
        elif param_name == "b1":
            self.b1[param_indices[0]] = original + eps
        elif param_name == "w2":
            self.w2[param_indices[0]] = original + eps
        else:
            self.b2 = original + eps

        loss_plus = self.loss(x, y_true)

        # f(x - eps)
        if param_name == "w1":
            self.w1[param_indices[0]][param_indices[1]] = original - eps
        elif param_name == "b1":
            self.b1[param_indices[0]] = original - eps
        elif param_name == "w2":
            self.w2[param_indices[0]] = original - eps
        else:
            self.b2 = original - eps

        loss_minus = self.loss(x, y_true)

        # Restore
        if param_name == "w1":
            self.w1[param_indices[0]][param_indices[1]] = original
        elif param_name == "b1":
            self.b1[param_indices[0]] = original
        elif param_name == "w2":
            self.w2[param_indices[0]] = original
        else:
            self.b2 = original

        return (loss_plus - loss_minus) / (2.0 * eps)

    def relative_error(self, analytic: float, numerical: float) -> float:
        """Compute relative error."""
        denom = max(abs(analytic), abs(numerical), 1e-8)
        return abs(analytic - numerical) / denom


if __name__ == "__main__":
    random.seed(42)

    net = TinyNetwork()
    x = [0.5, -0.3]
    y_true = 0.7

    # Get analytic gradients
    dw1_ana, db1_ana, dw2_ana, db2_ana = net.analytic_gradients(x, y_true)

    print("Gradient checks:")
    max_rel_err = 0.0

    # Check w1
    for i in range(2):
        for j in range(2):
            num_grad = net.numerical_gradient(x, y_true, "w1", (i, j))
            rel_err = net.relative_error(dw1_ana[i][j], num_grad)
            max_rel_err = max(max_rel_err, rel_err)
            print(f"  w1[{i}][{j}]: analytic={dw1_ana[i][j]:.6f}, numerical={num_grad:.6f}, rel_err={rel_err:.2e}")

    # Check b1
    for i in range(2):
        num_grad = net.numerical_gradient(x, y_true, "b1", (i,))
        rel_err = net.relative_error(db1_ana[i], num_grad)
        max_rel_err = max(max_rel_err, rel_err)
        print(f"  b1[{i}]: analytic={db1_ana[i]:.6f}, numerical={num_grad:.6f}, rel_err={rel_err:.2e}")

    # Check w2
    for i in range(2):
        num_grad = net.numerical_gradient(x, y_true, "w2", (i,))
        rel_err = net.relative_error(dw2_ana[i], num_grad)
        max_rel_err = max(max_rel_err, rel_err)
        print(f"  w2[{i}]: analytic={dw2_ana[i]:.6f}, numerical={num_grad:.6f}, rel_err={rel_err:.2e}")

    # Check b2
    num_grad = net.numerical_gradient(x, y_true, "b2", ())
    rel_err = net.relative_error(db2_ana, num_grad)
    max_rel_err = max(max_rel_err, rel_err)
    print(f"  b2: analytic={db2_ana:.6f}, numerical={num_grad:.6f}, rel_err={rel_err:.2e}")

    print(f"\nMax relative error: {max_rel_err:.2e}")
    assert max_rel_err < 1e-4, f"Max relative error {max_rel_err} >= 1e-4"
    print("PASS")
