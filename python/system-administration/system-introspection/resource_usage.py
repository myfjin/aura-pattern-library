#!/usr/bin/env python3
"""
resource_usage: Extract memory/CPU metrics from /proc/[pid]/status.
THE ONE LAW: Parse real data, assert exact values; simulate missing fields, assert error.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import tempfile
import os

def parse_resource_metrics(status_text):
    """
    Extract VmRSS (RSS in kB), VmPeak (peak VM), Threads from /proc/[pid]/status.
    Return dict {rss_kb, peak_kb, threads} or raise ValueError if missing key fields.
    """
    metrics = {}
    for line in status_text.strip().split('\n'):
        if not line.strip() or ':' not in line:
            continue
        key, val = line.split(':', 1)
        key = key.strip()
        val = val.strip()

        if key == 'VmRSS':
            metrics['rss_kb'] = int(val.split()[0])
        elif key == 'VmPeak':
            metrics['peak_kb'] = int(val.split()[0])
        elif key == 'Threads':
            metrics['threads'] = int(val)

    # Validate required fields.
    required = {'rss_kb', 'peak_kb', 'threads'}
    if not required.issubset(metrics.keys()):
        missing = required - metrics.keys()
        raise ValueError(f"Missing required metrics: {missing}")

    return metrics

def main():
    # Synthetic /proc/[pid]/status data.
    complete_data = """Name:	test_proc
VmRSS:	 102400 kB
VmPeak:	 204800 kB
Threads:	4
State:	S (sleeping)
"""

    metrics = parse_resource_metrics(complete_data)
    assert metrics['rss_kb'] == 102400, f"Expected RSS 102400, got {metrics['rss_kb']}"
    assert metrics['peak_kb'] == 204800, f"Expected peak 204800, got {metrics['peak_kb']}"
    assert metrics['threads'] == 4, f"Expected 4 threads, got {metrics['threads']}"

    # FAILURE SIMULATION: Missing VmRSS should raise ValueError.
    broken_data = """Name:	test_proc
VmPeak:	 204800 kB
Threads:	4"""

    try:
        parse_resource_metrics(broken_data)
        assert False, "Should have raised ValueError for missing VmRSS"
    except ValueError as e:
        assert 'rss_kb' in str(e) or 'VmRSS' in str(e), f"Error should mention RSS metric, got: {e}"

    # Verify exact counts and values.
    assert len(metrics) == 3, f"Expected 3 metrics, got {len(metrics)}"
    assert isinstance(metrics['rss_kb'], int), "RSS should be int"
    assert isinstance(metrics['threads'], int), "Threads should be int"

    # Edge case: exact boundary values.
    boundary_data = """VmRSS:	 1 kB
VmPeak:	 2147483647 kB
Threads:	1"""
    boundary = parse_resource_metrics(boundary_data)
    assert boundary['rss_kb'] == 1, "Should parse minimum value"
    assert boundary['peak_kb'] == 2147483647, "Should parse large value"
    assert boundary['threads'] == 1, "Should parse single thread"

    print("✓ resource_usage passed")

if __name__ == '__main__':
    main()
