# lineage track

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 19 · Data pipeline ops

**Signature:** `(records: List[dict], lineage_path: str) → ?`

## What it does

Lineage Tracking Pattern
Track data provenance: which source records produced which output records.
Assert: complete lineage (every output maps to at least one source),
no dangling outputs, lineage is consistent.

## Guarantee

When it runs, lineage track guarantees 'output_id' in lin (weak-grade: directional, proven by run).

**Checkable constraints:**

- `len(output) == 3`
- `found`
- `'output_id' in lin`
- `found`
- `len(lineage1) == 3`
- `len(lineage2) == 3`
- `found`
- `len(output) == 2`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def transform_with_lineage(records, lineage_path):`
**Valid input:** `records` is a list of dicts with `'id'` and `'value'`; `lineage_path` is a writable JSON path.
**Core:** Maps each input record to exactly one output record, persisting the lineage (`source_id`, `output_id`, `output_value`) before adding the output; on resume, already-tracked IDs are replayed from lineage.
**Assert:** Every output record has a matching lineage entry and every lineage entry points to an output record; after a simulated crash/resume the lineage stays consistent with no dangling references.
**⚠️ Defect:** Lineage is 1-to-1 only; patterns that fan out or fan in are not represented. The lineage file stores the full output payload, so it grows with output size. Like the other checkpoint patterns, it rewrites the entire lineage file after every record.

---
*△ AURA Pattern Library — © Reality Optimizer*
