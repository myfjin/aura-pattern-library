# Bayes Factor for Normal Means

**File:** `python/data-science/bayesian_iii_approximate_inference/bayes_factor_normal_means.py`
**Sphere:** Data Science — Bayesian III: Approximate Inference
**Status:** ❌❌ INVALID — WRONG MATHEMATICS as shipped (Illia's audit 2026-07-19)

---

## What it solves

"Is this effect real?" — Bayesian style. Given data assumed `N(θ, 1)`, compares H1 (θ ≠ 0, with prior `θ ~ N(0, τ²)`) against H0 (θ = 0). Returns the **Bayes factor**: BF > 1 means the data favor an effect; BF < 1 favors none; magnitude = strength of evidence.

**When to use:** You have normally distributed data with known variance (σ²=1) and want a Bayesian answer to "is there an effect?" The Bayes factor tells you how many times more likely the data are under H1 vs H0 — a continuous measure of evidence, not a binary "significant/not."

---

## ⚠️ The defect (teaching gold — how wrong math survives three machine gates)

- Shipped evidence term: `y_mean²·n / (1+nτ²)`. Correct: `τ²·(Σy)² / (1+nτ²)` — **missing n·τ²**.
- Consequence, measured (brute-force integration as ground truth): 30 points at 2.0 → code said BF **1.24**; truth is **3 × 10²⁴**. Illia's 300 identical points AT the H1 mean → code said **0.42** (evidence *against* the visible truth); truth ≈ 10²⁵⁸ for.
- **Why it survived:** the planted demo passes at 1.24 > 1 *by a hair* (planted-test-too-easy); the oracle re-runs that same demo; assert_linter checks assert shape, not truth; cross-model review checks description-vs-intent, not derivations. **Only a numeric oracle or re-derivation catches this class** → new gate for the validation tool.
- Found by a human changing σ and n in the demo and asking "does this number even make sense?"

---

## Valid inputs (the corrected contract)

| Input | Domain | Violating it → |
|---|---|---|
| `data` | non-empty list of finite numbers | AURA-E-B8 (empty) / AURA-E008 (NaN/inf) |
| `prior_var_h1` | > 0 (it's a variance) | AURA-E-B5 |
| model assumption | data ~ N(θ, **1.0**) — σ is FIXED at 1 and must be true of your data | undeclared before; now stated |

---

## How inputs shape the output (corrected version)

- **Σy is the engine:** evidence grows with the *squared sum* — both effect size and n multiply in. 30 clean points at 2.0 is already overwhelming (10²⁵-class BF), which is why the shipped 1.24 should have smelled wrong.
- **τ² (prior width):** wider prior → mild penalty on H1 (the `-0.5·log(1+nτ²)` term) — you pay for vagueness; with strong data the payment is negligible.
- **Data near 0** → BF < 1 gently (H0 is simpler and fits); the two-sided claim needs both directions, and the corrected harness prints both as receipts.

---

## Worked example (corrected, real run)

```
$ python3 retrofit_demo/bayes_factor_normal_means_RETROFIT.py
PASS: BF(H1-data)=1.15e+25>1 · BF(H0-data)=0.18<1
```

**Reading the output:** receipts, not a bare PASS — the two claims and their measured values. 1.15e25 = overwhelming evidence for an effect; 0.18 = mild, honest preference for "no effect" on null data (Bayes factors are conservative toward H0 — that asymmetry is correct).

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| `data = []` | ZeroDivisionError (n=0) | empty data → undefined BF |
| `data = [float('nan'), 1.0]` | NaN propagates silently | E008-class |
| `prior_var_h1 = -1` | math domain error (log of negative) | B5, accidental catch |
| valid data, correct formula | **shipped code returns wrong BF** (see defect above) | AURA-E010 — wrong math |

---

## Provenance

Machine-VERIFIED under frozen ruler (planted test too easy — the gate this find upgrades) · cross-model reviewed MATCHES 2026-07-18 (intent-level, correctly so) · Illia's audit 2026-07-19: WRONG-MATH kill via free-play; fix derived, verified against brute-force integration same day · evidence: `output/manual_audit_2026-07-19.csv` · error: AURA-E010
