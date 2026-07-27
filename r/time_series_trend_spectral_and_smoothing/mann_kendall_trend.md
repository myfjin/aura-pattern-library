# mann kendall trend

**Language:** R · **Sphere:** R · **Category:** Time Series — Trend, Spectral & Smoothing

**Signature:** `(time: ?, value: ?) → ?`

## What it does

Mann-Kendall Trend Test: Kendall's S statistic over time index
Implements concordance pairs for trend detection; compares to cor.test(method="kendall")
Core: count concordant/discordant pairs between (time, value); S = (C - D) * 2 / (n*(n-1));
τ = S / (n*(n-1)/2), test significance via normal approximation
Planted: time series with clear uptrend and downtrend control series; trend detected, noise not

## Guarantee

When it runs, mann kendall trend guarantees all.equal(result_trend$tau, unname(oracle_trend$estimate), tolerance = 1e-06); all.equal(result_trend$p_value, oracle_trend$p.value, tolerance = 1e-05); result_trend$p_value < 0.05 (proven by run).

**Checkable constraints:**

- `result_trend$p_value < 0.05`
- `result_noise$p_value > 0.05`
- `all.equal(result_trend$tau, unname(oracle_trend$estimate), tolerance = 1e-06)`
- `all.equal(result_trend$p_value, oracle_trend$p.value, tolerance = 1e-05)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `mk_test(time, value)` → `list(S, tau, z, p_value)`.
**Valid input:** `time`, `value` equal-length numeric vectors. In-script: n=30, a trend series and a noise series.
**Core:** Mann-Kendall non-parametric trend test: S = Σ sign(t_j−t_i)·sign(v_j−v_i) over all pairs, variance `n(n−1)(2n+5)/18`, continuity-corrected Z, Kendall's τ. Verified against `cor.test(method="kendall")`.
**Assert:** trend series p<0.05, noise series p>0.05; τ and p match `cor.test` (tol 1e-6 / 1e-5).
**⚠️ Defect:** O(n²) double loop over all pairs (slow for long series). The variance formula uses the **no-ties** form — with tied values it overstates precision (no tie-correction term), so p-values are wrong for discrete/rounded data. n=30 is small for the normal approximation.

---
*△ AURA Pattern Library — © Reality Optimizer*
