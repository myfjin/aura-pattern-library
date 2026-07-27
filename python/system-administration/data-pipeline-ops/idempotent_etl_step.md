# idempotent etl step

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 19 · Data pipeline ops

**Signature:** `(records: List[dict], checkpoint_path: str) → ?`

## What it does

HEADLINE PATTERN: Idempotent ETL Step
Simulates pipeline crash mid-transformation, resumes from checkpoint,
asserts output is bit-identical and no duplicates despite replayed input.
THE ONE LAW: An idempotent transform produces identical output when run once
or replayed after crash. Counter-example: reading from offset N then
restarting from offset 0 produces duplicates.

## Guarantee

When it runs, idempotent etl step guarantees r['checksum'] == expected_checksum; len(output1) == 3; len(output2) == 3 (proven by run).

**Checkable constraints:**

- `len(output1) == 3`
- `len(output2) == 3`
- `norm(output1) == norm(output2)`
- `len(ids) == len(set(ids))`
- `r['checksum'] == expected_checksum`
- `len(output1) == 3`
- `len(output2) == 3`
- `len(combined) == 6`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — chaos (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def idempotent_transform(records, checkpoint_path):`, `def stable_checksum(value):`
**Valid input:** `records` is a list of dicts with `'id'` and `'value'`; `checkpoint_path` is a writable JSON path.
**Core:** Transforms each record (`value * 2` + SHA-256-derived checksum) and checkpoints the serialized output keyed by record ID before adding it to the output; on resume, already-checkpointed IDs are replayed from the checkpoint.
**Assert:** Full transform and crash/resume transform produce identical, duplicate-free outputs; checksums match the original value.
**⚠️ Defect:** The checkpoint is overwritten after every single record, so throughput is low for large inputs. The checksum uses only the first 8 hex chars of SHA-256, which is much weaker than a full hash. The function mutates/checkpoints based on `'id'` only, so a record whose value changes between runs would still be skipped.

---
*△ AURA Pattern Library — © Reality Optimizer*
