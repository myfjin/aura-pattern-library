# content addressed store

**Language:** Rust · **Sphere:** rust · **Category:** composed-systems

**Signature:** `(store: &mut BlobStore, blob: &[u8]) → [u8`

## What it does

content_addressed_store — blobs keyed by SHA-256; identical content dedups; corruption detected.

Core idea: store blobs by their SHA-256 hash (content-addressed). Identical content
naturally dedups. A corruption (bit flip) is caught when the retrieved blob's hash
doesn't match the key. THE LAW: store N blobs, corrupt one, retrieve, and assert
the corrupted blob's hash doesn't match its key — proving the store detects tampering.
When to use: content-addressed storage, Git objects, dedup systems, integrity.

## Guarantee

When it runs, content addressed store guarantees assert_eq!(retrieved, blob1.to_vec()); assert_eq!(hash1, hash2, "identical content has same hash"); assert_eq!(&retrieved, &blob.to_vec(), "blob {i} matches") (weak-grade: proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(retrieved, blob1.to_vec())`
- `assert!(verify(&retrieved, &hash1), "blob verifies against its hash")`
- `assert_eq!(hash1, hash2, "identical content has same hash")`
- `assert!(!verify(&corrupted, &hash1), "corrupted blob fails verification")`
- `assert_eq!(&retrieved, &blob.to_vec(), "blob {i} matches")`
- `assert!(retrieve(&blob_store, &fake_hash).is_none(), "missing blob is None")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **hard** — chaos (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
