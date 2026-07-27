# checkpoint resume

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 19 · Data pipeline ops

**Signature:** `(records: List[dict], checkpoint_path: str) → ?`

## What it does

Checkpoint/Resume Pattern
Simulates crash inside batch processing, resumes from last checkpoint,
asserts exactly-once processing and correct output.

## Guarantee

When it runs, checkpoint resume guarantees output1[0]['processed'] == 101; len(output1) == 2; len(full_output) == 4 (proven by run).

**Checkable constraints:**

- `len(output1) == 2`
- `output1[0]['processed'] == 101`
- `len(full_output) == 4`
- `ids == ['a', 'b', 'c', 'd']`
- `len(set(ids)) == len(ids)`
- `r['processed'] == expected.get(r['id'])`
- `len(output1) == 2`
- `len(output2) == 2`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — chaos, xlang (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def process_batch_with_checkpoint(records, checkpoint_path):`
**Valid input:** `records` is a list of dicts with `'id'` and `'value'`; `checkpoint_path` is a writable JSON path; batch size is fixed at 2.
**Core:** Processes records in batches of 2, writing a checkpoint (`batches_done` with batch id → processed records) after each batch commits; on resume, completed batches are replayed from the checkpoint.
**Assert:** Four records processed after a simulated crash after batch 0 yield all four records exactly once, in order, with `processed == value + 100`.
**⚠️ Defect:** The checkpoint stores full record outputs, so it grows linearly with input size. The batch size is hardcoded to 2. There is no cleanup of old checkpoints, and an interrupted checkpoint write leaves a partial JSON file that will crash the next run.

---
*△ AURA Pattern Library — © Reality Optimizer*
