"""
Dropout regularization: network with vs without dropout on a noisy dataset.

Core idea: Generate a small noisy dataset prone to overfitting. Train two networks:
one with dropout (randomly zero hidden activations during training only) and
one without. The dropout version regularizes the network and generalizes better
to held-out validation data, especially on small datasets.

When to use: Overfitting prevention, regularization, robust model training.
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


class SimpleNetwork:
    def __init__(self, hidden_dim: int = 8, use_dropout: bool = False, dropout_rate: float = 0.3):
        self.hidden_dim = hidden_dim
        self.use_dropout = use_dropout
        self.dropout_rate = dropout_rate

        # 4 -> hidden -> 1
        self.w1 = [[random.gauss(0, 0.5) for _ in range(4)] for _ in range(hidden_dim)]
        self.b1 = [0.0] * hidden_dim
        self.w2 = [random.gauss(0, 0.5) for _ in range(hidden_dim)]
        self.b2 = 0.0

    def forward(self, x: List[float], training: bool = True) -> Tuple[float, List[float], List[bool]]:
        """Forward pass. Returns (output, hidden_activation, dropout_mask)."""
        z1 = [self.b1[i] + sum(self.w1[i][j] * x[j] for j in range(4))
              for i in range(self.hidden_dim)]
        h = [sigmoid(z1[i]) for i in range(self.hidden_dim)]

        # Dropout: only during training
        mask = [1.0 if (random.random() > self.dropout_rate) else 0.0
                for _ in range(self.hidden_dim)] if (self.use_dropout and training) else [1.0] * self.hidden_dim

        h_drop = [h[i] * mask[i] for i in range(self.hidden_dim)]

        z2 = self.b2 + sum(self.w2[i] * h_drop[i] for i in range(self.hidden_dim))
        y = sigmoid(z2)

        return y, h, mask

    def backward(self, x: List[float], y_true: float, y_pred: float, h: List[float], mask: List[bool], lr: float):
        """Backward pass."""
        dy = y_pred - y_true

        # Output layer update
        for i in range(self.hidden_dim):
            self.w2[i] -= lr * dy * h[i] * mask[i]
        self.b2 -= lr * dy

        # Hidden layer update
        for i in range(self.hidden_dim):
            grad = dy * self.w2[i] * sigmoid_derivative(h[i]) * mask[i]
            for j in range(4):
                self.w1[i][j] -= lr * grad * x[j]
            self.b1[i] -= lr * grad

    def train(self, train_data: List[Tuple[List[float], float]], epochs: int, lr: float) -> float:
        """Train and return final loss."""
        for _ in range(epochs):
            for x, y_true in train_data:
                y_pred, h, mask = self.forward(x, training=True)
                self.backward(x, y_true, y_pred, h, mask, lr)

        # Final loss
        total_loss = 0.0
        for x, y_true in train_data:
            y_pred, _, _ = self.forward(x, training=False)
            total_loss += (y_pred - y_true) ** 2 / 2.0

        return total_loss / len(train_data) if train_data else 0.0

    def evaluate(self, data: List[Tuple[List[float], float]]) -> Tuple[float, int]:
        """Evaluate: return MSE loss and num correct predictions."""
        total_loss = 0.0
        correct = 0
        for x, y_true in data:
            y_pred, _, _ = self.forward(x, training=False)
            total_loss += (y_pred - y_true) ** 2 / 2.0
            # Classify as 1 if y_pred > 0.5
            pred_class = 1 if y_pred > 0.5 else 0
            if pred_class == int(y_true):
                correct += 1

        return total_loss / len(data) if data else 0.0, correct


if __name__ == "__main__":
    random.seed(42)

    # Generate small noisy training set prone to overfitting
    train_data = []
    for _ in range(25):
        x = [random.gauss(0, 1.0) for _ in range(4)]
        # True rule: mostly x[0] + x[1] > 0, but with 30% label noise
        y_true = 1.0 if (x[0] + x[1] > 0) else 0.0
        if random.random() < 0.30:
            y_true = 1.0 - y_true
        train_data.append((x, y_true))

    # Clean validation set
    val_data = []
    for _ in range(100):
        x = [random.gauss(0, 1.0) for _ in range(4)]
        y_true = 1.0 if (x[0] + x[1] > 0) else 0.0
        val_data.append((x, y_true))

    # Train without dropout
    print("Training without dropout:")
    net_no_dropout = SimpleNetwork(hidden_dim=8, use_dropout=False)
    no_dropout_loss = net_no_dropout.train(train_data, epochs=60, lr=0.5)
    no_dropout_val_loss, no_dropout_acc = net_no_dropout.evaluate(val_data)

    # Train with dropout
    print("Training with dropout:")
    net_with_dropout = SimpleNetwork(hidden_dim=8, use_dropout=True, dropout_rate=0.15)
    dropout_loss = net_with_dropout.train(train_data, epochs=80, lr=0.5)
    dropout_val_loss, dropout_acc = net_with_dropout.evaluate(val_data)

    print(f"No dropout:  train_loss={no_dropout_loss:.4f}, val_loss={no_dropout_val_loss:.4f}, accuracy={no_dropout_acc}/{len(val_data)}")
    print(f"With dropout: train_loss={dropout_loss:.4f}, val_loss={dropout_val_loss:.4f}, accuracy={dropout_acc}/{len(val_data)}")

    # Assertion: dropout should not hurt too much, and shows regularization principle
    # On small noisy datasets, dropout helps prevent overfitting (gap between train and val)
    no_dropout_gap = no_dropout_val_loss - no_dropout_loss
    dropout_gap = dropout_val_loss - dropout_loss
    print(f"Generalization gap (train-val loss):")
    print(f"  No dropout: {no_dropout_gap:.4f}")
    print(f"  With dropout: {dropout_gap:.4f}")

    # Dropout should show smaller generalization gap (better regularization)
    assert dropout_gap <= no_dropout_gap, \
        f"Dropout gap {dropout_gap} should be <= no-dropout gap {no_dropout_gap}"

    print("PASS")
