# box muller gaussian

**Language:** C++ · **Sphere:** data-science · **Category:** Information Theory & Probability

**Signature:** `() → Tuple[float, float]`

## What it does

⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣

## Guarantee

When it runs, box muller gaussian guarantees abs(emp_mean) < 0.05; 0.95 < emp_var < 1.05; abs(emp_skew) < 0.1 (weak-grade: directional, proven by run on the PY original).

**Checkable constraints:**

- `abs(emp_mean) < 0.05`
- `0.95 < emp_var < 1.05`
- `abs(emp_skew) < 0.1`
- `0.65 < coverage_1sigma < 0.72`
- `0.93 < coverage_2sigma < 0.97`
- `0.99 < coverage_3sigma < 1.0`
- `negatives > 0 and positives > 0`
- `ratio > 0.45`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — established on the PY original and shared by this C++ twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def box_muller_pair() -> Tuple[float, float]:`, `def generate_gaussians(n: int) -> List[float]:`, `def empirical_mean(samples: List[float]) -> float:`, `def empirical_variance(samples: List[float]) -> float:`, `def empirical_skewness(samples: List[float]) -> float:`, `def coverage_percentile(samples: List[float], num_stds: float) -> float:`
**Valid input:** `n >= 1`; `num_stds >= 0`; samples are numeric.
**Core:** Box-Muller transform maps two independent Uniform(0,1) samples to two independent standard normal samples. The demo verifies mean ≈ 0, variance ≈ 1, skewness ≈ 0, and empirical-rule coverage for 1σ/2σ/3σ bands.
**Assert:** On 10,000 samples (seed 42), |mean| < 0.05, 0.95 < variance < 1.05, |skewness| < 0.1, and ~68%/95%/99.7% coverage within 1/2/3 standard deviations.
**⚠ Retrofit NOT in this twin:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E input-contract retrofit on the PY original (7497d40, 2026-07-21). That pass deliberately excluded the compiled lanes, so this C++ twin does NOT carry the contract its source now enforces. Declared in MANIFEST.json `twin_contract_divergence`; unblocking it needs the cpp attack lane. Corrected 2026-07-28 — the card previously claimed the fix was in this file.

---
*△ AURA Pattern Library — © Reality Optimizer*
