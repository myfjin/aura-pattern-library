# weibull mle

**Language:** Python · **Sphere:** data-science · **Category:** Survival & Reliability

**Signature:** `(times: List[float], max_iter: int, tol: float) → Tuple[float, float]`

## What it does

Weibull MLE: maximum-likelihood estimation of shape k and scale λ (uncensored).

For iid Weibull data the log-likelihood is
    ℓ(k,λ) = n·ln k − n·k·ln λ + (k−1)·Σ ln t_i − Σ (t_i/λ)^k.
Profiling out λ = (Σ t_i^k / n)^(1/k) leaves a single equation in k:
    1/k + (1/n)Σ ln t_i − (Σ t_i^k ln t_i)/(Σ t_i^k) = 0,
solved here by Newton-Raphson. This is the actual MLE (not a log-log probability-plot
regression). Core claim: planted shape/scale recovered by maximum likelihood.

## Guarantee

When it runs, weibull mle guarantees abs(k_est - k_true) < 0.3; abs(lam_est - lam_true) < 0.5; abs(score_k) < 1e-06 (proven by run).

**Checkable constraints:**

- `abs(k_est - k_true) < 0.3`
- `abs(lam_est - lam_true) < 0.5`
- `abs(score_k) < 1e-06`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def weibull_mle(times: List[float], max_iter: int = 100, tol: float = 1e-10) -> Tuple[float, float]:`
**Valid input:** `times` is a non-empty list of positive numbers; `max_iter` > 0; `tol` > 0.
**Core:** Maximum likelihood estimation of Weibull shape `k` and scale `λ` for uncensored data. Profiles out `λ` and solves the single-variable shape equation by Newton-Raphson, then computes `λ = (Σ t_i^k / n)^(1/k)`.
**Assert:** On 80 samples from Weibull(`k=2.0`, `λ=5.0`), estimates are within ±0.3 for shape and ±0.5 for scale; the MLE stationarity score is near zero.
**✔ Retrofitted:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E retrofit pass; the current signed code reflects the fix.

---
*△ AURA Pattern Library — © Reality Optimizer*
