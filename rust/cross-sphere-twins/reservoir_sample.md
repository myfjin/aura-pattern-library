# reservoir sample

**Language:** Rust · **Sphere:** rust · **Category:** cross-sphere-twins

**Signature:** `() → Vec<u32>`

## What it does

reservoir_sample — Algorithm R; UNIFORM over the stream, seeded-deterministic.

Core idea: keep a size-k reservoir. The first k items fill it; the i-th item thereafter
(i = total seen) replaces a uniformly-random reservoir slot with probability k/i. The
defining property is UNIFORMITY: after the stream, every element is in the sample with
probability k/n. THE LAW: a broken sampler using a constant probability (k/(k+1) instead
of k/i) is NOT uniform — so we assert, over many seeds, that each element's inclusion
frequency converges to k/n, plus determinism and valid-subset. When to use: streaming
uniform samples, online data collection.

## Guarantee

When it runs, reservoir sample guarantees assert_eq!(run(&[1, 2], 3, 7).len(), 2, "n<k keeps everything") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(run(&stream, k, 42), run(&stream, k, 42), "same seed → same sample")`
- `assert_eq!(s.len(), k, "sample size is k")`
- `assert!(stream.contains(&x), "sample element {x} came from the stream")`
- `assert_eq!(run(&[1, 2], 3, 7).len(), 2, "n<k keeps everything")`
- `assert!((freq - expected).abs() / expected < 0.06, "element {x} inclusion freq {freq} deviates >6% from uniform {expected} (non-uniform sampler)",)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
