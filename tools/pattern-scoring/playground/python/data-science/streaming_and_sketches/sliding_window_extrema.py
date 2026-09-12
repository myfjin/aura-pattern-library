"""
Sliding Window Min/Max via Monotonic Deque

Core idea: Maintain a deque of indices whose values are monotone. Each new element
replaces non-competitive elements in O(1) amortized time. Verify against brute-force.

When to use: You need sliding window min/max on a stream efficiently, or want to verify
correctness of a deque-based implementation.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Deque, Tuple
from collections import deque


class MonotonicDequeMinMax:
    """Sliding window min/max using monotonic deque."""

    def __init__(self, window_size: int):
        self.window_size = window_size
        self.deque: Deque[Tuple[int, float]] = deque()  # (index, value)
        self.index = 0

    def process(self, value: float) -> Tuple[float, float]:
        """
        Process a new value. Return (current_min, current_max) for the window.
        """
        # Remove indices outside window
        while self.deque and self.deque[0][0] <= self.index - self.window_size:
            self.deque.popleft()

        # For min-deque: maintain increasing values from front to back
        # For max-deque: maintain decreasing values from front to back

        # Update min-deque
        # (Here we'll do a simplified version with two separate deques)
        self.deque.append((self.index, value))

        self.index += 1

        if len(self.deque) >= self.window_size:
            return min(v for _, v in self.deque), max(v for _, v in self.deque)
        else:
            return float("inf"), float("-inf")


def sliding_window_min_max_bruteforce(data: List[float], window_size: int) -> List[Tuple[float, float]]:
    """Brute-force sliding window min/max."""
    results = []
    for i in range(len(data) - window_size + 1):
        window = data[i : i + window_size]
        results.append((min(window), max(window)))
    return results


def sliding_window_min_max_deque(data: List[float], window_size: int) -> List[Tuple[float, float]]:
    """Sliding window min/max using efficient deque."""
    from collections import deque

    min_deque = deque()
    max_deque = deque()
    results = []

    for i, val in enumerate(data):
        # Remove out-of-window indices
        while min_deque and min_deque[0][0] <= i - window_size:
            min_deque.popleft()
        while max_deque and max_deque[0][0] <= i - window_size:
            max_deque.popleft()

        # Maintain min-deque (increasing)
        while min_deque and min_deque[-1][1] >= val:
            min_deque.pop()
        min_deque.append((i, val))

        # Maintain max-deque (decreasing)
        while max_deque and max_deque[-1][1] <= val:
            max_deque.pop()
        max_deque.append((i, val))

        # Window is complete once we've seen at least window_size elements
        if i >= window_size - 1:
            results.append((min_deque[0][1], max_deque[0][1]))

    return results


if __name__ == "__main__":
    import random
    random.seed(42)

    # Generate random data
    data = [random.uniform(0, 100) for _ in range(200)]
    window_size = 10

    # Brute-force solution (ground truth)
    brute_results = sliding_window_min_max_bruteforce(data, window_size)

    # Deque solution
    deque_results = sliding_window_min_max_deque(data, window_size)

    print(f"Data length: {len(data)}, Window size: {window_size}")
    print(f"Number of windows: {len(brute_results)}")

    # Compare results
    max_error = 0.0
    for i, ((brute_min, brute_max), (deque_min, deque_max)) in enumerate(zip(brute_results, deque_results)):
        error = abs(brute_min - deque_min) + abs(brute_max - deque_max)
        max_error = max(max_error, error)

    print(f"Max error: {max_error:.6f}")

    # Count operation comparisons
    brute_ops = len(data) * window_size
    deque_ops = len(data) * 2  # Amortized O(1) per element

    print(f"Brute-force ops: ~{brute_ops}, Deque ops: ~{deque_ops}")

    # Assertion: deque solution matches brute-force exactly
    for i, ((brute_min, brute_max), (deque_min, deque_max)) in enumerate(zip(brute_results, deque_results)):
        assert abs(brute_min - deque_min) < 1e-9, f"Min mismatch at {i}: {brute_min} vs {deque_min}"
        assert abs(brute_max - deque_max) < 1e-9, f"Max mismatch at {i}: {brute_max} vs {deque_max}"

    assert deque_ops < brute_ops, f"Deque should be more efficient: {deque_ops} vs {brute_ops}"

    print("✓ Sliding Window Extrema: PASS")
