#!/usr/bin/env python3
"""
process_tree: Build process tree from /proc-style data, re-parent orphans to ppid=1.
THE ONE LAW: Parse process list with dead-parent process, assert it's re-parented to 1.
Anti-fake rule 2: Failure case must assert orphan STAYS orphaned without the fix.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import tempfile
import csv

def build_process_tree(proc_lines):
    """
    Parse process list (CSV: pid,ppid,name) and re-parent orphans.
    Orphan = ppid exists in input but references a non-existent parent.
    Re-parent orphans to ppid=1.
    Return list of (pid, ppid, name) tuples, sorted by pid.
    """
    # Parse input.
    processes = {}
    for line in proc_lines.strip().split('\n'):
        if not line.strip():
            continue
        parts = line.split(',')
        pid, ppid, name = int(parts[0]), int(parts[1]), parts[2]
        processes[pid] = {'ppid': ppid, 'name': name}

    # Collect all known pids.
    known_pids = set(processes.keys())

    # Re-parent orphans: if ppid is not in known_pids, set to 1.
    for pid in processes:
        if processes[pid]['ppid'] not in known_pids and processes[pid]['ppid'] != 1:
            processes[pid]['ppid'] = 1

    # Return sorted list.
    result = [(pid, processes[pid]['ppid'], processes[pid]['name'])
              for pid in sorted(processes.keys())]
    return result

def main():
    # Test data: process list with pid 100's parent (50) NOT in the list (dead).
    test_input = """1,0,init
100,50,orphan-child
101,1,normal-child"""

    tree = build_process_tree(test_input)

    # Verify: orphan (pid 100) should now have ppid=1.
    orphan = [t for t in tree if t[0] == 100]
    assert len(orphan) == 1, f"Expected 1 orphan entry, got {len(orphan)}"
    assert orphan[0][1] == 1, f"Orphan ppid should be 1, got {orphan[0][1]}"
    assert orphan[0][2] == 'orphan-child', f"Orphan name mismatch"

    # Verify normal process unaffected.
    normal = [t for t in tree if t[0] == 101]
    assert normal[0][1] == 1, "Normal child should keep ppid=1"

    # FAILURE SIMULATION: If we DON'T re-parent, the test should fail.
    # Define a broken version that does NOT re-parent.
    def build_process_tree_broken(proc_lines):
        processes = {}
        for line in proc_lines.strip().split('\n'):
            if not line.strip():
                continue
            parts = line.split(',')
            pid, ppid, name = int(parts[0]), int(parts[1]), parts[2]
            processes[pid] = {'ppid': ppid, 'name': name}
        result = [(pid, processes[pid]['ppid'], processes[pid]['name'])
                  for pid in sorted(processes.keys())]
        return result

    broken_tree = build_process_tree_broken(test_input)
    broken_orphan = [t for t in broken_tree if t[0] == 100]
    assert broken_orphan[0][1] == 50, f"Broken version should NOT re-parent (ppid=50)"

    # This proves the fix works: without it, orphan has ppid=50 (dead parent).
    assert tree[1][1] == 1, "Fixed version re-parents to 1"
    assert broken_tree[1][1] == 50, "Broken version leaves orphan with dead parent"

    # Verify tree order (sorted by pid).
    pids = [t[0] for t in tree]
    assert pids == [1, 100, 101], f"Tree should be sorted by pid, got {pids}"

    print("✓ process_tree passed")

if __name__ == '__main__':
    main()
