#!/usr/bin/env python3
"""
HEADLINE PATTERN: Idempotent ETL Step
Simulates pipeline crash mid-transformation, resumes from checkpoint,
asserts output is bit-identical and no duplicates despite replayed input.
THE ONE LAW: An idempotent transform produces identical output when run once
or replayed after crash. Counter-example: reading from offset N then
restarting from offset 0 produces duplicates.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import json
import tempfile
import os
import hashlib
from pathlib import Path


def stable_checksum(value):
    """Process-stable checksum (NOT the builtin hash(), which is PYTHONHASHSEED-salted
    and would differ across a real crash/resume process boundary)."""
    return int(hashlib.sha256(str(value).encode()).hexdigest()[:8], 16)


def idempotent_transform(records, checkpoint_path):
    """
    Transform records with write-ahead checkpoint before each record.
    Checkpoint holds (record_id, hash_of_output).
    On resume, skip records already checkpointed.
    """
    checkpoint = {}
    if os.path.exists(checkpoint_path):
        try:
            with open(checkpoint_path, 'r') as f:
                checkpoint = json.load(f)
        except (json.JSONDecodeError, IOError):
            checkpoint = {}

    output = []
    for record in records:
        rid = record['id']
        # Skip if already processed
        if rid in checkpoint:
            output.append(json.loads(checkpoint[rid]['output']))
            continue

        # Transform
        transformed = {
            'id': rid,
            'value': record['value'] * 2,
            'checksum': stable_checksum(record['value'])
        }
        output_json = json.dumps(transformed, sort_keys=True)

        # Checkpoint BEFORE adding to output (write-ahead)
        checkpoint[rid] = {'output': output_json}
        with open(checkpoint_path, 'w') as f:
            json.dump(checkpoint, f)

        output.append(transformed)

    return output


def test_idempotent_etl():
    """
    Test: Run ETL once fully, then simulate crash and replay.
    Assert: Output is identical, no duplicates.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        checkpoint_path = os.path.join(tmpdir, 'checkpoint.json')
        records = [
            {'id': 'a', 'value': 10},
            {'id': 'b', 'value': 20},
            {'id': 'c', 'value': 30}
        ]

        # First run: full transform
        output1 = idempotent_transform(records, checkpoint_path)
        assert len(output1) == 3, f"Expected 3 records, got {len(output1)}"

        # Simulate crash by truncating checkpoint (partial state)
        with open(checkpoint_path, 'r') as f:
            ckpt = json.load(f)
        partial = {k: ckpt[k] for k in list(ckpt.keys())[:2]}  # Keep only first 2
        with open(checkpoint_path, 'w') as f:
            json.dump(partial, f)

        # Resume from checkpoint
        output2 = idempotent_transform(records, checkpoint_path)
        assert len(output2) == 3, f"After resume, expected 3, got {len(output2)}"

        # Verify identical
        def norm(recs):
            return sorted([json.dumps(r, sort_keys=True) for r in recs])

        assert norm(output1) == norm(output2), "Outputs differ after crash+resume"

        # Verify no duplicates by ID
        ids = [r['id'] for r in output2]
        assert len(ids) == len(set(ids)), f"Duplicate IDs detected: {ids}"

        # Verify checksums match (output integrity)
        for r in output2:
            expected_checksum = stable_checksum(r['value'] // 2)
            assert r['checksum'] == expected_checksum, \
                f"Checksum mismatch for {r['id']}: got {r['checksum']}, expected {expected_checksum}"


def test_failure_non_idempotent():
    """
    Counter-example: naive offset-based resume.
    Simulates buggy code that doesn't track per-record state.
    """
    def buggy_transform(records, last_offset):
        """Buggy: resumes from offset, doesn't deduplicate."""
        return records[last_offset:]

    records = [{'id': 'a'}, {'id': 'b'}, {'id': 'c'}]

    # First run: transform all
    output1 = buggy_transform(records, 0)
    assert len(output1) == 3

    # "Resume" from last_offset=0 (buggy: we forgot to update offset)
    output2 = buggy_transform(records, 0)
    assert len(output2) == 3

    # Failure case: if we replay and naively append, we get duplicates
    combined = output1 + output2
    assert len(combined) == 6  # Duplicated!
    assert len(set(r['id'] for r in combined)) == 3  # Only 3 unique IDs
    # This would be the bug: assert len(combined) != 6 to catch it


if __name__ == '__main__':
    test_idempotent_etl()
    test_failure_non_idempotent()
    print("✓ idempotent_etl_step passed")
