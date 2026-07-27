# streaming bloom distinct

**Language:** Rust · **Sphere:** rust · **Category:** composed-systems

**Signature:** `(item: &str) → Vec<usize>`

## What it does

composes: parse-stream + k-hash-bloom-membership + cardinality-estimate-from-fill

A real k-hash bloom filter (not a single bit). Membership guarantees NO false negatives, and
the DISTINCT count is ESTIMATED FROM THE BLOOM ITSELF (via the fill ratio), not read off an
exact set — n ≈ -(m/k)·ln(1 - X/m), where X = set bits, m = size, k = hashes. We check the
estimate against the true cardinality (computed only as the test oracle).

## Guarantee

When it runs, streaming bloom distinct guarantees assert!(err < 0.15, "bloom fill-ratio estimate {est:.1} within 15% of true {true_distinct} (err {err:.3})"); assert!(bloom.set_bits() > true_distinct, "k-hash bloom sets more bits than there are items") (weak-grade: proven by rustc-run).

**Checkable constraints:**

- `assert!(bloom.contains(item), "bloom must never give a false negative")`
- `assert!(err < 0.15, "bloom fill-ratio estimate {est:.1} within 15% of true {true_distinct} (err {err:.3})")`
- `assert!(bloom.set_bits() > true_distinct, "k-hash bloom sets more bits than there are items")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
