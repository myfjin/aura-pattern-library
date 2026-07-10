#!/usr/bin/env python3
"""
Replay-Safe Pattern
Guarantee that replaying operations produces identical output.
Assert: first run and replay produce same result, idempotency holds.
Key: operations must be commutative and state-independent within a batch.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import json
import tempfile
import os


def replay_safe_aggregate(records, state_path):
    """
    Aggregate records into a summary.
    On replay, clear state and recalculate from records.
    """
    state = {'sum': 0, 'count': 0, 'max': None, 'min': None}
    if os.path.exists(state_path):
        try:
            with open(state_path, 'r') as f:
                state = json.load(f)
        except (json.JSONDecodeError, IOError):
            state = {'sum': 0, 'count': 0, 'max': None, 'min': None}

    # For replay-safety, recalculate from scratch rather than accumulating
    state = {'sum': 0, 'count': 0, 'max': None, 'min': None}

    for record in records:
        value = record['value']
        state['sum'] += value
        state['count'] += 1
        state['max'] = value if state['max'] is None else max(state['max'], value)
        state['min'] = value if state['min'] is None else min(state['min'], value)

    # Persist state
    with open(state_path, 'w') as f:
        json.dump(state, f)

    return state


def test_replay_safe():
    """
    Run aggregation, note result, clear state, run again with same input.
    Assert: output is identical (replay-safe).
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        state_path = os.path.join(tmpdir, 'state.json')

        records = [
            {'id': 'a', 'value': 10},
            {'id': 'b', 'value': 20},
            {'id': 'c', 'value': 30},
            {'id': 'd', 'value': 5}
        ]

        # First run
        state1 = replay_safe_aggregate(records, state_path)
        assert state1['sum'] == 65, f"Expected sum 65, got {state1['sum']}"
        assert state1['count'] == 4, f"Expected count 4, got {state1['count']}"
        assert state1['max'] == 30, f"Expected max 30, got {state1['max']}"
        assert state1['min'] == 5, f"Expected min 5, got {state1['min']}"

        # Clear state file (simulating fresh start/replay)
        if os.path.exists(state_path):
            os.remove(state_path)

        # Replay with same input
        state2 = replay_safe_aggregate(records, state_path)

        # Assert: identical output
        assert state1 == state2, f"Replay mismatch: {state1} != {state2}"
        assert state2['sum'] == 65
        assert state2['count'] == 4
        assert state2['max'] == 30
        assert state2['min'] == 5


def test_replay_order_independence():
    """
    Assert: replay with reordered input produces same aggregate.
    (Commutative aggregation)
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        state_path = os.path.join(tmpdir, 'state.json')

        records1 = [
            {'id': 'a', 'value': 10},
            {'id': 'b', 'value': 20},
            {'id': 'c', 'value': 30}
        ]

        state1 = replay_safe_aggregate(records1, state_path)

        # Reorder and replay
        records2 = [
            {'id': 'c', 'value': 30},
            {'id': 'a', 'value': 10},
            {'id': 'b', 'value': 20}
        ]

        if os.path.exists(state_path):
            os.remove(state_path)

        state2 = replay_safe_aggregate(records2, state_path)

        # Assert: same aggregate despite order
        assert state1['sum'] == state2['sum']
        assert state1['max'] == state2['max']
        assert state1['min'] == state2['min']
        assert state1['count'] == state2['count']


def test_failure_stateful_accumulation():
    """
    Counter-example: code that accumulates state across replays.
    """
    class StatefulBuggy:
        def __init__(self):
            self.sum = 0

        def aggregate(self, records):
            # Bug: accumulates across calls
            for r in records:
                self.sum += r['value']
            return self.sum

    bug = StatefulBuggy()

    records = [{'value': 10}, {'value': 20}, {'value': 30}]

    # First run
    result1 = bug.aggregate(records)
    assert result1 == 60

    # Replay: bug accumulates again!
    result2 = bug.aggregate(records)
    assert result2 == 120  # Bug: should be 60 again

    # Not replay-safe
    assert result1 != result2


if __name__ == '__main__':
    test_replay_safe()
    test_replay_order_independence()
    test_failure_stateful_accumulation()
    print("✓ replay_safe passed")
