# quorum write

**Language:** Rust · **Sphere:** rust · **Category:** cross-sphere-twins

**Signature:** `(key: String, value: String) → ?`

## What it does

quorum_write — N replicas, majority-ack required; minority partition refuses write.

Core idea: a write succeeds only if a majority of N replicas acknowledge. A minority
partition cannot succeed a write. THE LAW: split into majority and minority, attempt
a write on the minority, and assert it fails; majority succeeds.
When to use: quorum-based consensus, distributed databases, CRDT syncing.

## Guarantee

When it runs, quorum write guarantees assert_eq!(result, Some("value1".to_string())); assert_eq!(result2, None, "key2 not in majority") (weak-grade: proven by rustc-run).

**Checkable constraints:**

- `assert!(store.write("key1".to_string(), "value1".to_string(), &majority).is_ok(), "majority write succeeds")`
- `assert!(store.write("key2".to_string(), "value2".to_string(), &minority).is_err(), "minority write fails")`
- `assert_eq!(result, Some("value1".to_string()))`
- `assert_eq!(result2, None, "key2 not in majority")`
- `assert!(store.write("key3".to_string(), "value3".to_string(), &quorum).is_ok(), "exact quorum write succeeds")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
