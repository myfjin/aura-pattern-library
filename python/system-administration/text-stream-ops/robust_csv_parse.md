# robust csv parse

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 16 · Text/stream processing for ops

**Signature:** `(text: str, strict: bool) → ?`

## What it does

robust_csv_parse: Parse CSV with edge cases (quotes, embedded commas, newlines in fields).
THE ONE LAW: Handle real CSV edge cases, reject genuinely broken rows with precise errors.

## Guarantee

When it runs, robust csv parse guarantees parse_csv_line(lines[0]) == ['name', 'age', 'address']; alice == ['alice', '30', '123 Main St, Apt 4']; parse_csv_line(lines[2]) == ['bob', '25', '456 Oak Ave'] (weak-grade: directional, proven by run).

**Checkable constraints:**

- `parse_csv_line(lines[0]) == ['name', 'age', 'address']`
- `alice == ['alice', '30', '123 Main St, Apt 4']`
- `parse_csv_line(lines[2]) == ['bob', '25', '456 Oak Ave']`
- `'Malformed CSV' in str(e)`
- `'expected after' in str(e)`
- `parse_csv_line(malformed, strict=False) is None`
- `'Malformed CSV' in str(e)`
- `parse_csv_line(multiline, strict=True) == ['name', 'address\nline2']`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **hard** — positive (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
