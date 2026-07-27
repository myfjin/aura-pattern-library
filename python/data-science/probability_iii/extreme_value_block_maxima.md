# extreme value block maxima

**Language:** Python · **Sphere:** data-science · **Category:** Probability III

**Signature:** `(block_maxima: List[float]) → Tuple[float, float]`

## What it does

Block maxima: fit Gumbel distribution to extreme values for return-level estimation.

Core claim: planted return level recovered; CDF fit verified on known quantiles.

## Guarantee

When it runs, extreme value block maxima guarantees abs(mu_est - mu_true) < 5; abs(sigma_est - sigma_true) < 3; abs(gumbel_cdf(median_true, mu_true, sigma_true) - 0.5) < 1e-09 (proven by run).

**Checkable constraints:**

- `abs(mu_est - mu_true) < 5`
- `abs(sigma_est - sigma_true) < 3`
- `abs(gumbel_cdf(median_true, mu_true, sigma_true) - 0.5) < 1e-09`
- `abs(rl_est - rl_true) < 2 * sigma_true`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
