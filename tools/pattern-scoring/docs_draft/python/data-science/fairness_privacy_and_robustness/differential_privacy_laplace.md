# Differential Privacy via Laplace Mechanism

**File:** `python/data-science/fairness_privacy_and_robustness/differential_privacy_laplace.py`
**Sphere:** Data Science — Fairness, Privacy, and Robustness

---

## What it solves

**How to answer a query about private data without revealing any individual's information.** Add carefully calibrated noise to the answer. The Laplace mechanism adds noise from a Laplace distribution with scale = sensitivity / ε. The privacy budget ε controls the tradeoff: smaller ε = more privacy (more noise), larger ε = more accuracy (less noise). This pattern verifies that the likelihood ratio of neighboring datasets is bounded by e^ε — the mathematical guarantee of differential privacy.

**When to use:** You need to release statistics about sensitive data (counts, sums, means) while providing a formal privacy guarantee. The Laplace mechanism is the simplest building block of differential privacy.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `epsilon` | > 0, privacy budget | 0 → infinite noise (useless) |
| `true_count` | int ≥ 0 | — |
| `scale` | = 1/epsilon | — |

---

## How inputs shape the output

- **ε is the privacy knob:** ε=1.0 gives moderate privacy (the demo's setting). ε=0.1 gives strong privacy (noise overwhelms signal). ε=10 gives weak privacy (almost true value).
- **The likelihood ratio check proves the guarantee:** the ratio of probabilities of the same output under neighboring datasets (differing by 1 record) is bounded by e^ε. If this fails, the mechanism isn't differentially private.
- **Utility loss grows as ε shrinks:** the demo checks that the noisy count is within 100 of the true count — a weak check that passes even at small ε.

---

## Worked example (real run)

```
$ python3 python/data-science/fairness_privacy_and_robustness/differential_privacy_laplace.py
PASS
```

**Reading the output:** the likelihood ratio is bounded by e^1.0 ≈ 2.718, and the noisy count is within 100 of the true count 50. The privacy guarantee holds.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| `epsilon = 0` | ZeroDivision in scale | needs guard |
| `epsilon < 0` | negative scale, nonsense | needs guard |
| very small ε | utility loss may exceed 100 | expected behavior |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-18 · evidence: `output/manual_audit_2026-07-19.csv`
