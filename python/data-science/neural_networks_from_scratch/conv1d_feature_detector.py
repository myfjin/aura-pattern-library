"""
1D convolution layer learning to detect a planted motif in sequences.

Core idea: Implement 1D convolution from scratch. Convolve a learnable kernel
over a 1D sequence. Data contains a planted motif; over training the kernel
learns to detect it, producing high responses when centered on the motif and low
elsewhere.

When to use: Understanding convolution mechanics, feature detection, temporal
pattern recognition.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
import random
from typing import List, Tuple


def mse_loss(pred: float, target: float) -> float:
    return (pred - target) ** 2 / 2.0


class Conv1D:
    def __init__(self, kernel_size: int = 3, lr: float = 0.01):
        self.kernel_size = kernel_size
        self.lr = lr
        # Single kernel (filter)
        self.kernel = [random.gauss(0, 0.1) for _ in range(kernel_size)]
        self.bias = 0.0

    def convolve(self, x: List[float]) -> List[float]:
        """Apply 1D convolution: valid padding."""
        output = []
        for i in range(len(x) - self.kernel_size + 1):
            conv_sum = self.bias
            for k in range(self.kernel_size):
                conv_sum += self.kernel[k] * x[i + k]
            output.append(conv_sum)
        return output

    def backward(self, x: List[float], conv_out: List[float],
                 target_responses: List[float]) -> float:
        """Backward pass: update kernel and bias based on response errors."""
        total_loss = 0.0

        # Compute loss and gradients
        dkernel = [0.0] * self.kernel_size
        dbias = 0.0

        for i in range(len(conv_out)):
            error = conv_out[i] - target_responses[i]
            loss = mse_loss(conv_out[i], target_responses[i])
            total_loss += loss

            # Gradient w.r.t. bias
            dbias += error

            # Gradient w.r.t. kernel
            for k in range(self.kernel_size):
                dkernel[k] += error * x[i + k]

        # Update
        for k in range(self.kernel_size):
            self.kernel[k] -= self.lr * dkernel[k]
        self.bias -= self.lr * dbias

        return total_loss / len(conv_out) if conv_out else 0.0


if __name__ == "__main__":
    random.seed(42)

    # Motif: [1.0, -0.5, 1.0]
    motif = [1.0, -0.5, 1.0]
    kernel_size = len(motif)

    # Generate training data: sequences with motif planted at specific positions
    # and noise elsewhere
    data = []

    # Positive samples: sequences containing the motif
    for _ in range(10):
        seq_len = 20
        seq = [random.gauss(0, 0.3) for _ in range(seq_len)]
        # Plant motif at random position
        motif_pos = random.randint(0, seq_len - kernel_size)
        for k in range(kernel_size):
            seq[motif_pos + k] = motif[k] + random.gauss(0, 0.1)
        data.append(seq)

    # Create training targets: high response at motif positions, low elsewhere
    targets_per_sample = []
    for seq in data:
        targets = []
        for i in range(len(seq) - kernel_size + 1):
            # Heuristic: check if this window contains high variance pattern
            window = seq[i:i+kernel_size]
            # Target high if window matches motif-like structure
            similarity = sum(window[k] * motif[k] for k in range(kernel_size))
            target = max(0.0, min(1.0, (similarity + 1.0) / 2.0))
            targets.append(target)
        targets_per_sample.append(targets)

    # Train
    conv_layer = Conv1D(kernel_size=kernel_size, lr=0.1)

    for epoch in range(200):
        total_loss = 0.0
        for seq, targets in zip(data, targets_per_sample):
            conv_out = conv_layer.convolve(seq)
            loss = conv_layer.backward(seq, conv_out, targets)
            total_loss += loss

    print(f"Final avg loss per sample: {total_loss / len(data):.6f}")
    print(f"Learned kernel: {[f'{k:.4f}' for k in conv_layer.kernel]}")
    print(f"Original motif: {motif}")

    # Evaluate: planted motif should produce high response
    test_seq = [random.gauss(0, 0.3) for _ in range(30)]
    motif_pos = 10
    for k in range(kernel_size):
        test_seq[motif_pos + k] = motif[k]

    responses = conv_layer.convolve(test_seq)
    response_at_motif = responses[motif_pos]
    avg_response_elsewhere = sum(responses[i] for i in range(len(responses)) if i != motif_pos) / (len(responses) - 1)

    print(f"Response at motif position: {response_at_motif:.4f}")
    print(f"Average response elsewhere: {avg_response_elsewhere:.4f}")

    # Assertion: response at motif should be much higher
    assert response_at_motif > avg_response_elsewhere * 2, \
        f"Motif response {response_at_motif} not >> non-motif {avg_response_elsewhere}"

    print("PASS")
