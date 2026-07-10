#!/usr/bin/env python3
"""
Checkpoint/Resume Pattern
Simulates crash inside batch processing, resumes from last checkpoint,
asserts exactly-once processing and correct output.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import json
import tempfile
import os


def process_batch_with_checkpoint(records, checkpoint_path):
    """
    Process records in batches of 2. Checkpoint after each batch commits.
    On resume, skip completed batches. Store processed results in checkpoint.
    """
    checkpoint = {'batches_done': {}}  # batch_id -> list of processed records
    if os.path.exists(checkpoint_path):
        try:
            with open(checkpoint_path, 'r') as f:
                checkpoint = json.load(f)
        except (json.JSONDecodeError, IOError):
            checkpoint = {'batches_done': {}}

    output = []
    batch_size = 2

    for i in range(0, len(records), batch_size):
        batch_id = str(i // batch_size)
        if batch_id in checkpoint['batches_done']:
            # Skip: batch already processed, retrieve from checkpoint
            output.extend(checkpoint['batches_done'][batch_id])
            continue

        batch = records[i:i+batch_size]
        # Process batch
        processed = [{'id': r['id'], 'processed': r['value'] + 100} for r in batch]
        output.extend(processed)

        # Checkpoint: mark batch as done with results
        checkpoint['batches_done'][batch_id] = processed
        with open(checkpoint_path, 'w') as f:
            json.dump(checkpoint, f)

    return output


def test_checkpoint_resume():
    """
    Simulate crash after 1 batch, resume and process remaining.
    Assert: All records processed exactly once.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        checkpoint_path = os.path.join(tmpdir, 'checkpoint.json')
        records = [
            {'id': 'a', 'value': 1},
            {'id': 'b', 'value': 2},
            {'id': 'c', 'value': 3},
            {'id': 'd', 'value': 4}
        ]

        # Run first batch
        output1 = process_batch_with_checkpoint(records[:2], checkpoint_path)
        assert len(output1) == 2, f"Expected 2 after first batch, got {len(output1)}"
        assert output1[0]['processed'] == 101

        # Simulate crash: manually truncate checkpoint to first batch only
        with open(checkpoint_path, 'w') as f:
            json.dump({'batches_done': {'0': output1}}, f)

        # Resume with full input
        full_output = process_batch_with_checkpoint(records, checkpoint_path)
        assert len(full_output) == 4, f"Expected 4 total, got {len(full_output)}"

        # Verify each record processed exactly once
        ids = [r['id'] for r in full_output]
        assert ids == ['a', 'b', 'c', 'd'], f"Order mismatch: {ids}"
        assert len(set(ids)) == len(ids), "Duplicate IDs"

        # Verify values transformed
        for r in full_output:
            expected = {'a': 101, 'b': 102, 'c': 103, 'd': 104}
            assert r['processed'] == expected.get(r['id']), \
                f"Invalid processed value for {r['id']}: {r['processed']}"


def test_failure_missing_checkpoint():
    """
    Counter-example: code that forgets to checkpoint.
    Verify that without checkpointing, replayed input is duplicated.
    """
    def buggy_process(records):
        """No checkpoint: always processes all records."""
        return [{'id': r['id'], 'processed': r['value'] + 100} for r in records]

    records = [{'id': 'a', 'value': 1}, {'id': 'b', 'value': 2}]

    # First run
    output1 = buggy_process(records)
    assert len(output1) == 2

    # Simulate "resume" by calling again with same input
    output2 = buggy_process(records)
    assert len(output2) == 2

    # Concatenating outputs shows duplication (the bug)
    combined = output1 + output2
    assert len(combined) == 4  # Duplicated!


if __name__ == '__main__':
    test_checkpoint_resume()
    test_failure_missing_checkpoint()
    print("✓ checkpoint_resume passed")
