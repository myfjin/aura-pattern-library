# hmm baum welch

**Language:** Python · **Sphere:** data-science · **Category:** Probabilistic Modeling

**Signature:** `(obs_seq: List[int], pi: List[float], A: List[List[float]], B: List[List[float]]) → Tuple[List[List[float]], float, List[float]]`

## What it does

HMM Baum-Welch (EM) training: learn emission and transition probabilities.

Core idea: E-step computes forward-backward statistics; M-step re-estimates parameters.
Likelihood increases monotonically. Recovered probs ≈ planted truth.

When to use: sequence tagging, time-series classification, learning from unlabeled sequences.

## Guarantee

When it runs, hmm baum welch guarantees abs(sum(pi_learned) - 1.0) < 0.01; abs(sum(A_learned[i]) - 1.0) < 0.01; abs(sum(B_learned[i]) - 1.0) < 0.01 (proven by run).

**Checkable constraints:**

- `abs(sum(pi_learned) - 1.0) < 0.01`
- `abs(sum(A_learned[i]) - 1.0) < 0.01`
- `abs(sum(B_learned[i]) - 1.0) < 0.01`
- `b >= a - 1e-06`
- `eB < 0.15`
- `eA < 0.2`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
