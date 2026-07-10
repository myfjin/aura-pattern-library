#!/usr/bin/env python3
"""
top_n_by_resource: Rank processes by a resource metric (RSS, CPU, etc.).
THE ONE LAW: Sort and rank, assert exact ordering; simulate unsorted input.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import tempfile

def rank_by_memory(process_lines, n):
    """
    Parse process lines (pid,name,rss_kb) and return top N by RSS.
    Return list of (pid, name, rss_kb) tuples, sorted by RSS descending.
    """
    processes = []
    for line in process_lines.strip().split('\n'):
        if not line.strip():
            continue
        parts = line.split(',')
        pid, name, rss_str = int(parts[0]), parts[1], int(parts[2])
        processes.append((pid, name, rss_str))

    # Sort by RSS descending.
    sorted_procs = sorted(processes, key=lambda x: x[2], reverse=True)
    return sorted_procs[:n]

def main():
    # Synthetic process list.
    process_data = """1,init,1024
100,chrome,524288
50,bash,2048
200,python,262144
150,sshd,1024"""

    top_3 = rank_by_memory(process_data, 3)

    # Verify exact ranking.
    assert len(top_3) == 3, f"Expected 3 results, got {len(top_3)}"
    assert top_3[0][1] == 'chrome', f"Top 1 should be chrome, got {top_3[0][1]}"
    assert top_3[0][2] == 524288, f"chrome RSS should be 524288, got {top_3[0][2]}"
    assert top_3[1][1] == 'python', f"Top 2 should be python, got {top_3[1][1]}"
    assert top_3[1][2] == 262144, f"python RSS should be 262144, got {top_3[1][2]}"
    assert top_3[2][1] == 'bash', f"Top 3 should be bash, got {top_3[2][1]}"
    assert top_3[2][2] == 2048, f"bash RSS should be 2048, got {top_3[2][2]}"

    # FAILURE SIMULATION: If not sorted, would get wrong top 3.
    # Verify our sort is actually happening by checking descending order.
    for i in range(len(top_3) - 1):
        assert top_3[i][2] >= top_3[i+1][2], f"Not sorted: {top_3[i][2]} < {top_3[i+1][2]}"

    # Edge case: Request more than available.
    top_10 = rank_by_memory(process_data, 10)
    assert len(top_10) == 5, f"Expected 5 (all available), got {len(top_10)}"
    assert top_10[0][1] == 'chrome', "Top should still be chrome"

    # Edge case: N=1 (top process).
    top_1 = rank_by_memory(process_data, 1)
    assert len(top_1) == 1, "Should return 1 result"
    assert top_1[0][1] == 'chrome', "Top process should be chrome"

    # Edge case: N=0 (empty result).
    top_0 = rank_by_memory(process_data, 0)
    assert len(top_0) == 0, "Should return 0 results"

    # Verify exact values (no approximation).
    all_sorted = rank_by_memory(process_data, 100)
    assert all_sorted[0][2] == 524288, "Largest should be 524288"
    assert all_sorted[-1][2] == 1024, "Smallest should be 1024"
    assert all_sorted[1][2] == 262144, "2nd should be 262144"

    # Test with tied values (same RSS).
    tied_data = """1,proc_a,1000
2,proc_b,1000
3,proc_c,500"""
    tied_top = rank_by_memory(tied_data, 2)
    assert len(tied_top) == 2, "Should return 2 even with ties"
    assert tied_top[0][2] == 1000, "Top should be 1000"
    assert tied_top[1][2] == 1000, "Second should also be 1000"

    print("✓ top_n_by_resource passed")

if __name__ == '__main__':
    main()
