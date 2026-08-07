# target encoding smoothing

**Language:** Python · **Sphere:** data-science · **Category:** Applied DS Practice

**Signature:** `(cats: List[str], targets: List[int], alpha: float) → Dict[str, float]`

## What it does

Target encoding with smoothing + out-of-fold fitting.

Target (mean) encoding replaces a category with the mean target of that
category — powerful, and the classic way to leak: if the encoding is fit on
data that includes the rows being encoded (or the test set), the feature
memorizes target noise and shows FAKE predictive skill. Two defenses, both
implemented here: SMOOTHING (shrink rare-category means toward the global
prior: (sum + a*prior)/(count + a)) and OUT-OF-FOLD fitting (each training
row is encoded using an encoding fit WITHOUT its own fold; test rows use an
encoding fit on all of train).

The demo plants PURE-NOISE targets, so any measured "skill" is fabricated:
leaky encoding shows high test correlation on noise; OOF shows ≈ zero — the
truth. Use when: encoding high-cardinality categoricals for models.

## Guarantee

When it runs, target encoding smoothing guarantees corr_test_leaky > 0.3; corr_test_proper < 0.15; corr_train_oof < 0.15 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `corr_test_leaky > 0.3`
- `corr_test_proper < 0.15`
- `corr_train_oof < 0.15`
- `abs(smooth - rare_prior) < abs(raw - rare_prior)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def fit_encoding(cats: List[str], targets: List[int], alpha: float = 0.0) -> Dict[str, float]:`, `def apply_encoding(cats: List[str], enc: Dict[str, float], default: float) -> List[float]:`, `def oof_encode_train(cats: List[str], targets: List[int], n_folds: int = 5, alpha: float = 5.0) -> List[float]:`, `def abs_correlation(X: List[float], y: List[int]) -> float:`
**Valid input:** `cats` and `targets` same-length lists; binary targets in `targets`; `n_folds >= 2`; `alpha >= 0`.
**Core:** Target (mean) encoding with smoothing and true out-of-fold (OOF) fitting. The demo plants pure-noise targets to show that leakage (encoding fit on train+test) fabricates test-set "skill" while OOF and proper train-only encoding show near-zero correlation.
**Assert:** On 80 categories × 5 rows of pure-noise binary targets, leaky test-set |correlation| > 0.30, proper test |correlation| < 0.15, OOF train |correlation| < 0.15, and smoothing pulls a rare category toward the global prior.
**✔ Retrofitted:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E retrofit pass; the current signed code reflects the fix.

---
*△ AURA Pattern Library — © Reality Optimizer*
