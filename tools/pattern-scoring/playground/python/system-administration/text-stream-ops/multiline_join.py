#!/usr/bin/env python3
"""
multiline_join: Join split multiline log entries (e.g., Python stacktraces).
THE ONE LAW: Parse real messy multiline data with proper continuation detection.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import tempfile
import os

def join_multiline_logs(lines, continuation_prefix='    '):
    """
    Join multiline log entries. Lines starting with continuation_prefix
    are continuations of the previous entry.
    Return list of complete log entries.
    """
    result = []
    current_entry = None

    for line in lines:
        if line.startswith(continuation_prefix):
            # Continuation of previous entry.
            if current_entry is not None:
                current_entry += '\n' + line
        else:
            # New log entry.
            if current_entry is not None:
                result.append(current_entry)
            current_entry = line

    # Don't forget the last entry.
    if current_entry is not None:
        result.append(current_entry)

    return result

def main():
    # Synthetic multiline log data with stacktraces.
    log_data = """2024-07-10 ERROR: Division by zero
    File "app.py", line 42
    result = 10 / x
2024-07-10 WARNING: Memory low
    Available: 512MB
    Threshold: 1GB"""

    lines = log_data.strip().split('\n')
    joined = join_multiline_logs(lines)

    # Verify exact entry count and content.
    assert len(joined) == 2, f"Expected 2 entries, got {len(joined)}"
    assert joined[0].startswith('2024-07-10 ERROR'), "First entry should be ERROR"
    assert 'Division by zero' in joined[0], "Should contain error message"
    assert 'File "app.py"' in joined[0], "Should contain file reference"
    assert 'result = 10 / x' in joined[0], "Should contain code line"

    assert joined[1].startswith('2024-07-10 WARNING'), "Second entry should be WARNING"
    assert 'Memory low' in joined[1], "Should contain warning message"
    assert 'Available: 512MB' in joined[1], "Should contain detail"

    # FAILURE SIMULATION: Not joining continuation lines.
    def join_multiline_logs_broken(lines, continuation_prefix='    '):
        """Broken: doesn't join continuations."""
        return lines

    broken = join_multiline_logs_broken(lines)
    assert len(broken) == len(lines), f"Broken version returns all lines: {len(broken)}"
    assert len(broken) != len(joined), "Broken version should have wrong count"

    # Edge case: All continuation lines (orphaned continuations).
    orphan_data = "    Orphan line 1\n    Orphan line 2\n    Orphan line 3"
    orphan_lines = orphan_data.split('\n')
    orphan_joined = join_multiline_logs(orphan_lines)
    assert len(orphan_joined) == 0, f"Orphan continuations should yield no entries, got {len(orphan_joined)}: {orphan_joined}"

    # Edge case: Single-line entries (no continuations).
    single_data = """Entry 1
Entry 2
Entry 3"""
    single_lines = single_data.strip().split('\n')
    single_joined = join_multiline_logs(single_lines)
    assert len(single_joined) == 3, f"Single-line entries should stay as-is, got {len(single_joined)}"
    assert single_joined == single_lines, "Single-line entries should match input"

    # Edge case: Deep stacktrace (many continuation lines).
    deep_data = """Traceback
    at func1()
    at func2()
    at func3()
    at func4()
    at func5()"""
    deep_lines = deep_data.strip().split('\n')
    deep_joined = join_multiline_logs(deep_lines)
    assert len(deep_joined) == 1, "Deep stacktrace should be 1 entry"
    assert deep_joined[0].count('\n') == 5, "Should have 5 newlines (6 lines total)"

    # Verify exact newline count.
    for i, entry in enumerate(joined):
        newlines = entry.count('\n')
        assert newlines == 2, f"Entry {i} should have 2 newlines, got {newlines}"

    print("✓ multiline_join passed")

if __name__ == '__main__':
    main()
