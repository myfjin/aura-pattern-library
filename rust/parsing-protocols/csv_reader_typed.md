# csv reader typed

**Language:** Rust · **Sphere:** rust · **Category:** parsing-protocols

**Signature:** `(s: &str) → FieldType`

## What it does

csv_reader_typed — quoted-field CSV split + type inference; matches planted rows.

Core idea: parse CSV with proper quote handling, split into rows, infer field types
(int, float, string). THE ONE LAW: plant CSV with quoted fields, escaped quotes, and
mixed types, parse it, then assert row count, field count, and inferred types match
the planted data — a naive split on comma would fail on quoted fields containing commas.
When to use: data ingestion, CSV→DB import, columnar type detection.

## Guarantee

When it runs, csv reader typed guarantees assert_eq!(rows.len(), 4, "row count mismatch"); assert_eq!(row.len(), 4, "field count mismatch"); assert_eq!(rows[0][0], "Alice") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(rows.len(), 4, "row count mismatch")`
- `assert_eq!(row.len(), 4, "field count mismatch")`
- `assert_eq!(rows[0][0], "Alice")`
- `assert_eq!(rows[0][1], "30")`
- `assert_eq!(rows[0][2], "95.5")`
- `assert_eq!(rows[0][3], "She scored well")`
- `assert_eq!(rows[2][0], "Smith, John", "quoted field with comma failed")`
- `assert_eq!(rows[2][1], "45")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
