# rank correlation

**Language:** C++ · **Sphere:** data-science · **Category:** Model Diagnostics

**Signature:** `(data: List[float]) → List[float]`

## What it does

rank_correlation.cpp — Spearman's rho and Kendall's tau.

## Guarantee

When it runs, rank correlation guarantees abs(rho_perfect - 1.0) < 0.01; abs(tau_perfect - 1.0) < 0.01; len(x) == len(y) (proven by run on the PY original).

**Checkable constraints:**

- `len(x) == len(y)`
- `len(x) == len(y)`
- `abs(rho_perfect - 1.0) < 0.01`
- `abs(tau_perfect - 1.0) < 0.01`
- `abs(rho_random) < 0.4`
- `abs(tau_random) < 0.4`
- `abs(rho_decreasing - -1.0) < 0.01`
- `abs(tau_decreasing - -1.0) < 0.01`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — established on the PY original and shared by this C++ twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `spearman_correlation(x, y) → float`, `kendall_tau(x, y) → float`
**Valid input:** `x, y: List[float]` — same length, at least 2 samples.
**Core:** Spearman's rho: Pearson correlation on ranks. Kendall's tau: (concordant - discordant) / total pairs. Both measure monotonic association. Tested on perfect monotone (rho=1, tau=1), independent random (rho≈0, tau≈0), and perfect decreasing (rho=-1, tau=-1).
**Assert:** Perfect increasing: rho=1, tau=1 (within 0.01). Random 100 samples: |rho| < 0.4, |tau| < 0.4. Perfect decreasing: rho=-1, tau=-1 (within 0.01).
**⚠️ Defect:** Kendall's tau is O(n²) — for n=100 it computes 4,950 pairs, which is fine, but for n > 10,000 it becomes prohibitive. The test uses n=100 for random data, which is reasonable, but the function has no early-exit or approximation for large n. Also, tied pairs are silently ignored rather than using tau-b correction.

---
*△ AURA Pattern Library — © Reality Optimizer*
