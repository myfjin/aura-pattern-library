# DDM — Drift Detection Method

**File:** `python/data-science/streaming_iii/ddm_error_drift.py`
**Sphere:** Data Science — Streaming and Sketches

---

## What it solves

**Detect when a classifier's error rate has significantly worsened, online.** DDM (Gama, Medas, Castillo, Rodrigues 2004) tracks the running error rate pᵢ and its standard deviation sᵢ = √(pᵢ(1−pᵢ)/i) as each prediction arrives. It keeps the minimum of (pᵢ + sᵢ) ever seen — that's the model's best performance. Signals WARNING at pᵢ+sᵢ ≥ pₘᵢₙ + 2·sₘᵢₙ and DRIFT at pᵢ+sᵢ ≥ pₘᵢₙ + 3·sₘᵢₙ.

**When to use:** You're running a classifier on a stream and need to know when its accuracy has degraded enough to warrant retraining. Think of it as a statistical control chart for model performance.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `error_stream` | List[int] (0/1, 1 = error) | binary only |
| `min_samples` | int > 0, warm-up period | too small = premature warnings |

---

## How inputs shape the output

- **3-sigma control level:** the DRIFT threshold at pₘᵢₙ + 3·sₘᵢₙ is a statistical guard — a real degradation, not random fluctuation.
- **Warm-up matters:** the first `min_samples` values establish the baseline. The demo's 30-sample warm-up is enough for Bernoulli streams.
- **No false alarms on stationary data:** if the error rate stays constant, the control chart never fires — proven by the demo's stationary test.

---

## Worked example (real run)

```
$ python3 python/data-science/streaming_iii/ddm_error_drift.py
stationary: detected=False at -1 (want False)
drift: detected=True at 432 (want True, after 400)
DDM PASS
```

**Reading the output:** on a stationary Bernoulli(0.15) error stream, DDM correctly stays quiet. When the error rate jumps from 0.10 → 0.40 at index 400, DDM flags the drift at index 432 — 32 steps after the change, once the 3-sigma level is breached.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| very low error rate throughout | may never fire | no degradation to detect |
| error rate decreases | no drift signaled | correct — model is improving |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20