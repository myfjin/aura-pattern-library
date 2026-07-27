# conv1d feature detector

**Language:** Python · **Sphere:** data-science · **Category:** Neural Networks From Scratch

**Signature:** `(pred: float, target: float) → float`

## What it does

1D convolution layer learning to detect a planted motif in sequences.

Core idea: Implement 1D convolution from scratch. Convolve a learnable kernel
over a 1D sequence. Data contains a planted motif; over training the kernel
learns to detect it, producing high responses when centered on the motif and low
elsewhere.

When to use: Understanding convolution mechanics, feature detection, temporal
pattern recognition.

## Guarantee

When it runs, conv1d feature detector guarantees response_at_motif > avg_response_elsewhere * 2 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `response_at_motif > avg_response_elsewhere * 2`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `Conv1D(kernel_size=3, lr=0.01)` → `convolve(x) → list` → `backward(x, conv_out, targets) → loss`
**Valid input:** `x: List[float]` — 1D sequence, length ≥ kernel_size. `target_responses: List[float]` same length as conv output.
**Core:** 1D convolution from scratch. Single learnable kernel convolved over input (valid padding). Trained to detect a planted motif [1.0, -0.5, 1.0] in noisy sequences. MSE loss, gradient descent on kernel and bias.
**Assert:** On 10 training sequences (length 20, motif planted at random positions), 200 epochs at lr=0.1, response at motif position > 2× average response elsewhere on a held-out test sequence.
**⚠️ Defect:** The training targets are computed heuristically (dot product similarity to the motif, scaled to [0,1]), not as a clean binary signal. This means the kernel learns to approximate the motif detector indirectly, and the quality depends on the heuristic threshold. A cleaner approach would use binary targets (1 at motif position, 0 elsewhere).

---
*△ AURA Pattern Library — © Reality Optimizer*
