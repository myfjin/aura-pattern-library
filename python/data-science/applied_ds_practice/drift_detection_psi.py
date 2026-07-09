"""
Population Stability Index (PSI) and KS-statistic for feature drift detection.

PSI measures how a feature's distribution shifts between a reference period
(e.g., training data) and a current window (e.g., production data).
KS-statistic tests whether two distributions are significantly different.
Both detect dataset shift / concept drift.

Use: production monitoring, model retraining triggers, data quality checks.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
from collections import defaultdict


def reference_bin_edges(ref_values: list[float], n_bins: int = 10) -> list[float]:
    """Quantile (equal-frequency) bin edges computed from the REFERENCE window.
    PSI's defining discipline: BOTH windows are binned on these same edges.
    Binning each window on its own min/max is the classic PSI bug — a shifted
    distribution looks normal in its own bins, and the drift signal is erased
    by the binning itself."""
    s = sorted(ref_values)
    n = len(s)
    return [s[min(n - 1, int(n * k / n_bins))] for k in range(1, n_bins)]


def bin_with_edges(values: list[float], edges: list[float]) -> list[int]:
    """Assign each value to a bin defined by the reference edges."""
    out = []
    for v in values:
        b = 0
        while b < len(edges) and v > edges[b]:
            b += 1
        out.append(b)
    return out


def population_stability_index(ref_bins: list[int], curr_bins: list[int],
                               n_bins: int = 10) -> float:
    """
    Compute PSI: sum over bins of (curr% - ref%) * ln(curr% / ref%).
    Higher PSI indicates more drift. Typical threshold: PSI > 0.25 warns of drift.
    """
    ref_counts = defaultdict(int)
    curr_counts = defaultdict(int)

    for b in ref_bins:
        ref_counts[b] += 1
    for b in curr_bins:
        curr_counts[b] += 1

    n_ref = len(ref_bins) if ref_bins else 1
    n_curr = len(curr_bins) if curr_bins else 1

    psi = 0.0
    for b in range(n_bins):
        ref_pct = (ref_counts[b] + 1) / (n_ref + n_bins)  # Laplace smooth
        curr_pct = (curr_counts[b] + 1) / (n_curr + n_bins)

        ratio = curr_pct / ref_pct if ref_pct > 0 else 1
        psi += (curr_pct - ref_pct) * math.log(ratio) if ratio > 0 else 0

    return psi


def kolmogorov_smirnov_statistic(ref_vals: list[float], curr_vals: list[float]) -> float:
    """
    Compute KS statistic: max absolute difference between CDFs.
    Higher KS indicates more drift.
    """
    # Merge and sort
    all_vals = sorted(set(ref_vals + curr_vals))
    if not all_vals:
        return 0.0

    # Empirical CDFs
    ref_cdf = {}
    curr_cdf = {}

    for v in all_vals:
        ref_cdf[v] = sum(1 for rv in ref_vals if rv <= v) / len(ref_vals) if ref_vals else 0
        curr_cdf[v] = sum(1 for cv in curr_vals if cv <= v) / len(curr_vals) if curr_vals else 0

    # Max absolute difference
    ks = max(abs(ref_cdf[v] - curr_cdf[v]) for v in all_vals) if all_vals else 0
    return ks


if __name__ == "__main__":
    import random
    random.seed(42)

    # Scenario 1: No drift (reference and current drawn from same distribution)
    print("Scenario 1: No drift (same distribution)")
    ref_no_drift = [random.gauss(100, 15) for _ in range(500)]
    curr_no_drift = [random.gauss(100, 15) for _ in range(500)]

    edges_nd = reference_bin_edges(ref_no_drift, n_bins=10)
    ref_bins_nd = bin_with_edges(ref_no_drift, edges_nd)
    curr_bins_nd = bin_with_edges(curr_no_drift, edges_nd)

    psi_no_drift = population_stability_index(ref_bins_nd, curr_bins_nd, n_bins=10)
    ks_no_drift = kolmogorov_smirnov_statistic(ref_no_drift, curr_no_drift)

    print(f"  PSI:  {psi_no_drift:.4f} (threshold: 0.25)")
    print(f"  KS:   {ks_no_drift:.4f} (threshold: 0.1)")
    print(f"  Drift: {'Yes' if psi_no_drift > 0.25 else 'No'}")
    assert psi_no_drift < 0.25, f"No-drift PSI {psi_no_drift} should be < 0.25"
    assert ks_no_drift < 0.1, f"No-drift KS {ks_no_drift} should be < 0.1"
    print()

    # Scenario 2: Planted drift (current shifted 3 SDs higher, larger variance)
    print("Scenario 2: Planted drift (mean shift +3 SD, variance increase)")
    ref_drift = [random.gauss(100, 15) for _ in range(500)]
    curr_drift = [random.gauss(145, 25) for _ in range(500)]  # Mean + 3*SD, wider

    edges_d = reference_bin_edges(ref_drift, n_bins=10)
    ref_bins_d = bin_with_edges(ref_drift, edges_d)
    curr_bins_d = bin_with_edges(curr_drift, edges_d)

    psi_drift = population_stability_index(ref_bins_d, curr_bins_d, n_bins=10)
    ks_drift = kolmogorov_smirnov_statistic(ref_drift, curr_drift)

    print(f"  PSI:  {psi_drift:.4f}")
    print(f"  KS:   {ks_drift:.4f} (threshold: 0.1)")
    print(f"  Drift detected by KS: {'Yes' if ks_drift > 0.1 else 'No'}")
    assert ks_drift > 0.1, f"Drift KS {ks_drift} should be > 0.1"
    # The industry threshold, met honestly: a +3σ shift must trip PSI > 0.25.
    assert psi_drift > 0.25, f"Drift PSI {psi_drift} should exceed the 0.25 threshold"
    assert psi_drift > psi_no_drift, f"Drift PSI {psi_drift} should be > no-drift PSI {psi_no_drift}"
    print()

    print("drift_detection_psi.py PASS")
