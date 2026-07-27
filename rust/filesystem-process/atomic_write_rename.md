# atomic write rename

**Language:** Rust · **Sphere:** rust · **Category:** filesystem-process

**Signature:** `(target: &str, content: &str) → Result<(), Box<dyn std::error::Error>>`

## What it does

atomic_write_rename — temp-write+rename atomicity; partial never visible; cleans up.

Core idea: write to a temp file, then rename atomically to the target. This prevents
partial visibility. THE ONE LAW: write content to temp, assert target does NOT exist
before rename, perform rename, assert target NOW holds the FULL content, then clean up.
A broken rename or missing cleanup would fail.
When to use: atomic config updates, crash-safe writes, database snapshots.

## Guarantee

When it runs, atomic write rename guarantees assert_eq!(target_content, content, "target must have full content after rename") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(temp_content, content, "temp file must have correct content")`
- `assert!(!target_exists_before, "target must not exist before rename (simulated in test)")`
- `assert_eq!(target_content, content, "target must have full content after rename")`
- `assert!(!temp_path.exists(), "temp file must be gone after rename")`
- `assert_eq!(read_back, content1, "written content must match")`
- `assert_eq!(read_back.len(), content2.len(), "full content must be present")`
- `assert_eq!(read_back, content2, "written content must match exactly")`
- `assert!(!stale_temp.exists(), "temp file must be cleaned up")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
