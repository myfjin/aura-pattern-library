# ansi strip

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 16 · Text/stream processing for ops

**Signature:** `(text: str) → ?`

## What it does

ansi_strip: Strip ANSI escape codes from text (colors, bold, etc.).
THE ONE LAW: Remove all escape sequences, assert exact output.

## Guarantee

When it runs, ansi strip guarantees exact_stripped == 'Hello World'; '\x1b' not in stripped; 'Red text' in stripped (proven by run).

**Checkable constraints:**

- `'\x1b' not in stripped`
- `'Red text' in stripped`
- `'Green text' in stripped`
- `stripped == 'Red text Green text'`
- `'\x1b' in broken`
- `'\x1b' not in stripped`
- `bold_stripped == 'Bold Red'`
- `underlined_stripped == 'Underlined'`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
