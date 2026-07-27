# inclusion exclusion derangements

**Language:** Python · **Sphere:** data-science · **Category:** Probability III

**Signature:** `(n: int) → int`

## What it does

Inclusion-exclusion: count derangements (permutations with no fixed points).

!n = n! · Σ (−1)^k / k! ≈ n! / e. Core claim: exact formula matches simulation;
!n / n! → 1/e as n → ∞.

## Guarantee

When it runs, inclusion exclusion derangements guarantees abs(observed_proportion - expected_proportion) < 0.05; abs(ratio - 1 / math.e) < 0.01 (proven by run).

**Checkable constraints:**

- `abs(observed_proportion - expected_proportion) < 0.05`
- `abs(ratio - 1 / math.e) < 0.01`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
