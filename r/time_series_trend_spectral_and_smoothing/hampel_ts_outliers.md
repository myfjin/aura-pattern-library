# hampel ts outliers

**Language:** R · **Sphere:** R · **Category:** Time Series — Trend, Spectral & Smoothing

**Signature:** `(x: ?, win: ?, threshold: ?) → ?`

## What it does

hampel_ts_outliers.R
Hampel identifier: rolling median and MAD for spike removal.
Claim: planted spikes detected and removed; clean data untouched on separate sample.
Tolerance: spike removal flag 100% sensitivity on planted, 0% false positive on clean.

## Guarantee

When it runs, hampel ts outliers guarantees sensitivity == 1; planted_detected; specificity > 0.95 (proven by run).

**Checkable constraints:**

- `planted_detected`
- `sensitivity == 1`
- `specificity > 0.95`
- `length(flags_outliers) == n`
- `sum(flags_outliers) <= 5`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `hampel_outliers(x, win = 7, threshold = 3.5)` → `list(flags, median, mad)`.
**Valid input:** `x` numeric series; `win` positive half-window; `threshold` positive. In-script: n=150 with 3 planted spikes of +15.
**Core:** Hampel filter for outlier flagging: within a sliding ±win window, compute the median and normalized MAD (`1.4826·median|x−med|`), flag point i if `|x_i − med_i|/MAD_i > threshold`.
**Assert:** flags the 3 planted outliers on the dirty series; ~no flags on the clean series.
**⚠️ Defect:** Windows are **truncated (asymmetric) at the series ends** (`max(1,i−win):min(n,i+win)`), so edge points get a smaller, biased window and reduced robustness. When MAD = 0 (flat window) it can't flag anything (returns FALSE) — outliers in constant stretches are missed. A cluster of adjacent outliers within one window can corrupt the median and mask each other.

---
*△ AURA Pattern Library — © Reality Optimizer*
