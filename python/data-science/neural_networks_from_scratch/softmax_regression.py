"""
Multi-class softmax regression with cross-entropy loss.

Core idea: Learn to classify 3 synthetic clusters in 2D using a linear classifier
with softmax output and cross-entropy loss. Gradient descent updates weights to
maximize log-probability of true class.

When to use: Multiclass classification, understanding softmax and cross-entropy,
baseline for any categorical prediction task.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
import random
from typing import List, Tuple


def softmax(logits: List[float]) -> List[float]:
    """Softmax normalization."""
    max_logit = max(logits)
    exp_logits = [math.exp(z - max_logit) for z in logits]
    sum_exp = sum(exp_logits)
    return [e / sum_exp for e in exp_logits]


def cross_entropy(probs: List[float], target_class: int) -> float:
    """Cross-entropy loss: -log(probs[target_class])."""
    return -math.log(max(probs[target_class], 1e-10))


class SoftmaxRegression:
    def __init__(self, input_dim: int = 2, num_classes: int = 3, lr: float = 0.01):
        self.input_dim = input_dim
        self.num_classes = num_classes
        self.lr = lr

        # Weights: (num_classes, input_dim)
        self.W: List[List[float]] = [
            [random.gauss(0, 0.1) for _ in range(input_dim)]
            for _ in range(num_classes)
        ]
        self.b: List[float] = [0.0] * num_classes

    def forward(self, x: List[float]) -> Tuple[List[float], List[float]]:
        """Forward pass. Returns (softmax_probs, logits)."""
        logits = [self.b[c] + sum(self.W[c][d] * x[d] for d in range(self.input_dim))
                  for c in range(self.num_classes)]
        probs = softmax(logits)
        return probs, logits

    def backward(self, x: List[float], probs: List[float], target_class: int):
        """Gradient of cross-entropy w.r.t. logits: probs - one_hot."""
        # Gradient w.r.t. logits
        grad_logits = probs[:]
        grad_logits[target_class] -= 1.0

        # Gradient w.r.t. weights
        for c in range(self.num_classes):
            for d in range(self.input_dim):
                self.W[c][d] -= self.lr * grad_logits[c] * x[d]
            self.b[c] -= self.lr * grad_logits[c]

    def train(self, data: List[Tuple[List[float], int]], epochs: int) -> float:
        """Train on data, return final average cross-entropy loss."""
        for _ in range(epochs):
            total_loss = 0.0
            for x, y_true in data:
                probs, _ = self.forward(x)
                loss = cross_entropy(probs, y_true)
                total_loss += loss
                self.backward(x, probs, y_true)

        # Final loss
        total_loss = 0.0
        for x, y_true in data:
            probs, _ = self.forward(x)
            loss = cross_entropy(probs, y_true)
            total_loss += loss

        return total_loss / len(data) if data else 0.0

    def predict(self, x: List[float]) -> int:
        """Return predicted class."""
        probs, _ = self.forward(x)
        return probs.index(max(probs))


if __name__ == "__main__":
    random.seed(42)

    # Synthetic 3-class dataset: clusters around (0, 0), (3, 0), (1.5, 3)
    data = []

    # Class 0: around (0, 0)
    for _ in range(10):
        x = [random.gauss(0, 0.3), random.gauss(0, 0.3)]
        data.append((x, 0))

    # Class 1: around (3, 0)
    for _ in range(10):
        x = [random.gauss(3, 0.3), random.gauss(0, 0.3)]
        data.append((x, 1))

    # Class 2: around (1.5, 3)
    for _ in range(10):
        x = [random.gauss(1.5, 0.3), random.gauss(3, 0.3)]
        data.append((x, 2))

    # Train
    model = SoftmaxRegression(input_dim=2, num_classes=3, lr=0.1)
    final_loss = model.train(data, epochs=100)

    # Evaluate
    correct = sum(1 for x, y_true in data if model.predict(x) == y_true)
    accuracy = correct / len(data)

    print(f"Final cross-entropy loss: {final_loss:.4f}")
    print(f"Accuracy: {accuracy:.2%}")

    # Assertions
    assert accuracy >= 0.9, f"Accuracy {accuracy} below 0.9"
    print("PASS")
