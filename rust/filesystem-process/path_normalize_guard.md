# path normalize guard

**Language:** Rust · **Sphere:** rust · **Category:** filesystem-process

**Signature:** `(path: &str, base: &str) → Result<String, String>`

## What it does

path_normalize_guard — normalize + traversal-escape guard; ../ escapes blocked.

Core idea: normalize paths and prevent directory traversal attacks (e.g., ../../etc).
THE ONE LAW: plant a path with ../.. sequences, normalize it, assert it stays within
the base directory and traversal escapes are blocked.
When to use: web servers, file handlers, security boundaries.

## Guarantee

When it runs, path normalize guard guarantees assert_eq!(norm1, "/home/user/data/subdir/file.txt"); assert_eq!(norm2, "/home/user/data/subdir/file.txt"); assert_eq!(norm3, "/home/user/data/subdir/file.txt") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(norm1, "/home/user/data/subdir/file.txt")`
- `assert!(is_under_base(&norm1, base), "should be under base")`
- `assert_eq!(norm2, "/home/user/data/subdir/file.txt")`
- `assert_eq!(norm3, "/home/user/data/subdir/file.txt")`
- `assert!(is_under_base(&norm3, base), "should still be under base")`
- `assert!(result1.is_err(), "escape attempt should be rejected")`
- `assert!(result2.is_err(), "deep escape attempt should be rejected")`
- `assert_eq!(norm4, "/home/user/data")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
