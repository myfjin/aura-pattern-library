# welford online stats

**Language:** Python · **Sphere:** data-science · **Category:** Applied DS Practice

**Signature:** `(values: list[float]) → float`

## What it does

Welford's online algorithm for running mean and variance.

Welford's algorithm computes running mean and variance in a single pass with
O(1) memory and perfect numerical stability. It avoids the naive sum-of-squares
formula which catastrophically cancels when data has a large offset.

Use: streaming metrics, online parameter updates, memory-constrained environments.

## Guarantee

When it runs, welford online stats guarantees abs(welford_var - batch_var) < 1e-10; abs(welford_var - batch_var) < 1e-06; abs(naive_var - batch_var) > 1.0 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `abs(welford_var - batch_var) < 1e-10`
- `abs(welford_var - batch_var) < 1e-06`
- `abs(naive_var - batch_var) > 1.0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `class WelfordStats` with `def update(self, x: float) -> None:`, `def variance(self) -> float:`, `def std_dev(self) -> float:`, `def naive_variance(values: list[float]) -> float:`, `def batch_variance(values: list[float]) -> float:`
**Valid input:** `values` is a list of numbers with at least two elements for meaningful variance.
**Core:** Welford's online algorithm for stable one-pass mean and sample variance, compared against a naive sum-of-squares formula and a batch reference. The demo shows catastrophic cancellation in the naive formula for large-offset data.
**Assert:** On 1,000 N(0,1) samples, Welford variance matches batch variance within 1e-10. On 1,000 samples with offset 1e10, Welford variance still matches batch variance within 1e-6 while naive variance diverges by more than 1.0.
**⚠️ Defect:** `naive_variance` can return `0.0` when the population formula `E[X²] - E[X]²` yields a tiny negative number due to floating-point cancellation, hiding the numerical instability. The function returns `var * n/(n-1)` only when `var > 0`, otherwise `0.0`. `WelfordStats.variance()` returns `0.0` for `count < 2`, which is a sensible sentinel but not an error, and the class does not expose the running mean as a public accessor.

---

## Category: data_wrangling_from_scratch

---
*△ AURA Pattern Library — © Reality Optimizer*
