# Dirichlet Stick-Breaking Process

**File:** `python/data-science/bayesian_iii_modeling_and_selection/dirichlet_stick_breaking.py`
**Sphere:** Data Science — Bayesian III: Modeling and Selection
**Status:** PASS-WITH-FLAG (Illia's audit 2026-07-19)

---

## What it solves

**The problem: "how many groups are in my data, when I don't know the number in advance?"** You're clustering customers, or finding topics in documents. K-means demands you pick K first. The Dirichlet Process says: *don't pick — let the data decide, keep a bit of probability aside for "a group I haven't seen yet."* Stick-breaking is HOW you build that:

Imagine a stick of length 1 (= 100% of probability). Break off a random piece — that's group 1's share. Break a piece of the REMAINDER — group 2's share. Keep going. Every break is `Beta(1, α)`-distributed, so **α (concentration) controls the breaking style**:
- **small α (0.5)** → big first breaks → a few dominant groups (most customers fall in 2-3 types)
- **large α (5+)** → tiny slivers → many small groups (long tail of niche types)

**When to use:** You're doing clustering or topic modeling and don't know the number of clusters in advance. The stick-breaking process is the engine behind infinite mixture models and Latent Dirichlet Allocation.

**NOT:** neural-network weights (the name misleads). These are **probability shares of clusters/topics** in Bayesian nonparametrics.

---

## Valid inputs (the contract — to be enforced per fix queue #7)

| Input | Domain | Today → |
|---|---|---|
| `alpha` | > 0 | stdlib gammavariate error (delegated, misattributed message) |
| `num_breaks` | ≥ 1, and **≫ 2.3·(1+α)** for the sum≈1 promise to hold | 0 → `[]` silently (E009 class) |

---

## How inputs shape the output

- **α is the fragmentation knob** (see above: few-big vs many-small pieces).
- **num_breaks is the truncation** — and here lives the flag: the leftover stick after k breaks averages `(α/(1+α))^k`. For α=0.5, 100 breaks leave ~nothing (sum≈1 ✅). **For α=100, 100 breaks leave ~37% unbroken — the weights sum to ~0.6, and the "sums to ≈1" promise breaks.** Rule of thumb: need `num_breaks ≈ 2.3·(1+α)` per decade of remainder you want gone.
- **Weights arrive unsorted** — early pieces aren't necessarily biggest for large α.

---

## Worked example (real runs, Illia's session)

```
stick_breaking_process(2.0, 5)  → [0.052, 0.061, 0.050, 0.167, 0.154]   # sums to 0.48
```

**Reading it:** 5 breaks with α=2 leave half the stick unbroken — correct truncation behavior, NOT a bug; the docstring's "sum→1" arrow means convergence as breaks→∞. The demo's own α=100 run (Illia) tripped its own ≥0.9 assert — that's the overclaim, not the math, failing.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| `alpha = -1` or `0` | ValueError from `random.gammavariate` — names STDLIB's params, not yours | α must be > 0; message misattributed (delegated catch) |
| `num_breaks = 0` | `[]` silently — sums to 0, contradicting the invariant | E009-class degenerate |
| `alpha ≫ num_breaks` | valid inputs, own assert fails (sum 0.6 < 0.9) | AURA-E011 overclaimed invariant |

---

## Provenance

Machine-VERIFIED (frozen ruler; planted demo only tested α=0.5/5) · cross-model reviewed 2026-07-18 · Illia's audit 2026-07-19: E011 found via α=100 free-play; description ruled below comprehension gate (docstring lines 3–4 near-duplicates) — this sheet is the mandated rewrite source · evidence: `output/manual_audit_2026-07-19.csv`
