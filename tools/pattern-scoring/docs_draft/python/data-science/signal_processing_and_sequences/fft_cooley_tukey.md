# FFT via Cooley-Tukey Algorithm

**File:** `python/data-science/signal_processing_and_sequences/fft_cooley_tukey.py`
**Sphere:** Data Science — Signal Processing and Sequences

---

## What it solves

**The algorithm that makes digital signal processing practical.** The Discrete Fourier Transform (DFT) converts a signal from time domain to frequency domain — but the naive algorithm is O(N²), too slow for any real use. The Cooley-Tukey FFT is a recursive divide-and-conquer that runs in O(N log N). For N=256, that's 65,536 vs 2,048 operations — a 32× speedup. This pattern implements both and verifies they produce identical results.

**When to use:** Any time you need to analyze the frequency content of a signal — audio processing, communications, vibration analysis, image processing. The FFT is everywhere.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `signal` | list of float, length must be power of 2 | non-power-of-2 → wrong results |

---

## How inputs shape the output

- **FFT matches DFT exactly:** the max error between FFT and naive DFT is < 1e-6 for N=256.
- **Operation count is dramatically lower:** FFT ops = N·log₂(N) vs naive = N². The speedup grows with N.
- **The algorithm is recursive:** it splits the signal into even/odd indices, recurses, and combines with twiddle factors.

---

## Worked example (real run)

```
$ python3 python/data-science/signal_processing_and_sequences/fft_cooley_tukey.py
N=256 | Naive ops: 65536 | FFT ops: 2048 | Speedup: 32.0x | Max error: 3.82e-15 | PASS
```

**Reading the output:** for a 256-point signal, the naive DFT needs 65,536 operations; the FFT needs only 2,048 — a 32× speedup. The results match to machine precision.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| non-power-of-2 length | wrong results (algorithm assumes N=2^m) | needs guard |
| empty signal | returns `[]` | correct |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-18
