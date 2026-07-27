# tiny autoencoder

**Language:** Python · **Sphere:** data-science · **Category:** Neural Networks From Scratch

**Signature:** `(x: float) → float`

## What it does

1-hidden-layer autoencoder compressing correlated 8D data to 2D and back.

Core idea: Encoder maps 8D input -> 2D bottleneck via sigmoid. Decoder maps
2D -> 8D reconstruction. Train to minimize reconstruction error. With correlated
input (columns highly linearly dependent), 2D bottleneck should capture main
variance; reconstruction error should be far below random baseline.

When to use: Dimensionality reduction, data compression, unsupervised learning,
understanding encoder-decoder architectures.

## Guarantee

When it runs, tiny autoencoder guarantees trained_error < random_recon_error / 2 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `trained_error < random_recon_error / 2`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `TinyAutoencoder(input_dim=8, bottleneck_dim=2, lr=0.5)` → `train(data, epochs) → float`
**Valid input:** `data: List[List[float]]` — 8D vectors, normalized to [0,1]. At least 1 sample.
**Core:** 1-hidden-layer autoencoder (8→2→8) with sigmoid activations. Encoder compresses to 2D bottleneck, decoder reconstructs. Trained with MSE reconstruction loss. With correlated 8D input (driven by 2 latent signals), 2D bottleneck captures main variance.
**Assert:** On 50 correlated 8D samples (driven by 2 latent signals), 100 epochs at lr=0.5, trained reconstruction error < random reconstruction error / 2.
**✔ Retrofitted:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E retrofit pass; the current signed code reflects the fix.

---
*△ AURA Pattern Library — © Reality Optimizer*
