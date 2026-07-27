# kde seeded gmm

**Language:** Python · **Sphere:** data-science · **Category:** Composed Tools

**Signature:** `(values: List[float], grid: List[float]) → List[float]`

## What it does

KDE-Seeded Gaussian Mixture — the nonparametric scout guides the parametric army.

COMPOSED PATTERN: kernel_density_estimation (Statistical Modeling) x
gaussian_mixture_em (Core ML) — embedding bridge 0.494, found 2026-07-06.
KDE and GMM are the two classic answers to "what distribution is this?" —
composed, KDE runs first as a scout: its density modes reveal HOW MANY
components exist and WHERE, seeding EM's initial means. Random-initialized EM
on unbalanced mixtures routinely collapses two components into one; the
KDE-seeded start doesn't have to guess.

Use when: fitting mixtures without knowing k, or when random-init EM is
unstable on unbalanced components.

## Guarantee

When it runs, kde seeded gmm guarantees recovered(mu_s, true_means); n_random_ok < 6; ll_seeded >= best_random_ll - 1.0 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `len(modes) == 3`
- `recovered(mu_s, true_means)`
- `n_random_ok < 6`
- `ll_seeded >= best_random_ll - 1.0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
