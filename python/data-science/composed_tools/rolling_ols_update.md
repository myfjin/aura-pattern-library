# rolling ols update

**Language:** Python · **Category:** composed tools

## What it does

Rolling OLS Update — a running balance instead of a recount.

FUSED-BRIDGE COMPOSED PATTERN: online_covariance (Streaming & Sketches) x
sliding_window_regression (Time Series) — proposed by BOTH signals 2026-07-10:
structural edge `matrix` (an incremental covariance feeds the slope formula) +
semantic 0.408. sliding_window_regression REFITS OLS from scratch every step —
O(window) work per sample. Since the OLS slope is just cov(x,y)/var(x), the
composition maintains the window's covariance INCREMENTALLY (subtract the
departing point, add the arriving point, Welford-style) and reads the slope off
it: identical coefficients, O(1) per step instead of O(window).

Human logic of the name: a bank teller adjusts the balance per transaction
rather than recounting all the money each time a customer arrives.

---
*△ AURA Pattern Library — © Reality Optimizer*
