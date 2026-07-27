# kl divergence cross entropy

**Language:** Python · **Sphere:** data-science · **Category:** Information Theory & Probability

**Signature:** `(p: List[float], q: List[float]) → float`

## What it does

KL divergence, cross-entropy, and Jensen-Shannon divergence between discrete distributions.

Core idea: KL divergence D(p||q) = sum(p[i] * log(p[i]/q[i])) measures how q differs from p.
Cross-entropy H(p,q) = -sum(p[i] * log(q[i])) is the expected bits needed when using distribution q
to encode samples from p. Jensen-Shannon distance is symmetric: JS(p||q) = 0.5*D(p||q) + 0.5*D(q||p).

Use when: comparing probability distributions, measuring distribution divergence, evaluating
generative models (cross-entropy loss), constructing symmetric distance metrics for clustering.

## Guarantee

When it runs, kl divergence cross entropy guarantees abs(computed_kl - expected_kl) < 1e-09; len(p) == len(q); len(p) == len(q) (proven by run).

**Checkable constraints:**

- `len(p) == len(q)`
- `len(p) == len(q)`
- `len(p) == len(q)`
- `abs(kl_self) < 1e-09`
- `abs(hpq - (hp + dpq)) < 1e-09`
- `abs(js_pq - js_qp) < 1e-09`
- `0 <= js_pr <= 1`
- `abs(computed_kl - expected_kl) < 1e-09`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def kl_divergence(p: List[float], q: List[float]) -> float:`, `def cross_entropy(p: List[float], q: List[float]) -> float:`, `def shannon_entropy(p: List[float]) -> float:`, `def jensen_shannon_distance(p: List[float], q: List[float]) -> float:`
**Valid input:** `p` and `q` are valid, equal-length discrete probability distributions.
**Core:** Information-theoretic divergences: KL divergence `D(p||q)`, cross-entropy `H(p,q)`, Shannon entropy `H(p)`, and symmetric Jensen-Shannon distance (square root of JS divergence). Verifies identities and hand-computed examples.
**Assert:** `KL(p||p) = 0`; `H(p,q) = H(p) + D(p||q)`; JS distance is symmetric and bounded in [0, 1]; hand-computed 2-point example matches within 1e-9.
**⚠️ Defect:** No validation that inputs are valid probability distributions (non-negative and sum to 1). If `q[i] = 0` while `p[i] > 1e-10`, the code raises `ZeroDivisionError` rather than returning `+inf` or a clean error. The `1e-10` threshold is arbitrary and can silently drop mass from near-zero probabilities.

---
*△ AURA Pattern Library — © Reality Optimizer*
