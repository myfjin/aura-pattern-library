#!/usr/bin/env python3
"""
mount_disk_usage: Parse mount output and extract filesystem usage.
THE ONE LAW: Parse real df-style output, assert exact usage percentages.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import tempfile
import os

def parse_df_output(df_text):
    """
    Parse df-style output: lines with "Filesystem Size Used Avail Use% Mounted on"
    Return list of dicts: {fs, size_kb, used_kb, avail_kb, use_pct, mount}
    """
    lines = df_text.strip().split('\n')
    result = []

    for line in lines:
        parts = line.split()
        if len(parts) < 6:
            continue
        # Handle mount paths with spaces by taking last 2 parts.
        fs, size_str, used_str, avail_str, use_str = parts[:5]
        mount = ' '.join(parts[5:])

        try:
            size_kb = int(size_str)
            used_kb = int(used_str)
            avail_kb = int(avail_str)
            use_pct = int(use_str.rstrip('%'))
        except ValueError:
            continue

        result.append({
            'fs': fs,
            'size_kb': size_kb,
            'used_kb': used_kb,
            'avail_kb': avail_kb,
            'use_pct': use_pct,
            'mount': mount
        })

    return result

def main():
    # Synthetic df output.
    df_output = """/dev/sda1 1024000 512000 512000 50% /
/dev/sda2 2048000 1024000 1024000 50% /home
tmpfs 1024 0 1024 0% /dev/shm"""

    filesystems = parse_df_output(df_output)
    assert len(filesystems) == 3, f"Expected 3 filesystems, got {len(filesystems)}"

    # Find / filesystem.
    root_fs = [fs for fs in filesystems if fs['mount'] == '/']
    assert len(root_fs) == 1, "Should find root filesystem"
    root = root_fs[0]

    assert root['fs'] == '/dev/sda1', f"Expected /dev/sda1, got {root['fs']}"
    assert root['size_kb'] == 1024000, f"Expected size 1024000, got {root['size_kb']}"
    assert root['used_kb'] == 512000, f"Expected used 512000, got {root['used_kb']}"
    assert root['avail_kb'] == 512000, f"Expected avail 512000, got {root['avail_kb']}"
    assert root['use_pct'] == 50, f"Expected use% 50, got {root['use_pct']}"

    # FAILURE SIMULATION: Incorrect percentage calculation.
    # If we computed use_pct as (used/size)*100 dynamically instead of reading,
    # we might get rounding errors. Verify we read it directly.
    home_fs = [fs for fs in filesystems if fs['mount'] == '/home']
    home = home_fs[0]
    assert home['use_pct'] == 50, "Should read use% from output, not recalculate"
    # If we recalculated: (1024000 / 2048000) * 100 = 50.0, so same. Test with oddness.

    # Edge case: 0% usage.
    zero_usage = """tmpfs 1024 0 1024 0% /dev/shm"""
    zero_fs = parse_df_output(zero_usage)
    assert zero_fs[0]['use_pct'] == 0, "Should handle 0% usage"
    assert zero_fs[0]['used_kb'] == 0, "Used should be 0"

    # Edge case: 99% usage.
    high_usage = """/dev/sda1 1000 990 10 99% /
"""
    high_fs = parse_df_output(high_usage)
    assert high_fs[0]['use_pct'] == 99, "Should handle 99% usage"
    assert high_fs[0]['used_kb'] == 990, "Used should be 990"
    assert high_fs[0]['avail_kb'] == 10, "Avail should be 10"

    # Verify sum constraint: used + avail ~= size (or close).
    for fs in filesystems:
        total = fs['used_kb'] + fs['avail_kb']
        assert total == fs['size_kb'], f"For {fs['mount']}: used+avail={total} != size={fs['size_kb']}"

    # Verify fields are present.
    for fs in filesystems:
        required_keys = {'fs', 'size_kb', 'used_kb', 'avail_kb', 'use_pct', 'mount'}
        assert required_keys == set(fs.keys()), f"Missing keys in {fs}"

    print("✓ mount_disk_usage passed")

if __name__ == '__main__':
    main()
