# chunked reader

**Language:** Python · **Sphere:** programming · **Category:** Io

**Signature:** `(filename: str, num_lines: int) → None`

## What it does

Line-delimited file parser with chunked reads.

This module provides classes for efficiently reading and parsing large files
by reading them in chunks and processing line by line, handling partial lines
across chunk boundaries correctly.

## Guarantee

When it runs, chunked reader guarantees got == truth; len(got) == 1000; got == ['first', 'second', 'last-without-newline'] (proven by run).

**Checkable constraints:**

- `got == truth`
- `len(got) == 1000`
- `got == ['first', 'second', 'last-without-newline']`
- `got == ['', '', long_line, 'end']`
- `len(got[2]) == 10000`
- `got == ['a', 'bb', 'ccc']`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
