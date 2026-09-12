"""
FFT via Cooley-Tukey Algorithm — the algorithm that makes digital signal processing
practical.

WHAT IT DOES: The Discrete Fourier Transform (DFT) converts a signal from time domain
to frequency domain — but the naive algorithm is O(N^2), too slow for any real use.
The Cooley-Tukey FFT is a recursive divide-and-conquer that runs in O(N log N).
For N=256, that's 65,536 vs 2,048 operations — a 32x speedup. This pattern implements
both and verifies they produce identical results.

WHEN TO USE: Any time you need to analyze the frequency content of a signal — audio
processing, communications, vibration analysis, image processing. The FFT is everywhere.

GUARANTEES: FFT matches naive DFT to within 1e-6 (machine precision). FFT operation
count (N*log2(N)) is less than naive DFT (N^2). The speedup grows with N.

NOT: A general FFT library. Only handles power-of-2 lengths (radix-2). Does not
handle complex inputs, inverse FFT, or windowing. The operation count is approximate
(only counts complex multiplications).
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
