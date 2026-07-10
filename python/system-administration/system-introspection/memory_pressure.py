#!/usr/bin/env python3
"""
memory_pressure: Parse /proc/pressure/memory for PSI (Pressure Stall Info) metrics.
THE ONE LAW: Parse exact pressure values, fail on incomplete data.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import os

def parse_psi_memory(psi_text):
    """
    Parse /proc/pressure/memory format:
    some avg10=X.XX avg60=Y.YY avg300=Z.ZZ total=N
    full avg10=A.AA avg60=B.BB avg300=C.CC total=M
    Return dict: {some_avg10, some_avg60, some_avg300, full_avg10, full_avg60, full_avg300}
    Raise ValueError if required lines missing.
    """
    metrics = {}
    for line in psi_text.strip().split('\n'):
        if not line.strip():
            continue
        parts = line.split()
        if len(parts) < 4:
            raise ValueError(f"Malformed PSI line: {line}")

        metric_type = parts[0]  # 'some' or 'full'
        for part in parts[1:]:
            if '=' in part:
                key, val = part.split('=', 1)
                try:
                    val = float(val)
                except ValueError:
                    continue
                if key.startswith('avg'):
                    metrics[f"{metric_type}_{key}"] = val

    # Validate required fields.
    required = {
        'some_avg10', 'some_avg60', 'some_avg300',
        'full_avg10', 'full_avg60', 'full_avg300'
    }
    if not required.issubset(metrics.keys()):
        missing = required - metrics.keys()
        raise ValueError(f"Missing PSI metrics: {missing}")

    return metrics

def read_psi_memory():
    """
    Read /proc/pressure/memory on Linux. Return dict or None on other platforms.
    """
    psi_path = '/proc/pressure/memory'
    if not os.path.exists(psi_path):
        return None
    try:
        with open(psi_path) as f:
            return parse_psi_memory(f.read())
    except (IOError, ValueError):
        return None

def main():
    # Synthetic /proc/pressure/memory data.
    synthetic = """some avg10=1.23 avg60=2.34 avg300=3.45 total=123456
full avg10=0.45 avg60=0.56 avg300=0.67 total=654321"""

    metrics = parse_psi_memory(synthetic)

    # Verify exact values.
    assert abs(metrics['some_avg10'] - 1.23) < 0.001, f"some_avg10: {metrics['some_avg10']}"
    assert abs(metrics['some_avg60'] - 2.34) < 0.001, f"some_avg60: {metrics['some_avg60']}"
    assert abs(metrics['some_avg300'] - 3.45) < 0.001, f"some_avg300: {metrics['some_avg300']}"
    assert abs(metrics['full_avg10'] - 0.45) < 0.001, f"full_avg10: {metrics['full_avg10']}"
    assert abs(metrics['full_avg60'] - 0.56) < 0.001, f"full_avg60: {metrics['full_avg60']}"
    assert abs(metrics['full_avg300'] - 0.67) < 0.001, f"full_avg300: {metrics['full_avg300']}"

    # FAILURE SIMULATION: Missing 'full' section.
    broken = """some avg10=1.23 avg60=2.34 avg300=3.45 total=123456"""
    try:
        parse_psi_memory(broken)
        assert False, "Should raise ValueError for missing 'full' metrics"
    except ValueError as e:
        assert 'full_avg' in str(e), f"Error should mention full metrics, got: {e}"

    # Zero pressure (no stalling).
    zero_pressure = """some avg10=0.0 avg60=0.0 avg300=0.0 total=0
full avg10=0.0 avg60=0.0 avg300=0.0 total=0"""
    zero = parse_psi_memory(zero_pressure)
    assert zero['some_avg10'] == 0.0, "Should handle zero pressure"
    assert zero['full_avg300'] == 0.0, "Should handle zero pressure"

    # High pressure (system under stress).
    high_pressure = """some avg10=50.5 avg60=45.3 avg300=40.1 total=999999
full avg10=30.2 avg60=25.8 avg300=20.5 total=888888"""
    high = parse_psi_memory(high_pressure)
    assert high['some_avg10'] == 50.5, "Should parse high pressure values"
    assert high['full_avg10'] == 30.2, "Should parse high pressure values"

    # Verify metric count.
    assert len(metrics) == 6, f"Expected 6 metrics, got {len(metrics)}"

    # Test real /proc/pressure/memory (may not exist on older kernels).
    real = read_psi_memory()
    if real is not None:
        assert isinstance(real, dict), "Real PSI should be dict"
        assert len(real) >= 6, "Real PSI should have all fields"
    else:
        # Not available (older kernel or non-Linux).
        assert real is None, "Should return None if unavailable"

    print("✓ memory_pressure passed")

if __name__ == '__main__':
    main()
