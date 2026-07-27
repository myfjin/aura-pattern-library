# inverse transform sampling

**Language:** Python · **Sphere:** data-science · **Category:** Information Theory & Probability

**Signature:** `(u: float, rate: float) → float`

## What it does

Inverse-transform sampling: generate samples from an arbitrary distribution via inverse CDF.

Core idea: If U ~ Uniform(0, 1) and F^{-1} is the inverse CDF, then X = F^{-1}(U) is distributed
according to the target distribution. For tractable F^{-1}, this is efficient and exact.

Use when: sampling from a distribution with known CDF, generating random variates, creating
synthetic data from a specified distribution.

## Guarantee

When it runs, inverse transform sampling guarantees abs(emp_mean_exp - true_mean_exp) < 0.05; abs(emp_var_exp - true_var_exp) < 0.05; abs(q50_exp - expected_median_exp) < 0.05 (proven by run).

**Checkable constraints:**

- `abs(emp_mean_exp - true_mean_exp) < 0.05`
- `abs(emp_var_exp - true_var_exp) < 0.05`
- `all((x >= 0 for x in samples_exp))`
- `abs(q50_exp - expected_median_exp) < 0.05`
- `all((0 <= x <= 2 for x in samples_piecewise))`
- `count_first_half > count_second_half`
- `0.6 < count_first_half / n_piecewise < 0.75`
- `abs(q_at_one - 2.0 / 3.0) < 0.05`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — positive, xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def exponential_inverse_cdf(u: float, rate: float) -> float:`, `def piecewise_inverse_cdf(u: float) -> float:`, `def sample_from_inverse_transform(inverse_cdf: Callable[[float], float], n: int) -> List[float]:`, `def empirical_mean(samples: List[float]) -> float:`, `def empirical_variance(samples: List[float]) -> float:`, `def empirical_quantile(samples: List[float], q: float) -> float:`
**Valid input:** `u` ∈ (0, 1); `rate` > 0; `n > 0`; `q` ∈ [0, 1].
**Core:** Inverse-transform sampling: if `U ~ Uniform(0,1)`, then `X = F^{-1}(U)` follows the target distribution. Includes exponential inverse CDF, a custom piecewise CDF, and sample diagnostics (mean, variance, quantile).
**Assert:** Exponential samples with rate=2 have mean ≈ 0.5 and variance ≈ 0.25; all samples non-negative; median ≈ ln(2)/rate. Piecewise distribution puts ~2/3 of mass on [0,1] and ~1/3 on (1,2], with CDF at x=1 ≈ 2/3.
**✔ Retrofitted:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E retrofit pass; the current signed code reflects the fix.

---
*△ AURA Pattern Library — © Reality Optimizer*
