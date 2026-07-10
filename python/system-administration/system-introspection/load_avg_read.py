#!/usr/bin/env python3
"""
load_avg_read: Parse /proc/loadavg (1min, 5min, 15min load averages).
THE ONE LAW: Parse exact values, fail on missing fields.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import os

def parse_loadavg(loadavg_text):
    """
    Parse /proc/loadavg format: "1min 5min 15min running_procs total_procs last_pid\n"
    Return (load_1min, load_5min, load_15min) as floats.
    Raise ValueError if fewer than 3 fields.
    """
    parts = loadavg_text.strip().split()
    if len(parts) < 3:
        raise ValueError(f"Expected at least 3 load fields, got {len(parts)}")
    try:
        load_1 = float(parts[0])
        load_5 = float(parts[1])
        load_15 = float(parts[2])
    except ValueError as e:
        raise ValueError(f"Failed to parse load values: {e}")
    return (load_1, load_5, load_15)

def read_loadavg_real():
    """
    Read /proc/loadavg on Linux. Return tuple or (None, None, None) on other platforms.
    """
    if not os.path.exists('/proc/loadavg'):
        return (None, None, None)
    try:
        with open('/proc/loadavg') as f:
            return parse_loadavg(f.read())
    except (IOError, ValueError):
        return (None, None, None)

def main():
    # Synthetic /proc/loadavg data.
    synthetic = "2.50 1.80 0.95 3/256 12345\n"
    load_1, load_5, load_15 = parse_loadavg(synthetic)

    assert load_1 == 2.50, f"Expected 1min load 2.50, got {load_1}"
    assert load_5 == 1.80, f"Expected 5min load 1.80, got {load_5}"
    assert load_15 == 0.95, f"Expected 15min load 0.95, got {load_15}"

    # FAILURE SIMULATION: Missing 15min field (only 2 load values).
    broken = "2.50 1.80\n"
    try:
        parse_loadavg(broken)
        assert False, "Should raise ValueError for missing 15min load"
    except ValueError as e:
        assert "3 load fields" in str(e), f"Error should mention field requirement, got: {e}"

    # Verify zero loads (system idle).
    idle = "0.0 0.0 0.0 0/256 12345\n"
    i1, i5, i15 = parse_loadavg(idle)
    assert i1 == 0.0, "Should accept zero load"
    assert i5 == 0.0, "Should accept zero load"
    assert i15 == 0.0, "Should accept zero load"

    # High load values.
    high = "16.5 15.2 14.8 128/256 12345\n"
    h1, h5, h15 = parse_loadavg(high)
    assert h1 == 16.5, f"Expected 16.5, got {h1}"
    assert h5 == 15.2, f"Expected 15.2, got {h5}"

    # Verify trend (typically 1 >= 5 >= 15 or increasing/decreasing).
    synthetic2 = "3.0 2.5 2.0 1/256 12345\n"
    l1, l5, l15 = parse_loadavg(synthetic2)
    assert l1 >= l5 >= l15, "Trend should be decreasing in this sample"

    # Test real /proc/loadavg.
    real = read_loadavg_real()
    if real[0] is not None:
        assert isinstance(real[0], float), "Load values should be float"
        assert real[0] >= 0, "Load should be non-negative"
        assert real[1] >= 0, "Load should be non-negative"
        assert real[2] >= 0, "Load should be non-negative"
    else:
        assert real == (None, None, None), "Non-Linux should return (None, None, None)"

    print("✓ load_avg_read passed")

if __name__ == '__main__':
    main()
