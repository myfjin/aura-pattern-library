# lln clt demo

**Language:** Python · **Sphere:** data-science · **Category:** Information Theory & Probability

**Signature:** `(source_distribution: List[float], sample_size: int, num_samples: int) → List[float]`

## What it does

Law of Large Numbers and Central Limit Theorem: asymptotic behavior of sample means.

Core idea: LLN: sample mean converges to population mean as n → ∞.
CLT: the distribution of sample means approaches normal, regardless of source distribution.
Standardized sample means satisfy ~68% within 1σ, ~95% within 2σ, ~99.7% within 3σ.

Use when: understanding sampling distributions, validating statistical inference,
demonstrating convergence rates, checking normality of sample statistics.

## Guarantee

When it runs, lln clt demo guarantees 0.9 < source_mean < 1.1; source_skew > 1.5; errors[-1] < errors[0] (weak-grade: directional, proven by run).

**Checkable constraints:**

- `0.9 < source_mean < 1.1`
- `source_skew > 1.5`
- `errors[-1] < errors[0]`
- `skew_small > skew_medium > skew_large`
- `0.6 < cov_1sig < 0.76`
- `0.92 < cov_2sig < 0.98`
- `0.98 < cov_3sig < 1.0`
- `cov_1sig_small < cov_1sig or cov_2sig_small < cov_2sig`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def sample_means(source_distribution: List[float], sample_size: int, num_samples: int) -> List[float]:`, `def empirical_mean(samples: List[float]) -> float:`, `def empirical_std(samples: List[float]) -> float:`, `def coverage_percentile(samples: List[float], true_mean: float, num_stds: float) -> float:`, `def skewness(samples: List[float]) -> float:`
**Valid input:** `source_distribution` non-empty; `sample_size`, `num_samples` ≥ 1; `true_mean` numeric.
**Core:** Demonstrates the Law of Large Numbers (sample mean converges to population mean as `n` grows) and the Central Limit Theorem (distribution of sample means becomes normal, satisfying the empirical rule, regardless of skewed source). Uses an exponential source distribution.
**Assert:** Final error across `n = 10, 50, 100, 500` decreases (LLN); skewness of sample means decreases as `n` increases (CLT); for `n=500`, 1σ coverage ≈ 68%, 2σ ≈ 95%, 3σ ≈ 99.7%.
**✔ Retrofitted:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E retrofit pass; the current signed code reflects the fix.

---
*△ AURA Pattern Library — © Reality Optimizer*
