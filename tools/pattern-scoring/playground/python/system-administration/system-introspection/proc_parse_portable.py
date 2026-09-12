#!/usr/bin/env python3
"""
proc_parse_portable: Parse /proc-style process info, portable across platforms.
Handles missing /proc gracefully; tests against synthetic data regardless.
THE ONE LAW: Simulate parse failure on malformed data, assert it's caught.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import os
import tempfile
import subprocess
import sys

def parse_proc_info(proc_text):
    """Parse /proc/[pid]/status-style text. Return dict of key-value pairs."""
    result = {}
    for line in proc_text.strip().split('\n'):
        if not line.strip() or ':' not in line:
            continue
        key, val = line.split(':', 1)
        result[key.strip()] = val.strip()
    return result

def read_proc_status(pid):
    """
    Read /proc/[pid]/status on Linux; fallback to None on other platforms.
    Return parsed dict or None.
    """
    proc_path = f"/proc/{pid}/status"
    if not os.path.exists(proc_path):
        return None
    try:
        with open(proc_path) as f:
            return parse_proc_info(f.read())
    except (IOError, PermissionError):
        return None

def main():
    # HEADLINE PATTERN: Test synthetic /proc data, then real platform fallback.
    # Synthetic data: typical /proc/[pid]/status snippet.
    synthetic_data = """Name:	bash
State:	S (sleeping)
Tgid:	1234
Pid:	1234
PPid:	1000
Uid:	1000	1000	1000	1000
VmPeak:	 123456 kB
VmHWM:	  89012 kB
"""

    # Parse synthetic data.
    parsed = parse_proc_info(synthetic_data)

    # FAILURE SIMULATION: Missing Name key should fail.
    broken_data = """State:	S (sleeping)
VmPeak:	 123456 kB"""
    broken_parsed = parse_proc_info(broken_data)
    assert 'Name' not in broken_parsed, "Broken data should not have Name"
    assert 'VmPeak' in broken_parsed, "VmPeak should be parsed"

    # Verify exact parsed values for synthetic data.
    assert parsed['Name'] == 'bash', f"Expected Name=bash, got {parsed['Name']}"
    assert parsed['Pid'] == '1234', f"Expected Pid=1234, got {parsed['Pid']}"
    assert parsed['PPid'] == '1000', f"Expected PPid=1000, got {parsed['PPid']}"
    assert parsed['State'] == 'S (sleeping)', f"Expected State with value, got {parsed['State']}"
    assert len(parsed) == 8, f"Expected 8 fields, got {len(parsed)}"

    # Test real read fallback (will be None on non-Linux or permission denied).
    result = read_proc_status(os.getpid())
    if result is not None:
        assert 'Pid' in result, "Real /proc parse should have Pid"
        assert 'State' in result, "Real /proc parse should have State"
    # On macOS or if no /proc, result is None — assert the guard worked.
    assert result is None or isinstance(result, dict), "read_proc_status returns None or dict"

    print("✓ proc_parse_portable passed")

if __name__ == '__main__':
    main()
