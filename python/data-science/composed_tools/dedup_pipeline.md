# dedup pipeline

**Language:** Python · **Sphere:** data-science · **Category:** Composed Tools

**Signature:** `(docs: List[str], cand_thresh: float, verify_ratio: float) → ?`

## What it does

Three-Stage Dedup Pipeline — find fast, verify exactly, explain honestly.

CROSS-SPHERE COMPOSED PATTERN (three parents): minhash_dedup (DS) generates
candidate pairs cheaply, edit_distance (DS/Text) VERIFIES them exactly, and
diff_engine (programming sphere, awesome-python-patterns) EXPLAINS what
actually differs — embedding bridges 0.545/0.530/0.486, found 2026-07-06.
Each stage covers the previous one's weakness: MinHash is fast but
approximate, edit distance is exact but O(n*m) per pair, a diff is readable
but only worth computing for confirmed near-duplicates.

Use when: deduplicating document collections where all-pairs exact comparison
is too expensive and silent deletion is unacceptable (the diff is the audit).

## Guarantee

When it runs, dedup pipeline guarantees set(planted) <= set(verified); all((p in planted for p in verified)); len(candidates) < 0.2 * total_pairs (weak-grade: directional, proven by run).

**Checkable constraints:**

- `set(planted) <= set(verified)`
- `all((p in planted for p in verified))`
- `len(candidates) < 0.2 * total_pairs`
- `any((tok.startswith(('-', '+')) for tok in sample))`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **hard** — positive, xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
