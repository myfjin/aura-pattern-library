"""
Early stopping with patience-based validation monitoring.

Core idea: Train a network and monitor validation loss each epoch. If validation loss
doesn't improve for `patience` consecutive epochs, stop training early and restore the
best weights seen. Prevents overfitting and wasted computation.

When to use: Any supervised training with validation data, preventing overfitting,
efficient hyperparameter search.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
import random
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
    _aura_validate_sigmoid(x)
    if x < -500:
        return 0.0
    if x > 500:
        return 1.0
    return 1.0 / (1.0 + math.exp(-x))


def sigmoid_derivative(s: float) -> float:
    return s * (1 - s)


class NetworkWithEarlyStopping:
    def __init__(self):
        # Simple 2-layer network: 3 -> 6 -> 1
        self.w1 = [[random.gauss(0, 0.5) for _ in range(3)] for _ in range(6)]
        self.b1 = [0.0] * 6
        self.w2 = [random.gauss(0, 0.5) for _ in range(6)]
        self.b2 = 0.0

    def forward(self, x: List[float]) -> Tuple[float, List[float]]:
        """Forward pass."""
        z1 = [self.b1[i] + sum(self.w1[i][j] * x[j] for j in range(3))
              for i in range(6)]
        h = [sigmoid(z1[i]) for i in range(6)]
        z2 = self.b2 + sum(self.w2[i] * h[i] for i in range(6))
        y = sigmoid(z2)
        return y, h

    def backward(self, x: List[float], y_true: float, y_pred: float, h: List[float], lr: float):
        """Backward pass."""
        dy = y_pred - y_true

        # Output layer
        for i in range(6):
            self.w2[i] -= lr * dy * h[i]
        self.b2 -= lr * dy

        # Hidden layer
        for i in range(6):
            grad = dy * self.w2[i] * sigmoid_derivative(h[i])
            for j in range(3):
                self.w1[i][j] -= lr * grad * x[j]
            self.b1[i] -= lr * grad

    def save_weights(self) -> Tuple[List[List[float]], List[float], List[float], float]:
        """Save current weights."""
        w1_copy = [[self.w1[i][j] for j in range(3)] for i in range(6)]
        b1_copy = self.b1[:]
        w2_copy = self.w2[:]
        b2_copy = self.b2
        return w1_copy, b1_copy, w2_copy, b2_copy

    def restore_weights(self, weights: Tuple[List[List[float]], List[float], List[float], float]):
        """Restore weights from checkpoint."""
        self.w1, self.b1, self.w2, self.b2 = weights

    def train_with_early_stopping(self, train_data: List[Tuple[List[float], float]],
                                   val_data: List[Tuple[List[float], float]],
                                   max_epochs: int = 100, patience: int = 10, lr: float = 0.1) -> Tuple[int, float]:
        """Train with early stopping. Returns (epochs_trained, best_val_loss)."""
        best_val_loss = float('inf')
        best_weights = self.save_weights()
        patience_counter = 0
        epoch_stopped = 0

        for epoch in range(max_epochs):
            # Train on all training data
            for x, y_true in train_data:
                y_pred, h = self.forward(x)
                self.backward(x, y_true, y_pred, h, lr)

            # Evaluate on validation data
            val_loss = 0.0
            for x, y_true in val_data:
                y_pred, _ = self.forward(x)
                val_loss += (y_pred - y_true) ** 2 / 2.0
            val_loss /= len(val_data)

            # Check if validation loss improved
            if val_loss < best_val_loss:
                best_val_loss = val_loss
                best_weights = self.save_weights()
                patience_counter = 0
            else:
                patience_counter += 1

            # Early stopping criterion
            if patience_counter >= patience:
                epoch_stopped = epoch + 1
                break

        # Restore best weights
        self.restore_weights(best_weights)
        return epoch_stopped if epoch_stopped > 0 else max_epochs, best_val_loss


if __name__ == "__main__":
    random.seed(42)

    # Generate training and validation data
    # Task: classify if x[0] + x[1] > 0, with some noise
    train_data = []
    for _ in range(40):
        x = [random.gauss(0, 1.0) for _ in range(3)]
        y_true = 1.0 if (x[0] + x[1] > 0) else 0.0
        if random.random() < 0.1:
            y_true = 1.0 - y_true
        train_data.append((x, y_true))

    val_data = []
    for _ in range(40):
        x = [random.gauss(0, 1.0) for _ in range(3)]
        y_true = 1.0 if (x[0] + x[1] > 0) else 0.0
        val_data.append((x, y_true))

    # Train without early stopping (baseline)
    print("Training without early stopping (max 100 epochs):")
    net_no_stop = NetworkWithEarlyStopping()
    train_loss_no_stop = 0.0
    for epoch in range(100):
        for x, y_true in train_data:
            y_pred, h = net_no_stop.forward(x)
            net_no_stop.backward(x, y_true, y_pred, h, lr=0.1)

    # Evaluate
    for x, y_true in train_data:
        y_pred, _ = net_no_stop.forward(x)
        train_loss_no_stop += (y_pred - y_true) ** 2 / 2.0
    train_loss_no_stop /= len(train_data)

    val_loss_no_stop = 0.0
    for x, y_true in val_data:
        y_pred, _ = net_no_stop.forward(x)
        val_loss_no_stop += (y_pred - y_true) ** 2 / 2.0
    val_loss_no_stop /= len(val_data)

    # Train with early stopping
    print("Training with early stopping (patience=10):")
    net_with_stop = NetworkWithEarlyStopping()
    epochs_trained, best_val_loss = net_with_stop.train_with_early_stopping(
        train_data, val_data, max_epochs=100, patience=10, lr=0.1
    )

    # Evaluate
    train_loss_with_stop = 0.0
    for x, y_true in train_data:
        y_pred, _ = net_with_stop.forward(x)
        train_loss_with_stop += (y_pred - y_true) ** 2 / 2.0
    train_loss_with_stop /= len(train_data)

    val_loss_with_stop = best_val_loss  # Already evaluated in early stopping loop

    print(f"Without early stopping: epochs=100, train_loss={train_loss_no_stop:.4f}, val_loss={val_loss_no_stop:.4f}")
    print(f"With early stopping: epochs={epochs_trained}, train_loss={train_loss_with_stop:.4f}, val_loss={val_loss_with_stop:.4f}")

    # Assertions
    assert epochs_trained < 100, f"Early stopping should stop before max_epochs (got {epochs_trained})"
    assert val_loss_with_stop <= val_loss_no_stop * 1.1, \
        f"Early stopping val_loss {val_loss_with_stop} should be comparable to no-stop {val_loss_no_stop}"

    print("PASS")
