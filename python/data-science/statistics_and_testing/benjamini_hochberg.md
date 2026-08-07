# benjamini hochberg

**Language:** Python · **Sphere:** data-science · **Category:** Statistics & Testing

**Signature:** `(p_values: List[float], alpha: float) → Tuple[List[bool], float]`

## What it does

Benjamini-Hochberg False Discovery Rate Correction

Core idea: When testing many hypotheses, Bonferroni is overly conservative. Benjamini-Hochberg
controls the False Discovery Rate (FDR): the expected proportion of false positives among
rejected hypotheses. Sort p-values, find largest index i where p_i <= (i/m) * alpha,
then reject all p-values up to that index.

When to use: Multiple hypothesis testing (e.g., genome-wide association, gene expression).
FDR is less stringent than family-wise error rate (FWER), allowing more discoveries.

## Guarantee

When it runs, benjamini hochberg guarantees num_rejected_null <= 2; num_rejected_mixed >= 3; rejected_mixed[0] and rejected_mixed[1] and rejected_mixed[2] (weak-grade: directional, proven by run).

**Checkable constraints:**

- `num_rejected_null <= 2`
- `num_rejected_mixed >= 3`
- `rejected_mixed[0] and rejected_mixed[1] and rejected_mixed[2]`
- `num_rejected_alt >= 5`
- `num_rejected_large >= 40`
- `num_rejected_large <= 150`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def benjamini_hochberg(p_values: List[float], alpha: float = 0.05) -> Tuple[List[bool], float]:`
**Valid input:** `p_values` is a list of floats in [0, 1]; `alpha` is a float in (0, 1].
**Core:** Benjamini-Hochberg FDR procedure. Sorts p-values, finds the largest rank where `p_i <= (i/m) * alpha`, and rejects all hypotheses up to that rank.
**Assert:** A uniform null set of 10 p-values yields very few rejections; a mixed set of small planted signals yields several rejections and the three smallest p-values are rejected; a large 1000-test scenario with 50 true effects detects most true effects while keeping total rejections bounded.
**✔ Retrofitted:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E retrofit pass; the current signed code reflects the fix.

---
*△ AURA Pattern Library — © Reality Optimizer*
