# entropy estimators

**Language:** Python · **Sphere:** data-science · **Category:** Information Theory & Probability

**Signature:** `(probabilities: List[float]) → float`

## What it does

Shannon entropy estimation from samples: naive plug-in vs Miller-Madow bias correction.

Core idea: Naive plug-in uses empirical frequencies as probabilities; Miller-Madow correction
adds a bias term (-1/(2*N) * number_of_symbols) to reduce bias on small samples. The correction
pulls the estimate closer to the true entropy when N is small.

Use when: estimating entropy from limited data, correcting bias in frequency-based statistics,
comparing sample-based estimates to ground truth.

## Guarantee

When it runs, entropy estimators guarantees abs(true_h - 2.0) < 1e-09; abs(naive_large - true_h) < 0.1; abs(mm_large - true_h) < 0.1 (proven by run).

**Checkable constraints:**

- `abs(true_h - 2.0) < 1e-09`
- `mm_error < naive_error`
- `abs(naive_large - true_h) < 0.1`
- `abs(mm_large - true_h) < 0.1`
- `mm_large > naive_large`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def true_entropy(probabilities: List[float]) -> float:`, `def naive_plugin_entropy(samples: List[int]) -> float:`, `def miller_madow_entropy(samples: List[int]) -> float:`
**Valid input:** `probabilities` is a valid distribution (sums to 1, non-negative); `samples` is a non-empty list of discrete symbol indices.
**Core:** Estimates Shannon entropy in bits. `true_entropy` computes ground truth from known probabilities. `naive_plugin_entropy` uses empirical frequencies as probabilities. `miller_madow_entropy` adds the standard bias correction `(k - 1)/(2N ln 2)` to reduce small-sample underestimation.
**Assert:** For uniform(4), true entropy = 2.0 bits. On N=20 samples, Miller-Madow is closer to the true entropy than naive plug-in; on N=10,000 both converge to ≈2.0 bits and the correction is small and positive.
**⚠️ Defect:** The estimators do not validate that `samples` is non-empty (empty input returns 0.0). `miller_madow_entropy` uses the number of *observed* symbols `k` rather than the true alphabet size, so the correction is wrong when some symbols are unseen but the alphabet size is known.

---
*△ AURA Pattern Library — © Reality Optimizer*
