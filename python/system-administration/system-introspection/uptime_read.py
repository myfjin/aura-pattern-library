#!/usr/bin/env python3
"""
uptime_read: Parse /proc/uptime to extract uptime in seconds and idle time.
THE ONE LAW: Parse exact values, assert single clock (no time() calls during parse).
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import os

def parse_uptime(uptime_text):
    """
    Parse /proc/uptime format: "uptime_sec idle_sec\n"
    Return (uptime_sec, idle_sec) as floats.
    Raise ValueError if malformed.
    """
    line = uptime_text.strip()
    parts = line.split()
    if len(parts) != 2:
        raise ValueError(f"Expected 2 fields, got {len(parts)}")
    try:
        uptime = float(parts[0])
        idle = float(parts[1])
    except ValueError as e:
        raise ValueError(f"Failed to parse floats: {e}")
    return (uptime, idle)

def read_uptime_real():
    """
    Read /proc/uptime on Linux; return (uptime, idle) or (None, None) on other platforms.
    """
    if not os.path.exists('/proc/uptime'):
        return (None, None)
    try:
        with open('/proc/uptime') as f:
            return parse_uptime(f.read())
    except (IOError, ValueError):
        return (None, None)

def main():
    # Synthetic /proc/uptime data.
    synthetic = "12345.67 98765.43\n"
    uptime, idle = parse_uptime(synthetic)

    assert uptime == 12345.67, f"Expected uptime 12345.67, got {uptime}"
    assert idle == 98765.43, f"Expected idle 98765.43, got {idle}"

    # FAILURE SIMULATION: Missing field.
    broken = "12345.67\n"
    try:
        parse_uptime(broken)
        assert False, "Should raise ValueError for missing field"
    except ValueError as e:
        assert "2 fields" in str(e), f"Error should mention field count, got: {e}"

    # Verify exact floating-point values (no rounding errors).
    precise = "0.01 0.02\n"
    p_up, p_idle = parse_uptime(precise)
    assert abs(p_up - 0.01) < 1e-9, f"Precision lost: {p_up}"
    assert abs(p_idle - 0.02) < 1e-9, f"Precision lost: {p_idle}"

    # Verify large values.
    large = "999999999.99 999999999.99\n"
    l_up, l_idle = parse_uptime(large)
    assert l_up == 999999999.99, f"Large value failed: {l_up}"

    # Edge case: zero uptime (shouldn't happen, but test boundary).
    zero = "0.0 0.0\n"
    z_up, z_idle = parse_uptime(zero)
    assert z_up == 0.0, "Should accept zero uptime"

    # Test real /proc/uptime (Linux only).
    real = read_uptime_real()
    if real[0] is not None:
        uptime, idle = real
        assert isinstance(uptime, float), "Real uptime should be float"
        assert isinstance(idle, float), "Real idle should be float"
        assert uptime > 0, "Real uptime should be positive"
        assert idle > 0, "Real idle should be positive"
    else:
        # Non-Linux: result is (None, None).
        assert real == (None, None), "Non-Linux should return (None, None)"

    print("✓ uptime_read passed")

if __name__ == '__main__':
    main()
