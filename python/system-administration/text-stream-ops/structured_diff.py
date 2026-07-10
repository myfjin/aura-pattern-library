#!/usr/bin/env python3
"""
structured_diff: Diff two structured outputs (e.g., process lists, config states).
THE ONE LAW: Parse both versions, identify exact adds/removes/changes.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

def diff_lines(before, after):
    """
    Diff two lists of lines.
    Return dict {added, removed, unchanged}.
    """
    before_set = set(before)
    after_set = set(after)

    added = [line for line in after if line not in before_set]
    removed = [line for line in before if line not in after_set]
    unchanged = [line for line in before if line in after_set]

    return {
        'added': sorted(added),
        'removed': sorted(removed),
        'unchanged': sorted(unchanged)
    }

def diff_structured_output(before_text, after_text, key_field=None):
    """
    Diff structured outputs (e.g., ps, netstat).
    Parse lines into fields, identify changes by key field.
    Return dict {added, removed, changed, unchanged}.
    """
    before_lines = before_text.strip().split('\n')
    after_lines = after_text.strip().split('\n')

    # Simple line-based diff if no key field specified.
    if key_field is None:
        return diff_lines(before_lines, after_lines)

    # Parse into dicts by key field.
    before_dict = {}
    for line in before_lines:
        parts = line.split()
        if len(parts) > key_field:
            key = parts[key_field]
            before_dict[key] = line

    after_dict = {}
    for line in after_lines:
        parts = line.split()
        if len(parts) > key_field:
            key = parts[key_field]
            after_dict[key] = line

    # Identify changes.
    added = [after_dict[k] for k in after_dict if k not in before_dict]
    removed = [before_dict[k] for k in before_dict if k not in after_dict]
    changed = [after_dict[k] for k in after_dict if k in before_dict and after_dict[k] != before_dict[k]]
    unchanged = [before_dict[k] for k in before_dict if k in after_dict and after_dict[k] == before_dict[k]]

    return {
        'added': sorted(added),
        'removed': sorted(removed),
        'changed': sorted(changed),
        'unchanged': sorted(unchanged)
    }

def main():
    # Synthetic process list (before and after), keyed by first field (PID).
    before = """1000 alice   /bin/bash
2000 bob     /usr/bin/python
3000 charlie /bin/sh"""

    after = """1000 alice   /bin/bash
2000 bob     /usr/bin/python3
4000 dave    /bin/zsh"""

    # Use key_field=0 to diff by PID (first field).
    diff = diff_structured_output(before, after, key_field=0)

    # Verify changes.
    assert len(diff['removed']) == 1, f"Should have 1 removed, got {len(diff['removed'])}: {diff['removed']}"
    assert len(diff['added']) == 1, f"Should have 1 added, got {len(diff['added'])}: {diff['added']}"
    assert len(diff['changed']) == 1, f"Should have 1 changed, got {len(diff['changed'])}: {diff['changed']}"
    assert len(diff['unchanged']) == 1, f"Should have 1 unchanged, got {len(diff['unchanged'])}: {diff['unchanged']}"

    # Verify exact content.
    assert '3000' in diff['removed'][0], "Charlie (3000) should be removed"
    assert '4000' in diff['added'][0], "Dave (4000) should be added"
    assert 'python3' in diff['changed'][0], "Bob's command changed to python3"
    assert 'alice' in diff['unchanged'][0], "Alice (1000) unchanged"

    # FAILURE SIMULATION: Not detecting changes.
    def diff_structured_output_broken(before_text, after_text):
        """Broken: returns empty diffs."""
        return {'added': [], 'removed': [], 'changed': [], 'unchanged': []}

    broken = diff_structured_output_broken(before, after)
    assert broken['added'] == [], "Broken should have empty added"
    assert len(diff['added']) > 0, "Real diff should have additions"

    # Test with line-based diff (no key field).
    simple_before = "line_a\nline_b\nline_c"
    simple_after = "line_a\nline_b\nline_d"
    simple_diff = diff_lines(simple_before.split('\n'), simple_after.split('\n'))
    assert simple_diff['added'] == ['line_d'], "Should detect added line"
    assert simple_diff['removed'] == ['line_c'], "Should detect removed line"
    assert simple_diff['unchanged'] == ['line_a', 'line_b'], "Should detect unchanged"

    # Edge case: No changes.
    no_change_diff = diff_lines(['A', 'B'], ['A', 'B'])
    assert no_change_diff['added'] == [], "No additions"
    assert no_change_diff['removed'] == [], "No removals"
    assert no_change_diff['unchanged'] == ['A', 'B'], "All unchanged"

    # Edge case: Complete replacement.
    complete_diff = diff_lines(['A', 'B'], ['X', 'Y'])
    assert complete_diff['added'] == ['X', 'Y'], "All new"
    assert complete_diff['removed'] == ['A', 'B'], "All old removed"
    assert complete_diff['unchanged'] == [], "Nothing unchanged"

    # Verify exact sorted order of diffs.
    unsorted_before = "z\na\nm"
    unsorted_after = "a\nm\nx"
    unsorted_diff = diff_lines(unsorted_before.split('\n'), unsorted_after.split('\n'))
    assert unsorted_diff['added'] == ['x'], "Added should be sorted"
    assert unsorted_diff['removed'] == ['z'], "Removed should be sorted"
    assert unsorted_diff['unchanged'] == ['a', 'm'], "Unchanged should be sorted"

    print("✓ structured_diff passed")

if __name__ == '__main__':
    main()
