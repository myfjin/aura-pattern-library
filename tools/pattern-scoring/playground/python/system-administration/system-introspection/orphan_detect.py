#!/usr/bin/env python3
"""
orphan_detect: Identify orphaned processes (parent pid doesn't exist).
THE ONE LAW: Parse tree, identify orphans by ppid not in known pids, return exact list.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

def detect_orphans(process_lines):
    """
    Parse process list (pid,ppid,name) and identify orphans.
    Orphan = ppid exists and is not 1 or 0, but ppid is not in known pids.
    Return sorted list of orphan pids.
    """
    processes = {}
    for line in process_lines.strip().split('\n'):
        if not line.strip():
            continue
        parts = line.split(',')
        pid, ppid, name = int(parts[0]), int(parts[1]), parts[2]
        processes[pid] = {'ppid': ppid, 'name': name}

    known_pids = set(processes.keys())
    orphans = []

    for pid in processes:
        ppid = processes[pid]['ppid']
        # Orphan: ppid not in known_pids and ppid != 1 (init) and ppid != 0 (kernel).
        if ppid not in known_pids and ppid != 1 and ppid != 0:
            orphans.append(pid)

    return sorted(orphans)

def main():
    # Synthetic process tree with orphans.
    # PID 100's parent (999) is dead (not in the list).
    # PID 101's parent (888) is also dead.
    process_data = """1,0,init
10,1,sshd
20,1,httpd
100,999,orphan_1
101,888,orphan_2
102,100,child-of-orphan"""

    orphans = detect_orphans(process_data)

    # Verify exact orphan list.
    assert orphans == [100, 101], f"Expected orphans [100, 101], got {orphans}"

    # FAILURE SIMULATION: Missing an orphan.
    def detect_orphans_broken(process_lines):
        """Broken version: only detects ppid=999 orphans, misses ppid=888."""
        processes = {}
        for line in process_lines.strip().split('\n'):
            if not line.strip():
                continue
            parts = line.split(',')
            pid, ppid, name = int(parts[0]), int(parts[1]), parts[2]
            processes[pid] = {'ppid': ppid, 'name': name}

        known_pids = set(processes.keys())
        orphans = []
        for pid in processes:
            if processes[pid]['ppid'] == 999 and 999 not in known_pids:
                orphans.append(pid)
        return sorted(orphans)

    broken_orphans = detect_orphans_broken(process_data)
    assert broken_orphans == [100], "Broken version finds only ppid=999 orphans"
    assert broken_orphans != orphans, "Broken version missed ppid=888 orphans"

    # Verify correct version finds both.
    assert len(orphans) == 2, f"Should find 2 orphans, got {len(orphans)}"
    assert 100 in orphans, "Should find PID 100"
    assert 101 in orphans, "Should find PID 101"

    # Edge case: No orphans.
    clean_data = """1,0,init
10,1,child
20,10,grandchild"""
    clean_orphans = detect_orphans(clean_data)
    assert clean_orphans == [], f"Clean tree should have no orphans, got {clean_orphans}"

    # Edge case: Multiple orphans from same dead parent.
    multi_orphan_data = """1,0,init
100,777,orphan_a
101,777,orphan_b
102,777,orphan_c"""
    multi = detect_orphans(multi_orphan_data)
    assert multi == [100, 101, 102], f"Expected 3 orphans from ppid 777, got {multi}"
    assert len(multi) == 3, "All 3 should be identified as orphans"

    # Edge case: Process with ppid=0 (kernel process, not orphaned).
    kernel_data = """0,0,kernel_main
1,0,init
100,0,kernel_child"""
    kernel_orphans = detect_orphans(kernel_data)
    assert kernel_orphans == [], "Kernel processes (ppid=0) should not be marked as orphans"

    # Edge case: Process with ppid=1 (init parent, not orphaned).
    init_child_data = """1,0,init
100,1,init_child"""
    init_orphans = detect_orphans(init_child_data)
    assert init_orphans == [], "Init children (ppid=1) should not be marked as orphans"

    # Verify sorting (descending or natural order).
    unsorted_data = """1,0,init
999,9999,missing_parent
42,8888,another_missing
777,7777,third_missing"""
    unsorted_orphans = detect_orphans(unsorted_data)
    assert unsorted_orphans == [42, 777, 999], f"Orphans should be sorted, got {unsorted_orphans}"

    print("✓ orphan_detect passed")

if __name__ == '__main__':
    main()
