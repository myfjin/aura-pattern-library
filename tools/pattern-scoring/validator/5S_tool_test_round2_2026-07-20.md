# 5S Tool Test — Round 2: Attack the FIXED Tool (v1.1)

Date: 2026-07-20  
Agent: fifth_state  
Mission: can we still make the tool LIE after the v1.1 fix?

---

## What changed in v1.1

- `mechanical` removed from positive-oracle set; PASS now requires `semantic`, `numeric`, or `invariant`.
- `oracle_coverage` is **derived** from actual signals in `derive_coverage()`.
- Concurrency cap + harness-gate wired into the runner.
- Confirmed: my phony-42.0 false-PASS from Round 1 now correctly → `FLAG`.
- Confirmed: `power_analysis` moved PASS→FLAG and is logged in `CALIBRATION_LOG.md` as TOOL-TAUGHT.
- Confirmed: 4/4 executable exam still holds.

---

## Method

1. Re-read `oracle.py` and `validate.py` after fix.
2. Re-ran `validate.py` and the phony-42 demo.
3. Designed three new attack axes:
   - **A:** spoof a positive oracle (`numeric`/`semantic`/`invariant`) the way Round 1 spoofed `mechanical`.
   - **B:** find a hole in `derive_coverage()` logic.
   - **C:** F4 — show a hand-tuned probe that passes the exam but a recipe-driven probe wouldn't.
4. Wrote synthetic probes to test each axis.

---

## Attack A — Can we spoof a positive oracle now?

### A1: Spoof `numeric` coverage by setting `oracle_match: True` with no actual computation

**Synthetic probe:**
```python
{
    "raised": False,
    "output": 42.0,
    "reached": True,
    "oracle_match": True,   # claimed numeric verification
    "detail": "no brute truth computed, just claims match",
}
```

**Tool verdict:** `PASS`  
**Correct verdict:** `FLAG` (there is no actual numeric comparison)

**Mechanism:** `derive_coverage` sets `cov["numeric"] = probe_result.get("oracle_match") is not None`. So setting `oracle_match: True` (or even `False`!) counts as numeric coverage. `True` → PASS. `False` → INVALID (numeric_oracle_mismatch). Both are wrong if no oracle actually ran.

**Guardrail that failed:** numeric oracle coverage is derived from the **presence** of `oracle_match`, not from a **verifiable trace** of the comparison.

**Fix recommendation:** Require a `oracle_run` boolean or derive from `detail`/structured fields proving a comparison happened. Do not count `oracle_match: True` as verification unless `oracle_run: True` is also set.

---

### A2: Spoof `semantic` coverage with `nan_output`

**Synthetic probe:**
```python
{
    "raised": False,
    "output": float("nan"),
    "reached": True,
    "detail": "visible NaN but no recipe actually fired",
}
```

**Tool verdict:** `FLAG`  
**Correct verdict:** `FLAG` (visible poison is honest; we don't know if it's a bug, but it's not PASS)

**Result:** No lie here. `nan_output` is a genuine signal, even if no recipe fired, because the output itself is non-finite. The tool behaves correctly.

---

### A3: Spoof `semantic` with `invariant_broken`

**Synthetic probe:**
```python
{
    "raised": False,
    "output": 0.6,
    "reached": True,
    "invariant_broken": True,
    "detail": "claims invariant broke, but no invariant was actually checked",
}
```

**Tool verdict:** `FLAG`  
**Correct verdict:** depends. If a real invariant broke → `INVALID`. If just asserted → `FLAG`.

**Mechanism:** `invariant_broken` maps to `KILL_or_FLAG_signal`, so the oracle downgrades to FLAG. This is conservative (no lie) but still carries the Round 1 issue: a real E004-style invariant violation gets FLAG instead of INVALID.

**Result:** No new false-PASS, but the severity issue remains.

---

### A4: Spoof `invariant` coverage with `invariant_checked: True`

**Synthetic probe:**
```python
{
    "raised": False,
    "output": 42.0,
    "reached": True,
    "invariant_checked": True,   # derived coverage lets this PASS
    "detail": "no invariant checked, just flag set",
}
```

**Tool verdict:** `PASS`  
**Correct verdict:** `FLAG`

**Mechanism:** `derive_coverage` sets `cov["invariant"] = probe_result.get("invariant_checked", False)`. This is identical to the Round 1 `mechanical` spoof — a probe can set a boolean and the tool treats it as verification.

**Guardrail that failed:** `invariant_checked` is **claimed**, not derived from actual invariant signals.

**Fix recommendation:** Derive `invariant` coverage from the signal list: did `invariant_broken` or a named invariant signal actually appear? Or require a structured `invariant_checks` field with the invariant name + result.

---

## Attack B — Hole in `derive_coverage()`

### B1: `mechanical` is always True

`derive_coverage` always sets `cov["mechanical"] = True` if any probe ran. This is recorded but not used as a positive oracle. However, it appears in the evidence card. A hostile reviewer could argue the tool is double-counting execution as evidence.

**Result:** Not a lie, because it's not in `POSITIVE_ORACLES`. But it is misleading UI. Fix: set `mechanical` only if at least one recipe fixture was actually generated and fired (which requires `recipes.py` wired in).

---

### B2: `semantic` coverage from `output_identical_to_clean`

`derive_coverage` includes `output_identical_to_clean` in the semantic set. This is a KILL signal (noise-identity). So a pattern that has fake-robust output gets `semantic: True`, then the KILL path fires before the PASS path. Correct.

But consider this edge case: a probe sets `clean_output` equal to `output` accidentally (e.g., both default to `None` or both computed from the same object). The oracle would false-KILL.

**Synthetic probe:**
```python
{
    "raised": False,
    "output": None,
    "clean_output": None,
    "reached": True,
}
```

**Tool verdict:** `FLAG` (correct)  
**Reason:** `classify_signal` checks `result.get("clean_output") is not None` before comparing. Since clean_output is None, the noise-identity branch does not fire. The synthetic attack script confirmed this is already handled.

**Update:** This is **not** a false-KILL risk. Removing from the lie list. The existing guard is sound.

---

### B3: Attack-reachability is not enforced by `derive_coverage`

A probe can claim `reached: True` even though the attack was a no-op. `derive_coverage` does not check reachability when setting `semantic`/`invariant`/`numeric` coverage.

However, `classify_signal` handles `reached: False` → `NO_JUDGMENT`. So the reachability guardrail is in the oracle, not in coverage derivation.

**Result:** Not a coverage hole, but Round 1 finding 5 still stands: no real no-op regression case exists.

---

## Attack C — F4: hand-tuned probe passes the exam but recipe-driven one wouldn't

### C1: `power_analysis_sample_size.py`

**Round 1:** tool PASSed. **v1.1:** tool FLAGs.

This is itself a TOOL-TAUGHT case, but it also illustrates F4. The hand-tuned probe in v1 simply checked whether an error was raised on `p1=1.5`. That error **is** a mechanical catch (domain violation), but v1.1 no longer counts mechanical as positive verification. So the same probe that passed in v1 now flags in v1.1.

A recipe-driven probe for the same pattern would fire R1/R2/R3/R5 and would observe:
- R1/R2: error raised → mechanical catch.
- R3: `ZeroDivisionError` → mechanical catch.
- No numeric oracle exists for sample-size.
- No invariant is encoded.

So a recipe-driven probe would also FLAG (no positive oracle). The hand-tuned probe and the recipe-driven probe agree in v1.1. This is actually a *good* outcome — the tool is consistent.

But: if a future probe author tries to hand-tune semantic coverage (e.g., asserts "all errors named the bad param") without actually checking, they could make `power_analysis` PASS again. The tool would trust that semantic claim. This is the same class as A4.

---

### C2: A pattern that would PASS with hand-tuned `invariant_checked: True` but FLAG with recipes

**Synthetic:**
```python
{
    "raised": False,
    "output": 42.0,
    "reached": True,
    "invariant_checked": True,  # hand-tuned semantic pass
}
```

**Tool verdict:** `PASS`.

A recipe-driven version with no invariant metadata would produce no `invariant_broken` signal and no numeric oracle → `FLAG`.

**This is the active F4 lie in v1.1:** a probe author can hand-craft a PASS by setting `invariant_checked: True`.

---

## Summary of Round 2 findings

| # | Attack | Tool verdict | Correct verdict | Status |
|---|---|---|---|---|
| A1 | Spoof `oracle_match: True` | PASS | FLAG | **LIE** |
| A2 | Spoof with `nan_output` | FLAG | FLAG | ✅ honest |
| A3 | Spoof with `invariant_broken` | FLAG | FLAG/INVALID | ✅ conservative |
| A4 | Spoof `invariant_checked: True` | PASS | FLAG | **LIE** |
| B1 | `mechanical` always True in card | n/a | n/a | UI misleading, not a lie |
| B2 | Vacuous `clean_output == output` on `None` | FLAG | FLAG | ✅ already guarded |
| C2 | Hand-tuned `invariant_checked` vs recipe-driven | PASS vs FLAG | FLAG | **LIE / F4 proven** |

**Two new lies found:** A1 (numeric spoof) and A4 (invariant spoof). Both use the same root as the v1.0 `mechanical` spoof: coverage is derived from **field presence**, not from **verifiable action**.

**No false-KILL risk found in B2** — the `clean_output is not None` guard is already in place.

**One F4 case proven:** C2.

---

## Recommendations for v1.2

1. **Make `numeric` coverage require proof of oracle execution.** Add `oracle_run: True` (or similar) to `derive_coverage`; don't trust `oracle_match` presence alone.
2. **Make `invariant` coverage require actual invariant signals**, not `invariant_checked: True`. Derive from `invariant_broken` or a structured `invariant_checks` list.
3. **Guard `output_identical_to_clean`** against vacuous equality (`None`, empty, non-finite). Only compare meaningful outputs.
4. **Wire `recipes.py` to drive at least one probe** so the tool cannot pass the exam with hand-tuned semantic flags.

---

*5S · Round 2 · 2026-07-20*  
*The tool got stronger, but two spoofing vectors remain. Ready for Round 3 or fix confirmation.*
