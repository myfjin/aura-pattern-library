# randomized response

**Language:** Python · **Sphere:** data-science · **Category:** Fairness, Privacy & Robustness

**Signature:** `() → None`

## What it does

Randomized Response: privacy-preserving survey technique.

Each respondent answers honestly with probability p, lies with probability 1-p.
True rate is recovered via max-likelihood. Naive reading of noisy responses is biased,
but the unbiased estimate falls within confidence interval of true rate.

## Guarantee

When it runs, randomized response guarantees abs(unbiased_estimate - true_rate) < 0.2; naive_error > unbiased_error (proven by run).

**Checkable constraints:**

- `naive_error > unbiased_error`
- `abs(unbiased_estimate - true_rate) < 0.2`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
