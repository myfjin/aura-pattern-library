# Savitzky-Golay Filter

**File:** `python/data-science/signal_processing_and_sequences/savitzky_golay_lite.py`
**Sphere:** Data Science — Signal Processing and Sequences

---

## What it solves

**Smooth your signal without destroying the peaks.** Moving averages blur sharp features. The Savitzky-Golay filter fits a low-order polynomial (e.g. quadratic) to a rolling window — it smooths noise while preserving peak heights and widths much better than a moving average. This pattern demonstrates the difference: SG preserves a smooth Gaussian peak while the moving average visibly clips it.

**When to use:** You have a noisy signal with smooth, band-limited peaks that you want to preserve. Common in spectroscopy, chromatography, and any domain where peak shape carries information.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `signal` | list of float | — |
| `window_size` | odd int ≥ 3 | even → asymmetric window |
| `poly_order` | int ≥ 1, typically 2-3 | — |

---

## How inputs shape the output

- **SG preserves smooth peaks:** a local quadratic fits a Gaussian peak well, so the filtered peak is close to the true peak (error < 0.9).
- **Moving average clips peaks:** averaging with neighbors attenuates the peak (error > 1.1).
- **SG clearly beats MA:** the SG error is less than 70% of the MA error.

---

## Worked example (real run)

```
$ python3 python/data-science/signal_processing_and_sequences/savitzky_golay_lite.py
True peak: 9.00 | SG filtered peak: 8.72 (error=0.28) | MA filtered peak: 6.42 (error=2.58) | SG improvement: 89.1% | PASS
```

**Reading the output:** the true peak is 9.00. SG preserves it at 8.72 (error 0.28). MA clips it to 6.42 (error 2.58). SG is 89% better at preserving the peak.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| `window_size > len(signal)` | works but window is whole signal | correct but degenerate |
| constant signal | both filters return same value | correct |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-18
