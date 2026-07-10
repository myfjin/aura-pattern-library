#!/usr/bin/env python3
"""
Partition Management Pattern
Manage partitions (e.g., date-based, range-based).
Track which partitions are closed (immutable), which are open (mutable).
Assert: no reprocessing closed partitions, exactly-once per partition.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import json
import tempfile
import os


def process_partitioned(records, partition_meta_path):
    """
    Records belong to partitions (e.g., date).
    Track: which partitions are closed (no more records).
    """
    partition_meta = {'closed': [], 'processed_count': {}}
    if os.path.exists(partition_meta_path):
        try:
            with open(partition_meta_path, 'r') as f:
                partition_meta = json.load(f)
        except (json.JSONDecodeError, IOError):
            partition_meta = {'closed': [], 'processed_count': {}}

    output = []

    for record in records:
        partition = record['partition']

        # If partition is closed, skip
        if partition in partition_meta['closed']:
            continue

        # Process record
        output.append({
            'id': record['id'],
            'partition': partition,
            'value': record['value']
        })

        # Update count for this partition
        if partition not in partition_meta['processed_count']:
            partition_meta['processed_count'][partition] = 0
        partition_meta['processed_count'][partition] += 1

    # Check if any partitions should be closed
    # Close partition if it has max 2 records (arbitrary rule)
    max_per_partition = 2
    for partition, count in partition_meta['processed_count'].items():
        if count >= max_per_partition and partition not in partition_meta['closed']:
            partition_meta['closed'].append(partition)

    with open(partition_meta_path, 'w') as f:
        json.dump(partition_meta, f)

    return output, partition_meta


def test_partition_manage():
    """
    Process records from partitions 'p1' (2 records) and 'p2' (3 records).
    Close 'p1' when full, keep 'p2' open.
    Assert: 'p1' not reprocessed, 'p2' accepts more.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        meta_path = os.path.join(tmpdir, 'partition.json')

        # Batch 1: p1 gets 2 records, p2 gets 1
        records1 = [
            {'id': 'a', 'partition': 'p1', 'value': 10},
            {'id': 'b', 'partition': 'p1', 'value': 20},
            {'id': 'c', 'partition': 'p2', 'value': 30}
        ]

        output1, meta1 = process_partitioned(records1, meta_path)
        assert len(output1) == 3, f"Expected 3 processed, got {len(output1)}"
        assert 'p1' in meta1['closed'], "p1 should be closed after 2 records"
        assert 'p2' not in meta1['closed'], "p2 should still be open"

        # Batch 2: try to add more to p1 (should be skipped), add to p2
        records2 = [
            {'id': 'x', 'partition': 'p1', 'value': 100},  # Should be skipped
            {'id': 'd', 'partition': 'p2', 'value': 40},
            {'id': 'e', 'partition': 'p2', 'value': 50}
        ]

        output2, meta2 = process_partitioned(records2, meta_path)
        assert len(output2) == 2, f"Expected 2 processed (p1 skipped), got {len(output2)}"

        # Verify p1 record was skipped
        p1_ids_in_output2 = [r['id'] for r in output2 if r['partition'] == 'p1']
        assert len(p1_ids_in_output2) == 0, f"p1 records in batch 2: {p1_ids_in_output2}"

        # Verify p2 records were added
        p2_ids = [r['id'] for r in output2 if r['partition'] == 'p2']
        assert set(p2_ids) == {'d', 'e'}, f"p2 records: {p2_ids}"


def test_partition_closed_immutable():
    """
    Assert: closed partition never reprocesses records.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        meta_path = os.path.join(tmpdir, 'partition.json')

        # Close 'p1' by processing 2 records
        records1 = [
            {'id': 'a', 'partition': 'p1', 'value': 10},
            {'id': 'b', 'partition': 'p1', 'value': 20}
        ]
        output1, _ = process_partitioned(records1, meta_path)
        assert len(output1) == 2

        # Try to reprocess same partition (with same or different records)
        records2 = [
            {'id': 'a', 'partition': 'p1', 'value': 10},  # Same ID
            {'id': 'b', 'partition': 'p1', 'value': 20}   # Same ID
        ]
        output2, _ = process_partitioned(records2, meta_path)
        assert len(output2) == 0, "Closed partition should not reprocess"


def test_failure_no_partition_tracking():
    """
    Counter-example: code without partition closing.
    """
    def buggy_process(records):
        """No partition tracking: always processes."""
        return [{'id': r['id'], 'partition': r['partition']} for r in records]

    records1 = [
        {'id': 'a', 'partition': 'p1', 'value': 10},
        {'id': 'b', 'partition': 'p1', 'value': 20}
    ]
    records2 = [
        {'id': 'a', 'partition': 'p1', 'value': 10},  # Duplicate
        {'id': 'b', 'partition': 'p1', 'value': 20}   # Duplicate
    ]

    output1 = buggy_process(records1)
    output2 = buggy_process(records2)

    # Bug: both batches process partition p1 fully, can cause duplicates
    assert len(output1) == 2
    assert len(output2) == 2


if __name__ == '__main__':
    test_partition_manage()
    test_partition_closed_immutable()
    test_failure_no_partition_tracking()
    print("✓ partition_manage passed")
