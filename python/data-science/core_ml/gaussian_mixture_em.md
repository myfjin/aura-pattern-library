# gaussian mixture em

**Language:** Python · **Sphere:** data-science · **Category:** Core ML

**Signature:** `(x: float, mean: float, var: float) → float`

## What it does

Gaussian Mixture Model (1D) via Expectation-Maximization (from scratch).

Core idea: Model data as a mixture of k Gaussian distributions. EM iteratively
infers cluster responsibilities (E-step) and updates Gaussian parameters (M-step).
Converges to a local maximum of the likelihood.

When to use: Soft clustering; probabilistic model of data; identifying mixture components.

## Guarantee

When it runs, gaussian mixture em guarantees abs(means_sorted[1] - 5.0) < 1.5; abs(sum(weights) - 1.0) < 1e-05; means_sorted[0] < 2.5 (proven by run).

**Checkable constraints:**

- `means_sorted[0] < 2.5`
- `means_sorted[1] > 2.5`
- `abs(means_sorted[0]) < 1.5`
- `abs(means_sorted[1] - 5.0) < 1.5`
- `all((v > 0 for v in variances))`
- `abs(sum(weights) - 1.0) < 1e-05`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `em_fit_1d(X, k, max_iterations=100, tolerance=1e-6) → (means, variances, weights)`
**Valid input:** `X: List[float]` — 1D data, non-empty. `k: int` ≥ 1. `max_iterations ≥ 1`.
**Core:** 1D Gaussian Mixture Model via EM. E-step: compute responsibilities γᵢⱼ = πⱼ·N(xᵢ|μⱼ,σⱼ²) / Σ πₖ·N(xᵢ|μₖ,σₖ²). M-step: update πⱼ, μⱼ, σⱼ². Initialize with random data points as means, equal variances/weights. Converges when log-likelihood change < tolerance.
**Assert:** On 2-component mixture (μ=0, μ=5, σ=1 each, 25 pts each), recovered means within 1.5 of true, variances positive, weights sum to 1.
**✔ Retrofitted:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E retrofit pass; the current signed code reflects the fix.

---
*△ AURA Pattern Library — © Reality Optimizer*
