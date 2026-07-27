# file dedup hash

**Language:** Rust · **Sphere:** rust · **Category:** filesystem-process

**Signature:** `(data: &[u8]) → u64`

## What it does

file_dedup_hash — group synthetic file table by content hash; planted dupes grouped.

Core idea: hash file contents, group files by hash, identify duplicates.
THE ONE LAW: plant a table of files with known duplicates, compute hashes, group
by hash, and assert duplicates are correctly grouped and unique files are singletons.
A broken hash or missing grouping would fail.
When to use: deduplication, backup, storage optimization, file integrity.

## Guarantee

When it runs, file dedup hash guarantees assert_eq!(groups.len(), 3, "should have 3 unique content hashes"); assert_eq!(hello_group.len(), 3, "hello should have 3 duplicates"); assert_eq!(groups[&world_hash].len(), 1, "world should be singleton") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(groups.len(), 3, "should have 3 unique content hashes")`
- `assert!(groups.contains_key(&hello_hash), "hello hash should exist")`
- `assert_eq!(hello_group.len(), 3, "hello should have 3 duplicates")`
- `assert!(hello_group.contains(&"a.txt".to_string()))`
- `assert!(hello_group.contains(&"b.txt".to_string()))`
- `assert!(hello_group.contains(&"d.txt".to_string()))`
- `assert_eq!(groups[&world_hash].len(), 1, "world should be singleton")`
- `assert_eq!(groups[&goodbye_hash].len(), 1, "goodbye should be singleton")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
