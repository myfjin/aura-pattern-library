"""
1-hidden-layer autoencoder compressing correlated 8D data to 2D and back.

Core idea: Encoder maps 8D input -> 2D bottleneck via sigmoid. Decoder maps
2D -> 8D reconstruction. Train to minimize reconstruction error. With correlated
input (columns highly linearly dependent), 2D bottleneck should capture main
variance; reconstruction error should be far below random baseline.

When to use: Dimensionality reduction, data compression, unsupervised learning,
understanding encoder-decoder architectures.
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


class TinyAutoencoder:
    def __init__(self, input_dim: int = 8, bottleneck_dim: int = 2, lr: float = 0.1):
        self.input_dim = input_dim
        self.bottleneck_dim = bottleneck_dim
        self.lr = lr

        # Encoder: input_dim -> bottleneck_dim
        self.we = [[random.gauss(0, 0.2) for _ in range(input_dim)]
                   for _ in range(bottleneck_dim)]
        self.be = [0.0] * bottleneck_dim

        # Decoder: bottleneck_dim -> input_dim
        self.wd = [[random.gauss(0, 0.2) for _ in range(bottleneck_dim)]
                   for _ in range(input_dim)]
        self.bd = [0.0] * input_dim

    def encode(self, x: List[float]) -> List[float]:
        """Map input to bottleneck."""
        z = [self.be[i] + sum(self.we[i][j] * x[j] for j in range(self.input_dim))
             for i in range(self.bottleneck_dim)]
        h = [sigmoid(z[i]) for i in range(self.bottleneck_dim)]
        return h

    def decode(self, h: List[float]) -> List[float]:
        """Map bottleneck to reconstruction."""
        z = [self.bd[i] + sum(self.wd[i][j] * h[j] for j in range(self.bottleneck_dim))
             for i in range(self.input_dim)]
        recon = [sigmoid(z[i]) for i in range(self.input_dim)]
        return recon

    def forward(self, x: List[float]) -> Tuple[List[float], List[float]]:
        """Full autoencoder pass."""
        h = self.encode(x)
        recon = self.decode(h)
        return h, recon

    def backward(self, x: List[float], h: List[float], recon: List[float]):
        """Backward pass: update both encoder and decoder."""
        # Decoder gradients
        drecon_loss = [recon[i] - x[i] for i in range(self.input_dim)]

        # Gradients at decoder output pre-activation
        dz_d = [drecon_loss[i] * sigmoid_derivative(recon[i])
                for i in range(self.input_dim)]

        # Decoder weight and bias gradients
        for i in range(self.input_dim):
            for j in range(self.bottleneck_dim):
                self.wd[i][j] -= self.lr * dz_d[i] * h[j]
            self.bd[i] -= self.lr * dz_d[i]

        # Backprop to bottleneck
        dh = [sum(dz_d[i] * self.wd[i][j] for i in range(self.input_dim))
              for j in range(self.bottleneck_dim)]

        # Encoder gradients (chain through sigmoid)
        dz_e = [dh[i] * sigmoid_derivative(h[i]) for i in range(self.bottleneck_dim)]

        # Encoder weight and bias gradients
        for i in range(self.bottleneck_dim):
            for j in range(self.input_dim):
                self.we[i][j] -= self.lr * dz_e[i] * x[j]
            self.be[i] -= self.lr * dz_e[i]

    def train(self, data: List[List[float]], epochs: int) -> float:
        """Train on data, return final reconstruction error."""
        for _ in range(epochs):
            total_loss = 0.0
            for x in data:
                h, recon = self.forward(x)
                loss = sum((recon[i] - x[i]) ** 2 for i in range(self.input_dim)) / 2.0
                total_loss += loss
                self.backward(x, h, recon)

        # Final loss
        total_loss = 0.0
        for x in data:
            _, recon = self.forward(x)
            loss = sum((recon[i] - x[i]) ** 2 for i in range(self.input_dim)) / 2.0
            total_loss += loss

        return total_loss / len(data) if data else 0.0


if __name__ == "__main__":
    random.seed(42)

    # Generate correlated 8D data: first 4 dims are main signal, rest are small
    # perturbations, so most variance is capturable in 2D
    data = []
    for _ in range(50):
        # Base signal: 2 random components
        s1 = random.gauss(0, 1.0)
        s2 = random.gauss(0, 1.0)
        # Expand to 8D with strong correlations
        x = [
            s1,
            s1 + random.gauss(0, 0.1),
            s1 - random.gauss(0, 0.1),
            s1 * 0.7 + s2 * 0.3,
            s2,
            s2 + random.gauss(0, 0.1),
            s2 - random.gauss(0, 0.1),
            s2 * 0.7 + s1 * 0.3,
        ]
        # Normalize to [0, 1]
        x_min = min(x)
        x_max = max(x)
        if x_max > x_min:
            x = [(xi - x_min) / (x_max - x_min) for xi in x]
        data.append(x)

    # Untrained baseline: random reconstruction
    random_recon_error = 0.0
    for x in data:
        random_recon = [random.random() for _ in range(8)]
        error = sum((random_recon[i] - x[i]) ** 2 for i in range(8)) / 2.0
        random_recon_error += error
    random_recon_error /= len(data)

    # Train autoencoder
    ae = TinyAutoencoder(input_dim=8, bottleneck_dim=2, lr=0.5)
    trained_error = ae.train(data, epochs=100)

    print(f"Random reconstruction error: {random_recon_error:.6f}")
    print(f"Trained reconstruction error: {trained_error:.6f}")
    print(f"Improvement: {random_recon_error / trained_error:.2f}x")

    # Assertion: trained should be far better
    assert trained_error < random_recon_error / 2, \
        f"Trained error {trained_error} not significantly better than random {random_recon_error}"

    print("PASS")
