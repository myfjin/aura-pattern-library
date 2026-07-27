# kernel density estimation

**Language:** Python · **Sphere:** data-science · **Category:** Statistical Modeling

**Signature:** `(samples: List[float]) → float`

## What it does

Kernel Density Estimation (KDE) with Gaussian Kernel & Silverman Bandwidth.

Non-parametric density estimation via kernel smoothing.
Bandwidth chosen by Silverman's rule: h = (4/(3*n))^(1/5) * sigma.
Use for smooth density estimates from raw samples.

## Guarantee

When it runs, kernel density estimation guarantees abs(integral - 1.0) < 0.05; density_at_minus2 > density_at_0; density_at_2 > density_at_0 (proven by run).

**Checkable constraints:**

- `abs(integral - 1.0) < 0.05`
- `density_at_minus2 > density_at_0`
- `density_at_2 > density_at_0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `gaussian_kernel_density(samples, x, h) → float`, `silverman_bandwidth(samples) → float`
**Valid input:** `samples: List[float]` — at least 2 samples. `x: float`. `h > 0`.
**Core:** Non-parametric density estimation with Gaussian kernel. KDE: f̂(x) = (1/nh) Σ K((x-Xᵢ)/h) where K(u) = (1/√(2π))·exp(-u²/2). Bandwidth via Silverman's rule: h = (4/(3n))^{1/5} · σ̂.
**Assert:** On mixture of two Gaussians (40 pts from N(-2,0.5) + 40 pts from N(2,0.5)), KDE integral over [-5,5] within 0.05 of 1.0, density at modes (-2, 2) > density at center (0).
**✔ Retrofitted:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E retrofit pass; the current signed code reflects the fix.

---
*△ AURA Pattern Library — © Reality Optimizer*
