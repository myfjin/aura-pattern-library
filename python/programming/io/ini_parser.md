# ini parser

**Language:** Python · **Sphere:** programming · **Category:** Io

## What it does

Simple INI file parser module.

This module provides functionality to parse, manipulate, and write INI files.
It supports typed value retrieval and setting, section management, and default sections.

## Guarantee

When it runs, ini parser guarantees parser.get_int('key2') == 123; abs(parser.get_float('key3') - 45.67) < 1e-12; s1.get_int('count') == 42 (proven by run).

**Checkable constraints:**

- `parser.get('key1') == 'value1'`
- `parser.get_int('key2') == 123`
- `abs(parser.get_float('key3') - 45.67) < 1e-12`
- `parser.get_bool('key4') is True`
- `parser.get('quoted') == 'hello world'`
- `parser.get('single') == 'spaced value'`
- `s1 is not None`
- `s1.get('name') == 'example'`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
