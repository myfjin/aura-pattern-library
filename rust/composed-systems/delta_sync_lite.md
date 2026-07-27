# delta sync lite

**Language:** Rust · **Sphere:** rust · **Category:** composed-systems

**Signature:** `(block: &[u8]) → u64`

## What it does

delta_sync_lite — rsync-style block delta: match shared blocks old↔new, transfer + RECONSTRUCT.

Core idea: chunk OLD into fixed blocks and index them by hash. Scan NEW: where a window
matches an old block, emit a COPY(offset) (no data sent); otherwise emit a LITERAL byte. The
delta = that op stream. Applying the delta against OLD must reconstruct NEW EXACTLY — that
reconstruction is the whole point (a rolling hash alone does not sync). THE LAW: build the
delta, reconstruct and assert bytes-identical to NEW, prove blocks were actually reused (fewer
literals than a full copy), then CORRUPT the source and assert reconstruction diverges.
When to use: rsync-like transfer, incremental backup, block dedup.

## Guarantee

When it runs, delta sync lite guarantees assert_eq!(ops_same.iter().filter(|o| matches!(o, Op::Literal(_))).count(), 0, "identical → no literals") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(rebuilt, new, "reconstruction must equal NEW exactly")`
- `assert!(copies > 0, "at least one shared block must be COPY-referenced")`
- `assert!(literals < new.len(), "delta sends fewer literals than the whole file ({literals} < {})", new.len())`
- `assert_eq!(apply(&old, &ops_same), old, "identical inputs reconstruct exactly")`
- `assert_eq!(ops_same.iter().filter(|o| matches!(o, Op::Literal(_))).count(), 0, "identical → no literals")`
- `assert_ne!(rebuilt_bad, new, "corrupting the copy source must break reconstruction")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
