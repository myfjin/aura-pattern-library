# Power Iteration with Shift

**File:** `python/data-science/linear_algebra/power_iteration_shifted.py`
**Sphere:** Data Science — Linear Algebra

---

## What it solves

**Find the smallest eigenvalue without computing all of them.** Standard power iteration finds the largest eigenvalue. By shifting the matrix (A − σI), the largest |λ − σ| corresponds to the eigenvalue farthest from σ. Choose σ larger than the largest eigenvalue, and power iteration on the shifted matrix recovers the smallest eigenvalue. The Rayleigh quotient then extracts the true eigenvalue from the converged eigenvector.

**When to use:** You need the smallest eigenvalue of a symmetric matrix (e.g. for condition number estimation, convergence analysis, or checking positive definiteness) without computing the full spectrum.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `A` | symmetric square matrix (list of lists) | non-symmetric → wrong eigenvalue |
| `shift` | > λ_max to find smallest λ | wrong shift → wrong eigenvalue |
| `max_iter` | int ≥ 1 | — |
| `tol` | > 0, convergence threshold | — |

---

## How inputs shape the output

- **Shift choice is critical:** shift must be larger than the largest eigenvalue. The demo's matrix has λ_max ≈ 4.732, so shift=5.0 works. A shift inside the spectrum would converge to a different eigenvalue.
- **Convergence speed depends on the eigenvalue gap:** the larger the gap between the target eigenvalue and its nearest neighbor, the faster the convergence.
- **The Rayleigh quotient extracts the true eigenvalue:** after convergence on the shifted matrix, v·A·v / v·v recovers the actual eigenvalue of A (not the shifted one).

---

## Worked example (real run)

```
$ python3 python/data-science/linear_algebra/power_iteration_shifted.py
PASS
```

**Reading the output:** the smallest eigenvalue of the 3×3 matrix is recovered within [0.5, 1.5] (true value ≈ 1.268). The eigenvector check A·v ≈ λ·v confirms correctness.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| non-symmetric A | converges to wrong eigenvalue | assumption violation |
| shift inside spectrum | converges to a different eigenvalue | not a bug, user error |
| zero vector initialization | norm=0, breaks | needs guard |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-18 · evidence: `output/manual_audit_2026-07-19.csv`
