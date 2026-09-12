"""
Dynamic Range Compression via Logarithm and μ-Law.

Compress large dynamic range (e.g., audio amplitudes or intensity values)
into a narrower range while preserving relative differences at small scales.
Both log compression and μ-law compression should be invertible
and reduce the dynamic range.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
from typing import List


def log_compress(values: List[float], offset: float = 1.0) -> List[float]:
    """Log compression: log(|x| + offset)."""
    return [math.log(abs(v) + offset) for v in values]


def log_decompress(compressed: List[float], offset: float = 1.0) -> List[float]:
    """Invert log compression: exp(y) - offset."""
    return [math.exp(c) - offset for c in compressed]


def mu_law_compress(values: List[float], mu: float = 255.0) -> List[float]:
    """μ-law compression: sign(x) * ln(1 + μ|x|) / ln(1 + μ)."""
    return [
        math.copysign(math.log(1 + mu * abs(v)) / math.log(1 + mu), v)
        for v in values
    ]


def mu_law_decompress(compressed: List[float], mu: float = 255.0) -> List[float]:
    """Invert μ-law: sign(y) * (1/μ) * (exp(ln(1+μ)|y|) - 1)."""
    return [
        math.copysign(
            (math.exp(abs(c) * math.log(1 + mu)) - 1) / mu, c
        )
        for c in compressed
    ]


def dynamic_range(values: List[float]) -> float:
    """Ratio of max to min (absolute values)."""
    abs_vals = [abs(v) for v in values if v != 0]
    if not abs_vals:
        return 1.0
    return max(abs_vals) / min(abs_vals)


if __name__ == "__main__":
    import random

    random.seed(42)

    # Create data with large dynamic range: mix of small and large values (positive only)
    values = [0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]
    values = values + [random.uniform(0.001, 1000) for _ in range(10)]

    # Compute dynamic range before compression
    dr_original = dynamic_range(values)

    # Log compression
    log_compressed = log_compress(values, offset=0.1)
    dr_log = dynamic_range(log_compressed)

    log_reconstructed = log_decompress(log_compressed, offset=0.1)
    log_reconstruction_error = max(
        abs(values[i] - log_reconstructed[i]) / (abs(values[i]) + 1e-6)
        for i in range(len(values))
    )

    # μ-law compression
    mu_compressed = mu_law_compress(values, mu=255)
    dr_mu = dynamic_range(mu_compressed)

    mu_reconstructed = mu_law_decompress(mu_compressed, mu=255)
    mu_reconstruction_error = max(
        abs(values[i] - mu_reconstructed[i]) / (abs(values[i]) + 1e-6)
        for i in range(len(values))
    )

    # Assertions
    assert dr_log < dr_original, (
        f"Log compression did not reduce dynamic range: "
        f"original={dr_original:.1f}, log={dr_log:.1f}"
    )
    assert dr_mu < dr_original, (
        f"μ-law compression did not reduce dynamic range: "
        f"original={dr_original:.1f}, mu={dr_mu:.1f}"
    )
    assert log_reconstruction_error < 0.05, (
        f"Log reconstruction error too high: {log_reconstruction_error:.4f}"
    )
    assert mu_reconstruction_error < 0.05, (
        f"μ-law reconstruction error too high: {mu_reconstruction_error:.4f}"
    )

    print(
        f"Original range: {dr_original:.1f}x | "
        f"Log compressed: {dr_log:.1f}x ({dr_log/dr_original*100:.0f}%) | "
        f"μ-law compressed: {dr_mu:.1f}x ({dr_mu/dr_original*100:.0f}%) | "
        f"Log error: {log_reconstruction_error:.4f} | "
        f"μ-law error: {mu_reconstruction_error:.4f} | PASS"
    )
