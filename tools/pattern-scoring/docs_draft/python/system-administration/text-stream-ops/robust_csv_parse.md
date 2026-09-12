# Robust CSV Parse

**File:** `python/system-administration/text-stream-ops/robust_csv_parse.py`
**Sphere:** System Administration — Text Stream Operations
**Status:** PASS-WITH-FLAG (Illia's audit 2026-07-19)

---

## What it solves

Real-world CSV is dirty: quotes break, fields span lines, exports truncate. This parses a CSV line (or file) with **detection instead of guessing**: strict mode raises a precise error on malformed quoting; non-strict mode skips broken rows so one bad line doesn't kill a 10k-row import.

**When to use:** You're ingesting CSV from an uncontrolled source (user uploads, third-party exports, legacy systems) and need to distinguish *broken* from *foreign*. The parser handles any language/symbols in fields — Ukrainian, CJK, € — all parse cleanly.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `text` | str (may span physical lines inside quotes) | AURA-E006 (None currently coerced — flagged) |
| `strict` | bool: True = raise on malformed, False = skip (None per row) | — |
| any language/symbols in fields | VALID — text is text (Ukrainian, CJK, €… all parse) | rejecting them would be fake-strictness |

---

## How inputs shape the output

- **`strict` is the temperament knob:** same malformed row → strict raises `Malformed CSV: …` (pipeline stops, you learn immediately) · non-strict returns `None` for that row (pipeline survives, you count the Nones and investigate later). Choose by cost of a stopped pipeline vs cost of a silent gap.
- **Quoting drives everything:** an unclosed `"` makes the rest of the input one dangling field — that's "unexpected end of data". A doubled `""` inside quotes is an escaped quote, not a break.
- **Empty string → `[]`** (no row) — distinct from a row of empty fields (`",," → ['','','']`).

---

## Worked example (real runs, from Illia's session)

```
$ python3 python/system-administration/text-stream-ops/robust_csv_parse.py
✓ robust_csv_parse passed

attack: parse_csv_line("ім'я,\"вік,місто", strict=True)
→ ValueError: Malformed CSV: unexpected end of data        # deliberate, contract-quality ✅

attack: print(parse_csv_line("四十二,42.5,€", strict=True))
→ ['四十二', '42.5', '€']                                    # foreign ≠ malformed ✅
```

**Reading the output:** the strict error names the fault class (malformed CSV), and non-ASCII data parses cleanly — the parser distinguishes *broken* from *foreign*, which is exactly the judgment cheap parsers get wrong.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| unclosed quote, strict=True | `ValueError: Malformed CSV: unexpected end of data` — CONTRACT ✅ | the quote never closes; rest of input is one dangling field |
| unclosed quote, strict=False | returns `None` for that row (documented skip) | count your Nones |
| `None` as input | **silently returns `[]`** — io.StringIO(None) stdlib quirk equates None with `""` — AURA-E006 ⚠ | absence of input ≠ empty input; retrofit: type-check |

---

## Provenance

Machine-VERIFIED (frozen ruler) · Illia's audit 2026-07-19: 3 attacks → strict contract genuine, CJK clean, one silent coercion (E006) → PASS-WITH-FLAG · evidence: `output/manual_audit_2026-07-19.csv`
